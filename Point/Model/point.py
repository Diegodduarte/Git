class Point():

    def __init__(self):
        self.x = 0
        self.y = 0


    def SolicitarPontos(self):
        self.x = float(input('Informe o Ponto x'))
        self.y = float(input('Informe o Ponto y'))

    def __str__(self):
        result = 'Ponto 1' + str(self.x)
        result += 'Ponto 2' + str(self.y)
        return result

    def __add__(self,other):
        P1x = self.x
        P1y = self.y
        P2x = other.x
        P2y = other.y

        NovoPonto = Point()

        NovoPonto.x = P1x + P2x
        NovoPonto.Y = P1y + P2y


        return (NovoPonto)




