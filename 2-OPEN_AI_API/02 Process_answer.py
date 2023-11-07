# import re
input_file = "Alzheimer-OpenAI-answer.txt"
output_file = "Alzheimer-OpenAI-answer-PROCESSED.txt"


no_drug_words = ["no specific drug", "there is no mention of any specific drug or compound name", 
                 "there is no drug or compound name mentioned", "there is no mention of any specific drug or compound", 
                 "there is no drug or compound name", "the abstract does not provide any specific drug",
                 "no, this abstract does not mention any specific drug", 
                 "from this abstract, it is not possible", "there is no mention of any drug or compound",
                 "no, the ", "no, ", "no drug or compound name", "the abstract does not mention any specific drug or compound",
                 "there is no specific mention of any drug or compound",
                 "the abstract does not mention any drug or compound",
                 "is not mentioned", "not provide any specific drug or compound",
                 "not explicitly mentioned", "the abstract does not mention any specific drug or compound",
                 ]

#number of no drug info abstract
count = 0
i = 0
with open(input_file, "r") as f:
    lines = f.readlines()
    with open(output_file, "w") as ff:
        while i < len(lines):
        # while i < 30:
            #lấy ra 1 dòng
            line = lines[i].lower()

            #xét những dòng là gạch đầu dòng thì ghi vào
            if line.startswith("- "):
                ff.write(line)
            else:
                #xét những dòng là  số đầu dòng theo sau là dấu chấm thì ghi vào
                if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                    if line.find(" - ")>0:
                        # xét những dòng là title của bài báo
                        print(line)
                        #lấy dòng answer, kế sau dòng title
                        ans = lines[i+1]
                        #ban đầu xem như dòng đó chứa thông tin về drug
                        has_drug = True
                        #duyệt qua tất cả các cụm, chỉ cần có 1 cụm xuất hiện trong dòng thì xem như dòng đó ko có drug
                        for phrase in no_drug_words:
                            if phrase in ans:  # Simplified string search
                                has_drug = False
                                count+=1
                                break
                        if has_drug and ans!="\n":
                            ff.write(line)
                            ff.write(ans)
                    else:
                        ff.write(line)
            i+=1

print("no. of abstract with no drugs: ", count)