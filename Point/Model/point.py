class Point():

    def __init__(self,x,y,x2,y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

    def SolicitarPontos(x,y,x2,y2):
        x = float(input('Informe o primeiro Ponto x'))
        y = float(input('Informe o primeiro Ponto y'))
        x2 = float(input('Informe o segundo Ponto x'))
        y2 = float(input('Informe o segundo Ponto y'))

    def __add__(self,other):
        P1x = self.x
        P1y = self.y
        P2x = other.x
        P2y = other.Y

        SomaPontoX = P1x + P2x
        SomaPontoY = P1y + P2y

        NovoPonto.x = P1x + P2x
        NovoPonto.Y = P1y +P2y

        return (NovoPonto)




