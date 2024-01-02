from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyMLContent(IContent):
    def format(self):
        return f"<myML>\n{self.text}\n<myML>"


class MyEncryptedContent(IContent):
    def format(self):
        result = []
        for el in self.text:
            if not el.isdigit():
                result.append('@')
            else:
                result.append('#')
        return ''.join(result)


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):
    def __init__(self, protocol, content_type):
        self.protocol = protocol
        self.content_type = content_type
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content.format())


email = Email('IM', 'MyML')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(MyEncryptedContent('Welcom3 to th3 qu4ntum r34lm'))
print(email)

