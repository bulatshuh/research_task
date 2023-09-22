def delete_from_set(setx: set, element_to_delete):
    if element_to_delete in setx:
        setx.remove(element_to_delete)
    return setx


print(delete_from_set({1, 2, 'asd', 'qwe'}, 'qwe'))
