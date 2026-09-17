---
title: "yi-large"
publisher: "01-ai"
type: "endpoint"
updated: "2025-07-20T16:36:18.102Z"
description: "Powerful model trained on English and Chinese for diverse tasks including chatbot and creative writing."
canonical: "https://build.nvidia.com/01-ai/yi-large"
---

# Yi-Large Model Card

## Model Overview

Yi-Large is a model for generating code as well as logic and mathematical reasoning.  It is the latest proprietary dense model of the Yi Series State of the Art Large Language Models from 01.AI. The model was trained with significant improvement from the November 2023 Yi-34B open-source model detailed in this [tech report](https://arxiv.org/pdf/2403.04652). The larger and enhanced Yi-Large model demonstrates exceptional performance on all the benchmarks, especially code, math, and comprehensive reasoning. Overall, Yi-Large performs on par with GPT-4 and Claude3.

In addition, under its vision to Make AGI Accessible and Beneficial to Everyone and Everywhere, 01.AI values the needs and differences across different languages and cultures. Yi-Large performs strongly on multilingual benchmarks such as Chinese, Spanish, Japanese, German, and French per the new LMSYS chatbot arena [multilingual leaderboard](https://chat.lmsys.org/?leaderboard).

This model is for demonstration purposes and not for production usage.

## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to the [01.AI API Platform](https://platform.01.ai/).

## Terms of Use

By using Yi Model associated software, you are agreeing to the terms of use and the license under 01.AI's intellectual property or other rights owned by 01.AI, detailed [here](https://platform.01.ai/termsPage.html).

01.AI provides this and other large language models on NIM API Catalog for non-profit research purpose. Such large language models made available for trial (\"our models\") are still in the testing stage, and provided \"AS IS\" without any express or implicit warranty to users of NIM API Catalog. 01.AI does not assume any responsibility, nor warrant or guarantee, the models or any output or content therefrom in any and all aspects, including but not limited to the accuracy, completeness, legality, or suitability whatsoever.

Furthermore, 01.AI hereby expressly disavow any representation or warranty that our models are secure, error-free, uninterrupted, without interruptions, stable, or free from defects. Under no circumstances will our company be liable for any claims, damages, or losses arising from the trial of the Models or any output content, including direct, indirect, incidental, special, or punitive damages (such as loss of profits, loss of opportunities, costs paid to third parties, loss of reputation/goodwill, or damage), or any other liabilities, whether based on contract, warranty, tort, or any other theory of liability.

**Use Cases**

Seamlessly integrating with the OpenAI API, the Yi Model API offers compatibility with minimal code adjustments for a smooth transition.

-   **Knowledge Search and Query**

-   Yi-Large\'s extensive training corpus enables it to comprehend and process an array of diverse subjects, making it proficient in deciphering intricate queries.

-   A retrieval augmented generation process (Yi-Large-RAG) has been specifically engineered to enhance knowledge retrieval for this use case, boosting accuracy by 30%.

-   **Data Classification**

-   Yi-Large ensures precise data labeling with high consistency, minimizing the requirement for manual oversight.

-   **Chatbots**

-   Yi-Large\'s ability to generate human-like text makes it ideal for crafting chatbots capable of engaging in natural, fluid conversations with users.

-   Using system prompts, Yi-Large can customize responses based on user preferences and interactions, enhancing the chatbot\'s ability to personalize conversations.

-   **Customer Service**

-   Yi-Large accurately follows user instructions defining preferred reply formats and standards, in one use case increasing customer satisfaction by 50%.

-   Robust multilingual capabilities enable users to service customers all over the world.

**Model Release Date:** May 2024

**Model Type:** Large Language Model

Yi-Large is based on the decoder-only transformer architecture with several changes including pre-normalization, SwiGLU activation, RoPe for position embedding, and Group Query Attention (GQA).

## Input

-   Input Type: Text
-   Input Format: String
-   Message Type: System message, User message, Assistant message
-   Input Parameters: temperature, top_p, max_tokens, stream
-   Context length: 32k

## Output

-   Output Type: Text and Code
-   Output Format: String
-   Output Parameters: usage, finish_reason

## Training Dataset

Yi-Large has been trained from scratch using a multilingual tokenizer and multilingual data in pre-training including English, Chinese, Spanish, and Japanese, to name a few. Data quality was rigorously ensured throughout.

## Training Infrastructure Highlights

**Infrastructure Support**

01.AI's infrastructure supports full-stack development of the Yi model series, from pre-training to finetuning to serving. To support pre-training, it developed cross-cloud elastic task scheduling, automatic failure recovery, and topology-aware resource allocation. This allows it to run tasks according to the real-time availability of cross-cluster GPU nodes while incurring limited switching costs.

To support finetuning, 01.AI built a hierarchical scheduling framework that supports different distributed backends for different models (e.g., Megatron for the policy model and DeepSpeed for the reward model). For efficient inference, it uses 4-bit model and 8-bit KV cache quantization, combined with PagedAttention and Dynamic Batching.

**FP8 Training Paradigm**

The training framework developed by 01.AI is based on NVIDIA\'s Megatron-LM and is known as the Y training Framework. Its FP8 training is built upon NVIDIA's Transformer Engine. On this foundation, the 01.AI team has designed a training fault tolerance scheme. Due to the absence of a BF16 baseline to check if the loss reduction in FP8 training for a trillion-parameter model is normal, they simultaneously train with FP8 and BF16 at certain intervals and compare the loss diff and evaluation metrics between BF16 and FP8 to decide whether to correct FP8 training with BF16.

Since FP8 training requires the statistical information of a certain historical window to convert data from BF16 to FP8, the same logic for statistical quantization information must be supported during BF16 training within the Transformer Engine framework to ensure seamless switching from BF16 to FP8 training without introducing fluctuations in training performance. Throughout this process, 01.AI, leveraging NVIDIA's combined software and hardware technology stack, collaborated with NVIDIA's team to optimize the development, debugging, and performance aspects, completing the FP8 training and validation for large models. This resulted in a 1.3x performance improvement throughput relative to BF16 during training.

For inference, 01.AI developed the T-Inference Framework based on NVIDIA\'s TensorRT-LLM. This framework facilitates the conversion from Megatron to Hugging Face models and integrates features such as the Transformer Engine, supporting FP8 inference which significantly reduces the amount of video memory required for model execution and increases inference speed, making it easier for developers in the community to experience and develop. The specific process includes:

-   Integrating Transformer Engine layers into the Hugging Face model definition.

-   Developing a model converter to transform Megatron model weights into Hugging Face models.

-   Loading Hugging Face models with additional calibration data and benchmarking them with FP8 precision. This replaces BF16 tensors to save video memory usage and achieves a 2-to-5 times throughput improvement in bulk inference.

## Inference:
**Engine:** Tensor(RT)-LLM <br>
**Test Hardware:** NVIDIA H100

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
"model": "01-ai/yi-large",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```