---
title: "arctic-embed-l"
publisher: "snowflake"
type: "endpoint"
updated: "2025-03-21T13:13:13.363Z"
description: "Optimized community model for text embedding."
canonical: "https://build.nvidia.com/snowflake/arctic-embed-l"
---

## Model Overview

### Description

snowflake-arctic-embed is a suite of text embedding models that creates high-quality retrieval models optimized for performance.  These models are ready for commercial use free-of-charge. 

The snowflake-arctic-embedding models achieve state-of-the-art performance on the MTEB/BEIR leaderboard for each of their size variants. As shown below, each class of model size achieves SOTA retrieval accuracy compared to other top models.

The models are trained by leveraging existing open-source text representation models, such as bert-base-uncased, and are trained in a multi-stage pipeline to optimize their retrieval performance. Following pretraining, models are further optimized with long training on a smaller dataset (about 1m samples) of triplets of query, positive document, and negative document derived from hard harmful mining. Mining of the negatives and data curation is crucial to retrieval accuracy.

| Name                                                                    | MTEB Retrieval Score (NDCG @ 10) | Parameters (Millions) | Embedding Dimension |
| ----------------------------------------------------------------------- | -------------------------------- | --------------------- | ------------------- |
| [snowflake-arctic-embed-xs](https://huggingface.co/Snowflake/snowflake-arctic-embed-xs/)     | 50.15                            | 22                    | 384                 |
| [snowflake-arctic-embed-s](https://huggingface.co/Snowflake/snowflake-arctic-embed-s/)      | 51.98                            | 33                    | 384                 |
| [snowflake-arctic-embed-m](https://huggingface.co/Snowflake/snowflake-arctic-embed-m/)      | 54.90                            | 110                   | 768                 |
| [snowflake-arctic-embed-m-long](https://huggingface.co/Snowflake/snowflake-arctic-embed-m-long/) | 54.83                            | 137                   | 768                 |
| [snowflake-arctic-embed-l](https://huggingface.co/Snowflake/snowflake-arctic-embed-l/)      | 55.98                            | 335                   | 1024                |

Based on the [intfloat/e5-large-unsupervised](https://huggingface.co/intfloat/e5-large-unsupervised) model, the large model is a direct drop-in for closed APIs and delivers the most accurate retrieval experience.

| Model Name                                                         | MTEB Retrieval Score (NDCG @ 10) |
| ------------------------------------------------------------------ | -------------------------------- |
| [snowflake-arctic-embed-l](https://huggingface.co/Snowflake/snowflake-arctic-embed-l/) | 55.98        |
| Google-gecko-text-embedding                                        | 55.7                             |
| text-embedding-3-large                                             | 55.44                            |
| Cohere-embed-english-v3.0                                          | 55.00                            |
| bge-large-en-v1.5                                                  | 54.29                            |
| UAE-Large-V1                                                       | 54.66                            |
| bge-large-en-v1.5                                                  | 54.29                            |
| mxbai-embed-large-v1                                               | 54.39                            |
| e5-Large-v2                                                        | 50.56                            |

### Terms of use

Arctic is licensed under the [Apache-2](https://www.apache.org/licenses/LICENSE-2.0). 

### References

[HuggingFace](https://huggingface.co/Snowflake/snowflake-arctic-embed-l/)

[Github](https://github.com/Snowflake-Labs/arctic-embed)

[Blog post](https://www.snowflake.com/blog/introducing-snowflake-arctic-embed-snowflakes-state-of-the-art-text-embedding-family-of-models/)

## Model Architecture

**Architecture Type:** Transformer <br>
**Network Architecture:** Fine-tuned E5-Large-Unsupervised Retriever <br>
**Embedding Dimension:** 1024 <br>
**Parameter Count:** 335 million <br>

## Input

**Input Type:** Text <br>
**Input Format:** List of strings <br>

## Output

**Output Type:** Floating Points <br>
**Output Format:** list of float arrays <br>
**Other Properties Related to Output:** Each array contains the embeddings for the corresponding input string. <br>

## Model Version

`snowflake-arctic-embed-l`

## Supported Operating System(s):
* Linux <br>

## Training Dataset:

**Properties (Quantity, Dataset Descriptions, Sensor(s)):** Pretrained on large batches of query-document pairs where negatives are derived in-batch—pretraining leverages about 400m samples of a mix of public datasets and proprietary web search data. <br>

# Inference:
**Engine:** [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) with [Triton](https://developer.nvidia.com/triton-inference-server) <br>
**Test Hardware:** L40 <br>

## Prototype

```bash
invoke_url='https://ai.api.nvidia.com/v1/retrieval/snowflake/arctic-embed-l/embeddings'

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

```python
from openai import OpenAI

client = OpenAI(
api_key="$NVIDIA_API_KEY",
base_url="https://ai.api.nvidia.com/v1/retrieval/snowflake/arctic-embed-l"
)

response = client.embeddings.create(
input=[""],
model="snowflake/arctic-embed-l",
encoding_format="",
extra_body={"input_type": "", "truncate": "NONE"}
)

print(response.data[0].embedding)
```

```python
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

client = NVIDIAEmbeddings(
model="snowflake/arctic-embed-l", 
api_key="$NVIDIA_API_KEY", 
truncate="", 
)

embedding = client.embed_query("")
print(embedding)
```