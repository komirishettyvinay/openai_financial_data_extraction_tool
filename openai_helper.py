import openai
from secret_key import openai_key

import json
import pandas as pd
openai.api_key = openai_key


def extract_financial_data(text):
    prompt = get_Prompt_financial() + text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]   
    )
    content = response.choices[0]['message']['content']

    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(), columns=["Measure", "Value"])
    except (json.JSONDecodeError, IndexError):
        pass


    return pd.DataFrame({
        "Measure" : ["Company Name", "Stock Symbol", "Revunue", "Net Income" ,"EPS"],
        "Value"   : ["", "", "", "", ""]
    })


def get_Prompt_financial():
    return ''' Please retrieve a company name, revenue, net income and earning per share (a.k.a EPS) from the following article. 
    If you cant find the information from this article then return. Do not make things up.
    Then retreive a stock symbol corresponding to that company. 
    For this you can use your general knowledge (it doesn't have to be from this article) 
    Always return your response as a valid JSON string. The format of that string should be in this,
    {
      "Company Name" : "Apple",
      "Stock Symbol" : "APP",
      "Revunue" : "$94.52 billion",
      "Net Income" : "$25.56 billion",
      "EPS" : "2.5 $"
    }
    News Article :
    ==============================

   '''

if __name__ == '__main__':
    text = '''
            Q2 Results: Tata Motors, the passenger cars and commercial vehicle manufacturer, is set to announce its financial results for the quarter ended September 2023 today. The automobile major is expected to remain profitable during the quarter as against reporting a net loss in the corresponding quarter of last fiscal.

            The automobile sector saw strong dispatches for SUV fueled by order book execution and improvement in supply chain situation. However, demand moderated for lower-end passenger vehicles (PV). Among all the segments, MHCV appeared to be better placed despite a drop in discounts, driven by healthy demand across most of the underlying industries, analysts said.

            Read Tata Motors Q2 Results Live Updates here

            Tata Motors, which also owns luxury car brand Jaguar Land Rover (JLR), is estimated to report a net profit of ₹3,994 crore in the second quarter of FY24 led by lower commodity prices, operating leverage and volume ramp-up at JLR, as per average estimates of six brokerages. 

            The auto major is expected to report total revenue of ₹1,05,883 crore in the quarter ended September 2023, registering a growth of 33% from ₹79,611.4 crore in the year-ago quarter.

            The company’s India business performance was a mixed bag as commercial vehicle (CV) volumes grew 3.5% YoY while passenger vehicle (PV) volumes fell 3% YoY. JLR volumes are expected to grow YoY due to easing chip shortage situation and continued traction in new models.

            (Exciting news! Mint is now on WhatsApp Channels :rocket: Subscribe today by clicking the link and stay updated with the latest financial insights! Click here!)

            At the operational level, Tata Motors’ earnings before interest, tax, depreciation and amortization (EBITDA) during the July-September quarter of FY24 is expected to jump by 130% to ₹14,257 crore from ₹6,196.2 crore in the same quarter last fiscal year, as per street estimates.

            EBITDA margin is likely to improve by 572 basis points (bps) to 13.5% in Q2FY24 from 7.8%, YoY, led by raw material tailwinds and operating leverage benefits, partly offset by lower spares mix.

            Brokerage firm Kotak Institutional Equities expects Tata Motors’ standalone business revenues to increase by 27% YoY in Q2FY24, led by 4% YoY improvement in volumes due to strong demand trends in MHCV trucks and passenger segment and 20-22% YoY increases in ASPs due to richer product mix, price hikes taken in the last one year and lower discounts as a percentage of average selling prices (ASP).
                        
        '''
    
    df = extract_financial_data(text)
    print(df.to_string())