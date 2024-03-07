from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
import os
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/descargarVideo', methods=['POST'])
def descargar_video():
    if request.method == 'POST':
        url_video = request.form['urlVideo']
        try:
            yt = YouTube(url_video)
            stream = yt.streams.get_highest_resolution()
            path = Path("Videos")
            folder = "VideosYT"
            url_descargas = str(Path.home() / path)
            stream.download(output_path=os.path.join(url_descargas, folder))
            return redirect(url_for('home'))
        except Exception as e:
            return f"Ocurrió un error al descargar el video: {e}"

if __name__ == '__main__':
    app.run(debug=True)
