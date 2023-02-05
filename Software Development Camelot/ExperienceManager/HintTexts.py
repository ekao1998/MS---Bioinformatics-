class HintTexts:

    def __init__(self,M) -> None:
        self.M = M

    story_hints = {

        "en": {

            "home_1" : [
                "Magnifying glass might be useful."
                ],

            "sedonia_1" : [
                "Fair warning dear player. Elmwood forest is fraught with spirits of haunted dead.", 
                "Without protection you may very well soon join their ranks."

            ],

            "castlecrossroad_1": [

                "......Mystery whisper......",
                "Seems to have a secret path in the city...",
                "Beautiful creature srrounding by the water..."
                ],

            "spooky_1": [
                "I can hear voices nearby",
                "I might be able to hear something important if I stay quiet enough"],

        },

        "sw": {
        "home_1" : [
            "Kioo cha kukuza kinaweza kuwa muhimu."
            ],

            "sedonia_1": [
                "[EndDialog|Toka]",                
            ],

            "castlecrossroad_1": [
                "......Minong'ono ya siri......", 
                "Inaonekana kuwa na njia ya siri mjini...", 
                "Kiumbe mrembo anayezunguka maji..."
                ],

            "spooky_1": [
                "Nasikia sauti karibu",
                "Ninaweza kusikia kitu muhimu ikiwa nikikaa kimya vya kutosha"
                ],

        }

    }

    
    def get_text(self, hint_label,language="en"):
        text = self.story_hints[language][hint_label]
        return text

    # Additional texts to be added
    def set_text(self, hint_label, language="en", text_list=[]):
        self.story_hints[language][hint_label] = text_list
        return True

    def get_specific_class(self,language="en",hint_class=""):
        texts = [val for key,val in self.story_hints[language].items() if hint_class.lower() in key.lower()]
        return texts

if __name__ == '__main__':
    H = HintTexts()
    # print(D.get_text("initial_hamlin_conversation"))
    print(H.get_specific_class(hint_class="sed"))