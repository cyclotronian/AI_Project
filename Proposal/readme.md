## Learning to Talk Like a Character

#### Problem Statement
Train a chatbot to copy the mannerism and style of a specific person, for example a famous TV character.

#### Summary
A brief survey of the existing work suggests that building a chatbot by training on a large dialogue corpus is at a relatively matured state (Resources [1][2][3][4], Previous Work [2][3][4]). However, instilling a personality into an AI chatbot is a fresh trend in the AI community. Recent papers try to encode personality to the AI bots by using persona-based models (Previous work [7]) and sequence-to-sequence models (Previous work [8]). However their performance tend to be short-sighted and tend to ignore information given in the past. A Deep Learning technique used in [5] incorporates future reward into their model and hence is able to foster a more sustained conversation in a dialogue simulation. We aim to combine the method used in [5] in order to enable the bot to sustain a longer, context based conversation. The first phase of our project would involve understanding/replicating the work of [5][7][8][9]. Next phase would be incorporating Deep RL techniques as mentioned in [5] into the models that extract personality from dialogues.

#### Previous work (Chronological)
1. [ELIZA - the first chatbot (1966)](http://web.stanford.edu/class/cs124/p36-weizenabaum.pdf)
2. [Using dialogue corpora to train a chatbot (2003)](https://www.researchgate.net/publication/267575064_Using_dialogue_corpora_to_train_a_chatbot)
3. [FAQBot for topic specific dialogues (2013)](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6572650)
4. [Survey Paper on previous Chatbots (2015)](https://pdfs.semanticscholar.org/cb4a/4f326c925009c6f575d1874dea056c731b63.pdf)
5. [Deep RL for Dialogue Generation (2016)](https://arxiv.org/pdf/1606.01541.pdf)
6. [Visual Dialog (2016)](https://arxiv.org/pdf/1611.08669.pdf)
7. [A persona based conversational model (2016)](https://arxiv.org/pdf/1603.06155.pdf)
8. [A neural chatbot with personality (2017)](http://web.stanford.edu/class/cs224n/reports/2761115.pdf)
9. [Adversarial Learning for Dialogue Generation (2017)](https://arxiv.org/pdf/1701.06547.pdf)
10. [Style Transfer to Natural Language (2017)](http://web.stanford.edu/class/cs224s/reports/Thaminda_Edirisooriya.pdf)*


#### Resources (In order of importance/relevance)
1. [WildML Chatbox Series](http://www.wildml.com/2016/04/deep-learning-for-chatbots-part-1-introduction/)
2. [ChatterBox](https://github.com/gunthercox/ChatterBot)
3. [Chatbot using Tensorflow](https://github.com/llSourcell/tensorflow_chatbot)
4. [Chatbot Preprocessing](https://github.com/shreyans29/thesemicolon/blob/master/chatbotPreprocessing.py), [Chatbot Training](https://github.com/shreyans29/thesemicolon/blob/master/chatbotlstmtrain.py) and [Chatbot Chat](https://github.com/shreyans29/thesemicolon/blob/master/chat.py)
5. [Deep RL for Chatbots - Article](https://venturebeat.com/2017/09/25/microsoft-dynamics-365-customers-get-service-chatbots-as-part-of-ai-push/)
6. [Stanford Course on Text Processing - Chatbot PPT](https://web.stanford.edu/class/cs124/lec/chatbot17.pdf) 
7. [Stanford PPT - Personality Detection (Slide 64 onwards)](http://web.stanford.edu/class/cs124/lec/emo2016.pdf)
8. Building a Chatbot - [Part 1](http://lauragelston.ghost.io/speakeasy-pt1/) and [Part 2](http://lauragelston.ghost.io/speakeasy-pt2/)
9. [Building AI Chatbot using Python/Tensorflow - PPT](https://speakerdeck.com/inureyes/building-ai-chat-bot-using-python-3-and-tensorflow)
10. [Building a 'Dadbot' - Article](http://www.npr.org/2017/07/23/538825555/creating-a-dadbot-to-talk-with-a-dead-father)


\* off-topic, however similar to the idea I mentioned about capturing style of a famous painter in a random image or composing a song in flavor of a famous composer - basically mimicking the personality from one artistic entity to another.

## RL related

#### Problem Statement
Use Reinforcement Learning to 'Learn' the heurustics of an A* search. 