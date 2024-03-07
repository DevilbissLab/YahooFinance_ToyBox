# in terminal run - pip install "yfinance[nospam,repair]"
#import yfinance as yf
from yahooquery import Ticker
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns


def get_fund2benchmark(FundTickers, BenchmarkTickers, Parms):
    Fund_df = FundTickers.history(period=Parms.period, interval=Parms.interval)
    Fund_df_pivot = Fund_df.reset_index().pivot(index='date', columns='symbol', values='adjclose')
    Benchmark_df = BenchmarkTickers.history(period=Parms.period, interval=Parms.interval)
    Benchmark_df_pivot = Benchmark_df.reset_index().pivot(index='date', columns='symbol', values='adjclose')
    for x in Parms.funds:
        try:
            result = pd.merge(Fund_df_pivot[x[0]], Benchmark_df_pivot[x[1]], how="left", on=["date"])
            result = result.div(result.iloc[0, :]).mul(100)
            #bob['QCGLIX_PctBenchmark'] = (bob[x[0]] / bob[x[1]] * 100)
            Fund_df_pivot[x[0]] = (result[x[0]] / result[x[1]] * 100)
        except:
            print(['error merging ', x[0], ' and ', x[1] ], " >> using ^RUA")
            result = pd.merge(Fund_df_pivot[x[0]], Benchmark_df_pivot["^RUA"], how="left", on=["date"])
            result = result.div(result.iloc[0, :]).mul(100)
            Fund_df_pivot[x[0]] = (result[x[0]] / result["^RUA"] * 100)
    return Fund_df_pivot


def plot_fund2benchmark(Fund_df_pivot):
    #sns.set_theme()
    #sns.set_style("whitegrid")
    #sns.set_style("ticks")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.lineplot(data=Fund_df_pivot, dashes=False)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1), labelspacing=0.1)
    ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=1))
    ax.set_xlim(Fund_df_pivot.index.min(), Fund_df_pivot.index.max())

    fmt = '%.0f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    ax.yaxis.set_major_locator(mtick.MultipleLocator(10))

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.suptitle('Percent of benchmark')
    plt.show()

def plot_Tickers(obj, Parms):
    df = obj.history(period=Parms.period, interval=Parms.interval)
    #df = obj.history()
    df_pivot = df.reset_index().pivot(index='date', columns='symbol', values='adjclose')
    df_pivot_perc = df_pivot.div(df_pivot.iloc[0, :]).mul(100)
    #sns.set_theme()
    #sns.set_style("whitegrid")
    # sns.set_style("ticks")
    fig, ax = plt.subplots(figsize=(10, 6))

    ax = sns.lineplot(data=df_pivot_perc, dashes=False)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1), labelspacing=0.1)
    ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=1))
    ax.set_xlim(df_pivot.index.min(), df_pivot.index.max())

    fmt = '%.0f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    ax.yaxis.set_major_locator(mtick.MultipleLocator(10))

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

#
# #fundList = ["^DJI ^GSPC ^RUI ^MID ^RUT AGG"]
# #fund = Ticker(fundList[0])
#
# # Default period = ytd, interval = 1d
# df = fund.history()
# # get your df into a shape that is easier to digest for plotting methods
# df_pivot = df.reset_index().pivot(index='date', columns='symbol', values='adjclose')
#
# # sns.set_theme()
# #
# # fig, ax = plt.subplots(figsize=(10,6))
# #
# # ax = sns.lineplot(data=df_pivot, palette=['r','b'], dashes=False)
# #
# # # adjust axes for readability
# # ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday = 1))
# # ax.set_xlim(df_pivot.index.min(), df_pivot.index.max())
# # ax.yaxis.set_major_locator(mtick.MultipleLocator(50))
# #
# # plt.xticks(rotation=90)
# # plt.tight_layout()
# # plt.show()
#
# # or by percent
# df_pivot_perc = df_pivot.div(df_pivot.iloc[0,:]).mul(100)
# fig, ax = plt.subplots(figsize=(10,6))
#
# #ax = sns.lineplot(data=df_pivot_perc, palette=['r','b'], dashes=False)
# ax = sns.lineplot(data=df_pivot_perc, dashes=False)
# ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday = 1))
# ax.set_xlim(df_pivot.index.min(), df_pivot.index.max())
#
# fmt = '%.0f%%'
# yticks = mtick.FormatStrFormatter(fmt)
# ax.yaxis.set_major_formatter(yticks)
# ax.yaxis.set_major_locator(mtick.MultipleLocator(10))
#
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()
