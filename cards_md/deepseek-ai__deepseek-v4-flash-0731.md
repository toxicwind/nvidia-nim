---
title: "deepseek-v4-flash-0731"
publisher: "deepseek-ai"
type: "endpoint"
updated: "2026-08-19T01:03:08.022Z"
description: "284B MoE (13B active) model ideal for long-context workloads optimized for coding, chat, and agentic workflows"
canonical: "https://build.nvidia.com/deepseek-ai/deepseek-v4-flash-0731"
---

# DeepSeek-V4-Flash-0731

## Description
DeepSeek-V4-Flash-0731 is a 304B-parameter sparse Mixture-of-Experts language model for text generation, coding, reasoning, long-context, and agentic workflows. It supports a one-million-token context and includes an attached speculative decoding module.

This model is ready for commercial or non-commercial use.

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [DeepSeek-V4-Flash-0731 Model Card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731).

## License and Terms of Use:
GOVERNING TERMS: This trial service is governed by the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). Use of this model is governed by the [NVIDIA Open Model Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-agreement/). Additional Information: [MIT](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash/blob/main/LICENSE).

## Deployment Geography:
Global

## Use Case:
**Use Case:** Text generation, coding, reasoning, long-context, and agentic tool-use workflows.

## Release Date:
**NGC:** 08/13/2026 via [link](https://catalog.ngc.nvidia.com/orgs/nim/deepseek-ai/models/deepseek-v4-flash-0731)<br>
**Build.NVIDIA.com:** 08/17/2026 via [link](https://build.nvidia.com/deepseek-ai/deepseek-v4-flash-0731)<br>
**Hugging Face:** 07/30/2026 via [link](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)

## Reference(s):
**References:**
- [DeepSeek-V4-Flash-0731 Model Page](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)
- [DeepSeek-V4 Technical Report](https://arxiv.org/abs/2606.19348)

## Model Architecture:
**Architecture Type:** Transformer
**Network Architecture:** Sparse Mixture of Experts with hybrid Compressed Sparse Attention and Heavily Compressed Attention, Manifold-Constrained Hyper-Connections, and an attached speculative decoding module
**Total Parameters:** 304B
**Active Parameters:** 13B

### Input:
**Input Types:** Text
**Input Formats:** String
**Input Parameters:** One Dimensional (1D)
**Other Input Properties:** Supports multi-turn messages encoded in OpenAI-compatible format and low, high, and max reasoning-effort levels.
**Input Context Length (ISL):** 1 million tokens
### Output:
**Output Types:** Text
**Output Format:** String
**Output Parameters:** One Dimensional (1D)
**Other Output Properties:** Supports text completions and reasoning content.

__Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA's hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.__

## Software Integration:
**Runtime Engines:**
- **SGLang**
- **vLLM**

**Supported Hardware:**
- **NVIDIA Blackwell:** NVIDIA B200 Tensor Core GPU, NVIDIA RTX PRO 6000D
- **NVIDIA Hopper:** NVIDIA H100 Tensor Core GPU, NVIDIA H200 Tensor Core GPU, NVIDIA H20 Tensor Core GPU

**Operating System:** Linux

__The integration of foundation and fine-tuned models into AI systems requires additional testing using use-case-specific data to ensure safe and effective deployment. Following the V-model methodology, iterative testing and validation at both unit and system levels are essential to mitigate risks, meet technical and functional requirements, and ensure compliance with safety and ethical standards before deployment.__

## Model Version(s)
DeepSeek-V4-Flash-0731

## Training, Testing, and Evaluation Datasets:

### Training Dataset
**Data Modality:** Text
**Text Training Data Size:** [More than 10 Trillion Tokens]
**Data Collection Method by dataset:** Undisclosed
**Labeling Method by dataset:** Undisclosed
**Properties:** The DeepSeek-V4 family was pretrained on more than 32 trillion diverse tokens and then post-trained for reasoning and agentic capabilities.

### Testing Dataset
**Data Collection Method by dataset:** Undisclosed
**Labeling Method by dataset:** Undisclosed
**Properties:** Undisclosed

### Evaluation Dataset
**Evaluation Benchmark Score:** DeepSeek-V4-Flash-0731 reports 82.7 on Terminal Bench 2.1, 76.7 on Cybergym, 70.3 on Toolathlon-Verified, 68.7 on DSBench-FullStack, and 59.6 on DSBench-Hard.

<details>
<summary><strong>Detailed Benchmark Comparison Table</strong></summary>

| Benchmark | DeepSeek-V4-Flash-0731 | DeepSeek-V4-Flash (Preview) | DeepSeek-V4-Pro (Preview) | GLM-5.2 | Opus-4.8 |
|---|---:|---:|---:|---:|---:|
| Terminal Bench 2.1 | 82.7 | 61.8 | 72.1 | 81.0 | 85.0 |
| NL2Repo | 54.2 | 39.4 | 38.5 | 48.9 | 69.7 |
| Cybergym | 76.7 | 38.7 | 52.7 | - | 83.1 |
| DeepSWE | 54.4 | 7.3 | 12.8 | 46.2 | 58.0 |
| Toolathlon-Verified | 70.3 | 49.7 | 55.9 | 59.9 | 76.2 |
| Agents' Last Exam | 25.2 | 15.8 | 16.5 | 23.8 | 25.7 |
| AutomationBench Public | 25.1 | 10.8 | 12.8 | 12.9 | 27.2 |
| DSBench-FullStack † | 68.7 | 37.0 | 41.8 | 61.8 | 71.6 |
| DSBench-Hard † | 59.6 | 25.8 | 31.1 | 54.5 | 71.7 |

**Evaluation Methodology Notes:**

1. For the Code Agent tasks among the public benchmarks above, DeepSeek-V4-Flash-0731 is evaluated with the minimal mode of DeepSeek Harness (to be released) as the agent framework, using the `max` reasoning effort level with `temperature = 1.0, top_p = 0.95`.
2. † DSBench-FullStack is an internal full-stack development test set; DSBench-Hard is an internal test set of difficult coding-agent problems.

</details>

**Data Collection Method by dataset:** [Hybrid: Automated, Manually-Collected]
**Labeling Method by dataset:** [Hybrid: Automated, Manually-Labeled]
**Properties:** Evaluated on coding-agent, repository, cybersecurity, software-engineering, and tool-use benchmarks.

## Inference
**Acceleration Engine:** vLLM
**Test Hardware:** NVIDIA Hopper (H100)

## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment.

Please report model quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Specifications

- **Context Length:** 1,048,576 tokens
- **Parameters:** 284,000,000,000
- **Input:** Text
- **Output:** Text

## Capabilities

- **Function Calling:** Supported
- **Structured Output:** Supported
- **Reasoning:** Supported

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
extra_body={"chat_template_kwargs":{"thinking":True,"reasoning_effort":"high"}},
stream=NaN
)

reasoning = getattr(completion.choices[0].message, "reasoning", None) or getattr(completion.choices[0].message, "reasoning_content", None)
if reasoning:
print(reasoning)
print(completion.choices[0].message.content)
```

```python
from langchain_nvidia_ai_endpoints import ChatNVIDIA

client = ChatNVIDIA(
model="",
api_key="$NVIDIA_API_KEY",
temperature=,
top_p=,
max_tokens=,
extra_body={"chat_template_kwargs":{"thinking":True,"reasoning_effort":"high"}},
)

response = client.invoke([{"role":"user","content":""}])
reasoning = response.additional_kwargs.get("reasoning") or response.additional_kwargs.get("reasoning_content") if response.additional_kwargs else None
if reasoning:
print(reasoning)
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
chat_template_kwargs: {"thinking":true,"reasoning_effort":"high"},
stream: 
})

const reasoning = completion.choices[0]?.message?.reasoning || completion.choices[0]?.message?.reasoning_content;
if (reasoning) process.stdout.write(reasoning + "\n");
process.stdout.write(completion.choices[0]?.message?.content || '');

}

main();
```

```bash
invoke_url='https://integrate.api.nvidia.com/v1/chat/completions'

payload=$(cat <<'JSON'
{
"model": "",
"messages": [{"role":"user","content":""}],
"temperature": ,
"top_p": ,
"max_tokens": ,
"chat_template_kwargs": {"thinking":true,"reasoning_effort":"high"},
"stream": 
}
JSON
)

curl -sS \
--request POST \
--url "$invoke_url" \
--header "Authorization: Bearer $NVIDIA_API_KEY" \
--header "Content-Type: application/json" \
--data "$payload"
```