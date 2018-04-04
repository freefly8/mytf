from sqlalchemy import create_engine
import tushare as ts
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model import Channel

def test():
    print(ts.get_hist_data('002405', start='2015-01-05', end='2015-01-09'))
    print(ts.get_today_all())


# 初始化数据库连接,:
engine = create_engine('mysql://root:root@127.0.0.1/stock?charset=utf8')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()


def query():
    # 查操作
    session1 = DBSession()
    channel = session1.query(Channel).filter(Channel.id < '4').all()

    for i in range(len(channel)):
        print(channel[i].id)
        print(channel[i].channel_name)
        print(channel[i].address)
        print(channel[i].service_name)


if __name__ == "__main__":
    query()
