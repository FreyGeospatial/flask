# flask

A Flask application is an instance of the Flask class. Everything about the application, such as configuration and URLs will be registered with this class.

The most straightforward way to create a Flask app is to create a global Flask instance directly at the top of your code. This is a simple approach, and while useful, it can cause issues as projects grow.

It is instead better to create a Flask instance inside a function, which is known as the application factory. All configuration, registration and setup the app needs will happen there.

## how to run app/api:
`flask --app flaskr run --debug`

If you load http://127.0.0.1:5000/hello in a web browser, you will get the text or html returned by the application, as well as a the print statement in the console.

If you run `curl http://127.0.0.1:5000/hello`, anything that is returned by the app will be returned by the API.