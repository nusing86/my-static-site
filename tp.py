from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    image_folder = os.path.join('static', 'images')
    images = [os.path.join(image_folder, image) for image in os.listdir(image_folder) if image.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
