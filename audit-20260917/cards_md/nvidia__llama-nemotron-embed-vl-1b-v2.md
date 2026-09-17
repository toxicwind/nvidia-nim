---
title: "llama-nemotron-embed-vl-1b-v2"
publisher: "nvidia"
type: "endpoint"
updated: "2026-02-10T04:49:01.412Z"
description: "Multimodal question-answer retrieval representing user queries as text and documents as images."
canonical: "https://build.nvidia.com/nvidia/llama-nemotron-embed-vl-1b-v2"
---

# Llama-Nemotron-Embed-VL-1B-v2

## Description

The Llama-Nemotron-Embed-VL-1B-v2 model is optimized for **multimodal** question-answering retrieval. The model can embed 'documents' in the form of image, text, or image and text combined. Documents can be retrieved given a user query in text form. The model supports images containing text, tables, charts, and infographics. This model was evaluated on [ViDoRe V1](https://huggingface.co/spaces/vidore/vidore-leaderboard) and two internal multimodal retrieval benchmarks.

An embedding model is a crucial component of a retrieval system, because it transforms information into dense vector representations. An embedding model is typically a transformer encoder that processes tokens of input (text or image) (for example: question, passage) to output an embedding. The Llama-Nemotron-Embed-VL-1B-v2 model is a combined language model and vision model.

The Llama-Nemotron-Embed-VL-1B-v2 model is a part of the NVIDIA NeMo Retriever collection of NIM, which provides state-of-the-art, commercially-ready models and microservices optimized for the lowest latency and highest throughput. It features a production-ready information retrieval pipeline with enterprise support. The models that form the core of this solution have been trained using responsibly selected, auditable data sources. With multiple pre-trained models available as starting points, developers can readily customize them for domain-specific use cases, such as information technology, human resource help assistants, and research & development research assistants.

*This model is ready for commercial use.*

## License and Terms of Use:

**GOVERNING TERMS:** The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). ADDITIONAL INFORMATION: [Llama 3.2 Community License Agreement](https://www.llama.com/llama3_2/license/). Built with Llama.

**You are responsible for ensuring that your use of NVIDIA provided models complies with all applicable laws.**

## Deployment Geography:
Global

## Use Case:
**Use Case:** The Llama-Nemotron-Embed-VL-1B-v2 model is most suitable for users who want to build a multimodal question-and-answer application over a large corpus, leveraging the latest dense retrieval technologies.

## Release Date:
**Build.NVIDIA.com:** 02/10/2026 via [link](https://build.nvidia.com/nvidia/llama-nemotron-embed-vl-1b-v2)  
**Huggingface:** 12/18/2025 via [link](https://huggingface.co/nvidia/llama-nemotron-embed-vl-1b-v2)

## Reference(s):
**References:**
- [ViDoRe V1 Benchmark](https://huggingface.co/spaces/vidore/vidore-leaderboard)
- [Eagle 2 Work](https://arxiv.org/abs/2501.14818)

## Model Architecture:
**Architecture Type:** Transformer  
**Network Architecture:** Fine-tuned MultiModal Llama 3.2 1B Retriever

This NeMo Retriever embedding model is a transformer encoder. It is a fine-tuned version of Llama 3.2 1B with SigLip2 400M, with 16 layers and an embedding size of 2048, which is trained on public datasets. Embedding models for text retrieval are typically trained using a bi-encoder architecture. This involves encoding a pair of query and document independently using the embedding model. Contrastive learning is used in this model to maximize the similarity between the query and the document that contains the answer, while minimizing the similarity between the query and sampled negative documents not useful to answer the question.

The vision-language model encoder incorporates key innovations from NVIDIA, including [Eagle 2 work](https://arxiv.org/abs/2501.14818) and [nemoretriever-parse](https://build.nvidia.com/nvidia/nemoretriever-parse), which use a tiling-based VLM architecture. This architecture, available on [Hugging Face](https://huggingface.co/collections/nvidia/eagle-2-6764ba887fa1ef387f7df067), significantly enhances multimodal understanding through its dynamic tiling and mixture of vision encoders design. It particularly improves performance on tasks that involve high-resolution images and complex visual content.

### Input:
**Input Types:** Text (for queries), Text | Image (for documents)  
**Input Formats:** List of strings (for queries), List of strings | List of Images (for documents)  
**Input Parameters:** One Dimensional (1D)  
**Other Input Properties:** The model's maximum context length is 8192 tokens. Texts longer than maximum length must either be chunked or truncated. Images must be `8192 x 16384` or `16384 x 8192` and less than 25MB. They are resized automatically by the NIM.

### Output:
**Output Types:** Floats  
**Output Format:** List of float arrays  
**Output Parameters:** One Dimensional (1D)  
**Other Output Properties:** Model outputs embedding vectors of maximum dimension 2048 for each input.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:
**Runtime Engines:**
- **NeMo Retriever Embedding NIM:** Primary runtime engine

**Supported Hardware:**
- **NVIDIA Ampere:** A100, A6000, A40
- **NVIDIA Blackwell:** B200, B100, GB200
- **NVIDIA Hopper:** H100, H200
- **NVIDIA Lovelace:** L40S, L40, RTX 6000 Ada Generation

**Operating Systems:** Linux

**Additional Testing Statement:**
__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Inference
**Acceleration Engine:** TensorRT <br>
**Test Hardware:** H100 PCIe/SXM, A100 PCIe/SXM, L40s, L4, and A10G

## Model Version(s)
Llama-Nemotron-Embed-VL-1B-v2

Short Name: `llama-nemotron-embed-vl-1b-v2`

## Training, Testing, and Evaluation Datasets:

### Training Dataset
**Data Modality:** Text, Image  
**Data Sources:** Public QA datasets with commercial licensing. The text component is comprised of semi-supervised pre-training on 12M samples from public datasets and fine-tuning on 1.5M samples from public datasets. The VLM component uses only commercially-viable data from the [Eagle2](https://github.com/NVlabs/EAGLE) training data.  
**Data Collection Method:** Hybrid: Automated, Human, Synthetic  
**Labeling Method:** Hybrid: Automated, Human, Synthetic  
**Other Properties:** NVIDIA's training dataset is based on public QA datasets, and only includes datasets that have a license for commercial applications.

### Evaluation Datasets
**Data Modality:** Text, Image  
**Data Sources:** [ViDoRe V1](https://huggingface.co/spaces/vidore/vidore-leaderboard) benchmark and two internal multimodal retrieval benchmarks. One internal dataset (DigitalCorpora-767) can be created by following instructions in [this notebook](https://github.com/NVIDIA/nv-ingest/blob/main/evaluation/digital_corpora_download.ipynb).  
**Data Collection Method:** Hybrid: Automated, Human, Synthetic  
**Labeling Method:** Hybrid: Automated, Human, Synthetic  
**Other Properties:** [DigitalCorpora-767](https://github.com/NVIDIA/nv-ingest/blob/main/evaluation/digital_corpora_download.ipynb) is a set of 767 PDFs that have a good mixture of text, tables, and charts.

### Evaluation Results

We evaluated the NeMo Retriever Multimodal Embedding Model against both published literature and existing open-source and commercial retriever models. Our evaluation used three benchmark datasets for question-answering tasks: the public [ViDoRe V1](https://huggingface.co/spaces/vidore/vidore-leaderboard) benchmark and two internal multimodal retrieval benchmarks.

| Model                                          | # Params Vision (in M) | # Params LLM-backbone (in M) | Average Recall@5 on DigitalCorpora-767, Earnings, ViDoRe V1 |
|------------------------------------------------|------------------------|------------------------------|--------------|
| llama-nemotron-embed-vl-1b-v2                  |                    429 |                         1236 |        80.9% |
| llamaindex/vdr-2b-multi-v1                     |                    665 |                         1544 |        80.9% |
| MrLight/dse-qwen2-2b-mrl-v1                    |                    665 |                         1544 |        80.4% |
| Alibaba-NLP/gme-Qwen2-VL-2B-Instruct           |                    665 |                         1544 |        79.9% |

We do not compare to col-style embedding (late interaction) models because late interaction embeddings require a significant embedding store.

### Detailed Performance Analysis

The model's performance was evaluated across different modalities and compared with other models using various pipelines. The following table contains the detailed results for the DigitalCorpora-767 dataset:

| Modality | Queries | Text-based Pipeline | VLM-based Pipeline<br>(llama-nemotron-embed-vl-1b-v2) |
|----------|---------|---------------------|------------------------------------------------------|
| Multimodal | 991 | 0.845 | 0.865 |
| Table | 235 | 0.753 | 0.838 |
| Chart | 268 | 0.881 | 0.881 |
| Text | 488 | 0.869 | 0.869 |

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case, and address unforeseen product misuse.

For more detailed information on ethical considerations for this model, see the Model Card++ subcards: Bias, Explainability, Privacy, and Safety & Security.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Context Length:** 16,384 tokens
- **Parameters:** 1,678,252,480

## Bias

# Bias Subcard - Llama-Nemotron-Embed-VL-1B-v2

| Field | Response |
| ----- | ----- |
| Participation considerations from adversely impacted groups [protected classes](https://calcivilrights.ca.gov/disputeresolution/protected-characteristics/) in model design and testing | None |
| Measures taken to mitigate against unwanted bias | None |

## Explainability

# Explainability Subcard - Llama-Nemotron-Embed-VL-1B-v2

| Field | Response |
| ----- | ----- |
| Intended Application & Domain: | Document and query embedding for question and answer retrieval. |
| Model Type: | Transformer encoder. |
| Intended User: | Generative AI creators working with conversational AI models. Users who want to build a question and answer application over a large corpus, leveraging the latest dense retrieval technologies. The corpus can be images of PDFs, such as text, tables, charts or infographics. |
| Output: | Array of float numbers (Dense Vector Representation for the input text). |
| Describe how the model works: | Model transforms the input into a dense vector representation. |
| Performance Metrics: | Accuracy, Throughput, and Latency. |
| Potential Known Risks: | This model does not guarantee to always retrieve the correct passage(s) for a given query. |
| Technical Limitations: | The model's max sequence length is 8192. Longer text inputs should be truncated. |
| Name the adversely impacted groups this has been tested to deliver comparable outcomes regardless of: | N/A |
| Verified to have met prescribed NVIDIA quality standards: | Yes |

## Privacy

# Privacy Subcard - Llama-Nemotron-Embed-VL-1B-v2

| Field | Response |
| ----- | ----- |
| Generatable or reverse engineerable personal data? | None |
| Personal data used to create this model? | None |
| How often is dataset reviewed? | Dataset is initially reviewed upon addition, and subsequent reviews are conducted as needed or upon request for changes. |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | No, not possible with externally-sourced data. |
| Applicable Privacy Policy | https://www.nvidia.com/en-us/about-nvidia/privacy-policy/ |

## Safety & Security

# Safety and Security Subcard - Llama-Nemotron-Embed-VL-1B-v2

| Field | Response |
| ----- | ----- |
| Model Application Field(s): | Document Embedding for Retrieval. User queries can be text and documents can be images of text, charts, tables, and infographics. |
| Describe the life critical impact (if present). | Not applicable |
| Use Case Restrictions: | Abide by The trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). ADDITIONAL INFORMATION: [Llama 3.2 Community License Agreement](https://www.llama.com/llama3_2/license/). Built with Llama. |
| Model and dataset restrictions: | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```bash
image_source="https://assets.ngc.nvidia.com/products/api-catalog/nemo-retriever/embedding/court-sizing-metrics.png"
if [[ $image_source == http* ]]; then
base64_image=$(curl -s "${image_source}" | base64 -w 0)
else
base64_image=$(base64 -w 0 < "${image_source}")
fi

json_payload='{
"input": ["data:image/png;base64,'"${base64_image}"'"],
"model": "nvidia/llama-nemotron-embed-vl-1b-v2",
"modality": ["image"],
"input_type": "",
"encoding_format": "float",
"truncate": "NONE"
}'

echo "${json_payload}" | \
curl -X POST https://integrate.api.nvidia.com/v1/embeddings \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $NVIDIA_API_KEY" \
-d @-
```

```python
import base64
import requests
from openai import OpenAI

image_source = "https://assets.ngc.nvidia.com/products/api-catalog/nemo-retriever/embedding/court-sizing-metrics.png"

if image_source.startswith(('http://', 'https://')):
response = requests.get(image_source)
image_b64 = base64.b64encode(response.content).decode()
else:
with open(image_source, "rb") as image_file:
image_b64 = base64.b64encode(image_file.read()).decode()

client = OpenAI(
api_key="$NVIDIA_API_KEY",
base_url="https://integrate.api.nvidia.com/v1"
)

response = client.embeddings.create(
input=[f"data:image/png;base64,{image_b64}"],
model="nvidia/llama-nemotron-embed-vl-1b-v2",
encoding_format="float",
extra_body={"modality": ["image"], "input_type": "", "truncate": "NONE"}
)

print(response.data[0].embedding)
```

```python
import base64
import requests
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

image_source = "https://assets.ngc.nvidia.com/products/api-catalog/nemo-retriever/embedding/court-sizing-metrics.png"

if image_source.startswith(('http://', 'https://')):
response = requests.get(image_source)
image_b64 = base64.b64encode(response.content).decode()
else:
with open(image_source, "rb") as image_file:
image_b64 = base64.b64encode(image_file.read()).decode()

client = NVIDIAEmbeddings(
model="nvidia/llama-nemotron-embed-vl-1b-v2",
api_key="$NVIDIA_API_KEY",
truncate="NONE",
)

image_input = f"data:image/png;base64,{image_b64}"

embedding = client.embed_documents([image_input])
print(embedding)
```