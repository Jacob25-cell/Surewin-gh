import os
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "surewin-gh-secret-key-2025")

@app.route('/')
def index():
    """Homepage with free daily predictions"""
    return render_template('index.html')

@app.route('/vip')
def vip():
    """VIP tips page with password protection"""
    return render_template('vip.html')

@app.route('/howtopay')
def howtopay():
    """Payment instructions page"""
    return render_template('howtopay.html')

@app.route('/testimonials')
def testimonials():
    """Testimonials page"""
    return render_template('testimonials.html')

@app.route('/contact')
def contact():
    """Contact support page"""
    return render_template('contact.html')

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
