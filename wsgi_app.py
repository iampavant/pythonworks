from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def student_application(environ, start_response):

    # Get requested path
    path = environ.get("PATH_INFO", "/")

    # Get query-string parameters
    query = parse_qs(
        environ.get("QUERY_STRING", "")
    )

    if path == "/":

        status = "200 OK"

        content = """
        <html>
        <body>
            <h1>Student Information System</h1>

            <p>
            Try:
            /student?name=Ravi&course=MCA
            </p>
        </body>
        </html>
        """

    elif path == "/student":

        name = query.get(
            "name", ["Unknown"]
        )[0]

        course = query.get(
            "course", ["Not Specified"]
        )[0]

        status = "200 OK"

        content = f"""
        <html>
        <body>

            <h1>Student Details</h1>

            <p>
                <b>Name:</b> {name}
            </p>

            <p>
                <b>Course:</b> {course}
            </p>

            <p>
                <b>Status:</b> Active
            </p>

        </body>
        </html>
        """

    else:

        status = "404 Not Found"

        content = """
        <h1>404</h1>
        <p>Page Not Found</p>
        """

    headers = [
        ("Content-Type", "text/html")
    ]

    start_response(
        status,
        headers
    )

    return [
        content.encode("utf-8")
    ]


if __name__ == "__main__":

    with make_server(
        "127.0.0.1",
        8000,
        student_application
    ) as server:

        print(
            "WSGI Server running at "
            "http://127.0.0.1:8000"
        )

        server.serve_forever()
