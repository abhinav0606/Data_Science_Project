import pandas as pd
from Levenshtein import ratio
import colorama
colorama.init()
from colorama import Style,Back,Fore
df=pd.read_excel(r"C:\Users\abhin\Desktop\Projects\Data_Science_CustomasizePvtLtd\faqs.xlsx")
def getResults(questions, fn):
    def getResult(q):
        answer, score, prediction = fn(q)
        return([q, prediction, answer, score])

    return(pd.DataFrame(list(map(getResult, questions)), columns=["TOPIC", "Prediction", "INFO", "Score"]))
from Levenshtein import ratio
def getApproximateAnswer(q):
    max_score = 0
    answer = ""
    prediction = ""
    for idx, row in df.iterrows():
        score = ratio(row["TOPIC"], q)
        if score >= 0.8:  # I'm sure, stop here 
            return  row["INFO"], score, row["TOPIC"]
        elif score > max_score: # I'm unsure, continue
            max_score = score
            answer = row["INFO"]
            prediction = row["TOPIC"]

    # if max_score>=0.6:
    return answer, max_score, prediction
    # return "Sorry, I didn't get you.", max_score, prediction
def chat():
    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        x=input("")
        l=[]
        l.append(x)
        result=getResults(l,getApproximateAnswer)
        # print(result)
        r=result["INFO"][0]
        # print(result["Score"][0])
        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,r)
print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
chat()
# print(getResults(["Procedures covered in Day care activity?"], getApproximateAnswer)["INFO"][0])