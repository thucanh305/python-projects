from question import Question

question_prompts = [
    "What color are apples?\n (a) Reg/Green \n (b) Purple \n (c) Orange \n\n",
    "What color are bananas?\n (a) Teal\n(b) Magenta\n(c) Yellow \n\n",
    "What color are strawberries? \n (a) Yellow\n (b) Red \n (c) Blue \n\n"]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")]


def run_test(questionns) :
    score = 0
    for question in questionns :
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print ("You got " + str(score) + "/" + str(len(questionns)) +  " correct")
run_test(questions)
