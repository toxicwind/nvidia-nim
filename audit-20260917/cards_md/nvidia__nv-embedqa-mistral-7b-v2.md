---
title: "nv-embedqa-mistral-7b-v2"
publisher: "nvidia"
type: "endpoint"
updated: "2025-03-11T16:27:06.248Z"
description: "Multilingual text question-answering retrieval, transforming textual information into dense vector representations."
canonical: "https://build.nvidia.com/nvidia/nv-embedqa-mistral-7b-v2"
---

## Model Overview<a id="model-overview"></a>

### Description<a id="description"></a>

The NVIDIA Retrieval QA Mistral 7B Embedding model is an embedding model optimized for text question-answering retrieval.

An embedding model is a crucial component of a text retrieval system, as it transforms textual information into dense vector representations. They are typically transformer encoders that process tokens of input text (for example, question, passage) to output an embedding.

This model is ready for commercial use.

NVIDIA Retrieval QA Mistral 7B Embedding model is part of the NVIDIA NeMo Retriever, which provides state-of-the-art, commercially-ready models and microservices, optimized for the lowest latency and highest throughput. It features a production-ready information retrieval pipeline with enterprise support. The models that form the core of this solution have been trained using responsibly selected, auditable data sources. With multiple pre-trained models available as starting points, developers can also readily customize them for their domain-specific use cases, such as Information Technology, Human Resource help assistants, and Research & Development research assistants.

### Intended use<a id="intended-use"></a>

The NVIDIA Retrieval QA Mistral 7B Embedding model is most suitable for users who want to build a question and answer application over a large text corpus, leveraging the latest dense retrieval technologies.

### License/Terms of use<a id="terms-of-use"></a>

