from bson.objectid import ObjectId
from connection import Connection
from competitors import *
from customerReviews import *
import pandas as pd


class CompetitorsAdding:
    def __init__(self, df):
        self.df = df

    def competitor_iteration(self):
        for index, row in self.df.iterrows():
            competitor = Competitors()
            competitor.competitor_name = row['Company']
            competitor.url = row['Url1']
            competitor.org_vals = OrgValues(place=row['Country'], shares=row['Public/private'], cb_rank=row['CB'])
            competitor.product = Product(
                first_product=FirstProduct(energy=row['Energy_p'], wavelength=row['Wavelength_p']),
                second_product=SecondProduct(energy=row['Energy_f'], wavelength=row['Wavelength_f']),
                third_product=ThirdProduct(avg_delivery=row['Shipment'], avg_price=row['Price'],
                                           technical=ThirdProductTech(energy=row['Energy'],
                                                                      wavelength=row['Wavelength'])))
            competitor.technology = Technology(sphere=row['Total_medicine'],
                                               tech=row['Total_x'] + row['Total_y'],
                                               conference_presence=row['Spie_company'])

            competitor.save()


class ReviewsAdding:
    def __init__(self, df, collection):
        self.df = df
        self.collection = collection

    def reviews_iteration(self):
        for index, row in self.df.iterrows():
            original_id = self.collection.find({'url': {'$eq': row['Url']}})['_id']

            compcust = CompetitorsCustomers()
            compcust.url = original_id
            compcust.customers = Customers(mentions_num=row['Mentions'],
                                          subscribers=row['Subscribers'],
                                          rank=Rank(overall_rank=row[''], reach_rank=row[''], rank_per_million=row['']),
                                          views=Views(pv_rank=row[''], pv_per_user=row['']))

            compcust.reviews = []
            for i in row['Reviews']:
                compcust.reviews.append(Reviews(text='', tonality=0.0, score=0))

            compcust.save()


if __name__ == '__main__':
    # Connecting to database collection
    conn = Connection()
    db_cursor = conn.connect()
    coll = db_cursor['Competitors']

    # Adding data
    df = pd.read_excel(r'C:\Users\maxim\OneDrive\Desktop\folder\diplom\data\parsing\final_companies.xlsx')
    obj = CompetitorsAdding(df)
    obj.competitor_iteration()
    print('Competitors added!')

    #Adding text fields
    df1 = pd.read_excel('')
    obj2 = ReviewsAdding(df1, coll)
