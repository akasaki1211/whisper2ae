import os
import json
import time
import argparse

import whisper

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(CURRENT_DIR, 'outputs')
MODEL_DIR = os.path.join(CURRENT_DIR, 'models')

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--path",
        type=str,
        default=''
    )
    parser.add_argument(
        "--model",
        type=str,
        default='base'
    )
    parser.add_argument(
        "--language",
        type=str,
        default=None
    )
    parser.add_argument(
        "--savejson",
        type=bool,
        default=False
    )

    opt = parser.parse_args()

    if not opt.path:
        return
    
    # load model
    model = whisper.load_model(opt.model, download_root=MODEL_DIR)
    print('device : {}'.format(model.device))

    # transcribe
    st = time.time()
    if opt.language:
        result = model.transcribe(opt.path, verbose=True, language=opt.language)
    else:
        result = model.transcribe(opt.path, verbose=True)

    t = whisper.utils.format_timestamp(time.time()-st, always_include_hours=True)
    print('transcribe time : ' + t)

    # save
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    output_name = os.path.splitext(os.path.basename(opt.path))[0] + '_' + opt.model

    # save TXT to AE
    datalist = []
    for seg in result['segments']:
        datalist.append('{}\t{}\t{}\n'.format(seg['start'], seg['end'], seg['text']))

    with open(os.path.join(OUTPUT_DIR, output_name + '.txt'), 'w', encoding='utf-8') as f:
        f.writelines(datalist)

    # save JSON
    if opt.savejson:
        with open(os.path.join(OUTPUT_DIR, output_name + '.json'), 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

main()