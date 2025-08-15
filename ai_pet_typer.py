#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import requests

OLLAMA_HOST = "http://localhost:11434"
DEFAULT_MODEL = "tinyllama"
##given dict, return blurb uses ollama first
def write_bio(pet, model=DEFAULT_MODEL, host=OLLAMA_HOST):
    name = pet.get("name","This pet")
    breed = (pet.get("breeds") or {}).get("primary","mixed")
    age = (pet.get("age") or "").lower()
    city = ((pet.get("contact") or {}).get("address") or {}).get("city","nearby")
    prompt = f"Write a cute, honest 2–3 sentence adoption blurb for {name}, a {age} {breed} in {city}. Avoid making up facts."
    try:
        ##call ollamas endpoint
        j = requests.post(
            f"{host}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=60
        ).json()
        return j.get("response","")
    except Exception:
        return f"Meet {name}! A {breed} in {city} hoping to find a loving home."


# In[ ]:




