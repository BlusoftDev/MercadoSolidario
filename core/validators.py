from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    
    if filesize > 1048576:
        raise ValidationError("El valor máximo de la foto no puede ser mayor a 1 MB")
    else:
        return value