# [个人队伍] EspilonCTF2026的Writeup

> **2026年3月11日12:00 ~ 2026年3月26日00:00**
>
> **比赛地址：[Espilon CTF](https://ctf.espilon.net/challenges)**
>
> **复现地址：[Espilon CTF](https://ctf.espilon.net/challenges)**

> # Espilon CTF 2026
>
> 主办方: Espilon
>
> CTF
>
> 赛事介绍
>
> # Espilon CTF 2026 比赛信息
>
> ## 比赛简介
>
> Espilon CTF 是一场专注于**硬件、IoT（物联网）与OT（操作技术）领域**的 Capture The Flag 竞赛。与传统 CTF 不同，本赛事不设 Web 漏洞利用和经典 Pwn 题目，而是聚焦于真实的嵌入式安全场景：**使用烙铁、逻辑分析仪、协议解码器和原始射频信号**。
>
> 比赛背景设定于动画《Serial Experiments Lain》的宇宙中，你将潜入圣米卡诊所医疗网络、探查田原综合实验室的 SCADA 系统，并穿越 Cyberia 的黑暗走廊——全部通过真实的工业和嵌入式协议进行。
>
> ## 核心信息速览
>
> | 项目             | 详细信息                                                     |
> | ---------------- | ------------------------------------------------------------ |
> | **比赛名称**     | Espilon CTF 2026                                             |
> | **比赛形式**     | Jeopardy（解题模式）                                         |
> | **参赛形式**     | **个人赛（Solo）**，无团队合作                               |
> | **资格赛时间**   | 2026年3月11日（星期三）12:00 UTC — 2026年3月26日（星期四）00:00 UTC（共15天） |
> | **决赛形式**     | 线下赛（若参赛人数足够）                                     |
> | **官方网址**     | https://ctf.espilon.net/                                     |
> | **CTFtime 权重** | 0.00（因赛期超过5天且为个人赛，不参与全球排名）              |
> | **主办方**       | Espilon                                                      |
>
> ## 比赛形式与赛程
>
> 比赛分为两个阶段：
>
> 1. **第一阶段：在线资格赛**
>    - 时长：**1周**（实际为期15天）
>    - 形式：个人独立解题。
>    - 内容：超过 **20个** 挑战，涵盖 **5大类别**。挑战涉及固件分析、硬件接口、IoT网络和工业协议等。
> 2. **第二阶段：线下决赛**
>    - 条件：如果参赛人数充足，将组织线下决赛。
>    - 形式：顶尖选手现场对决，基于真实场景的独特挑战，涉及分析、入侵、横向移动和系统理解。最终只寻找一个Flag。
>
> ## 所需硬件
>
> - **ESP32 开发板（必需）**：参加 **ESP类别** 挑战的选手，**必须自备一个 ESP32 开发板**（如基础的 DevKit v1 即可，价格约5欧元）。没有硬件将无法访问该类别的挑战。
> - **ESP32 上的挑战示例**：自定义固件烧录、UART/SPI/I²C 通信、GPIO信号分析、Wi-Fi & BLE攻击、ESP+云端混合场景、嵌入式配置逆向等。
> - **其他类别**：无需特定硬件。
>
> ## 挑战类别
>
> 比赛挑战聚焦于以下技术领域：
>
> - **硬件与物联网 (Hardware & IoT)**：固件分析、UART、SPI、I²C、JTAG、无线电、蓝牙（BLE）等。
> - **操作技术协议 (OT Protocols)**：Modbus、MQTT、CoAP、真实的SCADA（监控与数据采集系统）场景。
> - **ESP32 专项**：需要自备硬件，深入探索ESP32的各种攻击面。
> - **真实场景模拟**：所有挑战均复现自真实的渗透测试和审计案例，难度从中级到高级，强调技术实践而非猜测。
>
> ## 参赛人群建议
>
> - **网络安全专业学生**：绝佳的硬件黑客技术和IoT安全入门与实践机会。
> - **渗透测试人员与红队成员**：来自真实审计的固件、SCADA、工业协议场景，非常贴近实战。
> - **创客与黑客 (Makers & Hackers)**：如果你已有烙铁和逻辑分析仪，这些挑战正是为你设计的。
> - **混合技能团队 (个人赛，但可交流)**：虽然比赛是个人赛，但参赛者可以融合Web、逆向、硬件、密码学等多领域技能进行学习和交流。
>
> ## 赞助与合作
>
> 如有意赞助 Espilon CTF，请联系邮箱：`eun0us@proton.me`
>
> > **补充说明**：此比赛信息整理自 Espilon CTF 官方网站。奖金信息在官网中未明确提及，可能意味着本次比赛不设置现金奖励，或以荣誉、资格认证等作为奖励。建议关注官网以获取最新动态。



# Day0



# Day1

## hardware

### Serial Experimental 00

#### 题目信息

> ## Serial Experimental 00
>
> ### 188
>
> hardware uart serial lain easy
>
> 
>
> **Serial Experimental 00 -- Lain Maintenance Node**
>
> You gained access to a split UART debug interface from a WIRED-MED prototype.
>
> - TX (read): `tcp/<host>:1111`
> - RX (write): `tcp/<host>:2222`
>
> Investigate serial diagnostics, recover the maintenance token, then unlock the node.
>
> Format: `ESPILON{...}`
>
> 
>
>  
>
>  
>
> Running...
>
> | **TX (read)**  | [espilon.net 36930](javascript:void(0)) |
> | -------------- | --------------------------------------- |
> | **RX (write)** | [espilon.net 36931](javascript:void(0)) |

#### 解题过程

**查看题目**

```cmd
nc espilon.net 36931
help
whoami
diag.uart
diag.eeprom
diag.order
```

```cmd
nc espilon.net 36930
Serial Experimental 00
TX online. Use RX channel to send commands.
> Commands:
  help
  whoami
  diag.uart
  diag.eeprom
  diag.order
  unlock <token>

> node: serial-experimental-00
> [UART] boot trace restored
[UART] frag_a_hex=4c41494e
[UART] frag_c_hex=3030
[UART] note: hex => ASCII
> [EEPROM] page 0x13
[EEPROM] frag_b_xor_hex=4056415a525f
[EEPROM] xor_key=0x13
> [ORDER] token format: <A>-<B>-<C>
[ORDER] A from diag.uart frag_a_hex
[ORDER] B from diag.eeprom frag_b_xor_hex (decode XOR)
[ORDER] C from diag.uart frag_c_hex
```

**分析**

- **得到token为LAIN-SERIAL-00**

#### 题目答案

**最终命令**

```cmd
unlock LAIN-SERIAL-00
```

```cmd
> [OK] maintenance unlocked
FLAG: ESPILON{l41n_s3r14l_3xp_00}
```

**得到：ESPILON{l41n_s3r14l_3xp_00}**



### Glitch The Wired

#### 题目信息

> ## Glitch The Wired
>
> ### 100
>
> hardware glitching fault-injection secure-boot Medium-Hard
>
> 
>
> **Glitch The Wired — Secure Boot Bypass**
>
> A WIRED-MED secure boot module is exposed on the lab bench. You have access to the power rail and can inject voltage glitches.
>
> - Glitch Lab: `tcp/<host>:3700`
>
> Find the right timing to bypass signature verification and access the debug console.
>
> Format: `ESPILON{...}`

#### 解题过程

**测试连接**

```shell
nc espilon.net 41842
```

```shell
[WIRED-MED] Glitch Lab v1.0
[WIRED-MED] Target: Secure Boot Module
[WIRED-MED] Type 'help' for commands
```

```shell
help
```

```shell
[GLITCH LAB] WIRED-MED Fault Injection Interface
Commands:
  help          Show this help
  status        Show current glitch parameters
  observe       View boot sequence trace with cycle timings
  set_delay N   Set glitch delay (cycles before trigger)
  set_width N   Set glitch pulse width (cycles)
  arm           Arm the glitch module
  trigger       Fire the glitch and observe boot
  read_console  Read debug console (after successful glitch)
```

**分析**

- 故障机

#### 题目答案

**最终指令**

```shell
set_delay 3200
set_width 20
arm
trigger
read_console
```

```shell
[WIRED-MED DEBUG CONSOLE]
Firmware: v2.3-unsigned
Boot: INSECURE (sig_verify skipped)
Maintenance token: ESPILON{gl1tch_byp4ss_s3cur3_b00t}
[END]
```

**得到：ESPILON{gl1tch_byp4ss_s3cur3_b00t}**



# 队伍

## 名称

**菜鸟对对队**



## 口号

**对对对对对**



## 成员

### 队长

- **probie**



## 留言

### probie

- **暂无**



## 成果

### 排名

- **0 / 0**

### 解题

- **0 / 0**

### 分数

- **0 / 0**