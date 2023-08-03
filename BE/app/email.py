from fastapi import APIRouter
import smtplib  # SMTP 사용을 위한 모듈
from apscheduler.schedulers.background import BackgroundScheduler
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈
import os
from datetime import datetime
from dotenv import load_dotenv

from database.database import SessionLocal
from database.query import read_all_emails

from app.generate import run

load_dotenv(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), ".env"))

email_router = APIRouter()
scheduler = BackgroundScheduler()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def send_email(mail):
    # smpt 서버와 연결
    gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
    gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
    smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)

    # 로그인
    my_account = "hn06038@gmail.com"
    my_password = os.environ["SMTP_PASSWORD"]
    smtp.login(my_account, my_password)
    
    # 메일을 받을 계정
    to_mail = mail
    
    # 메일 기본 정보 설정
    msg = MIMEMultipart()
    msg["Subject"] = datetime.now().strftime("[Genimate] %Y년%m월%d일 날씨")  # 메일 제목
    msg["From"] = my_account
    msg["To"] = to_mail
    
    # 메일 본문 내용
    html = f"""\
    <html>
        <body align="center">
            <div>
                <h2>Genimate</h2>
                <div style="font-family:Arial,sans-serif;font-size:18px;line-height:20px;color:#66758a;font-weight:bold;padding-top:34px">
                    <span style="color: #333333;">오늘의 날씨</span>
                    <span style="color:#dadff1">&nbsp;|&nbsp;</span>
                    {datetime.now().strftime('%Y년 %m월 %d일, %A')}
                </div>
                <hr>
                <h3>이미지를 보고 맞춰보세요!</h3>
                <img src="cid:image1" alt="Image 1">
                <p>위 이미지는 이메일 수신자마다 달라요!</p>
            </div>
        </body>
    </html>
    """

    html_part = MIMEText(html, "html")
    msg.attach(html_part)
    
    # 이미지 파일 추가
    image_name = os.path.join('images', sorted(os.listdir("images/"))[-1])
    with open(image_name, 'rb') as file:
        img = MIMEImage(file.read())
        img.add_header('Content-ID', '<image1>')
        msg.attach(img)
    
    # 받는 메일 유효성 검사 거친 후 메일 전송
    smtp.sendmail(my_account, to_mail, msg.as_string())
 
    # smtp 서버 연결 해제
    smtp.quit()

def send_emails():
    db = next(get_db())
    emails = read_all_emails(db)
    for email in emails:
        print(email.email)
        run()
        send_email(email.email)

@email_router.on_event("startup")
async def send_email_scheduler():
    scheduler.add_job(send_emails, 'cron', hour=7, minute=0, timezone="Asia/Seoul")
    scheduler.start()

@email_router.on_event("shutdown")
async def shutdown_scheduler():
    scheduler.shutdown()