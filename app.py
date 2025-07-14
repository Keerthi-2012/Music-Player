from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path

app = Flask(__name__)

# Use relative path for database
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'playlist.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Song model
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=True)

    def __repr__(self):
        return f'<Song {self.title}>'

# Ensure instance folder exists
Path(os.path.join(basedir, 'instance')).mkdir(exist_ok=True)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_song', methods=['POST'])
def add_song():
    try:
        title = request.form.get('title')
        if not title:
            return "Song title is required", 400
            
        existing = Song.query.filter_by(title=title).first()
        if existing is None:
            new_song = Song(title=title)
            db.session.add(new_song)
            db.session.commit()
        
        # Get the redirect page from form, default to playlist if not specified
        redirect_page = request.form.get('filename', 'playlist')
        return redirect(url_for(redirect_page))
    except Exception as e:
        db.session.rollback()
        return f"An error occurred: {str(e)}", 500

@app.route('/remove_song', methods=['POST'])
def remove_song():
    try:
        title = request.form.get('title')
        if not title:
            return "Song title is required", 400
            
        song = Song.query.filter_by(title=title).first()
        if song:
            db.session.delete(song)
            db.session.commit()
        return redirect(url_for('playlist'))
    except Exception as e:
        db.session.rollback()
        return f"An error occurred: {str(e)}", 500

@app.route('/playlist')
def playlist():
    try:
        songs = Song.query.all()
        return render_template("playlist.html", data=songs)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Artist routes
@app.route('/artists')
def artists():
    return render_template('artist.html')  # Make sure this matches the actual filename
# Album routes (keeping the existing routes)
@app.route('/about')
def about():
    return render_template('about.html')  # Remove 'templates/' prefix

@app.route('/bornpsongs')
def bornpsongs():
    return render_template('bornpsongs.html')

@app.route('/bpal')
def bpal():
    return render_template('bpal.html')

@app.route('/btsal')
def btsal():
    return render_template('btsal.html')

@app.route('/checkmate')
def checkmate():
    return render_template('checkmate.html')

@app.route('/cheshire')
def cheshire():
    return render_template('cheshire.html')

@app.route('/dandwsongs')
def dandwsongs():
    return render_template('dandwsongs.html')

@app.route('/fearless')
def fearless():
    return render_template('fearless.html')

@app.route('/guesswho')
def guesswho():
    return render_template('guesswho.html')

@app.route('/ITZME')
def ITZME():
    return render_template('ITZME.html')

@app.route('/itzyal')
def itzyal():
    return render_template('itzyal.html')

@app.route('/killsongs')
def killsongs():
    return render_template('killsongs.html')

@app.route('/loc')
def loc():
    return render_template('loc.html')

@app.route('/lover')
def lover():
    return render_template('lover.html')

@app.route('/lysongs')
def lysongs():
    return render_template('lysongs.html')

@app.route('/mapsongs')
def mapsongs():
    return render_template('mapsongs.html')

@app.route('/midnights')
def midnights():
    return render_template('midnights.html')

@app.route('/rainsongs')
def rainsongs():
    return render_template('rainsongs.html')

@app.route('/raresongs')
def raresongs():
    return render_template('raresongs.html')

@app.route('/red')
def red():
    return render_template('red.html')

@app.route('/reputation')
def reputation():
    return render_template('reputation.html')

@app.route('/revalacion')
def revalacion():
    return render_template('revalacion.html')

@app.route('/rev')
def rev():
    return render_template('rev.html')

@app.route('/revsongs')
def revsongs():
    return render_template('revsongs.html')

@app.route('/searchpage')
def searchpage():
    return render_template('searchpage.html')

@app.route('/selal')
def selal():
    return render_template('selal.html')

@app.route('/spotlight')
def spotlight():
    return render_template('spotlight.html')

@app.route('/squareonesongs')
def squareonesongs():
    return render_template('squareonesongs.html')

@app.route('/squaresongs')
def squaresongs():
    return render_template('squaresongs.html')

@app.route('/sunsongs')
def sunsongs():
    return render_template('sunsongs.html')

@app.route('/tayloral')
def tayloral():
    return render_template('tayloral.html')

@app.route('/thesongs')
def thesongs():
    return render_template('thesongs.html')

@app.route('/wingssongs')
def wingssongs():
    return render_template('wingssongs.html')

@app.route('/youngsongs')
def youngsongs():
    return render_template('youngsongs.html')

if __name__ == '__main__':
    app.run(debug=True)
