from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import openai

# Initialize a client
pc = Pinecone(api_key='c8179f79-5b6b-4ff1-bcf7-1163df2f9055')

# get API key from top-right dropdown on OpenAI website
openai.api_key = "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"
# Create a serverless index
index_name = "ikyeu"
limit = 3750

index = pc.Index(index_name)


print(index.describe_index_stats())

embed_model = "text-embedding-ada-002"
query = "How to make Whispery Rice?"
# res = openai.embeddings.create(
#     input=[
#         query
#     ], model=embed_model
# )
# xq = res.data[0].embedding
# res = index.query(xq, top_k=2, include_metadata=True)
#
# print(res)

# res = index.query(xq, top_k=3, include_metadata=True)


def complete(prompt):
    res = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": [{"type": "text", "text":prompt}]}],
        temperature=0,
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return res.choices[0].message.content


def retrieve(query):
    res = openai.embeddings.create(
        input=[query],
        model=embed_model
    )

    # retrieve from Pinecone
    xq = res.data[0].embedding

    # get relevant contexts
    res = index.query(xq, top_k=5, include_metadata=True)
    contexts = [
        x['metadata']['text'] for x in res['matches']
    ]

    # build our prompt with the retrieved contexts included
    prompt_start = (
        "Answer the question based on the context below.\n\n"+
        "Context:\n"
    )
    prompt_end = (
        f"\n\nQuestion: {query}\nAnswer:"
    )
    # append contexts until hitting limit
    for i in range(1, len(contexts)):
        if len("\n\n---\n\n".join(contexts[:i])) >= limit:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts[:i-1]) +
                prompt_end
            )
            break
        elif i == len(contexts)-1:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(contexts) +
                prompt_end
            )
    return prompt

query_with_contexts = retrieve(query)

print(complete(query_with_contexts))