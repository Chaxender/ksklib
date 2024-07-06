from nltk.chat.util import Chat, reflections

pairs = [
    ["Merhaba", ["Merhaba! Size nasıl yardımcı olabilirim?"]],
    ["Nasılsın?", ["İyiyim, teşekkür ederim. Siz nasılsınız?"]],
    ["(.*) hava (.*)", ["Hava durumu hakkında bilgim yok, ama size nasıl yardımcı olabilirim?"]],
    ["(.*) yaşındasın?", ["Ben bir bilgisayar programıyım, bu yüzden yaşım yok."]],
    ["(.*) hoşça kal", ["Görüşmek üzere! İyi günler."]],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
