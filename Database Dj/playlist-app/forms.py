"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import Length, InputRequired

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Playlist Name', validators=[Length(min=1), InputRequired()], render_kw={"placeholder": "Playlist Name"})
    description = TextAreaField('Playlist Description', render_kw={"placeholder": "Playlist Description"})

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Song Name', validators=[Length(min=1), InputRequired()], render_kw={"placeholder": "Song Name"})
    artist = StringField('Song Artist', validators=[Length(min=1), InputRequired()], render_kw={"placeholder": "Song Artist"})

class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)