from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدأ استـخـراج الجـلسة", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجـوع 🔙", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "سـوࢪس السيد", url="https://t.me/syntral"
            )
        ],
        [
            InlineKeyboardButton("- كيـفـية اެݪاستـخـدام", callback_data="help"),
            InlineKeyboardButton("- حـول", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور", url="https://t.me/s_i_d")],
    ]

    START = """
مـࢪحبـًا عـزيـزي  {}
أنـا مـخـصـص لاسـتخـࢪاج اެݪجـلـسات
بـايـࢪوجࢪام أو تـيـࢪمـكس
للبـدء في الاسـتـخࢪاج اضغط بدأ استـخࢪاج اެݪجـلـسة
المطوࢪ  : @s_i_d
    """

    HELP = """
 **الأوامࢪ المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ࢪيبو البوت
/generate - لاستخࢪاج الجلسات 
/cancel - لإلغاء الاستخࢪاج 
/restart - لتࢪسيت اليوت
"""

    # About Message
    ABOUT = """
**حول البوت** 

مـࢪحبـًا عـزيـزي أنا هـنا لاسـتـخࢪاج الجـلـسات بـࢪمـجـة المطـوࢪ @s_i_d

قناة السوࢪس : [SOuRCe ALsiD](https://t.me/syntral)
لغة البـرمـجـة : [بـايروجرام](docs.pyrogram.org)
اللغة : [بايثون](www.python.org)
المـطـور : @s_i_d
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
سبحان الله وبحمده سبحان الله العضيم 🤍  
┏━━━━━━━━━━━━━━━━━┓
┣★ معلومات عن مطـوري . [✨](https://t.me/ujijs)
┣★ الـمطور : [اضغط هنا](https://t.me/s_i_d)
┣★ السـورس [SOuRCe ALsiD](https://t.me/Tepthon)
┗━━━━━━━━━━━━━━━━━┛
💞 
إذا كان لديك أي سؤال ، فࢪاسل » المطوࢪ » [المـطور] @s_i_d
   """
