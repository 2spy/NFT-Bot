import json
import os

try:
    import time, requests, praw, random  # pip install requests, praw
except:
    os.system("pip install requests")
    os.system("pip install praw")
try:
    from alive_progress import alive_bar
except:
    os.system("pip install alive_progress")
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System  # pip install pystyle
except:
    os.system("pip install pystyle")

try:
    os.system("cls")
except:
    os.system("clear")

with open("config.json", 'r') as confg:
    config = json.load(confg)


class Spy:
    gris = "\033[1;30;1m"
    rouge = "\033[1;31;1m"
    vert = "\033[1;32;1m"
    jaune = "\033[1;33;1m"
    bleu = "\033[1;34;1m"
    violet = "\033[1;35;1m"
    cyan = "\033[1;36;1m"
    blanc = "\033[2;0;1m"


reddit = praw.Reddit(client_id=config["clientid"],
                     client_secret=config["clientsecret"],
                     user_agent="<console:HAPPY:1.0>",
                     username=config["pseudo"],
                     password=config["motdepasse"])

#################################################################
#                                                               #
#                                                               #
#                         BOT REDDIT                            #
#           DISCORD :    https://dsc.gg/spyy                    #
#################################################################


class RedditBot:
    def __init__(self, subcatego="NFTsMarketPlace", nbr_message=1000):
        self.__cooldown = 10
        self.__subcatego = subcatego
        self.__nbr_message = int(
            input(f"{Spy.violet}[{Spy.vert}+{Spy.violet}] Combien de message voulez-vous envoyer ? "))


        category = input(f"{Spy.violet}[{Spy.vert}+{Spy.violet}] Dans quel catégorie voulez-vous ? (hot/new) ")
        if category == "hot":
            self.__category = reddit.subreddit(subcatego).hot(limit=nbr_message)
        if category == "new":
            self.__category = reddit.subreddit(subcatego).new(limit=nbr_message)

    def run(self):
        with open("config.json", 'r') as confg:
            config = json.load(confg)



        try:
            for submission in reddit.subreddit("all").hot(limit=1):
                submission.upvote()
        except:
            print(f"{Spy.violet}[{Spy.rouge}+{Spy.violet}] Les informations du compte sont invalides !")
            input("...")
            return
        error = False
        start = True
        message = 0
        while start or (message != self.__nbr_message):
            with alive_bar(self.__nbr_message, title=f"Reddit Bot", bar='classic',
                           spinner='waves') as bar:

                for submission in self.__category:
                    if message == self.__nbr_message:
                        start = False
                        break
                    data = {"username": "NFT Bot",
                            "avatar_url": "https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/1/6/4"
                                          "/1642c0dc85_50184905_bored-ape-yatch-club-2344.jpg",
                            "embeds": [{
                                "description": f"**Lien du post :** {submission.url}\n\n"
                                               f"**Nom du post :** ``{submission.title}``"
                                               f"\n\n**ID du post :** ``{submission.id}``"
                                               f"\n\n**Commentaire :** {config['metakey']} - "
                                               f"{random.choice(config['phrase'])}\n\n"
                                               f"**Catégorie :**``{self.__subcatego}``\n\n"
                                               f"**Support :** [Join discord](https://discord.com/invite/9pVk32cgCG)",

                                "title": "[✅] **NOUVEAU POSTE !**", "thumbnail": {"url": f"{submission.url}"},
                                "footer": {
                                    "text": "Merci d'utiliser le bot ! Cela me donne de la force ! Bonne chance."}}]}

                    success = {"username": "NFT Bot", "embeds": [
                        {
                            "description": f"**Allez consulter votre compte opensea il se peut que des NFT vous sont "
                                           f"envoyés !!**\n\n**Support :** [Join discord]("
                                           f"https://discord.com/invite/9pVk32cgCG)",
                            "title": "[✅] **PROGRAMME TERMINE !**",
                            "thumbnail": {
                                "url": f"https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/1/6/4"
                                       f"/1642c0dc85_50184905_bored-ape-yatch-club-2344.jpg "
                            }}]}

                    with open('post_list.txt', 'r') as populist:
                        allpost = populist.readline()

                    if submission in allpost.split():
                        message += 1
                        bar()
                        time.sleep(5)

                    else:
                        try:
                            submission.upvote()
                            submission.reply(
                                f"My Metamask Key > {config['metakey']} !"
                                f" {random.choice(config['phrase'])}")
                            requests.post(config['webhook'], json=data)
                            with open("post_list.txt", 'a+') as fishier:
                                fishier.write(f"{submission}\n")
                            message += 1
                            bar()
                            time.sleep(random.randint(20,40))
                        except Exception as err:
                            with bar.pause():
                                    error = {"username": "NFT Bot", "embeds": [
                                        {
                                            "description": f"Allez consulter votre compte reddit il se peut que "
                                                           f"vous êtes rate limited ou que vôtre compte soit "
                                                           f"bannis de reddit ou du subreddit !\n\n```"
                                                           f"{err}```\n\n **Support :** [Join discord]("
                                                           f"https://discord.com/invite/9pVk32cgCG)",
                                            "title": "[❌] **ERREUR !**",
                                            "thumbnail": {
                                                "url": f"https://cdn.futura-sciences.com/buildsv6/images"
                                                       f"/mediumoriginal/1/6/4/1642c0dc85_50184905_bored-ape"
                                                       f"-yatch-club-2344.jpg "
                                            }}]}
                                    err = err
                                    requests.post(config['webhook'], json=error)
                                    error = True

                                    os.system("clear")

                                    print(Spy.violet)
                                    cooldown = self.__cooldown
                                    self.__cooldown *= 10
                                    with alive_bar(cooldown, title="Cooldown - RateLimit", bar='classic',
                                                   spinner="waves", stats=True, elapsed=False,
                                                   monitor=False) as bar2:
                                        while cooldown > 0:
                                            time.sleep(1)
                                            cooldown -= 1
                                            bar2()


                                    os.system("clear")

                                    print(self.__confignumber)
                                    self.run()
            if not error:
                requests.post(config['webhook'], json=success)
            else:
                input(f"{Spy.rouge} >>>> Appuyez sur entrer pour fermer le programme !")


