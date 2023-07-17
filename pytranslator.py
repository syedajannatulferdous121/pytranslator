import requests

class PyTranslator:
    def __init__(self):
        self.base_url = "https://translation-api.example.com"
    
    def translate_text(self, text, source_language, target_language):
        endpoint = f"{self.base_url}/translate"
        params = {
            "text": text,
            "source_language": source_language,
            "target_language": target_language
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            translated_text = response.json()["translation"]
            return translated_text
        else:
            return None
    
    def get_supported_languages(self):
        endpoint = f"{self.base_url}/languages"
        response = requests.get(endpoint)
        if response.status_code == 200:
            supported_languages = response.json()["languages"]
            return supported_languages
        else:
            return None

def main():
    translator = PyTranslator()

    while True:
        print("PyTranslator - Language Translation Application")
        print("Enter 'exit' to quit the application.")
        print("Enter 'languages' to get a list of supported languages.")

        source_language = input("Enter the source language: ")
        if source_language.lower() == "exit":
            break
        elif source_language.lower() == "languages":
            supported_languages = translator.get_supported_languages()
            if supported_languages:
                print("Supported languages:")
                for language in supported_languages:
                    print(f"- {language}")
            else:
                print("Failed to retrieve supported languages.")
            continue

        target_language = input("Enter the target language: ")
        if target_language.lower() == "exit":
            break
        elif target_language.lower() == "languages":
            supported_languages = translator.get_supported_languages()
            if supported_languages:
                print("Supported languages:")
                for language in supported_languages:
                    print(f"- {language}")
            else:
                print("Failed to retrieve supported languages.")
            continue

        text = input("Enter the text to translate: ")
        if text.lower() == "exit":
            break

        translated_text = translator.translate_text(text, source_language, target_language)
        if translated_text:
            print(f"\nTranslated text: {translated_text}")
        else:
            print("Translation failed. Please try again.")

if __name__ == "__main__":
    main()
