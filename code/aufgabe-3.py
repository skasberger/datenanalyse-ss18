import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def import_data(filename, encoding):

    df = pd.read_csv(filename, sep=';', decimal=',', encoding=encoding)
    return df


if __name__ == '__main__':

    df_nrw17 = import_data('../data/nrw17.csv', 'utf-8')
    df_nrw17['gkz'] = [int(gkz[1:]) for gkz in df_nrw17['gkz']]

    df_ages = import_data('../data/alter.csv', 'utf-8')
    df_nrw17 = pd.merge(df_nrw17, df_ages, how='left', on=['gkz', 'gkz'])

    df_households = import_data('../data/haushalte.csv', 'utf-8')
    df_nrw17 = pd.merge(df_nrw17, df_households, how='left', on=['gkz', 'gkz'])

    df_foreigners = import_data('../data/nationalitaet.csv', 'utf-8')
    df_nrw17 = pd.merge(df_nrw17, df_foreigners, how='left', on=['gkz', 'gkz'])

    df_nrw17.to_csv('../data/data.csv', sep=';', index=False, decimal=',')
