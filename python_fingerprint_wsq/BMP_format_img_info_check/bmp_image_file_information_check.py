import struct

def read_bmp_header(file_path):
    with open(file_path, 'rb') as bmp_file:
        # Read the BMP file header (14 bytes)
        header = bmp_file.read(14)

        # Unpack the header data
        # Format: <little-endian, 2s (signature), I (file size), I (reserved), I (offset to pixel data)
        signature, file_size, reserved, offset = struct.unpack('<2sIII', header)

        # Check if the file is a BMP file
        if signature != b'BM':
            raise ValueError("Not a valid BMP file")

        # Read the DIB header (Information header)
        dib_header_size = struct.unpack('<I', bmp_file.read(4))[0]

        # Depending on the DIB header size, read the appropriate number of bytes
        dib_header = bmp_file.read(dib_header_size - 4)

        # Unpack the DIB header data
        if dib_header_size == 40:  # BITMAPINFOHEADER
            width, height, planes, bit_count, compression, image_size, x_pixels_per_meter, y_pixels_per_meter, colors_used, important_colors = struct.unpack('<IIHHIIIIII', dib_header)
        elif dib_header_size == 108:  # BITMAPV4HEADER
            width, height, planes, bit_count, compression, image_size, x_pixels_per_meter, y_pixels_per_meter, colors_used, important_colors, red_mask, green_mask, blue_mask, alpha_mask, cs_type, endpoints, gamma_red, gamma_green, gamma_blue = struct.unpack('<IIHHIIIIIIIIIIIIIII', dib_header)
        elif dib_header_size == 124:  # BITMAPV5HEADER
            width, height, planes, bit_count, compression, image_size, x_pixels_per_meter, y_pixels_per_meter, colors_used, important_colors, red_mask, green_mask, blue_mask, alpha_mask, cs_type, endpoints, gamma_red, gamma_green, gamma_blue, intent, profile_data, profile_size, reserved = struct.unpack('<IIHHIIIIIIIIIIIIIIIIIIII', dib_header)
        else:
            raise ValueError("Unsupported DIB header size")

        return {
            'signature': signature,
            'file_size': file_size,
            'reserved': reserved,
            'offset': offset,
            'dib_header_size': dib_header_size,
            'width': width,
            'height': height,
            'planes': planes,
            'bit_count': bit_count,
            'compression': compression,
            'image_size': image_size,
            'x_pixels_per_meter': x_pixels_per_meter,
            'y_pixels_per_meter': y_pixels_per_meter,
            'colors_used': colors_used,
            'important_colors': important_colors
        }

# Example usage
file_path = './dataset/3__M_Left_index_finger.BMP'
bmp_info = read_bmp_header(file_path)
print("BMP File Information:")
for key, value in bmp_info.items():
    print(f"{key}: {value}")

