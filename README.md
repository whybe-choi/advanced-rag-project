# advanced-rag-project
Advanced Dr.KHU using llama-index 🦙

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

5. Chroma
```shell
python upload.py
```
