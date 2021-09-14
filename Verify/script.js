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

function verify() {
    var name = document.getElementById("namevalue").value;
    for (var i = 0; i < people.length; i++) {
        if (name == people[i].name){
            window.location.href =  'https://batch-2021.joshuafelipe.repl.co/';
            return
        }
    }

    alert("Sorry name not found");
}