import io

from flask import request, send_file

from helpers import error

from lib.generate_pdf import generate_pdf

@app.route("/")
def index():
    return "html-to-pdf service alive and kicking!"


@app.route("/generate", methods=["POST"])
def generate_pdf_from_html():
    mimetype = request.mimetype

    html_string = None
    if mimetype == 'text/html':
        html_string = request.get_data()
    elif mimetype == 'multipart/form-data':
        if "file" not in request.files:
            return error(
                "multipart/form-data MIME type was provided but no 'file' " \
                "entry was provided. The 'file' entry should contain the " \
                "uploaded file.",
                400
            )

        html_file = request.files["file"]
        if html_file.filename != '':
            html_string = html_file.read()
        else:
            return error(
                "multipart/form-data MIME type was provided but the 'file' " \
                "entry was empty.",
                400
            )

    if html_string is None:
        return error(
            f"Provided MIME type ({mimetype}) is not supported. Either " \
            "upload a file (using multipart/form-data) or send HTML content.",
            415
        )

    pdf_bytes = generate_pdf(html_string)
    return send_file(
        io.BytesIO(pdf_bytes),
        download_name='rendered.pdf',
        mimetype='application/pdf'
    )
