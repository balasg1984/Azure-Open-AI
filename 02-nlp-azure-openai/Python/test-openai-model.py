import os
from dotenv import load_dotenv

import openai


def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_MODEL")
        
        # Read text from file
        
        text = open(file="C:/Users/balag/azure-openai/Labfiles/02-nlp-azure-openai/text-files/sample-text.txt", encoding="utf8").read()
        
        # Set OpenAI configuration settings
        openai.api_type = "azure"
        openai.api_base = azure_oai_endpoint
        openai.api_version = "2023-03-15-preview"
        openai.api_key = azure_oai_key
        
         # Send request to Azure OpenAI model
        print("Sending request for summary to Azure OpenAI endpoint...\n\n")
        response = openai.ChatCompletion.create(
         engine=azure_oai_model,
         temperature=1,
         max_tokens=120,
         messages=[
         {"role": "system", "content": "You are a helpful assistant. Summarize the following text in 60 words or less."},
         {"role": "user", "content": text}
         ]
 )

        print("Summary: " + response.choices[0].message.content + "\n")

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()