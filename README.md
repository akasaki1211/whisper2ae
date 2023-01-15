# Whisper to AE
Transcribe from a video with audio using [OpenAI Whisper](https://github.com/openai/whisper) and turn the result into a Text Layers in AfterEffects. Text Layers are split into segments. 

## Setup
1. Create a venv (optional)  
2. Install whisper  
```commandline
cd whisper2ae
python -m venv whisper
.\whisper\Scripts\activate

pip install git+https://github.com/openai/whisper.git 
```

## 1. Transcribe for AE
The following command will download the models into the `models` folder and begin transcription. The result `txt` file will be created in the `outputs` folder.  

Minimum command :  
```commandline
python whisper_transcribe.py --path .\sources\input.mp4
```

with options :  
```commandline
python whisper_transcribe.py --path .\sources\input.mp4 --model large --language ja --savejson 1
```

## 2. Load to AE
Run [txt2aeLayer.jsx](./txt2aeLayer.jsx) in AfterEffects and select the result `txt`. If a Text Layer is selected, it will be created by duplication.  
