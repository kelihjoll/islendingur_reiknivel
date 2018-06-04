
class Question(object):

    def __init__(self, question, type):
        self.question = question;
        self.type = type;

    choices = [];

# questions = [{
#     question: "First question",
#     type: "multiple_choice",
#     choices: ["Choice 1","Choice 2", "Choice 3"]
# }, {
#     question: "question nr 2",
#     type: "yes_no"
# }]