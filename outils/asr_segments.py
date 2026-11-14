import sherpa_onnx, soundfile as sf, json, re, subprocess
d='/home/claude/asr/sherpa-onnx-whisper-base/'
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d+'base-encoder.int8.onnx',decoder=d+'base-decoder.int8.onnx',tokens=d+'base-tokens.txt',language='fr',task='transcribe')
a,sr=sf.read('vo16.wav')
out=subprocess.run("ffmpeg -nostdin -i vo.mp3 -af silencedetect=noise=-35dB:d=0.25 -f null -",shell=True,capture_output=True,text=True).stderr
ss=[float(x) for x in re.findall(r"silence_start: ([\d.]+)",out)]; se=[float(x) for x in re.findall(r"silence_end: ([\d.]+)",out)]
segs=[(e,min([s for s in ss if s>e])) for e in se if any(s>e for s in ss)]
res=[]
for s,e in segs:
    st=rec.create_stream(); st.accept_waveform(sr,a[int(max(0,s-0.05)*sr):int((e+0.05)*sr)]); rec.decode_stream(st)
    print(f"{s:6.2f} {e:6.2f} {st.result.text}"); res.append((s,e,st.result.text))
json.dump(res,open('segs.json','w'),ensure_ascii=False)
