from PIL import Image

# 1200x720の画像からステータス領域を切り抜いて返します。
# TODO 失敗した場合はNoneを返します。
def GetStatusView(screenshot):
    if screenshot is None:
        return None
    (w, h) = screenshot.size
    if w != 1200 or h != 720:
        return None
    return screenshot.crop((491, 147, 491 + 690, 147 + 555))

# 690x550の画像のリストを受け取り、並べた画像を生成して返します。
# TODO 失敗した場合はNoneを返します。
def GetOrganizedStatus(images):
    count = len(images)
    if count <= 0:
        return None

    # サイズを計算
    if count == 1:
        width = 1
    elif count <= 7:
        width = 2
    else:
        width = int((count - 1) / 6) * 3
    if count == 7:
        height = 4
    elif count >= 8:
        height = 3
    else:
        height = int((count - 1) / 2) + 1

    result = Image.new("RGB", (width * 690, height * 550))
    i = 0
    for image in images:
        if count == 7 and i == 6:
            x = 0
            y = 3
        else:
            x = (i % 2) + int(i / 6) * 2
            y = int((i % 6) / 2)
        result.paste(image, (x * 690, y * 550))
        i+=1
    
    return result
