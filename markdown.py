#!/bin/python3

#> Imports
import re
import typing
from inspect import cleandoc
#</Imports

#> Header >/
def preprocess(text: str):
    '''
        Cleans text to prepare it to be converted to markdown
            Currently just runs inspect.cleandoc(text)
    '''
    return cleandoc(text)

# Headers
def header(line: str, level: int = 0):
    '''
        Generates a markdown header from a preprocessed line
        Level of header is equal to the `level` variable, for example:
            header('Top-level', 0) -> '# Top-level'
            header('Second-level', 1) -> '# Second-level'
            ...etc.
    '''
    assert '\n' not in line, 'Headers should not have multiple lines!'
    return f'#{"#"*level} {line}'
_header_link_remove = re.compile(r'[^\w\-]')
def header_link(line: str, label: str | None = None, *,
                process: typing.Callable[[str], str] = lambda t: _header_link_remove.sub('', t.replace(' ', '-')).lower(), bare: bool = False):
    '''
        Returns an anchor ("#") link to a header (or a preprocessed line that would become a header)
            The text first has leading '#' and ' ' removed if it starts with a '#'
            Then it is processed with the "process" function, which by default:
                1) replaces ' ' with '-'
                2) removes anything matching the pattern [^\w\-]
                3) converts the text to lowercase
        If label is None, then it is set to the contents of line (with the same stripping of '#' and ' ')
        If bare is truthy, then a label is not added and the link is returned as-is
    '''
    if line.startswith('#'): line = line.lstrip('# ')
    assert '\n' not in line, 'Header should not have multiple lines!'
    if bare: return process(line)
    assert (label is None) or ('\n' not in label), 'Label should not have multiple lines!'
    return link(process(line), line if label is None else label)
header.link = header # OO-like alias

# Links
def link(target: str, label: str | None = None):
    '''Generates a link. If label is not provided, it is set to target'''
    assert '\n' not in target, 'Target should not have multiple lines!'
    assert '\n' not in label, 'Label should not have multiple lines!'
    return f'[{target if label is None else label}]({target})'
