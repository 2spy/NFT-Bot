import os
from config import mdp, webhookurl, metakey, goodmessage, clientid, clientsecret, pseudo #This is config file
try:
    import time, requests, praw, random #pip install requests, praw
except:
    os.system("pip install requests")
    os.system("pip install praw")
    os.system("cls")
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System #pip install pystyle
except:
    os.system("pip install pystyle")
    os.system("cls")
try:
    from colorama import init, Fore #pip install colorama
except:
    os.system("pip install colorama")
    os.system("cls")
    
init()
reddit = praw.Reddit(client_id = clientid,
                     client_secret = clientsecret,
                     user_agent = "<console:HAPPY:1.0>",
                     username = pseudo,
                     password= mdp) 
def input_cat(subreddit, nbr_giveaway):
    '''
    Entrer [>] rien -> Sortie [>] str(choix de l'utilisateur)
    [>] Demande la catégorie de l'utilisateur
    [>] Si catégorie invalide -> boucle
    [>] Si condition réunis alors on retourne le choix
    '''
    condition = True
    while condition:
        catego = str(input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Dans quel catégorie voulez-vous que le bot consulte les messages  (hot / new) >>> "))
        subcatego = ""
        if catego.lower() == "new":
            subcatego = subreddit.new(limit=nbr_giveaway)
            condition = False
            return subcatego, catego.lower()
        if catego.lower() == "hot":
            subcatego = subreddit.hot(limit=nbr_giveaway)
            condition = False
            return subcatego, catego.lower()
        print(f"{Fore.WHITE}[{Fore.GREEN}O{Fore.WHITE}] Choix introuvable reformulez la catégorie voulue !")


       
def stop():
    '''
    Entrer [>] rien -> Sortie [>] rien
    [>] Attends que l'utilisateur lise le message d'erreur
    [>] Puis qu'il appuie sur entrer !
    [>] Fin du programme !
    '''
    input(f"{Fore.WHITE}[{Fore.GREEN}O{Fore.WHITE}] Appuyez sur entrer pour fermer le programme !")
#################################################################
#                                                               #
#                                                               #
#                         BOT REDDIT                            #
#           DISCORD :    https://discord.gg/3JWKnxydHz          #
#################################################################        

def bot():
    '''
    Entrer [>] rien -> Sortie [>] rien
    [>] Envoie des commentaires remplissant les conditions du giveaway automatiquement !
    [>] Si il y a une erreur envoie une requête sur le webhook + print l'erreur
    [>] En cas de problème tout est formulé sur le PDF
    
    #Ceci est une version 1 du bot !
    #Merci de laisser le lien du discord pour me soutenir gratuitement :)
    #J'espère que vous gagnerez des NFT ou autre selon le subreddit
    #Une version Twitter et instagram arrive dans quelque semaine !
    #N'hésitez pas à partager le bot !
    '''
    
    
    System.Title("NFT | Bot | By : 2$.py#6495")
    emoj = ["🤞","🙏","❤️","💯","▶️","🔔","🆔","💸"] 
    
    
    try:
        commentd = reddit.comment("t3_qsj32h")
        commentd.upvote()
        commentd.reply(f"{metakey}")
    except Exception as err:
        if str(err) == f"received 403 HTTP response":
            print(f"{Fore.RED}---------------------------------\n{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Compte bannis de Reddit !")
        if str(err) == f"received 401 HTTP response":
            print(f"{Fore.RED}---------------------------------\n{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Les informations du compte ne sont pas valides vérifier les !")
        time.sleep(2)
        stop()
        return
    
    
    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Merci de votre contribution ! Bonne chance !")
    subreddit = reddit.subreddit("NFTsMarketplace")
    msg_posted = 0  
    
    nbr_giveaway = int(input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Nombre de giveaway sur lesquels vous voulez participer (conseillé : 200) :  "))
    if nbr_giveaway == "":
        nbr_giveaway = 200
    
    subcatego = input_cat(subreddit, nbr_giveaway) 

             


        
    while True:
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] C'est partit !")
        for submission in subcatego[0]:
            messg = random.choice(goodmessage)
            emj = random.choice(emoj)
            err = ""
            data = {
                "username" : "NFT Bot",
                "avatar_url" : "https://cdn.discordapp.com/avatars/755734583005282334/f50603ab57beb11b22be7500742aea6b.png?size=1024"
                }
            data["embeds"] = [
            {
                "description" : f"**Lien du post :** {submission.url}\n\n**Nom du post :** ``{submission.title}``\n\n**ID du post :** ``{submission.id}``\n\n**Commentaire :** ``{metakey} - {messg}``\n\n**Nombre de message envoyé :** ``{msg_posted}``\n\n**Catégorie :** ``{subcatego[1]}``\n\n**Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
                "title" : "[>] **Le bot a posté un commentaire !**",
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
                "description" : f"**Allez consulter votre compte opensea il se peut que des NFT vous sont envoyés !!**\n\n**Nombre de message posté :**  ``{msg_posted}``\n\n**Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
                "title" : "[>] **Le bot a fini d'envoyer les messages !**",
                "thumbnail" : {
                    "url" : f"https://cdn.discordapp.com/avatars/755734583005282334/f50603ab57beb11b22be7500742aea6b.png?size=1024"
                    }}]


            error = {
            "username" : "NFT Bot"
            }
            error["embeds"] = [
            {
                "description" : f"Allez consulter votre compte reddit il se peut que vous êtes rate limited ou que vôtre compte soit bannis de reddit ou du subreddit !\n\n**Nombre de message posté :**  ``{msg_posted}``\n\n```{err}```\n\n **Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
                "title" : "[>] **Le bot a rencontré une erreur !**",
                "thumbnail" : {
                    "url" : f"https://cdn.discordapp.com/avatars/755734583005282334/f50603ab57beb11b22be7500742aea6b.png?size=1024"
                    }}]


            msg_posted +=1
            
            try:
                with open("post_list.txt","r") as f:
                    postid = f.readline()
                if submission.id in postid:
                    print(f"{Fore.RED}---------------------------------\n{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] Le bot a déjà posté un commentaire sous se poste !")
                    time.sleep(5)
                else:
                    with open("post_list.txt","a+") as f:
                        f.write(submission.id+"\n")
                    submission.reply(f"""{emj} Metamask > {metakey} !
                                    {messg}""")
                    submission.upvote()
                    print(f"{Fore.RED}---------------------------------\n{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Le bot a posté un commentaire ! \n[{Fore.RED}>{Fore.WHITE}] ID du poste | {submission.id}\n[{Fore.RED}>{Fore.WHITE}] Commentaire | {metakey} - {messg}\n[{Fore.RED}>{Fore.WHITE}] Upvote | True\n[{Fore.RED}>{Fore.WHITE}] Webhook Posté | True")
                    result = requests.post(webhookurl, json = data)
                    System.Title(f"NFT | Bot | Nombre de message > {msg_posted}")
                    time.sleep(random.randint(20,40))
            
            except Exception as err:
                if str(err) == f"received 403 HTTP response":
                    print(f"{Fore.RED}---------------------------------\n{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Compte bannis de Reddit !")
                    err = "Compte bannis de reddit !"
                    error_requests = requests.post(webhookurl, json = error)
                    stop()
                    return
                    
                if str(err) == f"received 401 HTTP response":
                    print(f"{Fore.RED}---------------------------------\n{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Les informations du compte ne sont pas valides vérifier les !")
                    err = "Les informations du compte ne sont pas valides vérifier les !"
                    error_requests = requests.post(webhookurl, json = error)
                    stop()
                    return
        break       
    
    
    
    print(f"{Fore.GREEN} [>] Sucess !\n[>] Le bot reprendra tout à l'heure !")
    sucessfull = requests.post(webhookurl, json = sucess)
    
    
    time.sleep(60*60)
    bot()
        
        
        
        
        
            
#################################################################
#                                                               #
#                                                               #
#                            MAIN                               #
#                                                               #
#                                                               #
#################################################################        



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
            |  |  I LOVE NFT!    |  |  |     |         |      |
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

        ██████╗  ██████╗ ████████╗    ███╗   ██╗███████╗████████╗
        ██╔══██╗██╔═══██╗╚══██╔══╝    ████╗  ██║██╔════╝╚══██╔══╝
        ██████╔╝██║   ██║   ██║       ██╔██╗ ██║█████╗     ██║   
        ██╔══██╗██║   ██║   ██║       ██║╚██╗██║██╔══╝     ██║   
        ██████╔╝╚██████╔╝   ██║       ██║ ╚████║██║        ██║   
        ╚═════╝  ╚═════╝    ╚═╝       ╚═╝  ╚═══╝╚═╝        ╚═╝   
                                                         
"""[1:]

Anime.Fade(Center.Center(banner), Colors.yellow_to_red, Colorate.Vertical, enter=True)
bot()
