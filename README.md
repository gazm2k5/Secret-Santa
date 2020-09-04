# Secret-Santa
Python code to assign Secret Santa gifts. It can be double blind (you don't know who you're giving to or who you're recieving from) and can facilitate each  gifting multiple gifts.

## Web version
I have made a web app version of this code, which is much more user friendly. Ignore the rest of this page and go here: https://www.sunfire.xyz/secret-santa/ unless you want to see the code.

## Numberphile's "The Problems with Secret Santa"
The algorithm was based off of Hannah Fry's explanation: https://www.youtube.com/watch?v=5kC5k5QBqcc
The code mimics everyone being assigned a number. Their number is also written down on a piece of paper X times, then split between other people in the group with a "shifting" method.

The result is a list of who everyone is gifting in number format. You can organise neat piles with number labels, and everyone goes round putting their gifts down in the assigned pile. This would make it double blind, as you wouldn't know who you're gifting, or who has given gifts to you.

## Why did I make this
See https://www.sunfire.xyz/secret-santa/ for explanation of why this is a better Secret Santa method.

## Difference between version 3 and version 4.5
Secret Santa 3 was the third iteration of the project. The first two mimicked picking names out of a hats etc, which are flawed methods as seen in numberphile's video. Version 3 therefore follows the method shown in the video, "shifting" tickets along.

Secret Santa 4.5 also allows different numbers of gifts per person. If everyone in a group of 15 has been assigned to give and receive 3 gifts, but one person turns up with only one gift, they can still participate as this function can assign the "awkward" person one person to give to, and will also only be assigned to one other person.

## How to run
Simply run either of the two Python versions in Python 3.8 or higher. It has a simple console output. The last line in the file runs the functions, so you pass in how many people there are in the group, and how many gifts each person will gift/receive.

For version 4.5, any numbers after the first 2 arguments are the number of gifts awkward people have, so if there are 12 people in the group and you have agreed to gift 5 times each, but one person has turned up with 3 gifts, and another with only 1 gift you can run: `secretSanta(12, 5, 1, 3)`


## Error checking
There are a few sanity check functions built in to let you know that everyone has been assigned the correct number of gifts, and that no one has incorrectly been assigned themselves, or that one person has been assigned to gift the same person twice.

The shifting method in version 3 is always succesful, but in 4.5 the ticket shifting sometimes loops round in a funny way after the tickets are shuffled. As a result it sometimes doesn't assign everyone correctly, however it always performs checks and will tell you if an error has occured.
