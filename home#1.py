import openai as oai

oai.api_key = ""

res = oai.Image.create(
    prompt="tiny robot",
    n=4,
    size="1024x1024",
)
    

print(res)
