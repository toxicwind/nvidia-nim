---
title: "palmyra-med-70b"
publisher: "writer"
type: "endpoint"
updated: "2025-05-22T00:17:45.789Z"
description: "Leading LLM for accurate, contextually relevant responses in the medical domain."
canonical: "https://build.nvidia.com/writer/palmyra-med-70b"
---

# **Model Overview**

**Model Developer:** Writer  
**Model Release Date:** June 10th, 2024

## **Description:**

Palmyra-Med is a model built by Writer specifically to meet the needs of the healthcare industry. The leading LLM on biomedical benchmarks, with an average score of 85.87%, outperforming base models in the industry and a medically trained human test-taker. NVIDIA has optimized this model using TRT-LLM with 2 H100s.

This model is ready for non-commercial use.

## **Third-Party Community Consideration**

This model is not owned or developed by NVIDIA. This model has been developed and built to a third-party’s requirements for this application and use case; see link to Writer's [Model Card](https://huggingface.co/Writer/Palmyra-Med-70B).

## **License, Acceptable Use, and Research Privacy Policy**

The trial service is governed by the NVIDIA API Trial Terms of Service (found at [https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)[)](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf)); and the use of this model is governed by the [Writer Open Model License](https://writer.com/legal/open-model-license/).

#### **Specialized for Biomedical Applications**

Palmyra-Med-70B is meticulously designed to meet the unique linguistic and knowledge demands of the medical and life sciences sectors. It has been fine-tuned on an extensive collection of high-quality biomedical data, ensuring it can comprehend and generate text with precise domain-specific accuracy and fluency.

## **Intended Use**

**Intended Use Cases** Palmyra-Med-70b is intended for non-commercial and research use in English. Instruction tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

**Out-of-scope** Use in any manner that violates applicable laws or regulations (including trade compliance laws). Use in any other way that is prohibited by the Acceptable Use Policy and Writer Open source License. Use in languages other than English\*\*.

\*\*Developers may fine-tune Palmyra-Med-70b models for languages beyond English provided they comply with the Writer Open source License and the Acceptable Use Policy.

## **Medical Use Cases**

Palmyra-Med-70b excels in analyzing and summarizing complex clinical notes, EHR data, and discharge summaries, extracting key information to generate concise, structured summaries. It can answer a wide range of medical questions and perform advanced clinical entity recognition, identifying key medical concepts such as diseases, symptoms, medications, procedures, and anatomical structures from unstructured text.

By leveraging its deep understanding of medical terminology, the model enhances information retrieval, data analysis, and knowledge discovery from EHRs, research articles, and other biomedical sources. These capabilities support applications like clinical decision support, pharmacovigilance, and medical research.

## **Bias, Risks, and Limitations**

Palmyra-Med-70b, despite leveraging high-quality data, may contain inaccuracies, biases, or misalignments and has not been rigorously evaluated in clinical trials or real-world healthcare settings. It is advised not to use the model for direct patient care, clinical decision support, or professional medical purposes. Palmyra-Med-70b should not replace professional medical judgment, and adapting it for medical use would require extensive additional work, including thorough testing, guideline alignment, bias mitigation, human oversight, and regulatory compliance. Always consult a qualified healthcare provider for personal medical needs.

**Model Architecture**

* Architecture Type: Transformer  
* Network Architecture: Llama  
* Finetuned from model: Palmyra-X-004
* Model Version: 0.1

**Input**

* Input Type: Text  
* Input Format: String  
* Input Parameters: max\_tokens, temperature, top\_p, stop, frequency\_penalty, presence\_penalty, seed

**Output**

* Output Type: Text  
* Output Format: String

## **Software Integration:**

* Supported Hardware Platform(s): NVIDIA Hopper  
* \[Preferred/Supported\] Operating System(s): Linux

## **Inference**

**Engine:** TensorRT-LLM  
**Test Hardware:** H100

## **Evaluation Results**

Palmyra-Med-70b achieves state-of-the-art results with an average score of 85.9% despite having fewer parameters than typical language models. Its strong performance in tasks like Clinical Knowledge Graph (KG), Medical Genetics, and PubMedQA underscores its effective grasp of biomedical knowledge. More information can be found here: [https://huggingface.co/Writer/Palmyra-Med-70B](https://huggingface.co/Writer/Palmyra-Med-70B) 

## **Ethical Considerations:**

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

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
"model": "writer/palmyra-med-70b",
"messages": [{"role":"user","content":""}],
"temperature": ,   
"top_p": ,
"max_tokens": ,
"stream":                 
}'
```