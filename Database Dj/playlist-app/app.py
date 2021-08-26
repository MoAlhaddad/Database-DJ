from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template('playlist.html', playlist=playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:
    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        new_playlist = Playlist(name=name, description=description)
        db.session.add(new_playlist)

        try:
            db.session.commit()
        except IntegrityError as e:
            if 'name' in e.orig.pgerror:
                form.name.errors.append('Playlist name already exists. Please choose another.')
                return render_template('new_playlist.html', form=form)

        return redirect('/playlists')
    
    return render_template('new_playlist.html', form=form)

##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    song = Song.query.get_or_404(song_id)
    return render_template('song.html', song=song)

@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:
    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    form = SongForm()

    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data

        if Song.query.filter(Song.title == title, Song.artist == artist).first():
            form.title.errors.append('A song with that name and artist already exists in the database.')
            return render_template('new_song.html', form=form)

        new_song = Song(title=title, artist=artist)
        db.session.add(new_song)
        db.session.commit()

        return redirect('/songs')

    return render_template('new_song.html', form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    curr_on_playlist = [s.id for s in playlist.songs]
    form.song.choices = (db.session.query(Song.id, Song.title)
                        .filter(Song.id.notin_(curr_on_playlist))
                        .all())

    if form.validate_on_submit():
        song = Song.query.get(form.song.data)
        playlist.songs.append(song)
        db.session.commit()

        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                            playlist=playlist,
                            form=form)