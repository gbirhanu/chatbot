## Report on: OgeettiiBot: Medical Information Assistant bot for Afaan Oromo

## Language

## By

## Gemechu Brihanu Adeba (PI)

## Tafary Kababa Tolassa (Co-PI)

## This Research Report is submitted to the Research and Publication Director of

## Jimma Institute of Technology, Jimma University

## Jimma

## October, 2021

```
I
```

(^) I

# Abstract

The main aim of this research project is to develop a medical information assistant for Afaan
Oromoo users using a chatbot system. Chatbot system now a day is used for different purposes.
For example, they are used for flight booking, language learning, online shopping, Computer
system diagnosis and soon. The chatbot system gives users a natural way of conversation when
they use it. They can use Natural language question like “What is the best pesticide?”. Then The
system understands the question of the user and answers it from its knowledge bases. The
conversation will go on until user ends the conversation.

Chatbot system can be rule-based or corpus-based system. The corpus-based approach of chatbot
system usually need large data set of user’s real conversation possible conversation. Contrary to
our initial proposal we have implemented data-based Chat Bot in this work. The rational for this
change is first we have now a lot of medical information online through the boom of social
media. There are a lot of medical doctors online who share a lot of information about significant
amount of diseases. Second using machine learning algorithm conversation can be learnt from
small amount of data. In this work we have gathered data from known medical online
conversation, from Oromia health Bureau documents and from medical staff of Jimma university
through interview. We have created intents from the collected data and the intent pass-through
different NLP process like: tokenization, stemming and converted to bag of words (BoW). After
that we have trained pattern to response mapping using simple deep learning network with three
layers with ReLu activation. The chatbot is evaluated by user and users gives as good feedback.

Keyword: Deep Learn, Chatbot, Relu activation, Bag of words

```
II
```

(^) II

# Acknowledgement

First of all, I would like to give gratitude Jimma university to give me this opportunity, and fund
this research so that I can explore application of AI in health sector. During this work I have
consulted different health professionals, I would like to give them my greatest gratitude for their
help, suggestion, tipping improvement idea about the application. I also thanks some of my
colleague in Faculty of computing and informatics to give me valuable comments

```
III
```

(^) III

# Table of Contents

....................................................................................................................................................................... I
Abstract ......................................................................................................................................................... I
Acknowledgement ...................................................................................................................................... II
List of table and figure ............................................................................................................................. IV
Acronyms .................................................................................................................................................... V
1 Introduction ......................................................................................................................................... 1
1.1 Background ................................................................................................................................... 1
1.1.1 Chatbot Components ............................................................................................................. 2
1.2 Statement of the Problem .............................................................................................................. 3
2 Objectives of the Project..................................................................................................................... 4
2.1 General Objectives of the Project ................................................................................................. 4
2.2 Specific Objectives of the project ................................................................................................. 4
3 Literature review ................................................................................................................................ 4
3.1 AI based Conversational agents .................................................................................................... 4
3.2 Health care Chat bots .................................................................................................................... 5
4 Methodology ........................................................................................................................................ 6
4.1 Data Collection and intent creation ............................................................................................... 6
4.2 OgeettiiBot, Afaan Oromo health assistant chat bot ..................................................................... 6
4.3 Tokenization ................................................................................................................................. 7
4.4 Stemming ...................................................................................................................................... 7
4.5 Bag of word generation ................................................................................................................. 8
4.6 Training and evaluation ................................................................................................................ 8
4.6.1 Training ............................................................................................................................... 8
4.6.2 Evaluation ............................................................................................................................ 9
5 Result and discussion .......................................................................................................................... 9
6 Conclusion and Recommendations .................................................................................................. 11
References .................................................................................................................................................. 12

```
IV
```

(^) IV

# List of table and figure

Figure 1OgeettiiBot architecture ................................................................................................................... 7
Figure 2 Accuracy and loss curve of the training ......................................................................................... 9
Figure 3 Ogeettii bot User interfaces .......................................................................................................... 10

