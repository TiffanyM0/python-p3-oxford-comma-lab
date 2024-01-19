def oxford_comma(items):
    pass
    if len(items) > 2:
        for i in range(len(items)-1):
            return ", ".join(items)
    return " and ".join(items)