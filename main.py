import speedtest

Test = speedtest.Speedtest()
Down = Test.download()
Up = Test.upload()

print(f"Download Speed :{Down / 1024 / 1024:.2f} Mbit/s")
print(f"Upload Speed :{Up / 1024 / 1024:.2f} Mbit/s")

