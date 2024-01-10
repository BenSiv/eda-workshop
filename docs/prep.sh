#!/bin/bash

marp presentation.md --output presentation.pdf --allow-local-files
pandoc --from markdown+hard_line_breaks --output transcript.pdf transcript.md