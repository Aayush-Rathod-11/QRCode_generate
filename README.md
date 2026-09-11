# ✨ Text to QR Code Generator

A clean, single-page **Flask** web app that turns any text or URL into a downloadable QR code — instantly, in the browser, with nothing saved to disk.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**🔗 Live demo:** [ar11.pythonanywhere.com](https://ar11.pythonanywhere.com)

---

## 📖 About

Paste in a link, message, or any plain text and get a scannable QR code back in one click — no signup, no ads, no files left behind on the server. The QR code is generated in memory and streamed to the page as a Base64 image, then offered as a one-click PNG download.

## 🚀 Features

- 🔤 **Any text or URL** — convert links, messages, contact info, Wi-Fi strings, anything
- ⚡ **Instant generation** — no page reloads beyond the single form submit
- 🖼️ **In-memory rendering** — QR codes are built with Pillow and never saved as loose `.png` files on the server
- ⬇️ **One-click download** — grab the generated code as a PNG straight from the page
- 🎨 **Polished UI** — a responsive, gradient two-panel layout with live validation messaging
- 🛡️ **Input validation** — friendly error message if the text field is submitted empty

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Backend | [Flask](https://flask.palletsprojects.com/) |
| QR generation | [`qrcode`](https://pypi.org/project/qrcode/) |
| Image handling | [Pillow](https://python-pillow.org/) |
| Frontend | HTML5, CSS3 (Google Fonts – Poppins), Jinja2 templating |

## 📁 Project Structure

```
Text_QRcode/
├── app.py                 # Flask app & QR generation logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Main page (form + QR preview)
└── static/
    └── style.css           # Styling for the app
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.9 or higher
- `pip`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Aayush-Rathod-11/Text_QRcode.git
cd Text_QRcode

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser. 🎉

## 🧪 Usage

1. Type or paste any text/URL into the input box.
2. Click **Generate QR Code**.
3. Scan it directly from the screen, or click **Download PNG** to save it.

## 🗺️ Roadmap

- [ ] Custom QR colors from the UI
- [ ] Logo/image embedding in the QR code
- [ ] Support for SVG export
- [ ] Dockerfile for one-command deployment

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](../../issues) or open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

## 🙌 Acknowledgements

- [qrcode](https://pypi.org/project/qrcode/) — Python QR code generation library
- [Flask](https://flask.palletsprojects.com/) — lightweight WSGI web framework
- [Shields.io](https://shields.io/) — badges used in this README

---

<p align="center">Made with 💜 using Flask + qrcode</p>