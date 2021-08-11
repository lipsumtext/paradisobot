import unittest
import paradisobot

class TestCp(unittest.TestCase):
    def test_cp_glasses(self):
        synonymF = ['glasses','fubuki']
        for i in synonymF:
            self.assertEqual(paradisobot.copypasta(i), """Glasses are really versatile. First, you can have glasses-wearing girls take them off and suddenly become beautiful, or have girls wearing glasses flashing those cute grins, or have girls stealing the protagonist's glasses and putting them on like, "Haha, got your glasses!' That's just way too cute! Also, boys with glasses! I really like when their glasses have that suspicious looking gleam, and it's amazing how it can look really cool or just be a joke. I really like how it can fulfill all those abstract needs. Being able to switch up the styles and colors of glasses based on your mood is a lot of fun too! It's actually so much fun! You have those half rim glasses, or the thick frame glasses, everything! It's like you're enjoying all these kinds of glasses at a buffet. I really want Luna to try some on or Marine to try some on to replace her eyepatch. We really need glasses to become a thing in hololive and start selling them for HoloComi. Don't. You. Think. We. Really. Need. To. Officially. Give. Everyone. Glasses?""")


    def test_cp_marine(self):
        synonymM = ['marineass', 'marinebutt']
        for i in synonymM:
            self.assertEqual(paradisobot.copypasta(i), """I don't think you would understand this. But my butt is really big, it's like "What happened to this?" To explain just how big it is. If i were to take a fall that would break a normal person's bones my butt will absorb all the damage. My bones would be completely fine. It will only end with a single bruise. My butt is the absolute strongest. It's very sturdy, the muscle is so thick. To explain just how thick it is... In my head, i think of myself as having a hitbox and i walk based on that. But while i walk, my butt sways left and right. It's not like it's swaying because i'm trying to shake it. It's just so big it moves on its own and it just becomes a shaky mess. I don`t intent to shake it, i don't mean to walk like a penguin. But it's just so big my body is taken along for the ride. And my body is shaken around by my butt. So, then my hitbox gets misaligned so i start banging into things. Like i think i can get through here, but my butt goes BOOM! And you might think it hurst and that's that but my butt is so much like a cushion but it bounces and sends me flying. I think ...it's like that, its just that bouncy it has its own hitbox. Then there's what happens in bed. You might not understand because you're boys, but when a woman with a butt as big as mine goes to bed, when i lay down my butt is so big my hips start floating. Understand?""")


    def test_cp_navy(self):
        self.assertEqual(paradisobot.copypasta('navyseals'), """What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.""")


    def test_cp_amogus(self):
        self.assertEqual(paradisobot.copypasta('amogus'), """I can't fucking take it. I see an image of a random object posted and then I see it, I fucking see it. "Oh that looks kinda like the among us guy" it started as. That's funny, that's a cool reference. But I kept going, I'd see a fridge that looked like among us, I'd see an animated bag of chips that looked like among us, I'd see a hat that looked like among us. And every time I'd burst into an insane, breath deprived laugh staring at the image as the words AMOGUS ran through my head. It's torment, psychological torture, I am being conditioned to laugh maniacly any time I see an oval on a red object. I can't fucking live like this... I can't I can't I can't I can't I can't! And don't get me fucking started on the words! I'll never hear the word suspicious again without thinking of among us. Someone does something bad and I can't say anything other than "sus." I could watch a man murder everyone I love and all I would be able to say is "red sus" and laugh like a fucking insane person. And the word "among" is ruined. The phrase "among us" is ruined. I can't live anymore. Among us has destroyed my fucking life. I want to eject myself from this plane of existence. MAKE IT STOP!""")


    def test_cp_amoguspeepee(self):
        self.assertEqual(paradisobot.copypasta('amoguscock'), """```
        ‎‎‎⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀ 
 ⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆ 
 ⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟ 
 ⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀ 
 ⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀ ⠀
  ⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⠉⠁⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀ 
     ⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀ ⠀⠀ ⠀⠀⠀⠀
     ⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠀
```""")



if __name__ == '__main__':
    unittest.main()
