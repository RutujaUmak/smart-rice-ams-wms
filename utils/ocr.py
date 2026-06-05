import easyocr

reader = easyocr.Reader(['en'])

def read_plate(image_path):
    result = reader.readtext(image_path)

    if len(result) > 0:
        return result[0][1]

    return "No Plate Found"