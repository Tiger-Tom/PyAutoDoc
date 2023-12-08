#!/bin/python3

#> Imports
from inspect import cleandoc
#</Imports

#> Header >/
def preprocess(text: str):
    '''
        Cleans text to prepare it to be converted to markdown
            Currently just runs inspect.cleandoc(text)
    '''
    return cleandoc(text)
