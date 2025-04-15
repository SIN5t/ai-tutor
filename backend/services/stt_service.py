import asyncio
import logging
import zhconv


from backend.config import STT_CONFIG
from faster_whisper import WhisperModel

model = WhisperModel(STT_CONFIG["whisper_model"])

# 全局变量来跟踪转录状态
should_stop = False
# 添加一个变量来跟踪当前转录的文件路径
current_file = None


# faster-whisper 模型，将视频转换为文字
async def transcribe_audio(file_path: str) -> list:
    global should_stop, current_file
    should_stop = False
    current_file = file_path

    try:
        segments_generator = model.transcribe(file_path, beam_size=STT_CONFIG["beam_size"],
                                              language=STT_CONFIG["language"], vad_filter=STT_CONFIG["vad_filter"])

        transcription = []
        segments, info = segments_generator

        for segment in segments:
            if should_stop:
                current_file = None
                raise asyncio.CancelledError("Transcription cancelled")
            
            # 转换为简体
            simplified_text = zhconv.convert(segment.text, 'zh-cn')  # 转为简体

            transcription.append({
                "start": segment.start,
                "end": segment.end,
                "text": simplified_text
            })

            await asyncio.sleep(0)

        current_file = None
        return transcription

    except asyncio.CancelledError as e:
        should_stop = True
        current_file = None
        logging.error(f"Transcription was cancelled: {str(e)}", exc_info=True)  # exc_info=True 会打印堆栈信息
        raise
    except Exception as e:
        should_stop = True
        current_file = None
        logging.error(f"An error occurred during transcription: {str(e)}", exc_info=True)  # exc_info=True 会打印堆栈信息
        raise
    finally:
        should_stop = False
        current_file = None


def stop_transcription():
    global should_stop
    should_stop = True


def is_file_being_transcribed(file_path: str) -> bool:
    """检查指定文件是否正在被转录"""
    return current_file == file_path
