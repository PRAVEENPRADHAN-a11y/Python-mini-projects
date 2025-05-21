with open("story.txt","r") as f:
  story=f.read()
words=set()
st_of_the_w="<"
end_of_the_w=">"
word_st_idx=-1
for i,char in enumerate(story):
  if char==st_of_the_w:
    word_st_idx=i
  if char==end_of_the_w and word_st_idx!=-1:
    wd=story[word_st_idx:i+1]
    words.add(wd)
    word_st_idx=-1
answers={}
for word in words:
  answer=input(f"enter the answer for {word}  : ")
  answers[word]=answer
for word in words:
 story=story.replace(word,answers[word])
print (story)
