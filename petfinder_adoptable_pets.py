#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, requests
from dotenv import load_dotenv, find_dotenv


###env file should be hidden
load_dotenv(find_dotenv())

CID = os.getenv("PETFINDER_CLIENT_ID")
SECRET = os.getenv("PETFINDER_CLIENT_SECRET")

def token():
    r = requests.post(
        "https://api.petfinder.com/v2/oauth2/token",
        data={"grant_type":"client_credentials", "client_id": CID, "client_secret": SECRET},
        timeout=20
    )
    r.raise_for_status()
    return r.json()["access_token"]

def get_pets(species="Dog", zip_code="10001", how_many=5):
    t = token()
    r = requests.get(
        "https://api.petfinder.com/v2/animals",
        headers={"Authorization": f"Bearer {t}"},
        params={"type": species, "location": zip_code, "limit": how_many, "status": "adoptable"},
        timeout=30
    )
    r.raise_for_status()
    return r.json().get("animals", [])


# In[ ]:





# In[ ]:





# In[ ]:




