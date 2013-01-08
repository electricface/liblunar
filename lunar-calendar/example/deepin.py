#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2013 Deepin, Inc.
#               2013 Zhai Xiang
# 
# Author:     Zhai Xiang <zhaixiang@linuxdeepin.com>
# Maintainer: Zhai Xiang <zhaixiang@linuxdeepin.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

try:
    from dtk.ui.init_skin import init_skin
    from dtk.ui.utils import get_parent_dir
except ImportError:
    print "=============Please Install Deepin UI============="
    print "git clone git@github.com:linuxdeepin/deepin-ui.git"
    print "=================================================="

import os

app_theme = init_skin(
    "deepin-ui-demo", 
    "1.0",
    "01",
    os.path.join(get_parent_dir(__file__), "skin"),
    os.path.join(get_parent_dir(__file__), "app_theme"),
    )

from dtk.ui.application import Application
from dtk.ui.constant import DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT
import gtk
import deepin_lunar

if __name__ == "__main__":
    # Init application.
    application = Application()

    # Set application default size.
    application.set_default_size(DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)

    # Set application icon.
    application.set_icon(app_theme.get_pixbuf("icon.ico"))
    
    # Set application preview pixbuf.
    application.set_skin_preview(app_theme.get_pixbuf("frame.png"))
    
    # Add titlebar.
    application.add_titlebar(
        ["theme", "max", "min", "close"], 
        app_theme.get_pixbuf("logo.png"), 
        "LunarCalendar demo",
        "LunarCalendar demo",
        )
    
    # Add Scalebar.
    deepin_lunar_obj = deepin_lunar.new()
    align = gtk.Alignment()
    align.set(0.5, 0.5, 1, 1)
    align.set_padding(0, 2, 2, 2)
    align.add(deepin_lunar_obj)
    
    application.main_box.pack_start(align)

    application.run()
