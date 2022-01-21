import os
import json
try:
    import time, requests, praw, random #pip install requests, praw
except:
    os.system("pip install requests")
    os.system("pip install praw")
try:
    from alive_progress import alive_bar
except:
    os.system("pip install alive_progress")
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System #pip install pystyle
except:
    os.system("pip install pystyle")
    
os.system("cls")

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
    
editconfig = input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Voulez-vous modifier la config ? (y/n)")
if editconfig == "y" or editconfig == "Y" or editconfig == "yes" or editconfig == "YES":
    with open("config.json", "w+") as confg:
        config["pseudo"] = input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Pseudo du compte reddit :" )
        config["motdepasse"] = input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Mot de passe du compte reddit : ")
        config["clientid"] = input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Client ID de l'application : ")
        config["clientsecret"] = input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Client Secret de l'application : ")
        config["webhook"] = input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Lien du webhook : ")
        config["metakey"] = input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Votre clé métamask : ")
        json.dump(config,confg,indent=4)

try:
    reddit = praw.Reddit(client_id = config["clientid"],
                        client_secret = config["clientsecret"],
                        user_agent = "<console:HAPPY:1.0>",
                        username = config["pseudo"],
                        password= config["motdepasse"])
except:
    print(f"{Spy.blanc}[{Spy.rouge}+{Spy.blanc}] Les informations du compte sont invalides !")


#################################################################
#                                                               #
#                                                               #
#                         BOT REDDIT                            #
#           DISCORD :    https://dsc.gg/spyy                    #
#################################################################        
        
class RedditBot:
    def __init__(self, subcatego = "NFTsMarketPlace", nbr_message = 200, catego = "hot"):
        self.__subcatego = subcatego
        self.__nbr_message = int(input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Combien de message voulez-vous envoyer ? "))
        catego = input(f"{Spy.blanc}[{Spy.vert}+{Spy.blanc}] Dans quel catégorie voulez-vous ? (hot/new) ")
        if catego == "hot":
            self.__catego = reddit.subreddit(subcatego).hot(limit = nbr_message)
        if catego == "new":
            self.__catego = reddit.subreddit(subcatego).new(limit = nbr_message)

            
    
    def run(self):
        erreur = False
        start = True    
        while start == True:
            print(Spy.vert)
            with alive_bar(self.__nbr_message ,title = "Reddit Bot",  bar='classic', spinner='twirls') as bar:
                for submission in self.__catego:
                    data = {
                        "username" : "NFT Bot",
                        "avatar_url" : "https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/1/6/4/1642c0dc85_50184905_bored-ape-yatch-club-2344.jpg"
                        }
                    data["embeds"] = [
                    {
                        "description" : f"**Lien du post :** {submission.url}\n\n**Nom du post :** ``{submission.title}``\n\n**ID du post :** ``{submission.id}``\n\n**Commentaire :** {config['metakey']} - {random.choice(config['phrase'])}\n\n**Catégorie :**``{self.__subcatego}``\n\n**Support :** [Join discord](https://discord.com/invite/9pVk32cgCG)",
                        "title" : "[✅] **NOUVEAU POSTE !**",
                        "thumbnail" : {
                            "url" : f"{submission.url}"
                            },
                        "footer" : {
                            "text" : "Merci d'utiliser le bot ! Cela me donne de la force ! Bonne chance."
                        }}]

                    sucess = {
                    "username" : "NFT Bot"
                    }
                    sucess["embeds"] = [
                    {
                        "description" : f"**Allez consulter votre compte opensea il se peut que des NFT vous sont envoyés !!**\n\n**Support :** [Join discord](https://discord.com/invite/9pVk32cgCG)",
                        "title" : "[✅] **PROGRAMME TERMINE !**",
                        "thumbnail" : {
                            "url" : f"https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/1/6/4/1642c0dc85_50184905_bored-ape-yatch-club-2344.jpg"
                            }}]                    

                        
                    with open('post_list.txt', 'r') as postlist:
                        allpost = postlist.readline()
                    if submission in allpost.split():
                        bar()
                        time.sleep(5)
                    else:
                        try:
                            submission.upvote()
                            submission.reply(f"My Metamask Key > {config['metakey']} ! {random.choice(config['phrase'])}")
                            requests.post(config['webhook'], json = data)
                            with open("post_list.txt", 'a+') as fichier:
                                fichier.write(f"{submission}\n")
                            bar()
                            time.sleep(random.randint(20,40))
                        except Exception as err:
                            error = {
                            "username" : "NFT Bot"
                            }
                            error["embeds"] = [
                            {   
                            "description" : f"Allez consulter votre compte reddit il se peut que vous êtes rate limited ou que vôtre compte soit bannis de reddit ou du subreddit !\n\n```{err}```\n\n **Support :** [Join discord](https://discord.com/invite/9pVk32cgCG)",
                            "title" : "[❌] **ERREUR !**",
                            "thumbnail" : {
                                "url" : f"https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/1/6/4/1642c0dc85_50184905_bored-ape-yatch-club-2344.jpg"
                            }}]
                            err = err
                            requests.post(config['webhook'], json = error)
                            erreur = True
                            print(f"{Spy.blanc}[{Spy.rouge}+{Spy.blanc}] Une erreur est survenue ! Le bot s'est arrété !")
                            start = False
                            break

                if erreur == False:
                    requests.post(config['webhook'], json = sucess)
                else:
                    input(f"{Spy.rouge} >>>> Appuyez sur entrer pour fermer le programme !")
                            
                                                                 
        
        
    


System.Clear()
System.Title("NFT | Bot | By : 2$.py#6495")
System.Size(140, 45)

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

Anime.Fade(Center.Center(banner), Colors.white_to_red  , Colorate.Vertical, enter=True)
RedditBot().run()