The use of this model is governed by the [NVIDIA AI Foundation Models Community License Agreement](https://developer.nvidia.com/downloads/nv-ai-foundation-models-license) and the [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/).

Technology can have a profound impact on people and the world, and NVIDIA is committed to enabling trust and transparency in AI development. NVIDIA encourages users to adopt principles of AI ethics and trustworthiness to guide your business decisions by following the guidelines in the NVIDIA AI Foundation Models Community License Agreement.

### Model Architecture<a id="model-architecture"></a>

**Architecture Type:** Transformer <br>
**Network Architecture:** Fine-tuned Mistral 7B foundation model <br>
**Embedding Dimension:** 4096 <br>
**Parameter Count:** 7.1 billion <br>

The NVIDIA Retrieval QA Mistral 7B Embedding model is a transformer encoder - a fine-tuned version of [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1), with 32 layers and 4096 as embedding size, which is trained on public datasets. Mistral Models are pre-trained with casual attention. As our research demonstrated that bi-directional attention improved the performance, we converted the model to bi-directional attention. Embedding models for text retrieval are typically trained using a bi-encoder architecture. This involves encoding a pair of sentences (for example, query and chunked passages) independently using the embedding model. Contrastive learning is used to maximize the similarity between the query and the passage that contains the answer, while minimizing the similarity between the query and sampled negative passages not useful to answer the question.

### Model Version(s)<a id="model-versions"></a>

NVIDIA Retrieval QA Mistral 7B Embedding v2

Short name: NV-EmbedQA-Mistral-7B-v2

## Training Dataset & Evaluation<a id="training-dataset--evaluation"></a>

### Training Dataset<a id="training-dataset"></a>

The development of large-scale public open-QA datasets has enabled tremendous progress in powerful embedding models. However, one popular dataset named [MS MARCO](https://microsoft.github.io/msmarco/) restricts commercial licensing, limiting the use of these models in commercial settings. To address this, we created our own training dataset blend based on public QA datasets, which each has a license for commercial applications. The pretrained [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) embedding model was fine-tuned with contrastive learning with the prefix of “query:” for questions and “passage:” for context passages, using a mixture of commercially-viable public datasets.

The training dataset details are as follows:

**Use Case:** Information retrieval for question and answering over text documents. <br>
**Data Sources:** Public datasets licensed for commercial use. <br>
**Language:** English (US), potential support for other languages (in research) <br>
**Volume:** 600k samples from public datasets <br>
**Data Collection Method by dataset:** Unknown <br>
**Labeling Method by dataset:** Unknown

### Evaluation Results<a id="evaluation-results"></a>

We evaluated the NVIDIA Retrieval QA Mistral 7B Embedding model in comparison to literature open & commercial retriever models on academic benchmarks for question-answering - [NQ](https://huggingface.co/datasets/BeIR/nq), [HotpotQA](https://huggingface.co/datasets/hotpot_qa) and [FiQA(Finance Q\&A)](https://huggingface.co/datasets/BeIR/fiqa) from BeIR benchmark, and TechQA dataset. Note that the model was evaluated offline on A100 GPUs using the model's PyTorch checkpoint. In this benchmark, the metric used was Recall@5.

| **Open & Commercial Retrieval Models** | **Average Recall@5 on NQ, HotpotQA, FiQA, TechQA dataset** |
| :------------------------------------: | :--------------------------------------------------------: |
|        NV-EmbedQA-Mistral-7B-v2        |                           72.97%                           |
|        NV-EmbedQA-Mistral-7B-v1        |                           64.93%                           |
|            NV-EmbedQA-E5-v5            |                           62.07%                           |
|            NV-EmbedQA-E5-v4            |                           57.65%                           |
|         E5-large-unsupervised          |                           48.03%                           |
|                  BM25                  |                           44.67%                           |

**Data Collection Method by dataset:** Unknown <br>
**Labeling Method by dataset:** Unknown <br>
**Properties:** The evaluation datasets are based on the MTEB/BEIR TextQA, and [TechQA dataset](https://huggingface.co/datasets/PrimeQA/TechQA/tree/main) which are 4 public datasets. The size ranges between 10,000s up to 5M depending on the dataset. <br>

## Technical Details<a id="technical-details"></a>

### Input<a id="input"></a>

**Input Type:** Text <br>
**Input Format:** List of strings <br>
**Other Properties Related to Input:** The model was trained with input length up to 512 tokens, whereas the Mistral-7B model has a theoretical attention span of approximately 131K tokens.

### Output<a id="output"></a>

**Output Type:** Floats <br>
**Output Format:** List of float arrays <br>
**Other Properties Related to Output:** Model outputs embedding vectors of dimension 4096 for each text string.

### Software Integration<a id="software-integration"></a>

**Runtime:** NeMo Retriever Text Embedding NIM <br>
**Supported Hardware Microarchitecture Compatibility:** NVIDIA Ampere, NVIDIA Hopper, NVIDIA Lovelace <br>
**Supported Operating System(s):** Linux <br>
**Engine:** [TensorRT](https://developer.nvidia.com/tensorrt-getting-started) <br>
**Test Hardware:** See Support Matrix from [NIM documentation](https://docs.nvidia.com/nim/nemo-retriever/text-embedding/latest/overview.html). <br>

We evaluated the models optimized for different hardware on a small sample dataset of 600 queries.

## Ethical Considerations<a id="ethical-considerations"></a>

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. For more detailed information on ethical considerations for this model, please see the Model Card++ tab for the Explainability, Bias, Safety & Security, and Privacy subcards. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

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
|Output:                        | Array of float numbers (Dense Vector Representation for the input text) |
|Describe how the model works:  | Model transforms the tokenized input text into a dense vector representation.  |
|Performance Metrics:           | Throughput and Latency                                         |
|Potential Known Risks:         | This model does not always guarantee to retrieve the correct passage(s) for a given query. |
|Licensing:                     | [NVIDIA AI Foundation Models Community License Agreement](https://developer.nvidia.com/downloads/nv-ai-foundation-models-license) and the [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/) |
|Technical Limitations:         | The model was trained with input length up to 512 tokens, therefore, it may perform poorly on specialized longer text inputs. |

## Privacy

| Field              | Response |
|:-------------------|:---------|
|Generatable or reverse engineerable personally-identifiable information (PII)?    | Neither              |
|Was consent obtained for any PII used?                                            | Not Applicable       |
|Personal data used to create this model?                                          | None                 |
|How often is dataset reviewed?                                                    | Before Every Release |
|Is a mechanism in place to honor data subject right of access or deletion of personal data? | No         |
|If personal data was collected for the development of the model, was it collected directly by NVIDIA? | Not Applicable |
|If personal data was collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects? | Not Applicable |
|If personal data collected for the development of this AI model, was it minimized to only what was required? | Not Applicable |
|Is there provenance for all datasets used in training?                            | Yes                  |
|Does data labeling (annotation, metadata) comply with privacy laws?               | Yes                  |
|Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data|

## Safety & Security

| Field              | Response |
|:-------------------|:---------|
|Verified to have met prescribed quality standards: | Yes |
|Target Key Performance Indicator(s) (KPI(s)): | Accuracy, Latency, Throughput |
|Model Application(s):                                 | Text Embedding for Retrieval    |
|Describe the physical safety impact (if present).     | Not Applicable                  |
|Use Case Restrictions:| Commercial license available from NVIDIA AI Enterprise. |
|Model and dataset restrictions:| The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```bash
invoke_url='https://integrate.api.nvidia.com/v1/embeddings'

authorization_header='Authorization: Bearer '
accept_header='Accept: application/json'
content_type_header='Content-Type: application/json'

data=$'{
"model": "nvidia/nv-embedqa-mistral-7b-v2",
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
model="nvidia/nv-embedqa-mistral-7b-v2",
encoding_format="float",
extra_body={"input_type": "", "truncate": "NONE"}
)

print(response.data[0].embedding)
```

```python
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

client = NVIDIAEmbeddings(
model="nvidia/nv-embedqa-mistral-7b-v2", 
api_key="$NVIDIA_API_KEY", 
truncate="NONE", 
)

embedding = client.embed_query("")
print(embedding)
```