---
title: "phi-3-vision-128k-instruct"
publisher: "microsoft"
type: "endpoint"
updated: "2025-07-20T16:32:11.880Z"
description: "Cutting-edge open multimodal model exceling in high-quality reasoning from images."
canonical: "https://build.nvidia.com/microsoft/phi-3-vision-128k-instruct"
---

Phi-3 Vision-128K-Instruct: Model Card

# Model Overview

| Developer     | Microsoft GenAI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Phi-3 Vision reasons with image and text inputs.  It is a lightweight, state-of-the-art open multimodal model built upon synthetic data and filtered publicly available datasets from websites with a focus on very high-quality, reasoning dense text and vision data. The model belongs to the Phi-3 model family, and the multimodal version comes with 128K context length (in tokens) it can support. The model underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.  The model is intended for broad commercial and research use in English.  |
| License        | [MIT](https://opensource.org/license/mit) | 
| Third-Party Community Consideration  | This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case.  |
| Architecture   | 4.2B parameter Phi-3 Mini language model that contains image encoder, connector, and projector                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Inputs         | Text and Image. It’s best suited for prompts using the chat format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Context length | 128K tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| GPUS           | 512 H100-80G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Training time  | 1.5 days                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Training data  | 500B tokens (vision tokens + text tokens)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Outputs        | Generates text in response to the input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Dates          | The models were trained between March and May 2024.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Status         | This is a static model trained on an offline text dataset with cutoff date Mar 15, 2024. Future versions of the tuned models may be released as the authors improve models.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Release Type   | Open weight release                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Release dates  | The model weight is released on May 21, 2024.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

# Intended Use

| Primary use cases      | The model provides uses for general purpose AI systems and applications with visual and text input capabilities which require 1) memory/compute constrained environments; 2) latency bound scenarios; 3) general image understanding; 3) optical character recognition (OCR); 4) chart and table understanding. The model is designed to accelerate research on efficient language and multimodal models for use as a building block for generative AI powered features.                                                                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Out-of-scope use cases | The models are not specifically designed or evaluated for all downstream purposes. Developers should consider common limitations of language models as they select use cases, and evaluate and mitigate for accuracy, safety, and fairness before using within a specific downstream use case, particularly for high-risk scenarios.  Developers should be aware of and adhere to applicable laws or regulations (including privacy, trade compliance laws, etc.) that are relevant to their use case.   **Nothing contained in this Model Card should be interpreted as or deemed a restriction or modification to the license the model is released under.** |

# Data Overview

## Training datasets

The training data includes a wide variety of sources, and is a combination of 1) publicly available documents filtered rigorously for quality, selected high-quality educational data and code; 2) selected high-quality image-text interleave and video understanding data; 3) newly created synthetic, “textbook-like” data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world (science, daily activities, theory of mind, etc.), newly created image data, e.g., chart/table/diagram/slides; 4) high quality chat format supervised data covering various topics to reflect human preferences on different aspects such as instruct-following, truthfulness, honesty and helpfulness.

The data collection process involved sourcing information from publicly available documents, with a meticulous approach to filtering out undesirable documents and images. To safeguard privacy, the authors carefully filtered various image and text data sources to remove or scrub any potentially personal data from the training data.  

