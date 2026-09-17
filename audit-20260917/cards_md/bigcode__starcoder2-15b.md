---
title: "starcoder2-15b"
publisher: "bigcode"
type: "endpoint"
updated: "2025-07-20T16:36:21.523Z"
description: "Advanced programming model for code completion, summarization, and generation"
canonical: "https://build.nvidia.com/bigcode/starcoder2-15b"
---

# StarCoder2 Model Overview

## Description:

StarCoder2-15B is a state-of-the-art language model with 15 billion parameters, trained on over 600 programming languages using The Stack v2 dataset. It employs advanced techniques like Grouped Query Attention and sliding window attention to enhance its performance on coding tasks. The model is optimized to handle a context window of 16,384 tokens and was trained using the Fill-in-the-Middle objective on 4+ trillion tokens. Trained with NVIDIA's NeMo™ Framework on the NVIDIA Eos Supercomputer, it represents a significant advancement in code generation and understanding.

## Terms of Use

GOVERNING TERMS: Your use of this model is governed by the [BigCode OpenRAIL-M v1 License Agreement](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement).

## References(s):

[StarCoder2-15B on Hugging Face](https://huggingface.co/bigcode/starcoder2-15b)

## Model Architecture:

**Architecture Type:** Transformer decoder <br>
**Network Architecture:** Grouped Query Attention, sliding window attention <br>
**Model Version:** 2.0 <br>

## Input:

**Input Format:** Text <br>
**Input Parameters:** Temperature, Top P, Max Output Tokens <br>

## Output:

**Output Format:** Text <br>
**Output Parameters:** None <br>

## Software Integration:

**Supported Hardware Platform(s):** NVIDIA H100 GPUs <br>
**Supported Operating System(s):** Linux <br>

# Inference:

**Engine:** Triton Inference Server <br>
**Test Hardware:** NVIDIA DGX H100 systems <br>

## Prototype

```python
from openai import OpenAI

client = OpenAI(
base_url = "https://integrate.api.nvidia.com/v1",
api_key = "$NVIDIA_API_KEY"
)

completion = client.completions.create(
model="",
prompt="",
temperature=,
top_p=,
max_tokens=,
stream=NaN
)

print(completion.choices[0].text)
```

```javascript
import OpenAI from 'openai';

const openai = new OpenAI({
apiKey: '$NVIDIA_API_KEY',
baseURL: 'https://integrate.api.nvidia.com/v1',
})

async function main() {
const completion = await openai.completions.create({
model: "",
prompt: "",
temperature: ,
top_p: ,
max_tokens: ,
stream: ,
})

process.stdout.write(completion.choices[0]?.text);

}

main();
```

```bash
invoke_url='https://integrate.api.nvidia.com/v1/completions'

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