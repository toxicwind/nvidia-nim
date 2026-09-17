---
title: "riva-translate-4b-instruct"
publisher: "nvidia"
type: "endpoint"
updated: "2025-07-10T06:02:38.503Z"
description: "Translation model in 12 languages with few-shots example prompts capability."
canonical: "https://build.nvidia.com/nvidia/riva-translate-4b-instruct"
---

# Model Overview

### Description:
The Riva-Translate-4B-Instruct Neural Machine Translation model translates text in 12 languages. The supported languages are: English(en), German(de), European Spanish(es-ES), LATAM Spanish(es-US), France(fr), Brazillian Portugese(pt-BR), Russian(ru), Simplified Chinese(zh-CN), Traditional Chinese(zh-TW), Japanese(ja),Korean(ko), Arabic(ar). 
This model is ready for commercial use. <br> 

### License/Terms of Use
NIM Package: [NVIDIA AI Foundation Models Community License Agreement](https://docs.nvidia.com/ai-foundation-models-community-license.pdf) <br> 
Downloadable NIM: [NVIDIA AI Foundation Models Community License Agreement](https://docs.nvidia.com/ai-foundation-models-community-license.pdf) <br>    
HuggingFace Model: [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) <br> 
Model preview in API catalog: [NVIDIA Open Model License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/) <br> 

### Deployment Geography:
Global <br>

### Use Case: <br>
Translators, marketers, and web developers who deliver content in multiple languages. <br>

### Release Date:  <br>
Huggingface 06/05/2025 via https://huggingface.co/nvidia/Riva-Translate-4B-Instruct <br> 

## References(s):
[1] Vaswani, Ashish, et al. "Attention is all you need." arXiv preprint arXiv:1706.03762 (2017).
[2] https://github.com/openai/tiktoken
[3] https://en.wikipedia.org/wiki/BLEU
[4] https://github.com/mjpost/sacreBLEU
[5] https://github.com/Unbabel/COMET
[6] NVIDIA NeMo Toolkit
<br> 

## Model Architecture:
**Architecture Type:** Transformer <br>

**Network Architecture:** Decoder-only <br>

This model was developed based on Transformer architecture originally presented in "Attention Is All You Need" paper [1]. It is a fine-tuned version of a 4B Base model that was pruned and distilled from nvidia/Mistral-NeMo-Minitron-8B-Base using our LLM compression technique. The model was trained using a multi-stage CPT and SFT. It uses tiktoken [2] as the tokenizer. The model supports a context length of 8K tokens.
<br> 

## Input: <br>
**Input Type(s):** Text <br>
**Input Format:** String <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Input:** This model supports a context length of 8K. <br>

## Output: <br>
**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** This model supports a context length of 8K. <br>
Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions. <br>

## Prompt Format: <br>
We recommend using the following prompt template, which was used to fine-tune the model. The model may not perform optimally without it.
```
<s>System
You are an expert at translating text from {Source_language} to {Target_language}.</s>
<s>User
What is the {Target_language} translation of the sentence: {Input_Sentence}?</s>
<s>Assistant\n
<br>
```

## Performance: 
COMET score of any2en and en2any direction for Flores-101 dataset

| Language               | Eng -> Language | Language -> Eng |
|------------------------|-----------------|-----------------|
| German                 |     0.663       |       0.7575    |
| European Spanish       |     0.7475      |       0.7317    |
| Latin American Spanish |     0.7472      |       0.7318    |
| French                 |     0.824       |       0.8154    |
| Brazil Portuguese      |     0.894       |       0.8466    |
| Russian                |     0.7234      |       0.6427    |
| Simplified Chinese     |     0.6609      |       0.701     |
| Traditional Chinese    |     0.6319      |       0.6745    |
| Japanese               |     0.7263      |       0.6664    |
| Korean                 |     0.712       |       0.6801    |
| Arabic                 |     0.6888      |       0.7073    |

## Software Integration:
**Runtime Engine(s):** NeMo Framework 24.09 <br> 

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere <br>
* NVIDIA Blackwell <br>
* NVIDIA Hopper <br>
* NVIDIA Lovelace <br>

**Supported Operating System(s):** <br>
* Linux <br>

## Model Version(s):
Riva-Translate-4B-Instruct <br>

# Training & Evaluation: 
### Training Dataset:

Data Collection Method by dataset:  <br>
* Hybrid: Human, Synthetic <br>

Labeling Method by dataset:  <br>
* Automated <br>

**Properties:** This model is trained on open-sourced datasets and synthetic datasets of text parallel corpora generated via back-translation and monolingual datasets. Each entry in the parallel corpus consists of a text in the source language and its translation in the target language. The monolingual datasets contain texts from each of the 12 target language domains. See bias subcard for language distribution.  <br>

## Evaluation Dataset:

**Link:** We used Flores101 [1], NTREX-128 [2], FRMT [3https://www.statmt.org/wmt19/translation-task.html], WMT 19 [4], WMT20 [5] to evaluate the model.
<br>

Data Collection Method by dataset:  <br>
* Automated <br>

Labeling Method by dataset:  <br>
* Automated <br>

## References:
For more information about these datasets, please see the links below.
[1] https://aclanthology.org/2022.tacl-1.30.pdf
[2] https://aclanthology.org/2022.sumeval-1.4.pdf
[3] https://aclanthology.org/2023.tacl-1.39.pdf
[4] https://www.statmt.org/wmt19/translation-task.html
[5] https://www.statmt.org/wmt20/translation-task.html

# Inference:
**Acceleration Engine:** TensorRT-LLM <br>
**Test Hardware:** <br>  
* A100 <br>
* A10G <br>
* H100 <br>
* L40S <br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. <br> 

For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards. <br>

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).  <br>

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing:  |  None
Measures taken to mitigate against unwanted bias:                                                   |  None
Bias Metric (If Measured):                                                   			    |  None

## Language Distribution:
AR: 0.09 <br>
DE: 0.09 <br>
ES-ES: 0.09 <br>
ES-US: 0.09 <br>
FR: 0.09 <br>
JA: 0.09 <br>
KO: 0.09 <br>
PT-BR: 0.09 <br>
RU: 0.09 <br>
ZH-CN: 0.09 <br>
ZH-TW: 0.09 <br>

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Task/Domain:                                                                                  |  Translation
Model Type:                                                                                            |  Decoder-only Transformer
Intended Users:                                                                                        |  Translators, marketers, and web developers who deliver content in multiple languages.
Output:                                                                                                |  Text in the target language.
Describe how the model works:                                                                          |  Text input is encoded into tokens before being passed into transformer-based language model and output as a translation result in the target language.
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Not Applicable
Technical Limitations & Mitigation:                                                                    |  Accuracy varies based on the characteristics of input (Domain, Use Case, Noise, Context, etc.). Grammar errors and semantic issues may be present. As a potential mitigation, the user can change the prompt to get a better translation. 
Verified to have met prescribed NVIDIA quality standards:  					       |  Yes
Performance Metrics:                                                                                   |  BLEU, COMET scores.
Potential Known Risks:                                                                                 |  Translations may not be 100% accurate. This is not recommended for word-for-word translation. 
Licensing:                                                                                             |  Please see the overview [Overview](https://gitlab-master.nvidia.com/api-catalog/examples/-/blob/mengruw/Riva-Translate-4B-Instruct/nv-modelcard++/overview.md)

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personal data?   				                                                   |  No
Personal data used to create this model?                                                                                           |  No
How often is dataset reviewed?                                                                                                     |  Before Release
Is there provenance for all datasets used in training?                                                                             |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  No, not possible with externally-sourced data.
Applicable Privacy Policy                                                                                                           |  https://www.nvidia.com/en-us/about-nvidia/privacy-policy/

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
stream: 
})

process.stdout.write(completion.choices[0]?.message?.content);

}

main();
```

```bash
invoke_url='https://integrate.api.nvidia.com/v1/chat/completions'

authorization_header='Authorization: Bearer '
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data=$'{
"messages": [
{
"role": "user",
"content": ""
}
]
}'

response=$(curl --silent -i -w "\n%{http_code}" --request POST \
--url "$invoke_url" \
--header "$authorization_header" \
--header "$accept_header" \
--header "$content_type_header" \
--data "$data"
)

echo "$response"
```