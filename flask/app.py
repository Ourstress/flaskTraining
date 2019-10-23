# import Flask class - notice the caps - by convention, python classes are capitalised
from flask import Flask

# create an instance of Flask class
# instance refers to an individual object of a certain class.
# TLDR: objects are instances of types

# the flask object implements a WSGI application
# An instance of this class will be our WSGI application
# WSGI stands for Web Server Gateway Interface
# WSGI introduced a single calling convention that every web server could implement, thereby making that web server instantly compatible with all of the Python web applications and web frameworks that also support WSGI.
# Flask application gives us a WSGI server that knows howto use HTTP to talk to a web browser and an application written to respond correctly when invoked per the WSGI calling convention

# To initiate an instance, flask expects the name of the module of the application
# The name is important because it is used to resolve resources from inside the package or the folder the module is contained in depending on
# The idea of the first parameter is to give Flask an idea of what belongs to your application. This name is used to find resources on the filesystem and more

# If you are using a single module, __name__ is always the correct value
# Every module in Python has a special attribute called __name__. It is a built-in variable that returns the name of the module.

# application below is just a variable that refers to the Flask instance
application = Flask(__name__)

# create a list of todos
todos = ["buy rice", "feed cat"]

# Route definition is the simple act of assigning URLs to functions containing view logic
# maps URL to action

# route() is a decorator that is used to register a view function for a given URL rule
# A decorator is a way to extend the functionality of a Python function with another function by “wrapping” said function with logic
# The name of our route function is important. It is a best practice to refer to routes by name as opposed to URL. Therefore, a route with a function named home() with henceforth be known as  home, as opposed to “/“
@application.route('/')
def index():
  return str(todos)

# When a module is run as a script, its __name__ is set to __main__
if __name__ == "__main__":
  # run() runs the application on a local development server
  # If the debug flag is set the server will automatically reload for code changes and show a debugger in case an exception happened
	application.run(debug=True)

# SOURCES
# https://hackersandslackers.com/the-art-of-building-flask-routes/
# https://www.phys.hawaii.edu/~idlab/bronson/projects/erle-robotics-python-gitbook-free.pdf