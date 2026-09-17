---
title: "palmyra-fin-70b-32k"
publisher: "writer"
type: "endpoint"
updated: "2025-05-22T00:17:55.901Z"
description: "Specialized LLM for financial analysis, reporting, and data processing"
canonical: "https://build.nvidia.com/writer/palmyra-fin-70b-32k"
---

## Model Description

- Developed by: Writer
- Model type: Llama
- Language(s) (NLP): English
- Parameters: 70 billion
- Finetuned from model: Palmyra-X-004
- Model Version: 0.1

## Model Details

Palmyra-Fin-70B-32K excels in analyzing and summarizing complex financial reports, market data, and economic indicators, extracting key information to generate concise, structured summaries; it is a model built by Writer specifically to meet the needs of the financial industry. It is a leading LLM on financial benchmarks, outperforming other large language models in various financial tasks and evaluations.

This model is ready for commercial use.

By leveraging its deep understanding of financial terminology, the model enhances information retrieval, data analysis, and knowledge discovery from financial reports, research articles, and other economic sources. These capabilities support applications like investment analysis, risk management, and financial research.

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to the (Hugging Face) Model Card (https://huggingface.co/Writer/Palmyra-Fin-70B-32K).

### License/Terms of Use: 
The trial service is governed by the NVIDIA API Service Agreement; and the use of this model is governed by the (Writer Open Model License)[https://writer.com/legal/open-model-license/].

## Specialized for Financial Applications

Palmyra-Fin-70B-32K is meticulously designed to meet the unique linguistic and knowledge demands of the finance and economics sectors. It has been fine-tuned on an extensive collection of high-quality financial data, ensuring it can comprehend and generate text with precise domain-specific accuracy and fluency.

Our system integrates a specialized internal finance dataset and a well-crafted fine-tuning recipe, making it highly adept at handling the specific needs of this field. Key components of our training pipeline include:

- Specialized Dataset: Utilizing a proprietary internal finance dataset to enhance the model's performance.
- Fine-tuning approach: Custom financial instruction dataset (Writer in-house build)

## Intended Use

### Intended Use Cases
Palmyra-Fin-70B-32K is intended for use in English for financial analysis, market trend prediction, risk assessment, financial report generation, and automated financial advice. It excels at answering questions from long financial documents, making it ideal for in-depth financial research and analysis.

### Out-of-Scope
Use in any manner that violates applicable laws or regulations (including trade compliance laws). Use in any other way that is prohibited by [Writer's Acceptable Use Policy](https://writer.com/legal/acceptable-use/) and [the Writer open model license](https://writer.com/legal/acceptable-use/). Use in languages other than English.

**Note:** Users should be aware that while the model is highly capable, it should not be used as the sole basis for making significant financial decisions.

## Model Architecture: 
**Architecture Type:** Transformer-Based  <br>
**Network Architecture:** Llama <br>

## Input:
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Input:** - Context window: 32,768 tokens <br>

## Output:
**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** [(2D, 3D)] <br>

### Use with transformers 

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "Writer/Palmyra-Fin-70B-32K"

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
"content": "You are a highly knowledgeable and experienced expert in the financial sector, possessing extensive knowledge and practical expertise in financial analysis, markets, investments, and economic principles.",
},
{
"role": "user",
"content": "Can you explain how central banks printing more money (quantitative easing) affects the stock market and how investors might react to it?",
},
]

input_ids = tokenizer.apply_chat_template(
messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
)

gen_conf = {
"max_new_tokens": 1024,
"eos_token_id": tokenizer.eos_token_id,
"temperature": 0.0,
"top_p": 0.9,
}

with torch.inference_mode():
output_id = model.generate(input_ids, **gen_conf)

output_text = tokenizer.decode(output_id[0][input_ids.shape[1] :])

print(output_text)
```

## Model Version(s): 
nim_palmyra-fin-70b-32k_h100x2 [0.1]  <br>

## Evaluation Results

Palmyra-Fin-70B-32K outperforms other models on internal finance evaluations, achieving state-of-the-art results across various financial datasets. Its strong performance in tasks like financial document analysis, market trend prediction, and risk assessment underscores its effective grasp of financial knowledge.

Key Performance Metrics:

- 100% accuracy on needle-in-haystack tasks
- Superior performance on internal finance evaluations compared to other models

Palmyra-Fin-70B-32K achieves 100% accuracy on needle-in-haystack tasks across its entire 32,768 token context window, demonstrating exceptional capability in precise information extraction from extensive financial documents.

## Long-Fin-Eval Performance:

To further assess the model's capabilities, we developed and conducted an evaluation using long-fin-eval, an internally created benchmark designed to simulate real-world financial use cases. This evaluation consists of samples containing long documents paired with high-quality question-answer sets. The model's task is to generate responses based on the provided document and question, with the output evaluated by GPT-4 Turbo.

The long-fin-eval methodology assesses both the model's information retrieval capabilities and its ability to engage in extended dialogue on complex financial topics. This approach provides insight into the model's capacity to process and synthesize information from lengthy financial documents while maintaining coherent and contextually appropriate conversational output.

In this evaluation, Palmyra-Fin-70B-32K showed superior performance compared to both open-source and proprietary benchmark models. These results indicate the model's effectiveness in addressing real-world financial applications that require both comprehensive understanding of extensive documents and the ability to articulate nuanced insights.

|  model name          | long-fin-eval  |
| -------------------- | -------------- |
|  Palmyra-Fin-70B-32K |      9.04      |  
|  Claude 3.5 Sonnet   |      9.02      |  
|  Qwen-2 70B instruct |      8.9       |  
|  gpt-4o              |      8.72      |
|  palmyra-fin-56b     |      8.23      |
|  mixtral-8x7b        |      7.57      |  

## Inference:
**Engine:** TensorRT <br>
**Test Hardware [Name the specific test hardware model]:** <br>
* H100 <br>

## Bias, Risks, and Limitations

Palmyra-Fin-70B-32K, despite leveraging high-quality data, may contain inaccuracies, biases, or misalignments and has not been rigorously evaluated in real-world financial settings.

It is advised not to use the model for direct financial decision-making or professional financial advice without human oversight. Instead, its use should be confined to research and analysis by qualified individuals who understand its limitations. Palmyra-Fin-70B-32K should not replace professional financial judgment, and adapting it for critical financial use would require extensive additional work, including thorough testing, regulatory compliance, bias mitigation, and human oversight. Always consult a qualified financial professional for personal financial needs.

## Citation and Related Information
To cite this model:
```
@misc{Palmyra-Fin-70B-32k,
author = {Writer Engineering team},
title = {{Palmyra-Fin-70B-32k: a powerful LLM designed for Finance}},
howpublished = {\url{https://dev.writer.com}},
year = 2024,
month = July 
}
```
Contact Hello@writer.com

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
"model": "writer/palmyra-fin-70b-32k",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```