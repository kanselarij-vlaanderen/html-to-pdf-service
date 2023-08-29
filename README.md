# HTML to PDF service
A microservice that lets you generate PDF files from HTML content

## Tutorials
### Add the html-to-pdf-service to a stack
Add the following snippet to your `docker-compose.yml` file to include the html-to-pdf service in your project.

```yml
html-to-pdf:
  image: kanselarij/html-to-pdf-service
```

## Reference

### API
#### POST `/generate`

Generate a PDF based on the provided HTML content.

#### Response
##### 200 OK

This endpoint accepts two ways of generating a PDF: you can either send HTML text as the request body or upload a file. In both cases the endpoint will return a `200 OK` response that contains the contents of the generated PDF.
When choosing to upload a file, make sure that the file is sent in the `multipart/form-data` entry called `file`.

**Sending HTML text as the request body via cURL:** `curl -H "Content-Type: text/html" -d "<h1>your html goes here</h1>" http://html-to-pdf/generate`
**Uploading an HTML file via cURL:** `curl -F "file=@/your/html/file/goes/here.html" http://html-to-pdf/generate`

##### 400 Bad Request
When using `multipart/form-data` the HTML file should be provided in the `file` entry. If no such entry is provided, this endpoint will return a `400 Bad Request` response:

```json
{
  "errors": [
    {
      "detail": "multipart/form-data MIME type was provided but no 'file' entry was provided. The 'file' entry should contain the uploaded file.",
      "status": 400
    }
  ]
}
```

If the `file` entry doesn't actually contain a file (e.g. when making this request from an HTML form and no file is selected), this endpoint will return a `400 Bad Request` response:

```json
{
  "errors": [
    {
      "detail": "multipart/form-data MIME type was provided but the 'file' entry was empty.",
      "status": 400
    }
  ]
}
```

##### 415 Unsupported Media Type
This endpoint only supports HTML provided as the request body (sent using content type `text/html`) or as an uploaded file (as a `multipart/form-data` with the file sent with entry name `file`). If a different content type header is provided, this endpoint will return a `415 Unsupported Media Type` response:

```json
{
  "errors": [
    {
      "detail": "Provided MIME type is not supported. Either upload a file (using multipart/form-data) or send HTML content",
      "status": 415
    }
  ]
}
```
