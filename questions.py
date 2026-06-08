# questions.py — Trilingual question bank for Samjna Web
# Identical content to the desktop version's utils/questions.py

import random

BASELINE = {
    "english": [
        "What did you have for breakfast or lunch today?",
        "Describe the layout of your bedroom or current workspace.",
        "What path or mode of transport do you usually take to go to your college or workplace?",
    ],
    "tamil": [
        "இன்று காலை அல்லது மதியம் என்ன சாப்பிட்டீர்கள்?",
        "உங்கள் படுக்கையறை அல்லது தற்போதைய பணியிடத்தின் அமைப்பை விவரிக்கவும்.",
        "நீங்கள் வழக்கமாக கல்லூரி அல்லது பணியிடத்திற்கு எந்த வழியில் செல்வீர்கள்?",
    ],
    "kannada": [
        "ಇಂದು ಬೆಳಿಗ್ಗೆ ಅಥವಾ ಮಧ್ಯಾಹ್ನ ನೀವು ಏನು ತಿಂದಿದ್ದೀರಿ?",
        "ನಿಮ್ಮ ಮಲಗುವ ಕೋಣೆ ಅಥವಾ ಪ್ರಸ್ತುತ ಕೆಲಸದ ಸ್ಥಳದ ವಿನ್ಯಾಸವನ್ನು ವಿವರಿಸಿ.",
        "ನೀವು ಸಾಮಾನ್ಯವಾಗಿ ಕಾಲೇಜು ಅಥವಾ ಕೆಲಸದ ಸ್ಥಳಕ್ಕೆ ಯಾವ ಮಾರ್ಗ ಬಳಸುತ್ತೀರಿ?",
    ],
}

