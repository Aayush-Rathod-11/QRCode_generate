from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    qr_image = None
    text_value = ''
    error = None

    if request.method == 'POST':
        text_value = request.form.get('text', '').strip()

        if not text_value:
            error = "Please enter some text or a URL first."
        else:
            # Build the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
            )
            qr.add_data(text_value)
            qr.make(fit=True)
            img = qr.make_image(fill_color="#1e1b4b", back_color="#ffffff")

            # Keep it in memory only — no leftover .png files on disk
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            qr_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render_template(
        'index.html',
        qr_image=qr_image,
        text_value=text_value,
        error=error,
    )


if __name__ == '__main__':
    app.run(debug=True)
