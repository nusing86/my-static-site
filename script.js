const images = ['法师_000001.jpg', '法师_000130.jpg', /* 更多图片文件名 */];
const gallery = document.getElementById('gallery');

images.forEach(image => {
    const img = document.createElement('img');
    img.src = `image/${image}`;
    img.alt = image;
    gallery.appendChild(img);
});
