import pandas as pd
import datetime
import yfinance as yf
from matplotlib import pyplot as plt
import mplcyberpunk
import smtplib
from email.message import EmailMessage

# pegar os dados do Yahoo Finance
# criando uma lista com os códigos bovespa
# pegando código das acoes no yahoo = ^BVSP e BRL=X ("PRNR3.SA","IRBR3.SA","MRFG3.SA", "PPLA11.SA", "CVBI11.SA", "MXRF11.SA" )


ativos = ("PRNR3.SA", "IRBR3.SA", "MRFG3.SA",
          "PPLA11.SA", "CVBI11.SA", "MXRF11.SA")
hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days=365)
dados_mercado = yf.download(ativos, um_ano_atras, hoje)

print(dados_mercado)

dados_fechamento = dados_mercado['Adj Close']

dados_fechamento = dados_fechamento.dropna()

print(dados_fechamento.head(50))

# Qdo quiser alterar os nomes das colunas use dados.fechamento.columns = ['nome1', 'nome2', etc..]

dados_fechamento_mensal = dados_fechamento.resample("M").last()  # mensal
dados_fechamento_anual = dados_fechamento.resample("Y").last()  # anual


print(dados_fechamento_mensal)
print(dados_fechamento_anual)
# MAnipular os dados
dados_mercado['Adj Close']

retorno_do_ano = dados_fechamento_anual.pct_change().dropna()
retorno_do_mes = dados_fechamento_mensal.pct_change().dropna()
retorno_do_dia = dados_fechamento.pct_change().dropna()
print(retorno_do_ano)
print(retorno_do_mes)
print(retorno_do_dia)


# LOC referencia à partir do nome
# ILOC referencia como matriz
# retorno_do_dia.loc[linha,coluna]


# print(retorno_do_dia.loc['2023-03-29', 'CVBI11.SA'])  # somente desse
# print(retorno_do_dia.loc['2023-03-29'])  # de todos
# print(retorno_do_dia.iloc[1, 1])

retorno_do_dia_prnr3 = retorno_do_dia.iloc[-1, 0]
retorno_do_dia_irbr3 = retorno_do_dia.iloc[-1, 1]
retorno_do_dia_mrfg = retorno_do_dia.iloc[-1, 2]
retorno_do_dia_ppla = retorno_do_dia.iloc[-1, 3]
retorno_do_dia_cvbi = retorno_do_dia.iloc[-1, 4]
retorno_do_dia_mxrf = retorno_do_dia.iloc[-1, 5]

retorno_do_mes_prnr3 = retorno_do_mes.iloc[-1, 0]
retorno_do_mes_irbr3 = retorno_do_mes.iloc[-1, 1]
retorno_do_mes_mrfg = retorno_do_mes.iloc[-1, 2]
retorno_do_mes_ppla = retorno_do_mes.iloc[-1, 3]
retorno_do_mes_cvbi = retorno_do_mes.iloc[-1, 4]
retorno_do_mes_mxrf = retorno_do_mes.iloc[-1, 5]

retorno_do_ano_prnr3 = retorno_do_ano.iloc[-1, 0]
retorno_do_ano_irbr3 = retorno_do_ano.iloc[-1, 1]
retorno_do_ano_mrfg = retorno_do_ano.iloc[-1, 2]
retorno_do_ano_ppla = retorno_do_ano.iloc[-1, 3]
retorno_do_ano_cvbi = retorno_do_ano.iloc[-1, 4]
retorno_do_ano_mxrf = retorno_do_ano.iloc[-1, 5]

retorno_do_dia_prnr3 = round(retorno_do_dia_prnr3 * 100, 2)
retorno_do_dia_irbr3 = round(retorno_do_dia_irbr3 * 100, 2)
retorno_do_dia_mrfg = round(retorno_do_dia_mrfg * 100, 2)
retorno_do_dia_ppla = round(retorno_do_dia_ppla * 100, 2)
retorno_do_dia_cvbi = round(retorno_do_dia_cvbi * 100, 2)
retorno_do_dia_mxrf = round(retorno_do_dia_mxrf * 100, 2)

retorno_do_mes_prnr3 = round(retorno_do_mes_prnr3 * 100, 2)
retorno_do_mes_irbr3 = round(retorno_do_mes_irbr3 * 100, 2)
retorno_do_mes_mrfg = round(retorno_do_mes_mrfg * 100, 2)
retorno_do_mes_ppla = round(retorno_do_mes_ppla * 100, 2)
retorno_do_mes_cvbi = round(retorno_do_mes_cvbi * 100, 2)
retorno_do_mes_mxrf = round(retorno_do_mes_mxrf * 100, 2)

retorno_do_ano_prnr3 = round(retorno_do_ano_prnr3 * 100, 2)
retorno_do_ano_irbr3 = round(retorno_do_ano_irbr3 * 100, 2)
retorno_do_ano_mrfg = round(retorno_do_ano_mrfg * 100, 2)
retorno_do_ano_ppla = round(retorno_do_ano_ppla * 100, 2)
retorno_do_ano_cvbi = round(retorno_do_ano_cvbi * 100, 2)
retorno_do_ano_mxrf = round(retorno_do_ano_mxrf * 100, 2)


print("ret dia=============================================================================")
print(retorno_do_dia_prnr3)
print(retorno_do_dia_irbr3)
print(retorno_do_dia_mrfg)
print(retorno_do_dia_ppla)
print(retorno_do_dia_ppla)
print(retorno_do_dia_mxrf)
print("ret mes=============================================================================")
print(retorno_do_mes_prnr3)
print(retorno_do_mes_irbr3)
print(retorno_do_mes_mrfg)
print(retorno_do_mes_ppla)
print(retorno_do_mes_ppla)
print(retorno_do_mes_mxrf)
print("ret ano=============================================================================")
print(retorno_do_ano_prnr3)
print(retorno_do_ano_irbr3)
print(retorno_do_ano_mrfg)
print(retorno_do_ano_ppla)
print(retorno_do_ano_ppla)
print(retorno_do_ano_mxrf)
# fazer os gráficos
