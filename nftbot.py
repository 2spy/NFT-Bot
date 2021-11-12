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
    commentd = reddit.comment("t3_qsj32h")
    commentd.upvote()
    commentd.reply(f"{metakey}")
    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Merci de votre contribution ! Bonne chance !")
    subreddit = reddit.subreddit("NFTsMarketplace")
    msg_posted = 0
    nbr_giveaway = int(input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Nombre de giveaway sur lesquels vous voulez participer (conseillé : 200) :  "))
    
    if nbr_giveaway == "":
        nbr_giveaway = 200
        
    while True:
        print("ok")
        for submission in subreddit.hot(limit=nbr_giveaway):
            messg = random.choice(goodmessage)
            emj = random.choice(emoj)
            data = {
                "username" : "NFT Bot"
            }
            data["embeds"] = [
                {
                    "description" : f"**Lien du post :** {submission.url}\n\n**Nom du post :** ``{submission.title}``\n\n**ID du post :** ``{submission.id}``\n\n**Commentaire :** ``{metakey} - {messg}``\n\n**Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
                    "title" : "[>] **Le bot a posté un commentaire !**",
                    "thumbnail" : {
                        "url" : f"https://i.ibb.co/r6rhKS0/hack.png"
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
                    "description" : f"**Allez consulter votre compte reddit il se peut que vous êtes rate limited ou que vôtre compte soit bannis de reddit ou du subreddit !!**\n\n**Nombre de message posté :**  ``{msg_posted}``\n\n```Consultez le PDF afin de savoir ce que vous pouvez faire !```\n\n **Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
                    "title" : "[>] **Le bot a fini d'envoyer les messages !**",
                    "thumbnail" : {
                        "url" : f"https://cdn.discordapp.com/avatars/755734583005282334/f50603ab57beb11b22be7500742aea6b.png?size=1024"
                        }}]

            msg_posted +=1
            try:
                submission.reply(f"{emj} Metamask > {metakey}\n{messg}")
                submission.upvote()
                print(f"{Fore.RED}---------------------------------\n{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Le bot a posté un commentaire ! \n[{Fore.RED}>{Fore.WHITE}] ID du poste | {submission.id}\n[{Fore.RED}>{Fore.WHITE}] Commentaire | {metakey} - {messg}\n[{Fore.RED}>{Fore.WHITE}] Upvote | True\n[{Fore.RED}>{Fore.WHITE}] Webhook Posté | True")
                result = requests.post(webhookurl, json = data)
                System.Title(f"NFT | Bot | Nombre de message > {msg_posted}")
                time.sleep(random.randint(15,30))
            except:
                print(f"{Fore.RED}---------------------------------\n{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] RATE LIMITED ! or check your acmsg_posted if you are banned ?! En cas d'erreur rejoignez le discord !")
                error_requests = requests.post(webhookurl, json = error)
                time.sleep(60*60*60)
                
        print(f"{Fore.GREEN} Sucess !")
        sucessfull = requests.post(webhookurl, json = sucess)
        time.sleep(60*60*60)
            
#################################################################
#                                                               #
#                                                               #
#                            MAIN                               #
#                                                               #
#################################################################        
System.Clear()
System.Title("NFT | Bot | By : 2$.py#6495")
System.Size(140, 45)

banner = r"""
                        ╒════╕   
                        │    │   
                      └─┬────┬─┘ 
                        │    ├┐  
                        │☻ ☻ └│  
                        │ <  └┘  
                        │    │   
                        │└─┘ │   
                        │    │   
                        └──┘ │   
                          │  │   
                          │  │   


██████╗  ██████╗ ████████╗    ███╗   ██╗███████╗████████╗
██╔══██╗██╔═══██╗╚══██╔══╝    ████╗  ██║██╔════╝╚══██╔══╝
██████╔╝██║   ██║   ██║       ██╔██╗ ██║█████╗     ██║   
██╔══██╗██║   ██║   ██║       ██║╚██╗██║██╔══╝     ██║   
██████╔╝╚██████╔╝   ██║       ██║ ╚████║██║        ██║   
╚═════╝  ╚═════╝    ╚═╝       ╚═╝  ╚═══╝╚═╝        ╚═╝   
                                                         
"""[1:]

Anime.Fade(Center.Center(banner), Colors.red_to_white, Colorate.Vertical, enter=True) # Thanks to Billythegoat356
bot()