#!/usr/bin/env python3

ESCAPE = "\033"

RESET = "[0m"

RED = "[31m"
GREEN = "[32m"
YELLOW = "[33m"
BLUE = "[34m"

def paint(color, text, end = "\n"):
    print(ESCAPE + color + text + ESCAPE + RESET, end = end)
