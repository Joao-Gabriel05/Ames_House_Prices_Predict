# Ames_House_Prices_Predict

# Relatório:
 O modelo alcançou um erro percentual médio de 13 % e um resíduo médio de R$ 17 153 no conjunto de teste, ao prever imóveis na faixa de R$ 100 000 a R$ 500 000. Esses resultados indicam que ele pode ser aplicado em cenários reais — respeitando as limitações descritas no `README.md`.

 Em particular, observou-se que o modelo tende a subperformar em casas de menor valor (por volta de R$ 100 000), com qualidade média e última reforma por volta de  2000 e 2005, apresentando aí maiores discrepâncias nas previsões.

 A principal feature na determinação do preço do imóvel é  `Gr.Liv.Area_log`, que faz sentido sendo que essa feature representa a soma do tamanho de todos os comodos da casa acima do solo. Outras que também são importantes são `Lot.Area_log` que representa o tamamnho do lot em metros quadrados e `Overall.Qual`, que é a qualidade da casa

Próximos passos:  acredito que ainda seja possível achar um modelo melhor, talvez fazer um ensamble de modelos lineares, incluindo outros modelos lineares mais robustos e até o próprio ElasticNet dado que o desempenho dele não foi tão pior que o do modelo linear. Talvez seja até interessante separar um modelo específico para prever valores menores de casas.

# Limitações:
O modelo foi treinado e validado somente em registros que atendem aos seguintes critérios:

- **Bairros**  
  Os seguintes bairros não foram inclusos no treinamento do modelo:
  `Blmngtn`, `Veenker`, `NPkVill`, `Blueste`, `Greens`, `GrnHill`, `Landmrk`

- **Banheiros**  
  - Número de banheiros > 0

- **Quartos**  
  - Número de quartos > 3

- **Cozinhas**  
  - Número de cozinhas ≥ 1 e ≤ 3

- **Faixa de Preço**  
  - Valor mínimo: R\$ 52 377,03  
  - Valor máximo: R\$ 528 901,65

- **Ano de Construção / Remodelação**  
  - Somente imóveis construídos ou reformados a partir de 1950