# Verifie la langue parlee : transcrit sans forcer la langue (detection auto) par fenetres de 8 s.
# Usage : python3 check_langue.py video.mp4 [duree_max]
import sherpa_onnx, soundfile as sf, subprocess, sys, tempfile, os
d='/home/claude/asr/sherpa-onnx-whisper-base/'
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=d+'base-encoder.int8.onnx',decoder=d+'base-decoder.int8.onnx',tokens=d+'base-tokens.txt',language='',task='transcribe')
f=sys.argv[1]; T=float(sys.argv[2]) if len(sys.argv)>2 else 60
w=os.path.join(tempfile.mkdtemp(),'a.wav')
subprocess.run(['ffmpeg','-v','error','-y','-t',str(T),'-i',f,'-vn','-ar','16000','-ac','1',w],check=True)
a,sr=sf.read(w)
for i in range(0,len(a),8*sr):
    st=rec.create_stream(); st.accept_waveform(sr,a[i:i+8*sr]); rec.decode_stream(st)
    r=st.result; print(f"{i/sr:5.0f}s [{getattr(r,'lang','?')}] {r.text}")
