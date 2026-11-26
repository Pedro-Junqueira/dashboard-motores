import pandas as pd
import numpy as np

df = pd.read_csv('telemetria_motores.csv', parse_dates=['data_hora'])

cols = ['data_hora', 'codigo_motor', 'aplicacao', 'linha_rendimento',
        'potencia_nominal_kw', 'potencia_kw', 'vibracao_rms_mm_s',
        'temperatura_mancal_c', 'temperatura_ambiente_c', 'ruido_db',
        'horas_desde_manutencao']

df = df[cols]

df['carga'] = df['potencia_kw'] / df['potencia_nominal_kw']
df['hora'] = df['data_hora'].dt.hour
df['dia_semana'] = df['data_hora'].dt.dayofweek
df['mes'] = df['data_hora'].dt.strftime('%Y-%m')
df['periodo'] = np.where((df['hora'] >= 6) & (df['hora'] < 22), 'turno', 'noite')

df['data'] = df['data_hora'].dt.strftime('%Y-%m-%d')
df = df.drop(columns='data_hora')

df = df.round(2)
df.to_csv('dados.csv', index=False)




