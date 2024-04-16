import snowboydecoder

def hotword_detected_callback():
    print("Hotword detected!")

# Replace "your_hotword_model.pmdl" with the path to your hotword model file
model = "your_hotword_model.pmdl"

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print("Listening... Press Ctrl+C to exit")

# This function will continuously listen for the hotword
detector.start(detected_callback=hotword_detected_callback,
               interrupt_check=lambda: False,
               sleep_time=0.03)
