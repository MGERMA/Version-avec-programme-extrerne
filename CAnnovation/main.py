# -*- coding: utf-8-*- 

#import direct.directbase.DirectStart 
from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject 
from panda3d.core import *
from direct.task import Task

from modCAO import * # Import du module de connexion

# a bit of qts
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 

#world object management
from src.scenemanager.ObjectManager import ObjectManager

#camera management
from src.camera.CameraManager import CameraManager

#gui imports
from src.gui.QTTest import QTTest
from src.gui.GuiManager import GuiManager
from src.gui.SceneGraphBrowser import SceneGraphBrowser

#input management
from src.input.InputHandler import InputHandler
from src.input.EventHandler import EventHandler

#third party tools management
from src.thirdparty.ThirdPartyToolsManager import ThirdPartyToolsManager

import sys,__builtin__

from pandac.PandaModules import loadPrcFileData 


loadPrcFileData("", """
text-encoding utf8
show-frame-rate-meter 1
sync-video #f
""")

configsocket=param() # Demande des identifiants de connexion

class World(ShowBase):	
	def __init__(self):
		ShowBase.__init__(self)
		#starting all base methods
		__builtin__.myApp = self
		__builtin__.myObjectManager = ObjectManager()
		__builtin__.myGui = GuiManager()
		__builtin__.myCamera = CameraManager()
		__builtin__.myInputHandler = InputHandler()
		__builtin__.myEventHandler = EventHandler()
		__builtin__.myThirdPartyTools = ThirdPartyToolsManager()
		
		#default config when just opened
		myCamera.mm.showMouse()
		myCamera.setUtilsActive()
		self.defineBaseEvents()
		
		self.mainScene = render.attachNewNode("mainScene")
	
	def pandaCallback(self):
		taskMgr.step()
	
	def getSceneNode(self):
		return self.mainScene
	
	def exportScene(self):
		s.refresh()
		
	def defineBaseEvents(self):
		base.accept("escape", sys.exit)
		

w = World()

app = QApplication(sys.argv)

# panneau parametres
q = QTTest(w.pandaCallback)
q.show()

# panneau browser
s = SceneGraphBrowser()
s.show()

app.exec_()
w.run() # Demarrage du moteur avec les parametres demandees.
