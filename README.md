# flask

A Flask application is an instance of the Flask class. Everything about the application, such as configuration and URLs will be registered with this class.

The most straightforward way to create a Flask app is to create a global Flask instance directly at the top of your code. This is a simple approach, and while useful, it can cause issues as projects grow.

It is instead better to create a Flask instance inside a function, which is known as the application factory. All configuration, registration and setup the app needs will happen there.