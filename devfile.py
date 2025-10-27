import subprocess

def ping_host(host):
    try:
        # ใช้คำสั่ง ping ตามระบบปฏิบัติการ
        command = ["ping", "-c", "1", host]  # สำหรับ macOS / Linux
        # ถ้าใช้ Windows ให้เปลี่ยนเป็น:
        # command = ["ping", "-n", "1", host]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print(f"✅ {host} ตอบกลับปกติ")
            return True
        else:
            print(f"❌ {host} ไม่ตอบกลับ")
            return False

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return False
    
def pong_host(host):
    pass

def pong_host1(host):
    pass

def pong_host2(host):
    pass

# ตัวอย่างการใช้งาน
ping_host("8.8.8.8")
