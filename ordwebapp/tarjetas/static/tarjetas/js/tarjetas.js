document.addEventListener("DOMContentLoaded", function() {
    const themeSwitch = document.querySelector('#theme-toggle');
    themeSwitch.checked = localStorage.getItem('switchedTheme') === 'true';
    const darkimg = document.querySelector("#img-darktheme");
    const lightimg = document.querySelector("#img-lighttheme");
    
    if (localStorage.getItem('switchedTheme') === 'true') {
        darkimg.style.display = 'none';
        lightimg.style.display = 'inline';
    }

    themeSwitch.addEventListener('change', function (e) {
        if(e.currentTarget.checked === true) {
            // Add item to localstorage
            localStorage.setItem('switchedTheme', 'true');
            darkimg.style.display = "none";
            lightimg.style.display = "inline";

        } else {
            // Remove item if theme is switched back to normal
            localStorage.removeItem('switchedTheme');
            lightimg.style.display = "none";
            darkimg.style.display = "inline";
        }
    });
});

function machineWrite(msg) {
    msg.innerHTML = msg.textContent.replace(/\S/g, "<span class='letter'>$&</span>");
    var spans = msg.getElementsByClassName('letter');
    var nSpans = spans.length;
    var i;
    for (i = 0; i < nSpans; i++) {
        typing(i, spans)
    }
}

function typing(i, spans) { 
    setTimeout(function() {
        spans[i].classList.add('shw');
    }, 25 * i); 
} 

function showTranslation() {
    var checkBox = document.getElementById("swipe-card");
    var norwegian = document.getElementById("norwegian-SD");
    var translation = document.getElementById("translation-SD");
    var card = document.getElementsByClassName("button sid")[0];

    if (checkBox.checked == true){
        setTimeout(() => { norwegian.classList.add("swip") }, 200);
        setTimeout(() => { translation.classList.add("swip") }, 200);
        card.classList.add("swip");
    } else {
        setTimeout(() => { norwegian.classList.remove("swip") }, 200);
        setTimeout(() => { translation.classList.remove("swip")}, 200);
        card.classList.remove("swip");
    }
}

var counter = 0;
function profesor() {
    if(event.key === 'Enter') {
        const correct = document.getElementById("correct");
        const fail = document.getElementById("fail");
        const fail2 = document.getElementById("fail2");
        var guess = document.getElementById("guess-it").value.toUpperCase();
        var swer = document.getElementById("swer").textContent.toUpperCase();
        var spswer = swer.split("/");
        var calif = spswer.includes(guess);
        if(calif == true) {
            counter++;
            if (counter == 1) {
                fail.style.display = "none";
                fail2.style.display = "none";
                correct.style.display = "block";
            }
            if (counter == 2) {
                location.reload();
            }
        } else {
            fail.style.display = "block";
            fail2.style.display = "block";
            fail2.innerText = "Maybe you meant: " + spswer;
        }
    }
}