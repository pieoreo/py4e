content = ("심리학자 오카다 타다시의 말을 빌려 가스라이팅 당하는 사람의 특징을 심리 조작의 비밀, 2012알려드리려고 해요.\n\n" +
" 진짜 이 문제로 끙끙 앓고 계신 분들이라면 팩트로 뚜까 맞을지도 모릅니다...ㅠㅠ \n\n" +
"1 지나치게 남에게 의존해요 주체적이지 못하며 지나칠 정도로 상대방을 배려하는 의존성 성격장애, 들어보셨나요?\n\n" +
"이 성격 장애를 겪는 사람들은 의견이 충돌하는 걸 두려워해 항상 맞추어 살아가려고만 하죠.\n\n"+
"또한 자신을 과소평가하기 때문에 누군가에게 의지하지 않으면 늘 불안해 합니다.\n\n" +
"언뜻 보면 이들은 상대와 조화를 이루고 타인의 의견을 존중하는 사람처럼 보입니다.\n\n" +
"결국 이들은 남에게 미움받을까 봐, 자신의 의사와는 반대되거나 손해를 보는 일까지도 마다하지 못해요.\n\n" +
"2 귀가 너무 얇아요. SINK INTO THE FLOOR. SINK.\n\n" +
"귀가 얇은 사람들은 자신에게 들어오는 정보의 옳고 그름을 비판할 능력이 떨어져 있어요.\n\n" +
"이들은 어떤 정보든 따지지도 않고 받아들입니다.\n\n" +
"필터라는 게 없는 이들은 그저 주어진 지시대로 행동하죠.\n\n" +
"타인의 말을 곧이곧대로 들어주는 탓에 스스로 의사결정도 잘하지 못해요.\n\n" +
"3 있는 그대로의 자신을 사랑하지 못해요. How could I be so stupid?\n\n" +
" 마음속에 높은 포부를 지니고 화려한 성공을 꿈꾸고 있지만,\n\n" +
"다른 한편으로는 열등감이 강하여있는 그대로의 자신을 사랑하지 못하는 사람입니다.\n\n" +
"즉, 불균형한 자기애를 가졌다는 거죠. 스스로 원하는 자신의 이상과 현실의 불균형이 클수록 자기애가 손상되곤 합니다.\n\n"+
"이렇게 균형을 잃은 사람은 아무리 똑똑하다고 해도 흐린 눈을 하게 됩니다.\n\n"+
"누가 봐도 수상한 사람조차 자신을 채워줄 사람으로 여기고 떠받듭니다.\n\n"+
"이 모든 게 손상된 자기애를 보상받기 위해서죠.\n\n"+
"4 스트레스를 많이 받아요 제아무리 강한 사람일지라도 좌절, 병, 이별, 경제적 어려움 등으로 마음이 고달플 때는 가스라이팅에 취약해집니다.\n\n"+
"현재의 스트레스뿐 아니라 스트레스를 제때 해소하지 못하고 과거의 스트레스까지 영향을 끼치기도 하는데요.\n\n"+
"쌓이게 되면 불안감이 심해지고 의지할 사람을 찾게 됩니다.\n\n"+
"5 의지할 사람이 없어요 주변에 전혀 기댈 사람이 없으면 내게 다가오는 상대를 똑똑하게 살피지 못한 채 의지하기 쉽답니다.\n\n"+
"이렇게 외로운 사람들은 가스라이팅 하는 사람에게 제일 쉬운 먹잇감이죠.\n\n"+
"근처에 이들을 적극적으로 도와줄 사람도 없는데다, 외로워 하지마. 내가 있잖아! 하면서 살살 꼬시면 낚일게 뻔하거든요.\n")

file = open("Be careful of the fact bombing! The characteristics that people who get gaslighted.txt", "w+")
file.write(str(content))
file.write("\n저자 : 연애의과학 박상예 에디터\n\n")
file.write("참고문헌 :오타다 히카시 심리 조작의 비밀")
file.close()

file = open("Be careful of the fact bombing! The characteristics that people who get gaslighted.txt", "r")
print(file.read())

search_word_count = input('Let us find some word: ')

file = open("Be careful of the fact bombing! The characteristics that people who get gaslighted.txt" , "r")

read_data = file.read()

word_count = read_data.count(search_word_count)

print(f"The word ' {search_word_count}' appeared {word_count} times.")
