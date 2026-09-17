---
title: "granite-34b-code-instruct"
publisher: "ibm"
type: "endpoint"
updated: "2025-07-20T16:37:31.210Z"
description: "Software programming LLM for code generation, completion, explanation, and multi-turn conversion."
canonical: "https://build.nvidia.com/ibm/granite-34b-code-instruct"
---

# Model Overview

## Description

Granite-34B-Code-Instruct generates, explains, and translates code from a natural language prompt.  It is a 34B parameter model fine tuned from Granite-34B-Code-Base on a combination of permissively licensed instruction data to enhance instruction following capabilities including logical reasoning and problem-solving skills.  This model is ready for commercial use.

## Third-Party Community Consideration

This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to the [Granite-34B-Code-Instruct  Model Card](https://huggingface.co/ibm-granite/granite-34b-code-instruct).

## License and Terms of use
<b>GOVERNING TERMS</b>: Your use of this API is governed by the <a href="https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf" rel="noreferrer" target="_blank">NVIDIA API Trial Service Terms of Use</a>; and the use of this model is governed by the <a href="https://docs.nvidia.com/ai-foundation-models-community-license.pdf" rel="noreferrer" target="_blank">NVIDIA AI Foundation Models Community License</a> and <a href="https://apache.org/licenses/LICENSE-2.0" rel="noreferrer" target="_blank">Apache 2.0 License</a>.

**Model Developer:** IBM Research <br> 
**Model Release Date:** May 6th, 2024

**Model Architecture** 
* Architecture Type: Transformer <br> 
* Network Architecture: GPT Big Code

**Input** 
* Input Type: Text
* Input Format: String
* Input Parameters: max_tokens, temperature, top_p, stop, frequency_penalty, presence_penalty, seed

**Output** 
* Output Type: Text
* Output Format: String

## Software Integration:
* Supported Hardware Platform(s): NVIDIA Hopper <br>

**[Preferred/Supported] Operating System(s):** 
* Linux <br>

## Training Data
Granite Code Instruct models are trained on the following types of data.
* Code Commits Datasets: we sourced code commits data from the [CommitPackFT](https://huggingface.co/datasets/bigcode/commitpackft) dataset, a filtered version of the full CommitPack dataset. From CommitPackFT dataset, we only consider data for 92 programming languages. Our inclusion criteria boils down to selecting programming languages common across CommitPackFT and the 116 languages that we considered to pretrain the code-base model (*Granite-8B-Code-Base*). 
* Math Datasets: We consider two high-quality math datasets, [MathInstruct](https://huggingface.co/datasets/TIGER-Lab/MathInstruct) and [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA). Due to license issues, we filtered out GSM8K-RFT and Camel-Math from MathInstruct dataset. 
* Code Instruction Datasets: We use [Glaive-Code-Assistant-v3](https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v3), [Glaive-Function-Calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2), [NL2SQL11](https://huggingface.co/datasets/bugdaryan/sql-create-context-instruction) and a small collection of synthetic API calling datasets.
* Language Instruction Datasets: We include high-quality datasets such as [HelpSteer](https://huggingface.co/datasets/nvidia/HelpSteer) and an open license-filtered version of [Platypus](https://huggingface.co/datasets/garage-bAInd/Open-Platypus). We also include a collection of hardcoded prompts to ensure our model generates correct outputs given inquiries about its name or developers.

## Inference

**Engine:** Triton + TensorRT-LLM <br>
**Test Hardware:** H100 <br>

## Ethical Considerations and Limitations
Granite code instruct models are primarily finetuned using instruction-response pairs across a specific set of programming languages. Thus, their performance may be limited with out-of-domain programming languages. In this situation, it is beneficial providing few-shot examples to steer the model's output. Moreover, developers should perform safety testing and target-specific tuning before deploying these models on critical applications. The model also inherits ethical considerations and limitations from its base model. For more information, please refer to *[Granite-34B-Code-Base](https://huggingface.co/ibm-granite/granite-34b-code-base)* model card.

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
"model": "ibm/granite-34b-code-instruct",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```