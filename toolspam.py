#Note: Yêu Cầu Thư Viện "pyautogui" để cài thư viện này các bạn vào cmd và chạy lệnh sau: "pip install pyautogui" (Các bạn bỏ ngoặc kép nha chỉ có pip install pyautogui thôi)
#Khai báo thư viện
import pyautogui, pyperclip, random, time
#Tên Tool
print("Tool Spam Inbox by Sơn v1.0")
#Nội dung cần spam
#.split( " || ") là ngăn cách cách thứ tự
noidung = input("Nhập nội dung cần spam: ").split(" || ")
solan = int(input("Nhập số lần Lặp Lại:  "))
delay = float(input("Nhập thời gian delay: "))

#Chuẩn bị chạy
print("Chuẩn bị")
#Đếm ngược 5 giây
for i in range(5,0,-1):
	print(i,end="...",flush='True')
	time.sleep(1)
#Bắt đầu chạy
print("Bắt đầu")

#SPAM
for i in range(solan):
	pyperclip.copy(random.choice(noidung))
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	time.sleep(delay)
	
#Bay Màu Prrrrrrrrrrrrrrr
