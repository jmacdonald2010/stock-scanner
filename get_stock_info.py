import yfinance as yf
from connect import connect_to_session
from tables import Stocks, Industry, Sector, StockInfo
import json

def get_new_stock_info(symbol):

    # Connect to DB
    session = connect_to_session()

    # Get the symbols/ids for the stock you wish to update
    symbols_ids = get_stock_symbol_id()

    # Make the call to yf
    data = yf.Ticker(symbol).info

    # Check through the data to see if any of the necessary keys are missing
    with open('stock_info_keys_values.json') as f:
        column_k_v = json.load(f)

    for x, y in column_k_v.items():
        if y not in data.keys():
            data[y] = None

    # Create a new object for the StockInfo
    info = StockInfo(
        symbol_id=symbols_ids[symbol],
        ebitda_margins=data['ebitdaMargins'],
        profit_margins=data['profitMargins'],
        gross_margins=data['grossMargins'],
        operating_cash_flow=data['operatingCashflow'],
        revenue_growth = data['revenueGrowth'],
        operating_margins = data['operatingMargins'],
        ebitda = data['ebitda'],
        target_low_price = data['targetLowPrice'],
        recommendation_key = data['recommendationKey'],
        gross_profits = data['grossProfits'],
        free_cash_flow = data['freeCashflow'],
        target_median_price = data['targetMedianPrice'],
        current_price = data['currentPrice'],
        earnings_growth = data['earningsGrowth'],
        current_ratio = data['currentRatio'],
        return_on_assets = data['returnOnAssets'],
        number_of_analyst_opinions = data['numberOfAnalystOpinions'],
        target_mean_price = data['targetMeanPrice'],
        debt_to_equity = data['debtToEquity'],
        return_on_equity = data['returnOnEquity'],
        target_high_price = data['targetHighPrice'],
        total_cash = data['totalCash'],
        total_debt = data['totalDebt'],
        total_revenue = data['totalRevenue'],
        total_cash_per_share = data['totalCashPerShare'],
        revenue_per_share = data['revenuePerShare'],
        quick_ratio = data['quickRatio'],
        recommendation_mean = data['recommendationMean'],
        enterprise_to_revenue = data['enterpriseToRevenue'],
        beta_3_year = data['beta3Year'], # In AAPL, this is None, so we need to check to make sure that this gets written properly
        enterprise_to_ebitda = data['enterpriseToEbitda'],
        fifty_two_week_change = data['52WeekChange'],
        morning_star_risk_rating = data['morningStarRiskRating'],
        forward_eps = data['forwardEps'],
        revenue_quarterly_growth = data['revenueQuarterlyGrowth'],
        shares_outstanding = data['sharesOutstanding'],
        book_value = data['bookValue'],
        shares_short = data['sharesShort'],
        shares_percent_shares_out = data['sharesPercentSharesOut'],
        held_percent_institutions = data['heldPercentInstitutions'],
        net_income_to_common = data['netIncomeToCommon'],
        trailing_eps = data['trailingEps'],
        last_dividend_value = data['lastDividendValue'],
        s_and_p_fifty_two_week_change = data['SandP52WeekChange'],
        price_to_book = data['priceToBook'],
        held_percent_insiders = data['heldPercentInsiders'],
        short_ratio = data['shortRatio'],
        float_shares = data['floatShares'],
        beta = data['beta'],
        enterprise_value = data['enterpriseValue'],
        price_hint = data['priceHint'],
        last_split_date = data['lastSplitDate'],
        last_split_factor = data['lastSplitFactor'],
        last_dividend_date = data['lastDividendDate'],
        earnings_quarterly_growth = data['earningsQuarterlyGrowth'],
        price_to_sales_ttm = data['priceToSalesTrailing12Months'],
        date_short_interest = data['dateShortInterest'],
        peg_ratio = data['pegRatio'],
        forward_pe = data['forwardPE'],
        short_percent_of_float = data['shortPercentOfFloat'],
        shares_short_prior_month = data['sharesShortPriorMonth'],
        previous_close = data['previousClose'],
        regular_market_open = data['regularMarketOpen'],
        two_hundred_day_average = data['twoHundredDayAverage'],
        trailing_annual_dividend_yield = data['trailingAnnualDividendYield'],
        payout_ratio = data['payoutRatio'],
        volume_twenty_four_hour = data['volume24Hr'],
        regular_market_day_high = data['regularMarketDayHigh'],
        average_daily_volume_ten_day = data['averageDailyVolume10Day'],
        regular_market_previous_close = data['regularMarketPreviousClose'],
        fifty_day_average = data['fiftyDayAverage'],
        trailing_annual_dividend_rate = data['trailingAnnualDividendRate'],
        open_price = data['open'],
        average_volume_ten_days = data['averageVolume10days'],
        dividend_rate = data['dividendRate'],
        ex_dividend_date = data['exDividendDate'],
        regular_market_day_low = data['regularMarketDayLow'],
        trailing_pe = data['trailingPE'],
        regular_market_volume = data['regularMarketVolume'],
        market_cap = data['marketCap'],
        average_volume = data['averageVolume'],
        day_low = data['dayLow'],
        ask = data['ask'],
        ask_size = data['askSize'],
        volume = data['volume'],
        fifty_two_week_high = data['fiftyTwoWeekHigh'],
        five_year_avg_dividend_yield = data['fiveYearAvgDividendYield'],
        fifty_two_week_low = data['fiftyTwoWeekLow'],
        bid = data['bid'],
        dividend_yield = data['dividendYield'],
        bid_size = data['bidSize'],
        day_high = data['dayHigh'],
        regular_market_price = data['regularMarketPrice'],
        trailing_peg_ratio = data['trailingPegRatio'],
    )

    session.add(info)
    session.commit()
    # session.close()

    return info


def get_stock_symbol_id():

    """Creates and returns a dict of all symbols as keys, ids as values for all entries in the Stock table."""

    # Connect to DB
    session = connect_to_session()

    symbol_id_dict = dict()

    # Make a dict of all symbols/ids
    for symbol, id in session.query(Stocks.symbol, Stocks.id):
        symbol_id_dict[symbol] = id

    return symbol_id_dict