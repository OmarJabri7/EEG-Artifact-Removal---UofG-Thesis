import numpy as np
import os
import scipy.signal as sig
from scipy.signal import butter, lfilter, filtfilt
import pandas as pd
import matplotlib.pyplot as plt
import scipy

NOISE_SRC = ["blink", "eyescrunching", "flow",
             "readingsitting", "sudoku",
             "templerun", "wordsearch", "jaw", "turninghead", "lie_relax",
             "raisingeyebrows", "readinglieing"]


class EEG_GEN():

    def __init__(self) -> None:
        self.alphas = {}
        self.deltas = {}
        self.noises = {}
        self.fs = 1000.0

    def folders_in(self, path_to_parent):
        for fname in os.path.listdir(path_to_parent):
            if os.path.isdir(os.path.join(path_to_parent, fname)):
                yield os.path.join(path_to_parent, fname)

    def load_data(self, dir, eeg_subj, noise_source):
        if("+" in noise_source):
            noises = noise_source.split("+")
            artefact = 0
            noise_lengths = []
            for noise in noises:
                noise_lengths.append(
                    self.get_noise_length(str(eeg_subj), noise))
            self.get_min_samples(noise_lengths)
            for noise in noises:
                if(self.folders_in(dir)):
                    self.artefact = np.loadtxt(
                        f"{dir}/subj{eeg_subj}/{noise}/emgeeg.dat")
                    artefact += self.artefact[:self.samples, 2]
                    if(eeg_subj in self.noises):
                        if(noise_source in self.noises[eeg_subj]):
                            self.noises[eeg_subj][noise_source] = artefact
                        else:
                            self.noises[eeg_subj][noise_source] = {}
                            self.noises[eeg_subj][noise_source] = artefact
                    else:
                        self.noises[eeg_subj] = {}
                        self.noises[eeg_subj][noise_source] = {}
                        self.noises[eeg_subj][noise_source] = artefact
                else:
                    self.artefact = np.loadtxt(
                        f"{dir}/subj{eeg_subj}/{noise_source}.dat")
                    self.artefact = self.artefact
        else:
            if(self.folders_in(dir)):
                self.artefact = np.loadtxt(
                    f"{dir}/subj{eeg_subj}/{noise_source}/emgeeg.dat")
                if(eeg_subj in self.noises):
                    if(noise_source in self.noises[eeg_subj]):
                        self.noises[eeg_subj][noise_source] = self.artefact[:, 2]
                    else:
                        self.noises[eeg_subj][noise_source] = {}
                        self.noises[eeg_subj][noise_source] = self.artefact[:, 2]
                else:
                    self.noises[eeg_subj] = {}
                    self.noises[eeg_subj][noise_source] = {}
                    self.noises[eeg_subj][noise_source] = self.artefact[:, 2]
            else:
                self.artefact = np.loadtxt(
                    f"{dir}/subj{eeg_subj}/{noise_source}.dat")
                self.artefact = self.artefact

    def get_sampling_rate(self, dir, eeg_subj, noise_source):
        if(self.folders_in(dir)):
            self.artefact = np.loadtxt(
                f"{dir}/subj{eeg_subj}/{noise_source}/emgeeg.dat")
            ts = self.artefact[:, 0]
            self.fs = 1/(ts[1] - ts[0])
        else:
            self.artefact = np.loadtxt(
                f"{dir}/subj{eeg_subj}/{noise_source}.dat")
            ts = self.artefact[:, 0]
            self.fs = 1/(ts[1] - ts[0])

    def get_min_samples(self, noise_samples):
        self.samples = min(noise_samples)

    def butter_bandpass(self, signal, lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        y = lfilter(b, a, signal)
        return y

    def butter_bandstop(self, signal, lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='bandstop')
        y = lfilter(b, a, signal)
        return y

    def butter_lowpass(self, signal, cutoff, fs, order=5):
        nyq = 0.5*fs
        normal_cutoff = cutoff/nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        y = filtfilt(b, a, signal)
        return y

    def butter_highpass(self, signal, cutoff, fs, order=5):
        nyq = 0.5*fs
        normal_cutoff = cutoff/nyq
        b, a = butter(order, normal_cutoff, btype='high', analog=False)
        y = filtfilt(b, a, signal)
        return y

    def gen_sine_alpha(self, A, f, freqs, fs=1000, bandpass=False, sum_sines=False, optimal=False) -> None:
        x = np.arange(self.samples)
        self.fs = fs
        self.alpha = A * np.sin(2 * np.pi * f * x / fs)
        if(sum_sines):
            self.alpha += 2 * np.sin(2 * np.pi * freqs[0] * x / fs)
            self.alpha += 0.1 * np.sin(2 * np.pi * freqs[1] * x / fs)
            self.alpha += 0.3 * np.sin(2 * np.pi * freqs[3] * x / fs)
            self.alpha += 0.01 * np.sin(2 * np.pi * freqs[4] * x / fs)
        if(bandpass):
            self.alpha = self.butter_bandpass(
                self.alpha, freqs[0] - 1, freqs[4] + 1, self.fs, 2)
        if(optimal):
            pass

    def gen_sine_delta(self, A, f, freqs, fs=1000, bandpass=False, sum_sines=False, optimal=False) -> None:
        x = np.arange(self.samples)
        self.fs = fs
        self.delta = A * np.sin(2 * np.pi * f * x / fs)
        if(sum_sines):
            self.delta += 2 * np.sin(2 * np.pi * freqs[0] * x / fs)
            self.delta += 0.1 * np.sin(2 * np.pi * freqs[1] * x / fs)
            self.delta += 0.3 * np.sin(2 * np.pi * freqs[3] * x / fs)
            self.delta += 0.01 * np.sin(2 * np.pi * freqs[4] * x / fs)
        if(bandpass):
            self.delta = self.butter_bandpass(
                self.delta, freqs[0] - 1, freqs[4] + 1, self.fs, 2)
        if(optimal):
            pass

    def set_noise(self, eeg_subj, noise_source, noise_new):
        self.noises[eeg_subj][noise_source] = noise_new

    def gen_eeg_alpha(self, eeg_subj, noise_source) -> None:
        if(eeg_subj in self.alphas):
            if(noise_source in self.alphas[eeg_subj]):
                tmp_noise = self.noises[eeg_subj][noise_source]
                self.alphas[eeg_subj][noise_source] = self.alpha + \
                    tmp_noise[:self.samples]
            else:
                self.alphas[eeg_subj][noise_source] = {}
                tmp_noise = self.noises[eeg_subj][noise_source]
                self.alphas[eeg_subj][noise_source] = self.alpha + \
                    tmp_noise[:self.samples]
        else:
            self.alphas[eeg_subj] = {}
            self.alphas[eeg_subj][noise_source] = {}
            tmp_noise = self.noises[eeg_subj][noise_source]
            self.alphas[eeg_subj][noise_source] = self.alpha + \
                tmp_noise[:self.samples]

    def gen_eeg_delta(self, eeg_subj, noise_source) -> None:
        if(eeg_subj in self.deltas):
            if(noise_source in self.deltas[eeg_subj]):
                tmp_noise = self.noises[eeg_subj][noise_source]
                self.deltas[eeg_subj][noise_source] = self.delta + \
                    tmp_noise[:self.samples]
            else:
                self.deltas[eeg_subj][noise_source] = {}
                tmp_noise = self.noises[eeg_subj][noise_source]
                self.deltas[eeg_subj][noise_source] = self.delta + \
                    tmp_noise[:self.samples]
        else:
            self.deltas[eeg_subj] = {}
            self.deltas[eeg_subj][noise_source] = {}
            tmp_noise = self.noises[eeg_subj][noise_source]
            self.deltas[eeg_subj][noise_source] = self.delta + \
                tmp_noise[:self.samples]

    def gen_alpha_optimal(self, eeg_subj, noise_source):
        self.alpha_data = np.loadtxt(
            f"{dir}/subj{eeg_subj}/{noise_source}/emgeeg.dat")
        self.alpha_eeg = self.alpha_data[:, 1]
        self.t = self.alpha_data[:, 0]
        self.fit_sin(self.t, self.alpha_eeg)

    def gen_delta_optimal():
        pass

    def fit_sin(self, tt, yy):
        '''Fit sin to the input time sequence, and return fitting parameters "amp", "omega", "phase", "offset", "freq", "period" and "fitfunc"'''
        tt = np.array(tt)
        yy = np.array(yy)
        # assume uniform spacing
        ff = np.fft.fftfreq(len(tt), (tt[1]-tt[0]))
        Fyy = abs(np.fft.fft(yy))
        # excluding the zero frequency "peak", which is related to offset
        guess_freq = abs(ff[np.argmax(Fyy[1:])+1])
        guess_amp = np.std(yy) * 2.**0.5
        guess_offset = np.mean(yy)
        guess = np.array(
            [guess_amp, 2.*np.pi*guess_freq, 0., guess_offset])

        def sinfunc(t, A, w, p, c): return A * np.sin(w*t + p) + c

        popt, pcov = scipy.optimize.curve_fit(
            sinfunc, tt, yy, p0=guess, maxfev=5000)
        A, w, p, c = popt
        f = w/(2.*np.pi)
        def fitfunc(t): return A * np.sin(w*t + p) + c
        opt_res = {"amp": A, "omega": w, "phase": p, "offset": c, "freq": f, "period": 1. /
                   f, "fitfunc": fitfunc, "maxcov": np.max(pcov), "rawres": (guess, popt, pcov)}
        self.optimal_alpha = opt_res["amp"] * np.sin(
            2 * np.pi * opt_res["omega"] * self.t + opt_res["phase"]) + opt_res["offset"]

    def gen_gain(self, signal) -> float:
        signal = np.abs(signal)
        str_signal = str(signal)
        str_signal = str_signal.split(".")
        digits = str_signal[0]
        n = len(digits)
        return 1/(10**(n - 1))

    def save_data(self, eeg_data, noise_data, subj, sig_type):
        sig_fake = np.column_stack((eeg_data, noise_data[:self.samples]))
        signal_df = pd.DataFrame(sig_fake)
        signal_df.to_csv(
            f"deepNeuronalFilter/SubjectData/{sig_type}/EEG_Subject{subj}.tsv", index=True, header=False, sep="\t")
        print(f"{sig_type} Signals Saved!")

    def save_xls(self, list_dfs, xls_path, sheet_names):
        with pd.ExcelWriter(xls_path) as writer:
            i = 0
            for df in (list_dfs):
                df.to_excel(writer, f"{sheet_names[i]}", index=False)
                i += 1
            writer.save()

    def get_eeg_alpha(self, eeg_subj, noise_source) -> np.array:
        return self.alphas[eeg_subj][noise_source]

    def get_eeg_delta(self, eeg_subj, noise_source) -> np.array:
        return self.deltas[eeg_subj][noise_source]

    def get_noise(self, eeg_subj, noise_source) -> np.array:
        if(noise_source == "all"):
            return self.noises[eeg_subj]
        return self.noises[eeg_subj][noise_source]

    def get_pure_alpha(self) -> np.array:
        return self.alpha

    def get_pure_delta(self) -> np.array:
        return self.delta

    def get_noise_length(self, eeg_subj, noise_source):
        return len(self.noises[eeg_subj][noise_source])

    def calc_SNR(self, signal, noise, sig_type, snr_fct, calc=0) -> float:
        N = len(signal)
        if(sig_type == 0):
            start = 8
            end = 12
        elif(sig_type == 1):
            start = 1
            end = 5
        if(snr_fct == 0):
            noise_pow = 1/N * (np.sum(noise**2))
            sig_pow = 1/N * (np.sum(signal**2))
        elif(snr_fct == 1):
            sig_fft = np.abs(np.fft.fft(signal)[
                0: np.int(N / 2)])
            noise_fft = np.abs(np.fft.fft(noise)[
                0: np.int(N / 2)])
            sig_fft[0] = 0
            noise_pow = (np.sum(noise_fft[start:end]))
            sig_pow = (np.sum(sig_fft[start:end]))
        elif(snr_fct == 2):
            sig_fft = np.abs(np.fft.fft(signal)[
                0: np.int(N / 2)])
            noise_fft = np.abs(np.fft.fft(noise)[
                0: np.int(N / 2)])
            sig_fft[0] = 0
            noise_pow = (np.sum(noise_fft[start:end]**2))
            sig_pow = (np.sum(sig_fft[start:end]**2))
        if(calc == 0):
            return np.abs(sig_pow - noise_pow)/noise_pow
        elif(calc == 1):
            return sig_pow/noise_pow

    def plot_psd(self, signal):
        freqs, psd = sig.welch(signal)
        plt.semilogx(freqs, psd)
        plt.title('PSD: power spectral density')
        plt.xlabel('Frequency')
        plt.ylabel('Power')
        plt.figure()

    def plot_spectrogram(self, signal):
        freqs, times, spectrogram = sig.spectrogram(signal)
        plt.plot(freqs, spectrogram)
        plt.title('Spectrogram')
        plt.ylabel('Frequency band')
        plt.xlabel('Time window')
        plt.figure()

    def plot_freq_resp(self, signal, Fs, title):
        fourierTransform = np.fft.fft(signal)/len(signal)
        fourierTransform = fourierTransform[range(int(len(signal)/2))]
        tpCount = len(signal)
        values = np.arange(int(tpCount/2))
        timePeriod = tpCount/Fs
        frequencies = values/timePeriod
        plt.plot(frequencies, abs(fourierTransform))
        plt.title(title)
        # plt.xlim(0, 200)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude (V)')
        plt.savefig(f"Results-Generation/Frequency_{title}")
        fig = plt.figure()
        return fig

    def plot_freq_resp(self, signal, Fs, title):
        fourierTransform = np.fft.fft(signal)/len(signal)
        fourierTransform = fourierTransform[range(int(len(signal)/2))]
        tpCount = len(signal)
        values = np.arange(int(tpCount/2))
        timePeriod = tpCount/Fs
        frequencies = values/timePeriod
        plt.plot(frequencies, abs(fourierTransform))
        plt.title(title)
        # plt.xlim(0, 200)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude (V)')
        plt.savefig(f"Results-Generation/Frequency_{title}")
        fig = plt.figure()
        return fig

    def plot_freq_resp_vs(self, signal, target, Fs, title, signal1, signal2):
        fourierTransform = np.fft.fft(signal)/len(signal)
        fourierTransform = fourierTransform[range(int(len(signal)/2))]
        tpCount = len(signal)
        values = np.arange(int(tpCount/2))
        timePeriod = tpCount/Fs
        frequencies = values/timePeriod
        fourierTransform2 = np.fft.fft(target)/len(target)
        fourierTransform2 = fourierTransform2[range(int(len(target)/2))]
        tpCount2 = len(target)
        values2 = np.arange(int(tpCount2/2))
        timePeriod2 = tpCount2/Fs
        frequencies2 = values2/timePeriod2
        plt.plot(frequencies, abs(fourierTransform))
        plt.plot(frequencies2, abs(fourierTransform2))
        plt.title(title)
        # plt.xlim(0, 200)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude (microV)')
        plt.legend([f"{signal1}", f"{signal2}"])
        plt.savefig(f"Results-Generation/Frequency_Diff_{title}")
        fig = plt.figure()
        return fig

    def plot_welch(self, signal, Fs, title):
        win = Fs
        freqs, psd = sig.welch(signal, Fs)
        plt.plot(freqs, psd, lw=2)
        plt.title(title)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power spectral density (V^2 / Hz)')
        fig = plt.figure()
        return fig

    def plot_welch_vs(self, signal, target, Fs, title, signal1, signal2):
        win = 4*Fs
        freqs1, psd1 = sig.welch(signal, Fs)
        freqs2, psd2 = sig.welch(target, Fs)
        plt.plot(freqs1, psd1, lw=2)
        plt.plot(freqs2, psd2, lw=2)
        plt.title(title)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power spectral density (V^2 / Hz)')
        plt.legend([f"{signal1}", f"{signal2}"])
        fig = plt.figure()
        return fig

    def plot_time_series(self, signal, title):
        plt.plot(signal)
        plt.title(title)
        plt.ylabel("Signal Voltage (microV)")
        plt.xlabel("Time (s)")
        # plt.ylim(-7, 7)
        plt.savefig(f"Results-Generation/Temporal_{title}")
        fig = plt.figure()
        return fig

    def plot_all(self, eeg, noise):
        eeg_time = self.plot_time_series(eeg, "Noisy Time Spectrum")
        noise_time = self.plot_time_series(noise, "Noise Time Spectrum")
        eeg_fr = self.plot_freq_resp(eeg, self.fs, "Noisy Frequency Spectrum")
        noise_fr = self.plot_freq_resp(
            noise, self.fs, "Noise Frequency Spectrum")
        plt.show()