Table 1 training configuration ...................................................................................................................... 8

```
V
```

(^) V

# Acronyms

BoW --------------------------------------------------------- Bag of word

NLU ----------------------------------------------------------- Natural language understanding

NLP ----------------------------------------------------------- Natural language processing

IR ------------------------------------------------------------- Information retrieval

AI ------------------------------------------------------------- Artificial intelligence

ReLu --------------------------------------------------------- Rectified Linear Unit

# 1 Introduction

## 1.1 Background

Digital Information Assistant also known as a Chatbots are systems that can carry on extended
conversations with the goal of mimicking the unstructured conversational or ‘chats’
characteristic of human-human interaction [1]. When it is First started people use Chatbot system
for Entertainment purposes. For example, Microsoft’s XiaoIce system [ 2 ], which chats with
people on text messaging platforms, is just for entertaining purposes for lonely people. Yet
starting from the very first system, ELIZA [ 3 ], chatbots have also been used for practical
purposes, such as testing theories of psychological counseling. Now a days it is widely used in
businesses like flight booking, language learning, Information Retrieving (IR), and mostly in
assisting customer in online business [ 4 ]. As Information retrieval tool Chatbot system gives user
flexibility of asking a question in a natural language. Unlike the traditional IR system, the
response from such system is not the document which contains the information rather it is the
Information it self. For example, if user ask the system by saying “What is the best coffee in
Ethiopia?” the system will answer by displaying answer text like “The best coffee in Ethiopia is
Jimma Coffee.”. Conversation can goon if the user also asks for the price of Jimma Coffee. This
is what differs it from simple question answering.

When we come to health care, chatbots or health bots are intended to provide personalized health
assistance and therapy information to patients, provide relevant products and services to patients,
as well as suggest diagnoses and recommend treatments based on patient symptoms. Chatbots in
health care may have the potential to provide patients with access to immediate medical
information, recommend diagnoses at the first sign of illness, or connect patients with suitable
health care centers in their vicinity [ 9 , 10 ]. Theoretically, in some instances, chatbots may be
better suited to help patient needs than a human physician because they have no biological
gender, age, or race and elicit no bias toward patient demographics. Chatbots do not get tired,
fatigued, or sick, and they do not need to sleep; they are cost-effective to operate and can run 24
hours a day, which is especially useful for patients who may have medical concerns outside of
their doctor’s operating hours.

**1.1.1 Chatbot Components**
Even if the detail implementation or algorithm used in Chatbot system may differ from system to
system, most of the chatbot system have the following model [5].

1. Question Analysis: - This stage is primarily focused on extracting meaning from user
   question in natural language or determining the function of the text/sentence in user’s
   question (e.g. is this a question, suggestion, offer, or command). To extract meaning from
   user’s question text, the system will convert unstructured text written into a chatbot to
   structured grammatical data objects, which will be further processed by the system.
2. Response Generation: - Response generation is arguably the most central component of
   the chatbot architecture. As input, the Response Generator (RG) receives a structured
   representation of the user question. In most architecture of chatbot system, the response
   selector has access to three key components it will use to make its decision about what to
   respond to user:
   I. a knowledge database (Rules) / data corpus, which will differ in content based on
   implementation.
   II. a dialogue history corpus, which will only exist in more complex models, and
   III. an external data source, which provides the bot with intelligence (e.g. a dog is an
   animal).
3. Knowledge Base Creation
   In order for chatbot system to work as an intelligent information assistant there should be
   a knowledge base for it. They way data stored is depend on the type of method used for
   response generation. For example, if it is rule-based system, there will be collection of
   rules for the bot system to refer when it answers user question. If it is corpus based there
   will be data set from where the answer is generated either using machine learning
   technique or using Infor0mation Retrieval model depending on the type of the bot.
