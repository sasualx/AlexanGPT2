from transformers import pipeline

generator = pipeline('text-generation',model='../ML/model_parameters', tokenizer='gpt2', config={'max_length':10000})

def generate_response(input):
    print(input)
    output = generator(input, do_sample=True, max_length=len(input.split())+60, top_k=50, top_p=0.95, num_returned_sequences=1)[0]['generated_text']
    return output[:output.rfind('\n')+1]
