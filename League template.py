import APIGrabber
import tkinter

class LeagueOfLegends:
    def __init__(self):
        self._window = tkinter.Tk()
        self._getRegion() #starts a chain of functions being called
        self._region = "";
        self._championName = "";
        self._championKey = "";

    def start(self)->None:
        #starts the program
        self._window.mainloop()

        
#helper functions
        
    def _getRegion(self)->None:
        #Displays prompt and region buttons
        self._labelFrame = tkinter.Frame(master = self._window)
        self._labelFrame.grid(row = 0, column = 0, padx = 10, pady = (10, 100), sticky = tkinter.E + tkinter.W)
        label = tkinter.Label(master = self._labelFrame, text = 'Please click on your region.',
                              font = ('Helvetica', 30))
        label.pack()
        
        self._buttonFrame = tkinter.Frame(master = self._window)
        self._buttonFrame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.E + tkinter.W)
        na = tkinter.Button(master = self._buttonFrame, text = 'NA', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("na"))
        euw = tkinter.Button(master = self._buttonFrame, text = 'EUW', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("euw"))
        eune = tkinter.Button(master = self._buttonFrame, text = 'EUNE', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("eune"))
        lan = tkinter.Button(master = self._buttonFrame, text = 'LAN', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("lan"))
        las = tkinter.Button(master = self._buttonFrame, text = 'LAN', font =
                             ('Helvetica', 20), command = lambda : self._setRegion("las"))
        br = tkinter.Button(master = self._buttonFrame, text = 'BR', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("br"))
        oce = tkinter.Button(master = self._buttonFrame, text = 'OCE', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("oce"))
        pbe = tkinter.Button(master = self._buttonFrame, text = 'PBE', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("pbe"))
        tr = tkinter.Button(master = self._buttonFrame, text = 'TR', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("tr"))
        ru = tkinter.Button(master = self._buttonFrame, text = 'RU', font =
                            ('Helvetica', 20), command = lambda :self._setRegion("ru"))
        na.pack(side = 'left')
        euw.pack(side = 'left')
        eune.pack(side = 'left')
        lan.pack(side = 'left')
        las.pack(side = 'left')
        br.pack(side = 'left')
        oce.pack(side = 'left')
        pbe.pack(side = 'left')
        tr.pack(side = 'left')
        ru.pack(side = 'left')
    
    def _getChampion(self)->None:
        self._createAChampionFrame()
        
        
        self._bChampionsFrame = tkinter.Frame(master = self._window)
        self._bChampionsFrame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._cChampionsFrame = tkinter.Frame(master = self._window)
        self._cChampionsFrame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._dChampionsFrame = tkinter.Frame(master = self._window)
        self._dChampionsFrame.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._eChampionsFrame = tkinter.Frame(master = self._window)
        self._eChampionsFrame.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._fChampionsFrame = tkinter.Frame(master = self._window)
        self._fChampionsFrame.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._gChampionsFrame = tkinter.Frame(master = self._window)
        self._gChampionsFrame.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._hChampionsFrame = tkinter.Frame(master = self._window)
        self._hChampionsFrame.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._iChampionsFrame = tkinter.Frame(master = self._window)
        self._iChampionsFrame.grid(row = 8, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._jChampionsFrame = tkinter.Frame(master = self._window)
        self._jChampionsFrame.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._kChampionsFrame = tkinter.Frame(master = self._window)
        self._kChampionsFrame.grid(row = 10, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._lChampionsFrame = tkinter.Frame(master = self._window)
        self._lChampionsFrame.grid(row = 11, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._mChampionsFrame = tkinter.Frame(master = self._window)
        self._mChampionsFrame.grid(row = 12, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._nChampionsFrame = tkinter.Frame(master = self._window)
        self._nChampionsFrame.grid(row = 13, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._oChampionsFrame = tkinter.Frame(master = self._window)
        self._oChampionsFrame.grid(row = 14, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._pChampionsFrame = tkinter.Frame(master = self._window)
        self._pChampionsFrame.grid(row = 15, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._qChampionsFrame = tkinter.Frame(master = self._window)
        self._qChampionsFrame.grid(row = 16, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._rChampionsFrame = tkinter.Frame(master = self._window)
        self._rChampionsFrame.grid(row = 17, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._sChampionsFrame = tkinter.Frame(master = self._window)
        self._sChampionsFrame.grid(row = 18, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._tChampionsFrame = tkinter.Frame(master = self._window)
        self._tChampionsFrame.grid(row = 19, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._uChampionsFrame = tkinter.Frame(master = self._window)
        self._uChampionsFrame.grid(row = 20, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._vChampionsFrame = tkinter.Frame(master = self._window)
        self._vChampionsFrame.grid(row = 21, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._wChampionsFrame = tkinter.Frame(master = self._window)
        self._wChampionsFrame.grid(row = 22, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._xChampionsFrame = tkinter.Frame(master = self._window)
        self._xChampionsFrame.grid(row = 23, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._yChampionsFrame = tkinter.Frame(master = self._window)
        self._yChampionsFrame.grid(row = 24, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._zChampionsFrame = tkinter.Frame(master = self._window)
        self._zChampionsFrame.grid(row = 25, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

#helper to helper functions

    def _setRegion(self, region)->None:
        #called in getRegion()
        #sets the region name and calls _getChampion
        self._region = region
        self._buttonFrame.destroy()
        self._labelFrame.destroy()
        self._getChampion()
        
    def _setChampion(self, championName, championKey)->None:
        #sets the champion name
        self._championName = championName
        self._championKey = championKey

    def _createAChampionFrame(self):
        #called in _getChampion()
        #creates the frame for the champions starting with A
        self._aChampionsFrame = tkinter.Frame(master = self._window)
        self._aChampionsFrame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
        aatroxPhoto = tkinter.PhotoImage(file = "Aatrox.png")
        aatrox = tkinter.Button(master = self._aChampionsFrame, image = aatroxPhoto, command = lambda : self._setChampion("Aatrox", "Aatrox"))
        aatrox.image = aatroxPhoto
        aatrox.pack(side = "left")
        
        ahriPhoto = tkinter.PhotoImage(file = "Ahri.png")
        ahri = tkinter.Button(master = self._aChampionsFrame, image = ahriPhoto, command = lambda : self._setChampion("Ahri", "Ahri"))
        ahri.image = ahriPhoto
        ahri.pack(side = "left")
        
        akaliPhoto = tkinter.PhotoImage(file = "Akali.png")
        akali = tkinter.Button(master = self._aChampionsFrame, image = akaliPhoto, command = lambda : self._setChampion("Akali", "Akali"))
        akali.image = akaliPhoto
        akali.pack(side = "left")

        alistarPhoto = tkinter.PhotoImage(file = "Alistar.png")
        alistar = tkinter.Button(master = self._aChampionsFrame, image = alistarPhoto, command = lambda : self._setChampion("Alistar", "Alistar"))
        alistar.image = alistarPhoto
        alistar.pack(side = "left")
        
        amumuPhoto = tkinter.PhotoImage(file = "Amumu.png")
        amumu = tkinter.Button(master = self._aChampionsFrame, image = amumuPhoto, command = lambda : self._setChampion("Amumu", "Amumu"))
        amumu.image = amumuPhoto
        amumu.pack(side = "left")
                               
        aniviaPhoto = tkinter.PhotoImage(file = "Anivia.png")
        anivia = tkinter.Button(master = self._aChampionsFrame, image = aniviaPhoto, command = lambda : self._setChampion("Anivia", "Anivia"))
        anivia.image = aniviaPhoto
        anivia.pack(side = "left")
                                
        anniePhoto = tkinter.PhotoImage(file = "Annie.png")
        annie = tkinter.Button(master = self._aChampionsFrame, image = anniePhoto, command = lambda : self._setChampion("Annie", "Annie"))
        annie.image = anniePhoto
        annie.pack(side = "left")
                               
        ashePhoto = tkinter.PhotoImage(file = "Ashe.png")
        ashe = tkinter.Button(master = self._aChampionsFrame, image = ashePhoto, command = lambda : self._setChampion("Ashe", "Ashe"))
        ashe.image = ashePhoto
        ashe.pack(side = "left")
            
        azirPhoto = tkinter.PhotoImage(file = "Azir.png")
        azir = tkinter.Button(master = self._aChampionsFrame, image = azirPhoto, command = lambda : self._setChampion("Azir", "Azir"))
        azir.image = azirPhoto
        azir.pack(side = "left")
        
if __name__ == '__main__':
    LeagueOfLegends().start()
