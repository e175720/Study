# 必要なライブラリ
import math
import numpy as np

# ピンクノイズの関数定義
def synth_pinknoise(duration=1.0, samprate=44100):
    """
    Generate pinknoise using Voss algorithm
    http://www.firstpr.com.au/dsp/pink-noise/
    """
    f_low = 10   # lowest frequency to keep pink (Hz)
    levels = math.ceil(np.log2(samprate/f_low))
    t = np.arange(start=0, stop=duration, step=1/samprate)
    out = np.zeros(len(t))
    x = np.random.normal(size=levels)
    for n in range(math.ceil(samprate * duration)):
        for m in range(levels):
            if n % 2**(m+1) == 0:
                x[m] = np.random.normal()
            out[n] = np.random.normal() + np.sum(x)
    return(out / max(abs(out)), t)


# 使い方（戻り値は、x：ピンクノイズ信号、t：各サンプルの時刻）
x, t = synth_pinknoise(duration=60.0, samprate=48000)

# WAVファイルに書き出し
import soundfile as sf
sf.write("pinknoise.wav", x, 48000, subtype='PCM_24')