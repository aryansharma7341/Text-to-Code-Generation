import torch
from transformers import AutoTokenizer,AutoModelForCausalLM
from peft import LoraConfig, get_peft_model
from transformers import BitsAndBytesConfig

from flask import Flask, render_template, request
import requests


# Create a Flask web application
app = Flask(__name__)




model_id = "EleutherAI/gpt-neo-2.7B"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_min_max_vals=None
)
device = "cuda:0"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map='cuda',  trust_remote_code=True)

lora_config = LoraConfig.from_pretrained('D:/study material/My Projects/Text-to-code-generation/my_text-to-code-model')
model = get_peft_model(model, lora_config)

@app.route('/', methods=['POST', 'GET'])
def recommend():
    return render_template('welcome.html')

@app.route('/Query_And_Code', methods=['POST', 'GET'])
def query_code():
    if request.method == 'POST':

        User_Query = str(request.form['input_query'])

        inputs = tokenizer(User_Query, return_tensors="pt").to(device)
        outputs = outputs = model.generate(**inputs,max_new_tokens=150,num_beams=10, temperature=0.2, no_repeat_ngram_size=3, repetition_penalty=1.5,
                                            length_penalty=0.8, pad_token_id=50256, num_return_sequences=1)

        print(tokenizer.decode(outputs[0], skip_special_tokens=True))

        Code_Output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print('THE INPUT QUERY IS')
        print("\n")
        print(User_Query)
        print(Code_Output)
        return render_template('output_page.html', result=Code_Output)

    else:
        return render_template('text.html')




