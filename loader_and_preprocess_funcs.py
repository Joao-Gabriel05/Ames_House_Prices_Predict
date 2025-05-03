import pandas as pd
from typing import List, Optional
import numpy as np

def remove_outliers_iqr(
    df: pd.DataFrame,
    columns: Optional[List[str]] = None,
    multiplier: float = 1.5
) -> pd.DataFrame:
    """
    Remove outliers de um DataFrame usando o método IQR,
    imprimindo os limites e a quantidade de dados perdidos.

    Args:
        df: DataFrame de entrada.
        columns: lista de colunas numéricas nas quais aplicar a remoção.
                 Se None, usa todas as colunas numéricas do df.
        multiplier: fator para definir os limites (padrão 1.5).

    Returns:
        Um novo DataFrame sem as linhas que contenham outliers em qualquer
        das colunas especificadas.
    """
    original_count = len(df)

    if columns is None:
        columns = df.select_dtypes(include='number').columns.tolist()

    mask = pd.Series(True, index=df.index)

    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - multiplier * IQR
        upper_bound = Q3 + multiplier * IQR

        col_mask = df[col].between(lower_bound, upper_bound)
        removed_by_col = (~col_mask).sum()


        mask &= col_mask

    filtered_df = df.loc[mask].copy()
    removed_total = original_count - len(filtered_df)
    pct_removed = removed_total / original_count * 100



    return filtered_df


def load__data(data_dir='ames.csv'):
    
    csv_path = data_dir 
    df = pd.read_csv(csv_path)
    return df

def choose_feat(data,list):
    data= data[list]
    return data


def group_overall_qual(x):
    if x < 4:
        return 'Less than 4'
    elif x > 8:
        return 'Greater than 8'
    else:
        return str(x)
    
def group_rare_categories_auto(data, column, threshold=0.05, new_label='Other'):
    """
    Agrupa automaticamente categorias que aparecem menos que o threshold em 'Other'.
    """
    data = data.copy()
    proportions = data[column].value_counts(normalize=True)
    rare_labels = proportions[proportions < threshold].index.tolist()
    
    data[column] = data[column].apply(lambda x: new_label if x in rare_labels else x)
    
    return data

def preprocessor(data):
    ''''  
    Função para pré-processar os dados.
    '''
    columns = [
    'Lot.Area',
    'Lot.Frontage',
    'Gr.Liv.Area',
    'SalePrice'
]
    for col in columns:
        data[col + '_log'] = np.log10(data[col])
        data.drop(columns=[col], inplace=True)
        
    data = remove_outliers_iqr(data, columns=['SalePrice_log'], multiplier=1.8)
    data = remove_outliers_iqr(data, columns=['Lot.Area_log'], multiplier=1.8)
    data = remove_outliers_iqr(data, columns=['Gr.Liv.Area_log'], multiplier=1.8)
    
    data['Open.Porch.SF_bin'] = data['Open.Porch.SF'].apply(lambda x: 1 if x > 0 else 0)
    data.drop(columns=['Open.Porch.SF'], inplace=True)

    threshold = 0.01

    neigh_prop = data['Neighborhood'].value_counts(normalize=True)

    drop_neigh = neigh_prop[neigh_prop < threshold].index.tolist()
    data = data[~data['Neighborhood'].isin(drop_neigh)].copy()
    list = ['Foundation','Roof.Style','House.Style']
    
    for var in list:
        data=group_rare_categories_auto(data,var)
    
    data['Overall.Qual'] = data['Overall.Qual'].apply(group_overall_qual)
    
    data['Full.Bath'] = data['Full.Bath'].apply(lambda x: 'More than 2' if x > 2 else x)
    data = data[data['Full.Bath']!=0]
    
    data = data[data['TotRms.AbvGrd']>3]
    data['TotRms.AbvGrd'] = data['TotRms.AbvGrd'].apply(lambda x: 'More than 10' if x > 10 else x)
    
    data['Fireplaces'] = data['Fireplaces'].apply(lambda x: 'More than 1' if x > 1 else x)

    data['Heating.QC'] = data['Heating.QC'].apply(lambda x: 'Fa/Po' if x=='Fa' or x=='Po' else x)

    data = data[
        (data['Kitchen.AbvGr'] > 0) 
        & 
        (data['Kitchen.AbvGr'] < 3)
    ].copy()

    cols = ['Neighborhood', 'House.Style', 'Overall.Qual', 'Full.Bath',
        'TotRms.AbvGrd', 'Fireplaces', 'Foundation',
        'Roof.Style', 'Heating.QC','Open.Porch.SF_bin','Kitchen.AbvGr']

    data[cols] = data[cols].astype(str)
    data = data[data['Year.Remod.Add'] > 1950]

    return data
    