SOCIAL_STRESS = {
    "english": [
        "Tell me about your single greatest academic failure. Why did you fall short?",
        "If your closest friends were asked to name your biggest personality flaw, what would they say?",
        "Describe a situation where a teacher criticised your work harshly in front of others.",
        "Why do you think some peers balance high grades and internships effortlessly, while you struggle?",
        "Tell me about a time you let your parents down regarding career choices or exam scores.",
        "If we interviewed your past group-project partners, what complaints would they have?",
        "Explain a scenario where you lost your train of thought during a presentation.",
        "What is the most critical feedback you received about your communication or intelligence?",
        "Describe a time you felt completely unqualified compared to everyone else in a room.",
        "You have 30 seconds to explain why we should value your potential over a higher-GPA student. Start now.",
    ],
    "tamil": [
        "உங்கள் மிகப்பெரிய கல்வித் தோல்வியைப் பற்றி சொல்லுங்கள். நீங்கள் ஏன் தோல்வியடைந்தீர்கள்?",
        "உங்கள் நெருங்கிய நண்பர்கள் உங்கள் மிகப்பெரிய குணக் குறையை கூறுமாறு கேட்கப்பட்டால், என்ன சொல்வார்கள்?",
        "ஒரு ஆசிரியர் மற்றவர்கள் முன்னிலையில் உங்கள் பணியை கடுமையாக விமர்சித்த சூழ்நிலையை விவரிக்கவும்.",
        "சில சக மாணவர்கள் உயர் மதிப்பெண்களை எளிதாக சமநிலைப்படுத்தும்போது, நீங்கள் ஏன் போராடுகிறீர்கள்?",
        "உங்கள் வாழ்க்கை தேர்வுகள் தொடர்பாக நீங்கள் பெற்றோரை ஏமாற்றிய நேரத்தைப் பற்றி சொல்லுங்கள்.",
        "உங்கள் கடந்த கால குழு திட்ட கூட்டாளிகளை நாங்கள் நேர்காணல் செய்தால், என்ன புகார்கள் கூறுவார்கள்?",
        "நீங்கள் விளக்கக்காட்சியின்போது சிந்தனையை இழந்த சூழ்நிலையை விளக்குங்கள்.",
        "உங்கள் தொடர்புத் திறன் பற்றி நீங்கள் பெற்ற மிக கடுமையான கருத்து என்ன?",
        "ஒரு வகுப்பறையில் நீங்கள் முற்றிலும் தகுதியற்றவராக உணர்ந்த நேரத்தை விவரிக்கவும்.",
        "அதிக GPA கொண்ட மாணவரை விட உங்கள் திறனை ஏன் மதிக்க வேண்டும் என்று 30 வினாடிகளில் விளக்குங்கள்.",
    ],
    "kannada": [
        "ನಿಮ್ಮ ಅತ್ಯಂತ ದೊಡ್ಡ ಶೈಕ್ಷಣಿಕ ವಿಫಲತೆಯ ಬಗ್ಗೆ ಹೇಳಿ. ನೀವು ಏಕೆ ವಿಫಲರಾದಿರಿ?",
        "ನಿಮ್ಮ ಆತ್ಮೀಯ ಗೆಳೆಯರನ್ನು ನಿಮ್ಮ ಅತಿ ದೊಡ್ಡ ವ್ಯಕ್ತಿತ್ವ ದೋಷ ಹೇಳಲು ಕೇಳಿದರೆ ಏನು ಹೇಳುತ್ತಾರೆ?",
        "ಶಿಕ್ಷಕರು ಇತರರ ಮುಂದೆ ನಿಮ್ಮ ಕೆಲಸವನ್ನು ಕಟುವಾಗಿ ಟೀಕಿಸಿದ ಸಂದರ್ಭವನ್ನು ವಿವರಿಸಿ.",
        "ಕೆಲವು ಸಹಪಾಠಿಗಳು ಉತ್ತಮ ಅಂಕಗಳನ್ನು ಸಲೀಸಾಗಿ ಸಮತೋಲಿಸುವಾಗ ನೀವು ಏಕೆ ಹೆಣಗಾಡುತ್ತೀರಿ?",
        "ನಿಮ್ಮ ವೃತ್ತಿ ಆಯ್ಕೆಗಳ ಬಗ್ಗೆ ನೀವು ಪೋಷಕರನ್ನು ನಿರಾಶೆಗೊಳಿಸಿದ ಸಮಯದ ಬಗ್ಗೆ ಹೇಳಿ.",
        "ನಿಮ್ಮ ಹಿಂದಿನ ಗುಂಪು ಯೋಜನೆ ಪಾಲುದಾರರನ್ನು ಸಂದರ್ಶಿಸಿದರೆ ಏನು ದೂರುತ್ತಾರೆ?",
        "ಪ್ರಸ್ತುತಿಯ ಸಮಯದಲ್ಲಿ ಆಲೋಚನೆ ಕಳೆದುಕೊಂಡ ಸನ್ನಿವೇಶವನ್ನು ವಿವರಿಸಿ.",
        "ನಿಮ್ಮ ಸಂವಹನ ಬಗ್ಗೆ ನೀವು ಪಡೆದ ಅತ್ಯಂತ ಕಟು ಪ್ರತಿಕ್ರಿಯೆ ಯಾವುದು?",
        "ತರಗತಿಯಲ್ಲಿ ಇತರರಿಗೆ ಹೋಲಿಸಿದರೆ ಸಂಪೂರ್ಣ ಅನರ್ಹ ಎಂದು ಭಾಸವಾದ ಸಮಯವನ್ನು ವಿವರಿಸಿ.",
        "ಹೆಚ್ಚಿನ GPA ವಿದ್ಯಾರ್ಥಿಗಿಂತ ನಿಮ್ಮನ್ನು ಏಕೆ ಮೌಲ್ಯಮಾಪನ ಮಾಡಬೇಕು ಎಂಬುದನ್ನು 30 ಸೆಕೆಂಡ್‌ಗಳಲ್ಲಿ ವಿವರಿಸಿ.",
    ],
}

