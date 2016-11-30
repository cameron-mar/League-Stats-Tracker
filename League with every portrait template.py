import APIGrabber
import tkinter

class LeagueOfLegends:
    def __init__(self):
        self._window = tkinter.Tk()
        self._window.resizable(width = "false", height = "false")
        self._getRegion() #starts a chain of functions being called
        self._region = "";
        self._championName = "";
        self._championKey = "";

    def start(self)->None:
        #starts the program
        self._window.mainloop()

        
#helper functions
        
    def _getRegion(self)->None:
        #Called in init 
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
        #called in _setRegion
        self._createAChampionFrame()
        self._createBChampionFrame()
        self._createCChampionFrame()
        self._createDChampionFrame()
        self._createEChampionFrame()
        self._createFChampionFrame()
        self._createGChampionFrame()
        self._createHChampionFrame()
        self._createIChampionFrame()
        self._createJChampionFrame()
        self._createKChampionFrame()
        self._createLChampionFrame()
        self._createMChampionFrame()
        self._createNChampionFrame()
        self._createOChampionFrame()
        self._createPChampionFrame()
        self._createQChampionFrame()
        self._createRChampionFrame()
        self._createSChampionFrame()
        self._createTChampionFrame()
        self._createUChampionFrame()
        self._createVChampionFrame()
        self._createWChampionFrame()
        self._createXChampionFrame()
        self._createYChampionFrame()
        self._createZChampionFrame()

