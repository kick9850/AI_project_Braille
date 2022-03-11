from PIL import Image

image1 = Image.open('merged_image.jpg')
image1.show()

image2 = Image.open('merged_image1.jpg')
image2.show()
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB', (image2_size[0], 2 * image2_size[1]), (250, 250, 250))
new_image.paste(image1, (0, 0))
new_image.paste(image2, (0, image1_size[1]))
new_image.save("test_image.jpg", "JPEG")
new_image.show()
