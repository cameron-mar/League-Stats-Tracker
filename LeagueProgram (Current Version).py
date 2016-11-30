import LeagueLogic
import tkinter

class LeagueProgram:
    def __init__(self):
        self._window = tkinter.Tk()
        self._getRegion()#starts a chain of functions
        self._region = "";
        self._championName = "";
        self._championKey = "";
        self._runes = {}

    def start(self):
        self._window.mainloop()
        
#getter functions
        
    def _getRegion(self)->None:
        #Called in init 
        #Displays prompt and region buttons
        self.createRegionButtons()
        #hands off job to _setRegion()
    
    def _getChampion(self)->None:
        #called in _setRegion
        self._createStackingFrames()
        self._championFillTopFrames() #fill the frames with alphabet buttons that will make buttons of champions
        self._championFillMidFrames()
        self._championFillBotFrames()
        self._championFillBotBotFrames()
        #hands off job to _setChampion()

    def _getRunes(self)->None:
        self._getQuints()
        self._getSeals()
        self._getGlyphs()
        self._getMarks()

    def _getQuints(self):
        self._createQuintButtons()
    
        
#setter functions

    def _setRegion(self, region)->None:
        #called in getRegion()
        #sets the region name and calls _getChampion
        self._region = region
        self._deleteStackingFrames()
        self._getChampion()
        
    def _setChampion(self, championName, championKey)->None:
        #called after button push in a frame maker function
        #sets the champion name and destroys the frame with champion buttons
        self._championName = championName
        self._championKey = championKey
        self._championFrame.destroy() #created in _createChampionFrame()
        self._getRunes()
        #print(self._championName)
        #print(self._championKey)

    def _setRunes(self,ID:{int}):
        #the key is the rune ID and the value is the number of that type of rune
        self._runes = ID
        

#Frame Creation Functions
        
    def _createStackingFrames(self):
        #called in createRegionButtons(), _getChampion(), _createQuintButtons(), _createSealButtons(),
        #_createGlyphButtons(), _createMarkButtons()
        #creates 4 frames on top of each other
        self._topFrame = tkinter.Frame(master = self._window)
        self._topFrame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._midFrame = tkinter.Frame(master = self._window)
        self._midFrame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._botFrame = tkinter.Frame(master = self._window)
        self._botFrame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)
        self._botBotFrame = tkinter.Frame(master = self._window)
        self._botBotFrame.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

    def _createChampionFrame(self):
        #called in every function that creates champion buttons
        #destroys the four stacking frames and makes a frame for the champion buttons
        self._deleteStackingFrames()
        self._championFrame = tkinter.Frame(master = self._window)
        self._championFrame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W + tkinter.E)

#Deletion Functions

    def _deleteStackingFrames(self):
        #called in getRegion()
        #deletes the four frames made in _createStackingFrames()
        self._topFrame.destroy()
        self._midFrame.destroy()
        self._botFrame.destroy()
        self._botBotFrame.destroy()
        
#Frame filling functions
        
    def _championFillTopFrames(self):
        #called in _getChampion()
        #creates buttons for A-H
        a = tkinter.Button(master = self._topFrame, text = "A", font = ("Helvetica", 30), command = lambda : self._createAChampionButtons())
        a.pack(side = "left")
        b = tkinter.Button(master = self._topFrame, text = "B", font = ("Helvetica", 30), command = lambda : self._createBChampionButtons())
        b.pack(side = "left")
        c = tkinter.Button(master = self._topFrame, text = "C", font = ("Helvetica", 30), command = lambda : self._createCChampionButtons())
        c.pack(side = "left")
        d = tkinter.Button(master = self._topFrame, text = "D", font = ("Helvetica", 30), command = lambda : self._createDChampionButtons())
        d.pack(side = "left")
        e = tkinter.Button(master = self._topFrame, text = "E", font = ("Helvetica", 30), command = lambda : self._createEChampionButtons())
        e.pack(side = "left")
        f = tkinter.Button(master = self._topFrame, text = "F", font = ("Helvetica", 30), command = lambda : self._createFChampionButtons())
        f.pack(side = "left")
        g = tkinter.Button(master = self._topFrame, text = "G", font = ("Helvetica", 30), command = lambda : self._createGChampionButtons())
        g.pack(side = "left")
        h = tkinter.Button(master = self._topFrame, text = "H", font = ("Helvetica", 30), command = lambda : self._createHChampionButtons())
        h.pack(side = "left")
                
    def _championFillMidFrames(self):
        #called in _getChampion()
        #creates buttons for I-P
        i = tkinter.Button(master = self._midFrame, text = "I", font = ("Helvetica", 30), command = lambda : self._createIChampionButtons())
        i.pack(side = "left")
        j = tkinter.Button(master = self._midFrame, text = "J", font = ("Helvetica", 30), command = lambda : self._createJChampionButtons())
        j.pack(side = "left")
        k = tkinter.Button(master = self._midFrame, text = "K", font = ("Helvetica", 30), command = lambda : self._createKChampionButtons())
        k.pack(side = "left")
        l = tkinter.Button(master = self._midFrame, text = "L", font = ("Helvetica", 30), command = lambda : self._createLChampionButtons())
        l.pack(side = "left")
        m = tkinter.Button(master = self._midFrame, text = "M", font = ("Helvetica", 30), command = lambda : self._createMChampionButtons())
        m.pack(side = "left")
        n = tkinter.Button(master = self._midFrame, text = "N", font = ("Helvetica", 30), command = lambda : self._createNChampionButtons())
        n.pack(side = "left")
        o = tkinter.Button(master = self._midFrame, text = "O", font = ("Helvetica", 30), command = lambda : self._createOChampionButtons())
        o.pack(side = "left")
        p = tkinter.Button(master = self._midFrame, text = "P", font = ("Helvetica", 30), command = lambda : self._createPChampionButtons())
        p.pack(side = "left")

    def _championFillBotFrames(self):
        #called in _getChampion()
        #creates buttons for Q-X
        q = tkinter.Button(master = self._botFrame, text = "Q", font = ("Helvetica", 30), command = lambda : self._createQChampionButtons())
        q.pack(side = "left")
        r = tkinter.Button(master = self._botFrame, text = "R", font = ("Helvetica", 30), command = lambda : self._createRChampionButtons())
        r.pack(side = "left")
        s = tkinter.Button(master = self._botFrame, text = "S", font = ("Helvetica", 30), command = lambda : self._createSChampionButtons())
        s.pack(side = "left")
        t = tkinter.Button(master = self._botFrame, text = "T", font = ("Helvetica", 30), command = lambda : self._createTChampionButtons())
        t.pack(side = "left")
        u = tkinter.Button(master = self._botFrame, text = "U", font = ("Helvetica", 30), command = lambda : self._createUChampionButtons())
        u.pack(side = "left")
        v = tkinter.Button(master = self._botFrame, text = "V", font = ("Helvetica", 30), command = lambda : self._createVChampionButtons())
        v.pack(side = "left")
        w = tkinter.Button(master = self._botFrame, text = "W", font = ("Helvetica", 30), command = lambda : self._createWChampionButtons())
        w.pack(side = "left")
        x = tkinter.Button(master = self._botFrame, text = "X", font = ("Helvetica", 30), command = lambda : self._createXChampionButtons())
        x.pack(side = "left")

    def _championFillBotBotFrames(self):
        #called in _getChampion()
        #creates buttons for Y and Z
        y = tkinter.Button(master = self._botBotFrame, text = "Y", font = ("Helvetica", 30), command = lambda : self._createYChampionButtons())
        y.pack(side = "left")
        z = tkinter.Button(master = self._botBotFrame, text = "Z", font = ("Helvetica", 30), command = lambda : self._createZChampionButtons())
        z.pack(side = "left")    