#helper to helper functions

    def _setRegion(self, region)->None:
        #called in getRegion()
        #sets the region name and calls _getChampion
        self._region = region
        self._buttonFrame.destroy()
        self._labelFrame.destroy()
        self._getChampion()
        
    def _setChampion(self, championName, championKey)->None:
        #called after button push in a frame maker function
        #sets the champion name
        self._championName = championName
        self._championKey = championKey
        print(self._championName)
        print(self._championKey)

    def _createAChampionFrame(self):
        #called in _getChampion()
        #creates the frame for the champions starting with A
        self._aChampionsFrame = tkinter.Frame(master = self._window)
        self._aChampionsFrame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
        aatroxPhoto = tkinter.PhotoImage(file = "League Pictures\Aatrox.png")
        aatrox = tkinter.Button(master = self._aChampionsFrame, image = aatroxPhoto, command = lambda : self._setChampion("Aatrox", "Aatrox"))
        aatrox.image = aatroxPhoto
        aatrox.pack(side = "left")
        
        ahriPhoto = tkinter.PhotoImage(file = "League Pictures\Ahri.png")
        ahri = tkinter.Button(master = self._aChampionsFrame, image = ahriPhoto, command = lambda : self._setChampion("Ahri", "Ahri"))
        ahri.image = ahriPhoto
        ahri.pack(side = "left")
        
        akaliPhoto = tkinter.PhotoImage(file = "League Pictures\Akali.png")
        akali = tkinter.Button(master = self._aChampionsFrame, image = akaliPhoto, command = lambda : self._setChampion("Akali", "Akali"))
        akali.image = akaliPhoto
        akali.pack(side = "left")

        alistarPhoto = tkinter.PhotoImage(file = "League Pictures\Alistar.png")
        alistar = tkinter.Button(master = self._aChampionsFrame, image = alistarPhoto, command = lambda : self._setChampion("Alistar", "Alistar"))
        alistar.image = alistarPhoto
        alistar.pack(side = "left")
        
        amumuPhoto = tkinter.PhotoImage(file = "League Pictures\Amumu.png")
        amumu = tkinter.Button(master = self._aChampionsFrame, image = amumuPhoto, command = lambda : self._setChampion("Amumu", "Amumu"))
        amumu.image = amumuPhoto
        amumu.pack(side = "left")
                               
        aniviaPhoto = tkinter.PhotoImage(file = "League Pictures\Anivia.png")
        anivia = tkinter.Button(master = self._aChampionsFrame, image = aniviaPhoto, command = lambda : self._setChampion("Anivia", "Anivia"))
        anivia.image = aniviaPhoto
        anivia.pack(side = "left")
                                
        anniePhoto = tkinter.PhotoImage(file = "League Pictures\Annie.png")
        annie = tkinter.Button(master = self._aChampionsFrame, image = anniePhoto, command = lambda : self._setChampion("Annie", "Annie"))
        annie.image = anniePhoto
        annie.pack(side = "left")
                               
        ashePhoto = tkinter.PhotoImage(file = "League Pictures\Ashe.png")
        ashe = tkinter.Button(master = self._aChampionsFrame, image = ashePhoto, command = lambda : self._setChampion("Ashe", "Ashe"))
        ashe.image = ashePhoto
        ashe.pack(side = "left")
            
        azirPhoto = tkinter.PhotoImage(file = "League Pictures\Azir.png")
        azir = tkinter.Button(master = self._aChampionsFrame, image = azirPhoto, command = lambda : self._setChampion("Azir", "Azir"))
        azir.image = azirPhoto
        azir.pack(side = "left")

    def _createBChampionFrame(self):
        #called in _getChampion()
        #creates the frame for champions starting with B
        self._bChampionsFrame = tkinter.Frame(master = self._window)
        self._bChampionsFrame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        bardPhoto = tkinter.PhotoImage(file = "League Pictures\Bard.png")
        bard = tkinter.Button(master = self._bChampionsFrame, image = bardPhoto, command = lambda : self._setChampion("Bard", "Bard"))
        bard.image = bardPhoto
        bard.pack(side = "left")

        blitzcrankPhoto = tkinter.PhotoImage(file = "League Pictures\Blitzcrank.png")
        blitzcrank = tkinter.Button(master = self._bChampionsFrame, image = blitzcrankPhoto, command = lambda : self._setChampion("Blitzcrank", "Blitzcrank"))
        blitzcrank.image = blitzcrankPhoto
        blitzcrank.pack(side = "left")

        brandPhoto = tkinter.PhotoImage(file = "League Pictures\Brand.png")
        brand = tkinter.Button(master = self._bChampionsFrame, image = brandPhoto, command = lambda : self._setChampion("Brand", "Brand"))
        brand.image = brandPhoto
        brand.pack(side = "left")

        braumPhoto = tkinter.PhotoImage(file = "League Pictures\Braum.png")
        braum = tkinter.Button(master = self._bChampionsFrame, image = braumPhoto, command = lambda : self._setChampion("Braum", "Braum"))
        braum.image = braumPhoto
        braum.pack(side = "left")

    def _createCChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with C
        self._cChampionsFrame = tkinter.Frame(master = self._window)
        self._cChampionsFrame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        caitlynPhoto = tkinter.PhotoImage(file = "League Pictures\Caitlyn.png")
        caitlyn = tkinter.Button(master = self._cChampionsFrame, image = caitlynPhoto, command = lambda : self._setChampion("Caitlyn", "Caitlyn"))
        caitlyn.image = caitlynPhoto
        caitlyn.pack(side = "left")

        cassiopeiaPhoto = tkinter.PhotoImage(file = "League Pictures\Cassiopeia.png")
        cassiopeia = tkinter.Button(master = self._cChampionsFrame, image = cassiopeiaPhoto, command = lambda : self._setChampion("Cassiopeia", "Cassiopeia"))
        cassiopeia.image = cassiopeiaPhoto
        cassiopeia.pack(side = "left")

        chogathPhoto = tkinter.PhotoImage(file = "League Pictures\Chogath.png")
        chogath = tkinter.Button(master = self._cChampionsFrame, image = chogathPhoto, command = lambda : self._setChampion("Cho'Gath", "Chogath"))
        chogath.image = chogathPhoto
        chogath.pack(side = "left")

        corkiPhoto = tkinter.PhotoImage(file = "League Pictures\Corki.png")
        corki = tkinter.Button(master = self._cChampionsFrame, image = corkiPhoto, command = lambda : self._setChampion("Corki", "Corki"))
        corki.image = corkiPhoto
        corki.pack(side = "left")
        
    def _createDChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with D
        self._dChampionsFrame = tkinter.Frame(master = self._window)
        self._dChampionsFrame.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        dariusPhoto = tkinter.PhotoImage(file = "League Pictures\Darius.png")
        darius = tkinter.Button(master = self._dChampionsFrame, image = dariusPhoto, command = lambda : self._setChampion("Darius", "Darius"))
        darius.image = dariusPhoto
        darius.pack(side = "left")
        
        dianaPhoto = tkinter.PhotoImage(file = "League Pictures\Diana.png")
        diana = tkinter.Button(master = self._dChampionsFrame, image = dianaPhoto, command = lambda : self._setChampion("Diana", "Diana"))
        diana.image = dianaPhoto
        diana.pack(side = "left")
        
        dravenPhoto = tkinter.PhotoImage(file = "League Pictures\Draven.png")
        draven = tkinter.Button(master = self._dChampionsFrame, image = dravenPhoto, command = lambda : self._setChampion("Draven", "Draven"))
        draven.image = dravenPhoto
        draven.pack(side = "left")
        
        drMundoPhoto = tkinter.PhotoImage(file = "League Pictures\DrMundo.png")
        drMundo = tkinter.Button(master = self._dChampionsFrame, image = drMundoPhoto, command = lambda: self._setChampion("Dr. Mundo", "DrMundo"))
        drMundo.image = drMundoPhoto
        drMundo.pack(side = "left")
        
    def _createEChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with E
        self._eChampionsFrame = tkinter.Frame(master = self._window)
        self._eChampionsFrame.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        ekkoPhoto = tkinter.PhotoImage(file = "League Pictures\Ekko.png")
        ekko = tkinter.Button(master = self._eChampionsFrame, image = ekkoPhoto, command = lambda : self._setChampion("Ekko", "Ekko"))
        ekko.image = ekkoPhoto
        ekko.pack(side = "left")
        
        elisePhoto = tkinter.PhotoImage(file = "League Pictures\Elise.png")
        elise = tkinter.Button(master = self._eChampionsFrame, image = elisePhoto, command = lambda : self._setChampion("Elise", "Elise"))
        elise.image = elisePhoto
        elise.pack(side = "left")
        
        evelynnPhoto = tkinter.PhotoImage(file = "League Pictures\Evelynn.png")
        evelynn = tkinter.Button(master = self._eChampionsFrame, image = evelynnPhoto, command = lambda : self._setChampion("Evelynn", "Evelynn"))
        evelynn.image = evelynnPhoto
        evelynn.pack(side = "left")
        
        ezrealPhoto = tkinter.PhotoImage(file = "League Pictures\Ezreal.png")
        ezreal = tkinter.Button(master = self._eChampionsFrame, image = ezrealPhoto, command = lambda : self._setChampion("Ezreal", "Ezreal"))
        ezreal.image = ezrealPhoto
        ezreal.pack(side = "left")
        
    def _createFChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with F
        self._fChampionsFrame = tkinter.Frame(master = self._window)
        self._fChampionsFrame.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

        fiddleSticksPhoto = tkinter.PhotoImage(file = "League Pictures\FiddleSticks.png")
        fiddleSticks = tkinter.Button(master = self._fChampionsFrame, image = fiddleSticksPhoto, command = lambda : self._setChampion("Fiddlesticks", "FiddleSticks"))
        fiddleSticks.image = fiddleSticksPhoto
        fiddleSticks.pack(side = "left")

        fioraPhoto = tkinter.PhotoImage(file = "League Pictures\Fiora.png")
        fiora = tkinter.Button(master = self._fChampionsFrame, image = fioraPhoto, command = lambda : self._setChampion("Fiora", "Fiora"))
        fiora.image = fioraPhoto
        fiora.pack(side = "left")

        fizzPhoto = tkinter.PhotoImage(file = "League Pictures\Fizz.png")
        fizz = tkinter.Button(master = self._fChampionsFrame, image = fizzPhoto, command = lambda : self._setChampion("Fizz", "Fizz"))
        fizz.image = fizzPhoto
        fizz.pack(side = "left")
        
    def _createGChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with G
        self._gChampionsFrame = tkinter.Frame(master = self._window)
        self._gChampionsFrame.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = tkinter.E)

        galioPhoto = tkinter.PhotoImage(file = "League Pictures\Galio.png")
        galio = tkinter.Button(master = self._gChampionsFrame, image = galioPhoto, command = lambda : self._setChampion("Galio", "Galio"))
        galio.image = galioPhoto
        galio.pack(side = "left")

        gangplankPhoto = tkinter.PhotoImage(file = "League Pictures\Gangplank.png")
        gangplank = tkinter.Button(master = self._gChampionsFrame, image = gangplankPhoto, command = lambda : self._setChampion("Gangplank", "Gangplank"))
        gangplank.image = gangplankPhoto
        gangplank.pack(side = "left")
        
        garenPhoto = tkinter.PhotoImage(file = "League Pictures\Garen.png")
        garen = tkinter.Button(master = self._gChampionsFrame, image = garenPhoto, command = lambda : self._setChampion("Garen", "Garen"))
        garen.image = garenPhoto
        garen.pack(side = "left")

        gnarPhoto = tkinter.PhotoImage(file = "League Pictures\Gnar.png")
        gnar = tkinter.Button(master = self._gChampionsFrame, image = gnarPhoto, command = lambda : self._setChampion("Gnar", "Gnar"))
        gnar.image = gnarPhoto
        gnar.pack(side = "left")

        gragasPhoto = tkinter.PhotoImage(file = "League Pictures\Gragas.png")
        gragas = tkinter.Button(master = self._gChampionsFrame, image = gragasPhoto, command = lambda : self._setChampion("Gragas", "Gragas"))
        gragas.image = gragasPhoto
        gragas.pack(side = "left")
        
        gravesPhoto = tkinter.PhotoImage(file = "League Pictures\Graves.png")
        graves = tkinter.Button(master = self._gChampionsFrame, image = gravesPhoto, command = lambda : self._setChampion("Graves", "Graves"))
        graves.image = gravesPhoto
        graves.pack(side = "left")
        
    def _createHChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with H
        self._hChampionsFrame = tkinter.Frame(master = self._window)
        self._hChampionsFrame.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createIChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with I
        self._iChampionsFrame = tkinter.Frame(master = self._window)
        self._iChampionsFrame.grid(row = 8, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createJChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with J
        self._jChampionsFrame = tkinter.Frame(master = self._window)
        self._jChampionsFrame.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createKChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with K
        self._kChampionsFrame = tkinter.Frame(master = self._window)
        self._kChampionsFrame.grid(row = 10, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createLChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with L
        self._lChampionsFrame = tkinter.Frame(master = self._window)
        self._lChampionsFrame.grid(row = 11, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createMChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with M
        self._mChampionsFrame = tkinter.Frame(master = self._window)
        self._mChampionsFrame.grid(row = 12, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createNChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with N
        self._nChampionsFrame = tkinter.Frame(master = self._window)
        self._nChampionsFrame.grid(row = 13, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createOChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with O
        self._oChampionsFrame = tkinter.Frame(master = self._window)
        self._oChampionsFrame.grid(row = 14, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createPChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with P
        self._pChampionsFrame = tkinter.Frame(master = self._window)
        self._pChampionsFrame.grid(row = 15, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createQChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with Q
        self._qChampionsFrame = tkinter.Frame(master = self._window)
        self._qChampionsFrame.grid(row = 16, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createRChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with R
        self._rChampionsFrame = tkinter.Frame(master = self._window)
        self._rChampionsFrame.grid(row = 17, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createSChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with S
        self._sChampionsFrame = tkinter.Frame(master = self._window)
        self._sChampionsFrame.grid(row = 18, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createTChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with T
        self._tChampionsFrame = tkinter.Frame(master = self._window)
        self._tChampionsFrame.grid(row = 19, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createUChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with U
        self._uChampionsFrame = tkinter.Frame(master = self._window)
        self._uChampionsFrame.grid(row = 20, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createVChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with V
        self._vChampionsFrame = tkinter.Frame(master = self._window)
        self._vChampionsFrame.grid(row = 21, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createWChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with W
        self._wChampionsFrame = tkinter.Frame(master = self._window)
        self._wChampionsFrame.grid(row = 22, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createXChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with X
        self._xChampionsFrame = tkinter.Frame(master = self._window)
        self._xChampionsFrame.grid(row = 23, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createYChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with Y
        self._yChampionsFrame = tkinter.Frame(master = self._window)
        self._yChampionsFrame.grid(row = 24, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        
    def _createZChampionFrame(self):
        #called in_getChampion()
        #creates the frame for champions starting with Z
        self._zChampionsFrame = tkinter.Frame(master = self._window)
        self._zChampionsFrame.grid(row = 25, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)                          
        
if __name__ == '__main__':
    LeagueOfLegends().start()
