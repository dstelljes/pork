#!/usr/bin/env python3

import console
import time
from datetime import datetime
from getpass import getpass
from splinter import Browser

POKE_BASE = "https://www.facebook.com/pokes"
POKE_WAIT = 5

username = input("Email/phone: ")
password = getpass("Password: ")
agent = input("Preferred browser [chrome]: ") or "chrome"

with Browser(agent) as browser:
    # Get signed in:
    browser.visit(POKE_BASE)
    browser.fill("email", username)
    browser.fill("pass", password)
    browser.find_by_name("login").click()

    if (browser.url == POKE_BASE):
        console.paint(console.GREEN, "Logged in! Poking will commence shortly.", end = "\n\n")
    else:
        console.paint(console.RED, "Login failed!")
        exit(1)

    # Sleep for awhile until the notifications modal goes away:
    time.sleep(3)

    # Do some poking:
    try:
        while True:
            victims = browser.find_by_css("[id^=poke_live_item]")

            for victim in victims:
                name = victim.find_by_css("[data-hovercard]").value
                poker = victim.find_by_css("[role=button].selected")

                if not poker:
                    continue

                console.paint(console.YELLOW, "[%s] " % datetime.now().isoformat(), end = "")
                print("Poked %s!" % name)
                poker.click()

            time.sleep(POKE_WAIT)
    except KeyboardInterrupt:
        print("")
        exit(0)
