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

# Links
def link(target: str, label: str | None = None):
    '''Generates a link. If label is not provided, it is set to target'''
    assert '\n' not in target, 'Target should not have multiple lines!'
    assert '\n' not in label, 'Label should not have multiple lines!'
    return f'[{target if label is None else label}]({target})'
