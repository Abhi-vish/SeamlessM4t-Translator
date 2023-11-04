from gradio_client import Client

file = "f97baaa4ab58f6473077e6be12c1c92f453082cbbe1f69d1d5ea430d.wav"
client = Client("https://facebook-seamless-m4t.hf.space/--replicas/frq8b/")
result = client.predict(
		"S2ST (Speech to Speech translation)",	
		file,
		"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	
		"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	
		None,
		None,
		"Hindi",	
		api_name="/run"
        
)
print(result)