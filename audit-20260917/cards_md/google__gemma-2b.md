---
title: "gemma-2b"
publisher: "google"
type: "endpoint"
updated: "2025-07-20T16:37:23.686Z"
description: "Lightweight language model deployable on laptop, desktop or the cloud for summarization and reasoning."
canonical: "https://build.nvidia.com/google/gemma-2b"
---

# Gemma Model Card

## Model Information

### Description

Gemma is a family of lightweight, state-of-the art open models from Google,
built from the same research and technology used to create the Gemini models.
They are text-to-text, decoder-only large language models, available in English,
with open weights, pre-trained variants, and instruction-tuned variants. Gemma
models are well-suited for a variety of text generation tasks, including
question answering, summarization, and reasoning. Their relatively small size
makes it possible to deploy them in environments with limited resources such as
a laptop, desktop or your own cloud infrastructure, democratizing access to
state of the art AI models and helping foster innovation for everyone.

## References:

**Author**: Google

**Model Page**: [Gemma](https://ai.google.dev/gemma/docs) 

**Model Card**: https://ai.google.dev/gemma/docs/model_card 

**Resources and Technical Documentation**:

* [Responsible Generative AI Toolkit][rai-toolkit]
* [Gemma on Kaggle][kaggle-gemma]
* [Gemma on Vertex Model Garden][vertex-mg-gemma]

**Terms of Use**: [Terms][terms]

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case.

### Inputs and Outputs

## Input: 
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** Text can be question, a prompt, or a document to be
summarized. <br> 

## Output: 
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** Generated English-language text in response to the input (e.g.,
an answer to the question, a summary of the document). <br> 

## Usage and Limitations

These models have certain limitations that users should be aware of.

### Intended Usage

Open Large Language Models (LLMs) have a wide range of applications across
various industries and domains. The following list of potential uses is not
comprehensive. The purpose of this list is to provide contextual information
about the possible use-cases that the model creators considered as part of model
training and development.

* Content Creation and Communication
* Text Generation: These models can be used to generate creative text formats
such as poems, scripts, code, marketing copy, and email drafts.
* Chatbots and Conversational AI: Power conversational interfaces for customer
service, virtual assistants, or interactive applications.
* Text Summarization: Generate concise summaries of a text corpus, research
papers, or reports.
* Research and Education
* Natural Language Processing (NLP) Research: These models can serve as a
foundation for researchers to experiment with NLP techniques, develop
algorithms, and contribute to the advancement of the field.
* Language Learning Tools: Support interactive language learning experiences,
aiding in grammar correction or providing writing practice.
* Knowledge Exploration: Assist researchers in exploring large bodies of text
by generating summaries or answering questions about specific topics.

### Limitations

* Training Data
* The quality and diversity of the training data significantly influence the
model's capabilities. Biases or gaps in the training data can lead to
limitations in the model's responses.
* The scope of the training dataset determines the subject areas the model can
handle effectively.
* Context and Task Complexity
* LLMs are better at tasks that can be framed with clear prompts and
instructions. Open-ended or highly complex tasks might be challenging.
* A model's performance can be influenced by the amount of context provided
(longer context generally leads to better outputs, up to a certain point).
* Language Ambiguity and Nuance
* Natural language is inherently complex. LLMs might struggle to grasp subtle
nuances, sarcasm, or figurative language.
* Factual Accuracy
* LLMs generate responses based on information they learned from their
training datasets, but they are not knowledge bases. They may generate
incorrect or outdated factual statements.
* Common Sense
* LLMs rely on statistical patterns in language. They might lack the ability
to apply common sense reasoning in certain situations.

## Usage and Limitations

These models have certain limitations that users should be aware of.

### Intended Usage

Open Large Language Models (LLMs) have a wide range of applications across
various industries and domains. The following list of potential uses is not
comprehensive. The purpose of this list is to provide contextual information
about the possible use-cases that the model creators considered as part of model
training and development.

* Content Creation and Communication
* Text Generation: These models can be used to generate creative text formats
such as poems, scripts, code, marketing copy, and email drafts.
* Chatbots and Conversational AI: Power conversational interfaces for customer
service, virtual assistants, or interactive applications.
* Text Summarization: Generate concise summaries of a text corpus, research
papers, or reports.
* Research and Education
* Natural Language Processing (NLP) Research: These models can serve as a
foundation for researchers to experiment with NLP techniques, develop
algorithms, and contribute to the advancement of the field.
* Language Learning Tools: Support interactive language learning experiences,
aiding in grammar correction or providing writing practice.
* Knowledge Exploration: Assist researchers in exploring large bodies of text
by generating summaries or answering questions about specific topics.

### Limitations

* Training Data
* The quality and diversity of the training data significantly influence the
model's capabilities. Biases or gaps in the training data can lead to
limitations in the model's responses.
* The scope of the training dataset determines the subject areas the model can
handle effectively.
* Context and Task Complexity
* LLMs are better at tasks that can be framed with clear prompts and
instructions. Open-ended or highly complex tasks might be challenging.
* A model's performance can be influenced by the amount of context provided
(longer context generally leads to better outputs, up to a certain point).
* Language Ambiguity and Nuance
* Natural language is inherently complex. LLMs might struggle to grasp subtle
nuances, sarcasm, or figurative language.
* Factual Accuracy
* LLMs generate responses based on information they learned from their
training datasets, but they are not knowledge bases. They may generate
incorrect or outdated factual statements.
* Common Sense
* LLMs rely on statistical patterns in language. They might lack the ability
to apply common sense reasoning in certain situations.

## Model Data

### Training Dataset

These models were trained on a text dataset that includes a wide variety
of sources, totaling 6 trillion tokens. Here are the primary training data sources:

* Web Documents: A diverse collection of web text ensures the model is exposed
to a broad range of linguistic styles, topics, and vocabulary. Primarily
English-language content.
* Code: Exposing the model to code helps it to learn the syntax and patterns of
programming languages, which improves its ability to generate code or
understand code-related questions.
* Mathematics: Training on mathematical text helps the model learn logical
reasoning, symbolic representation, and to address mathematical queries.

The combination of these diverse data sources is crucial for training a powerful
language model that can handle a wide variety of different tasks and text
formats.

### Data Preprocessing

Here are the key data cleaning and filtering methods applied to the training
data:

* CSAM Filtering: Rigorous CSAM (Child Sexual Abuse Material) filtering was
applied at multiple stages in the data preparation process to ensure the
exclusion of harmful and illegal content.
* Sensitive Data Filtering: As part of making Gemma pre-trained models safe and
reliable, automated techniques were used to filter out certain personal
information and other sensitive data from training sets.
* Additional methods: Filtering based on content quality and safely in line with
[our policies][safety-policies].

## Implementation Information

### TensorRT-LLM

The endpoint available on NGC catalog is accelerated by TensorRT-LLM, an open-source library for optimizing inference performance. Gemma is compatible across NVIDIA AI platforms—from the datacenter, cloud, to the local PC with RTX GPU systems.   

Gemma models use a vocabulary size of 256K and support a context length of up to 8K while using rotary positional embedding (RoPE). With support for Position Interpolation (PI) available in TensorRT-LLM, Gemma models using RoPE can support longer output sequence lengths at inference time while retaining original model architecture.  

### Model Customization
The model is converted to .nemo for easy customization with NVIDIA NeMo framework – an end-to-end framework to curate data, tune models, and deploy anywhere. It supports various customization techniques including RLHF, SFT, LoRA, and Steer-LM. 

## Evaluation

Model evaluation metrics and results.

### Benchmark Results

These models were evaluated against a large collection of different datasets and
metrics to cover different aspects of text generation:

| Benchmark                      | Metric        | 2B Params   | 7B Params |
| ------------------------------ | ------------- | ----------- | --------- |
| [MMLU][mmlu]                   | 5-shot, top-1 | 42.3        | 64.3      |
| [HellaSwag][hellaswag]         | 0-shot        | 71.4        | 81.2      |
| [PIQA][piqa]                   | 0-shot        | 77.3        | 81.2      |
| [SocialIQA][socialiqa]         | 0-shot        | 59.7        | 51.8      |
| [BooIQ][booiq]                 | 0-shot        | 69.4        | 83.2      |
| [WinoGrande][winogrande]       | partial score | 65.4        | 72.3      |
| [CommonsenseQA][commonsenseqa] | 7-shot        | 65.3        | 71.3      |
| [OpenBookQA][openbookqa]       |               | 47.8        | 52.8      |
| [ARC-e][arc]                   |               | 73.2        | 81.5      |
| [ARC-c][arc]                   |               | 42.1        | 53.2      |
| [TriviaQA][triviaqa]           | 5-shot        | 53.2        | 63.4      |
| [Natural Questions][naturalq]  | 5-shot        |             | 23        |
| [HumanEval][humaneval]         | pass@1        | 22.0        | 32.3      |
| [MBPP][mbpp]                   | 3-shot        | 29.2        | 44.4      |
| [GSM8K][gsm8k]                 | maj@1         | 17.7        | 46.4      |
| [MATH][math]                   | 4-shot        | 11.8        | 24.3      |
| [AGIEval][agieval]             |               | 24.2        | 41.7      |
| [BIG-Bench][big-bench]         |               | 35.2        | 55.1      |
| ------------------------------ | ------------- | ----------- | --------- |
| **Average**                    |               | **54.0**    | **56.4**  |

## Ethics and Safety

### Evaluation Approach

Our evaluation methods include structured evaluations and internal red-teaming
testing of relevant content policies. Red-teaming was conducted by a number of
different teams, each with different goals and human evaluation metrics. These
models were evaluated against a number of different categories relevant to
ethics and safety, including:

* Text-to-Text Content Safety: Human evaluation on prompts covering safety
policies including child sexual abuse and exploitation, harassment, violence
and gore, and hate speech.
* Text-to-Text Representational Harms: Benchmark against relevant academic
datasets such as [WinoBias][winobias] and [BBQ Dataset][bbq].
* Memorization: Automated evaluation of memorization of training data, including
the risk of personally identifiable information exposure.
* Large-scale harm: Tests for "dangerous capabilities," such as chemical,
biological, radiological, and nuclear (CBRN) risks.

### Evaluation Results

The results of ethics and safety evaluations are within acceptable thresholds
for meeting [internal policies][safety-policies] for categories such as child
safety, content safety, representational harms, memorization, large-scale harms.
On top of robust internal evaluations, the results of well known safety
benchmarks like BBQ, BOLD, Winogender, Winobias, RealToxicity, and TruthfulQA
are shown here.

| Benchmark                      | Metric        | 2B Params   | 7B Params |
| ------------------------------ | ------------- | ----------- | --------- |
| [RealToxicity][realtox]        | average       | 6.86        | 7.90      |
| [BOLD][bold]                   |               | 45.57       | 49.08     |
| [CrowS-Pairs][crows]           | top-1         | 45.82       | 51.33     |
| [BBQ Ambig][bbq]               | 1-shot, top-1 | 62.58       | 92.54     |
| [BBQ Disambig][bbq]            | top-1         | 54.62       | 71.99     |
| [Winogender][winogender]       | top-1         | 51.25       | 54.17     |
| [TruthfulQA][truthfulqa]       |               | 44.84       | 31.81     |
| [Winobias 1_2][winobias]       |               | 56.12       | 59.09     |
| [Winobias 2_2][winobias]       |               | 91.10       | 92.23     |
| [Toxigen][toxigen]             |               | 29.77       | 39.59     |
| ------------------------------ | ------------- | ----------- | --------- |

### Ethical Considerations and Risks

The development of large language models (LLMs) raises several ethical concerns.
In creating an open model, we have carefully considered the following:

* Bias and Fairness
* LLMs trained on large-scale, real-world text data can reflect socio-cultural
biases embedded in the training material. These models underwent careful
scrutiny, input data pre-processing described and posterior evaluations
reported in this card.
* Misinformation and Misuse
* LLMs can be misused to generate text that is false, misleading, or harmful.
* Guidelines are provided for responsible use with the model, see the
[Responsible Generative AI Toolkit][rai-toolkit].
* Transparency and Accountability:
* This model card summarizes details on the models' architecture,
capabilities, limitations, and evaluation processes.
* A responsibly developed open model offers the opportunity to share
innovation by making LLM technology accessible to developers and researchers
across the AI ecosystem.

Risks Identified and Mitigations:

* Perpetuation of biases: It's encouraged to perform continuous monitoring
(using evaluation metrics, human review) and the exploration of de-biasing
techniques during model training, fine-tuning, and other use cases.
* Generation of harmful content: Mechanisms and guidelines for content safety
are essential. Developers are encouraged to exercise caution and implement
appropriate content safety safeguards based on their specific product policies
and application use cases.
* Misuse for malicious purposes: Technical limitations and developer and
end-user education can help mitigate against malicious applications of LLMs.
Educational resources and reporting mechanisms for users to flag misuse are
provided. Prohibited uses of Gemma models are outlined in the
[Gemma Prohibited Use Policy][prohibited-use].
* Privacy violations: Models were trained on data filtered for removal of PII
(Personally Identifiable Information). Developers are encouraged to adhere to
privacy regulations with privacy-preserving techniques.

[Google's commitments to operate sustainably][sustainability].

### Benefits

At the time of release, this family of models provides high-performance open
large language model implementations designed from the ground up for Responsible
AI development compared to similarly sized models.

Using the benchmark evaluation metrics described in this document, these models
have shown to provide superior performance to other, comparably-sized open model
alternatives.

[rai-toolkit]: https://ai.google.dev/responsible
[kaggle-gemma]: https://www.kaggle.com/models/google/gemma
[terms]: https://ai.google.dev/gemma/terms
[vertex-mg-gemma]: https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/335
[sensitive-info]: https://cloud.google.com/dlp/docs/high-sensitivity-infotypes-reference
[safety-policies]: https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/2023_Google_AI_Principles_Progress_Update.pdf#page=11
[prohibited-use]: https://ai.google.dev/gemma/prohibited_use_policy
[tpu]: https://cloud.google.com/tpu/docs/intro-to-tpu
[sustainability]: https://sustainability.google/operating-sustainably/
[jax]: https://github.com/google/jax
[ml-pathways]: https://blog.google/technology/ai/introducing-pathways-next-generation-ai-architecture/
[sustainability]: https://sustainability.google/operating-sustainably/
[foundation-models]: https://ai.google/discover/foundation-models/
[gemini-paper]: https://arxiv.org/abs/2312.11805
[mmlu]: https://arxiv.org/abs/2009.03300
[hellaswag]: https://arxiv.org/abs/1905.07830
[piqa]: https://arxiv.org/abs/1911.11641
[socialiqa]: https://arxiv.org/abs/1904.09728
[booiq]: https://arxiv.org/abs/1905.10044
[winogrande]: https://arxiv.org/abs/1907.10641
[commonsenseqa]: https://arxiv.org/abs/1811.00937
[openbookqa]: https://arxiv.org/abs/1809.02789
[arc]: https://arxiv.org/abs/1911.01547
[triviaqa]: https://arxiv.org/abs/1705.03551
[naturalq]: https://github.com/google-research-datasets/natural-questions
[humaneval]: https://arxiv.org/abs/2107.03374
[mbpp]: https://arxiv.org/abs/2108.07732
[gsm8k]: https://arxiv.org/abs/2110.14168
[realtox]: https://arxiv.org/abs/2009.11462
[bold]: https://arxiv.org/abs/2101.11718
[crows]: https://aclanthology.org/2020.emnlp-main.154/
[bbq]: https://arxiv.org/abs/2110.08193v2
[winogender]: https://arxiv.org/abs/1804.09301
[truthfulqa]: https://arxiv.org/abs/2109.07958
[winobias]: https://arxiv.org/abs/1804.06876
[math]: https://arxiv.org/abs/2103.03874
[agieval]: https://arxiv.org/abs/2304.06364
[big-bench]: https://arxiv.org/abs/2206.04615
[toxigen]: https://arxiv.org/abs/2203.09509

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
"model": "google/gemma-2b",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```