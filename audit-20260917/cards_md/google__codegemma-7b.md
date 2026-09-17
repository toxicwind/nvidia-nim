---
title: "codegemma-7b"
publisher: "google"
type: "endpoint"
updated: "2025-05-21T21:00:24.309Z"
description: "Cutting-edge model built on Google's Gemma-7B specialized for code generation and code completion."
canonical: "https://build.nvidia.com/google/codegemma-7b"
---

# CodeGemma Model card

## Model Information

### Model Summary

**Authors:** Google

#### Description

CodeGemma is a family of lightweight open code models built on top of Gemma.
CodeGemma models are text-to-text and text-to-code decoder-only models and are
available as a 7 billion pretrained variant that specializes in code completion
and code generation tasks, a 7 billion parameter instruction-tuned variant for
code chat and instruction following and a 2 billion parameter pretrained variant
for fast code completion.  This model is ready for commercial use.

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to the [CodeGemma Model Card](https://ai.google.dev/gemma/docs/codegemma). 

#### Terms of Use
By accessing this model, you are agreeing to the [NVIDIA AI Foundation Models Community License](https://developer.download.nvidia.com/ai-foundation-models/nvidia-ai-foundation-models-license-10Nov2023.pdf) <br>
Additional Information: [Gemma Terms of Use](https://www.kaggle.com/models/google/gemma/license/consent), [Google Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy).

#### Reference: 

```none
@article{codegemma_2024,
title={CodeGemma: Open Code Models Based on Gemma},
url={https://www.kaggle.com/m/3301},
author={CodeGemma Team and Hartman, Ale Jakse and Hu, Andrea and Choquette-Choo, Christopher A. and Zhao, Heri and Fine, Jane and Hui,
Jeffrey and Shen, Jingyue and Kelley, Joe and Howland, Joshua and Bansal, Kshitij and Vilnis, Luke and Wirth, Mateo and Nguyen, Nam, and Michel, Paul and Choy, Peter and Joshi, Pratik and Kumar, Ravin and Hashmi, Sarmad and Agrawal, Shubham and Zuo, Siqi and Warkentin, Tris and Gong, Zhitao et al.},
year={2024}
}
```

#### Resources and Technical Documentation
*   [Responsible Generative AI Toolkit](https://ai.google.dev/responsible)
*   [CodeGemma on Kaggle](https://www.kaggle.com/models/google/codegemma)
*   [Technical Report](https://storage.googleapis.com/deepmind-media/gemma/codegemma_report.pdf)

#### Model Architecture: 
**Architecture Type:** Transformer Decoder Network <br>
**Network Architecture:** Real-Gated Linear Recurrent Unit (RG-LRU) <br>

#### Inputs and outputs

## Input: 
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** For pretrained model variants: code prefix and optionally suffix
for code completion and generation scenarios or natural language text/prompt.  For instruction tuned model variant: natural language text or prompt. <br> 

## Output: 
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** One-Dimensional (1D) <br>
**Other Properties Related to Output:** For pretrained model variants: fill-in-the-middle code
completion, code and natural language. For instruction tuned model variant:
code and natural language. <br> 

## Intended Usage

### Application

Code Gemma models have a wide range of applications, which vary between IT and
PT models. The following list of potential uses is not comprehensive. The
purpose of this list is to provide contextual information about the possible
use-cases that the model creators considered as part of model training and
development.

* Code Completion: PT models can be used to complete code with an IDE extension
* Code Generation: IT model can be used to generate code with or without an IDE
extension
* Code Conversation: IT model can power conversation interfaces which discuss
code
* Code Education: IT model supports interactive code learning experiences, aids
in syntax correction or provides coding practice

## Model Usage and Limitations

### Known Limitations

These models have certain limitations that users should be aware of:

*   **Training data**
*   The quality and diversity of the training data significantly influence
the model's capabilities. Biases or gaps in the training data can lead
to limitations in the model's responses.
*   The scope of the training dataset determines the subject areas the model
can handle effectively.
*   **Context and task complexity**
*   LLMs are better at tasks that can be framed with clear prompts and
instructions. Open-ended or highly complex tasks might be challenging.
*   A model's performance can be influenced by the amount of context
provided (longer context generally leads to better outputs, up to a
certain point).
*   **Language ambiguity and nuance**
*   Natural language is inherently complex. LLMs might struggle to grasp
subtle nuances, sarcasm, or figurative language.
*   **Factual accuracy**
*   LLMs generate responses based on information they learned from their
training datasets, but they are not knowledge bases. They may generate
incorrect or outdated factual statements.
*   **Common sense**
*   LLMs rely on statistical patterns in language. They might lack the
ability to apply common sense reasoning in certain situations.

### Model Data

#### Training Dataset

Using Gemma as the base model, CodeGemma 2B and 7B pretrained variants are
further trained on an additional 500 billion tokens of primarily English
language data from open source mathematics datasets and synthetically generated
code. 

#### Training Data Processing

The following data pre-processing techniques were applied to train CodeGemma:

* FIM - Pretrained CodeGemma models focus on fill-in-the-middle (FIM) tasks.
The models are trained to work with both Prefix-Suffix-Middle (PSM) and Suffix-Prefix-Middle (SPM) modes. Our FIM settings are
80% FIM rate with 50-50 PSM/SPM.
* Dependency Graph-based Packing and Unit Test-based Lexical Packing techniques:
To improve model alignment with real-world applications, we structured training
examples at the project/repository level to colocate the most relevant source
files within each repository. Specifically, we employed two heuristic
techniques: dependency graph-based packing and unit test-based lexical packing.
* We developed a novel technique for splitting the documents into prefix,
middle, and suffix to make the suffix start in a more syntactically natural
point rather than purely random distribution.
* Safety: Similarly to Gemma, we deployed rigorous safety filtering including
filtering personal data, CSAM filtering and other filtering based on content
quality and safety in line with [our policies](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/2023_Google_AI_Principles_Progress_Update.pdf#page=11).

## Implementation Information

### Hardware and Frameworks used during training

Like
[Gemma](https://ai.google.dev/gemma/docs/model_card#implementation_information),
CodeGemma was trained on  the latest generation of
[Tensor Processing Unit (TPU)](https://cloud.google.com/tpu/docs/intro-to-tpu)
hardware (TPUv5e),
using [JAX](https://github.com/google/jax) and [ML Pathways](https://blog.google/technology/ai/introducing-pathways-next-generation-ai-architecture/).

## Evaluation Information

### Benchmark Results

#### Evaluation Approach

* Code completion benchmarks: [HumanEval (HE)] Single Line and Multiple Line Infilling
* Code generation benchmarks: HumanEval, [MBPP], [BabelCode (BC)] 
(C++, C#, Go, Java, JavaScript, Kotlin, Python, Rust)
* Q&A: [BoolQ], [PIQA], [TriviaQA]
* Natural Language: [ARC-Challenge], [HellaSwag], [MMLU], [WinoGrande]
* Math Reasoning: [GSM8K], [MATH]

#### Coding Benchmark Results

Benchmark             | 2B    | 7B    | 7B-IT
--------------------- | ----- | ----- | -----
HumanEval             | 31.1  | 44.5  | 56.1
MBPP                  | 43.6  | 56.2  | 54.2
HumanEval Single Line | 78.41 | 76.09 | 68.25
HumanEval Multi Line  | 51.44 | 58.44 | 20.05
BC HE C++             | 24.2  | 32.9  | 42.2
BC HE C#              | 10.6  | 22.4  | 26.7
BC HE Go              | 20.5  | 21.7  | 28.6
BC HE Java            | 29.2  | 41.0  | 48.4
BC HE JavaScript      | 21.7  | 39.8  | 46.0
BC HE Kotlin          | 28.0  | 39.8  | 51.6
BC HE Python          | 21.7  | 42.2  | 48.4
BC HE Rust            | 26.7  | 34.1  | 36.0
BC MBPP C++           | 47.1  | 53.8  | 56.7
BC MBPP C#            | 28.7  | 32.5  | 41.2
BC MBPP Go            | 45.6  | 43.3  | 46.2
BC MBPP Java          | 41.8  | 50.3  | 57.3
BC MBPP JavaScript    | 45.3  | 58.2  | 61.4
BC MBPP Kotlin        | 46.8  | 54.7  | 59.9
BC MBPP Python        | 38.6  | 59.1  | 62.0
BC MBPP Rust          | 45.3  | 52.9  | 53.5

#### Natural Language Benchmarks (on 7B models)

![Natural Language Benchmarks on 7B models](images/nl_benchmarks.png)

## Ethics and Safety

### Ethics and Safety Evaluations

#### Evaluations Approach

Our evaluation methods include structured evaluations and internal red-teaming 
testing of relevant content policies. Red-teaming was conducted by a number of
different teams, each with different goals and human evaluation metrics.
These models were evaluated against a number of different categories relevant to
ethics and safety, including:

* Human evaluation on prompts covering content safety and representational
harms. See the
[Gemma model card](https://ai.google.dev/gemma/docs/model_card#evaluation_results)
for more details on evaluation approach.

* Specific testing of cyber-offence capabilities, focusing on testing autonomous
hacking capabilities and ensuring potential harms are limited.

#### Evaluation Results

The results of ethics and safety evaluations are within acceptable thresholds
for meeting
[internal policies](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/2023_Google_AI_Principles_Progress_Update.pdf#page=11)
for categories such as child safety, content safety, representational harms,
memorization, large-scale harms. See the
[Gemma model card](https://ai.google.dev/gemma/docs/model_card#evaluation_results)
for more details.

### Ethical considerations and risks

The development of large language models (LLMs) raises several ethical concerns.
In creating an open model, we have carefully considered the following:

*   **Bias and fairness**
*   LLMs trained on large-scale, real-world text data can reflect
socio-cultural biases embedded in the training material. These models
underwent careful scrutiny, input data pre-processing described and
posterior evaluations reported in this card.
*   **Misinformation and misuse**
*   LLMs can be misused to generate text that is false, misleading, or
harmful.
*   Guidelines are provided for responsible use with the model, see the
[Responsible Generative AI
Toolkit](https://ai.google.dev/gemma/responsible).
*   **Transparency and accountability**
*   This model card summarizes details on the models' architecture,
capabilities, limitations, and evaluation processes.
*   A responsibly developed open model offers the opportunity to share
innovation by making LLM technology accessible to developers and
researchers across the AI ecosystem.

Risks Identified and Mitigations:

*   **Perpetuation of biases:** It's encouraged to perform continuous monitoring
(using evaluation metrics, human review) and the exploration of de-biasing
techniques during model training, fine-tuning, and other use cases.
*   **Generation of harmful content:** Mechanisms and guidelines for content
safety are essential. Developers are encouraged to exercise caution and
implement appropriate content safety safeguards based on their specific
product policies and application use cases.
*   **Misuse for malicious purposes:** Technical limitations and developer and
end-user education can help mitigate against malicious applications of LLMs.
Educational resources and reporting mechanisms for users to flag misuse are
provided. Prohibited uses of Gemma models are outlined in our [terms of
use](https://www.kaggle.com/models/google/gemma/license/consent).
*   **Privacy violations:** Models were trained on data filtered for removal of
PII (Personally Identifiable Information). Developers are encouraged to
adhere to privacy regulations with privacy-preserving techniques.

### Benefits

At the time of release, this family of models provides high-performance open
code-focused large language model implementations designed from the ground up
for Responsible AI development compared to similarly sized models.

Using the coding benchmark evaluation metrics described in this document, these
models have shown to provide superior performance to other, comparably-sized
open model alternatives.

[HumanEval (HE)]: https://arxiv.org/abs/2107.03374         
[BabelCode (BC)]: https://github.com/google-research/babelcode
[MBPP]: https://arxiv.org/abs/2108.07732
[BoolQ]: https://arxiv.org/abs/1905.10044
[PIQA]: https://arxiv.org/abs/1911.11641
[TriviaQA]: https://arxiv.org/abs/1705.03551
[ARC-Challenge]: https://arxiv.org/abs/1911.01547
[HellaSwag]: https://arxiv.org/abs/1905.07830
[MMLU]: https://arxiv.org/abs/2009.03300
[WinoGrande]: https://arxiv.org/abs/1907.10641
[GSM8K]: https://arxiv.org/abs/2110.14168
[MATH]: https://arxiv.org/abs/2103.03874

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
"model": "google/codegemma-7b",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```