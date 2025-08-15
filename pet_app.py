#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


import gradio as gr
from petfinder_adoptable_pets import get_pets
from ai_pet_typer import write_bio
##external data is get_pets, and ai bios is write_bio

##pull pets matching to filter
def run(species, zip_code, how_many):
    pets = get_pets(species, zip_code, how_many)
    if not pets:
        return "_No results. Try a different ZIP or species._"

    out = "# Adoptable pets\n\n"
    for a in pets:
        #extract key fields
        name = a.get("name","Pet")
        breed = (a.get("breeds") or {}).get("primary","Mixed")
        city = ((a.get("contact") or {}).get("address") or {}).get("city","")
        url = a.get("url","")
        
        ##request ai for short bio
        bio = write_bio(a)
        out += f"**{name}** — {breed} — {city}\n{bio}\n" + (f"[More info]({url})" if url else "") + "\n\n"
    return out

##gradio interface
demo = gr.Interface(
    fn=run,
    inputs=[gr.Dropdown(["Dog","Cat"], value="Dog", label="Species"),
            gr.Textbox(value="10001", label="ZIP / Postal"),
            gr.Slider(1, 10, value=3, step=1, label="How many")],
    outputs=gr.Markdown(),
    title="🐾 Simple Pet Adoption Helper",
    description="Fetch adoptable pets (Petfinder) and auto-write cute bios with TinyLlama (Ollama)."
)
##share for public
if __name__ == "__main__":
    demo.launch(share=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




