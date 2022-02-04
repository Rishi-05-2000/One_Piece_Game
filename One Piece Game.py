name = input('Please type your name: ')
Greet = print("Welcome", name ,"\nyou are about to enter a new World of Adventure.\nPrepare to be Amazed...;)\nyou are in the great pirate age where you go on different adventures on the Sea with your crew memberes and face different challenges along the way.\n Suddenly there is a three way cannal ahead of you,each one leads to different adventures and you need to decide which way to go.If you are lucky You will get the Great Treasure of ONE PIECE left behind by the Legendary Pirate King GOLD.D.Roger")
choice = input("You are given three choices.Each withholds a different adventure,They are:-\n'Marineford,\nLand of Wano,\nSkypiea'.\nPlease select one: ")
while choice == 'Marineford':
    q1 = input("Hello,Marineford is a great adventure filled Story,the Hero of which is you\nNow you are a pirate and you have eaten a Devilfruit named Gomu-Gomu,which makes you a rubber man.\nYou want to save your crew members which are held hostage at the marines headquarters.There is marine admiral named 'Akainu'.\n He has the power of Magu-Magu devilfruit which makes him a Magma mam.He challenges you to a Dual and if you win you will get your crew members or else you will also be captured along with them.Now would that be a yes or no for the challenge?: ")
    if q1 == 'yes':
        print("Hell Yeah,you are Brave.Now you are in the fight for your crew.you are completely beat up but still you have the energy to create a final blow which will be enough to win.come on,you need to win this and for that you first transform to gear 3,a special transformation that upgrades your powers.Now there is one move out of two.you need to choose what it will be? ")
    elif q1 == 'no':
        print("Oooooo no.Wished that you would have tried atleast...")
        break
    q2 = input("you have 'Will smasher' which concentrates all your will power to a single destructive blow and second you have 'Elephant gun' which makes a giant punch and can destroy a whole island.So whats it gonna be?.Thnink wisely.One correct choice and you get your crew or they are gone.Enter the Move name with all your power:  ")
    if q2 == 'Will smasher':
            print("Smooshhhhhhhh.\nyou WIN......\nAlways remember having strong will power will enable you to conquor the Impossible things,and to also your Dreams.So always believe in yourself more than anything. ")
    else :
            print("thushhhhhhhhhhhhhh\nyou landed a blow but he was not at all affected by it.Now he has you and your crew arrested and your great pirate era ends here.But remember... \nnext time choose what your Heart says,what you believe might be true or might not be...\n Never the less thank you for playing along and have a great day...")
    break
while choice == 'Land of Wano':
    q3 = input("Hello,you choose Land of Wano.what are you...,a Hero...\nLand of Wano is the land of samurai.It is the land where the katana's(swords) are used more than words.It is land of fearless.Imagine yourself to be in this world.You were the son of the shogun(King) but your father was betrayed and killed while you were sailing through the sea,going on adventures,fighting different villians,training to be the best.after returning you were shocked to here this tragedy.Now what do want('revenge or no revenge')?  ")
    if q3 == 'revenge':
        print("That's the correct choice")
        q4 = input("Now with all your might and anger you challenge the evil shogun to a dual.but there's a twist...The shogun agrees to the dual on one condition.The condition is if you lose your family will be killed(yes you have a wife and a child) and in addition to that you will have to serve the shogun as a servant for your rest of the life leaving all your pride aside.What will you do?(dual or no dual)?  ")
        if q4 == 'dual' :
            q5 = input("Yes that is what you want.Now you entered the dual.you fight with all you got.The shogun is too strong.But you don't lose hope.The fight is moving towards its end.You are badly hurt and beaten up.There is no way you can win but you have never lost your hope.what will you do?(continue or surrender)?  ")
            if q5 == 'continue':
                print("since you continue the fight,you show the determination you have,you never give up.Suddenly a storm appers out of no where and this tilts the tip towards you.you have the training of fghting in this kind of weather while the shogun doesn't.Thus at the end you kill him and you get your long waited revenge.\nThe thing you learned here is when you never lose hope,and are determined towards achieving it you will always get it.The universe will help you get it.So Never Ever Give up.")
            else:
                print("You should have continued....")
                break
        else:
            print("oooops,Better luck next time")
            break
    else :
        print("WHAT!!,That was no good.Please don't play....")
        break
    break
while choice == 'Skypiea':
    print("Great choice.\nImagine yourself to be in the wonderful city which is above the sky.it is a beautiful city with wonderfull and unimaginable things which are entirely made from clouds.Now what could possibly go wrong here...?\n well often the things that look good from the outside are in reality not soo good....")
    q6 = input("You find that all the beauty that island has was tainted with the blood of the innocent people that made them.The king of Skypiea,Enel,a self-proclaimed God who ate the Goro-Goro-nomi Devilfruit,abused his powers of lightning on people who refused to work for him.When you realised this truth from your friend who lived there,you decided to stop him.Somehow Enel realizes this and kills your friend.This triggers you even more.Now Choose between going berserk over him or cool-mindedly handling situation(Enter ber or cool). ")
    if q6 == 'cool':
        q7 = input("You made the right and smart choice.Now you come up with a plan of defeating him.You decided to reach him in disguise and that worked.It was shocking to him but now there is a all out battle between you and him.You are a rubber man which makes you shock resistant from the attacks thrown by Enel.But Enel Plays it dirty.He makes One of your crew members his target and at the same time Leaves his big ship moving towards the city the impact of which will kill thousands of innocant people.what will you do?you will save both or you will choose one?Enter both or one: ")
        if q7 == 'both' :
            print("That is the only correct option here because you will always find a way if you truely believe that there is always a way.Your crew member tries to lead him try to lure him towards the ship and he accidently attacks the ship which completely destroys it and now you caught him.So now not only you have him but as a gift, the citizens offer you the map of ONE PIECE which is hidden there.You find it.")
            print("On opening the ONE PIECE you found that the ONE PIECE is empty....But you realize that it actually isn't.The ONE PIECE is just a way of showing you all the great adventures you had along with your crew members.You made a new Family, you made countless friends,you became the Strongest by fighting different enemies,you truely acheived all the things that the world has to provide to you.\nThe greatest treasure would not be money,it would be memories...")
        else :
            print("Choosing one was a bad move.please choose both....")
            break
    else:
        print("If you go berserk you get killed by Enel and his Companions.So wrong choice by selecting Your Anger")
        break
    break
