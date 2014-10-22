# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SVG2ColoR
                                 A QGIS plugin
 Generates color-ramp styles from SVG files.  It also compatible with CPT-CITY styles.
 SVG2ColoR improves your color-ramp library, by the way your maps look better.
                              -------------------
        begin                : 2014-10-17
		version				 : 0.9
        copyright            : (C) 2014 by Mehmet Selim BILGIN
        email                : mselimbilgin@yahoo.com
		web					 : http://cbsuygulama.wordpress.com/svg2color
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load SVG2ColoR class from file SVG2ColoR
    from svg2color import SVG2ColoR
    return SVG2ColoR(iface)
