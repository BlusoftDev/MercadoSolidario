from django.core.exceptions import ValidationError

# try:
#     model.full_clean()
# except ValidationError as e:
#     non_field_errors = e.message_dict[NON_FIELD_ERRORS]
#     raise e("El valor máximo de la foto no puede ser mayor a 1 MB")
#     pass


def validate_file_size(value):
    
    filesize = value.size
    
    if filesize > 1048576:
        raise ValidationError("El valor máximo de la foto no puede ser mayor a 1 MB")
    else:
        return value