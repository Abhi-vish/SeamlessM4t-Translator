from gradio_client import Client
import json
import base64

class Translate:
    
    def translate(self, task=None, audio=None, text=None, input_language=None, target_language=None):
        client = Client("https://facebook-seamless-m4t.hf.space/")
        
        audio_content = None  # Initialize to None
        result = None  # Initialize result
        
        if audio is not None:
            # Handle the uploaded audio file
            audio_content = audio.read()  # Read the binary content of the uploaded audio
            audio.close()  # Close the uploaded file
            # Convert audio content to base64-encoded string
            audio_content = base64.b64encode(audio_content).decode('utf-8')
        
            # Call the Gradio predict method and store the result
            result = client.predict(
                task,
                audio_content,  # Pass the audio content as base64-encoded string
                "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
                "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
                text,
                input_language,
                target_language,
                api_name="/run"
            )
        else:
            result = client.predict(
                task,
                audio_content,  # Pass the audio content as base64-encoded string
                "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
                "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
                text,
                input_language,
                target_language,
                api_name="/run"
            )

        

        # Serialize the dictionary to a JSON-serializable string
        result_str = json.dumps(result)
        
        return result_str