COGNITIVE = {
    "english": [
        "Please count backward aloud from 1,022 in steps of 13. Do not pause.",
        "Spell the word 'MULTIMODAL' completely backward, then state the total number of vowels.",
        "If a train leaves Chennai at 60 km/h and another leaves Bangalore 2 hours later at 80 km/h, how many hours until they cross?",
        "Mentally multiply 14 by 17, subtract 11, and state only the final number aloud.",
        "Recite the months of the year in reverse order, skipping every second month. Start with December.",
        "Take the number 800. Continuously subtract 17 from it out loud until I tell you to stop.",
        "Listen: 7, 3, 9, 1, 5, 8. Recite them back in exact ascending order.",
        "Spell the name of your native city backward while tapping your desk with your finger.",
        "If an assessment has 45 questions and you answer two-fifths incorrectly, how many did you answer correctly?",
        "Repeat the alphabet backward from Z, alternating with numbers starting at 1. Example: Z-1, Y-2. Go fast.",
    ],
    "tamil": [
        "1,022 இலிருந்து 13 படிகளில் பின்னோக்கி எண்ணுங்கள். நிறுத்தாமல் விரைவாக செய்யுங்கள்.",
        "'MULTIMODAL' என்ற வார்த்தையை தலைகீழாக உச்சரித்து, உயிர் எழுத்துகளின் எண்ணிக்கையை கூறுங்கள்.",
        "ஒரு ரயில் சென்னையிலிருந்து 60 கி.மீ./மணி, இன்னொரு 2 மணி பின்னர் பெங்களூரிலிருந்து 80 கி.மீ./மணி, எத்தனை மணி நேரத்தில் சந்திப்பார்கள்?",
        "மனதில் 14-ஐ 17-ஆல் பெருக்கி, 11-ஐ கழித்து, இறுதி எண்ணை மட்டும் சத்தமாக கூறுங்கள்.",
        "ஆண்டின் மாதங்களை தலைகீழ் வரிசையில் ஒவ்வொரு இரண்டாவது மாதத்தை தவிர்த்து சொல்லுங்கள்.",
        "800 இலிருந்து தொடர்ந்து 17-ஐ கழித்துக் கொண்டே போங்கள்.",
        "இலக்கங்கள்: 7, 3, 9, 1, 5, 8. ஏறுவரிசையில் சொல்லுங்கள்.",
        "உங்கள் சொந்த ஊர் பெயரை தலைகீழாக உச்சரியுங்கள், மேஜையை தொடர்ந்து தட்டுங்கள்.",
        "45 கேள்விகள், ஐந்தில் இரண்டு தவறு என்றால், சரியாக எத்தனை பதில் சொன்னீர்கள்?",
        "Z-1, Y-2 என்று தலைகீழ் அகரவரிசையை எண்களுடன் சொல்லுங்கள். விரைவாக செய்யுங்கள்.",
    ],
    "kannada": [
        "1,022 ರಿಂದ 13 ಹೆಜ್ಜೆಗಳಲ್ಲಿ ಹಿಮ್ಮುಖವಾಗಿ ಎಣಿಸಿ. ನಿಲ್ಲಿಸದೆ ವೇಗವಾಗಿ ಮಾಡಿ.",
        "'MULTIMODAL' ಪದವನ್ನು ಹಿಮ್ಮುಖವಾಗಿ ಉಚ್ಚರಿಸಿ, ಸ್ವರಗಳ ಸಂಖ್ಯೆ ಹೇಳಿ.",
        "ಚೆನ್ನೈನಿಂದ 60 ಕಿ.ಮೀ./ಗಂ, ಬೆಂಗಳೂರಿನಿಂದ 2 ಗಂಟೆ ನಂತರ 80 ಕಿ.ಮೀ./ಗಂ, ಎಷ್ಟು ಗಂಟೆಗಳಲ್ಲಿ ಭೇಟಿ?",
        "14 ಅನ್ನು 17 ರಿಂದ ಗುಣಿಸಿ, 11 ಕಳೆದು, ಅಂತಿಮ ಸಂಖ್ಯೆ ಹೇಳಿ.",
        "ತಿಂಗಳುಗಳನ್ನು ಹಿಮ್ಮುಖದಲ್ಲಿ ಪ್ರತಿ ಎರಡನೇ ತಿಂಗಳನ್ನು ಬಿಟ್ಟು ಹೇಳಿ. ಡಿಸೆಂಬರ್‌ನಿಂದ ಪ್ರಾರಂಭಿಸಿ.",
        "800 ರಿಂದ ನಿರಂತರವಾಗಿ 17 ಕಳೆಯುತ್ತಾ ಹೋಗಿ.",
        "ಅಂಕಿಗಳು: 7, 3, 9, 1, 5, 8. ಆರೋಹಣ ಕ್ರಮದಲ್ಲಿ ಹೇಳಿ.",
        "ನಿಮ್ಮ ಊರಿನ ಹೆಸರನ್ನು ಹಿಮ್ಮುಖವಾಗಿ ಉಚ್ಚರಿಸಿ, ಮೇಜನ್ನು ತಟ್ಟಿ.",
        "45 ಪ್ರಶ್ನೆಗಳಲ್ಲಿ ಐದರಲ್ಲಿ ಎರಡು ತಪ್ಪು ಉತ್ತರ, ಸರಿಯಾಗಿ ಎಷ್ಟು ಉತ್ತರಿಸಿದಿರಿ?",
        "Z-1, Y-2 ಎಂದು ವರ್ಣಮಾಲೆಯನ್ನು ಹಿಮ್ಮುಖವಾಗಿ ಸಂಖ್ಯೆಗಳೊಂದಿಗೆ ಹೇಳಿ. ವೇಗವಾಗಿ ಮಾಡಿ.",
    ],
}

