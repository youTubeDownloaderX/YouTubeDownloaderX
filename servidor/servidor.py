from flask import Flask, request

app = Flask(__name__)

@app.route('/descargarVideo', methods=['POST'])
def descargar_video():
    # Tu lógica para descargar el video aquí
    url_video = request.form['urlVideo']
    # Aquí usarías pytube para descargar el video desde la URL proporcionada
    # Ejemplo:
    # from pytube import YouTube
    # yt = YouTube(url_video)
    # yt.streams.get_highest_resolution().download('/ruta/donde/guardar/el/video')
    return 'Video descargado correctamente'

if __name__ == '__main__':
    app.run(debug=True)
