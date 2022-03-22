# Classes
from objects.databaser import Database
from objects.trader import Trader

# Bibliotecas
from matplotlib import pyplot as plt
import pandas as pd
import neat
import os


# Variáveis Globais.
GENERATION = 0  # Geração atual.
TRADERS = []    # Lista de individuos.
NETS = []       # Lista de redes neurais.
GE = []         # Lista de algoritmos genéticos.


# Funçao para criar os indivíduos.
def population(genome, config):
    global TRADERS, NETS, GE

    for genome_id, genome in genome:

        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)     # Criando uma rede neural.
        TRADERS.append(Trader())                                    # Adicionando um indivíduo.
        NETS.append(net)                                            # Adicionando a rede neural.
        GE.append(genome)                                           # Adicionando o algoritimo genético.


# Função principal.
def main(genome, config):
    global GENERATION, TRADERS, NETS, GE
    
    db = Database()             # Criando o objeto db para manipulação do banco de dados.
    db.create()                 # Criando a entidade.

    population(genome, config)  # Funçao para criar os indivíduos.
    
    # TODO Importar os dados.
    
    while True: # Loop principal.
        
        GENERATION += 1         # Incrementando a geração

        # TODO Tratar os dados.        

        for i, trader in enumerate(TRADERS): # Loop secundário.
            
            inputs = ('a','b','c','d','e','f','g') # TODO Setar os inputs.

            outputs = NETS[i].activate(inputs) # Enviar os inputs para a rede neural e captar as saídas.

            # TODO Tratar as saídas.

        break 


##################################################################################################################


# Configurando a Rede Neural(Padrão).
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.run(main,1) # run('Função main', 'Quantidade de gerações')

# Iniciando a aplicação
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)


##################################################################################################################
