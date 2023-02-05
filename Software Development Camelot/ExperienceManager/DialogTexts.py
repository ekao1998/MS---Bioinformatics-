class DialogTexts:

    def __init__(self,M) -> None:
        self.M = M

    story_conversations = {

        "en": {

            "hamlin_roll": [

                "Hamlin: My darling dearest daughter",
                "Hamlin: I am most distressed. Please come see at once whenever you can.",
                "Hamlin: Love Papa.", 
                "PS: Bring the magnifying glass with you. You will need it.",
                "[EndDialog|Exit]"
                
            ],

            "initial_hamlin_conversation" : [
                "Mirabel: Dad! What's wrong? You seem quite worried",
                "Hamlin: Oh honey! The king will have my head on a pike for this! Yes he will! What shall I do?",
                "Mirabel: What happened?",
                "Hamlin: Oh the most unspeakable happened! I lost a cherished gift from the king that he gave me many seasons back and a very confidential letter he gave me the other day.",
                "Mirabel: The King sends you letters and gifts?",
                "Hamlin: Yes. Yes! he's an old friend. An old friend who is going to execute me if I cannot find them again.",
                "Mirabel: What does it look like? May be I can help you look for it?",
                "Hamlin: The gift is a regular-looking gold coin! But it has the insignia of House Covingtomb engraved on one side.",
                "Mirabel: House Covingtomb insignia. The raven perched on a tombstone?",
                "Hamlin: Yes. Yes. The letter has the insignia too. Hard to miss it. Now hurry my dear and help me find it.",
                "[EndDialog|Exit]"

            ],

            "initial_dorothy_conversation_1" : [
                "Mirabel: Your father needs your help!",
                "[EndDialog|Exit]"                
            ],


            "initial_dorothy_conversation_2" : [
                "[Insults|Do I know you? Stay away from me.] | [Praises|Oh Dorothy you look lavish today.]"                
            ],


            "insult_dorothy" :[
                "Dorothy : Go away ungrateful child!",
                "[EndDialog|Exit]"

            ],

            "praise_dorothy" : [
                "Dorothy : Well I must. For my charming prince.",
                "Mirabel : The Prince?",
                "Dorothy : None other. Every prince needs a princess. Which is why I sit here looking all princessy until he notices me.)",
                "Mirabel : Well. I doubt the prince comes out this far South but he would be so lucky to have you as his princess.",
                "Mirabel : My father lost something very important. He's turned the house upside down looking for it.",
                "Dorothy : Curious you say that my child. I saw a man hovering outside your house at witching hour last night.",
                "Mirabel : Really. what did he look like?",
                "Dorothy : Tall and lean with a funny-looking long beard and the most foul of intentions dictating his every action.",
                "Mirabel : He might have stolen Papa's gift. Did you see where he went?",
                "Dorothy : Hmm can't quite remember. But I saw him leave the tavern earlier in the evening.",
                "Mirabel : Thank you Dorothy. You've been most helpful. I must go now.",
                "Dorothy : Do be careful. Especially at the tavern. Take that new boy Nicholaus with you to keep you safe.",
                "Mirabel : Whiny little Nicholaus? No thank you. I will be fine on my own don't worry one bit.",                
            ],


            "elmwood_backstory" : [

                "Long ago the vile witch Viola the Mousebeater lived in Elmwood Forest.",
                "Kingdomfolk lived in fear of her and plotted to have her killed.",
                "One day they stormed her lair and put her to the sword.",
                "However Viola had got wind of their planned execution.", 
                "So the vile witch had concocted a way to beat death.",
                "And now she roams the forest as a spirit. More powerful than ever before.",
                "Infecting those foolish enough to cross it without magical protection.",
                "And commands their captured spirits to commit more vile."

            ],

            "nicholaus_initial_conversation" : [
                "Nicholaus: Hi Mirabel, where you are off to?",
                "Mirabel: Am helping father find his lost gifts. I have a clue leading me to Ginezin",
                "Nicholaus: Sounds fun. Can I join you?",
                "Mirabel: Oh no need. The village needs you more with preparations for celebrations.",
                "Nicholaus: Oh ok. Can I at least scout ahead for you. You know it can be dangerous out here.",
                "[Take Nicholaus help|Ok.If you insist] | [Do not take nicholaus help|No I can take care of myself]"

            ],


            "nicholaus_initial_conversation" : [
                "Nicholaus: Hi Mirabel, where you are off to?",
                "Mirabel: Am helping father find his lost gifts. I have a clue leading me to Ginezin",
                "Nicholaus: Sounds fun. Can I join you?",
                "Mirabel: Oh no need. The village needs you more with preparations for celebrations.",
                "Nicholaus: Oh ok. Can I at least scout ahead for you. You know it can be dangerous out here.",
                "[Take Nicholaus help|Ok.If you insist] | [Do not take nicholaus help|No I can take care of myself]"

            ],

            "warn" : [
                "Fair warning dear player. Elmwood forest is fraught with spirits of haunted dead.", 
                "Without protection you may very well soon join their ranks."

            ],

            "secret_passage_spellbook" : [
                "A spellbook. Count Ginezin must have stolen this from one of his poor victims. I wonder if I can decipher its message",
                "Page One: Welcome O brave one to the fantastical whimsical world of benign witches and wizards where we specialize in whimsy and err...fantasy.",
                "Only a given chosen few can read the language of the Old language of the Cirth. So if you are reading this now I wonder what that says about you?",
                "Page Two: Should you ever find yourself in need then the Sisters of the Cirthian Order will answer your call of distress."
            ],
            "hail_help_prompt":[
                "[HailWitch|Hail a helping hand] "," [DontHailWitch|Find another way. Witch might not be friendly!]"

            ],
            "spellbook_riddle_prompt" : [
                "Safina: Peace to you child. My name is Safina.",
                "Safina: I am descended from a lineage of noble practitioners of the art of magic. We offer our services to the side of good and help to thwart evil.",
                "Safina: What sort of danger are you in child?",
                "Mirabel: My mother used to tell me about your kind. I have so so many questions...",
                "Mirabel: But they can wait. I need to leave this room. The secret path that brought me here is now hidden from me and the guards outside may not like my presence here.",
                "Safina: I sense a deep sense of honor and innocence in you child. But as is our custom I will give you a small test.",
                "Safina: A short riddle that only the kindest of heart can answer. Do you consent?",
                "[AgreeRiddle|Hmm...sure] | [RefuseRiddle|No...I don't have time for this]"
            ],

            "agree_riddle" : [
                "Safina: Because you are patient I'll give you an easy one.",
                "Safina: Only one color but not one size",
                "Safina: Stuck at the bottom yet easily flies.",
                "Safina: Love the sun but not the rain",
                "Safina: Doing no harm and feeling no pain",
                "Safina: What am I?",
                "[FailRiddle|S_l_nc_] | [SolveRiddle|Sh_d_w] | [FailRiddle|W_sd_m]"

            ],

            "refuse_riddle" : [
                "Safina: That's okay child. It takes a while for people to put their trust in us.",
                "Safina: I'll only help you out of the room but no further. I have something for you meanwhile."

            ],

            "reveal_thief" : [
                "Safina: My sisters saw a man scampering in the forest last night. Highly inebriated and barely coherent.",
                "Safina: They saw fit to liberate the following from him. I think they might be of interest to you.",
                "Mirabel: Oh thats my fathers lost souvenirs. Thank you so much.",
                "Safina: You are most welcome child. Well then I'll send you on your way."

            ],

            "solved_riddle" : [
                "Safina: Well done child. You have proven your worth.",
                "Safina: Before I send you on your way I have something for you. "
            ],


            "failed_riddle" : [
                "Safina: Hmm thats unfortunate. I had such high hopes in you.",
                "Safina: I'll only help you out of the room but no further. I have something for you meanwhile."
            ],

            "start_narration" : [
                "The Royal Prince turns 16 in a couple of weeks.In anticipation of his birthday all villages around the kingdom host week-long feasts to celebrate their beloved Royal Prince.",
                "His Highness the King traditionally rewards the villages that holds the most extravagant feast.",
                "This being a very special birthday it is rumored the King has a special prize in mind which is the appointment of one family into nobility as one of the Great Ruling Houses.",
                "Needless to say all villages in the kingdom have taken the rumors to heart and are working overtime to throw the best feast ever to grace the kingdom. The case is no different for the tiny provincial village of Sedonia"
            ],

            "ginezin_narration" : [
                "House Ginezin is one of the most ruthless and feared houses of the kingdom",
                "There have been reports for eons of how the House has crushed opposition and dissenters using threats or blackmail or outright torture and forced disappearances.",
                "All of this of course being the unofficial reports",
                "Because of their methods they have proven most useful to the king and House Covingtomb who as a result have turned a blind eye to the activities of House Ginezin",
                "What interest do they hold with Sedonia? Did they steal Hamlins gift and the letter from the King?"
            ],
            
            

            "prompt_eavesdrop_bandits" : [
                    "[EavesDropDialog|Stay and Eavesdrop] | [LeaveBanditsDialog|Leave]"
            ],

            "bandits_eavesdrop_dialog" : [

                "Bandit1: Have you heard the news.",
                "Bandit2: What news?",
                "Bandit1: From the folks up north.",
                "Bandit2: The barbarian kingdom? Those filthy carrion eaters?",
                "Bandit1: Those so-called filthy carrion eaters are about to make us rich you ogre.",
                "Bandit2: What how?",
                "Bandit1: See I got the scoop from some trustworthy source?",
                "Bandit1: Them barbarian-folk are planning to invade here. Starting with Sedonia.",
                "Bandit1: Think of all the gold and silver and such that they leave behind in the ruins of the poor villagers huh?",
                "Bandit2: Just waiting for us to pick up. Hmm very nice!",
            ],

            "inspect_coin_dialog" : [

                "That...looks like...",
                "That's the House Ginezin insignia on this coin.",
                "Oh no. What sort of trouble has the old man got us into now?"
            ],

            "castle_warning" : [
                "Guard: YOU SHALL NOT PASS!!!",
                
                "[Listen to the guard|Obey] | [Ignore the guard|I can can go wherever I want!]"

            ],


            "ginezin_letter" : [
                "Count Ginezin detailing plans to sabotage Sedonia plans for the celebration of the Prince's birthday. "
                "This is to prevent appointment of a Sedonian to House Lordship as he sees this a threat to his own Lordship status."
                "[Close the letter|Exit]"

            ],

            "menu_change_appearance" : [
                "Choose your character appearance",
                "[changetoBandit|Bandit] | [changetopeasant|Peasant]"
            ],

        },

        "sw": {

            "hamlin_roll": [

                "Hamlin: Binti yangu mpenzi",
                "Hamlin: Nimefadhaika zaidi. Tafadhali njoo uone mara moja unapoweza.",
                "Hamlin: Upendo Baba.",
                "PS: Leta kioo cha kukuza nawe. Utaihitaji.",
                "[EndDialog|Toka]"                
            ],

            "initial_hamlin_conversation" : [
               "Mirabel: Baba! Kuna nini? Unaonekana kuwa na wasiwasi",
                "Hamlin: Oh asali! Mfalme atakuwa na kichwa changu juu ya pike kwa hili! Ndiyo atafanya! Nifanye nini?",
                "Mirabel: Nini kilitokea",
                "Hamlin: Lo jambo lisilosemeka lilitokea! Nilipoteza zawadi niliyoithamini sana kutoka kwa mfalme ambayo alinipa misimu mingi nyuma na barua ya siri sana aliyonipa siku nyingine.",
                "Mirabel: Mfalme anakutumia barua na zawadi?",
                "Hamlin: Ndiyo. Ndiyo! yeye ni rafiki wa zamani. Rafiki wa zamani ambaye ataniua ikiwa sitawapata tena."
                "Mirabel: Inaonekanaje? Labda ninaweza kukusaidia kuitafuta?",
                "Hamlin: Zawadi ni sarafu ya dhahabu inayoonekana mara kwa mara! Lakini ina nembo ya House Covingtomb iliyochorwa upande mmoja.",
                "Mirabel: Nembo ya House Covingtomb. Kunguru alikaa juu ya jiwe la kaburi?",
                "Hamlin: Ndiyo. Ndiyo. Barua ina alama pia. Ni vigumu kuikosa. Sasa fanya haraka mpenzi wangu na unisaidie kuipata.",
                "[EndDialog|Exit]"

            ],

            "initial_dorothy_conversation_1" : [
                "Mirabel: Baba yako anahitaji msaada wako!",
                "[EndDialog|Exit]"                
            ],


            "initial_dorothy_conversation_2" : [
                "[Insults|Ninakujua? Kaa mbali nami.] | [Praises|Oh Dorothy unaonekana kifahari leo.]"                
            ],


            "insult_dorothy" :[
                "Dorothy: Ondoka mtoto asiye na shukrani!",
                "[EndDialog|Exit]"

            ],

            "praise_dorothy" : [
                "Dorothy: Sawa lazima. Kwa mkuu wangu mrembo.",
                "Mirabel: Mkuu?",
                "Dorothy : Hakuna mwingine. Kila mkuu anahitaji binti wa kifalme. Ndiyo maana mimi huketi hapa nikitazama kifalme hadi anitambue.)",
                "Mirabel : Sawa. Nina shaka kwamba mtoto wa mfalme atatoka huku Kusini, lakini atakuwa na bahati ya kuwa na wewe kama binti yake wa kifalme.",
                "Mirabel : Baba yangu alipoteza kitu muhimu sana. Amepindua nyumba akiitafuta.",
                "Dorothy : Nina hamu ya kusema hivyo mtoto wangu. Nilimwona mwanamume akipepea nje ya nyumba yako saa za uchawi jana usiku.",
                "Mirabel : Kweli. alikuwa na sura gani?",
                "Dorothy : Mrefu na konda mwenye ndevu ndefu zinazoonekana kuchekesha na nia chafu zaidi inayoamuru kila kitendo chake.",
                "Mirabel : Huenda aliiba zawadi ya Papa. Umeona alikokwenda?",
                "Dorothy : Hmm siwezi kukumbuka kabisa. Lakini nilimwona akiondoka kwenye tavern mapema jioni.",
                "Mirabel : Asante Dorothy. Umenisaidia sana. Ni lazima niende sasa.",
                "Dorothy : Uwe mwangalifu. Hasa kwenye tavern. Chukua mvulana huyo mpya Nicholaus ili akulinde.",
                "Mirabel : Nicholaus mdogo gani? Hapana asante. Nitakuwa sawa peke yangu usijali hata kidogo."               
            ],


            "elmwood_backstory" : [

                "Zamani mchawi mbaya Viola the Mousebater aliishi katika Msitu wa Elmwood.",
                "Kingdomfolk aliishi kwa kumwogopa na kupanga njama ya kumuua.",
                "Siku moja walivamia pango lake na kumuua kwa upanga.",
                "Hata hivyo Viola alipata taarifa kuhusu utekelezaji wao uliopangwa.",
                "Kwa hivyo yule mchawi mbaya alikuwa amebuni njia ya kupiga kifo.",
                "Na sasa anazurura msituni kama roho. Mwenye nguvu zaidi kuliko hapo awali.",
                "Kuambukiza wale wapumbavu kiasi cha kuvuka bila ulinzi wa kichawi.",
                "Na anaamuru roho zao zilizokamatwa kufanya uovu zaidi."

            ],

            "nicholaus_initial_conversation" : [
                "Nicholaus: Hi Mirabel, unaenda wapi?",
                "Mirabel: Namsaidia baba kupata zawadi zake zilizopotea. Nina kidokezo kinachoniongoza hadi Ginezin",
                "Nicolaus: Inaonekana kufurahisha. Je, ninaweza kujiunga nawe?",
                "Mirabel: Oh hakuna haja. Kijiji kinakuhitaji zaidi na maandalizi ya sherehe.",
                "Nicholaus: Sawa. Je! ninaweza angalau kukutafuta. Unajua inaweza kuwa hatari hapa nje.",
                "[Take Nicholaus help|Ok.If you insist] | [Do not take nicholaus help|No I can take care of myself]"

            ],


            "nicholaus_initial_conversation" : [
                "Nicholaus: Hi Mirabel, unaenda wapi?",
                "Mirabel: Namsaidia baba kupata zawadi zake zilizopotea. Nina kidokezo kinachoniongoza hadi Ginezin",
                "Nicolaus: Inaonekana kufurahisha. Je, ninaweza kujiunga nawe?",
                "Mirabel: Oh hakuna haja. Kijiji kinakuhitaji zaidi na maandalizi ya sherehe.",
                "Nicholaus: Sawa. Je! ninaweza angalau kukutafuta. Unajua inaweza kuwa hatari hapa nje.",
                "[Take Nicholaus help|Ok.If you insist] | [Do not take nicholaus help|No I can take care of myself]"

            ],

            "warn" : [
                "Onyo la haki mchezaji mpendwa. Msitu wa Elmwood umejaa roho za wafu.",
                "Bila ulinzi unaweza hivi karibuni kujiunga na safu zao."

            ],

            "secret_passage_spellbook" : [
                "Kitabu cha spelling. Hesabu Ginezin lazima aliiba hii kutoka kwa mmoja wa wahasiriwa wake maskini. Nashangaa kama ninaweza kufafanua ujumbe wake",
                "Ukurasa wa Kwanza: Karibu O shujaa kwa ulimwengu wa ajabu wa kichekesho wa wachawi na wachawi wazuri ambapo tuna utaalam wa kuropoka na kukosea...fantasia.",
                "Wachache waliochaguliwa tu ndio wanaweza kusoma lugha ya Lugha ya Kale ya Cirth. Kwa hivyo ikiwa unasoma hii sasa nashangaa hiyo inasema nini juu yako?",
                "Ukurasa wa Pili: Iwapo utawahi kujikuta katika mahitaji basi Masista wa Agizo la Cirthian watajibu wito wako wa dhiki."
            ],

            "hail_help_prompt":[
                "[HailWitch|Omba usaidizi] "," [DontHailWitch|Tafuta namna nyengine. Mchawe anaweza kuwa hasimu!]"

            ],
            "spellbook_riddle_prompt" : [
                "Safina: Amani kwako mtoto. Naitwa Safina.",
                "Safina: Nimetokana na ukoo wa watendaji wakuu wa sanaa ya uchawi. Tunatoa huduma zetu kwa upande wa wema na kusaidia kuzuia maovu.",
                "Safina: Ni hatari gani uliyo nayo mtoto?",
                "Mirabel: Mama yangu alikuwa akiniambia kuhusu aina yako. Nina maswali mengi ... ",
                "Mirabel: Lakini wanaweza kusubiri. Nahitaji kuondoka kwenye chumba hiki. Njia ya siri iliyonileta sasa imefichwa kwangu na walinzi wa nje wanaweza wasipende uwepo wangu hapa.",
                "Safina: Nahisi hisia za heshima na kutokuwa na hatia kwako mtoto. Lakini kama ilivyo desturi yetu nitakupa mtihani mdogo.",
                "Safina: Kitendawili kifupi ambacho ni mwenye moyo mkarimu pekee ndiye anayeweza kujibu. Je! unakubali?",
                "[AgreeRiddle|Hmm...sure] | [RefuseRiddle|No...I don't have time for this]"
            ],

            "agree_riddle" : [
                "Safina: Kwa sababu una subira nitakupa rahisi.",
                "Safina: Rangi moja tu lakini sio saizi moja",
                "Safina: Amekwama chini lakini anaruka kwa urahisi.",
                "Safina: Penda jua lakini sio mvua",
                "Safina: Hakudhuru wala kuhisi maumivu",
                "Safina: mimi ni nani?",
                "[FailRiddle|S_l_nc_] | [SolveRiddle|Sh_d_w] | [FailRiddle|W_sd_m]"

            ],

            "refuse_riddle" : [
                "Safina: Ni sawa mtoto. Inachukua muda kwa watu kuweka imani yao kwetu.",
                "Safina: Nitakusaidia tu kutoka nje ya chumba lakini si zaidi. Nina kitu kwa ajili yako wakati huo huo."

            ],

            "reveal_thief" : [
                "Safina: Dada zangu walimwona mwanamume akitoroka msituni jana usiku. Amelewa sana na hana uhusiano wowote.",
                "Safina: Waliona ni vyema kuwakomboa wafuatao kutoka kwake. Nadhani wanaweza kuwa na maslahi kwako.",
                "Mirabel: Ndio baba zangu walipoteza zawadi. Asante sana.",
                "Safina: Karibu sana mtoto. Basi nitakutumia njia yako."

            ],

            "solved_riddle" : [
                "Safina: Umefanya vizuri mtoto. Umethibitisha thamani yako.",
                "Safina: Kabla sijakupeleka njiani nina kitu kwa ajili yako."
            ],


            "failed_riddle" : [
                "Safina: Hmm hiyo ni bahati mbaya. Nilikuwa na matumaini makubwa na wewe.",
                "Safina: Nitakusaidia tu kutoka nje ya chumba lakini si zaidi. Nina kitu kwa ajili yako wakati huo huo."
            ],

            "start_narration" : [
                "Mfalme wa Kifalme anatimiza umri wa miaka 16 katika wiki chache. Kwa kutarajia siku yake ya kuzaliwa, vijiji vyote karibu na ufalme huandaa karamu za wiki nzima kusherehekea Prince wao mpendwa.",
                "Mtukufu Mfalme kwa jadi huzawadia vijiji vinavyofanya karamu kubwa zaidi.",
                "Hii ikiwa ni siku ya kuzaliwa ya kipekee sana inasemekana kuwa Mfalme ana tuzo maalum akilini ambayo ni kuteuliwa kwa familia moja kuwa ya kifahari kama moja ya Nyumba Kubwa za Utawala.",
                "Bila shaka vijiji vyote katika ufalme huo vimetilia maanani uvumi huo na wanafanya kazi kwa muda wa ziada ili kuandaa karamu bora zaidi kuwahi kupamba ufalme. Kesi hiyo sio tofauti kwa kijiji kidogo cha mkoa wa Sedonia"
            ],

            "ginezin_narration" : [
                "Nyumba ya Ginezin ni moja ya nyumba katili na za kuogopwa zaidi za ufalme",
                "Kumekuwa na ripoti kwa muda mrefu za jinsi Bunge lilivyokandamiza upinzani na wapinzani kwa kutumia vitisho au ulaghai au mateso ya moja kwa moja na kutoweka kwa lazima.",
                "Haya yote bila shaka ni ripoti zisizo rasmi",
                "Kwa sababu ya mbinu zao wamethibitisha kuwa muhimu zaidi kwa mfalme na House Covingtomb ambao kwa sababu hiyo wamefumbia macho shughuli za House Ginezin",
                "Je, wana maslahi gani na Sedonia? Je, waliiba zawadi ya Hamlins na barua kutoka kwa Mfalme?"
            ],
            
            "spooky_hint": [
                "Nasikia sauti karibu",
                "Ninaweza kusikia kitu muhimu ikiwa nikikaa kimya vya kutosha"

            ],

            "prompt_eavesdrop_bandits" : [
                    "[EavesDropDialog|Stay and Eavesdrop] | [LeaveBanditsDialog|Leave]"
            ],

            "bandits_eavesdrop_dialog" : [

                "Jambazi1: Umesikia habari.",
                 "Jambazi2: Habari gani?",
                 "Jambazi1: Kutoka kwa watu wa kaskazini.",
                 "Jambazi2: Ufalme wa kishenzi? Wala mizoga wachafu hao?",
                 "Jambazi1: Wale wanaoitwa walaji mizoga wachafu wanakaribia kututajirisha zimwi wewe.",
                 "Jambazi2: Vipi?",
                 "Jambazi1: Unaona nimepata habari kutoka kwa chanzo fulani cha kuaminika?",
                 "Jambazi1: Hao watu wa kishenzi wanapanga kuvamia hapa. Kuanzia Sedonia.",
                 "Jambazi1: Fikiria dhahabu na fedha yote na ambayo wanaacha nyuma katika magofu ya wanakijiji maskini?",
                 "Jambazi2: Inasubiri tu tuchukue. Hmm nzuri sana!",
            ],

            "inspect_coin_dialog" : [

                "Inaonekana kama ...",
                "Hiyo ni nembo ya Nyumba ya Ginezin kwenye sarafu hii.",
                "Hapana. Mzee ametuingiza kwenye matatizo gani sasa?"
            ],

            "castle_warning" : [
                "Mlinzi: HUTAPITA!!!",
                 "......Minong'ono ya siri......",
                 "Inaonekana kuwa na njia ya siri katika jiji ...",
                 "Kiumbe mzuri anayezunguka maji ...",
                "[Listen to the guard|Fuata amri] | [Ignore the guard|Nitaenda nitakako!]"

            ],

            "ginezin_letter" : [
                "Hesabu Ginezin akifafanua mipango ya kuharibu mipango ya Sedonia ya kusherehekea siku ya kuzaliwa ya Prince."
                "Hii ni kuzuia kuteuliwa kwa Sedonian kwa Ubwana wa Nyumba kwani anaona hii ni tishio kwa hali yake ya Ubwana."
                "[Close the letter|Exit]"

            ],
        }

    }     


    def get_text(self, conversation_label,language="en"):
        language = self.M.game_language
        text = self.story_conversations[language][conversation_label]
        return text

    # Additional texts to be added
    def set_text(self, conversation_label, language="en", text_list=[]):
        self.story_conversations[language][conversation_label] = text_list
        return True

    def get_specific_class(self,language="en",conversation_class=""):
        language = self.M.game_language
        texts = [val for key,val in self.story_conversations[language].items() if conversation_class.lower() in key.lower()]
        return texts

if __name__ == '__main__':
    D = DialogTexts()
    # print(D.get_text("initial_hamlin_conversation"))
    print(D.get_specific_class(conversation_class="initial"))