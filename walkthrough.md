# 🚀 SSH Brute-Force Detection Lab (Blue Team Walkthrough)

A lightweight, Docker-based hands-on lab designed to teach **SSH brute-force detection**, **log analysis**, and **basic blue-team investigation techniques**.

This project simulates:
- A **target server** running Ubuntu + SSH + Fail2Ban
- An **attacker container** using Hydra to perform a realistic brute-force attempt
- Log analysis that mirrors real SOC workflows

Everything here is lightweight, reproducible, and perfect for learning or showcasing blue-team skills on your GitHub profile.

---

# 🔵 1. **Lab Overview**
This setup helps you understand:
- What brute-force attacks look like in SSH logs
- How to identify patterns (frequency, repeated failures, attacker IP)
- How Fail2Ban reacts to attacks
- How to think like a SOC analyst using real evidence

This project focuses on **one username, many passwords** — the most common real-world brute-force pattern.

---

# 🔧 2. **Architecture**

### **Components**
- **Target container**: Ubuntu server with SSH and Fail2Ban
- **Attacker container**: Lightweight Alpine image with Hydra
- **Shared Docker network**: Isolated attack-and-defend environment

### **Why this design?**
- The target container generates authentic `auth.log` entries.
- The attacker container produces repeatable brute-force traffic.
- Fail2Ban gives insight into automated defensive responses.
- Logs are stored on the host for easy analysis.

---

# 🐳 3. **Docker Compose Setup**
Create a file called `docker-compose.yml`:

```yaml
version: "3.9"

services:
  target:
    container_name: ssh_target
    image: ubuntu:22.04
    command: bash -c "
      apt update &&
      apt install -y openssh-server fail2ban &&
      useradd -m admin &&
      echo 'admin:admin123' | chpasswd &&
      sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config &&
      mkdir -p /var/run/sshd &&
      service ssh start &&
      tail -f /var/log/auth.log
    "
    ports:
      - "2222:22"
    volumes:
      - ./logs:/var/log
    networks:
      - labnet

  attacker:
    container_name: hydra_attacker
    image: alpine:latest
    command: sh -c "
      apk update &&
      apk add hydra openssh-client &&
      tail -f /dev/null
    "
    networks:
      - labnet
    depends_on:
      - target
    volumes:
      - ./passwords.txt:/passwords.txt

networks:
  labnet:
    driver: bridge
```

---

# 📄 4. **Password List**
Create a file named **passwords.txt** in the same directory:

```
123456
password
admin
admin123
letmein
qwerty
```

Hydra will try these passwords against the `admin` user.

---

# ▶️ 5. **How to Run the Lab**

### **1. Start the environment**
```
docker compose up -d
```

### **2. Enter the attacker container**
```
docker exec -it hydra_attacker sh
```

### **3. Run Hydra brute-force attack**
```
hydra -l admin -P /passwords.txt ssh://target
```

### Expected behavior:
- Multiple failed SSH attempts
- Eventually, Hydra finds `admin123`
- Target logs all attempts
- Fail2Ban may block the attacking IP

---

# 🔍 6. **Log Analysis (Blue Team Section)**
Logs are stored locally in:
```
./logs/auth.log
```

### **What to look for:**

#### **1. Repeated failed attempts for the same user**
```
Failed password for admin from 172.20.0.10 port 50215 ssh2
```

#### **2. High-frequency attempts**
Attacks occur within seconds:
```
Failed password for admin ... 10:21:05
Failed password for admin ... 10:21:05
Failed password for admin ... 10:21:06
```

#### **3. Consistent source IP**
The attacker container maintains the same IP (e.g., 172.20.0.10).

#### **4. Successful brute-force login**
```
Accepted password for admin from 172.20.0.10 ssh2
```

#### **5. Fail2Ban ban event (if triggered)**
```
Ban 172.20.0.10
```

---

# 🛡️ 7. **Indicators of a Brute-Force Attack**
This lab teaches you key detection signals:

- Repeated failed logins in short bursts
- Same username targeted multiple times
- Same source IP for all attempts
- Attempts within milliseconds or seconds
- Final successful login after many failures
- Fail2Ban blocking the offending IP

These indicators reflect real-world SOC analysis.

---

# 🧠 8. **Blue Team Investigation Questions**
Use these to analyse your attack:

- How many failures occurred before success?
- What was the time gap between attempts?
- Did the attacker use password spraying or brute forcing?
- How did Fail2Ban respond?
- Would this attack be detectable in a SIEM?

You can include these answers in your write-up.

---

# 📌 9. **What You Learned**
By completing this lab, you gained practical experience with:

- SSH brute-force behavior
- Hydra attack patterns
- Authentication log interpretation
- Fail2Ban reactions
- Blue-team investigative reasoning

This project is a strong starting point for building detection engineering skills.

---

# 🌱 10. **Future Expansions**
You can upgrade this repo later with:
- Multi-user brute-force attacks (Mode B)
- Full brute-force (Mode C)
- SIEM integration (Wazuh, ELK, Splunk)
- Suricata or Zeek network detection
- Incident response timeline reconstruction

---

# 🏁 Final Notes
This walkthrough is intentionally simple, lightweight, and beginner-friendly while still giving you real blue-team value.

If you want help writing your GitHub description, repository structure, or diagrams, just ask!

