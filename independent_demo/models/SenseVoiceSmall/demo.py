from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

def sound_to_text(input_file):
    model_dir = "/home/luoqing/xiaozhi-esp32-server/main/xiaozhi-server/models/SenseVoiceSmall"
    model = AutoModel(
        model=model_dir,
        vad_model="fsmn-vad",
        vad_kwargs={"max_single_segment_time": 30000},
        # device="cuda:0",
        hub="hf",
    )

    # en
    res = model.generate(
        input=input_file,
        cache={},
        language="auto",  # "zn", "en", "yue", "ja", "ko", "nospeech"
        use_itn=True,
        batch_size_s=60,
        merge_vad=True,  #
        merge_length_s=15,
    )
    text = rich_transcription_postprocess(res[0]["text"])
    print(text)
    return text

sound_to_text("/home/luoqing/xiaozhi-esp32-server/main/xiaozhi-server/models/SenseVoiceSmall/example/en.mp3")
# model_dir = "./"


# model = AutoModel(
#     model=model_dir,
#     vad_model="fsmn-vad",
#     vad_kwargs={"max_single_segment_time": 30000},
#     # device="cuda:0",
#     hub="hf",
# )

# # en
# res = model.generate(
#     input=f"{model.model_path}/example/en.mp3",
#     cache={},
#     language="auto",  # "zn", "en", "yue", "ja", "ko", "nospeech"
#     use_itn=True,
#     batch_size_s=60,
#     merge_vad=True,  #
#     merge_length_s=15,
# )
# text = rich_transcription_postprocess(res[0]["text"])
# print(text)

