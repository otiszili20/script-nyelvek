import logging
import pandas as pd
from pymongo import MongoClient
from matplotlib import pyplot as plt
import seaborn as sns

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(
    filename='analitics.log',
    filemode='w',
    format=LOG_FORMAT,
    level=logging.DEBUG
)
LOG = logging.getLogger()


def _extract_city(address: str) -> str:
    return address.split('\n')[1].split(',')[0]


def _extract_state(address: str) -> str:
    result = ""
    try:
        result =  address.split('\n')[1].split(',')[1].split(' ')[1]
    except IndexError as err:
        result = None
        LOG.info(f'Index Error: {err}, address: {address}')
    return result


if __name__ == '__main__':
    USERNAME = 'root'
    PASSWORD = 'example'
    DB_NAME = 'sample'
    HOST = 'localhost'
    PORT = 27017
    CONNECTION_STRING = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?authSource=admin'
    client = MongoClient(CONNECTION_STRING)
    accounts_df = pd.DataFrame(list(client[DB_NAME]['accounts'].find()))
    customers_df = pd.DataFrame(list(client[DB_NAME]['customers'].find()))
    transactions_df = pd.DataFrame(list(client[DB_NAME]['transactions'].find()))
    customers_df['city'] = customers_df['address'].apply(_extract_city)
    customers_df['state'] = customers_df['address'].apply(_extract_state)
    customers_df['birth_year'] = customers_df.apply(lambda record: record['birthdate'].date().year, axis=1)
    year = customers_df.groupby(by='birth_year')['_id'].count().reset_index()['birth_year']
    no_of_customers = customers_df.groupby(by='birth_year')['_id'].count().reset_index()['_id']

    fig, ax = plt.subplots(1,1)
    ax.bar(year, no_of_customers)
    ax.set_xlabel('years')
    ax.set_ylabel('# Customers Birth')
    plt.show()

    sns.set()
    tmp = pd.DataFrame(data={
        'year': year,
        'no_of_customers': no_of_customers
    })
    sns.barplot(data=tmp, x='year', y='no_of_customers')
    plt.show()

    sns.relplot(data=customers_df, x='birth_year', y='state', kind='scatter')
    plt.show()
    print('PyCharm')
