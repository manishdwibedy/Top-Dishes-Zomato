class Mention(object):
    mentionText = ""
    context = ""
    def mention(self, mentionText, context, index):
        self.mentionText = mentionText
        self.context = self.getReviewContext()
        self.index = index
    def getReviewContext(self):
        mentionEnd =  self.index + self.mentionText.len()



