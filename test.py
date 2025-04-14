import moondream as md
from PIL import Image
# from secrets import API_KEY

model = md.vl(api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlfaWQiOiI2YWNlZTJjMy0xMjY1LTQ1NzgtOTcyNi03NzI4NjEzY2I2Y2YiLCJvcmdfaWQiOiJlcUVxdE5pRHNralBGV2pSejFhTEZMWEFvdDQxZGRUTiIsImlhdCI6MTc0NDU5NzkzNCwidmVyIjoxfQ.GY7NvQ71m4hFwf7BORuosya7VNDeNs9X3ctYAuubyqk")

image = Image.open("img1.jpg")

caption = model.caption(image)["caption"]

answer = model.query(image, "What is this image?")["answer"]

for chunk in model.caption(image, stream=True, length="short")["caption"]:
    print(chunk, end="", flush=True)