from PIL import Image 
image_file = Image.open("img.png").convert('LA')
image_file.save('greyimg.png')