4. Dialogue manager
   The unique feature of dialogue system or Chatbot is that they respond to user in very
   human like conversation. For example, if the user asks for “What is the date of today?”
   the don’t just respond by saying “Nov, 10, 2019”. Instead the answer it like human by
   saying “the date of today is Nov, 10, 2019”. This kind of feature is handled by dialogue
   manager of the chatbots. Chatbot system uses language tricks to generate human like
   responses.

5. Intents: Most of modern Chat Bot system have intents as their source of information.
   The intents usually contain three main components: this are:
   I. Tag: Tag includes related speeches for example; greeting, goodbye any related
   speech
   II. Patterns: patterns represent user question type, for example for greeting user can
   say “akkam”., “jirtuu?” and soon.
   III. Responses: represents Chatbot system answers for a user question.
   {
   "intents": [
   {
   "tag": "nagaa",
   "patterns": [
   "Hi",
   "akkam",
   "akkam jirta",
   "Fayyaadha Mitii",
   "Hello",
   "Guyyaan Akkam"
   ],
   "responses": [
   "akkam!",
   "akkam, waan nu dubbisteef galatoomi",
   "yooyyaa, maal isin gargaarru",
   "Ashamaa, gaaffii fayyaa qabduu"
   ]
   },
   }

Here in this work we have developed intents from data we have gathered from different sources.

## 1.2 Statement of the Problem

Digital Information Assistant systems are become very common these days. Peoples use
computer application to buy and sell goods online without human intervention. Also, people can
get different information on how to use different tools from this digital assistant system.
Unfortunately for under resourced language like Afaan Oromoo it is difficult to get such
services. Afaan Oromo is among the most widely spoken and used Afro-Asiatic languages [6]. In
Ethiopia, it is an official and mass communication language of Oromia regional state, which is
the largest region in Ethiopia. Besides being an official working language of Oromia regional
state, Afaan Oromo is the instructional medium for primary and secondary schools throughout

the region. It is used by Oromo people, who are the largest ethnic group in Ethiopia, which
amounts to 34.4% of the total population [7]. As a result, there are large portion of our
population who want to get information in this language. Most of the population who speak this
language lives in ruler area, where it is difficult to get medical consultation or health guide. So,
in this work we have developed the Medical Information Assistant in local languages,
specifically in Afaan Oromoo Language.

# 2 Objectives of the Project

The following were general and specific objectives of the project;

## 2.1 General Objectives of the Project

The main objective of this project was to develop Intelligent Medical Information Assistant for
Afaan Oromo using chatbot system.

## 2.2 Specific Objectives of the project

In order to achieve the general objective of the project, we have executed the following specific
objectives.

```
➢ Literature was searched and reviewed of existing technologies and techniques pertaining
to the development of Chatbot System
➢ We designed question and answer pattern rule for Afaan Oromoo Text
➢ Applied natural language processing (like stemming) to extract meaning (key word
extraction) of user question.
➢ We designed Pattern matching algorithm to generate response for user question.
➢ We designed architecture for implementation of Medical Information Assistant for Afaan
Oromoo.
➢ We evaluated the system and released for public use online.
```

# 3 Literature review

## 3.1 AI based Conversational agents

Conversational agents or chatbots are computer software that tried to imitate natural conversation
with human users through images and written or spoken language [ 1 1]. It is the way we create
human to machine relationship. This concept is here from very beginning of chat to history. For

example, the first most successful chat bot is a rule-based chatbot which was designed to take on
the role of psychotherapist mimic a patient-centered Rogerian psychotherapy exchange [ 3 ].
Another successful Chat bot in health care was called PARRY, which tried to assist people with
mental health related problem [ 12 ]. While ELIZA played the role of the therapist, PARRY took
on the part of a schizophrenic patient. Even though ELIZA passed a restricted Turing Test a
machine intelligence test with the success criterion of whether a human can distinguish a
machine from a human during a conversation [ 13 ], it was a rule-based and pre-scripted software
program [ 14 ]. Similarly, other early forms of the then-called chatterbots such as Psyxpert, an
expert system for disease diagnosis support written in Prolog [ 15 ] or SESAM-DIABETE, an
expert system for diabetic patient education written in Lisp [ 16 ], followed a rule-based approach.
ALICE (Artificial Linguistic Internet Computer Entity), in 1995, was the first computer system
to use natural language processing for the interpretation of user input [ 17 ].

Basically, there are three forms of Chatbots: Rule-based (fixed rule) chatbot, Self-Learning and
Generative-based chatbots. Self-learning is also called AI-Based Chatbots (Martin 2018). Now a
days since the machine learning algorithms are very mature and dynamic most of chat bot exist
uses machine learning based dynamic Chat Bot.

The rule-based methods depend on a list of simple predefined queries and possible resultant
answers. It does not need any machine learning approach and language processing is not
mandatory. They are intended for simple queries and they may fail for more complicated
questions since they can’t produce their own responses. This form of chatbots has one-to-one
input and replies.

## 3.2 Health care Chat bots

In health care, AI-based conversational agents have demonstrated multiple benefits for disease
diagnosis, monitoring, or treatment support in the last two decades [ 18 ]. They are used as digital
interventions to deliver cost-efficient, scalable, and personalized medical support solutions that
can be delivered at any time and any place via web-based or mobile apps [ 18 ]. Research studies
have investigated a variety of AI-based conversational agents for different health care
applications such as providing information to breast cancer patients [ 19 ]; providing information
about sex, drugs, and alcohol to adolescents; self-anamnesis for therapy patients; assistance for
health coaching to promote a healthy lifestyle or smoking cessation.

Chat bots depends highly on natural language understanding; thus, they are very language
specific. Most of chat bot available are in English or other well-resourced languages. As far as
out knowledge there is no work attempted for Afaan Oromo Language based chatbot system. In
this work we provided a simple health assistant chat bot which have capability to understand
Afaan Oromo.

# 4 Methodology

Generally, Chatbot system can use two approaches [1]; the first one is rule-based system and the
second one is corpus based (machine learning). Corpus based approach needs a large amount of
conversational data so that it can retrieve answers from it or trained on it to generate appropriate
answer for user’s question. Afaan Oromoo is under resourced language, that means we don’t
have rich data set in this language. However due to social media there are a lot of health-related
information on social media and on different website from well-known doctors in Afaan Oromo,
this makes it easy to gather large amount of data. Due to this we have implemented this chat bot
using machine learning by training the data we scrapped from different on-line media.

## 4.1 Data Collection and intent creation

In order to create dialogue agent, we have to gather documents in the domain of our interest, that
is in medical sector. So, document related to health were collected from different areas like from
Oromia Health Bureau, Oromia Broadcasting Network Health related archive, blogs and well-
known social media page. Dialog agents uses intents, which is used as information source for
the chat bot system. Intents contains tag, pattern, and responses. Tag indicated types of
conversation, i.e., it tells the bot what type of conversation it is, is it greeting, or saying good by
or asking question and soon. On the other hand, pattern represents question patterns from user.
Finally, response represents different ways of answering to the user question. We have created

## intents which have around 500 different health related conversation type.

## 4.2 OgeettiiBot, Afaan Oromo health assistant chat bot

Our chat bot system which is called OgeettiiBot, was developed using only three layers of deep
neural networks. The over all architecture was depicted in the following figure 1. The intents

were first converted to bag of words, which is numerical (vectorized) representation of tokens
(words).

Figure 1 OgeettiiBot architecture

## 4.3 Tokenization

Tokenization is the process of splitting sentences in to tokens. Tokens in this case may not
always the same as word. Token is any semantically signifant part of a sentences. For example
the word “dureettii” can be tokenized in to “duree” + “tti” depending on the requirement of the
task we are accomplishing.

## 4.4 Stemming

Stemming is the process of reducing a word to its word stem that affixes to suffixes and prefixes
or to the roots of words known as a lemma. Stemming is important in natural language
understanding (NLU) and natural language processing (NLP).

Stemming is a part of linguistic studies in morphology and artificial intelligence (AI) information
retrieval and extraction. Stemming and AI knowledge extract meaningful information from vast
sources like big data or the Internet since additional forms of a word related to a subject may

need to be searched to get the best results. Stemming is also a part of queries and Internet search
engines. Stemming will be very help full to get the meaning of the word even if it has different
forms. For example, the word “deeman”, “deemte”, “deeme” have the same meaning even if it
appears in different format. So, using stemmer we can reduce them to their root word “deem”. In
this word we have implemented and used rule-based stemmer by Debela [ 20 ].

## 4.5 Bag of word generation

Bag of Words (BOW) is a method to extract features from text documents. These features can be
used for training machine learning algorithms. It creates a vocabulary of all the unique words
occurring in all the documents in the training set. In this work we have used the simplest form of
bag of word as depicted in figure 1. Here is one example of BoW representation used in our
implementation.

sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bog = [ 0 , 1 , 0 , 1 , 0 , 0 , 0]

## 4.6 Training and evaluation

**4.6.1 Training**
As depicted in figure 1 we have trained the intents of our chat bot. we have trained it on Pytorch
deep learning framework. For activation we have used Relu activation function. The following
table shows the configuration.

Table 1 training configuration

S.No Parameter Value

1 No epoch 2000

2 Batch size 8

3 Learning rate 0.

4 Input size (Same as the shape of our data)

5 Hidden size 8

6 Out put size (Same as the shape of our data)

7 Activation function Relu activation

8 Loss function Cross Entropy Loss

We have split the data in to training and validation data set to check the accuracy and loss of the
training data. Figure 2 depicts the accuracy and loss curve of the training.

Figure 2 Accuracy and loss curve of the training

4.6.2 Evaluation
Chat bot system are highly human dependent. There is no formula and techniques to evaluate
them automatically. So, we tried to show our colleagues and health professional. We have used
five people two of them without health background and three of them are health professional.
Almost all of them indicated that the bot is good enough for simple conversation. But for
complex and continuous conversation it needs improvement. We also believe that our bot needs
more data to perform well.

# 5 Result and discussion

OgeettiiBot is may be the first real conversational agent for Afaan Oromo. But it need
improvement to work well. In this work we tried to interview health professional to get
symptoms of common diseases so that our Bot give suggestion to the user when the user tells our
bot how they feel. It is obvious that any Artificial intelligence-based application can never
substitute human doctor, however, they can support in different ways both the physician as well
as the patients. For example, this application can be extended to help doctor during diagnosis.

Doctors can as the bot about the symptoms of some diseases and the bot can respond. Bot can
actually do a lot of things, it can be used in patient registration, record patient history, suggest
possible diagnosis to some diseases and soon. In this work we only focus on patient side of
things. But in the future, this can be extended to cover all the health system. The following figure
3 shows the user interface for our bot. This bot can easily integrate to any website

Figure 3 Ogeettii bot User interfaces

# 6 Conclusion and Recommendations

Chat bots now a days are preferred way of developing user interfaces, what we develop
traditionally as app, now can be provided as conversation. For example, traditionally for
registration we create registration form and user will fill those forms, but with the advancement
of chat bot system they can gather that information while having conversation. In this work we
have gathered around 30 different symptoms of diseases and suggestion based on the symptoms.
This may be not enough but the frame work we have created is extendable by adding data to it.

Based on the feedback we can from users, we come to conclude that such system is very user
friendly and peoples need to use them. Health information should be accessible to anybody, so
developing such application will help in making health information accessible with a lot of
people. Based on this we recommend the following as a future work: -

## ➢ Extending this application so that it can help not only the patients but also the doctor and

## any health professional.

## ➢ Gather more health information and clean the information so that the bot has wide range

## of conversational topics with valid knowledge.

## ➢ Add functionality to make this application health management system which can give

## health tip information, register patient, record their diagnosis history and soon.

# References

1. Daniel Djurafsky, James H. Martin (2006). Speech and Language Processing,
   Prentice-Hall, Inc
2. Microsoft (2014). [http://www.msxiaoice.com..](http://www.msxiaoice.com..)
3. Weizenbaum, J. (1966). ELIZA – A computer program for the study of natural
   language communication between man and machine. Communications of the ACM,
   9(1), 36– 45
4. Shawar, Bayan Abu. ( 2007 ) “Chatbots: Are They Really Useful.” Ldv Forum.
5. Jack Cahn ( 2017 ) “CHATBOT: Architecture, Design, & Development”, Senior
   Thesis (EAS499) University of Pennsylvania
6. Anteneh, Getachew and Ado, Derib. (2008). Language Policy in Ethiopia: History
   and Current Trends. Ethiopia Journal of Education and Science, 2(1), 37-62.
7. Alemayehu, W. (2005). Rule Based Syntactic Disambiguation Parser For Amharic
   Sentence. Master’s thesis, Addis Ababa University. Master’s thesis, Addis Ababa
   University, Addis Ababa, Ethiopia.
8. Hiroshi Yamaguchi, Maxim Mozgovoy, Anna Danielewicz-Betz (2018), “A
   Chatbot Based on AIML Rules Extracted from Twitter Dialogues”, Communication
   Papers of the Federated Conference on Computer Science and Information Systems
   pp. 37– 42 , ISSN 2300-5963 ACSIS, Vol. 17
9. Amato F, Marrone S, Moscato V, Piantadosi G, Picariello A, (2017) Sansone C.
   “Chatbots Meet eHealth: Automatizing Healthcare” , CEUR Workshop
   Proceedings..
10. Morris RR, Kouddous K, Kshirsagar R, Schueller SM. Towards an artificially
    empathic conversational agent for mental health applications: system design and
    user perceptions. J Med Internet Res. 2018 Jun 26;20(6)

11. Laranjo L, Dunn AG, Tong HL, Kocaballi AB, Chen J, Bashir R, et al.
    Conversational agents in healthcare: a systematic review. J Am Med Inform Assoc
    2018 Sep 01;25(9):1248- 1258
12. Colby KM. Artificial Paranoia: A Computer Simulation of Paranoid Processes.
    Oxford: Pergamon Press; Jan 1976.
13. Saygin A, Cicekli I, Akman V. Turing test: 50 years later. Minds Mach
    2000;10(4):463-518.
14. Epstein J, Klinkenberg W. From Eliza to Internet: a brief history of computerized
    assessment. Comput Human Behav 2001 May;17(3):295-314.
15. Overby MA. Psyxpert: an expert system prototype for aiding psychiatrists in the
    diagnosis of psychotic disorders. Comput Biol Med 1987;17(6):383- 393
16. Levy M, Ferrand P, Chirat V. SESAM-DIABETE, an expert system for insulin-
    requiring diabetic patient education. Comput Biomed Res 1989 Oct;22(5):442- 453.
17. Suta P, Lan X, Wu B, Mongkolnam P, Chan J. An overview of machine learning in
    chatbots. Int J Mech Engineer Robotics Res 2020;9(4):502-510.
18. Schachner T, Keller R, von Wangenheim F Artificial Intelligence-Based
    Conversational Agents for Chronic Conditions: Systematic Literature Review J
    Med Internet Res 2020;22(9):e20701 DOI: 10.2196/
19. Chaix B, Bibault J, Pienkowski A, Delamon G, Guillemassé A, Nectoux P, et al.
    When chatbots meet patients: one-year prospective study of conversations between
    patients with breast cancer and a chatbot. JMIR Cancer 2019 May 02;5(1):e
20. Tesfaye, Debela, and Ermias Abebe. "Designing a Rule Based Stemmer for Afaan
    Oromo Text." International journal of computational linguistics (IJCL) 1.2 (2010):
    1 - 11.
