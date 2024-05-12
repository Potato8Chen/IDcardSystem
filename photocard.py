from PIL import Image, ImageDraw, ImageFont

def generate_business_card(name,gender,position,email,number):
    # 创建一张白色背景的画布
    width, height = 600, 400
    background_color = (255, 255, 255)  # 白色
    background_image = Image.open("cardbackground.png")
    image = Image.new("RGB", (width, height), background_color)
    image.paste(background_image, (0, 0))
    draw = ImageDraw.Draw(image)

    # 添加文本内容
    text_color = (0, 0, 0)  # 黑色
    font_size = 30
    font = ImageFont.truetype("simsun.ttc", font_size)
    text_content = [
        f"姓名: {name}",
        f"性别: {gender}",
        f"电话: {number}",
        "公司: XXXXXX公司",
        f"部门: {position}",
        f"邮箱: {email}",

    ]
    x_offset = 50
    y_offset = 50
    line_height = 40
    for line in text_content:
        draw.text((x_offset, y_offset), line, fill=text_color, font=font)
        y_offset += line_height

    # 保存生成的电子名片
    file_name = f"{name}_{position}_名片.png"
    image.save(file_name)
    return file_name

# 调用函数并生成名片
#file_name = generate_business_card("小明", "软件工程师")
# print("生成的电子名片文件名为:", file_name)

