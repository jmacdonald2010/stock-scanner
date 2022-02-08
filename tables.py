from http import server
import sqlalchemy
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Float, DateTime, TIMESTAMP, Boolean, func, Numeric
from sqlalchemy.orm import declarative_base
from base import Base

# Not sure if this will work
# Base = declarative_base()

class Stocks(Base):

    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True)
    short_name = Column(String)
    long_name = Column(String)
    industry_id = Column(Integer, ForeignKey('industry.id'))
    sector_id = Column(Integer, ForeignKey('sector.id'))
    is_held = Column(Boolean)
    datetime_updated = Column(DateTime(timezone=True))
    
""" class holdings(Base):

    __tablename__ = 'holdings'

    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('stocks.id')) """

class Sector(Base):

    __tablename__ = 'sector'

    id = Column(Integer, primary_key=True)
    sector_name = Column(String, unique=True)

class Industry(Base):

    __tablename__ = 'industry'

    id = Column(Integer, primary_key=True)
    industry_name = Column(String, unique=True)

class StockInfo(Base):

    __tablename__ = 'stock_info'

    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('stocks.id'))
    entry_datetime = Column(DateTime(timezone=True), server_default=func.now())
    ebitda_margins = Column(Numeric)
    profit_margins = Column(Numeric)
    gross_margins = Column(Numeric)
    operating_cash_flow = Column(Numeric)
    revenue_growth = Column(Numeric)
    operating_margins = Column(Numeric)
    ebitda = Column(Numeric)
    target_low_price = Column(Numeric)
    recommendation_key = Column(String)
    gross_profits = Column(Numeric)
    free_cash_flow = Column(Numeric)
    target_median_price = Column(Numeric)
    current_price = Column(Numeric)
    earnings_growth = Column(Numeric)
    current_ratio = Column(Numeric)
    return_on_assets = Column(Numeric)
    number_of_analyst_opinions = Column(Numeric)
    target_mean_price = Column(Numeric)
    debt_to_equity = Column(Numeric)
    return_on_equity = Column(Numeric)
    target_high_price = Column(Numeric)
    total_cash = Column(Numeric)
    total_debt = Column(Numeric)
    total_revenue = Column(Numeric)
    total_cash_per_share = Column(Numeric)
    revenue_per_share = Column(Numeric)
    quick_ratio = Column(Numeric)
    recommendation_mean = Column(Numeric)
    enterprise_to_revenue = Column(Numeric)
    beta_3_year = Column(Numeric) # In AAPL, this is None, so we need to check to make sure that this gets written properly
    enterprise_to_ebitda = Column(Numeric)
    fifty_two_week_change = Column(Numeric)
    morning_star_risk_rating = Column(String)
    forward_eps = Column(Numeric)
    revenue_quarterly_growth = Column(Numeric)
    shares_outstanding = Column(Numeric)
    book_value = Column(Numeric)
    shares_short = Column(Numeric)
    shares_percent_shares_out = Column(Numeric)
    held_percent_institutions = Column(Numeric)
    net_income_to_common = Column(Numeric)
    trailing_eps = Column(Numeric)
    last_dividend_value = Column(Numeric)
    s_and_p_fifty_two_week_change = Column(Numeric)
    price_to_book = Column(Numeric)
    held_percent_insiders = Column(Numeric)
    short_ratio = Column(Numeric)
    float_shares = Column(Numeric)
    beta = Column(Numeric)
    enterprise_value = Column(Numeric)
    price_hint = Column(Numeric)
    last_split_date = Column(Numeric)
    last_split_factor = Column(String)
    last_dividend_date = Column(Numeric)
    earnings_quarterly_growth = Column(Numeric)
    price_to_sales_ttm = Column(Numeric)
    date_short_interest = Column(Numeric)
    peg_ratio = Column(Numeric)
    forward_pe = Column(Numeric)
    short_percent_of_float = Column(Numeric)
    shares_short_prior_month = Column(Numeric)
    previous_close = Column(Numeric)
    regular_market_open = Column(Numeric)
    two_hundred_day_average = Column(Numeric)
    trailing_annual_dividend_yield = Column(Numeric)
    payout_ratio = Column(Numeric)
    volume_twenty_four_hour = Column(Numeric)
    regular_market_day_high = Column(Numeric)
    average_daily_volume_ten_day = Column(Numeric)
    regular_market_previous_close = Column(Numeric)
    fifty_day_average = Column(Numeric)
    trailing_annual_dividend_rate = Column(Numeric)
    open_price = Column(Numeric)
    average_volume_ten_days = Column(Numeric)
    dividend_rate = Column(Numeric)
    ex_dividend_date = Column(Numeric)
    regular_market_day_low = Column(Numeric)
    trailing_pe = Column(Numeric)
    regular_market_volume = Column(Numeric)
    market_cap = Column(Numeric)
    average_volume = Column(Numeric)
    day_low = Column(Numeric)
    ask = Column(Numeric)
    ask_size = Column(Numeric)
    volume = Column(Numeric)
    fifty_two_week_high = Column(Numeric)
    five_year_avg_dividend_yield = Column(Numeric)
    fifty_two_week_low = Column(Numeric)
    bid = Column(Numeric)
    dividend_yield = Column(Numeric)
    bid_size = Column(Numeric)
    day_high = Column(Numeric)
    regular_market_price = Column(Numeric)
    trailing_peg_ratio = Column(Numeric)