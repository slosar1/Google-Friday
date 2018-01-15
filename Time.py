state = input("enter what state you are currently in (USA ONLY):")


states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
         'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
         'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
         'Maine' 'Maryland','Massachusetts','Michigan','Minnesota',
         'Mississippi', 'Missouri','Montana','Nebraska','Nevada',
         'New Hampshire','New Jersey','New Mexico','New York',
         'North Carolina','North Dakota','Ohio',
         'Oklahoma','Oregon','Pennsylvania','Rhode Island',
         'South  Carolina','South Dakota','Tennessee','Texas','Utah',
         'Vermont','Virginia','Washington','West Virginia',
         'Wisconsin','Wyoming'
]



Eastern = ["Maine", "Florida", "New York", "Rhode Island", "Georgia", "Ohio", "Kentucky", "New Hampshire", "Michigan", "Illinois", "Pennsylvania", "Vermont", "Massachusetts", "Connecticut", "New Jersey", "Delaware", "Maryland", "Virginia", "North Carolina", "South Carolina"]
Central = ["North Dekota", "South Dekota", "Minnesota", "Wisconsin", "Illinois", "Nebraska", "Kansas", "Iowa", "Missouri", "Tennessee", "Oklahoma", "Arkansas", "Mississippi", "Alabama", "Louisiana", "Texas"]
Mountain = ["Montana", "Idaho", "Wyoming", "Utah", "Colorado", "Arizona", "New Mexico"]
Pacific = ["Washington", "Oregon", "Calafornia", "Nevada"]
Alaskan = ["Alaska"]
Hawaiin = ["Hawaii"]

import datetime

zone = {
	"Eastern" : -5,
	"Central" : -6,
	"Mountain" : -7,
	"Pacific" : -8,
	"Alaskan" : -9,
	"Hawaiin" : -10
}

now = datetime.datetime.now()

if state in Eastern:
	print(now-datetime.timedelta(hours = -5))
elif state in Central:
	print(now-datetime.timedelta(hours = -6))
elif state in Mountain:
	print(now-datetime.timedelta(hours = -7))
elif state in Pacific:
	print(now-datetime.timedelta(hours = -8))
elif state in Alaskan:
	print(now-datetime.timedelta(hours = -9))
elif state in Hawaiin:
	print(now-datetime.timedelta(hours = -10))
