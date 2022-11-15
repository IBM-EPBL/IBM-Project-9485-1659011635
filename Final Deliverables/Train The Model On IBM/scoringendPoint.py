import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "fsH4u8pB1MWyOFVTkocolZnL0zLrkGWkxQwzdFrT9-rp"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [['Present_Price','Car_age','Fuel_Type_Diesel','Seller_Type_Individual','Transmission_Manual']], "values": [[10000,123,0,1,0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/ac3da380-46b3-4cb0-8a5a-a92ce06939a1/predictions?version=2022-11-15', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
pred = response_scoring.json()
output = pred['predictions'][0]['values'][0][0]
print(output)