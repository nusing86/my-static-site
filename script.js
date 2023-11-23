const images = ['image1.jpg', 'image2.jpg', /* 更多图片文件名 */];
const gallery = document.getElementById('gallery');

images.forEach(image => {
    const img = document.createElement('img');
    img.src = `image/${image}`;
    img.alt = image;
    gallery.appendChild(img);
});
