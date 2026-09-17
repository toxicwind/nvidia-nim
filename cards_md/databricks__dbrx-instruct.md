---
title: "dbrx-instruct"
publisher: "databricks"
type: "endpoint"
updated: "2025-05-22T19:14:13.120Z"
description: "A general-purpose LLM with state-of-the-art performance in language understanding, coding, and RAG."
canonical: "https://build.nvidia.com/databricks/dbrx-instruct"
---

# Model Overview
## Description:

DBRX is a transformer-based decoder-only large language model (LLM) that was trained using next-token prediction. It uses a fine-grained mixture-of-experts (MoE) architecture with 132B total parameters of which 36B parameters are active on any input. 

Compared to other open MoE models like Mixtral-8x7B and Grok-1, DBRX is fine-grained, meaning it uses a larger number of smaller experts. DBRX has 16 experts and chooses 4, while Mixtral-8x7B and Grok-1 have 8 experts and choose 2. This provides 65x more possible combinations of experts and we found that this improves model quality. DBRX uses rotary position encodings (RoPE), gated linear units (GLU), and grouped query attention (GQA). It uses a converted version of the GPT-4 tokenizer as defined in the tiktoken repository. We made these choices based on exhaustive evaluation and scaling experiments.

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to Non-NVIDIA [DBRX Model Card](https://huggingface.co/databricks/dbrx-instruct).

## License and Terms of use
<b>GOVERNING TERMS</b>: Your use of this API is governed by the <a href="https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf" rel="noreferrer" target="_blank">NVIDIA API Trial Service Terms of Use</a>; and the use of this model is governed by the <a href="https://docs.nvidia.com/ai-foundation-models-community-license.pdf" rel="noreferrer" target="_blank">NVIDIA AI Foundation Models Community License</a> and <a href="https://www.databricks.com/legal/open-model-license" rel="noreferrer" target="_blank">Databricks Open Model License</a>.
## References(s):
[Blog post](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm)

## Model Architecture: 
**Architecture Type:** Transformer <br>
**Network Architecture:** Fine-grained Mixture of Experts (MoE) <br>

## Input:
**Input Format:** Text <br>
**Input Parameters:** Temperature, Top P, Max Output Tokens <br>

## Output: 
**Output Format:** Text <br>

## Software Integration:
* Supported Hardware Platform(s): Hopper <br>

**[Preferred/Supported] Operating System(s):** 
* Linux <br>

# Training, Testing, and Evaluation Datasets: 

## Training Dataset:

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Pre-trained on 12T tokens of text and code data.<br>

## Inference:
Engine: Triton, TRT-LLM <br>
Test Hardware: H100

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
"model": "databricks/dbrx-instruct",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```