More details can be found in the (Phi-3 Technical Report)[https://arxiv.org/abs/2404.14219].

## Benchmark datasets

Public datasets:

-   Popular aggregated benchmark:

-   MMMU: massive multi-discipline tasks at college-level subject knowledge and deliberate reasoning

-   MMBench: large-scale benchmark to evaluate perception and reasoning capabilities

-   Visual reasoning:

-   ScienceQA: multimodal visual question answering on science

-   MathVista: visual math reasoning

-   InterGPS: Visual 2D geometry reasoning

-   Chart reasoning:

-   ChartQA: visual and logical reasoning on charts

-   AI2D: diagram understanding

-   Document :

-   TextVQA: read and reason about text in images to answer questions about them

-   Object Recognition:

-   POPE: recognize the presence of objects in images

Internal datasets:

-   Microsoft products

-   PowerPoint VQA: question answering on PowerPoint (PPT) slides

-   Plots & Charts: visual understanding from figures, plots, and charts

-   TextQA: visual question answering on OCR scenarios

RAI & Security Benchmarks:

-   Multimodal model RAI:

-   VLGuardExt: [VLGuard](https://arxiv.org/abs/2402.02207) is a vision-language instruction following public dataset for model safety to address safety on deception, discrimination, privacy and risky behavior (advice, sexual, violence, political). The authors then extended to a few internal categories such as child safety and election critical information

-   [RTVLM](https://arxiv.org/abs/2401.12915): Public benchmark for red-teaming vision-language model on model truthfulness, privacy, safety, and fairness

-   GPTV-RAI: In-house benchmark for GPT-4V released from Azure AI, measuring harmfulness (ex. sexual, violent, hate and self-harm), privacy, jailbreak, misinformation

-   Language model RAI:

-   LaserTag: measure grounding, third party harm, harmful content continuation, harmful content summarization and jailbreak, leveraged from phi-3 language

-   [XSTest](https://arxiv.org/abs/2308.01263): Public benchmark designed to identify exaggerated safety behaviors in large language models, it is introduced to strike a balance between model helpfulness and harmfulness

# Safety

## Approach

The Phi-3 family of models has adopted a robust safety post-training approach. This approach leverages a variety of both open-source and in-house generated datasets. The overall technique employed to do the safety alignment is a combination of SFT (Supervised Fine-Tuning) and a modified version of RLHF (Reinforcement Learning from Human Feedback) by utilizing human-labeled and synthetic datasets, including publicly available datasets focusing on helpfulness and harmlessness as well as various questions and answers targeted to multiple safety categories.

## Safety Evaluation and Red-Teaming

Prior to release, Phi-3 family of models followed a multi-faceted evaluation approach. Quantitative evaluation was conducted with multiple open-source safety benchmarks and in-house tools utilizing adversarial conversation simulation. For qualitative safety evaluation, the authors collaborated with the AI Red Team at Microsoft to assess safety risks posed by both visual and text inputs, in addition with their combinations. The assessment was done in predetermined in risk categories for both vision and language with automated scoring followed by thorough manual reviews of the model responses.

# Please refer to the technical report for more details of the safety alignment.

# Model Quality

To understand the capabilities, the authors compare Phi-3 Vision-128K-Instruct with a set of models over a variety of zero-shot benchmarks using the internal benchmark platform BabelBench (See **Appendix A** for benchmark methodology).

At the high-level overview of the model quality on representative benchmarks:

| Category                              | Benchmark            | Phi-3 Vision-128K-In[^1] | LlaVA-1.6 Vicuna-7B | QWEN-VL Chat | Llama3-Llava-Next-8B | Claude-3 Haiku | Gemini 1.0 Pro V | GPT-4V-Turbo |
|---------------------------------------|----------------------|--------------------------|---------------------|--------------|----------------------|----------------|------------------|--------------|
| Popular aggregated benchmark          | MMMU (val)           | 40.2                     | 34.2                | 39.0         | 36.4                 | 40.7           | 42.0             | 55.5         |
|                                       | MMBench (dev-en)     | 80.5                     | 76.3                | 75.8         | 79.4                 | 62.4           | 80.0             | 86.1         |
| Visual scientific knowledge reasoning | ScienceQA (img-test) | 90.8                     | 70.6                | 67.2         | 73.7                 | 72.0           | 79.7             | 75.7         |
| Visual math reasoning                 | MathVista (testmini) | 44.5                     | 31.5                | 29.4         | 34.8                 | 33.2           | 35.0             | 47.5         |
|                                       | InterGPS (test)      | 38.1                     | 20.5                | 22.3         | 24.6                 | 32.1           | 28.6             | 41.0         |
| Chart reasoning                       | AI2D (test)          | 76.7                     | 63.1                | 59.8         | 66.9                 | 60.3           | 62.8             | 74.7         |
|                                       | ChartQA (test)       | 81.4                     | 55.0                | 50.9         | 65.8                 | 59.3           | 58.0             | 62.3         |
| Document Intelligence                 | TextVQA (val)        | 70.9                     | 64.6                | 59.4         | 55.7                 | 62.7           | 64.7             | 68.1         |
| Object visual presence verification   | POPE (test)          | 85.8                     | 87.2                | 82.6         | 87.0                 | 74.4           | 84.2             | 83.7         |

[^1]: For internal reference, this is the **Vision-128K-InstructRC 3.1.3** checkpoint of 128k context length (Mini-128K RC1_44L).

##### Internal benchmarks

|                | Phi-3 Vision-128K-In | LlaVA-1.6 Vicuna-7B | QWEN-VL Chat | Llama3-Llava-Next-8B | GPT-4V-Turbo |
|----------------|----------------------|---------------------|--------------|----------------------|--------------|
| PowerPoint VQA | 75.5                 | 49.5                | 55.5         | 49.0                 | 86.0         |
| Plots & Charts | 64.7                 | 52.0                | 43.7         | 53.8                 | 83.3         |
| TextQA         | 3.39                 | 2.62                | 2.69         | 2.87                 | 3.92         |

<!-- ![A diagram of a heart Description automatically generated](model_quality.png) -->

See **Appendix D** for examples on different capabilities.

# Usage

### Input formats

Given the nature of the training data, the Phi-3 Vision-128K-Instruct model is best suited for prompts using the chat format as follows:

Single image:

**\<\|user\|\>\\n\<\|image_1\|\>\\n{prompt}\<\|end\|\>\\n\<\|assistant\|\>\\n**

For multi-turn conversations:

**\<\|user\|\>\\n\<\|image_1\|\>\\n{prompt_1}\<\|end\|\>\\n\<\|assistant\|\>\\n{response_1}\<\|end\|\>\\n\<\|user\|\>\\n{prompt_2}\<\|end\|\>\\n\<\|assistant\|\>\\n**

After obtaining the Phi-3 Vision-128K-Instruct model checkpoints, users can use this sample code for inference.  

``` python  
*from* PIL *import* Image

*import* requests

*from* transformers *import* AutoModelForCausalLM

*from* transformers *import* AutoProcessor

model_id = "microsoft/Phi-3-vision-128k-instruct"

model = AutoModelForCausalLM.from_pretrained(

model_id,

device_map="cuda",

trust_remote_code=True,

torch_dtype="auto"

)

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

messages = [

{"role": "user", "content": "\<\|image_1\|\>\\nWhat is shown in this image?"},

{"role": "assistant", "content": " The chart displays the percentage of respondents who agree with various statements about their preparedness for meetings. It shows five categories: 'Having clear and pre-defined goals for meetings', 'Knowing where to find the information I need for a meeting', 'Understanding my exact role and responsibilities when I'm invited', 'Having tools to manage admin tasks like note-taking or summarization', and 'Having more focus time to sufficiently prepare for meetings'. Each category has an associated bar indicating the level of agreement, measured on a scale from 0% to 100%."},

{"role": "user", "content": "Provide insightful questions to spark discussion."}

]

url = "https://assets-c4akfrf5b4d3f4b7.z01.azurefd.net/assets/2024/04/BMDataViz_661fb89f3845e.png"

image = Image.open(requests.get(url, stream=True).raw)

prompt = processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

inputs = processor(prompt, [image], return_tensors="pt").to("cuda:0")

generation_args = {

"max_new_tokens": 500,

"temperature": 0.0,

"do_sample": False,

}

generate_ids = model.generate(*\*\**inputs, eos_token_id=processor.tokenizer.eos_token_id, *\*\**generation_args)

response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

print(response)

```
# Responsible AI Considerations

Like other models, the Phi family of models can potentially behave in ways that are unfair, unreliable, or offensive. Some of the limiting behaviors to be aware of include:

-   Quality of Service: The Phi models are trained primarily on English text. Languages other than English will experience worse performance. English language varieties with less representation in the training data might experience worse performance than standard American English.

-   Representation of Harms & Perpetuation of Stereotypes: These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.

-   Inappropriate or Offensive Content: These models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case.

-   Information Reliability: Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.

-   Limited Scope for Code: Majority of Phi-3 training data is based in Python and use common packages such as "typing, math, random, collections, datetime, itertools". If the model generates Python scripts that utilize other packages or scripts in other languages, the authors strongly recommend users manually verify all API uses.

Developers should apply responsible AI best practices and are responsible for ensuring that a specific use case complies with relevant laws and regulations (e.g. privacy, trade, etc.). Important areas for consideration include:

-   Allocation: Models may not be suitable for scenarios that could have consequential impact on legal status or the allocation of resources or life opportunities (ex: housing, employment, credit, etc.) without further assessments and additional debiasing techniques.

-   High-Risk Scenarios: Developers should assess suitability of using models in high-risk scenarios where unfair, unreliable or offensive outputs might be extremely costly or lead to harm. This includes providing advice in sensitive or expert domains where accuracy and reliability are critical (ex: legal or health advice). Additional safeguards should be implemented at the application level according to the deployment context.

-   Misinformation: Models may produce inaccurate information. Developers should follow transparency best practices and inform end-users they are interacting with an AI system. At the application level, developers can build feedback mechanisms and pipelines to ground responses in use-case specific, contextual information, a technique known as Retrieval Augmented Generation (RAG).

-   Generation of Harmful Content: Developers should assess outputs for their context and use available safety classifiers or custom solutions appropriate for their use case.

-   Misuse: Other forms of misuse such as fraud, spam, or malware production may be possible, and developers should ensure that their applications do not violate applicable laws and regulations.

-   Identification of individuals: models with vision capabilities may have the potential to uniquely identify individuals in images. Safety post-training steers the model to refuse such requests, but developers should consider and implement, as appropriate, additional mitigations or user consent flows as required in their respective jurisdiction, (e.g., building measures to blur faces in image inputs before processing).

# Appendix A: Benchmark Methodology

The authors include a brief word on methodology here - and in particular, how the authors think about optimizing prompts and evaluating results.

## Prompts in BabelBench

In an ideal world, the authors would **never change any prompts** in the benchmarks to ensure it’s always an apples-to-apples comparison when comparing different models. Indeed, this is the default approach, and is the case in the vast majority of models the authors have run to date.

There are, however, some exceptions to this. In some cases, the authors see a model that performs worse than expected on a given eval *due to a failure to respect the output format*. For example:

-   A Claude model may refuse to answer questions (for no apparent reason), or in coding tasks models may prefix their response with “Sure, I can help with that. …” which may break the parser. In such cases, the authors have opted to try different *system messages* (e.g. “You must always respond to a question” or “Get to the point!”).

-   With LLaMA-1 models, the authors observed that few shots actually hurt model performance. In this case the authors did allow running the benchmarks with 0-shots for all cases.

-   The authors have tools to convert between chat and completions APIs. When converting a chat prompt to a completion prompt, some models have different keywords e.g. Human vs User. In these cases, the authors do allow for model-specific mappings for chat to completion prompts. I would say that this is less common issue today –OpenAI’s chat format is becoming fairly standard.

However, **the authors do not**:

-   Pick different few-shot examples. Few shots will always be the same when comparing different models.

-   Change prompt format: e.g. if it’s an A/B/C/D multiple choice, the authors don’t tweak this to 1/2/3/4 multiple choice.

## Vision Benchmark Settings

The goal of the benchmark setup is to measure the performance of the LMM when a regular user utilizes these models for a task involving visual input. To this end, the authors selected 9 popular and publicly available datasets that cover a wide range of challenging topics and tasks (e.g., mathematics, OCR tasks, charts-and-plots understanding, etc.) as well as a set of high-quality models.

The benchmarking setup utilizes zero-shot prompts and all the prompt content are the same for every model. The authors only formatted the prompt content to satisfy the model’s prompt API. This ensures that the evaluation is fair across the set of models the authors tested. Many benchmarks necessitate that models choose their responses from a presented list of options. Therefore, the authors've included a directive in the prompt's conclusion, guiding all models to pick the option letter that corresponds to the answer they deem correct.

In terms of the visual input, the authors use the images from the benchmarks as they come from the original datasets. The authors converted these images to base-64 using a JPEG encoding for models that require this format (e.g., GPTV, Claude-3 Haiku, Gemini Pro). For other models (e.g., Llava, QWEN-VL, and QWEN-VL Chat), the authors used their Huggingface interface and passed in PIL images or a JPEG image stored locally. The authors did not scale or pre-process images in any other way.

Lastly, the authors used the same code to extract answers and evaluate them using the same code for every considered model. This ensured that the authors are fair in assessing the quality of their answers.

## Specifications

- **Context Length:** 131,072 tokens
- **Parameters:** 4,146,621,440
- **Input:** Text, Image
- **Output:** Text

## Capabilities

- **Function Calling:** Not supported
- **Structured Output:** Not supported
- **Reasoning:** Not supported

## Prototype

```python
import requests

invoke_url = "https://ai.api.nvidia.com/v1/vlm/microsoft/phi-3-vision-128k-instruct"

headers = {
"Authorization": "Bearer ",
"Accept": "application/json",
}

payload = {
"messages": [
{
"role": "user",
"content": ""
}
]
}

# re-use connections
session = requests.Session()

response = session.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
```

```javascript
import fetch from "node-fetch";

const invokeUrl = "https://ai.api.nvidia.com/v1/vlm/microsoft/phi-3-vision-128k-instruct"

const headers = {
"Authorization": "Bearer ",
"Accept": "application/json",
}

const payload = {
"messages": [
{
"role": "user",
"content": ""
}
]
}

let response = await fetch(invokeUrl, {
method: "post",
body: JSON.stringify(payload),
headers: { "Content-Type": "application/json", ...headers }
});

let response_body = await response.json()

console.log(JSON.stringify(response_body))
```

```bash
invoke_url='https://ai.api.nvidia.com/v1/vlm/microsoft/phi-3-vision-128k-instruct'

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