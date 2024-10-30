### Installation
**Setup** [Python 3.10](https://www.python.org/downloads/release/python-3100/)

1- Create Virtual Environment
```shell
python venv -m vir_env
```
2- Activate Virtual Environment
```shell
vir_env/Scripts/activate
```

3- Install packages in Python 3.10
```shell
pip install -r requirements.txt
```
4- Chnage Directory 
```text
cd basic-flask-template
```
5- Now run the flask app to test avatar
```shell
python app.py
```


**Notes:**
- Design the framework for whole project--- Done
- PineCone dataset accessed and tested---Done
- Integerate the OpenAI API ---- Done
- HeyGen login successfully and waiting for the credits in account---Wait
- Tested the Flask App with HeyGen Trial Token to complete POC --- Done
- Working to build the RAG for retreiving recipies data from pinecone --- In-Progress
- Working on the GPT Integeration module --- In-Progress
- Currently custom llm api endpoint not possible with heygen.
- It uses webrtc to their server to fetch the stream events(audio) and uses stream event to handle speech on their end.
- GPT-4o is being used for interactive avatar when we provide the api key.
- The solution for now is to use the default web ui of heygen to add knowledge base and prompt strucutre to use the interactive avatar. but it has limit of knowledge base size.

**Major Tasks:**
- Customize chef corner avatar from HeyGen
- RAG to retrive the recpies from Pinecone
- Conversational logic from OpenAi 


### Heygen SDK

https://github.com/HeyGen-Official/StreamingAvatarSDK

https://github.com/HeyGen-Official/InteractiveAvatarNextJSDemo

https://labs.heygen.com/interactive-avatar


### Keys
```text
OPENAI AI Avatars Secret Key --- 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

HeyGen --- not available in free version

Pinecone access --- marketing@iky.eu // IKnowYou@2024pin
database index
ikyeu

Pinecode api key
c8179f79-5b6b-4ff1-bcf7-1163df2f9055

host
https://ikyeu-e0d3co2.svc.aped-4627-b74a.pinecone.io

project id
8b453c19-3556-4655-bc64-13ea7a03e571

WordPress --- https://iky.eu/wp-admin  // webmaster@iky.eu // UqJ3V#FYl)PzCegcgakymLja

SFTP main --- 185.197.195.151 // root // 09!abv34Z1```


