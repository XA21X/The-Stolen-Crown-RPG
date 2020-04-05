#!/usr/bin/env python
__author__ = 'justinarmstrong'

from threading import Thread

"""This is a fantasy RPG game about a warrior whose
quest is to recover a magic crown"""

import sys
import pygame as pg
from data.main import main

if __name__ == '__main__':
    # Initialise audio system in another thread to fix segfault when first sound effect is played.
    Thread(target=pg.mixer.init).start()

    main()
    pg.quit()
    sys.exit()
