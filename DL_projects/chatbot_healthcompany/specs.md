Chatbot pour un site fictif qui réalise divers produits selon 3 axes différents :
- L'aide au diagnostic,  *MedIAg*
- La génération de données synthétiques, *SyntheMedix*
- L'analyse prédictive pour les soins de santé, *ForecastMed*

L'entreprise aura 3 produits phares qu'elle proposera aux clients, en offrant la possibilité de les adapter en fonction des besoins.

Le chatbot proposera également au client de parler d'un projet plus spécifique, ne rentrant pas forcément dans les cas mentionnés ci-dessus, en le renvoyant vers un expert.

Voici plusieurs exemples de schéma de conversation attendus, couvrant l'intégralité des intents du chatbot :

**Exemple 1**:
*Flow : Accueil → Présentation des produits → Choix du produit 1 → Prise de rendez-vous*
*BOT* : Bonjour et bienvenue chez FictiveCompany ! Je suis là pour vous aider.  Nous proposons plusieurs solutions innovantes en santé. Nos services incluent :
L'aide au diagnostic
La génération de données synthétiques
L'analyse prédictive pour les soins de santé
Seriez-vous intéressée par l'un de ces produits ? Ou peut-être souhaitez-vous une solution plus personnalisée ?
*USER* : Parlez-moi de l'aide au diagnostic.
*BOT* : [Présentation produit 1]
Est-ce que cela correspond à vos besoins ?
*USER* : Oui, tout à fait.
*BOT* : Je suis ravi que cela vous intéresse ! Souhaitez-vous en savoir plus sur un autre produit ?
*USER* : Non.
*BOT* : Désirez-vous parler à un de nos experts pour discuter plus en détail de cette solution ?
*USER* : Oui, j'aimerais bien.
*BOT* : Super ! Pour organiser un rendez-vous, pourriez-vous me fournir votre adresse e-mail, s'il vous plaît ?
*USER* : julie@example.com
*BOT* : Merci. Un de nos experts vous contactera à l’adresse julie@example.com d’ici demain pour planifier un rendez-vous. À bientôt !


**Exemple 2**:
*Flow : Accueil → Exploration de plusieurs produits → Recommandation personnalisée*
*BOT* : Bonjour ! Bienvenue chez FictiveCompany. Je peux vous présenter nos produits en santé. Êtes-vous intéressé par :
L'aide au diagnostic
La génération de données synthétiques
L'analyse prédictive pour les soins de santé
*USER* : Dites-moi d'abord ce qu'est la génération de données synthétiques.
*BOT* : [Présentation produit 1]
Est-ce que cela correspond à ce que vous recherchez ?
*USER* : Pas exactement. Et l'analyse prédictive, c'est quoi ?
*BOT* : [Présentation produit 2]
Pensez-vous que cela pourrait vous être utile ?
*USER* : Peut-être, mais ce n'est pas ce que je recherche non plus.
*BOT* : Je comprends. D’après ce que vous m'avez dit, je pense que notre solution d’aide au diagnostic pourrait mieux correspondre à vos besoins. Elle permet d'assister les médecins avec des recommandations précises basées sur l’analyse des données médicales.
Souhaitez-vous en savoir plus à ce sujet ou discuter avec un expert ?
*USER* : Oui, j'aimerais bien.
*BOT* : Super ! Pour organiser un rendez-vous, pourriez-vous me fournir votre adresse e-mail, s'il vous plaît ?
*USER* : julie@example.com
*BOT* : Merci. Un de nos experts vous contactera à l’adresse julie@example.com d’ici demain pour planifier un rendez-vous. À bientôt !

**Exemple 3**:
*Flow : Accueil → Présentation d’un produit → Questions spécifiques de l'utilisateur → Fallback → Prise de contact humain*
*BOT* : Bonjour ! Je suis le chatbot de FictiveCompany. Que puis-je faire pour vous aujourd'hui ?
*USER* : Qu'est-ce que vous proposez ?
*BOT* : Nous avons trois solutions principales :
L'aide au diagnostic
La génération de données synthétiques
L'analyse prédictive pour les soins de santé
Lequel vous intéresse ?
*USER* : L'analyse prédictive, c'est pour quoi ?
*BOT* : [Présentation produit 1]
*USER* : Ça marche comment en cas de problème rénal ?
*BOT* : Je suis désolé, je n’ai pas suffisamment d'informations spécifiques sur les problèmes rénaux à ce stade. Souhaitez-vous que je vous mette en contact avec un expert pour plus de détails ?
*USER* : Oui, s'il vous plaît.
*BOT* : Merci. Pour cela, pourriez-vous me fournir votre adresse e-mail afin qu'un expert vous contacte ?
*USER* : user@example.com
*BOT* : Merci. Un expert vous contactera sous 24 heures à julie@example.com pour répondre à toutes vos questions.

INTENTS : 
- Default Welcome Intent
- Présenter produits
- Saisir l'intérêt 
- Saisir le désintérêt
- Complete presentation
- Fallback 
- Prise de RDV
- Saisir l'adresse mail / le numéro de téléphone (+ confirmation ?).

CONTEXTS : 
- Ongoing présentation
- Ongoing organisation rdv
- Interest capture
- Fallback presentation

BACKEND : 
- Récupérer l'intérêt de l'utilisateur après la présentation des produits
- Faire vérifier l'adresse mail / le numéro de téléphone
- Si l'utilisateur n'a manifesté d'intérêt pour aucun des produits, ne rien faire (pas demander les infos de contact). Proposer de parler d'un projet particulier ?
- Ajouter les infos de contact + les sujets d'intérêt à une BDD pour gérer la prise de rdv.

https://clement1103.github.io/frontend/
