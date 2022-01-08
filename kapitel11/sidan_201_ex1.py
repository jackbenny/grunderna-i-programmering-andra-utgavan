class Hund(Husdjur):
    def __init__(self, namn, farg, ras, atit=0):
        Husdjur.__init__(self, namn=namn, farg=farg,
                    atit=atit, art="hund", laten="Voff")
        self.ras = ras

    def vilkenRas(self):
        return (self.namn + " är en " + self.ras)

class Katt(Husdjur):
    def __init__(self, namn, farg, ras, atit=0):
        Husdjur.__init__(self, namn=namn, farg=farg,
                    atit=atit, art="katt", laten="Mjau")
        self.ras = ras

    def vilkenRas(self):
        return (self.namn + " är en " + self.ras)
