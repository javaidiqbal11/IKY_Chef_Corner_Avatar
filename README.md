# IKY Chef Corner Avatar

## Setup
Install packages in Python 3.10
```shell
pip install -r requirements.txt
```

Now run the flask app to test avatar
```shell
python app.py
```


## Key Points
- Design the framework for whole project
- PineCone dataset accessed and tested
- Integerate the OpenAI API 
- HeyGen login successfully and waiting for the credits in account
- Tested the Flask App with HeyGen Trial Token to complete POC 
- Working to build the RAG for retreiving recipies data from pinecone --- Knowldge Based 
- Working on the GPT Integeration module 
- Currently custom llm api endpoint not possible with h eygen.
- It uses webrtc to their server to fetch the stream events(audio) and uses stream event to handle speech on their end.
- GPT-4o is being used for interactive avatar when we provide the api key.
- The solution for now is to use the default web ui of heygen to add knowledge base and prompt strucutre to use the interactive avatar.
but it has limit of knowledge base size.
- Spanish Avatar in the HeyGen 

## Updates and Delivered 
- Design the framework for whole project
- PineCone dataset accessed and tested
- Integerate the OpenAI API 
- HeyGen login successfully and waiting for the credits in account
- Tested the Flask App with HeyGen Trial Token to complete POC 
- Working to build the knowledge based for retreiving recipies data from pinecone 
- Spanish Avatar with custom vidoe developed and integereated with pinecone 
  

### Heygen SDK

- [HeyGen Official Website](https://github.com/HeyGen-Official/StreamingAvatarSDK)

- [HeyGen Interactive Avatar](https://github.com/HeyGen-Official/InteractiveAvatarNextJSDemo)

- [HeyGen Interactive Avatar Labs](https://labs.heygen.com/interactive-avatar)
- [Project Required Features and R&D](https://docs.google.com/document/d/1v7VXisC4FvhdEpD_Wj6v79LxoW5FaXVWdMLR-_wzkYU/edit?tab=t.0)



### Knowledge Base Generation
I have added the script to generate the Knowledge Base from Pinecone for HeyGen.

## Interactive Avatars 
1. [HeyGen Interactive Avatar](https://www.heygen.com/pricing)
2. [DeepBrain Interactive Avatar](https://app.aistudios.com/avatars/paige/peach/M000187655)
3. [Akool Streaming Avatar](https://akool.com/pricing)
4. [Synthesia Avatar](https://www.synthesia.io/pricing)
