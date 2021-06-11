import numpy as np

class GaussianBandit(object):

    def __init__(self, k_arms=10):
        self.bandits_expectations = np.random.normal(0,1,k_arms)
    
    def gamble(self, action):
        """ação(int) -> recompensa(int)
        Recebe uma ação representando o bandit que será acionado, que devolve uma recompensa baseada em uma distribuição normal de desvio padrão 1 e média 0.
        """
        return np.random.normal(self.bandits_expectations[action], 1)