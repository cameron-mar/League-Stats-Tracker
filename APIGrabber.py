import requests
import math
import string

class Setup:
    def checkRegion(region):
        #I use this to check if the region actually exists
        URL = "http://status.leagueoflegends.com/shards/" + region
        response = requests.get(URL)
        return response.json()

    def requestChampion(region, championName, APIKey):
        #I use this to find the champion and takes its ID
        URL = "https://global.api.pvp.net/api/lol/static-data/" + region + "/v1.2/champion?locale=en_US&api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

    def requestChampionStats(region, ID, APIKey):
        #I use this to retrieve the stats on a champion after retrieving its ID from the function above
        URL = "https://global.api.pvp.net/api/lol/static-data/" + region + "/v1.2/champion/" + ID + "?locale=en_US&champData=stats&api_key=" + APIKey
        response = requests.get(URL)
        return response.json()

    def requestItem(region, APIKey):
        #I use this to go through the list of item IDs to find the itemName in one of the IDs
        URL = "https://global.api.pvp.net/api/lol/static-data/" + region + "/v1.2/item?itemListData=stats&api_key=" +APIKey
        response = requests.get(URL)
        return response.json()

    def requestItemID(json, itemName):
        for i in json["data"]:
            if json["data"][i]["name"] == itemName:
                return json["data"][i]["id"]

    def printChampionStats(json, level = 1):
        print("\n" + json["name"], "---", "Level", str(level))
        print("-"*30)
        printArmor(json, level)
        printAttackDamage(json, level)
        printAttackRange(json, level)
        printAttackSpeed(json, level)
        printCritChance(json, level)
        printHP(json, level)
        printHPRegen(json, level)
        printMovementSpeed(json, level)
        printMP(json, level)
        printMPRegen(json, level)
        printMagicResist(json, level)
        print("\nNote: HP Regen is every 5 seconds\n")

    def printArmor(json, level):
        baseArmor = json["stats"]["armor"]
        armorPerLevel = json["stats"]["armorperlevel"]
        armor = baseArmor + armorPerLevel*(level-1)
        print("{:16}{:}".format("Armor", round(armor)))

    def printAttackDamage(json, level):
        baseAttackDamage = json["stats"]["attackdamage"]
        attackDamagePerLevel = json["stats"]["attackdamageperlevel"]
        attackDamage = baseAttackDamage + attackDamagePerLevel*(level-1)
        print("{:16}{:}".format("Attack Damage", round(attackDamage)))

    def printAttackRange(json, level):
        baseAttackRange = json["stats"]["attackrange"]
        print("{:16}{:}".format("Attack Range" , round(baseAttackRange)))

    def printAttackSpeed(json, level):
        attackSpeedOffset = json["stats"]["attackspeedoffset"]
        attackSpeedPerLevel = json["stats"]["attackspeedperlevel"]/100 #the attack speed per level is a percentage so 1.5 is actually 1.5%
        baseAttackSpeed = calculateBaseAttackSpeed(attackSpeedOffset)
        attackSpeed = baseAttackSpeed + baseAttackSpeed * (attackSpeedPerLevel*(level-1))
        print("{:16}{:.3g}".format("Attack Speed", attackSpeed))

    def printCritChance(json, level):
        baseCritChance = json["stats"]["crit"]
        print("{:16}{:}%".format("Crit Chance", round(baseCritChance)))

    def printHP(json, level):
        baseHP = json["stats"]["hp"]
        HPPerLevel = json["stats"]["hpperlevel"]
        HP = baseHP + HPPerLevel * (level-1)
        print("{:16}{:}".format("HP", round(HP)))

    def printHPRegen(json, level):
        baseHPRegen = json["stats"]["hpregen"]
        HPRegenPerLevel = json["stats"]["hpregenperlevel"]
        HPRegen = baseHPRegen + HPRegenPerLevel * (level-1)
        print("{:16}{:}".format("HP Regen", round(HPRegen)))

    def printMovementSpeed(json, level):
        baseMovementSpeed = json["stats"]["movespeed"]
        print("{:16}{:}".format("Movement Speed", round(baseMovementSpeed)))

    def printMP(json, level):
        baseMP = json["stats"]["mp"]
        MPPerLevel = json["stats"]["mpperlevel"]
        MP = baseMP + MPPerLevel * (level-1)
        print("{:16}{:}".format("MP", round(MP)))

    def printMPRegen(json, level):
        baseMPRegen = json["stats"]["mpregen"]
        MPRegenPerLevel = json["stats"]["mpregenperlevel"]
        MPRegen = baseMPRegen + MPRegenPerLevel * (level-1)
        print("{:16}{:}".format("MP Regen", round(MPRegen)))

    def printMagicResist(json, level):
        baseMagicResist = json["stats"]["spellblock"]
        magicResistPerLevel = json["stats"]["spellblockperlevel"]
        magicResist = baseMagicResist + magicResistPerLevel * (level-1)
        print("{:16}{:}".format("Magic Resist", round(magicResist)))
        
    def calculateBaseAttackSpeed(offset):
        #the method name
        num = 0.625 / (1 + offset)
        return num

    def createChampionKey(name):
        #after taking in a name from the user, I convert it into the key used in the api
        name = name.lower().title().strip()
        if name == "Wukong": #had to hardcode
            name = "MonkeyKing"
        elif name.lower() == "fiddlesticks": #had to hardcode
            name = "FiddleSticks"
        elif name == "Jarvan Iv": #somewhat avoidable, but easier this way
            name = "JarvanIV"
        elif " " in name: #if the name has two words, I condense it into one
            name = name.replace(" ","")
        elif "'" in name: #if the name has an apostrophe, I take it out and condense the two names into one
            name = name.replace("'","")
            if name[0] == "V" or name[0] == "C": #checks for Cho'Gath and Vel'Koz because Rito is inconsistent on naming
                name = name.lower().title()
        return name

    def createItemKey(name):
        name = string.capwords(name)
        print(name)
        return name
        
    def main():
        APIKey = "ae67cad8-39bb-4e95-9e8d-8fa94c56e51e"
        print("\nEnter your region to get started!")
        print("NA EUW EUNE LAN LAS BR OCE PBE TR RU\n")

        while True: #asking user for their region
            try:
                region = (str)(input('Type in one of the regions above: ')).strip().lower()
                checkRegion(region)
            except:
                print("\nThis region was not found.\nPlease try again.\n")
            else:
                break
            
        while True: #asking user for the champion name
            try:
                championInput = (str)(input("\nNote: Please type in spaces and apostrophes for certain champions.\nType in a champion's name and I will look it up: "))
                championKey = createChampionKey(championInput) 
                championResponse = requestChampion(region, championKey, APIKey)
                championID = str(championResponse['data'][championKey]['id'])
            except:
                print("\nThis champion doesn't exist or was spelled incorrectly.\nPlease try again.")
            else:
                break
            
        championStatsResponse = requestChampionStats(region, championID, APIKey)
        printChampionStats(championStatsResponse)

        while True: #taking in the level of the champion and printing results
            level = input("What level do you want to see this champion's stats? ").strip()
            try: #checks to see if this is a number
                int(level)
            except: #if its not a number, we redo the process
                print("\nPlease enter a number.\n")
                continue
            if int(level) < 1 or int(level) > 18: #if the level isn't 1-18
                print("\nChampions can't reach this level.\nPlease try again.\n")
                continue
            
            while True: #checking if the user has items
                checkItem = (str)(input("Do you have any(more) items? Y or N: ")).upper() #now we see if they have items
                if checkItem == "Y": #Has items
                    while True: #asking the user to input items
                        itemInput = (str)(input("\nPlease input the name of one item:\n"))
                        itemKey = createItemKey(itemInput)
                        try:
                            itemResponse = requestItem(region, APIKey)
                            itemID = requestItemID(itemResponse, itemKey)
                            print(itemID)
                            
                        except:
                            print("Invalid item name.\nPlease try again.\n")
                        

                elif checkItem == "N": #Don't have items
                    break
                else: #Didn't type Y or N
                    print("\nInvalid response.\nPlease try again.\n")
                    continue

            printChampionStats(championStatsResponse, int(level))
            
            while True:#checking if the user wants to continue to use the program
                response = (str)(input("Do you want to continue? Y or N: ")).upper()
                if response == "N": #Don't want to continue
                    print("\nThank you for using my program!")
                    return
                elif response == "Y": #Do want to continue
                    break
                else: #Didn't type Y or N
                    print("\nInvalid response.\nPlease try again.\n")
            


