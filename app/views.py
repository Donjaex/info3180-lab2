import datetime
from app import app
from flask import render_template

###
# Helper function
###

def format_date_joined(date):
    
    return date.strftime("%B, %Y")


###
# Routes
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Render website's about page."""
    return render_template('about.html', name="Donjae Marsh")


@app.route('/profile')
def profile():
    """Render user's profile page."""
    date_joined = datetime.date(2026, 2, 7)
    formatted_date = format_date_joined(date_joined)

    return render_template(
        'profile.html',
        name="Donjae Marsh",
        username="donjae",
        location="Kingston, Jamaica",
        joined=formatted_date,
        bio="Computer Science student interested in web development and AI.",
        posts=7,
        following=100,
        followers=250
    )


###
# Send text files
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send a text file from the static folder."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


###
# App-wide settings
###

@app.after_request
def add_header(response):
    """
    Add headers to prevent caching.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
