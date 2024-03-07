# Devilbiss Finance Project
# v.0.09 2024-3-5
#
# Requires install of the following libraries:
# yahooquery, matplotlib, pandas, seaborn, and their dependencies (i.d. numpy, etc), mpld3(optional)
# Will run in pyCharm virtual environment
# the idea of this is to get putative funds and compare them to their benchmarks to determine
# their performance.
# to do:
# yahoo finance api may not have all of the benchmarks avalable through their API.
# check plotting - something is wrong about percentages and the default format is busy.
from yahooquery import Ticker
from FinanceProject import *

# https://www.investopedia.com/articles/professionals/072415/value-or-growth-stocks-which-best.asp
# https://www.investopedia.com/articles/08/performance-measure.asp

class Parameters:
  def __init__(self):
    self.period = '10y'
    self.interval = '1wk'
    #Interval values must be one of 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
      #create tuple
    # self.benchmarks = ("^GDOW ^DJI ^GSPC ^DWLG ^RUI ^RMCCV ^DJUSRE ^DJUSTC ^DJTHCA ^RAV ^MID ^RUT AGG ^SPXHDUP")
    self.benchmarks = ("^RUA ^RAV ^RAG ^RUI ^RUT ^DJI ^GSPC ^MID AGG")
                       # Russel 1000 (RUI)- index for large-cap investing
                       # Russel 2000 (RUT)- index for small-cap to mid-cap stocks
                       # Russel 3000 (RUA)- comprehensive, unbiased, and stable barometer of the broad market
                       # Russel 3000 (RAV)- Value index for Russel 3000
                       # Russel 3000 (RAG)- Growth index for Russel 3000
                       # Dow Jones Industrial Average (DJI)- benchmark index in the U.S. for blue-chip stocks
                       # S&P 500 (GSPC)- represent most of the composition of the U.S. economy
                       #    The S&P 500 has outperformed the DJIA on an annualized basis over the last three-, five-, and 10-year periods
                       # S&P MID CAP 400 INDEX (MID)- index for mid-cap stocks
                       # iShares Core U.S. Aggregate Bond ETF (AGG)- General bond index
      #create paired list
    self.funds = [["QCGLIX",'^RAG'], #Global Large Cap Blend +Growth
                  ["QCGRIX",'^RAG'],   #US Large Cap Growth
                  ["QCSTIX",'^RAG'],   #Global Large Cap Blend Aggressive +Growth
                  ["RERGX", '^RAG'],    # Euro-Pacific Large Cap Growth
                  ["TRLGX", '^RAG'],    #US Large Cap Growth
                  ["TCIEX", '^RUA'],    #Global Large Cap Blend
                  ["TILVX", '^RAV'],    #US Large Cap Value
                  ["TISPX", '^GSPC'],    #S&P 500 Index
                  ["TISBX", '^RUT'],    # US Small-Cap Blend
                  ["VASVX", '^MID'],    #US Mid Cap Value
                  ["QREARX", '^DJUSRE'],   #US Real Estate
                  ["QCILIX", 'AGG'],     #Inflation-Linked Bond
                  ["TBIIX", 'AGG'],    #Bond Index
                  ["QCSCIX", '^GSPC'],   #Social Choice - Moderate Allocation - Bond Blend
                  ["JANBX", '^GSPC'],    #US Large Cap - Moderate Allocation - Bond Blend
                  ["JRSDX", '^RAG'],    #Global Large Cap Blend + growth
                  ["JNGLX", '^GSPC'],    #US Large Cap - Healthcare (Bad benchmark)
                  ["JANIX", '^RUT'],    # US Small-Cap growth
                  ["JNGTX", '^RUI'],    #Global Large Cap - tech
                  ["JFRDX", '^RAG'],    #US Large Cap Growth
                  ["ITYAX", '^RUI'],    #US Large Cap - tech
                  ["GGHCX", '^GSPC'],    #US Large Cap Blend - Healthcare (Bad benchmark)
                  ["KBWD",  '^RUT']     #US small Cap Value
                  ]

  def get_benchmarks(self):
    Tickers = Ticker(self.benchmarks)
    return Tickers

  def get_funds(self):
      #Tickers = [item[0] for item in self.funds]
      Tickers = Ticker([item[0] for item in self.funds])
      return Tickers

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Parms = Parameters()
    BenchmarkTickers = Parms.get_benchmarks()
    plot_Tickers(BenchmarkTickers, Parms)
    FundTickers = Parms.get_funds()
    plot_Tickers(FundTickers, Parms)
    Fund_df_pivot = get_fund2benchmark(FundTickers, BenchmarkTickers, Parms)
    plot_fund2benchmark(Fund_df_pivot)
    print('Done')
