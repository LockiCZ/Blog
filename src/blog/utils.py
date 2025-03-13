

def map_field_labels(form, name_map):
    """
    Map field names in a form to new names.

    Args:
        form (forms.Form): The form to modify.
        name_map (dict): A dictionary mapping old names to new names.

    Returns:
        forms.Form: The modified form.
    """
    for field in form.fields.values():
        if field.label in name_map:
            field.label = name_map[field.label]
    return form
