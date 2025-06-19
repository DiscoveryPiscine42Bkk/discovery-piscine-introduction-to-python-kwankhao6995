def find_theredheads (family):
    return list(filter(lambda name: family[name] == "red", family))

dupont_family = {
"florian": "red",
"sarrie": "blond",
"virdinie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))