from sqlalchemy import create_engine
import tushare as ts


def test():
    print(ts.get_hist_data('002405', start='2015-01-05', end='2015-01-09'))
    print(ts.get_today_all())


def insert_to_mysql():
    df = ts.get_tick_data('600848', date='2014-12-22')
    engine = create_engine('mysql://root:root@127.0.0.1/stock?charset=utf8')

    # 存入数据库
    df.to_sql('tick_data', engine)

    # 追加数据到现有表
    # df.to_sql('tick_data',engine,if_exists='append')
    engine


if __name__ == "__main__":
    insert_to_mysql()
