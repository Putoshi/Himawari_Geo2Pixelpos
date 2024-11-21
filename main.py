from himawari_geo2pixelpos import calculate_pixel_position

# 東京
# latitude = 35.689
# longitude = 139.692

# オーストラリアのてっぺん
# latitude = -10.692867
# longitude = 142.530188

# オーストラリアの西の端っこ
latitude = -21.801289
longitude = 114.157932


image_width = 11000

pixel_x, pixel_y = calculate_pixel_position(latitude, longitude, image_width)
print(f"Pixel Position: Left = {pixel_x}, Top = {pixel_y}")