RECOVERY = {
    "english": [
        "Tell me about your favourite hobby or what you like to do on weekends.",
        "What is a place you love visiting? Describe it.",
    ],
    "tamil": [
        "உங்கள் பொழுதுபோக்கு அல்லது வார இறுதியில் நீங்கள் ஓய்வெடுக்க விரும்புவதைப் பற்றி சொல்லுங்கள்.",
        "நீங்கள் விரும்பி செல்லும் இடம் எது? அதை விவரிக்கவும்.",
    ],
    "kannada": [
        "ನಿಮ್ಮ ನೆಚ್ಚಿನ ಹವ್ಯಾಸ ಅಥವಾ ವಾರಾಂತ್ಯದಲ್ಲಿ ಏನು ಮಾಡಲು ಇಷ್ಟಪಡುತ್ತೀರಿ ಎಂಬುದರ ಬಗ್ಗೆ ಹೇಳಿ.",
        "ನೀವು ಭೇಟಿ ಮಾಡಲು ಇಷ್ಟಪಡುವ ಸ್ಥಳ ಯಾವುದು? ಅದನ್ನು ವಿವರಿಸಿ.",
    ],
}

PSS = {
    "english": [
        "In the last month, how often have you been upset because of something unexpected?",
        "In the last month, how often have you felt unable to control the important things in your life?",
        "In the last month, how often have you felt nervous and stressed?",
        "In the last month, how often have you felt confident about handling your personal problems?",
        "In the last month, how often have you felt things were going your way?",
        "In the last month, how often have you been able to control irritations in your life?",
        "In the last month, how often have you felt you were on top of things?",
        "In the last month, how often have you been angered because of things outside your control?",
        "In the last month, how often have you felt difficulties were piling up too high?",
        "In the last month, how often have you been able to control the way you spend your time?",
    ],
    "tamil": [
        "கடந்த மாதம், எதிர்பாராத விதமாக நடந்த ஒன்றால் எத்தனை முறை மனம் வருந்தினீர்கள்?",
        "கடந்த மாதம், முக்கியமான விஷயங்களை கட்டுப்படுத்த முடியவில்லை என்று எத்தனை முறை உணர்ந்தீர்கள்?",
        "கடந்த மாதம், எத்தனை முறை பதட்டமாகவும் மன அழுத்தத்திலும் இருந்தீர்கள்?",
        "கடந்த மாதம், தனிப்பட்ட பிரச்சனைகளை சமாளிக்கும் திறனில் எத்தனை முறை நம்பிக்கையாக இருந்தீர்கள்?",
        "கடந்த மாதம், விஷயங்கள் சாதகமாக நடக்கின்றன என்று எத்தனை முறை உணர்ந்தீர்கள்?",
        "கடந்த மாதம், எரிச்சல்களை எத்தனை முறை கட்டுப்படுத்த முடிந்தது?",
        "கடந்த மாதம், எல்லாவற்றையும் கட்டுப்பாட்டில் வைத்திருக்கிறீர்கள் என்று எத்தனை முறை உணர்ந்தீர்கள்?",
        "கடந்த மாதம், கட்டுப்பாட்டிற்கு வெளியே உள்ள விஷயங்களால் எத்தனை முறை கோபமடைந்தீர்கள்?",
        "கடந்த மாதம், சிரமங்கள் மிகவும் அதிகமாக குவிகின்றன என்று எத்தனை முறை உணர்ந்தீர்கள்?",
        "கடந்த மாதம், நேரத்தை எப்படி செலவிடுகிறீர்கள் என்பதை எத்தனை முறை கட்டுப்படுத்த முடிந்தது?",
    ],
    "kannada": [
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ಅನಿರೀಕ್ಷಿತವಾಗಿ ಸಂಭವಿಸಿದ ಕಾರಣದಿಂದ ಎಷ್ಟು ಬಾರಿ ಮನನೊಂದಿದ್ದೀರಿ?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ಪ್ರಮುಖ ವಿಷಯಗಳನ್ನು ನಿಯಂತ್ರಿಸಲು ಸಾಧ್ಯವಾಗುತ್ತಿಲ್ಲ ಎಂದು ಎಷ್ಟು ಬಾರಿ ಅನ್ನಿಸಿದೆ?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ಎಷ್ಟು ಬಾರಿ ಆತಂಕ ಮತ್ತು ಒತ್ತಡ ಅನುಭವಿಸಿದ್ದೀರಿ?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ವೈಯಕ್ತಿಕ ಸಮಸ್ಯೆಗಳನ್ನು ನಿಭಾಯಿಸಲು ಎಷ್ಟು ಬಾರಿ ಆತ್ಮವಿಶ್ವಾಸ ಅನ್ನಿಸಿತು?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ವಿಷಯಗಳು ನಿಮ್ಮ ಅನುಕೂಲಕ್ಕೆ ನಡೆಯುತ್ತಿವೆ ಎಂದು ಎಷ್ಟು ಬಾರಿ ಅನ್ನಿಸಿತು?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ಕಿರಿಕಿರಿಗಳನ್ನು ಎಷ್ಟು ಬಾರಿ ನಿಯಂತ್ರಿಸಲು ಸಾಧ್ಯವಾಯಿತು?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ಎಲ್ಲವನ್ನೂ ನಿಯಂತ್ರಣದಲ್ಲಿ ಇಟ್ಟಿದ್ದೀರಿ ಎಂದು ಎಷ್ಟು ಬಾರಿ ಅನ್ನಿಸಿತು?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ನಿಯಂತ್ರಣದ ಹೊರಗಿದ್ದ ವಿಷಯಗಳಿಂದ ಎಷ್ಟು ಬಾರಿ ಕೋಪಗೊಂಡಿದ್ದೀರಿ?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ತೊಂದರೆಗಳು ತುಂಬಾ ಹೆಚ್ಚಾಗಿ ಪೇರಿಸಿಕೊಳ್ಳುತ್ತಿವೆ ಎಂದು ಎಷ್ಟು ಬಾರಿ ಅನ್ನಿಸಿತು?",
        "ಕಳೆದ ತಿಂಗಳಲ್ಲಿ, ಸಮಯವನ್ನು ಹೇಗೆ ಕಳೆಯುತ್ತೀರಿ ಎಂಬುದನ್ನು ಎಷ್ಟು ಬಾರಿ ನಿಯಂತ್ರಿಸಲು ಸಾಧ್ಯವಾಯಿತು?",
    ],
}

