def which_type(el):
    """ This function is needed to control which arguments are passed further. """
    if type(el) is str:                       # 3rd line
        return('The string has been given.')    # 4th line
    else:                                       # 5th line
        return('Another type has been given.')
