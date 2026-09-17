---
title: "embed-qa-4"
publisher: "nvidia"
type: "endpoint"
updated: "2025-06-30T20:36:49.023Z"
description: "GPU-accelerated generation of text embeddings used for question-answering retrieval."
canonical: "https://build.nvidia.com/nvidia/embed-qa-4"
---

## Model Overview

### Description

The NVIDIA Retrieval QA Embedding Model is an embedding model optimized for text question-answering retrieval. An embedding model is a crucial component of a text retrieval system, as it transforms textual information into dense vector representations. They are typically transformer encoders that process tokens of input text (for example, question, passage) to output an embedding.

NVIDIA Retrieval QA Embedding Model is a part of NVIDIA NeMo Retriever, which provides state-of-the-art, commercially-ready models and microservices, optimized for the lowest latency and highest throughput. It features a production-ready information retrieval pipeline with enterprise support. The models that form the core of this solution have been trained using responsibly selected, auditable data sources. With multiple pre-trained models available as starting points, developers can also readily customize them for their domain-specific use cases, such as Information Technology, Human Resource help assistants, and Research & Development research assistants.

### Terms of use

The use of this model is governed by
the [NVIDIA NeMo Foundational Models Evaluation License Agreement](https://registry.ngc.nvidia.com/orgs/ohlfw0olaadg/teams/ea-participants/resources/nemo_foundational_models_evaluation_license/files)

### References(s)

The NVIDIA Retrieval QA Embedding model is meant to be deployed using the [NeMo Retriever Embedding Microservice](https://registry.ngc.nvidia.com/orgs/ohlfw0olaadg/teams/ea-participants/containers/nemo-retriever-embedding-microservice). Check out the microservice documentation for more details.

[Technical Blog](https://developer.nvidia.com/blog/build-enterprise-retrieval-augmented-generation-apps-with-nvidia-retrieval-qa-embedding-model/)

### Intended use

The NVIDIA Retrieval QA Embedding model is most suitable for users who want to build a question and answer application over a large text corpus, leveraging the latest dense retrieval technologies.

### Model Architecture

**Architecture Type:** Transformer <br>
**Network Architecture:** Fine-tuned E5-Large-Unsupervised retriever <br>
**Embedding Dimension:** 1024 <br>
**Parameter Count:** 335 million <br>

The NVIDIA Retrieval QA Embedding Model is a transformer encoder - a finetuned version of [E5-Large-Unsupervised](https://huggingface.co/intfloat/e5-large-unsupervised), with 24 layers and an embedding size of 1024, which is trained on private and public datasets as described in the Dataset and Training section. It supports a maximum input of 512 tokens.

Embedding models for text retrieval are typically trained using a bi-encoder architecture. This involves encoding a pair of sentences (for example, query and chunked passages) independently using the embedding model. Contrastive learning is used to maximize the similarity between the query and the passage that contains the answer, while minimizing the similarity between the query and sampled negative passages not useful to answer the question.

### Input

**Input Type:** text <br>
**Input Format:** list of strings <br>

### Output

**Output Type:** floats <br>
**Output Format:** list of float arrays, each array containing the embeddings for the corresponding input string. <br>

### Model Version(s)

NVIDIA Retrieval QA Embedding Model-4.0

## Training Dataset & Evaluation

### Training Dataset

The development of large-scale public open-QA datasets has enabled tremendous progress in powerful embedding models. However, one popular dataset named [MSMARCO](https://microsoft.github.io/msmarco/) restricts ‌commercial licensing, limiting the use of these models in commercial settings. To address this, we created our own internal open-domain QA dataset to train a commercially-viable embedding model. For NVIDIA proprietary data collection, we searched the passages from web logs and selected a collection of passages relevant to customer use cases for annotation by the NVIDIA internal data annotation team.

To minimize the redundancy in our data collection process, we selected samples that maximized relevancy distance scores and increased diversity in the data. The pretrained [E5-Large-Unsupervised](https://huggingface.co/intfloat/e5-large-unsupervised) embedding model was fine-tuned with contrastive learning with the prefix of “query:” for questions and “passage:” for context passages. Specifically, a mixture of English language datasets are used including our proprietary dataset, along with selected samples from commercially-viable public datasets. The AdamW optimizer is employed, incorporating 300 warm-up steps and 1e-6 learning rate with linear annealing schedule.

The training dataset details are as follows:

**Use Case**: Information retrieval for question and answering over text documents. <br>

**Data Sources**:  <br>
- Public datasets licensed for commercial use. <br>
- Text from public websites. <br>
- Annotations created by NVIDIA’s internal team.<br>

**Language**: English (US) <br>

**Domains**: Knowledge, Description, Numeric (unit, time), Entity, Location, Person <br>

**Volume**: 40k internal proprietary samples, 200k samples from public dataset <br>

**High Level Schema**: <br>
- query: question text <br>
- doc: full document that contains the answer <br>
- chunk: section of the document that contains the answer <br>
- relevancy label: rating of how relevant the passage is to the question <br>
- span: exact token range in the chunk that contains the answer <br>

### Evaluation Results

We evaluated the NVIDIA Retrieval QA Embedding Model in comparison to literature open & commercial retriever models on academic benchmarks  - [NQ](https://huggingface.co/datasets/BeIR/nq), [HotpotQA](https://huggingface.co/datasets/hotpot_qa) and [FiQA(Finance Q&A)](https://huggingface.co/datasets/BeIR/fiqa) from BeIR benchmark, and the [TechQA(Tech Support Q&A)](https://arxiv.org/pdf/1911.02984v1.pdf) dataset. In this benchmark, the metric used was [Recall@5](https://en.wikipedia.org/wiki/Precision_and_recall).

| Open & Commercial Retrieval Models   | Average Recall@5 on NQ, HotpotQA, FiQA, TechQA dataset|
|-----------------------------|----------------------------|
| NVIDIA Retrieval QA         | 57.37%                     |
| E5-Large_unsupervised       | 45.58%                     |
| BM25                        | 39.97%                     |

We also evaluated our embedding model with real internal customer datasets from telco, IT, consulting, and energy industries. The metric was Recall@5, to emulate a retrieval augmented generation (RAG) scenario where we would provide the top five most relevant passages as context in the prompt for the LLM model that is going to respond to the question. We compared our model’s information retrieval accuracy to a number of well-known embedding models made available by the AI community, including ones trained on non-commercial dataset (which are marked with "*").

| Retrieval Model              | Average Recall@5 on Internal Customer Datasets |
|-----------------------------|-----------------------------|
| NVIDIA Retrieval QA         | 74.4%                       |
| DRAGON*                     | 72.7%                       |
| E5-Large*                   | 71.7%                       |
| BGE*                        | 71.1%                       |
| GTR*                        | 71.0%                       |
| Contriever*                 | 69.0%                       |
| GTE*                        | 63.9%                       |
| E5-Large_unsupervised       | 61.6%                       |
| BM25                        | 55.6%                       |

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-foundation/models/nvolve-29k/bias). Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

### Special Training Data Considerations

The model was trained on the data that may contain toxic language and societal biases originally crawled from the Internet. Therefore, the model may amplify those biases, for example, associating certain genders with certain social stereotypes.

## Bias

Field                                                                                               |  Response
:---------------------------------------------------------------------------------------------------|:---------------
Participation considerations from adversely impacted groups [protected classes](https://www.senate.ca.gov/content/protected-classes) in model design and testing:  |  None
Measures taken to mitigate against unwanted bias:                                                   |  None

## Explainability

| Field              | Response |
|:-------------------|:---------|
|Intended Application & Domain: | Passage and query embedding for question and answer retrieval  |
|Model Type:                    | Transformer encoder                                            |
|Intended User:                 | Generative AI creators working with conversational AI models.  |
|Output:                        | Text embedding (An array of float numbers, providing a dense vector representation for the input text) |
|Describe how the model works:  | The transformer encoder transforms the tokenized input text into a dense vector representation.  |
|Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | Not Applicable |
Verified to have met prescribed NVIDIA quality standards:  |  Yes
|Performance Metrics:           | Accuracy, Throughput, and Latency                                         |
|Potential Known Risks:         | The model was trained on the data that may contain toxic language and societal biases originally crawled from the Internet. Therefore, the model may amplify those biases, for example, associating certain genders with certain social stereotypes. |
|Licensing:                     | [NVIDIA NeMo Foundational Models Evaluation License Agreement](https://registry.ngc.nvidia.com/orgs/ohlfw0olaadg/teams/ea-participants/resources/nemo_foundational_models_evaluation_license/files)|
|Technical Limitations:         | The model's maximum context length is 512 tokens. Texts longer than maximum length must either be chunked or truncated.|

## Privacy

| Field              | Response |
|:-------------------|:---------|
|Generatable or reverse engineerable personally-identifiable information (PII)?    | None              |
|Was consent obtained for any PII used?                                            | Not Applicable       |
|IPII used to create this model?                                                   | None                 |
|How often is dataset reviewed?                                                    | Before Release |
|Is a mechanism in place to honor data subject right of access or deletion of personal data? | No         |
|If PII collected for the development of the model, was it collected directly by NVIDIA? | Not Applicable |
|If PII collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects? | Not Applicable |
|If PII collected for the development of this AI model, was it minimized to only what was required? | Not Applicable |
|Is there provenance for all datasets used in training?                            | Yes                  |
|Are we able to identify and trace source of dataset?                              | Yes                  |
|Does data labeling (annotation, metadata) comply with privacy laws?               | Yes                  | 
|Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data|

## Safety & Security

| Field              | Response |
|:-------------------|:---------|
|Model Application(s):                                 | Text Embedding for Retrieval    |
|Describe the life-critical impact (if present).     | Not Applicable                  |
|Use Case Restrictions:| Evaluation license for Non-Commerical Use Only. |
|Model and dataset restrictions:| The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```bash
invoke_url='https://integrate.api.nvidia.com/v1/embeddings'

authorization_header='Authorization: Bearer '
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data=$'{
"encoding_format": "float",
"truncate": "NONE",
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

```python
from openai import OpenAI

client = OpenAI(
api_key="$NVIDIA_API_KEY",
base_url="https://integrate.api.nvidia.com/v1"
)

response = client.embeddings.create(
input=[""],
model="nvidia/embed-qa-4",
encoding_format="float",
extra_body={"input_type": "", "truncate": "NONE"}
)

print(response.data[0].embedding)
```

```python
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

client = NVIDIAEmbeddings(
model="NV-Embed-QA", 
api_key="$NVIDIA_API_KEY", 
truncate="NONE", 
)

embedding = client.embed_query("")
print(embedding)
```