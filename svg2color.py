# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SVG2ColoR
                                 A QGIS plugin
 Generates color-ramp styles from SVG files.  It also compatible with CPT-CITY styles.
 SVG2ColoR improves your color-ramp library, by the way your maps look better.
                              -------------------
        begin                : 2014-06-17
		version				 : 0.7
        copyright            : (C) 2014 by Mehmet Selim BILGIN
        email                : mselimbilgin@yahoo.com
		web					 : http://cbsuygulama.wordpress.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import resources_rc
from svg2colordialog import SVG2ColoRDialog
from PyQt4.QtWebKit import QGraphicsWebView
import os
from xml.dom import minidom
import codecs


class SVG2ColoR:

	def __init__(self, iface):
		self.iface = iface

		self.plugin_dir = os.path.dirname(__file__)

		locale = QSettings().value("locale/userLocale")[0:2]
		localePath = os.path.join(self.plugin_dir, 'i18n', 'svg2color_{}.qm'.format(locale))

		if os.path.exists(localePath):
			self.translator = QTranslator()
			self.translator.load(localePath)

			if qVersion() > '4.3.3':
				QCoreApplication.installTranslator(self.translator)

	def initGui(self):
		self.action = QAction(
			QIcon(":/plugins/svg2color/icon.png"),
			u"SVG2ColoR", self.iface.mainWindow())

		self.action.triggered.connect(self.run)


		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(u"&SVG2ColoR", self.action)

	def unload(self):
		self.iface.removePluginMenu(u"&SVG2ColoR", self.action)
		self.iface.removeToolBarIcon(self.action)

	def browseFile(self):
		##File browsing.
		browseDlg = QFileDialog.getOpenFileName(self.dlg, 'Choose SVG File...', self.dlg.lineEdit.text(), 'SVG file (*.svg)')
		if browseDlg:
			self.dlg.lineEdit.setText(browseDlg)
			try:
				with codecs.open(browseDlg, encoding='utf-8', mode='r') as readFile:
					self.isLinearGrad(readFile.read())
			except Exception as readError:
				QMessageBox.critical(None, "Information", ("An error has occured: " + str(readError)))


	def isLinearGrad(self, svgDocument):
		##Checking SVG document for XML syntax.
		try:
			svgDoc = minidom.parseString(svgDocument)
			self.firstNode = svgDoc.getElementsByTagName('linearGradient')
			#Checking SVG document for containing linearGradient tag.
			if len(self.firstNode) == 0:
				QMessageBox.critical(None, "Information", 'The SVG file does not contain <b>linearGradient</b> tag. Please choose a proper SVG document. You can find lots of samples in <a href="http://soliton.vm.bytemark.co.uk/pub/cpt-city/">CPT-CITY webpage</a>')
				self.graphicRenderer(open(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'error.svg', 'r').read())
				self.dlg.pushButton_2.setEnabled(False)
			else:				
				try:
					self.colorList = list()
					for i in self.firstNode[0].getElementsByTagName('stop'):
						#Some SVG files contain hex values for defining colors. It must be converted to values. This issue is handling in here.
						if i.attributes['stop-color'].value[0] == '#':
							self.colorList.append([self.hexToRgb(i.attributes['stop-color'].value), float(i.attributes['offset'].value[:-1])/100])
						else:
							self.colorList.append([i.attributes['stop-color'].value[4:-1], float(i.attributes['offset'].value[:-1])/100])
					self.sampleSvg(self.firstNode[0])
					self.dlg.pushButton_2.setEnabled(True)
				except Exception as linearGradError:
					QMessageBox.critical(None, "Information", 'Can not read color values. Please choose a proper SVG document. You can find lots of samples in <a href="http://soliton.vm.bytemark.co.uk/pub/cpt-city/">CPT-CITY webpage</a>')
					self.graphicRenderer(open(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'error.svg', 'r').read())
					self.dlg.pushButton_2.setEnabled(False)
					
		except Exception as xmlError:
			QMessageBox.critical(None, "Information", 'The SVG file is not valid (XML syntax error).')
			self.graphicRenderer(open(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'error.svg', 'r').read())
			self.dlg.pushButton_2.setEnabled(False)
			
	def hexToRgb(self, hexademical): #Thanks for dan_waterworth from http://stackoverflow.com/questions/4296249/how-do-i-convert-a-hex-triplet-to-an-rgb-tuple-and-back
		num = str(hexademical[1:])
		#Sometimes hex codes can be shortand (3 digits). Here is the solution...
		if len(num) == 3:
			num = num[:1]*2 + num[1:2]*2 + num[2:3]*2
		
		return (str(int(num[:2], 16)) + ',' + str(int(num[2:4], 16)) + ',' + str(int(num[4:6], 16)))
		

	
	def styleMaker(self, colorList, name):
		##Generating QGIS style XML document.
		#Adding main elements.
		styleDoc = minidom.Document()
		qgisBase = styleDoc.createElement('qgis_style')
		qgisBase.setAttribute('version', '1')
		styleDoc.appendChild(qgisBase)

		symbols = styleDoc.createElement('symbols')
		qgisBase.appendChild(symbols)
		
		colorRamps = styleDoc.createElement('colorramps')
		qgisBase.appendChild(colorRamps)

		colorRamp = styleDoc.createElement('colorramp')
		colorRamp.setAttribute('type', 'gradient')
		colorRamp.setAttribute('name', name)
		colorRamps.appendChild(colorRamp)
		
		#Adding prop elements.
		prop1 = styleDoc.createElement('prop')
		prop1.setAttribute('k', 'color1')
		prop1.setAttribute('v', colorList[0][0])
		colorRamp.appendChild(prop1)

		prop2 = styleDoc.createElement('prop')
		prop2.setAttribute('k', 'color2')
		prop2.setAttribute('v', colorList[-1][0])
		colorRamp.appendChild(prop2)

		prop3 = styleDoc.createElement('prop')
		prop3.setAttribute('k', 'discrete')
		prop3.setAttribute('v', '0')
		colorRamp.appendChild(prop3)
		
		stopList = list()
		for j in colorList[1:-1]:
			stopList.append(str(j[1]) + ';' + j[0])
			
		prop4 = styleDoc.createElement('prop')
		prop4.setAttribute('k', 'stops')
		prop4.setAttribute('v', ':'.join(stopList))
		colorRamp.appendChild(prop4)
		return (styleDoc.toprettyxml(indent="    ", encoding="utf-8"))
		
		
	def sampleSvg(self, linearGradientTag):
		##Generating sample SVG document for visualisation.
		sampleSVG = minidom.Document()
		svgBase = sampleSVG.createElement('svg')
		svgBase.setAttribute('xmlns', 'http://www.w3.org/2000/svg')
		svgBase.setAttribute('version', '1.1')
		svgBase.setAttribute('width', '600px')
		svgBase.setAttribute('height', '110px')
		sampleSVG.appendChild(svgBase)
		
		defs = sampleSVG.createElement('defs')
		svgBase.appendChild(defs)		
		defs.appendChild(linearGradientTag)
		
		rectangle = sampleSVG.createElement('rect')
		rectangle.setAttribute('x', '1')
		rectangle.setAttribute('y', '1')
		rectangle.setAttribute('width', '493')
		rectangle.setAttribute('height', '93')
		rectangle.setAttribute('stroke-width', '1')
		rectangle.setAttribute('stroke', 'black')
		rectangle.setAttribute('fill', 'url(#' + linearGradientTag.attributes['id'].value + ')')
		svgBase.appendChild(rectangle)
		self.graphicRenderer(sampleSVG.toprettyxml(indent="    ", encoding="utf-8"))
		
	def graphicRenderer(self, svgInput):
		#Graphics rendering.
		scene = QGraphicsScene()
		self.dlg.graphicsView.setScene(scene)
		webview = QGraphicsWebView()
		webview.setContent(svgInput, 'image/svg+xml')
		scene.addItem(webview)
		
		
	def saveStyle(self):
		browseDlg = QFileDialog.getSaveFileName(self.dlg, 'Save Style File...', os.path.dirname(self.dlg.lineEdit.text()) + os.sep + os.path.splitext(os.path.basename(self.dlg.lineEdit.text()))[0], 'XML file (*.xml)')
		if browseDlg:
			try:
				with codecs.open(browseDlg, encoding='utf-8', mode='w') as saveFile:
					saveFile.write(self.styleMaker(self.colorList, os.path.splitext(os.path.basename(self.dlg.lineEdit.text()))[0]))
					QMessageBox.information(None, "Information", 'The style file succesfully saved in <b>%s</b>. \nNow you can import it from <b>Settings -> Style Manager</b> menu.' % (saveFile.name))

			except Exception as saveError:
				QMessageBox.critical(None, "Information", ("An error has occured: " + str(saveError)))


	def run(self):
		self.dlg = SVG2ColoRDialog()
		self.dlg.pushButton.clicked.connect(self.browseFile)
		self.dlg.pushButton_2.clicked.connect(self.saveStyle)
		self.graphicRenderer(open(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'opening.svg', 'r').read())
		self.dlg.exec_()

