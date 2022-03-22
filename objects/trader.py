# Classe Trader 
class Trader:
    
    # Função de inicialização de valores
    def __init__(self):
        
        self.balance = 0            # Saldo
        self.profitLoss = 0         # Lucro/prejuizo

        self.positioned = False     # Posicionado?
        self.positionType = ''      # Tipo da posição
        self.positionPrice = 0      # Preço de entrada na operação

        self.lastPrice = 0          # Último preço do ativo
        self.spread = 10            # Spread padrao por entrada e saída (10 pontos).

        self.balancePlot = []       # Variação do saldo ao longo do tempo
        

    # Função para fechar posicão
    def closePosition(self):
        
        if self.positioned:                     # Se está posicionado então continua

            if self.positionType == 'BUY':      # Caculando o lucro/prejuizo no caso de uma compra
                self.profitLoss = (self.positionPrice - self.lastPrice) - self.spread

            elif self.positionType == 'SELL':   # Caculando o lucro/prejuizo no caso de uma venda
                self.profitLoss = (self.lastPrice - self.positionPrice) - self.spread
            
            self.balance += self.profitLoss     # Somando o valor do lucro/prejuizo ao saldo
            self.positionType = ''              # Zerando o tipo de posição
            self.positioned = False             # Posicionado igual falso
            self.positionPrice = 0              # Zerando o preço da posição
            self.profitLoss = 0                 # Zerando o lucro/prejuizo

##########################################################################################################
