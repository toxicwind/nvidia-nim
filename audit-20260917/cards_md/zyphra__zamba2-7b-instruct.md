---
title: "zamba2-7b-instruct"
publisher: "zyphra"
type: "endpoint"
updated: "2025-07-20T16:36:42.562Z"
description: "Efficient hybrid state-space model designed for conversational and reasoning tasks."
canonical: "https://build.nvidia.com/zyphra/zamba2-7b-instruct"
---

# Model Overview
## Description:
Zamba2-7B is a hybrid model composed of state-space (Mamba) and transformer blocks. It follows the Zamba architecture which consists of a Mamba backbone alternating with shared transformer blocks. Zamba2-7B possesses four major improvements over Zamba1:
1.) Mamba1 blocks have been replaced with Mamba2 blocks.
2.) We apply a LoRA projector to each shared MLP and attention block, which allows the network to specialize at each invocation of the shared transformer layer across depth. LoRA enables us to add depth-specialization for only a minimal increase in total parameter count.
3.) We utilize two alternating shared attention blocks.
4.) We utilize rotary position embeddings in the shared attention layer.
We found that while hybrid SSM-transformer models are perfectly capable of performing well without position embeddings, adding rotary embeddings to the shared attention block slightly improved performance. Secondly, we utilize two alternating shared attention blocks. We find that this improves performance slightly over a single shared block in terms of performance at fixed parameter budget.
Zamba2-7B uses the Mistral v0.1 tokenizer and was pre-trained on 3T tokens of text and code data sourced from open web-datasets, including Zyda. Subsequently, in a second phase, Zamba2-7B was annealed on a mixture of approximately 100B high-quality tokens.

This model is ready for commercial and non-commercial use.
## Third-Party Community Consideration
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see Zyphra's Huggingface [Zamba2-7B model](https://huggingface.co/Zyphra/Zamba2-7B) card.
### License/Terms of Use:
GOVERNING TERMS: The trial service is governed by the NVIDIA API Trial Terms of Service; and the use of this model is governed by the NVIDIA AI Foundation Models Community License Agreement. ADDITIONAL INFORMATION: Apache 2.0 License.
## References:
Zamba2-7b [model card](https://huggingface.co/Zyphra/Zamba2-7B) on Huggingface <br>
Zamba2-7b [blog post](https://www.zyphra.com/post/zamba2-7b) <br>
## Model Architecture:
**Architecture Type:** Hybrid SSM Transformer <br>
**Network Architecture:** Zamba2 <br>
## Input:
**Input Type(s):** Text <br>
**Input Format(s):** String <br>
**Input Parameters:** max_tokens, temperature, top_p <br>
**Other Properties Related to Input:** None <br>
## Output:
**Output Type(s):** Text <br>
**Output Format:** String <br>
**Output Parameters:** None <br>
**Other Properties Related to Output:** None <br>
**Supported Hardware Microarchitecture Compatibility:** <br>
NVIDIA Ampere <br>
NVIDIA Hopper <br>
**[Preferred/Supported] Operating System(s):** <br>
Linux <br>
## Model Version(s):
The instruction-tuned 7B Zamba2 model, Zamba2-7B-Instruct <br>
## Inference:
**Engine:** Triton <br>
**Test Hardware:** <br>
Hopper <br>
## Ethical Considerations And Limitations:
Zamba2-7B is a large language model trained on highly diverse internet corpora. As such, despite our best efforts, it has likely been exposed to and may potentially reproduce factually innacurate information, hate speech, profanity, sexually explicit content, and other harmful content. Additionally it may confabulate incorrect or non-factual answers to queries. As such, please treat the model's output with a warranted degree of caution. 
## Benchmarks
| Model           | Piqa (0) | Arc Easy (0) | Arc Challenge (25) | Boolq (0) | Winogrande (0) | Hellaswag (0) | Openbookqa (0) | MMLU 5 shot |
|-----------------|----------|--------------|--------------------|-----------|----------------|---------------|----------------|-------------|
| Zamba2-7B       | 83       | 81.9         | 68.09              | 86        | 76.9           | 81.2          | 47             | 67.2        |
| Mistral-7B-v0.1 | 82.26    | 79.59        | 61.43              | 83.64     | 73.88          | 81.07         | 44.2           | 62.2        |
| Gemma 7B        | 81.12    | 80.77        | 61.09              | 83.12     | 73.8           | 80.46         | 45.2           | 62.9        |
| Llama3.1-8B     | 81.2     | 81.6         | 57.85              | 82.1      | 73.6           | 78.9          | 44.6           | 65.2        |

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
"model": "zyphra/zamba2-7b-instruct",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```