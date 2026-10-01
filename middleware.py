from flask import Flask
import time
app = Flask(__name__)
class RequestMonitorMiddleware:
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        start_time = time.perf_counter()
        method = environ.get("REQUEST_METHOD")
        path = environ.get("PATH_INFO")
        print("\nRequest received")
        print("Method :", method)
        print("Path   :", path)
        def custom_start_response(status, headers, exc_info=None):
            end_time = time.perf_counter()
            execution_time = (end_time - start_time) * 1000
            print("Status :", status)
            print(f"Response Time : {execution_time:.2f} ms")
            headers.append(
                ("X-Response-Time",
                 f"{execution_time:.2f} ms")
            )
            return start_response(
                status,
                headers,
                exc_info
            )
        return self.app(
            environ,
            custom_start_response
        )
app.wsgi_app = RequestMonitorMiddleware(app.wsgi_app)
@app.route("/")
def home():
    return """
    <h1>GITAM Student Portal</h1>
    <p>Welcome to the Student Information System.</p>
    <a href="/courses">
        <button>View Courses</button>
    </a>
    <a href="/results">
            <button>View Courses</button>
        </a>
    """
@app.route("/courses")
def courses():
    return """
    <h1>Available Courses</h1>
    <ul>
        <li>Python Programming</li>
        <li>Machine Learning</li>
        <li>Data Structures</li>
    </ul>
    """
@app.route("/results")
def results():
    return """
    <h1>Student Result</h1>
    <p>Student: Ravi</p>
    <p>Result: PASS</p>
    """


if __name__ == "__main__":
    app.run(debug=True)

