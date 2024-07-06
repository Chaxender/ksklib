from PIL import Image, ImageFilter

def apply_filter(image_path, filter_type):
    image = Image.open(image_path)
    if filter_type == "BLUR":
        filtered_image = image.filter(ImageFilter.BLUR)
    elif filter_type == "CONTOUR":
        filtered_image = image.filter(ImageFilter.CONTOUR)
    elif filter_type == "DETAIL":
        filtered_image = image.filter(ImageFilter.DETAIL)
    elif filter_type == "EDGE_ENHANCE":
        filtered_image = image.filter(ImageFilter.EDGE_ENHANCE)
    else:
        filtered_image = image
    return filtered_image

image_path = input("Filtre uygulamak istediğiniz resmin yolunu girin: ")
filter_type = input("Uygulamak istediğiniz filtreyi girin (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE): ")
filtered_image = apply_filter(image_path, filter_type)
filtered_image.show()
