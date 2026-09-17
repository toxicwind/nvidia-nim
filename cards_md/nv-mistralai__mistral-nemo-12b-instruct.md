---
title: "mistral-nemo-12b-instruct"
publisher: "nv-mistralai"
type: "endpoint"
updated: "2025-07-09T14:53:01.634Z"
description: "Most advanced language model for reasoning, code, multilingual tasks; runs on a single GPU."
canonical: "https://build.nvidia.com/nv-mistralai/mistral-nemo-12b-instruct"
---

# Model Overview

## Description:
Mistral-NeMo is a Large Language Model (LLM) composed of 12B parameters.  This model leads accuracy on popular benchmarks across common sense reasoning, coding, math, multilingual and multi-turn chat tasks; it significantly outperforms existing models smaller or similar in size.

This model is ready for commercial use. 

### Key features
1. Released under the Apache 2 License
2. Pre-trained and instructed versions
3. Trained with a 128k context window
4. Trained on a large proportion of multilingual and code data
5. Drop-in replacement of Mistral 7B

## Joint-Party Community Consideration
This model was a jointly trained by Mistral and NVIDIA.

## License & Terms of use
Your use of this API is governed by [the NVIDIA API Trial Service Terms of Use](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf); and the use of this model is governed by [the NVIDIA AI Foundation Models Community License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-ai-foundation-models-community-license-agreement/).  Mistral NeMo-12B is released under the Apache 2.0 license.

## References(s):
Mistral NeMo 12B [Blogpost](https://mistral.ai/news/mistral-nemo/)

## Model Architecture:
**Architecture Type:** Transformer <br>
**Network Architecture:** Mistral <br>
**Model Version:** 0.1 <br>

This transformer model has the following characteristics:
* Layers: 40
* Dim: 5,120
* Head dim: 128
* Hidden dim: 14,436
* Activation Function: SwiGLU
* Number of heads: 32
* Number of kv-heads: 8 (GQA)
* Rotary embeddings (theta = 1M)
* Vocabulary size: 2**17 ~= 128k

**Input** 
* Input Type: Text
* Input Format: String
* Input Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed

**Output** 
* Output Type: Text
* Output Format: String

## Software Integration:
* Supported Hardware Platform(s): NVIDIA Hopper 
* Preferred Operating System(s): Linux <br>

### Benchmarks
#### Main benchmarks
- HellaSwag (0-shot): 83.5%
- Winogrande (0-shot): 76.8%
- OpenBookQA (0-shot): 60.6%
- CommonSenseQA (0-shot): 70.4%
- TruthfulQA (0-shot): 50.3%
- MMLU (5-shot): 68.0%
- TriviaQA (5-shot): 73.8%
- NaturalQuestions (5-shot): 31.2%
#### Multilingual benchmarks
- MMLU
-  French: 62.3%
-  German: 62.7%
-  Spanish: 64.6%
-  Italian: 61.3%
-  Portuguese: 63.3%
-  Russian: 59.2%
-  Chinese: 59.0%
-  Japanese: 59.0%
#### Instruct benchmarks
- MT Bench (dev): 7.84
- MixEval Hard: 0.534
- IFEval-v5: 0.629
- Wildbench: 42.57

## Inference
**Engine:** TensorRT-LLM <br>
**Test Hardware:** H100

## Ethical Considerations:
When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

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
"model": "nv-mistralai/mistral-nemo-12b-instruct",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```