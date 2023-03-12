import openai as oai

oai.api_key = "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"

res = oai.Image.create(
    prompt="tiny robot",
    n=4,
    size="1024x1024",
)
    

print(res)