import pandas as pd
df = pd.read_csv('ClassicDisco.csv')

#Filtrar musicas lançadas depoi de 1980 e mostre apenas as colunas "year" e "Track"
print(df[df['Year'] > 1980][['Year', 'Track']])