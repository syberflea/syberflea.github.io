def camel_split(string):
    camel = [string[0].lower()]
    for ch in string[1:]:
        if ch.isupper():
            camel.append("_")
            camel.append(ch)
        else:
            camel[-1].append(ch)
    return [''.join(c) for c in camel]