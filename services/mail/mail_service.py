from fastapi_mail import FastMail,MessageSchema,ConnectionConfig,MessageType
from pydantic import EmailStr,BaseModel
from config import settings

from typing import List

class EmailSchema(BaseModel):
    email:List[EmailStr]

config = ConnectionConfig(
    MAIL_USERNAME="Rivo Official",
    MAIL_FROM=settings.EMAIL,
    MAIL_PASSWORD=settings.EMAIL_PASS,
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME=settings.COMPANY_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


async def send_welcome_email(name: str, email: EmailStr):
    html = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background-color:#f7f7f7; padding:20px;">
            <div style="max-width:600px; margin:auto; background:white; padding:30px; border-radius:10px;">
                
                <h2 style="color:#1a73e8;">Welcome to Rivo, {name}! 🏍️</h2>
                
                <p style="font-size:16px; color:#333;">
                    Thanks for joining <strong>Rivo</strong> — your smart and reliable bike ride partner.
                </p>

                <p style="font-size:16px; color:#333;">
                    With Rivo, you can book a bike rider anytime, anywhere and reach your destination 
                    quickly, safely, and affordably.
                </p>

                <h3 style="color:#222;">What you can do with Rivo:</h3>
                <ul style="font-size:15px; color:#555;">
                    <li>🏍️ Book nearby bike riders instantly</li>
                    <li>📍 Track your ride in real-time</li>
                    <li>💰 Enjoy affordable travel options</li>
                    <li>🛡️ Ride with verified partners</li>
                </ul>

                <p style="font-size:16px; color:#333;">
                    Ready for your first ride? Open the Rivo app and start exploring.
                </p>

                <div style="text-align:center; margin:30px 0;">
                    <a href="#" 
                       style="background:#1a73e8; color:white; padding:12px 25px; 
                       text-decoration:none; border-radius:6px; font-weight:bold;">
                       Book Your First Ride
                    </a>
                </div>

                <p style="font-size:14px; color:#777;">
                    Welcome aboard! We are excited to have you with us.
                </p>

                <p style="font-size:14px; color:#777;">
                    Team Rivo 🚀
                </p>

            </div>
        </body>
    </html>
    """

    message = MessageSchema(
        subject="Welcome to Rivo 🏍️",
        recipients=[email],
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(config)
    await fm.send_message(message)
    


async def send_password_reset_email(name: str, email: EmailStr, reset_link: str):
    html = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background-color:#f7f7f7; padding:20px;">
            <div style="max-width:600px; margin:auto; background:white; padding:30px; border-radius:10px;">
                
                <h2 style="color:#1a73e8;">Reset Your Rivo Password 🔐</h2>

                <p style="font-size:16px; color:#333;">
                    Hi <strong>{name}</strong>,
                </p>

                <p style="font-size:16px; color:#333;">
                    We received a request to reset your password for your Rivo account.
                    Click the button below to create a new password.
                </p>

                <div style="text-align:center; margin:30px 0;">
                    <a href="{reset_link}"
                       style="
                       background:#1a73e8;
                       color:white;
                       padding:14px 28px;
                       text-decoration:none;
                       border-radius:8px;
                       font-weight:bold;
                       display:inline-block;
                       ">
                       Reset Password
                    </a>
                </div>

                <p style="font-size:14px; color:#555;">
                    This password reset link will expire soon for your security.
                </p>

                <p style="font-size:14px; color:#555;">
                    If you did not request a password reset, you can safely ignore this email.
                    Your account will remain secure.
                </p>

                <hr style="border:none; border-top:1px solid #eee; margin:25px 0;">

                <p style="font-size:14px; color:#777;">
                    Ride safe and travel smart 🏍️
                </p>

                <p style="font-size:14px; color:#777;">
                    Team Rivo 🚀
                </p>

            </div>
        </body>
    </html>
    """

    message = MessageSchema(
        subject="Reset Your Rivo Password 🔐",
        recipients=[email],
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(config)
    await fm.send_message(message)
    
async def send_ride_completed_email(
    name: str,
    email: EmailStr,
    source: str,
    destination: str,
    rider_name: str,
    rider_phone: str,
    ride_time: str,
    distance: str,
    cost: str
):
    html = f"""
    <html>
        <body style="font-family: Arial, sans-serif; background-color:#f7f7f7; padding:20px;">
            <div style="max-width:600px; margin:auto; background:white; padding:30px; border-radius:12px;">
                
                <h2 style="color:#1a73e8;">
                    Ride Completed Successfully 🏍️
                </h2>

                <p style="font-size:16px; color:#333;">
                    Hi <strong>{name}</strong>,
                </p>

                <p style="font-size:16px; color:#333;">
                    Thank you for riding with <strong>Rivo</strong>.
                    Your trip has been completed successfully.
                </p>


                <div style="
                    background:#f8f9fa;
                    padding:20px;
                    border-radius:10px;
                    margin:25px 0;
                ">

                    <h3 style="color:#333; margin-top:0;">
                        Ride Details
                    </h3>

                    <p style="color:#555;">
                        📍 <strong>From:</strong> {source}
                    </p>

                    <p style="color:#555;">
                        🏁 <strong>To:</strong> {destination}
                    </p>

                    <p style="color:#555;">
                        🕒 <strong>Ride Time:</strong> {ride_time}
                    </p>

                    <p style="color:#555;">
                        🛣️ <strong>Distance:</strong> {distance} km
                    </p>

                </div>


                <div style="
                    background:#e8f5e9;
                    padding:20px;
                    border-radius:10px;
                    margin:20px 0;
                ">

                    <h3 style="color:#2e7d32; margin-top:0;">
                        Rider Details
                    </h3>

                    <p style="color:#555;">
                        🏍️ <strong>Rider:</strong> {rider_name}
                    </p>

                    <p style="color:#555;">
                        📞 <strong>Contact:</strong> {rider_phone}
                    </p>

                </div>


                <div style="
                    text-align:center;
                    background:#1a73e8;
                    color:white;
                    padding:20px;
                    border-radius:10px;
                    margin:25px 0;
                ">
                    <p style="margin:0; font-size:14px;">
                        Total Fare
                    </p>

                    <h1 style="margin:8px 0;">
                        ₹{cost}
                    </h1>
                </div>


                <p style="font-size:15px; color:#555;">
                    We hope you had a safe and comfortable ride.
                    Thank you for choosing Rivo for your daily journeys.
                </p>


                <div style="text-align:center; margin:30px 0;">
                    <a href="#"
                       style="
                       background:#111;
                       color:white;
                       padding:12px 25px;
                       text-decoration:none;
                       border-radius:6px;
                       font-weight:bold;
                       ">
                       Book Another Ride
                    </a>
                </div>


                <hr style="border:none; border-top:1px solid #eee;">

                <p style="font-size:13px; color:#777; text-align:center;">
                    Ride safe. Ride smart. 🏍️<br>
                    Team Rivo 🚀
                </p>

            </div>
        </body>
    </html>
    """

    message = MessageSchema(
        subject="Your Rivo Ride Receipt 🏍️",
        recipients=[email],
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(config)
    await fm.send_message(message)