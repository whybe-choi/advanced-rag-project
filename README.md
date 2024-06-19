# Dr.KHU : 의료 상담 챗봇 🤖

<div align="center">
Advanced Dr.KHU using LlamaIndex 🦙

<img src="./images/demo.GIF" witdh="600" height="600">
</div>

## Introduction
아래의 이미지는 [Medium - Corca : LLM Multi Agent: Customer Service를 기깔나게 자동화하는 방법](https://medium.com/corca/llm-multi-agent-customer-service%EB%A5%BC-%EA%B8%B0%EA%B9%94%EB%82%98%EA%B2%8C-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-2eaec7654385)에서 발췌한 이미지입니다. 해당 이미지와 동일한 기능을 하도록 코드를 개선하고 있는 중입니다.

<div align="center">
<img src=https://miro.medium.com/v2/resize:fit:1400/format:webp/1*k5c7ke1cy3-DKe_Ylkp8mg.png widh="400" height="400">
</div>

> 1. Leader Agent가 Key Point Analyzer Agent에게 복잡한 질문을 간단한 여러 개의 Sub-question으로 나눠달라고 요청합니다.
> 2. Leader Agent가 Sub-question 목록을 받으면 각각의 Sub-question에 대하여 Question Answerer Agent을 생성하고 답해달라고 요청합니다.
> 3. 이때 Question Answerer Agent는 각 Sub-question에 필요한 정보를 Vector Store에서 찾아와서 이를 참고하여 답합니다.
> 4. Leader Agent는 각각의 Sub-Question에 대한 답을 합하여 사용자 질의에 대한 답을 생성하고, Reviewer Agent에게 검토해달라고 요청합니다.
> 5. Reviewer Agent는 Leader Agent로부터 전달받은 답변에 대한 피드백을 말합니다. Leader Agent는 그 피드백을 반영하여 최종 답변을 생성한 후 사용자에게 전달합니다.

## How to use
1. 가상환경 설정
```shell
git clone https://github.com/whybe-choi/advanced-rag-project.git
cd advanced-rag-project
python -m venv venv
source venv/bin/activate
```

2. playwright 설치
```shell
playwright install
```

3. 라이브러리 설치
```shell
pip install -r requirements.txt
```

4. 데이터 크롤링
```shell
python crawling_faq.py
```

5. ChromaDB 생성
```shell
python upload.py
```

6. `.env.example`을 `.env`로 바꾸고 `CO_API_KEY` 입력
```text
CO_API_KEY=your-api-key
```

7. streamlit 실행
```shell
streamlit run app.py
```