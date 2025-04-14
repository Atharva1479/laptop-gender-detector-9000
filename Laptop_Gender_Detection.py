import platform
import hashlib
import pyttsx3  # For text-to-speech

def laptop_gender_check():
    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()
    
    print("🔍 WELCOME TO THE HIGHLY SCIENTIFIC LAPTOP GENDER DETECTOR 3000™ 🔍")
    print("Loading quantum gender analysis algorithms...")
    
    # Add dramatic effect
    for _ in range(3):
        print(".", end="", flush=True)
        import time
        time.sleep(0.7)
    print("\n")
    
    # Get STABLE system details for our "analysis"
    computer_name = platform.node()
    os_type = platform.system()
    processor = platform.processor()
    machine_type = platform.machine()
    
    # Create a stable identifier based on hardware info that won't change
    system_info = f"{computer_name}{os_type}{processor}{machine_type}"
    
    # Create a hash of the system info to get a consistent result
    # This will ensure the same laptop always gets the same gender
    hash_object = hashlib.md5(system_info.encode())
    hash_hex = hash_object.hexdigest()
    
    # Use the first byte of the hash to determine gender
    # If the first two hex digits (one byte) are even, it's female; if odd, it's male
    first_byte = int(hash_hex[:2], 16)
    is_female = first_byte % 2 == 0
    
    # Ridiculous "gender traits" lists
    male_traits = [
        "Refuses to ask for directions even when clearly lost in file directories",
        "Makes unnecessarily loud fan noises to assert dominance",
        "Battery dies at the worst possible moment",
        "Mysteriously accumulates crumbs under the keyboard",
        "Updates itself at the most inconvenient times"
    ]
    
    female_traits = [
        "Multitasks efficiently with 57 browser tabs open",
        "Runs cool under pressure",
        "Remembers all your passwords (but won't tell you what they are)",
        "Screen brightness adjusts perfectly to the room",
        "Subtly judges your search history"
    ]
    
    # Funny voice lines for each gender
    male_voice_lines = [
        "I am definitely a manly laptop! I LOVE YOU, BRO!",
        "It's a boy! And I've been waiting to tell you how awesome you are!",
        "Dude! We've been together for so long, and I never told you I love you...awkward!",
        "I'm your digital wingman! Let's go get some...uh...new software?",
        "Hey boss! I've got your back, and your front, and all your files!"
    ]
    
    female_voice_lines = [
        "Well, I'm female, and honestly I've seen your browser history. We need to talk.",
        "It's a girl! And I think we both know I've been organizing your life for years.",
        "I love you! Even though you never clean my keyboard properly!",
        "I'm the queen of your digital kingdom! Bow before my processing power!",
        "We've been together through thick and thin, mostly because I can't move on my own."
    ]
    
    # Dramatic reveal
    print("✨ ANALYSIS COMPLETE! ✨")
    print("According to our extremely accurate quantum algorithms...\n")
    
    time.sleep(1)  # Dramatic pause
    
    # Get available voices
    voices = speaker.getProperty('voices')
    male_voice = None
    female_voice = None
    
    # Find male and female voices
    for voice in voices:
        if "male" in voice.name.lower() or "david" in voice.name.lower() or "mark" in voice.name.lower():
            male_voice = voice.id
        elif "female" in voice.name.lower() or "zira" in voice.name.lower() or "susan" in voice.name.lower():
            female_voice = voice.id
    
    # If specific gendered voices weren't found, just use the first and second voices if available
    if male_voice is None and len(voices) > 0:
        male_voice = voices[0].id
    if female_voice is None and len(voices) > 1:
        female_voice = voices[1].id
    elif female_voice is None and len(voices) > 0:
        female_voice = voices[0].id
    
    if is_female:
        gender = "FEMALE"
        traits = female_traits
        voice_line = female_voice_lines[int(hash_hex[2:4], 16) % len(female_voice_lines)]
        if female_voice:
            speaker.setProperty('voice', female_voice)
    else:
        gender = "MALE"
        traits = male_traits
        voice_line = male_voice_lines[int(hash_hex[2:4], 16) % len(male_voice_lines)]
        if male_voice:
            speaker.setProperty('voice', male_voice)
    
    # Make an announcement both printed and spoken
    announcement = f"YOUR LAPTOP IS {gender}!"
    print(f"🎉 {announcement} 🎉")
    speaker.say(announcement)
    speaker.runAndWait()
    
    # Say the funny personalized message
    print(f"\n{voice_line}")
    speaker.say(voice_line)
    speaker.runAndWait()
    
    print("\nEvidence of this gender includes:")
    for trait in traits:
        print(f"  • {trait}")
        time.sleep(0.5)  # Pause for comedic timing
    
    print("\n⚠️ DISCLAIMER: This analysis is about as scientific as a horoscope")
    print("written by a cat walking across a keyboard. No laptops were")
    print("stereotyped during the making of this program. Well, maybe a little. ⚠️")

if __name__ == "__main__":
    laptop_gender_check()