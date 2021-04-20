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
            object_id = self.collection.find({'url': row['Url1']}, {"_id": 1})[0]['_id']
            compcust = CompetitorsCustomers()
            compcust.url = object_id
            aws1 = row['aws1'] if row['aws1'] != 'None' else -1
            tweets = 'no text' if pd.isna(row['Tweets']) else row['Tweets']

            compcust.customers = Customers(mentions_num=row['Mentions'],
                                          rank=Rank(overall_rank=aws1, reach_rank=row['aws2'], rank_per_million=row['aws3']),
                                          views=Views(pv_rank=row['aws4'], pv_per_user=0.0))

            compcust.reviews = []
            compcust.reviews.append(Reviews(text=tweets,
                                            tonality_score=row['Average positiveness'],
                                            positive_percent=row['Positiveness']))

            compcust.save()


if __name__ == '__main__':
    # Connecting to database collection
    conn = Connection()
    db_cursor = conn.connect()
    coll = db_cursor['competitors']

    # Adding data
    #df = pd.read_excel(r'C:\Users\maxim\OneDrive\Desktop\folder\diplom\data\parsing\final_companies.xlsx')
    #obj = CompetitorsAdding(df)
    #obj.competitor_iteration()
    #print('Competitors added!')

    #Adding text fields
    df1 = pd.read_excel(r"C:\Users\maxim\OneDrive\Desktop\folder\diplom\data\parsing\final_companies_with_text.xlsx")
    obj2 = ReviewsAdding(df1, coll)
    obj2.reviews_iteration()
    print('Reviews added!')
