import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    tamanho = list(players.shape)
    return tamanho
