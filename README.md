# Ames_House_Prices_Predict

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