# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:30:06 2024

@author: piyush.raj
"""

'Image Generator Website https://fal.ai/dashboard'

import fal_client
import os
import webbrowser
import pandas as pd

class img_generator():
    def __init__(self):
        self.cred=pd.read_excel(r'FAL_KEY_cred.xlsx')
        os.environ['FAL_KEY']=self.cred['FAL_KEY'][0] # My API KEY
        if not os.getenv('FAL_KEY'):
            raise Exception("FAL_KEY environment variable is not set!")    
        print("FAL_KEY environment variable is set successfully.")
        
    def sdxl_image_generator(self,prompt):
        handler = fal_client.submit(
            "fal-ai/fast-sdxl",
            arguments={
                "prompt": prompt
            },
        )
        result = handler.get()
        url=result['images'][0]['url']
        return url
    
    def flux_image_generator(self,prompt):
        handler = fal_client.submit(
            "fal-ai/flux/dev",
            arguments={
                "prompt": prompt
            },
        ) 
        result = handler.get()
        url=result['images'][0]['url']
        return url
        

              
