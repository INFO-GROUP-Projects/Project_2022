var synth = window.speechSynthesis

var voices = []
var data
var default_voice
var word = document.getElementById("spellingWord").value
var passWord
var index = 0

window.addEventListener("DOMContentLoaded", function(event){
    document.getElementById("gamemaster").addEventListener("click",wordToSpeech)
    console.log("okay")
})
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
        utterThis.rate = 0.75;
        synth.speak(utterThis);
      }

     function wordToSpeech(){  
        passWord = "Spell the word     " + word
        speak()
    }

    function speakAgain(){
        speak() 
    }
        

    