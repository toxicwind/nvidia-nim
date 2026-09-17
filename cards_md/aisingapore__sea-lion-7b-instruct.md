---
title: "sea-lion-7b-instruct"
publisher: "aisingapore"
type: "endpoint"
updated: "2025-01-17T20:19:18.239Z"
description: "LLM to represent and serve the linguistic and cultural diversity of Southeast Asia"
canonical: "https://build.nvidia.com/aisingapore/sea-lion-7b-instruct"
---

# Model Overview

## Description

SEA-LION-7B-Instruct is a multilingual model for natural language understanding (NLU), natural language generation (NLG), and natural language reasoning (NLR) tasks that has been fine-tuned with thousands of English and Indonesian instruction-completion pairs alongside a smaller pool of instruction-completion pairs from other Association of Southeast Asian Nations (ASEAN) languages. These instructions have been carefully curated and rewritten to ensure the model was trained on truly open, commercially permissive and high quality datasets.  This model is for demonstration purposes and not-for-production usage.

SEA-LION stands for Southeast Asian Languages In One Network.

## Third-Party Community Consideration

This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to the [SEA-LION Model Card](https://huggingface.co/aisingapore/sea-lion-7b-instruct).

## License and Terms of use
<b>GOVERNING TERMS</b>: Your use of this API is governed by the <a href="https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf" rel="noreferrer" target="_blank">NVIDIA API Trial Service Terms of Use</a>; and the use of this model is governed by the <a href="https://docs.nvidia.com/ai-foundation-models-community-license.pdf" rel="noreferrer" target="_blank">NVIDIA AI Foundation Models Community License</a> and <a href="https://opensource.org/license/MIT" rel="noreferrer" target="_blank">MIT License</a>.

**Model Developer:** Products Pillar, AI Singapore <br> 
**Model Release Date:** Jan 31, 2024.

**Model Architecture** 
* Architecture Type: Transformer <br> 
* Network Architecture: MosaicML Pretrained Transformer (MPT)

**Input** 
* Input Type: Text
* Input Format: String
* Input Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed

**Output** 
* Output Type: Text
* Output Format: String

## Training dataset

SEA-LION-7B-Instruct was trained on a wide range of instructions that were manually and stringently verified by our team. A large portion of the effort was dedicated to ensuring that each instruction-completion pair that the model sees is of a high quality and any errors were corrected and rewritten by native speakers or else dropped from our mix.

In addition, special care was taken to ensure that the datasets used had commercially permissive licenses through verification with the original data source. 

## Benchmark Performance
SEA-LION-7B-Instruct was evaluated on the BHASA benchmark ([arXiv](https://arxiv.org/abs/2309.06085v2) and [GitHub](https://github.com/aisingapore/bhasa)) across a variety of tasks. 

BHASA stands out amongst other evaluations for SEA languages for its holistic approach to evaluation, including not just traditional Natural Language Processing (NLP) benchmarking tasks (such as sentiment analysis and question answering), but also linguistic and cultural diagnostic tests which are meticulously handcrafted. 

The evaluation was done zero-shot with Indonesian prompts and only a sample of 100-1000 instances for each dataset was used as per the setting described in the BHASA paper. The scores shown in the table below have been adjusted to only consider answers provided in the appropriate language.

| Model                          | QA (F1) | Sentiment (F1) | Toxicity (F1) | Eng>Indo (ChrF++) | Indo>Eng (ChrF++) | Summary (ROUGE-L) | NLI (Acc) | Causal (Acc) |
|--------------------------------|---------|----------------|---------------|-------------------|-------------------|-------------------|-----------|--------------|
| SEA-LION-7B-Instruct-Research  | 24.86   | 76.13          | 24.45         | 52.50             | 46.82             | 15.44             | 33.20     | 23.80        |
| SEA-LION-7B-Instruct           | **68.41**| **91.45**     | 17.98         | 57.48             | 58.04             | **17.54**         | 53.10     | 60.80        |
| SeaLLM 7B v1                   | 30.96   | 56.29          | 22.60         | 62.23             | 41.55             | 14.03             | 26.50     | 56.60        |
| SeaLLM 7B v2                   | 44.40   | 80.13          | **55.24**     | 64.01             | **63.28**         | 17.31             | 43.60     | 82.00        |
| Sailor-7B (Base)               | 65.43   | 59.48          | 20.48         | **64.27**         | 60.68             | 8.69              | 15.10     | 38.40        |
| Sailor-7B-Chat                 | 38.02   | 87.64          | 52.07         | 64.25             | 61.87             | 15.28             | **68.30** |**85.60**     |
| Llama 2 7B Chat                | 11.12   | 52.32          | 0.00          | 44.09             | 57.58             | 9.24              | 0.00      | 0.00         |
| Mistral 7B Instruct v0.1       | 38.85   | 74.38          | 20.83         | 30.60             | 51.43             | 15.63             | 28.60     | 50.80        |
| GPT-4 (gpt-4-0314)             | 73.60   | 74.14          | 63.96         | 69.38             | 67.53             | 18.71             | 83.20     | 96.00        |

- For Natural Language Understanding (NLU) tasks, the model was tested on Sentiment Analysis (`Sentiment`) using the NusaX dataset, Question Answering (`QA`) using the TyDiQA dataset, and Toxicity Detection (`Toxicity`) using the Indonesian Multi-Label Hate Speech Detection dataset. The metrics used are F1 scores for all three tasks.
- For Natural Language Generation (NLG) tasks, the model was tested on Machine Translation from English to Indonesian (`Eng>Indo`) and from Indonesian to English (`Indo>Eng`) using the FLORES-200 dataset, and Abstractive Summarization (`Summary`) using the XLSum dataset. The metrics used for Machine Translation and Abstractive Summarization are ChrF++ and ROUGE-L respectively.
- For Natural Language Reasoning (NLR) tasks, the model was tested on Natural Language Inference (`NLI`) using the IndoNLI lay dataset and on Causal Reasoning (`Causal`) using the XCOPA dataset. The metrics are based on accuracy for both tasks.

## Software Integration:
* Supported Hardware Platform(s): Lovelace <br>

**[Preferred/Supported] Operating System(s):** 
* Linux <br>

## Model Version

SEA-LION-7B-Instruct

## Inference

**Engine:** Triton + TensorRT-LLM <br>
**Test Hardware:** L40S <br>

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

```python
from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = ChatNVIDIA(
model="",
api_key="$NVIDIA_API_KEY", 
temperature=,
top_p=,
max_tokens=,
)

response = client.invoke([{"role":"user","content":""}])
print(response.content)
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
"model": "aisingapore/sea-lion-7b-instruct",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```