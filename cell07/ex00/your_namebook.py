def array_of_names (name_diet):
    result = []
    for first, last in name_diet. items ():
        full_name = first.capltallze() +" "+ last.capitalized()
        result.append(full_name)
    return result
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "savler": "niel",
    "f1f1": "brindacler"
}

print(array_of_names (persons))