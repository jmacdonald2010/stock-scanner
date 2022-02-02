from ast import For
from ipaddress import collapse_addresses
import sqlalchemy
import yfinance as yf
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Float, DateTime, TIMESTAMP, Boolean
from sqlalchemy.orm import declarative_base

def build_db():

    # Create the database, or connect to it
    engine = create_engine('sqllite:///data.db')

    # Declare Database
    Base = declarative_base()

    return Base

def build_tables(Base):

    class stocks(Base):

        __tablename__ = 'stocks'

        id = Column(Integer, primary_key=True)
        symbol = Column(String, unique=True)
        short_name = Column(String)
        long_name = Column(String)
        industry = Column(String)
        sector_id = Column(Integer, ForeignKey('sector.id'))
        is_held = Column(Boolean)
        
    """ class holdings(Base):

        __tablename__ = 'holdings'

        id = Column(Integer, primary_key=True)
        symbol_id = Column(Integer, ForeignKey('stocks.id')) """

    class sector(Base):

        __tablename__ = 'sector'

        id = Column(Integer, primary_key=True)
        sector_name = Column(String, unique=True)

    class industry(Base):

        __tablename__ = 'industry'

        id = Column(Integer, primary_key=True)
        industry_name = Column(String, unique=True)

    class stock_info(Base):

        __tablename__ = 'stock_info'

        id = Column(Integer, primary_key=True)
        symbol_id = Column(Integer, ForeignKey('stocks.id'))
        ebitda_margins = Column(Float)
        profit_margins = Column(Float)
        gross_margins = Column(Float)
        operating_cash_flow = Column(Integer)
        revenue_growth = Column(Float)
        operating_margins = Column(Float)
        ebitda = Column(Integer)
        target_low_price = Column(Float)
        recommendation_key = Column(String)
        gross_profits = Column(Integer)
        free_cash_flow = Column(Integer)
        target_median_price = Column(Float)
        current_price = Column(Float)
        earnings_growth = Column(Float)
        current_ratio = Column(Float)
        return_on_assets = Column(Float)
        number_of_analyst_opinions = Column(Integer)
        target_mean_price = Column(Float)
        debt_to_equity = Column(Float)
        return_on_equity = Column(Float)
        target_high_price = Column(Float)
        total_cash = Column(Integer)
        total_debt = Column(Integer)
        total_revenue = Column(Integer)
        total_cash_per_share = Column(Float)
        revenue_per_share = Column(Float)
        quick_ratio = Column(Float)
        recommendation_mean = Column(Float)
        enterprise_to_revenue = Column(Float)
        beta_3_year = Column(Float) # In AAPL, this is None, so we need to check to make sure that this gets written properly
        enterprise_to_ebitda = Column(Float)
        fifty_two_week_change = Column(Float)
        morning_star_risk_rating = Column(String)
        forward_eps = Column(Float)
        revenue_quarterly_growth = Column(Float)
        shares_outstanding = Column(Integer)
        book_value = Column(Float)
        shares_short = Column(Integer)
        shares_percent_shares_out = Column(Float)
        held_percent_institutions = Column(Float)
        net_income_to_common = Column(Integer)
        trailing_eps = Column(Float)
        last_dividend_value = Column(Float)
        s_and_p_fifty_two_week_change = Column(Float)
        price_to_book = Column(Float)
        held_percent_insiders = Column(Float)
        short_ratio = Column(Float)
        float_shares = Column(Integer)
        beta = Column(Float)
        enterprise_value = Column(Integer)
        price_hint = Column(Integer)
        last_split_date = Column(Integer)
        last_split_factor = Column(String)
        last_dividend_date = Column(Integer)
        earnings_quarterly_growth = Column(Float)
        price_to_sales_ttm = Column(Float)
        date_short_interest = Column(Integer)
        peg_ratio = Column(Float)
        forward_pe = Column(Float)
        short_percent_of_float = Column(Float)
        shares_short_prior_month = Column(Integer)
        previous_close = Column(Float)
        regular_market_open = Column(Float)
        two_hundred_day_average = Column(Float)
        trailing_annual_dividend_yield = Column(Float)
        payout_ratio = Column(Float)
        volume_twenty_four_hour = Column(Integer)
        regular_market_day_high = Column(Integer)
        average_daily_volume_ten_day = Column(Integer)
        regular_market_previous_close = Column(Float)
        fifty_day_average = Column(Float)
        trailing_annual_dividend_rate = Column(Float)
        open_price = Column(Float)
        average_volume_ten_days = Column(Integer)
        dividend_rate = Column(Float)
        ex_dividend_date = Column(Integer)
        regular_market_day_low = Column(Float)
        trailing_pe = Column(Float)
        regular_market_volume = Column(Float)
        market_cap = Column(Integer)
        average_volume = Column(Integer)
        day_low = Column(Float)
        ask = Column(Float)
        ask_size = Column(Integer)
        volume = Column(Integer)
        fifty_two_week_high = Column(Float)
        five_year_avg_dividend_yield = Column(Float)
        fifty_two_week_low = Column(Float)
        bid = Column(Float)
        dividend_yield = Column(Float)
        bid_size = Column(Float)
        day_high = Column(Float)
        regular_market_price = Column(Float)
        trailing_peg_ratio = Column(Float)
