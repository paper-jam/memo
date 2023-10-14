# ============ contect manager


# -- ===== contexte manager -> definir une fonction __enter__ et __exit__
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __enter__(self):
        return self  # !!!!!!!!! important

    #  parameters are used for exception
    def __exit__(self, exc_type, exc_val, traceback):
        pass

    def calcul_aire(self):
        return self.longueur * self.largeur


with Rectangle(6, 12) as r:
    aire = r.calcul_aire()
    print(f"L'aire d'un rectangle de {r.largeur}m par {r.longueur} est de {aire} m²")
