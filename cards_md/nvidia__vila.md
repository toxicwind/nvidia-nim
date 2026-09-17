---
title: "vila"
publisher: "nvidia"
type: "endpoint"
updated: "2025-04-25T18:45:34.460Z"
description: "Multi-modal vision-language model that understands text/img/video and creates informative responses"
canonical: "https://build.nvidia.com/nvidia/vila"
---

#  Vila Model Card

## Description

NVIDIA Vila is a leading vision language model (VLMs) that enables the ability to query and summarize images and video from the physical or virtual world. Vila is deployable in the data center, cloud and at the edge, including Jetson Orin and laptop by AWQ 4bit quantization through TinyChat framework. We find: (1) image-text pairs are not enough, interleaved image-text is essential; (2) unfreezing LLM during interleaved image-text pre-training enables in-context learning; (3)re-blending text-only instruction data is crucial to boost both VLM and text-only performance.

This model is ready for commercial use. It was trained on commercial images and videos for all three stages of training and supports single image and video inference. This version does not support interleaved and in-context learning capabilities.

## References

- [VILA technical paper](https://arxiv.org/abs/2312.07533)
- [VILA github repo](https://github.com/NVlabs/VILA)

## License

The license to use this model is covered by the Model EULA. By downloading the unpruned or pruned version of the model, you accept the terms and conditions of these [licenses](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/)

## Model Architecture

**Architecture Type:** Transformer-based Network Architecture

**Network Architecture**
- Vision Encoder: SigLIP-400M
- Language Encoder: Yi-34B

### Input

- **Input Type(s):** Image, Video, Text
- **Input Format(s):** Image (Red, Green, Blue (RGB)), Video (.mp4), and Text (String)
- **Input Parameters:** Image (2D), Video (3D), Text (1D)

### Output

- **Output Type(s):** Text
- **Output Formats:** String
- **Output Parameters:** 1D
- **Other Properties Related to Output:** N/A

## Software Integration
- **Runtime Engine(s):** TensorRT-LLM
- **Supported Hardware Architecture(s):** NVIDIA Hopper
- **Supported Operating System(s):** Linux

## Model Versions

- Cosmos-Nemotron-SigLIP-Yi-34B

## Training Dataset

NV-Pretraining and NV-CosmosNemotron-SFT data were used.

Additionally, the commercial subset of following datasets were used:

* [OASST1](https://huggingface.co/datasets/OpenAssistant/oasst1)
* [OASST2](https://huggingface.co/datasets/OpenAssistant/oasst2)
* [Localized Narratives](https://google.github.io/localized-narratives/)
* [TextCaps](https://textvqa.org/textcaps/dataset/)
* [TextVQA](https://textvqa.org/dataset/)
* [RefCOCO](https://github.com/lichengunc/refer)
* [VQAv2](https://visualqa.org/)
* [GQA](https://cs.stanford.edu/people/dorarad/gqa/index.html)
* [SynthDoG-en](https://huggingface.co/datasets/naver-clova-ix/synthdog-en)
* [A-OKVQ](https://github.com/allenai/aokvqa)
* [WIT](https://github.com/google-research-datasets/wit)
* [CLEVR](https://cs.stanford.edu/people/jcjohns/clevr/)
* [CLEVR-X](https://github.com/ExplainableML/CLEVR-X)
* [CLEVR-Math](https://huggingface.co/datasets/dali-does/clevr-math)
* [ScreenQA](https://github.com/google-research-datasets/screen_qa)
* [WikiSQL](https://github.com/salesforce/WikiSQL)
* [WikiTablQuestions](https://github.com/ppasupat/WikiTableQuestions/)
* [RenderedText](https://github.com/GbotHQ/ocr-dataset-rendering/)
* [FinQA](https://github.com/czyssrs/FinQA)
* [TAT-QA](https://nextplusplus.github.io/TAT-QA/)
* [Dolly](https://huggingface.co/datasets/databricks/databricks-dolly-15k)
* [Websight](https://huggingface.co/datasets/HuggingFaceM4/WebSight)
* [RAVEN](https://github.com/WellyZhang/RAVEN)
* [VizWiz](https://vizwiz.org/tasks-and-datasets/vqa/)
* [Inter-GPS](https://github.com/lupantech/InterGPS)
* [YouCook2](http://youcook2.eecs.umich.edu/)
* [ActivityNet Captions](https://cs.stanford.edu/people/ranjaykrishna/densevid/)
* [Video Localized Narratives](https://google.github.io/video-localized-narratives/)
* [CLEVRER](https://google.github.io/video-localized-narratives/)
* [Perception Test](https://github.com/google-deepmind/perception_test)
* [Next-QA](https://github.com/doc-doc/NExT-QA)
* [Kinetics-400](https://paperswithcode.com/dataset/kinetics)

**Data Collection Method by dataset:**
- Hybrid: Human, Automatic/Sensors

**Labeling Method by dataset:**
- Hybrid: Human, Automatic/Sensors

**Properties:** 
- NV-Pretraining data was collected from 5M subsampled NV-CLIP dataset. Stage 3 NV-SFT data has 2.8M images and 3.58M annotations on images that only have commercial license. Additionally, 355K videos with commercial license and 400K annotations on videos were used.

## Evaluation Data

**Data Collection Method by dataset:**
- Hybrid: Human, Automatic/Sensors

**Labeling Method by dataset:**
- Hybrid: Human, Automatic/Sensors

**Properties:** 
- A collection of different benchmarks, including academic VQA benchmarks and recent benchmarks specifically proposed for instruction-following LMMs.

* [VQAv2](https://visualqa.org/)
* [GQA](https://cs.stanford.edu/people/dorarad/gqa/about.html)
* [ScienceQA Image](https://scienceqa.github.io/)
* [Text VQA](https://textvqa.org/)
* [POPE](https://github.com/AoiDragon/POPE)
* [MME](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models)
* [SEED-Bench](https://github.com/AILab-CVC/SEED-Bench)
* [MMMU](https://mmmu-benchmark.github.io/)
* [Video MME](https://video-mme.github.io/home_page.html)
* [Egoschema](https://egoschema.github.io/)
* [Perception Test](https://github.com/google-deepmind/perception_test)

### Methodology and KPI

|Benchmark|VQAv2|GQA   |SQA Image|Text VQA|POPE (Popular)|MME    |SEED |SEED Image|MMMU val (beam 5)|SEED Video|VideoMME w/o Sub @32f|VideoMME w/ Sub @32f|Egoschema (val)|Perception Test|
|---------|-----|------|---------|--------|--------------|-------|-----|----------|-----------------|----------|---------------------|--------------------|---------------|---------------|
|Accuracy |81.70|62.13 |79.62    |71.14   |85.61         |1649.62|70.36|74.12     |47.33            |58.21     |57.85                |60.67               |63.8           |61.76          |

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

For more detailed information on ethical considerations for this model, please see the Model Card++ Promise and the Explainability, Bias, Safety & Security, and Privacy Subcards.

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

## Bias

| Field | Response |
| -- | -- |
|Participation considerations from adversely impacted groups [(protected classes)](https://www.senate.ca.gov/content/protected-classes) in model design and testing: | None of the Above |
| Measures taken to mitigate against unwanted bias: | No measures taken to mitigate against unwanted bias.|

## Explainability

| Field | Response |
| -- | -- |
| Intended Application(s) & Domain(s): | Visual Question Answering. |
| Model Type: | Vision Language Model |
| Intended Users: | The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intelligence. |
| Output: | Text |
| Describe how the model works: | Chat based on image content |
| Technical Limitations: | Vila may not perform well on domain specific images. |
| Known Risk: | The Model may produce output that is biased, toxic, or a hallucination. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The Model may also generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text, producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. |
| Verified to have met prescribed NVIDIA standards: | Yes |
| Performance Metrics: | Visual Question Answering (VQA) , GQA, MME, MMMU, SQA-Image, etc.  |
| Potential Known Risks: |  None Known |
| Licensing: | [NVIDIA AI Foundation Models Community License](https://docs.nvidia.com/ai-foundation-models-community-license.pdf) |

## Privacy

| Field | Response |
| -- | -- |
| Generatable or reverse engineerable personally-identifiable information (PII)? | None |
| Protected classes used to create this model? | Not Applicable |
| Was consent obtained for any personal data used? | Not Applicable |
| How often is dataset reviewed? | 	Before Release |
| Is a mechanism in place to honor data subject right of access or deletion of personal data? | Not Applicable |
| If personal data collected for the development of the model, was it collected directly by NVIDIA? | Not Applicable |
| If personal data collected for the development of the model by NVIDIA, do you maintain or have access to disclosures made to data subjects?	| Not Applicable |
| If personal data collected for the development of this AI model, was it minimized to only what was required? | Not Applicable |
| Is there provenance for all datasets used in training? | Yes |
| Does data labeling (annotation, metadata) comply with privacy laws? | Yes |
| Is data compliant with data subject requests for data correction or removal, if such a request was made? | Yes, for data collected by NVIDIA.  No, for all externally-sourced data. |
| Applicable NVIDIA Privacy Policy	| [https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/) |

## Safety & Security

| Field | Response |
| -- | -- |
| Model Application(s): | Visual Question Answering and Conversation. Agent to understand and answer the scene. |
| Describe the life-critical application (if present). | None: Not within Operational Design Domain |
| Use Case Restrictions: | Abide by [https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/"](https://www.nvidia.com/en-us/data-center/products/nvidia-ai-enterprise/eula/). |
| Describe access restrictions (if any): | The Principle of least privilege (PoLP) is applied limiting access for dataset generation and model development. Restrictions enforce dataset access during training, and dataset license constraints adhered to. |

## Prototype

```python
import requests

invoke_url = "https://ai.api.nvidia.com/v1/vlm/nvidia/vila"

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
import fs from 'fs';
import axios from 'axios';
import path from 'path';

const invokeUrl = "https://ai.api.nvidia.com/v1/vlm/nvidia/vila";
const stream = ;
const query = 'Describe the scene';

const kNvcfAssetUrl = 'https://api.nvcf.nvidia.com/v2/nvcf/assets';

// Retrieve the API Key from environment variables
const kApiKey = process.env.TEST_NVCF_API_KEY;
if (!kApiKey) {
console.error("Generate API_KEY and export TEST_NVCF_API_KEY=xxxx");
process.exit(1);
}

const kSupportedList = {
"png": ["image/png", "img"],
"jpg": ["image/jpg", "img"],
"jpeg": ["image/jpeg", "img"],
"mp4": ["video/mp4", "video"]
};

// Get file extension
function getExtension(filename) {
const ext = path.extname(filename).toLowerCase();
return ext.slice(1); // remove the leading dot
}

// Get MIME type
function mimeType(ext) {
return kSupportedList[ext][0];
}

// Get media type
function mediaType(ext) {
return kSupportedList[ext][1];
}

// Upload asset
async function uploadAsset(mediaFile, description) {
const ext = getExtension(mediaFile);
if (!(ext in kSupportedList)) {
throw new Error(`Unsupported file extension: ${ext}`);
}

const dataInput = fs.readFileSync(mediaFile); // Sync file read

const headers = {
"Authorization": `Bearer ${kApiKey}`,
"Content-Type": "application/json",
"Accept": "application/json"
};

const postData = {
contentType: mimeType(ext),
description: description
};

// First API call to authorize asset upload
const { data: authorizeRes } = await axios.post(kNvcfAssetUrl, postData, { headers });
console.log(`uploadUrl: ${authorizeRes.uploadUrl}`);

// Second API call to upload the file
const response = await axios.put(authorizeRes.uploadUrl, dataInput, {
headers: {
"x-amz-meta-nvcf-asset-description": description,
"content-type": mimeType(ext)
}
});

if (response.status === 200) {
console.log(`upload asset_id ${authorizeRes.assetId} successfully!`);
//return uuidParse(authorizeRes.assetId);
return authorizeRes.assetId.toString()
} else {
console.log(`upload asset_id ${authorizeRes.assetId} failed.`);
throw new Error(`Asset upload failed: ${authorizeRes.assetId}`);
}
}

// Delete asset
async function deleteAsset(assetId) {
const headers = {
"Authorization": `Bearer ${kApiKey}`
};
const url = `${kNvcfAssetUrl}/${assetId}`;
await axios.delete(url, { headers });
}

// Chat with media NVCF
async function chatWithMediaNvcf(inferUrl, mediaFiles, query, stream = false) {
const assetList = [];
const extList = [];
let mediaContent = "";
let hasVideo = false;

for (const mediaFile of mediaFiles) {
const ext = getExtension(mediaFile);
if (!(ext in kSupportedList)) {
throw new Error(`${mediaFile} format is not supported`);
}

if (mediaType(ext) === "video") {
hasVideo = true;
}

console.log(`uploading file: ${mediaFile}`);
const assetId = await uploadAsset(mediaFile, "Reference media file");
console.log(`assetId: ${assetId}`);
assetList.push(assetId);
extList.push(ext);
mediaContent += `<${mediaType(ext)} src="data:${mimeType(ext)};asset_id,${assetId}" />`;
}

if (hasVideo && mediaFiles.length !== 1) {
throw new Error("Only a single video is supported.");
}

const assetSeq = assetList.join(',');
console.log(`received asset_id list: ${assetSeq}`);

const headers = {
"Authorization": `Bearer ${kApiKey}`,
"Content-Type": "application/json",
"NVCF-INPUT-ASSET-REFERENCES": assetSeq,
"NVCF-FUNCTION-ASSET-IDS": assetSeq,
"Accept": "application/json"
};

if (stream) {
headers["Accept"] = "text/event-stream";
}

const messages = [{
"role": "user",
"content": `${query} ${mediaContent}`
}];

const payload = {
max_tokens: 1024,
temperature: 0.2,
top_p: 0.7,
seed: 50,
num_frames_per_inference: 8,
messages: messages,
stream: stream,
model: "nvidia/vila"
};

// Post to the inference API
//let response = await axios.post(inferUrl, payload, { headers });
const response = await axios.post(inferUrl, payload, {
headers: headers,
responseType: stream ? 'stream' : 'json'
});

if (stream) {
response.data.on('data', (line) => {
console.log(line.toString());
});
} else {
console.log(JSON.stringify(response.data));
}

// Clean up uploaded assets
console.log(`deleting assets: ${assetList}`);
for (const assetId of assetList) {
await deleteAsset(assetId);
}
}

// Main function to run the script
async function main() {
const args = process.argv.slice(2);
if (args.length <= 0) {
console.log("Usage: export TEST_NVCF_API_KEY=xxx");
console.log(`python ${process.argv[0]} sample1.png sample2.png ... sample16.png`);
console.log(`python ${process.argv[0]} sample.mp4`);
process.exit(1);
}

const mediaSamples = args;
await chatWithMediaNvcf(invokeUrl, mediaSamples, query, stream);
}

main();
```

```bash
#!/bin/bash
stream=
# Check if TEST_NVCF_API_KEY is set
if [ -z "$TEST_NVCF_API_KEY" ]; then
echo "Generate API_KEY and export TEST_NVCF_API_KEY=xxxx"
exit 1
fi

invoke_url="https://ai.api.nvidia.com/v1/vlm/nvidia/vila"
kNvcfAssetUrl="https://api.nvcf.nvidia.com/v2/nvcf/assets"
query="Describe the scene"

# supported table
kSupportedList=("png:image/png,img" "jpg:image/jpg,img" "jpeg:image/jpeg,img" "mp4:video/mp4,video")

# get "mime,media"
get_media_info() {
local ext="$1"
for item in "${kSupportedList[@]}"; do
if [[ "$item" == "$ext:"* ]]; then
# Return "mime,media"
echo "${item#*:}"
return
fi
done
echo ""
}

get_extension() {
filename="$1"
echo "${filename##*.}" | tr '[:upper:]' '[:lower:]'
}

upload_asset() {
media_file="$1"
description="$2"
ext=$(get_extension "$media_file")

media_info=$(get_media_info "$ext")
if [ -z "$media_info" ]; then
echo "$media_file format is not supported"
exit 1
fi

mime_type="${media_info%%,*}"
media_type="${media_info#*,}"

# Get upload URL
response=$(curl -s -X POST "$kNvcfAssetUrl" \
-H "Authorization: Bearer $TEST_NVCF_API_KEY" \
-H "Content-Type: application/json" \
-H "accept: application/json" \
-d "{\"contentType\": \"$mime_type\", \"description\": \"$description\"}")

upload_url=$(echo "$response" | jq -r '.uploadUrl')
asset_id=$(echo "$response" | jq -r '.assetId')

# Upload the asset file to the URL
curl -s -X PUT "$upload_url" \
-H "x-amz-meta-nvcf-asset-description: $description" \
-H "content-type: $mime_type" \
--data-binary "@$media_file"

echo "$asset_id"
}

delete_asset() {
asset_id="$1"
curl -s -X DELETE "$kNvcfAssetUrl/$asset_id" \
-H "Authorization: Bearer $TEST_NVCF_API_KEY"
}

chat_with_media_nvcf() {
infer_url="$1"
query="$2"
shift 2
media_files=("$@")

asset_list=()
media_content=""

has_video=false

for media_file in "${media_files[@]}"; do
ext=$(get_extension "$media_file")

media_info=$(get_media_info "$ext")
if [ -z "$media_info" ]; then
echo "$media_file format is not supported"
exit 1
fi
mime_type="${media_info%%,*}"
media_type="${media_info#*,}"

if [[ "$mime_type" == "video" ]]; then
has_video=true
fi

echo "uploading media_file: $media_file"
asset_id=$(upload_asset "$media_file" "Reference media file")
asset_list+=("$asset_id")
media_content+="<$media_type src=\"data:$mime_type;asset_id,$asset_id\" />"
done

if $has_video && [ "${#media_files[@]}" -gt 1 ]; then
echo "Only single video supported."
exit 1
fi

asset_seq=$(IFS=,; echo "${asset_list[*]}")

headers=(
-H "Authorization: Bearer $TEST_NVCF_API_KEY"
-H "Content-Type: application/json"
-H "NVCF-INPUT-ASSET-REFERENCES: $asset_seq"
-H "NVCF-FUNCTION-ASSET-IDS: $asset_seq"
)
if [ "$stream" = true ]; then
headers+=(-H "Accept: text/event-stream")
else
headers+=(-H "Accept: application/json")
fi

payload=$(jq -n --arg query "$query" --arg media_content "$media_content" --argjson stream "$stream" '{
max_tokens: 1024,
temperature: 0.2,
top_p: 0.7,
seed: 50,
num_frames_per_inference: 8,
messages: [{"role": "user", "content": "\($query) \($media_content)"}],
stream: $stream,
model: "nvidia/vila"
}')

response=$(curl -s -X POST "$infer_url" "${headers[@]}" -d "$payload")

if [ "$stream" = true ]; then
echo "$response" | while IFS= read -r line; do
echo "$line"
done
else
echo "$response" | jq .
fi

# Cleanup uploaded assets
for asset_id in "${asset_list[@]}"; do
echo "deleting asset $asset_id"
delete_asset "$asset_id"
done
}

if [ "$#" -le 0 ]; then
echo "Usage: export TEST_NVCF_API_KEY=xxx"
echo "       $0 sample1.png sample2.png ... sample16.png"
echo "       $0 sample.mp4"
exit 1
fi

chat_with_media_nvcf "$invoke_url" "$query" "$@"
```