from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import zipfile, io, os

app = Flask(__name__)

# ================== HOME PAGE ==================
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# ================== CARD VIEW PAGE ==================
@app.route("/card/<card_id>")
def open_card(card_id):
    name = request.args.get("name")

    if not name:
        return "Name missing in URL. Go back and enter your name!"

    # Select card page
    if card_id == "card1":
        return render_template("card1.html", name=name)  # Christmas

    elif card_id == "card2":
        return render_template("card2.html", name=name)  # New Year

    elif card_id == "card3":
        return render_template("card3.html", name=name)  # Combo card (future)

    else:
        return "Card not found"


# ================== DOWNLOAD CARD ==================
@app.route('/download')
def download_card():
    name = request.args.get("name")
    theme = request.args.get("theme")  # card1/card2/card3

    if not name or not theme:
        return "Missing name or theme!"

    # Background image
    bg_path = f"static/cards/{theme}.png"
    img = Image.open(bg_path)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("static/fonts/Christmas.ttf", 80)
    text = f"Merry Christmas {name}!"

    W, H = img.size
    w, h = draw.textsize(text, font=font)
    draw.text(((W-w)/2, H/2), text, (255,255,255), font=font)

    # Save image
    output_img = f"card_{name}.png"
    img.save(output_img)

    # Create ZIP (card + music)
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zipf:
        zipf.write(output_img)
        zipf.write("static/music/christmas.mp3")

    zip_buffer.seek(0)
    os.remove(output_img)

    return send_file(
        zip_buffer,
        as_attachment=True,
        download_name=f"{name}_ChristmasCard.zip",
        mimetype="zip"
    )


# ================== RUN SERVER ==================
if __name__ == '__main__':
    app.run(debug=True)