PSS_OPTIONS = {
    "english": ["Never", "Almost Never", "Sometimes", "Fairly Often", "Very Often"],
    "tamil":   ["ஒருபோதும் இல்லை", "கிட்டத்தட்ட இல்லை", "சில சமயம்", "அடிக்கடி", "மிகவும் அடிக்கடி"],
    "kannada": ["ಎಂದಿಗೂ ಇಲ್ಲ", "ಬಹುತೇಕ ಇಲ್ಲ", "ಕೆಲವೊಮ್ಮೆ", "ಸಾಕಷ್ಟು ಬಾರಿ", "ತುಂಬಾ ಬಾರಿ"],
}

PSS_REVERSED = {3, 4, 5, 6, 9}  # 0-indexed reverse-scored items

# Phase config with YOUR timing values
PHASES = [
    {"id": "baseline",         "q_secs": 25, "prep_secs": 2,  "pick": 3},
    {"id": "social_stress",    "q_secs": 25, "prep_secs": 15, "pick": 3},
    {"id": "cognitive_stress", "q_secs": 25, "prep_secs": 5,  "pick": 3},
    {"id": "recovery",         "q_secs": 60, "prep_secs": 1,  "pick": 2},
]

Q_OFFSET = {"baseline": 0, "social_stress": 3, "cognitive_stress": 6, "recovery": 9}

BANKS = {
    "baseline":         BASELINE,
    "social_stress":    SOCIAL_STRESS,
    "cognitive_stress": COGNITIVE,
    "recovery":         RECOVERY,
}


def build_session(lang: str = "english"):
    """Return the full interview session config for one participant."""
    session = []
    for phase in PHASES:
        bank = BANKS[phase["id"]].get(lang, BANKS[phase["id"]]["english"])
        picked = random.sample(bank, min(phase["pick"], len(bank)))
        offset = Q_OFFSET[phase["id"]]
        for i, q_text in enumerate(picked):
            global_q = offset + i + 1
            session.append({
                "phase":     phase["id"],
                "global_q":  f"q{global_q}",
                "q_secs":    phase["q_secs"],
                "prep_secs": phase["prep_secs"],
                "text":      q_text,
            })
    return session
