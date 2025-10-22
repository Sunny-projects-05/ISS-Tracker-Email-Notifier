# ISS Tracker Email Notifier 🚀

This Python project automatically tracks the International Space Station (ISS) and sends you an email notification when it's passing overhead during nighttime.  

---

## 🌍 Features
- Uses Open Notify API for live ISS position tracking  
- Uses Sunrise–Sunset API to determine day/night time  
- Sends real-time email alerts using SMTP  
- Fully automated and customizable  

---

## 🧠 Skills Demonstrated
- Python scripting  
- API integration & JSON parsing  
- Conditional logic and scheduling  
- Email automation using `smtplib`  

---

## ⚙️ How It Works
1. The script fetches the current ISS coordinates using Open Notify API.  
2. It checks your location and determines if the ISS is within 5° of your position.  
3. It then fetches sunrise and sunset times to verify it's nighttime.  
4. If both conditions are true, it sends an email notification to you saying:  
   > "LOOK UP — The ISS is above you in the sky!"

---

## 🧩 Requirements
Make sure you have these Python libraries installed:

pip install requests

