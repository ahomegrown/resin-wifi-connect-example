#!/usr/bin/env python

import subprocess
import dothat.backlight as backlight
import dothat.lcd as lcd


def main():
    # Get the current SSID
    SSID = None
    try:
        SSID = subprocess.check_output(["iwgetid", "-r"]).strip()
    except subprocess.CalledProcessError:
        # If there is no connection subprocess throws a 'CalledProcessError'
        pass

if __name__ == "__main__":
    main()
