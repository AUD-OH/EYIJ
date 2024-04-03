# # graph = {
# #     "Seoul": {"Wonju": 88, "Daejeon": 140, "Gwangju": 270, "Sokcho": 168},
# #     "Wonju": {"Seoul": 88, "Sokcho": 110, "Daejeon": 120, "Busan": 260},
# #     "Daejeon": {"Wonju": 120, "Seoul": 140, "Gwangju": 200, "Busan": 200},
# #     "Gwangju": {"Daejeon": 200, "Seoul": 270, "Busan": 200},
# #     "Busan": {"Gwangju": 200, "Daejeon": 200, "Wonju": 200, "Sokcho": 340},
# #     "Sokcho": {"Seoul": 168, "Wonju": 110, "Busan": 340},
# # }

# import random

# # 대화 내용 데이터
# conversation = {
#     "안녕": ["안녕하세요!", "안녕하세요. 반가워요!", "안녕하세요. 무엇을 도와드릴까요?"],
#     "날씨": ["오늘은 맑은 날씨입니다.", "비가 올 것 같아요.", "오늘은 추워요."],
#     "음식 추천": ["피자 어떠세요?", "짜장면 어떠신가요?", "치킨이 어울릴 것 같아요."],
#     "잠자러 가야겠어": ["잘 자요!", "굿나잇!", "좋은 꿈 꾸세요!"],
#     "기타": ["죄송해요, 잘 이해하지 못했어요.", "무슨 일인가요?", "다시 한번 말씀해주세요."]
# }

# def siri():
#     while True:
#         user_input = input("사용자: ")
#         if user_input == "끝":
#             print("시리: 대화를 종료합니다.")
#             break
#         response = conversation.get(user_input, conversation["기타"])
#         print("시리:", random.choice(response))

# # 시리 실행
# print("시리: 안녕하세요! 대화를 시작해봐요.")
# siri()


