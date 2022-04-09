var synth = window.speechSynthesis

var voices = []
var data
var default_voice
var passWord
var index = 0

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
    
      function updateText(index){
        passWord = "Spell the word     " + data[index];
      }
    
    
    async function getWordsI(){
        let response = await fetch("https://"+window.location.host+'/api/getWordsIncrements/')
        data = await response.json()
        return data
    }

    async function wordToSpeech(){
        data = await getWordsI()
        let htmlBody = document.querySelector("#contents")
        let html
        html += `
            <input type ="text" id ="textBox"> 
            <label for = "textBox">Spell Word </label>
            <button onclick="speakAgain()"> Speak Slower </button>
            <button onclick="speakAgain()"> Speak </button>
            <button onclick="speakAgain()"> Speak Faster </button>
            <button onclick = "validate_Word()">Submit </button>
        `
        htmlBody.innerHTML = html
        updateText(index)
    }

    function speakAgain(){
        speak()
    }

    function validate_Word(){
        let inputField = document.querySelector('#textBox')
        let comp = inputField.value

        if(comp === data[index]){
            //do something
            console.log("Correct")
            if(index < 9){
                index = index + 1
                updateText(index)
                speakAgain()
            }
           
        }
        else{
            console.log("Incorrect word is " +data[index])
            //do something else
        }
    }
        

    