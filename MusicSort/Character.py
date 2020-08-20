import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

#ファイル読み込み
filename = 'Records/So_Obvious_R2.wav'

#y=オーディオ時系列、sr=目標サンプリングレート、offset=設定時間後に読み取り開始(秒単位)
#duration=入力されたオーディオを読み込む長さ(秒単位)
y, sr = librosa.load(filename, sr=4410, offset=0.0, duration=60.0)

#波形表示
librosa.display.waveplot(y=y, sr=sr)
plt.savefig('Pictures2/So_Obvious_1_2.png')

# n_mels=生成するメルバンドの数
n_mels=128
# hop_length=連続するフレームのサンプル数
hop_length=2068
# n_fft=窓関数の長さ(範囲)
n_fft=2048
# 各引数をメルフィルタに渡す
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, hop_length=hop_length, n_fft=n_fft)

#パワースペクトルをdB単位に変換する
log_S = librosa.power_to_db(S, ref=np.max)
print(log_S.shape)

#プロット
plt.figure(figsize=(12, 4))
librosa.display.specshow(data=log_S, sr=sr, hop_length=hop_length, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel spectrogram')
plt.tight_layout()
plt.savefig('Pictures2/So_Obvious_01_2.png')
