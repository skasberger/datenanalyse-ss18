import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def import_data(filename, encoding):

    df = pd.read_csv(filename, sep=';', decimal=',', encoding=encoding)
    return df


if __name__ == '__main__':

    df_nrw17 = import_data('../data/nrw17.csv', 'utf-8')
    df_nrw17['gkz'] = [int(gkz[1:]) for gkz in df_nrw17['gkz']]
    df_nrw17['wahlberechtigt_abs'] = df_nrw17['wahlberechtigt']
    df_nrw17['abgegeben_abs'] = df_nrw17['abgegeben']
    df_nrw17['ungueltig_rel'] = df_nrw17.apply(lambda row: round(row['ungueltig'] * 100 / row['abgegeben'], 2), axis=1)
    df_nrw17['gueltig_abs'] = df_nrw17['gueltig']
    df_nrw17['wahlberechtigt'] = df_nrw17['wahlberechtigt']

    df_nrw17['spoe_rel'] = df_nrw17.apply(lambda row: round(row['spoe'] * 100 / row['gueltig'], 2), axis=1)
    df_nrw17['oevp_abs'] = df_nrw17['oevp']
    df_nrw17['fpoe_rel'] = df_nrw17.apply(lambda row: round(row['fpoe'] * 100 / row['gueltig'], 2), axis=1)
    df_nrw17['gruene_rel'] = df_nrw17.apply(lambda row: round(row['gruene'] * 100 / row['gueltig'], 2), axis=1)
    del df_nrw17['wahlberechtigt']
    del df_nrw17['abgegeben']
    del df_nrw17['ungueltig']
    del df_nrw17['gueltig']
    del df_nrw17['spoe']
    del df_nrw17['oevp']
    del df_nrw17['fpoe']
    del df_nrw17['gruene']

    df_ages = import_data('../data/alter.csv', 'utf-8')
    df_ages['0_14_rel'] = df_ages.apply(lambda row: round(row['0_14'] * 100 / row['total'], 2), axis=1)
    df_ages['15_29_rel'] = df_ages.apply(lambda row: round(row['15_29'] * 100 / row['total'], 2), axis=1)
    df_ages['30_44_rel'] = df_ages.apply(lambda row: round(row['30_44'] * 100 / row['total'], 2), axis=1)
    df_ages['45_59_rel'] = df_ages.apply(lambda row: round(row['45_59'] * 100 / row['total'], 2), axis=1)
    df_ages['60_74_rel'] = df_ages.apply(lambda row: round(row['60_74'] * 100 / row['total'], 2), axis=1)
    df_ages['75_abs'] = df_ages['75']
    del df_ages['0_14']
    del df_ages['15_29']
    del df_ages['30_44']
    del df_ages['45_59']
    del df_ages['60_74']
    del df_ages['75']
    del df_ages['total']
    df_nrw17 = pd.merge(df_nrw17, df_ages, how='left', on=['gkz', 'gkz'])

    df_households = import_data('../data/haushalte.csv', 'utf-8')
    df_households['1p_rel'] = df_households.apply(lambda row: round(row['1p'] * 100 / row['total'], 2), axis=1)
    df_households['2p_rel'] = df_households.apply(lambda row: round(row['2p'] * 100 / row['total'], 2), axis=1)
    df_households['3p_abs'] = df_households['3p']
    df_households['4p_rel'] = df_households.apply(lambda row: round(row['4p'] * 100 / row['total'], 2), axis=1)
    df_households['5p_rel'] = df_households.apply(lambda row: round(row['5p'] * 100 / row['total'], 2), axis=1)
    del df_households['1p']
    del df_households['2p']
    del df_households['3p']
    del df_households['4p']
    del df_households['5p']
    del df_households['total']
    df_nrw17 = pd.merge(df_nrw17, df_households, how='left', on=['gkz', 'gkz'])
    #
    df_nation = import_data('../data/nationalitaet.csv', 'utf-8')
    df_nation['oesterreich_abs'] = df_nation['oesterreich']
    df_nation['ausland_rel'] = df_nation.apply(lambda row: round(row['ausland'] * 100 / row['total'], 2), axis=1)
    del df_nation['ausland']
    del df_nation['oesterreich']
    del df_nation['total']
    df_nrw17 = pd.merge(df_nrw17, df_nation, how='left', on=['gkz', 'gkz'])
    #
    df_nrw17.to_csv('../data/nrw17_data.csv', sep=';', index=False, decimal=',')
