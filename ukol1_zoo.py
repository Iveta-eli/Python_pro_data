
#--------------------------
#   TŘÍDA ZVÍŘE
#--------------------------

class Zvire:
    def __init__(self, jmeno: str, druh: str, vaha: int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha

    def __str__(self):
        #return f"Název zvířete: {self.druh}, jméno: {self.jmeno}, váha: {self.vaha}."
        return f"Jméno zvířete: {self.jmeno}, druh: {self.druh}, váha. {self.vaha} kg"

    def export_to_dict(self):
        return {
            'jmeno': self.jmeno,
            'druh': self.druh,
            'vaha': self.vaha
        }
    
zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},
]

seznam_zvirat = [Zvire(zvire['jmeno'], zvire['druh'], zvire['vaha']) for zvire in zvirata_dict]
for zvire in seznam_zvirat:
    print(zvire)

pavouk = Zvire(jmeno='Adolf', druh='Tarantule Velká', vaha=0.1)
pavouk_export = pavouk.export_to_dict()

print(pavouk)
print(pavouk.export_to_dict())

assert pavouk_export['jmeno'] == 'Adolf'
assert pavouk_export['druh'] == 'Tarantule Velká'
assert pavouk_export['vaha'] == 0.1


value = getattr(zvire, "vaha")


#-------------------------
#   TŘÍDA ZAMĚSTNANEC
#-------------------------

class Zamestnanec:
    def __init__(self, cele_jmeno: str, rocni_plat: int, pozice: str):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice

    def __str__(self):
        return f"Jméno zaměstnance: {self.cele_jmeno}, roční plat: {self.rocni_plat}, pozice: {self.pozice}."

    def ziskej_inicialy(self):
        jmena = self.cele_jmeno.split()
        if len(jmena) == 2:
            return f"{jmena[0][0]}.{jmena[1][0]}."
        else:
            return "Jméno se musí skládat z jednoho křestního jména a jednoho příjmení."
    
# OVĚŘENÍ SPRÁVNOSTI FCE: def ziskej_inicialy(self):
# pokusny_zamestnanec = Zamestnanec("Iveta Eliášková", 50_000, "Manažer")
# print(pokusny_zamestnanec)
# print("Iniciály: ", pokusny_zamestnanec.ziskej_inicialy())
#---------------

zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

seznam_zamestnancu = [Zamestnanec(zamestnanec["cele_jmeno"], zamestnanec["rocni_plat"], zamestnanec["pozice"]) for zamestnanec in zamestnanci_dict]
for zamestnanec in seznam_zamestnancu:
    print(zamestnanec)


#--------------------------
#   TŘÍDA ŘEDITEL
#--------------------------
"""
#když dědím z jiné třídy, tak musím zkopírovat: def __init__(všechny atributy, pak sem přidám nový atribut) toto píšu hned
# pod třídu, pak musím ještě napsat: super().__init__(sem dám všechny atributy z děděné třídy, nedávám sem přidaný atribut)

class Reditel(Zamestnanec):
                #cele_jmeno: str, rocni_plat: int, pozice: str
    def __init__(self, cele_jmeno: str, rocni_plat: int, pozice='Reditel', oblibene_zvire= Zvire):
        super().__init__(jmeno, rocni_plat, pozice='Reditel')
        self.oblibene_zvire = oblibene_zvire


#zvire = Zvire(jmeno="Tonda", druh="leguán", vaha="4kg")
zvire = Zvire()
reditel = Reditel(jmeno='Karel', rocni_plat=800_000, oblibene_zvire=Zvire)
print(reditel)
print(zvire)
assert reditel.pozice == 'Reditel'

assert isinstance(reditel.oblibene_zvire, Zvire) 
"""
class Reditel(Zvire, Zamestnanec):
    def __init__(self, jmeno: str, druh: str, vaha: int, cele_jmeno: str, rocni_plat: int, pozice='Reditel', oblibene_zvire= Zvire):
        Zvire.__init__(self, jmeno: str, druh: str, vaha: int)
        Zamestnanec.__init__(self, cele_jmeno, rocni_plat, pozice='Reditel')
        self.oblibene_zvire = oblibene_zvire

zvire = Zvire()
reditel = Reditel(jmeno='Karel', rocni_plat=800_000, oblibene_zvire=Zvire)
print(reditel)
print(zvire)
assert reditel.pozice == 'Reditel'

assert isinstance(reditel.oblibene_zvire, Zvire) 

"""
#--------------------------
#   TŘÍDA ZOO
#--------------------------

class Zoo(Zamestnanec, Zvire):
    def __init__(self, jmeno: str, adresa: str, reditel: Reditel, ):
        super().__init__(Zvire.vaha, Zamestnanec.cele_jmeno, pozice= reditel, zamestnanci= zamestnanci_dict, zvirata= zvirata_dict)
        # Vpravaé  Zvire.vaha, super().__init__(Zvire.vaha: int, Zamestnanec.cele_jmeno: str) 
        self.jmeno = jmeno
        self.adresa = adresa

        # self.rocni_plat = rocni_plat
        # self.pozice = pozice

    def __str__(self):
        return f"Název zoo: {self.jmeno}, adresa: {self.adresa}, pozice: {self.pozice}, seznam zaměstnanců {self.zamestnanci_dict }, seznam zvířat {self.zvirata}."   

    def vaha_vsech_zvirat_v_zoo(self):
        celkova_vaha = sum(zvire.vaha for zvire in self.zvira_dict)
        return celkova_vaha

    def mesicni_naklady_na_zamestnance(self):
        mesicni_naklady = sum(zamestnanec.rocni_plat / 12 for zamestnanec in self.zamestnanci)
        mesicni_naklady += self.reditel.rocni_plat / 12
        return mesicni_naklady



# Příklad použití třídy Zoo
zoo = Zoo(jmeno='ZOO Praha', adresa='U Trojského zámku 3/120')
# Příklad použití třídy Zoo 
#zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci_dict, zvirata_dict, zvire.vaha)
#zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci_dict, zvirata_dict)
# print(f"jmeno: {zoo.jmeno}")
#print(zoo)

# for zvire in seznam_zvirat:
#     print(f"Jméno: {zvire.jmeno}, Druh: {zvire.druh}, Váha: {zvire.vaha} kg")

# pavouk = Zvire(jmeno='Adolf', druh='Tarantule Velká', vaha=0.1)


# print(f"Ředitel: {zoo.reditel}")
#print(f"Celková váha zvířat v ZOO: {zoo.vaha()} kg")
# print(f"Měsíční náklady na zaměstnance: {zoo.mesicni_naklady_na_zamestnance()} Kč")

# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

# Zamestnanec class
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P.N.'

# Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

# Zoo class
zoologicka = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'jmeno') #nazev
# assert hasattr(zoo, 'adresa')
# assert hasattr(zoo, 'reditel')
# assert hasattr(zoo, 'zamestnanci')
# assert hasattr(zoo, 'zvirata')
# assert isinstance(zoo.nazev, str)
# assert isinstance(zoo.adresa, str)
# assert isinstance(zoo.reditel, Reditel)
# assert isinstance(zoo.zamestnanci, list)
# assert isinstance(zoo.zvirata, list)
# assert zoo.vaha_vsech_zvirat_v_zoo() == 150
# assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12

"""