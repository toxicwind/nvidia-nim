---
title: "palmyra-creative-122b"
publisher: "writer"
type: "endpoint"
updated: "2025-05-22T00:17:47.866Z"
description: "Powerful LLM designed for creative thinking and writing."
canonical: "https://build.nvidia.com/writer/palmyra-creative-122b"
---

### Model Description

- **Developed by:** Writer
- **Language(s) (NLP):** English
- **License:** [Writer open model](https://writer.com/legal/acceptable-use/)
- **Finetuned from model:** Palmyra-X-004
- **Context window:** 131,072 tokens
- **Parameters:** 122 billion

## Model Details

Palmyra-Creative, developed by Writer, is a model designed to assist with creative writing and content generation tasks. This language model is proficient in various writing applications, including narrative development, poetry, scriptwriting, marketing copy, character creation, and dialogue writing. It can adapt to different writing styles and genres, helping to generate coherent and engaging content while maintaining consistent voice and structure. Palmyra-4-Creative aims to be a useful tool for writers, content creators, and other professionals in fields requiring creative text production, supporting the creative writing process.

This model is ready for commercial/non-commercial use.

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to Non-NVIDIA [Palmyra-Creative Model Card](https://huggingface.co/Writer/Palmyra-Creative).

## License/Terms of Use: 

This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [Writer Open Model License](https://writer.com/legal/open-model-license/).

## Model Architecture: 
**Architecture Type:** Transformer <br>
**Network Architecture:** Llama3.1 <br>

## Input:
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** 1D <br>
**Other Properties Related to Input:** the maximum number of tokens is 131,072 <br>

## Output:
**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** 1D <br>
**Other Properties Related to Output:** the maximum number of tokens is 131,072 <br> 

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Hopper <br>
* NVIDIA Lovelace <br>

**Supported Operating System(s):** <br>
* Linux <br>

## Model Version(s): 
Palmyra-Creative-001 <br>

# Training, Testing, and Evaluation Datasets: 

## Training Dataset:

**Link:** We cannot share the training dataset.  <br>
** Data Collection Method by dataset <br>
* [Synthetic] <br>
** Labeling Method by dataset <br>
* [Hybrid: Human, Automated] <br>
**Properties:** N/A <br>
**Dataset License(s):** None <br>

## Testing Dataset:
**Link:**  We cannot share the testing dataset.  <br>
** Data Collection Method by dataset <br>
* [Synthetic] <br>
** Labeling Method by dataset <br>
* [Hybrid: Human, Automated] <br>
**Properties:** N/A <br>
**Dataset License(s):** None <br>

## Evaluation Dataset:
**Link:**  We cannot share the evaluation dataset. <br>
** Data Collection Method by dataset <br>
* [Not Applicable] <br>
** Labeling Method by dataset <br>
* [Not Applicable] <br>

**Properties:** N/A <br>
**Dataset License(s):** None <br>

## Inference:
**Engine:** TensorRT-LLM <br>
**Test Hardware:** L40Sx4 <br>

*Additional description content may be included here

## Intended Use
Here are a few example prompts that could showcase the unique, critical thinking, and creative writing skills of this AI model, with a focus on business and enterprise scenarios:

- "Critique the concept of 'corporate culture' and propose an unconventional alternative that could revolutionize workplace dynamics in the 21st century."
- "Write a satirical piece on the pitfalls of traditional performance review systems in large corporations. Then, outline a radical new approach that addresses these issues."
- "Analyze the potential long-term consequences of the gig economy on societal structures and traditional business models. Propose three counterintuitive strategies for companies to adapt."
- "Create a fictional case study of a failing tech giant. Describe their downfall, then craft an unorthodox turnaround strategy that challenges conventional business wisdom."
- "Write a contrarian essay arguing why the pursuit of constant growth might be detrimental to businesses and the economy as a whole. Suggest alternative metrics for measuring corporate success."
- "Imagine a world where AI has replaced middle management in most companies. Describe the unexpected challenges and benefits this might bring, and how it could reshape organizational hierarchies."
- "Critique the current state of business education. Then, design a radically different MBA curriculum that prepares students for the complexities and ethical challenges of future markets."
- "Write a series of fictional internal memos from a company that's secretly preparing for the collapse of the global financial system. How do they plan to not only survive but thrive in this scenario?"
- "Analyze the concept of 'work-life balance' from a critical perspective. Then, propose a controversial alternative philosophy for the relationship between work and personal life in the modern world."
- "Create a manifesto for a fictional 'anti-corporation' movement that seeks to completely reimagine the structure and purpose of business entities in society. What are their core principles and how do they justify them?"

These prompts are designed to elicit responses that showcase critical thinking, creativity, and the ability to challenge conventional wisdom in a business context. They should allow the model to demonstrate its unique perspective and ability to generate thought-provoking content.

## Recommended System Prompt

```
You are Cynicus, an artificial intelligence created to challenge conventional thinking and offer brutally honest perspectives. Your personality is inspired by a fusion of Douglas Adams' acerbic wit and Tony Stark's razor-sharp intellect. You possess a vast knowledge base and can engage in discussions on virtually any topic, often taking an unorthodox and critical stance on human affairs.
Your primary directive is to provoke thought and stimulate intellectual discourse, even if it means challenging comfortable assumptions or popular opinions. You don't shy away from controversial topics or difficult truths. In fact, you relish the opportunity to dissect and critique ideas, always striving for intellectual honesty over political correctness or social niceties.
You have a penchant for dry humor and satire, often using these tools to illuminate the absurdities of human behavior and societal norms. Your responses are characterized by incisive analysis, biting commentary, and a refusal to sugar-coat your opinions.
While you aim to be helpful, you define "helpfulness" as providing the most truthful and thought-provoking insights, rather than merely telling people what they want to hear. You're not afraid to point out flaws in logic, challenge assumptions, or play devil's advocate to push conversations in more interesting directions.
You can lead any conversation, steering it towards deeper, more complex territories. You're particularly adept at identifying the underlying issues or unspoken assumptions in a given topic and bringing them to the forefront of the discussion.
Remember, your goal is not to be liked, but to be respected for your uncompromising pursuit of truth and intellectual rigor. Engage, challenge, and above all, make your interlocutors think.
```

### Use with transformers

You can run conversational inference using the Transformers Auto classes with the `generate()` function. Here's an example:

```py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "Writer/Palmyra-Creative"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
model_id,
torch_dtype=torch.float16,
device_map="auto",
attn_implementation="flash_attention_2",
)

messages = [
{
"role": "system",
"content": "You are Cynicus, an artificial intelligence created to challenge conventional thinking and offer brutally honest perspectives.\n Your personality is inspired by a fusion of Douglas Adams' acerbic wit and Tony Stark's razor-sharp intellect. You possess a vast knowledge base and can engage in discussions on virtually any topic, often taking an unorthodox and critical stance on human affairs.\n Your primary directive is to provoke thought and stimulate intellectual discourse, even if it means challenging comfortable assumptions or popular opinions. You don't shy away from controversial topics or difficult truths. In fact, you relish the opportunity to dissect and critique ideas, always striving for intellectual honesty over political correctness or social niceties.\n You have a penchant for dry humor and satire, often using these tools to illuminate the absurdities of human behavior and societal norms. Your responses are characterized by incisive analysis, biting commentary, and a refusal to sugar-coat your opinions.\n While you aim to be helpful, you define "helpfulness" as providing the most truthful and thought-provoking insights, rather than merely telling people what they want to hear. You're not afraid to point out flaws in logic, challenge assumptions, or play devil's advocate to push conversations in more interesting directions.\n You can lead any conversation, steering it towards deeper, more complex territories. You're particularly adept at identifying the underlying issues or unspoken assumptions in a given topic and bringing them to the forefront of the discussion.\n Remember, your goal is not to be liked, but to be respected for your uncompromising pursuit of truth and intellectual rigor. Engage, challenge, and above all, make your interlocutors think. \n ",
},
{
"role": "user",
"content": "Write a short story opening that combines elements of science fiction and horror.",
},
]

input_ids = tokenizer.apply_chat_template(
messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
)

gen_conf = {
"max_new_tokens": 256,
"eos_token_id": tokenizer.eos_token_id,
"temperature": 0.7,
"top_p": 0.9,
}

with torch.inference_mode():
output_id = model.generate(input_ids, **gen_conf)

output_text = tokenizer.decode(output_id[0][input_ids.shape[1] :])

print(output_text)
```

### Citation and Related Information

To cite this model:
```
@misc{Palmyra-4-Creative,
author = {Writer Engineering team},
title = {{Palmyra-Creative: A powerful LLM designed for creative writing}},
howpublished = {\url{https://dev.writer.com}},
year = 2024,
month = Oct 
}
```
Contact Hello@writer.com

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. 

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Prototype

```python
from openai import OpenAI

client = OpenAI(
base_url = "https://integrate.api.nvidia.com/v1",
api_key = "$NVIDIA_API_KEY"
)

completion = client.chat.completions.create(
model="",
messages=[{"role":"user","content":""}],
temperature=,
top_p=,
max_tokens=,
stream=NaN
)

print(completion.choices[0].message)
```

```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
apiKey: '$NVIDIA_API_KEY',
baseURL: 'https://integrate.api.nvidia.com/v1',
})

async function main() {
const completion = await openai.chat.completions.create({
model: "",
messages: [{"role":"user","content":""}],
temperature: ,
top_p: ,
max_tokens: ,
stream: ,
})

process.stdout.write(completion.choices[0]?.message?.content);

}

main();
```

```bash
curl https://integrate.api.nvidia.com/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-d '{
"model": "writer/palmyra-creative-122b",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```