#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2026 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2026-04-28
################################################################

from .template_archer_y6 import HexFlowTemplateArcherY6


def main():
    template = HexFlowTemplateArcherY6()
    template.start()
    template.run()


if __name__ == "__main__":
    main()
