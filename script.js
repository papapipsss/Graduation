var people = [
    { 
        name: "cheska",
        password : "patrice",
        website : "./special/cheska.html"
    },

    { 
        name: "cleo",
        password : "margie",
        website : "./special/cleo.html"
    },

    { 
        name: "zam",
        password : "mae",
        website : "./special/zam.html"
    },

    { 
        name: "icy",
        password : "whysocold",
        website : "./special/icy.html"
    },

    { 
        name: "simon",
        password : "kape",
        website : "./special/simon.html"
    },

    { 
        name: "lucio",
        password : "ulol",
        website : "./special/lucio.html"
    },

    { 
        name: "ceej",
        password : "chel-zee",
        website : "./special/ceej.html"
    },

    { 
        name: "gaile",
        password : "drawer",
        website : "./special/gaile.html"
    },

    { 
        name: "erick",
        password : "justcallmeerick",
        website : "./special/erick.html"
    },

    { 
        name: "kim",
        password : "alexis",
        website : "./special/kim.html"
    },

    { 
        name: "faith",
        password : "marag-gun",
        website : "./special/faith.html"
    },

    { 
        name: "vj",
        password : "plok",
        website : "./special/vj.html"
    },

    { 
        name: "raian",
        password : "mrpresident",
        website : "./special/raian.html"
    },
    
    // { 
    //     name: "daphne",
    //     password : "daph",
    //     website : "./special/daphne.html"
    // },
] 

function getInfo() {
    var username = document.getElementById("name").value;
    var password = document.getElementById("password").value;

    for (var i = 0; i < people.length; i++) {
        if (username == people[i].name && password == people[i].password){
            window.location.href = people[i].website;
            return
        }
    }

    alert("Sorry Name or Password not found");
}

var isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
if (!isChrome){
    $('#iframeAudio').remove()
}
else {
    $('#playAudio').remove() // just to make sure that it will not have 2x audio in the background 
}