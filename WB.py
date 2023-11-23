import os
image_folder = 'path/to/your/image/folder'
images = os.listdir(image_folder)

with open('index.html', 'w') as file:
    file.write('<html><body>\n')
    for image in images:
        file.write(f'<img src="{image_folder}/{image}" alt="{image}">\n')
    file.write('</body></html>')
