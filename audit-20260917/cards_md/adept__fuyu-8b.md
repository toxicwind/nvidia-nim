---
title: "fuyu-8b"
publisher: "adept"
type: "endpoint"
updated: "2024-08-26T16:47:11.225Z"
description: "Multi-modal model for a wide range of tasks, including image understanding and language generation."
canonical: "https://build.nvidia.com/adept/fuyu-8b"
---

# Model Overview

## Description:

Fuyu-8B is a multi-modal transformer introduced by Adept AI. It can perform a wide range of tasks, 
including image understanding, text generation, and code generation.
Architecturally, Fuyu is a vanilla decoder-only transformer - there is no image encoder. 
Image patches are instead linearly projected into the first layer of the transformer, bypassing the embedding lookup. 
The transformer decoder is simply treated like an image transformer (albeit with no pooling and causal attention).

## Terms of use

By accessing this model, you are agreeing to the Fuyu-8b terms and conditions of the [CC BY-NC license](https://creativecommons.org/licenses/by-nc/4.0/deed.en).

## Third-Party Community Consideration:
This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see [Fuyu's Hugging Face Model Card](https://huggingface.co/adept/fuyu-8b).

## References(s):

* [Fuyu-8B Blog Post](https://www.adept.ai/blog/fuyu-8b) by adept.ai <br>
* [Fuyu-8B Model Card](https://huggingface.co/adept/fuyu-8b) on Hugging Face <br>

## Model Architecture: 
**Architecture Type:** Transformer <br>
**Network Architecture:** Fuyu-8b <br>
**Model Version:** N/A <br>

## Input:
**Input Format:**  Red, Green, Blue (RGB) Image + Text <br>
**Input Parameters:** None <br>

## Output:
**Output Format:** Text <br>
**Output Parameters:** None <br>

## Software Integration:
**Supported Hardware Platform(s):** Hopper, Ampere/Turing <br>
**Supported Operating System(s):** Linux <br>

# Inference:
**Engine:** [Triton](https://developer.nvidia.com/triton-inference-server) <br>
**Test Hardware:** Other <br>

## Specifications

- **Context Length:** 16,384 tokens
- **Parameters:** 9,408,238,592
- **Input:** Text, Image
- **Output:** Text

## Capabilities

- **Function Calling:** Not supported
- **Structured Output:** Not supported
- **Reasoning:** Not supported

## Prototype

```python
import requests

invoke_url = "https://ai.api.nvidia.com/v1/vlm/adept/fuyu-8b"

headers = {
"Authorization": "Bearer ",
"Accept": "application/json",
}

payload = {
"messages": [
{
"role": "user",
"content": ""
}
]
}

# re-use connections
session = requests.Session()

response = session.post(invoke_url, headers=headers, json=payload)

response.raise_for_status()
response_body = response.json()
print(response_body)
```

```javascript
import fetch from "node-fetch";

const invokeUrl = "https://ai.api.nvidia.com/v1/vlm/adept/fuyu-8b"

const headers = {
"Authorization": "Bearer ",
"Accept": "application/json",
}

const payload = {
"messages": [
{
"role": "user",
"content": ""
}
]
}

let response = await fetch(invokeUrl, {
method: "post",
body: JSON.stringify(payload),
headers: { "Content-Type": "application/json", ...headers }
});

let response_body = await response.json()

console.log(JSON.stringify(response_body))
```

```bash
invoke_url='https://ai.api.nvidia.com/v1/vlm/adept/fuyu-8b'

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