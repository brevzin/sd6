#!/usr/bin/env python3

import pathlib

print(
"""\
css: {datadir}/pandoc.css
filters: [{datadir}/pandoc.py]

template: {datadir}/template

metadata:
  highlighting:
    inline-code: cpp\
""".format(datadir=pathlib.Path(__file__).parent.resolve()))
