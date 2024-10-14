import pyautogui, time

# jeda sebelum mengetik
time.sleep(5)

# buka file dan baca isinya
with open("isipesan.txt","r") as tulisan:
      lines = tulisan.readlines()

      # loop sesuai isi file
      for text in lines:
            pyautogui.typewrite(text.strip())
            pyautogui.press('enter')
            time.sleep(1)
