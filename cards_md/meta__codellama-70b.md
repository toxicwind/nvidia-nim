---
title: "codellama-70b"
publisher: "meta"
type: "endpoint"
updated: "2025-03-31T19:29:19.449Z"
description: "LLM capable of generating code from natural language and vice versa."
canonical: "https://build.nvidia.com/meta/codellama-70b"
---

# Model Overview

## Description:

Code Llama is a large language artificial intelligence (AI) model that generates code and natural language about code built from a collection of models based on [Llama 2](https://ai.meta.com/llama/).

## Third-Party Community Consideration:

This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see [Meta's Code Llama Model Card](https://github.com/facebookresearch/codellama/blob/main/MODEL_CARD.md).

## Terms of use

By accessing this model, you are agreeing to the LLama 2 Terms and Conditions of the [License](https://ai.meta.com/resources/models-and-libraries/llama-downloads), [Acceptable Use Policy](https://l.facebook.com/l.php?u=https%3A%2F%2Fai.meta.com%2Fllama%2Fuse-policy&h=AT17YXIWa1dxwuzDq96w614_oshaUCWIQYHHHf9BgC0X5UK39DW2tpSP6NzkeadQVs0XBaNlFSo4nydTUcKB5r-Kn4OLs_5IbMEZYAf5hUvyzIwx8-mLom2ic1vw5rSPFUoc9A) and [Meta’s Privacy Policy](https://www.facebook.com/privacy/policy/)

## References(s):

[Code Llama: Open Foundation Models for Code Paper](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/) <br>
[Meta's Code Llama Model Card](https://github.com/facebookresearch/codellama/blob/main/MODEL_CARD.md) <br>

## Model Architecture:

**Architecture Type:** Transformer <br>
**Network Architecture:** Llama 2 <br>
**Model Version:** 0.1 <br>

## Input:

**Input Format:** Text <br>
**Input Parameters:** Temperature, Top P (Nucleus Sampling); Max Token Input 100k <br>

## Output:

**Output Format:** Text (code) <br>
**Output Parameters:** Max Output Tokens <br>

## Software Integration:

**Supported Hardware Platform(s):** Hopper, Ampere, Turing <br>
**Supported Operating System(s):** Linux <br>

# Training & Finetuning:

## Dataset:

**Data Collection Method by dataset:** Unknown <br>

**Labeling Method by dataset:** Not applicable <br>

Near-deduplicated dataset of publicly available code, property of Meta. 8% of samples data are sourced from natural language datasets related to code and contain discussions about code and code snippets included in natural language questions or answers. To help the model retain natural language understanding skills, dataset also inclues a small
proportion of batches from a natural language dataset.

# Inference:

**Engine:** [Triton](https://developer.nvidia.com/triton-inference-server) <br>
**Test Hardware:** Other <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards [Insert Link to Model Card++ here].  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

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
"model": "meta/codellama-70b",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```