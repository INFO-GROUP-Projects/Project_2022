var synth = window.speechSynthesis

var voices = []
var default_voice
var passWord;

function populateVoiceList(){
    voices = synth.getVoices().sort(function (a, b){
        const aname = a.name.toUpperCase(), bname = b.name.toUpperCase();
        if ( aname < bname ) return -1;
        else if ( aname == bname ) return 0;
        else return +1;
    });

    for(i = 0; i < voices.length(); i++){
            if(voices[i].default){
                default_voice = voices[i]
            }
    }
}

    function speak(){
        if (synth.speaking) {
            console.error('speechSynthesis.speaking');
            return;
        }

        var utterThis = new SpeechSynthesisUtterance(passWord);
        utterThis.onend = function (event) {
            console.log('SpeechSynthesisUtterance.onend');
        }
        
        utterThis.onerror = function (event) {
            console.error('SpeechSynthesisUtterance.onerror');
        }

        utterThis.voice = default_voice;
        utterThis.pitch = 1;
        utterThis.rate = 1;
        synth.speak(utterThis);
      }
    
    
    async function getWordsI(){
        let response = await fetch("https://"+window.location.host+'/api/getWordsIncrements/')
        let data = await response.json()
        return data
    }

    async function wordToSpeech(){
        data = await getWordsI()
        passWord = "Spell the word     " + data[0];
        speak()

    }