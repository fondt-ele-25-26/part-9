

class VanDerPol:
    def __init__(self, mu):
        self.mu = mu
        
    def __call__(self, X, t):
        x, y = X
        dx = y
        dy = self.mu * (1 - x**2) * y - x
        return (dx, dy)