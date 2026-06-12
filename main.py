from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # 👈 これが新しく必要になります
import random # randomライブラリを追加

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    return omikuji_list[random.randrange(10)]


# webページ
@app.get("/index")
def index():
    html_content = """
   <!DOCTYPE html>
    <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <title>課題9-1 | ネットワークプログラミング</title>
            <style>
                body {
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    background-color: #f4f7f6;
                    color: #333;
                    text-align: center;
                    padding: 50px 20px;
                }
                .container {
                    background-color: #ffffff;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #2c3e50;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                }
                p {
                    font-size: 1.1rem;
                    line-height: 1.6;
                }
                .highlight {
                    background-color: #f1c40f;
                    padding: 2px 6px;
                    border-radius: 4px;
                    font-weight: bold;
                }
                .btn {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #3498db;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                }
                .btn:hover {
                    background-color: #2980b9;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌐 課題9-1：Webページ公開テスト</h1>
                <p>ネットワークプログラミングの課題用ページです。</p>
                
                <p>Pythonの <span class="highlight">FastAPI</span> でサーバーを構築し、<br>
                GitHub経由で <strong>Render</strong> へのデプロイに成功しました！</p>
                
                <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                
                <p>👇 さっき作ったおみくじ機能にもここから飛べます</p>
                <a href="/omikuji" class="btn">今日のおみくじを引く 🔮</a>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)