from utils.voice import speech_to_text

print("🎤 Testing Microphone...")

text = speech_to_text()

print("\nYou said:")
print(text)