try:
    os.system("cls")
except:
    os.system("clear")

banner = r"""	

                    ,----------------,              ,---------,
               ,-----------------------,          ,"        ,"|
             ,"                      ,"|        ,"        ,"  |
            +-----------------------+  |      ,"        ,"    |
            |  .-----------------.  |  |     +---------+      |
            |  |                 |  |  |     | -==----'|      |
            |  |  NFT Bot V2!    |  |  |     |         |      |
            |  |  Bad command or |  |  |/----|`---=    |      |
            |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
            |  |                 |  |  |  // |(((( [33]|    ,"
            |  `-----------------'  |," .;'| |((((     |  ,"
            +-----------------------+  ;;  | |         |,"
                /_)______________(_/  //'   | +---------+
        ___________________________/___  `,
       /  oooooooooooooooo  .o.  oooo /,   \,"-----------
      / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
     /_==__==========__==_ooo__ooo=_/'   /___________,"
     `-----------------------------'

███▄▄▄▄      ▄████████     ███          ▀█████████▄   ▄██████▄      ███     
███▀▀▀██▄   ███    ███ ▀█████████▄        ███    ███ ███    ███ ▀█████████▄ 
███   ███   ███    █▀     ▀███▀▀██        ███    ███ ███    ███    ▀███▀▀██ 
███   ███  ▄███▄▄▄         ███   ▀       ▄███▄▄▄██▀  ███    ███     ███   ▀ 
███   ███ ▀▀███▀▀▀         ███          ▀▀███▀▀▀██▄  ███    ███     ███     
███   ███   ███            ███            ███    ██▄ ███    ███     ███     
███   ███   ███            ███            ███    ███ ███    ███     ███     
 ▀█   █▀    ███           ▄████▀        ▄█████████▀   ▀██████▀     ▄████▀   
                                                                                

 
                                                         
"""[1:]

Anime.Fade(Center.Center(banner), Colors.white_to_green, Colorate.Vertical, enter=True)
RedditBot().run()
