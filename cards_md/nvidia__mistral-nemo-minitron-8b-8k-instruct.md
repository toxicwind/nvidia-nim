---
title: "mistral-nemo-minitron-8b-8k-instruct"
publisher: "nvidia"
type: "endpoint"
updated: "2025-07-20T16:37:25.970Z"
description: "State-of-the-art small language model delivering superior accuracy for chatbot, virtual assistants, and content generation."
canonical: "https://build.nvidia.com/nvidia/mistral-nemo-minitron-8b-8k-instruct"
---

# Model Overview

## Description:
[//]: # ([Provide additional details about the algorithm/model; include supporting image/video and/or reference blog/article, if available.] [This model is ready for commercial/non-commercial use.] OR [This model is for research and development only.] OR [This model is for demonstration purposes and not for production usage.] <br>)

Mistral-NeMo-Minitron-8B-Instruct is a model for generating responses for various text-generation tasks including roleplaying, retrieval augmented generation, and function calling. It is a fine-tuned version of [nvidia/Mistral-NeMo-Minitron-8B-Base](https://huggingface.co/nvidia/Mistral-NeMo-Minitron-8B-Base), which was pruned and distilled from [Mistral-NeMo 12B](https://huggingface.co/nvidia/Mistral-NeMo-12B-Base) using [our LLM compression technique](https://arxiv.org/abs/2407.14679). The model was trained using a multi-stage SFT and preference-based alignment technique with [NeMo Aligner](https://github.com/NVIDIA/NeMo-Aligner). For details on the alignment technique, please refer to the [Nemotron-4 340B Technical Report](https://arxiv.org/abs/2406.11704). The model supports a context length of 8,192 tokens.

### License/Terms of Use: 
[NVIDIA Open Model License](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)

## Model Architecture:
**Architecture Type:** Transformer <br>
**Network Architecture:** Decoder-only <br>

## Input: 
**Input Type(s):**  Text (Prompt) <br>
**Input Format(s):** String <br>
**Input Parameters:** One Dimensional (1D) <br>
**Other Properties Related to Input:** The model has a maximum of 8192 input tokens. <br>

## Output: 
**Output Type(s):** Text (Response) <br>
**Output Format:** String <br>
**Output Parameters:** 1D <br>
**Other Properties Related to Output:**  The model has a maximum of 8192 input tokens. Maximum output for both versions can be set apart from input.<br>

## Prompt Format:

We recommend using the following prompt template, which was used to fine-tune the model. The model may not perform optimally without it.

```
<extra_id_0>System
{system prompt}

<extra_id_1>User
{prompt}
<extra_id_1>Assistant\n
```

- Note that a newline character `\n` should be added at the end of the prompt.
- We recommend using `<extra_id_1>` as a stop token.

## Evaluation Results

| Category              | Benchmark             | # Shots | Mistral-NeMo-Minitron-8B-Instruct |
|:----------------------|:----------------------|--------:|----------------------------------:|
| General               | MMLU                  |       5 |                              70.4 |
|                       | MT Bench (GPT4-Turbo) |       0 |                              7.86 |
| Math                  | GMS8K                 |       0 |                              87.1 |
| Reasoning             | GPQA                  |       0 |                              31.5 |
| Code                  | HumanEval             |       0 |                              71.3 |
|                       | MBPP                  |       0 |                              72.5 |
| Instruction Following | IFEval                |       0 |                              84.4 |
| Tool Use              | BFCL v2 Live          |       0 |                              67.6 |

## Software Integration: (Cloud)
**Runtime Engine:** NeMo Framework 24.09 <br>

**Supported Hardware Microarchitecture Compatibility:** <br>
* [NVIDIA Ampere] <br>
* [NVIDIA Blackwell] <br>
* [NVIDIA Hopper] <br>
* [NVIDIA Lovelace] <br>

**[Preferred/Supported] Operating System(s):** <br>
* Linux <br>

### Model Version(s)
Mistral-NeMo-Minitron 8B Instruct

# Training & Evaluation: 

## Training Dataset:

** Data Collection Method by dataset <br>
* Hybrid: Automated, Human <br>

** Labeling Method by dataset <br>
* Hybrid: Automated, Human <br>

## Evaluation Dataset:

** Data Collection Method by dataset <br>
* Hybrid: Automated, Human <br>

** Labeling Method by dataset <br>
* Human <br>

## Inference:
**Engine:** TRT-LLM <br>
**Test Hardware:** <br>
* A100 <br>
* A10G <br>
* H100  <br>
* L40S  <br>

**Supported Hardware Platform(s):** L40S, A10G, A100, H100<br>

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  

For more detailed information on ethical considerations for this model, please see the Model Card++ [Explainability](./explainability.md), [Bias](./bias.md), [Safety & Security](./safety.md), and [Privacy Subcards](./privacy.md).  

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Participation considerations from adversely impacted groups ([protected classes](https://www.senate.ca.gov/content/protected-classes)) in model design and testing:  |  None
Measures taken to mitigate against unwanted bias:                                                   |   None

## Explainability

Field                                                                                                  |  Response
:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------
Intended Domain:                                                                                       |
Model Type:                                                                                            |  Generative Pre-Trained Transformer (GPT)-3
Intended User:                                                                                         |  Enterprise developers building game NPCs.
Output:                                                                                                |  Text String(s)
Describe how the model works:                                                                          |  Generates a response using the input text and context such as NPC background information.   
Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of:  |  Not Applicable
Verified to have met prescribed NVIDIA quality standards:  |  Yes
Performance Metrics:                                                                                   |  Accuracy, Latency, and Throughput
Potential Known Risks:                                                                                 |  The model was trained on data that contains toxic language and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. This issue could be exacerbated without the use of the recommended prompt template. The model may also amplify biases and return toxic responses especially when prompted with toxic prompts. If you are going to use this model in an agentic workflow, validate that the imported packages are from a trusted source to ensure end-to-end security.
Licensing:                                                                                             |  [NVIDIA Open Model License](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)
Technical Limitations:                                                                                 |  The Model may generate answers that are inaccurate, omit key information, or include irrelevant or redundant text.

## Privacy

Field                                                                                                                              |  Response
:----------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------
Generatable or reverse engineerable personally-identifiable information (PII)?                                                     |  None
Was consent obtained for any personal data used?                                                                                             |  Not Applicable
Personal data  used to create this model?                                                                                       |  Datasets used for fine-tuning did not introduce any personal data that did not exist in the base model.
How often is dataset reviewed?                                                                                                     |  Before Release
Is a mechanism in place to honor data subject right of access or deletion of personal data?                                        |  Not Applicable
If personal data is collected for the development of the model, was it collected directly by NVIDIA?                                            |  Not Applicable
If personal data is collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?  |  Not Applicable
If personal data is collected for the development of this AI model, was it minimized to only what was required?                                 |  Not Applicable
Is there provenance for all datasets used in training?                                                                                                     |  Yes
Does data labeling (annotation, metadata) comply with privacy laws?                                                                |  Yes
Is data compliant with data subject requests for data correction or removal, if such a request was made?                           |  Not Applicable

## Safety & Security

Field                                               |  Response
:---------------------------------------------------|:----------------------------------
Model Application(s):                               |  Non-Playable Character Conversation 
Describe the life-critical impact (if present).   |  None Known
Use Case Restrictions:                              |  Abide by [NVIDIA AI Foundation Models Community License Agreement](https://developer.nvidia.com/downloads/nv-ai-foundation-models-license)
Model and dataset restrictions:            |  The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development.  Restrictions enforce dataset access during training, and dataset license constraints adhered to.

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
"model": "nvidia/mistral-nemo-minitron-8b-8k-instruct",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```