#Region button creation
        
    def createRegionButtons(self):
        #called in getRegion()
        #creates region buttons
        self._createStackingFrames()
        label = tkinter.Label(master = self._topFrame, text = 'Please click on your region.',
                              font = ('Helvetica', 30))
        label.pack()

        na = tkinter.Button(master = self._midFrame, text = 'NA', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("na"))
        euw = tkinter.Button(master = self._midFrame, text = 'EUW', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("euw"))
        eune = tkinter.Button(master = self._midFrame, text = 'EUNE', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("eune"))
        lan = tkinter.Button(master = self._midFrame, text = 'LAN', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("lan"))
        las = tkinter.Button(master = self._midFrame, text = 'LAN', font =
                             ('Helvetica', 20), command = lambda : self._setRegion("las"))
        br = tkinter.Button(master = self._midFrame, text = 'BR', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("br"))
        oce = tkinter.Button(master = self._midFrame, text = 'OCE', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("oce"))
        pbe = tkinter.Button(master = self._midFrame, text = 'PBE', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("pbe"))
        tr = tkinter.Button(master = self._midFrame, text = 'TR', font =
                            ('Helvetica', 20), command = lambda : self._setRegion("tr"))
        ru = tkinter.Button(master = self._midFrame, text = 'RU', font =
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
        
#Champion button creation functions

    def _createAChampionButtons(self):
        #called in _championFillTopFrames()
        #creates the buttons for the champions starting with A
        self._createChampionFrame()
            
        aatroxPhoto = tkinter.PhotoImage(file = "League Pictures\Aatrox.png")
        aatrox = tkinter.Button(master = self._championFrame, image = aatroxPhoto, command = lambda : self._setChampion("Aatrox", "Aatrox"))
        aatrox.image = aatroxPhoto
        aatrox.pack(side = "left")
            
        ahriPhoto = tkinter.PhotoImage(file = "League Pictures\Ahri.png")
        ahri = tkinter.Button(master = self._championFrame, image = ahriPhoto, command = lambda : self._setChampion("Ahri", "Ahri"))
        ahri.image = ahriPhoto
        ahri.pack(side = "left")
            
        akaliPhoto = tkinter.PhotoImage(file = "League Pictures\Akali.png")
        akali = tkinter.Button(master = self._championFrame, image = akaliPhoto, command = lambda : self._setChampion("Akali", "Akali"))
        akali.image = akaliPhoto
        akali.pack(side = "left")

        alistarPhoto = tkinter.PhotoImage(file = "League Pictures\Alistar.png")
        alistar = tkinter.Button(master = self._championFrame, image = alistarPhoto, command = lambda : self._setChampion("Alistar", "Alistar"))
        alistar.image = alistarPhoto
        alistar.pack(side = "left")
            
        amumuPhoto = tkinter.PhotoImage(file = "League Pictures\Amumu.png")
        amumu = tkinter.Button(master = self._championFrame, image = amumuPhoto, command = lambda : self._setChampion("Amumu", "Amumu"))
        amumu.image = amumuPhoto
        amumu.pack(side = "left")
                                   
        aniviaPhoto = tkinter.PhotoImage(file = "League Pictures\Anivia.png")
        anivia = tkinter.Button(master = self._championFrame, image = aniviaPhoto, command = lambda : self._setChampion("Anivia", "Anivia"))
        anivia.image = aniviaPhoto
        anivia.pack(side = "left")
                                    
        anniePhoto = tkinter.PhotoImage(file = "League Pictures\Annie.png")
        annie = tkinter.Button(master = self._championFrame, image = anniePhoto, command = lambda : self._setChampion("Annie", "Annie"))
        annie.image = anniePhoto
        annie.pack(side = "left")
                                   
        ashePhoto = tkinter.PhotoImage(file = "League Pictures\Ashe.png")
        ashe = tkinter.Button(master = self._championFrame, image = ashePhoto, command = lambda : self._setChampion("Ashe", "Ashe"))
        ashe.image = ashePhoto
        ashe.pack(side = "left")
                
        azirPhoto = tkinter.PhotoImage(file = "League Pictures\Azir.png")
        azir = tkinter.Button(master = self._championFrame, image = azirPhoto, command = lambda : self._setChampion("Azir", "Azir"))
        azir.image = azirPhoto
        azir.pack(side = "left")        

    def _createBChampionButtons(self):
        #called in _championFillTopFrames()
        #creates the buttons for champions starting with B
        self._createChampionFrame()

        bardPhoto = tkinter.PhotoImage(file = "League Pictures\Bard.png")
        bard = tkinter.Button(master = self._championFrame, image = bardPhoto, command = lambda : self._setChampion("Bard", "Bard"))
        bard.image = bardPhoto
        bard.pack(side = "left")

        blitzcrankPhoto = tkinter.PhotoImage(file = "League Pictures\Blitzcrank.png")
        blitzcrank = tkinter.Button(master = self._championFrame, image = blitzcrankPhoto, command = lambda : self._setChampion("Blitzcrank", "Blitzcrank"))
        blitzcrank.image = blitzcrankPhoto
        blitzcrank.pack(side = "left")

        brandPhoto = tkinter.PhotoImage(file = "League Pictures\Brand.png")
        brand = tkinter.Button(master = self._championFrame, image = brandPhoto, command = lambda : self._setChampion("Brand", "Brand"))
        brand.image = brandPhoto
        brand.pack(side = "left")

        braumPhoto = tkinter.PhotoImage(file = "League Pictures\Braum.png")
        braum = tkinter.Button(master = self._championFrame, image = braumPhoto, command = lambda : self._setChampion("Braum", "Braum"))
        braum.image = braumPhoto
        braum.pack(side = "left")        

    def _createCChampionButtons(self):
        #called in _championFillTopFrames()
        #creates the buttons for champions starting with C
        self._createChampionFrame()

        caitlynPhoto = tkinter.PhotoImage(file = "League Pictures\Caitlyn.png")
        caitlyn = tkinter.Button(master = self._championFrame, image = caitlynPhoto, command = lambda : self._setChampion("Caitlyn", "Caitlyn"))
        caitlyn.image = caitlynPhoto
        caitlyn.pack(side = "left")

        cassiopeiaPhoto = tkinter.PhotoImage(file = "League Pictures\Cassiopeia.png")
        cassiopeia = tkinter.Button(master = self._championFrame, image = cassiopeiaPhoto, command = lambda : self._setChampion("Cassiopeia", "Cassiopeia"))
        cassiopeia.image = cassiopeiaPhoto
        cassiopeia.pack(side = "left")

        chogathPhoto = tkinter.PhotoImage(file = "League Pictures\Chogath.png")
        chogath = tkinter.Button(master = self._championFrame, image = chogathPhoto, command = lambda : self._setChampion("Cho'Gath", "Chogath"))
        chogath.image = chogathPhoto
        chogath.pack(side = "left")

        corkiPhoto = tkinter.PhotoImage(file = "League Pictures\Corki.png")
        corki = tkinter.Button(master = self._championFrame, image = corkiPhoto, command = lambda : self._setChampion("Corki", "Corki"))
        corki.image = corkiPhoto
        corki.pack(side = "left")
            
    def _createDChampionButtons(self):
        #called in _championFillTopFrames()
        #creates the buttons for champions starting with D
        self._createChampionFrame()

        dariusPhoto = tkinter.PhotoImage(file = "League Pictures\Darius.png")
        darius = tkinter.Button(master = self._championFrame, image = dariusPhoto, command = lambda : self._setChampion("Darius", "Darius"))
        darius.image = dariusPhoto
        darius.pack(side = "left")
            
        dianaPhoto = tkinter.PhotoImage(file = "League Pictures\Diana.png")
        diana = tkinter.Button(master = self._championFrame, image = dianaPhoto, command = lambda : self._setChampion("Diana", "Diana"))
        diana.image = dianaPhoto
        diana.pack(side = "left")
            
        dravenPhoto = tkinter.PhotoImage(file = "League Pictures\Draven.png")
        draven = tkinter.Button(master = self._championFrame, image = dravenPhoto, command = lambda : self._setChampion("Draven", "Draven"))
        draven.image = dravenPhoto
        draven.pack(side = "left")
            
        drMundoPhoto = tkinter.PhotoImage(file = "League Pictures\DrMundo.png")
        drMundo = tkinter.Button(master = self._championFrame, image = drMundoPhoto, command = lambda: self._setChampion("Dr. Mundo", "DrMundo"))
        drMundo.image = drMundoPhoto
        drMundo.pack(side = "left")
            
    def _createEChampionButtons(self):
        #called in _championFillTopFrames())
        #creates the buttons for champions starting with E
        self._createChampionFrame()

        ekkoPhoto = tkinter.PhotoImage(file = "League Pictures\Ekko.png")
        ekko = tkinter.Button(master = self._championFrame, image = ekkoPhoto, command = lambda : self._setChampion("Ekko", "Ekko"))
        ekko.image = ekkoPhoto
        ekko.pack(side = "left")
            
        elisePhoto = tkinter.PhotoImage(file = "League Pictures\Elise.png")
        elise = tkinter.Button(master = self._championFrame, image = elisePhoto, command = lambda : self._setChampion("Elise", "Elise"))
        elise.image = elisePhoto
        elise.pack(side = "left")
            
        evelynnPhoto = tkinter.PhotoImage(file = "League Pictures\Evelynn.png")
        evelynn = tkinter.Button(master = self._championFrame, image = evelynnPhoto, command = lambda : self._setChampion("Evelynn", "Evelynn"))
        evelynn.image = evelynnPhoto
        evelynn.pack(side = "left")
            
        ezrealPhoto = tkinter.PhotoImage(file = "League Pictures\Ezreal.png")
        ezreal = tkinter.Button(master = self._championFrame, image = ezrealPhoto, command = lambda : self._setChampion("Ezreal", "Ezreal"))
        ezreal.image = ezrealPhoto
        ezreal.pack(side = "left")
            
    def _createFChampionButtons(self):
        #called in _championFillTopFrames()
        #creates the buttons for champions starting with F
        self._createChampionFrame()

        fiddleSticksPhoto = tkinter.PhotoImage(file = "League Pictures\FiddleSticks.png")
        fiddleSticks = tkinter.Button(master = self._championFrame, image = fiddleSticksPhoto, command = lambda : self._setChampion("Fiddlesticks", "FiddleSticks"))
        fiddleSticks.image = fiddleSticksPhoto
        fiddleSticks.pack(side = "left")

        fioraPhoto = tkinter.PhotoImage(file = "League Pictures\Fiora.png")
        fiora = tkinter.Button(master = self._championFrame, image = fioraPhoto, command = lambda : self._setChampion("Fiora", "Fiora"))
        fiora.image = fioraPhoto
        fiora.pack(side = "left")

        fizzPhoto = tkinter.PhotoImage(file = "League Pictures\Fizz.png")
        fizz = tkinter.Button(master = self._championFrame, image = fizzPhoto, command = lambda : self._setChampion("Fizz", "Fizz"))
        fizz.image = fizzPhoto
        fizz.pack(side = "left")
            
    def _createGChampionButtons(self):
        #called in _championFillTopFrames()
        #creates the buttons for champions starting with G
        self._createChampionFrame()

        galioPhoto = tkinter.PhotoImage(file = "League Pictures\Galio.png")
        galio = tkinter.Button(master = self._championFrame, image = galioPhoto, command = lambda : self._setChampion("Galio", "Galio"))
        galio.image = galioPhoto
        galio.pack(side = "left")

        gangplankPhoto = tkinter.PhotoImage(file = "League Pictures\Gangplank.png")
        gangplank = tkinter.Button(master = self._championFrame, image = gangplankPhoto, command = lambda : self._setChampion("Gangplank", "Gangplank"))
        gangplank.image = gangplankPhoto
        gangplank.pack(side = "left")
            
        garenPhoto = tkinter.PhotoImage(file = "League Pictures\Garen.png")
        garen = tkinter.Button(master = self._championFrame, image = garenPhoto, command = lambda : self._setChampion("Garen", "Garen"))
        garen.image = garenPhoto
        garen.pack(side = "left")

        gnarPhoto = tkinter.PhotoImage(file = "League Pictures\Gnar.png")
        gnar = tkinter.Button(master = self._championFrame, image = gnarPhoto, command = lambda : self._setChampion("Gnar", "Gnar"))
        gnar.image = gnarPhoto
        gnar.pack(side = "left")

        gragasPhoto = tkinter.PhotoImage(file = "League Pictures\Gragas.png")
        gragas = tkinter.Button(master = self._championFrame, image = gragasPhoto, command = lambda : self._setChampion("Gragas", "Gragas"))
        gragas.image = gragasPhoto
        gragas.pack(side = "left")
            
        gravesPhoto = tkinter.PhotoImage(file = "League Pictures\Graves.png")
        graves = tkinter.Button(master = self._championFrame, image = gravesPhoto, command = lambda : self._setChampion("Graves", "Graves"))
        graves.image = gravesPhoto
        graves.pack(side = "left")
            
    def _createHChampionButtons(self):
        #called in _championFillTopFrames()
        #creates the buttons for champions starting with H
        self._createChampionFrame()

        hecarimPhoto = tkinter.PhotoImage(file = "League Pictures\Hecarim.png")
        hecarim = tkinter.Button(master = self._championFrame, image = hecarimPhoto, command = lambda : self._setChampion("Hecarim", "Hecarim"))
        hecarim.image = hecarimPhoto
        hecarim.pack(side = "left")

        heimerdingerPhoto = tkinter.PhotoImage(file = "League Pictures\Heimerdinger.png")
        heimerdinger = tkinter.Button(master = self._championFrame, image = heimerdingerPhoto, command = lambda : self._setChampion("Heimerdinger", "Heimerdinger"))
        heimerdinger.image = heimerdingerPhoto
        heimerdinger.pack(side = "left")
            
    def _createIChampionButtons(self):
        #called in _championFillMidFrames()
        #creates the buttons for champions starting with I
        self._createChampionFrame()

        illaoiPhoto = tkinter.PhotoImage(file = "League Pictures\Illaoi.png")
        illaoi = tkinter.Button(master = self._championFrame, image = illaoiPhoto, command = lambda : self._setChampion("Illaoi", "Illaoi"))
        illaoi.image = illaoiPhoto
        illaoi.pack(side = "left")

        ireliaPhoto = tkinter.PhotoImage(file = "League Pictures\Irelia.png")
        irelia = tkinter.Button(master = self._championFrame, image = ireliaPhoto, command = lambda : self._setChampion("Irelia", "Irelia"))
        irelia.image = ireliaPhoto
        irelia.pack(side = "left")
            
    def _createJChampionButtons(self):
        #called in _championFillMidFrames()
        #creates the buttons for champions starting with J
        self._createChampionFrame()

        jannaPhoto = tkinter.PhotoImage(file = "League Pictures\Janna.png")
        janna = tkinter.Button(master = self._championFrame, image = jannaPhoto, command = lambda : self._setChampion("Janna", "Janna"))
        janna.image = jannaPhoto
        janna.pack(side = "left")

        jarvanPhoto = tkinter.PhotoImage(file = "League Pictures\JarvanIV.png")
        jarvan = tkinter.Button(master = self._championFrame, image = jarvanPhoto, command = lambda : self._setChampion("Jarvan IV", "JarvanIV"))
        jarvan.image = jarvanPhoto
        jarvan.pack(side = "left")

        jaxPhoto = tkinter.PhotoImage(file = "League Pictures\Jax.png")
        jax = tkinter.Button(master = self._championFrame, image = jaxPhoto, command = lambda : self._setChampion("Jax", "Jax"))
        jax.image = jaxPhoto
        jax.pack(side = "left")

        jaycePhoto = tkinter.PhotoImage(file = "League Pictures\Jayce.png")
        jayce = tkinter.Button(master = self._championFrame, image = jaycePhoto, command = lambda : self._setChampion("Jayce", "Jayce"))
        jayce.image = jaycePhoto
        jayce.pack(side = "left")
            
    def _createKChampionButtons(self):
        #called in _championFillMidFrames()
        #creates the buttons for champions starting with K
        self._createChampionFrame()

        kalistaPhoto = tkinter.PhotoImage(file = "League Pictures\Kalista.png")
        kalista = tkinter.Button(master = self._championFrame, image = kalistaPhoto, command = lambda : self._setChampion("Kalista", "Kalista"))
        kalista.image = kalistaPhoto
        kalista.pack(side = "left")
            
        karmaPhoto = tkinter.PhotoImage(file = "League Pictures\Karma.png")
        karma = tkinter.Button(master = self._championFrame, image = karmaPhoto, command = lambda : self._setChampion("Karma", "Karma"))
        karma.image = karmaPhoto
        karma.pack(side = "left")
            
        karthusPhoto = tkinter.PhotoImage(file = "League Pictures\Karthus.png")
        karthus = tkinter.Button(master = self._championFrame, image = karthusPhoto, command = lambda : self._setChampion("Karthus", "Karthus"))
        karthus.image = karthusPhoto
        karthus.pack(side = "left")
            
        kassadinPhoto = tkinter.PhotoImage(file = "League Pictures\Kassadin.png")
        kassadin = tkinter.Button(master = self._championFrame, image = kassadinPhoto, command = lambda : self._setChampion("Kassadin", "Kassadin"))
        kassadin.image = kassadinPhoto
        kassadin.pack(side = "left")
            
        katarinaPhoto = tkinter.PhotoImage(file = "League Pictures\Katarina.png")
        katarina = tkinter.Button(master = self._championFrame, image = katarinaPhoto, command = lambda : self._setChampion("Katarina", "Katarina"))
        katarina.image = katarinaPhoto
        katarina.pack(side = "left")
            
        kaylePhoto = tkinter.PhotoImage(file = "League Pictures\Kayle.png")
        kayle = tkinter.Button(master = self._championFrame, image = kaylePhoto, command = lambda : self._setChampion("Kayle", "Kayle"))
        kayle.image = kaylePhoto
        kayle.pack(side = "left")
            
        kennenPhoto = tkinter.PhotoImage(file = "League Pictures\Kennen.png")
        kennen = tkinter.Button(master = self._championFrame, image = kennenPhoto, command = lambda : self._setChampion("Kennen", "Kennen"))
        kennen.image = kennenPhoto
        kennen.pack(side = "left")
            
        khazixPhoto = tkinter.PhotoImage(file = "League Pictures\Khazix.png")
        khazix = tkinter.Button(master = self._championFrame, image = khazixPhoto, command = lambda : self._setChampion("Kha'Zix", "Khazix"))
        khazix.image = khazixPhoto
        khazix.pack(side = "left")
            
        kindredPhoto = tkinter.PhotoImage(file = "League Pictures\Kindred.png")
        kindred = tkinter.Button(master = self._championFrame, image = kindredPhoto, command = lambda : self._setChampion("Kindred", "Kindred"))
        kindred.image = kindredPhoto
        kindred.pack(side = "left")
            
        kogmawPhoto = tkinter.PhotoImage(file = "League Pictures\KogMaw.png")
        kogmaw = tkinter.Button(master = self._championFrame, image = kogmawPhoto, command = lambda : self._setChampion("Kog'Maw", "KogMaw"))
        kogmaw.image = kogmawPhoto
        kogmaw.pack(side = "left")
            
    def _createLChampionButtons(self):
        #called in _championFillMidFrames()
        #creates the buttons for champions starting with L
        self._createChampionFrame()

        leblancPhoto = tkinter.PhotoImage(file = "League Pictures\Leblanc.png")
        leblanc = tkinter.Button(master = self._championFrame, image = leblancPhoto, command = lambda : self._setChampion("Leblanc", "Leblanc"))
        leblanc.image = leblancPhoto
        leblanc.pack(side = "left")

        leesinPhoto = tkinter.PhotoImage(file = "League Pictures\LeeSin.png")
        leesin = tkinter.Button(master = self._championFrame, image = leesinPhoto, command = lambda : self._setChampion("Lee Sin", "LeeSin"))
        leesin.image = leesinPhoto
        leesin.pack(side = "left")

        leonaPhoto = tkinter.PhotoImage(file = "League Pictures\Leona.png")
        leona = tkinter.Button(master = self._championFrame, image = leonaPhoto, command = lambda : self._setChampion("Leona", "Leona"))
        leona.image = leonaPhoto
        leona.pack(side = "left")

        lissandraPhoto = tkinter.PhotoImage(file = "League Pictures\Lissandra.png")
        lissandra = tkinter.Button(master = self._championFrame, image = lissandraPhoto, command = lambda : self._setChampion("Lissandra", "Lissandra"))
        lissandra.image = lissandraPhoto
        lissandra.pack(side = "left")

        lucianPhoto = tkinter.PhotoImage(file = "League Pictures\Lucian.png")
        lucian = tkinter.Button(master = self._championFrame, image = lucianPhoto, command = lambda : self._setChampion("Lucian", "Lucian"))
        lucian.image = lucianPhoto
        lucian.pack(side = "left")

        luluPhoto = tkinter.PhotoImage(file = "League Pictures\Lulu.png")
        lulu = tkinter.Button(master = self._championFrame, image = luluPhoto, command = lambda : self._setChampion("Lulu", "Lulu"))
        lulu.image = luluPhoto
        lulu.pack(side = "left")

        luxPhoto = tkinter.PhotoImage(file = "League Pictures\Lux.png")
        lux = tkinter.Button(master = self._championFrame, image = luxPhoto, command = lambda : self._setChampion("Lux", "Lux"))
        lux.image = luxPhoto
        lux.pack(side = "left")
            
    def _createMChampionButtons(self):
        #called in _championFillMidFrames()
        #creates the buttons for champions starting with M
        self._createChampionFrame()

        malphitePhoto = tkinter.PhotoImage(file = "League Pictures\Malphite.png")
        malphite = tkinter.Button(master = self._championFrame, image = malphitePhoto, command = lambda : self._setChampion("Malphite", "Malphite"))
        malphite.image = malphitePhoto
        malphite.pack(side = "left")

        malzaharPhoto = tkinter.PhotoImage(file = "League Pictures\Malzahar.png")
        malzahar = tkinter.Button(master = self._championFrame, image = malzaharPhoto, command = lambda : self._setChampion("Malzahar", "Malzahar"))
        malzahar.image = malzaharPhoto
        malzahar.pack(side = "left")

        maokaiPhoto = tkinter.PhotoImage(file = "League Pictures\Maokai.png")
        maokai = tkinter.Button(master = self._championFrame, image = maokaiPhoto, command = lambda : self._setChampion("Maokai", "Maokai"))
        maokai.image = maokaiPhoto
        maokai.pack(side = "left")

        masterYiPhoto = tkinter.PhotoImage(file = "League Pictures\MasterYi.png")
        masterYi = tkinter.Button(master = self._championFrame, image = masterYiPhoto, command = lambda : self._setChampion("Master Yi", "Master Yi"))
        masterYi.image = masterYiPhoto
        masterYi.pack(side = "left")

        missFortunePhoto = tkinter.PhotoImage(file = "League Pictures\MissFortune.png")
        missFortune = tkinter.Button(master = self._championFrame, image = missFortunePhoto, command = lambda : self._setChampion("Miss Fortune", "MissFortune"))
        missFortune.image = missFortunePhoto
        missFortune.pack(side = "left")

        mordekaiserPhoto = tkinter.PhotoImage(file = "League Pictures\Mordekaiser.png")
        mordekaiser = tkinter.Button(master = self._championFrame, image = mordekaiserPhoto, command = lambda : self._setChampion("Mordekaiser", "Mordekaiser"))
        mordekaiser.image = mordekaiserPhoto
        mordekaiser.pack(side = "left")

        morganaPhoto = tkinter.PhotoImage(file = "League Pictures\Morgana.png")
        morgana = tkinter.Button(master = self._championFrame, image = morganaPhoto, command = lambda : self._setChampion("Morgana", "Morgana"))
        morgana.image = morganaPhoto
        morgana.pack(side = "left")
            
    def _createNChampionButtons(self):
        #called in _championFillMidFrames()
        #creates the buttons for champions starting with N
        self._createChampionFrame()

        namiPhoto = tkinter.PhotoImage(file = "League Pictures/Nami.png")
        nami = tkinter.Button(master = self._championFrame, image = namiPhoto, command = lambda : self._setChampion("Nami", "Nami"))
        nami.image = namiPhoto
        nami.pack(side = "left")

        nasusPhoto = tkinter.PhotoImage(file = "League Pictures/Nasus.png")
        nasus = tkinter.Button(master = self._championFrame, image = nasusPhoto, command = lambda : self._setChampion("Nasus", "Nasus"))
        nasus.image = nasusPhoto
        nasus.pack(side = "left")

        nautilusPhoto = tkinter.PhotoImage(file = "League Pictures/Nautilus.png")
        nautilus = tkinter.Button(master = self._championFrame, image = nautilusPhoto, command = lambda : self._setChampion("Nautilus", "Nautilus"))
        nautilus.image = nautilusPhoto
        nautilus.pack(side = "left")

        nidaleePhoto = tkinter.PhotoImage(file = "League Pictures/Nidalee.png")
        nidalee = tkinter.Button(master = self._championFrame, image = nidaleePhoto, command = lambda : self._setChampion("Nidalee", "Nidalee"))
        nidalee.image = nidaleePhoto
        nidalee.pack(side = "left")

        nocturnePhoto = tkinter.PhotoImage(file = "League Pictures/Nocturne.png")
        nocturne = tkinter.Button(master = self._championFrame, image = nocturnePhoto, command = lambda : self._setChampion("Nocturne", "Nocturne"))
        nocturne.image = nocturnePhoto
        nocturne.pack(side = "left")

        nunuPhoto = tkinter.PhotoImage(file = "League Pictures/Nunu.png")
        nunu = tkinter.Button(master = self._championFrame, image = nunuPhoto, command = lambda : self._setChampion("Nunu", "Nunu"))
        nunu.image = nunuPhoto
        nunu.pack(side = "left")
            
    def _createOChampionButtons(self):
        #called in _championFillMidFrames()
        #creates the buttons for champions starting with O
        self._createChampionFrame()

        olafPhoto = tkinter.PhotoImage(file = "League Pictures\Olaf.png")
        olaf = tkinter.Button(master = self._championFrame, image = olafPhoto, command = lambda : self._setChampion("Olaf", "Olaf"))
        olaf.image = olafPhoto
        olaf.pack(side = "left")

        oriannaPhoto = tkinter.PhotoImage(file = "League Pictures\Orianna.png")
        orianna = tkinter.Button(master = self._championFrame, image = oriannaPhoto, command = lambda : self._setChampion("Orianna", "Orianna"))
        orianna.image = oriannaPhoto
        orianna.pack(side = "left")
            
    def _createPChampionButtons(self):
        #called in _championFillMidFrames()
        #creates the buttons for champions starting with P
        self._createChampionFrame()

        pantheonPhoto = tkinter.PhotoImage(file = "League Pictures\Pantheon.png")
        pantheon = tkinter.Button(master = self._championFrame, image = pantheonPhoto, command = lambda : self._setChampion("Pantheon", "Pantheon"))
        pantheon.image = pantheonPhoto
        pantheon.pack(side = "left")

        poppyPhoto = tkinter.PhotoImage(file = "League Pictures\Poppy.png")
        poppy = tkinter.Button(master = self._championFrame, image = poppyPhoto, command = lambda : self._setChampion("Poppy", "Poppy"))
        poppy.image = poppyPhoto
        poppy.pack(side = "left")        
            
    def _createQChampionButtons(self):
        #called in _championFillBotFrames()
        #creates the buttons for champions starting with Q
        self._createChampionFrame()

        quinnPhoto = tkinter.PhotoImage(file = "League Pictures\Quinn.png")
        quinn = tkinter.Button(master = self._championFrame, image = quinnPhoto, command = lambda : self._setChampion("Quinn", "Quinn"))
        quinn.image = quinnPhoto
        quinn.pack(side = "left")
            
    def _createRChampionButtons(self):
        #called in _championFillBotFrames()
        #creates the buttons for champions starting with R
        self._createChampionFrame()

        rammusPhoto = tkinter.PhotoImage(file = "League Pictures\Rammus.png")
        rammus = tkinter.Button(master = self._championFrame, image = rammusPhoto, command = lambda : self._setChampion("Rammus", "Rammus"))
        rammus.image = rammusPhoto
        rammus.pack(side = "left")

        reksaiPhoto = tkinter.PhotoImage(file = "League Pictures\RekSai.png")
        reksai = tkinter.Button(master = self._championFrame, image = reksaiPhoto, command = lambda : self._setChampion("Rek'Sai", "RekSai"))
        reksai.image = reksaiPhoto
        reksai.pack(side = "left")

        renektonPhoto = tkinter.PhotoImage(file = "League Pictures\Renekton.png")
        renekton = tkinter.Button(master = self._championFrame, image = renektonPhoto, command = lambda : self._setChampion("Renekton", "Renekton"))
        renekton.image = renektonPhoto
        renekton.pack(side = "left")

        rengarPhoto = tkinter.PhotoImage(file = "League Pictures\Rengar.png")
        rengar = tkinter.Button(master = self._championFrame, image = rengarPhoto, command = lambda : self._setChampion("Rengar", "Rengar"))
        rengar.image = rengarPhoto
        rengar.pack(side = "left")

        rivenPhoto = tkinter.PhotoImage(file = "League Pictures\Riven.png")
        riven = tkinter.Button(master = self._championFrame, image = rivenPhoto, command = lambda : self._setChampion("Riven", "Riven"))
        riven.image = rivenPhoto
        riven.pack(side = "left")

        rumblePhoto = tkinter.PhotoImage(file = "League Pictures\Rumble.png")
        rumble = tkinter.Button(master = self._championFrame, image = rumblePhoto, command = lambda : self._setChampion("Rumble", "Rumble"))
        rumble.image = rumblePhoto
        rumble.pack(side = "left")

        ryzePhoto = tkinter.PhotoImage(file = "League Pictures\Ryze.png")
        ryze = tkinter.Button(master = self._championFrame, image = ryzePhoto, command = lambda : self._setChampion("Ryze", "Ryze"))
        ryze.image = ryzePhoto
        ryze.pack(side = "left")
            
    def _createSChampionButtons(self):
        #called in _championFillBotFrames()
        #creates the buttons for champions starting with S
        self._createChampionFrame()

        sejuaniPhoto = tkinter.PhotoImage(file = "League Pictures\Sejuani.png")
        sejuani = tkinter.Button(master = self._championFrame, image = sejuaniPhoto, command = lambda : self._setChampion("Sejuani", "Sejuani"))
        sejuani.image = sejuaniPhoto
        sejuani.pack(side = "left")

        shacoPhoto = tkinter.PhotoImage(file = "League Pictures\Shaco.png")
        shaco = tkinter.Button(master = self._championFrame, image = shacoPhoto, command = lambda : self._setChampion("Shaco", "Shaco"))
        shaco.image = shacoPhoto
        shaco.pack(side = "left")

        shenPhoto = tkinter.PhotoImage(file = "League Pictures\Shen.png")
        shen = tkinter.Button(master = self._championFrame, image = shenPhoto, command = lambda : self._setChampion("Shen", "Shen"))
        shen.image = shenPhoto
        shen.pack(side = "left")

        shyvanaPhoto = tkinter.PhotoImage(file = "League Pictures\Shyvana.png")
        shyvana = tkinter.Button(master = self._championFrame, image = shyvanaPhoto, command = lambda : self._setChampion("Shyvana", "Shyvana"))
        shyvana.image = shyvanaPhoto
        shyvana.pack(side = "left")

        singedPhoto = tkinter.PhotoImage(file = "League Pictures\Singed.png")
        singed = tkinter.Button(master = self._championFrame, image = singedPhoto, command = lambda : self._setChampion("Singed", "Singed"))
        singed.image = singedPhoto
        singed.pack(side = "left")

        sionPhoto = tkinter.PhotoImage(file = "League Pictures\Sion.png")
        sion = tkinter.Button(master = self._championFrame, image = sionPhoto, command = lambda : self._setChampion("Sion", "Sion"))
        sion.image = sionPhoto
        sion.pack(side = "left")

        sivirPhoto = tkinter.PhotoImage(file = "League Pictures\Sivir.png")
        sivir = tkinter.Button(master = self._championFrame, image = sivirPhoto, command = lambda : self._setChampion("Sivir", "Sivir"))
        sivir.image = sivirPhoto
        sivir.pack(side = "left")

        skarnerPhoto = tkinter.PhotoImage(file = "League Pictures\Skarner.png")
        skarner = tkinter.Button(master = self._championFrame, image = skarnerPhoto, command = lambda : self._setChampion("Skarner", "Skarner"))
        skarner.image = skarnerPhoto
        skarner.pack(side = "left")

        sonaPhoto = tkinter.PhotoImage(file = "League Pictures\Sona.png")
        sona = tkinter.Button(master = self._championFrame, image = sonaPhoto, command = lambda : self._setChampion("Sona", "Sona"))
        sona.image = sonaPhoto
        sona.pack(side = "left")

        sorakaPhoto = tkinter.PhotoImage(file = "League Pictures\Soraka.png")
        soraka = tkinter.Button(master = self._championFrame, image = sorakaPhoto, command = lambda : self._setChampion("Soraka", "Soraka"))
        soraka.image = sorakaPhoto
        soraka.pack(side = "left")

        swainPhoto = tkinter.PhotoImage(file = "League Pictures\Swain.png")
        swain = tkinter.Button(master = self._championFrame, image = swainPhoto, command = lambda : self._setChampion("Swain", "Swain"))
        swain.image = swainPhoto
        swain.pack(side = "left")

        syndraPhoto = tkinter.PhotoImage(file = "League Pictures\Syndra.png")
        syndra = tkinter.Button(master = self._championFrame, image = syndraPhoto, command = lambda : self._setChampion("Syndra", "Syndra"))
        syndra.image = syndraPhoto
        syndra.pack(side = "left")
            
    def _createTChampionButtons(self):
        #called in _championFillBotFrames()
        #creates the buttons for champions starting with T
        self._createChampionFrame()

        tahmKenchPhoto = tkinter.PhotoImage(file = "League Pictures\TahmKench.png")
        tahmKench = tkinter.Button(master = self._championFrame, image = tahmKenchPhoto, command = lambda : self._setChampion("Tahm Kench", "TahmKench"))
        tahmKench.image = tahmKenchPhoto
        tahmKench.pack(side = "left")

        talonPhoto = tkinter.PhotoImage(file = "League Pictures\Talon.png")
        talon = tkinter.Button(master = self._championFrame, image = talonPhoto, command = lambda : self._setChampion("Talon", "Talon"))
        talon.image = talonPhoto
        talon.pack(side = "left")

        taricPhoto = tkinter.PhotoImage(file = "League Pictures\Taric.png")
        taric = tkinter.Button(master = self._championFrame, image = taricPhoto, command = lambda : self._setChampion("Taric", "Taric"))
        taric.image = taricPhoto
        taric.pack(side = "left")

        teemoPhoto = tkinter.PhotoImage(file = "League Pictures\Teemo.png")
        teemo = tkinter.Button(master = self._championFrame, image = teemoPhoto, command = lambda : self._setChampion("Teemo", "Teemo"))
        teemo.image = teemoPhoto
        teemo.pack(side = "left")

        threshPhoto = tkinter.PhotoImage(file = "League Pictures\Thresh.png")
        thresh = tkinter.Button(master = self._championFrame, image = threshPhoto, command = lambda : self._setChampion("Thresh", "Thresh"))
        thresh.image = threshPhoto
        thresh.pack(side = "left")

        tristanaPhoto = tkinter.PhotoImage(file = "League Pictures\Tristana.png")
        tristana = tkinter.Button(master = self._championFrame, image = tristanaPhoto, command = lambda : self._setChampion("Tristana", "Tristana"))
        tristana.image = tristanaPhoto
        tristana.pack(side = "left")

        trundlePhoto = tkinter.PhotoImage(file = "League Pictures\Trundle.png")
        trundle = tkinter.Button(master = self._championFrame, image = trundlePhoto, command = lambda : self._setChampion("Trundle", "Trundle"))
        trundle.image = trundlePhoto
        trundle.pack(side = "left")

        tryndamerePhoto = tkinter.PhotoImage(file = "League Pictures\Tryndamere.png")
        tryndamere = tkinter.Button(master = self._championFrame, image = tryndamerePhoto, command = lambda : self._setChampion("Tryndamere", "Tryndamere"))
        tryndamere.image = tryndamerePhoto
        tryndamere.pack(side = "left")

        twistedFatePhoto = tkinter.PhotoImage(file = "League Pictures\TwistedFate.png")
        twistedFate = tkinter.Button(master = self._championFrame, image = twistedFatePhoto, command = lambda : self._setChampion("Twisted Fate", "TwistedFate"))
        twistedFate.image = twistedFatePhoto
        twistedFate.pack(side = "left")

        twitchPhoto = tkinter.PhotoImage(file = "League Pictures\Twitch.png")
        twitch = tkinter.Button(master = self._championFrame, image = twitchPhoto, command = lambda : self._setChampion("Twitch", "Twitch"))
        twitch.image = twitchPhoto
        twitch.pack(side = "left")
            
    def _createUChampionButtons(self):
        #called in _championFillBotFrames()
        #creates the buttons for champions starting with U
        self._createChampionFrame()

        udyrPhoto = tkinter.PhotoImage(file = "League Pictures/Udyr.png")
        udyr = tkinter.Button(master = self._championFrame, image = udyrPhoto, command = lambda : self._setChampion("Udyr", "Udyr"))
        udyr.image = udyrPhoto
        udyr.pack(side = "left")

        urgotPhoto = tkinter.PhotoImage(file = "League Pictures/Urgot.png")
        urgot = tkinter.Button(master = self._championFrame, image = urgotPhoto, command = lambda : self._setChampion("Urgot", "Urgot"))
        urgot.image = urgotPhoto
        urgot.pack(side = "left")
            
    def _createVChampionButtons(self):
        #called in _championFillBotFrames()
        #creates the buttons for champions starting with V
        self._createChampionFrame()

        varusPhoto = tkinter.PhotoImage(file = "League Pictures\Varus.png")
        varus = tkinter.Button(master = self._championFrame, image = varusPhoto, command = lambda : self._setChampion("Varus", "Varus"))
        varus.image = varusPhoto
        varus.pack(side = "left")

        vaynePhoto = tkinter.PhotoImage(file = "League Pictures\Vayne.png")
        vayne = tkinter.Button(master = self._championFrame, image = vaynePhoto, command = lambda : self._setChampion("Vayne", "Vayne"))
        vayne.image = vaynePhoto
        vayne.pack(side = "left")

        veigarPhoto = tkinter.PhotoImage(file = "League Pictures\Veigar.png")
        veigar = tkinter.Button(master = self._championFrame, image = veigarPhoto, command = lambda : self._setChampion("Veigar", "Veigar"))
        veigar.image = veigarPhoto
        veigar.pack(side = "left")

        velkozPhoto = tkinter.PhotoImage(file = "League Pictures\Velkoz.png")
        velkoz = tkinter.Button(master = self._championFrame, image = velkozPhoto, command = lambda : self._setChampion("Vel'Koz", "Velkoz"))
        velkoz.image = velkozPhoto
        velkoz.pack(side = "left")

        viPhoto = tkinter.PhotoImage(file = "League Pictures\Vi.png")
        vi = tkinter.Button(master = self._championFrame, image = viPhoto, command = lambda : self._setChampion("Vi", "Vi"))
        vi.image = viPhoto
        vi.pack(side = "left")

        viktorPhoto = tkinter.PhotoImage(file = "League Pictures\Viktor.png")
        viktor = tkinter.Button(master = self._championFrame, image = viktorPhoto, command = lambda : self._setChampion("Viktor", "Viktor"))
        viktor.image = viktorPhoto
        viktor.pack(side = "left")

        vladimirPhoto = tkinter.PhotoImage(file = "League Pictures\Vladimir.png")
        vladimir = tkinter.Button(master = self._championFrame, image = vladimirPhoto, command = lambda : self._setChampion("Vladimir", "Vladimir"))
        vladimir.image = vladimirPhoto
        vladimir.pack(side = "left")

        volibearPhoto = tkinter.PhotoImage(file = "League Pictures\Volibear.png")
        volibear = tkinter.Button(master = self._championFrame, image = volibearPhoto, command = lambda : self._setChampion("Volibear", "Volibear"))
        volibear.image = volibearPhoto
        volibear.pack(side = "left")
            
    def _createWChampionButtons(self):
        #called in _championFillBotFrames()
        #creates the buttons for champions starting with W
        self._createChampionFrame()

        warwickPhoto = tkinter.PhotoImage(file = "League Pictures\Warwick.png")
        warwick = tkinter.Button(master = self._championFrame, image = warwickPhoto, command = lambda : self._setChampion("Warwick", "Warwick"))
        warwick.image = warwickPhoto
        warwick.pack(side = "left")

        wukongPhoto = tkinter.PhotoImage(file = "League Pictures\MonkeyKing.png")
        wukong = tkinter.Button(master = self._championFrame, image = wukongPhoto, command = lambda : self._setChampion("Wukong", "MonkeyKing"))
        wukong.image = wukongPhoto
        wukong.pack(side = "left")
            
    def _createXChampionButtons(self):
        #called in _championFillBotFrames()
        #creates the buttons for champions starting with X
        self._createChampionFrame()

        xerathPhoto = tkinter.PhotoImage(file = "League Pictures\Xerath.png")
        xerath = tkinter.Button(master = self._championFrame, image = xerathPhoto, command = lambda : self._setChampion("Xerath", "Xerath"))
        xerath.image = xerathPhoto
        xerath.pack(side = "left")

        xinZhaoPhoto = tkinter.PhotoImage(file = "League Pictures\XinZhao.png")
        xinZhao = tkinter.Button(master = self._championFrame, image = xinZhaoPhoto, command = lambda : self._setChampion("Xin Zhao", "XinZhao"))
        xinZhao.image = xinZhaoPhoto
        xinZhao.pack(side = "left")
            
    def _createYChampionButtons(self):
        #called in _championFillBotBotFrames()
        #creates the buttons for champions starting with Y
        self._createChampionFrame()

        yasuoPhoto = tkinter.PhotoImage(file = "League Pictures\Yasuo.png")
        yasuo = tkinter.Button(master = self._championFrame, image = yasuoPhoto, command = lambda : self._setChampion("Yasuo", "Yasuo"))
        yasuo.image = yasuoPhoto
        yasuo.pack(side = "left")

        yorickPhoto = tkinter.PhotoImage(file = "League Pictures\Yorick.png")
        yorick = tkinter.Button(master = self._championFrame, image = yorickPhoto, command = lambda : self._setChampion("Yorick", "Yorick"))
        yorick.image = yorickPhoto
        yorick.pack(side = "left")
            
    def _createZChampionButtons(self):
        #called in _championFillBotBotFrames()
        #creates the buttons for champions starting with Z
        self._createChampionFrame()

        zacPhoto = tkinter.PhotoImage(file = "League Pictures\Zac.png")
        zac = tkinter.Button(master = self._championFrame, image = zacPhoto, command = lambda : self._setChampion("Zac", "Zac"))
        zac.image = zacPhoto
        zac.pack(side = "left")

        zedPhoto = tkinter.PhotoImage(file = "League Pictures\Zed.png")
        zed = tkinter.Button(master = self._championFrame, image = zedPhoto, command = lambda : self._setChampion("Zed", "Zed"))
        zed.image = zedPhoto
        zed.pack(side = "left")

        ziggsPhoto = tkinter.PhotoImage(file = "League Pictures\Ziggs.png")
        ziggs = tkinter.Button(master = self._championFrame, image = ziggsPhoto, command = lambda : self._setChampion("Ziggs", "Ziggs"))
        ziggs.image = ziggsPhoto
        ziggs.pack(side = "left")

        zileanPhoto = tkinter.PhotoImage(file = "League Pictures\Zilean.png")
        zilean = tkinter.Button(master = self._championFrame, image = zileanPhoto, command = lambda : self._setChampion("Zilean", "Zilean"))
        zilean.image = zileanPhoto
        zilean.pack(side = "left")

        zyraPhoto = tkinter.PhotoImage(file = "League Pictures\Zyra.png")
        zyra = tkinter.Button(master = self._championFrame, image = zyraPhoto, command = lambda : self._setChampion("Zyra", "Zyra"))
        zyra.image = zyraPhoto
        zyra.pack(side = "left")

#Rune Button Creation Functions

    def _createQuintButtons():
        self._createStackingFrames()
        #energy = tkinter.Button(master = self._topFrame, text = Energy, font = ("Helvetica", 30), command = lambda : self._setQuints

    def _createSealButtons():
        self._createStackingFrames()

    def _createGlyphButtons():
        self._createStackingFrames()

    def _createMarkButtons():
        self._createStackingFrames()
        
   
if __name__ == '__main__':
    LeagueProgram().start()
