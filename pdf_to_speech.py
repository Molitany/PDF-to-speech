from TTS.api import TTS
import re
import fitz
from argparse import ArgumentParser

def get_pdf_text(args):
    tts_text = ""
    with fitz.open(args.path) as doc:
        for page in doc:
            block = page.get_text("blocks")[1:]
            for x0, y0, x1, y1, text, block_no, block_type in block:
                if block_type == 0:
                    text = text.replace("\n", " ")
                    text = re.sub(r"([a-zA-Z])- ?([a-zA-Z])", r"\1\2", text)
                    tts_text += f"{text}\n"
    return tts_text.encode().decode()


def pdf_to_wav(text: str, args):
    model = "tts_models/en/vctk/vits"
    speaker = "p335"
    tts = TTS(model)
    path = args.path
    filename = re.search(r"(.*?)\.pdf$", path)[1]
    tts.tts_to_file(text,
        speaker=speaker, file_path=f"{filename}.wav", emotion="Happy")


if __name__ == "__main__":
    parser = ArgumentParser(prog="ArticleToSpeech")
    parser.add_argument("path", type=str)
    args = parser.parse_args()
    
    text = get_pdf_text(args)
    pdf_to_wav(text, args)
