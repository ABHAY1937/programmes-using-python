
# fs=444100
# second=int(input("enter the time duration in second:"))
# print("recording........\n")
# record_voice=sounddevice.rec(int(second*fs),samplerate=fs,
# sounddevice.wait()
# write("out.wav",fs,record_voice)
# print("finished.....\n please check it...")

fs=444100
second=int(input("enter the time duration in second:"))
print("recording........\n")
record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("out.wav",fs,record_voice)
print("finished.....\n please check it...")