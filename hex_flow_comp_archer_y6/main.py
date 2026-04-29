#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2026 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2026-04-28
################################################################

from .comp_archer_y6 import HexFlowCompArcherY6


def main():
    comp = HexFlowCompArcherY6()
    comp.start()
    comp.run()


if __name__ == "__main__":
    main()
