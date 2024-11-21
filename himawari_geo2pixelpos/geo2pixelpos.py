import math

def calculate_pixel_position(latitude, longitude, image_width):
    # 定数の設定
    margin = {'top': 0.006, 'right': 0.0045, 'bottom': 0.006, 'left': 0.0045}
    eccentricity_squared = 0.00669438003
    angle_factor = 0.1535
    focal_length = 6.613
    view_angle_rad = 81.3025 / 180.0 * math.pi

    # 緯度経度の変換
    if longitude < 0:
        longitude = 180 + (180 + longitude)

    radian_longitude = ((longitude + 180 - 140.7) % 360.0 - 180.0) / 180.0 * math.pi
    radian_latitude = ((latitude + 90.0) % 180.0 - 90.0) / 180.0 * math.pi

    # 半径の計算
    radius = image_width * (1.0 - margin['right'] - margin['left']) / 2
    n = radius / math.sqrt(1.0 - eccentricity_squared * math.sin(radian_latitude) * math.sin(radian_latitude))

    # 緯度経度の制限
    if radian_longitude < -view_angle_rad:
        radian_longitude = -view_angle_rad
    if radian_longitude > view_angle_rad:
        radian_longitude = view_angle_rad
    if radian_latitude < -view_angle_rad:
        radian_latitude = -view_angle_rad
    if radian_latitude > view_angle_rad:
        radian_latitude = view_angle_rad

    # ピクセル位置の計算
    z = radius * focal_length - (n * math.cos(radian_latitude) * math.cos(radian_longitude))
    pixel_x = n * math.cos(radian_latitude) * math.sin(radian_longitude)
    pixel_y = (n * (1.0 - eccentricity_squared)) * math.sin(radian_latitude)
    pixel_x = image_width / 2 * math.atan(pixel_x / z) / angle_factor
    pixel_y = image_width / 2 * math.atan(pixel_y / z) / angle_factor
    pixel_x += image_width / 2
    pixel_y = image_width / 2 - pixel_y

    return pixel_x, pixel_y