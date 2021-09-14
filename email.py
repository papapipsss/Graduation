import smtplib
from email.message import EmailMessage


people = {
		"person0" : { 
        "name": "joshuafelipe",
        "password" : "felipesakalam",
        "email" : "joshua.felipe.shs@ust.edu.ph"
    },

		# "person1" : { 
    #     "name": "cheska",
    #     "password" : "patrice",
    #     "email" : "francheskapatrice.aldaba.shs@ust.edu.ph"
    # },

    # "person2" : { 
    #     "name": "cleo",
    #     "password" : "margie",
    #     "email" : "margarethcleopatra.castillo.shs@ust.edu.ph"
    # },

    # "person3" : { 
    #     "name": "zam",
    #     "password" : "mae",
    #     "email" : "izzamae.deocampo.shs@ust.edu.ph"
    # },

    # "person4" : { 
    #     "name": "icy",
    #     "password" : "whysocold",
    #     "email" : "althealaicy.cruz.shs@ust.edu.ph "
    # },

    # "person5" :  { 
    #     "name": "simon",
    #     "password" : "kape",
    #     "email" : "simon.mina.shs@ust.edu.ph"
    # },

    # "person6" : { 
    #     "name": "lucio",
    #     "password" : "ulol",
    #     "email" : "lucioraphael.manucdoc.shs@ust.edu.ph"
    # },

    # "person7" : { 
    #     "name": "ceej",
    #     "password" : "chel-zee",
    #     "email" : "cheljeemei.mangulabnan.shs@ust.edu.ph"
    # },

    # "person8" : { 
    #     "name": "gaile",
    #     "password" : "drawer",
    #     "email" : "gailemeizty.mosada.shs@ust.edu.ph"
    # },

    # "person9" : { 
    #     "name": "erick",
    #     "password" : "justcallmeerick",
    #     "email" : "johnerick.mangubat.shs@ust.edu.ph"
    # },

    # "person10" : { 
    #     "name": "kim",
    #     "password" : "alexis",
    #     "email" : "kimalexis.ecabeza.shs@ust.edu.ph "
    # },

    # "person11" : { 
    #     "name": "faith",
    #     "password" : "marag-gun",
    #     "email" : "faithhenrick.maraggun.shs@ust.edu.ph"
    # },

    # "person12" : { 
    #     "name": "vj",
    #     "password" : "plok",
    #     "email" : "vincentjoshua.guellen.shs@ust.edu.ph"
    # },

    # "person13" : { 
    #     "name": "raian",
    #     "password" : "mrpresident",
    #     "email" : "raiananthony.diolata@ust.edu.ph"
    # },
    
    # "person14" : { 
    #     "name": "daphne",
    #     "password" : "daph",
    #     "email" : "daphnejanelyn.go.shs@ust.edu.ph"
    # },

}


def feedback():
	for i in people:
		message = f"Hi {people[i]['name'].title()},\n\nTo personally thank you for being part of my Senior High School life, I send you this personal website.\n\nBelow are the credentials that you may use in the website.\n\nUse this link to access the website:\thttps://batch-2021.joshuafelipe.repl.co/\n\nJust enter the details on the fill up form.\n\n\tName: {people[i]['name']}\n\n\tPassword: {people[i]['password']}\n\nThank you and Enjoy!"

		email = EmailMessage()
		email['from'] = 'no.reply.batch2021@gmail.com'
		email['to'] = f"{people[i]['email']}"
		email['subject'] = f"{people[i]['name'].title()} Congratulations"

		email.set_content(f'{message}\n\n\nFrom your very own, Pipapips <3')
		with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.login('no.reply.batch2021@gmail.com','joshuafelipe')
				smtp.send_message(email)
				print(f"Email succesfully sent to {people[i]['name'].title()}")

feedback()