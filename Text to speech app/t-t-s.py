# ============================================
#   TEXT TO SPEECH APP
#   Mini Python Project
#   Library used: pyttsx3
#   Install: pip install pyttsx3
# ============================================

# pyttsx3 works OFFLINE (no internet needed!)
import pyttsx3

# -------------------------------------------------------
# FUNCTION: speak_text
# Purpose : Takes a string and speaks it out loud
# -------------------------------------------------------
def speak_text(text, rate=150, volume=1.0, voice_index=0):
    """
    text        - the string to speak
    rate        - speed of speech (words per minute), default 150
    volume      - volume from 0.0 (silent) to 1.0 (full), default 1.0
    voice_index - 0 for first available voice (usually male),
                  1 for second (usually female)
    """

    # Step 1: Initialize the TTS engine
    engine = pyttsx3.init()

    # Step 2: Set the speech RATE (speed)
    engine.setProperty('rate', rate)

    # Step 3: Set the VOLUME
    engine.setProperty('volume', volume)

    # Step 4: Set the VOICE
    voices = engine.getProperty('voices')  # get list of available voices

    # Safety check — make sure the index is valid
    if voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    else:
        print(f"Voice index {voice_index} not found. Using default voice.")

    # Step 5: Pass the text to the engine
    engine.say(text)

    # Step 6: Wait for the speech to finish, then stop the engine
    engine.runAndWait()


# -------------------------------------------------------
# FUNCTION: show_menu
# Purpose : Shows the options menu to the user
# -------------------------------------------------------
def show_menu():
    print("\n" + "=" * 40)
    print("       TEXT TO SPEECH APP 🔊")
    print("=" * 40)
    print("1. Speak a sentence")
    print("2. Change speech speed")
    print("3. Change volume")
    print("4. Change voice (Male / Female)")
    print("5. Exit")
    print("=" * 40)


# -------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------
def main():
    print("\nWelcome to the Text-to-Speech App!")
    print("Made with Python + pyttsx3 library")

    # Default settings
    speech_rate   = 150    # normal speed
    speech_volume = 1.0    # full volume
    voice_index   = 0      # first voice

    # Keep running until user chooses to exit
    while True:
        show_menu()

        choice = input("\nEnter your choice (1-5): ").strip()

        # --- Option 1: Speak text ---
        if choice == "1":
            user_text = input("Enter the text you want to speak:\n> ").strip()

            if user_text == "":
                print("⚠️  You didn't enter any text. Please try again.")
            else:
                print("🔊 Speaking...")
                speak_text(user_text, speech_rate, speech_volume, voice_index)
                print("✅ Done!")

        # --- Option 2: Change speed ---
        elif choice == "2":
            print("\nCurrent speed (rate):", speech_rate)
            print("Recommended range: 80 (slow) to 300 (fast), default is 150")
            try:
                new_rate = int(input("Enter new speed: "))
                if 50 <= new_rate <= 400:
                    speech_rate = new_rate
                    print(f"✅ Speed changed to {speech_rate}")
                else:
                    print("⚠️  Please enter a value between 50 and 400.")
            except ValueError:
                print("⚠️  Invalid input. Please enter a number.")

        # --- Option 3: Change volume ---
        elif choice == "3":
            print("\nCurrent volume:", speech_volume)
            print("Enter a value between 0.0 (mute) and 1.0 (max)")
            try:
                new_volume = float(input("Enter new volume: "))
                if 0.0 <= new_volume <= 1.0:
                    speech_volume = new_volume
                    print(f"✅ Volume changed to {speech_volume}")
                else:
                    print("⚠️  Please enter a value between 0.0 and 1.0.")
            except ValueError:
                print("⚠️  Invalid input. Please enter a decimal number like 0.5")

        # --- Option 4: Change voice ---
        elif choice == "4":
            print("\nAvailable Voices:")
            # Initialize engine just to list voices
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.stop()

            for i, voice in enumerate(voices):
                print(f"  [{i}] {voice.name}")

            try:
                new_voice = int(input("Enter voice number: "))
                if 0 <= new_voice < len(voices):
                    voice_index = new_voice
                    print(f"✅ Voice changed to index {voice_index}")
                else:
                    print("⚠️  Invalid voice number.")
            except ValueError:
                print("⚠️  Please enter a valid number.")

        # --- Option 5: Exit ---
        elif choice == "5":
            print("\n👋 Goodbye! Thanks for using the TTS App.\n")
            break

        else:
            print("⚠️  Invalid choice. Please enter a number from 1 to 5.")



