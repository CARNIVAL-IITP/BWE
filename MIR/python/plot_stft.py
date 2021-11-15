import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec


# ## Window filepath
# input_original_path = '/home/utahboy3502/1007MIR/MIR/'
# input_unmasked_path = '/home/utahboy3502/1007MIR/MIR/output/'
# input_masked_path = '/home/utahboy3502/1007MIR/MIR/output/masked/'

# wav_original_name = 'test1.wav'
# unmasked_wav_name = 'unmasked_output.wav'
# masked_wav_name = 'kf99_output.wav'

# outputpath = '/home/utahboy3502/1007MIR/MIR/output/'

## Linux filepath
input_original_path = '/home/donghyun/Project/IITP/MIR/sample_audio_input/'
input_unmasked_path = '/home/donghyun/Project/IITP/MIR/output/1013/masked/'
input_masked_path = '/home/donghyun/Project/IITP/MIR/output/1013/masked/'

wav_original_name = 'set200002_clncut.wav'
unmasked_wav_name = 'output_kf99_sitec_1000.wav' 
masked_wav_name = 'output_dental_sitec_1000.wav'

outputpath = '/home/utahboy3502/Progress/Project/IITP/MIR/output/1013/'

sr = 16000
hop_length = 64
n_fft = 1024

wav_original = input_original_path + wav_original_name
wav_unmasked = input_unmasked_path + unmasked_wav_name
wav_masked = input_masked_path + masked_wav_name


## plot 3 waveform and spectrogram each
def stft1():
    fig = plt.figure(figsize=(12, 6))

    ##original
    s1_w = fig.add_subplot(2, 3, 1)
    y, sr = librosa.load(wav_original, sr=16000)
    librosa.display.waveplot(y, sr=sr)
    plt.title('Original')

    s1 = fig.add_subplot(2, 3, 4)
    stft = librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    print("Wave length: {}, Mel_S shape:{}".format(len(y) / sr, np.shape(stft)))

    ##unmasked
    s2_w = fig.add_subplot(2, 3, 2)
    y, sr = librosa.load(wav_unmasked, sr=16000)
    librosa.display.waveplot(y, sr=sr)
    plt.title('Unmasked')

    s2 = fig.add_subplot(2, 3, 5)
    stft = librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    print("Wave length: {}, Mel_S shape:{}".format(len(y) / sr, np.shape(stft)))

    ##masked
    s3_w = fig.add_subplot(2, 3, 3)
    y, sr = librosa.load(wav_masked, sr=16000)
    librosa.display.waveplot(y, sr=sr)
    plt.title('Masked')

    s3 = fig.add_subplot(2, 3, 6)
    stft = librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    print("Wave length: {}, Mel_S shape:{}".format(len(y) / sr, np.shape(stft)))

    plt.tight_layout()
    # plt.savefig(outputpath + 'output_stft_plot_.png')
    plt.show()

## plot waveform top, 3 spectrogram bottom
def stft2():
    fig = plt.figure(constrained_layout = True)

    gs = gridspec.GridSpec(2, 3, figure = fig)
    ax = fig.add_subplot(gs[0, :])
    y, sr = librosa.load(wav_original, sr=16000)
    librosa.display.waveplot(y, sr=sr)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Original Waveform')

    ax2 = fig.add_subplot(gs[1,0])
    y, sr = librosa.load(wav_original, sr=16000)
    stft = librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Original Spectrogram')

    ax3 = fig.add_subplot(gs[1,1])
    y, sr = librosa.load(wav_unmasked, sr=16000)
    stft = librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('KF-99 Mask Spectrogram')

    ax4 = fig.add_subplot(gs[1,2])
    y, sr = librosa.load(wav_masked, sr=16000)
    stft = librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Dental Mask Spectrogram')

    # plt.savefig('dental_fabric_stft.jpg')
    plt.show()

def stft3():
    fig = plt.figure(figsize=(12, 6))

    s1_w = fig.add_subplot(1, 3, 1)
    
    ref, sr = librosa.load(wav_original, sr=16000)
    stft = librosa.stft(y=ref, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Origianl Spectrogram')
    
    s2_w = fig.add_subplot(1, 3, 2)
   
    y, sr = librosa.load(wav_unmasked, sr=sr)
    stft = librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Fabric Mask Spectrogram')
    
    s3_w = fig.add_subplot(1, 3, 3)
    
    deg, sr = librosa.load(wav_masked, sr=16000)
    stft = librosa.stft(y=deg, n_fft=n_fft, hop_length=hop_length)
    magnitude = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(magnitude, ref=np.max)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='linear')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('KF-AD Mask Spectrogram')

    # score = pesq(ref, deg, sr)
    # print("PESQ Score is: ", score)

    # plt.colorbar(format='%+2.0f dB');
    plt.tight_layout()
    #plt.savefig('mel-spectrogram.png')
    plt.show()
    # plt.savefig('Mel-Spectrogram.png', dpi = 200)
    
    #waveplot
    #librosa.display.waveplot(y, sr=sr)

# stft1()
stft2()
# stft3()
