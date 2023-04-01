import telebot,requests,pyodbc
from telebot import types
token = '5848680311:AAGYP4LSs9JJcrTPAFO-IrVsOS5w3B-8NIE'
bot = telebot.TeleBot (token)
def search_card(card, place):
  conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Users\Rushidhar1999\Desktop\s\\'+place+'.accdb;')
  print("started")
  cursor = conn.cursor()
  card = f"'{card}'" if card.startswith("0") else f"{card}"
  cursor.execute(f"SELECT * FROM PERSON WHERE FAM_NO = {card}")
  rows = cursor.fetchall()
  print("ended")
  column_names = [column[0] for column in cursor.description]
  data = []
  for row in rows:
        data_row = {}
        for column_name, value in zip(column_names, row):
            print(column_name)
            if column_name in ["P_FIRST", "P_FATHER", "P_GRAND", "FAM_NO","RC_NAME"]:
                data_row[column_name] = str(value).strip().replace("\x84", "")
            if column_name == "P_BIRTH":
                data_row["BIRTH"] = str(value).strip()
        data.append(data_row)
  cursor.close()
  conn.close()

  return data
def search_person(first_name, father_name, grand_name, birth, place):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Rushidhar1999\HP\Desktop\s\\'+place+'.accdb;')
    cursor = conn.cursor()
    sql_command = f"SELECT * FROM PERSON WHERE P_FIRST LIKE '{first_name}%' AND P_FATHER LIKE '{father_name}%' AND P_GRAND LIKE '{grand_name}%' AND P_BIRTH LIKE '{birth}%'"
    print(sql_command)
    cursor.execute(sql_command)
    rows = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data_row = {}
        print(row)
        for column_name, value in zip(column_names, row):
            if column_name in ["P_FIRST", "P_FATHER", "P_GRAND", "FAM_NO",'RC_NAEM']:
                data_row[column_name] = str(value).strip().replace("\x84", "")
            if column_name == 'RC_NAME':
              data_row['RC_NAME']= str(value).strip()
            if column_name == "P_BIRTH":
                data_row["BIRTH"] = str(value).strip()
        data.append(data_row)
    cursor.close()
    conn.close()
    return data
@bot.message_handler(commands = ['start'])
def phone(message):
 u = open('pay.txt').read()
 key = types.InlineKeyboardMarkup()
 key.row_width = 3
 a1 = types.InlineKeyboardButton(text="- اربيل .",callback_data="ar")
 a2 = types.InlineKeyboardButton(text="- الانبار .",callback_data="an")
 a3 = types.InlineKeyboardButton(text="- النجف .",callback_data="n")
 a4= types.InlineKeyboardButton(text="- بابل .",callback_data="ba")
 a5 = types.InlineKeyboardButton(text="- البصرة .",callback_data="bs")
 a6 = types.InlineKeyboardButton(text="- دهوك .",callback_data="dh")
 a7 = types.InlineKeyboardButton(text="- ديالى .",callback_data="dy")
 a8 = types.InlineKeyboardButton(text="- ذي قار .",callback_data="zy")
 a9 = types.InlineKeyboardButton(text="- سليمانية .",callback_data="sl")
 a10 = types.InlineKeyboardButton(text="- صلاح الدين .",callback_data="sa")
 a11 = types.InlineKeyboardButton(text="- القادسية .",callback_data="qa")
 a12 = types.InlineKeyboardButton(text="- كربلاء .",callback_data="kr")
 a13 = types.InlineKeyboardButton(text="- كركوك .",callback_data="ko")
 a14 = types.InlineKeyboardButton(text="- المثنى .",callback_data="mu")
 a15 = types.InlineKeyboardButton(text="- ميسان .",callback_data="mes")
 a16 = types.InlineKeyboardButton(text="- نينوى .",callback_data="ny")
 a17 = types.InlineKeyboardButton(text="- واسط .",callback_data="wa")
 a18 = types.InlineKeyboardButton(text="- بغداد .",callback_data="bag")
 key.add(a1,a2,a3,a4,a5,a18,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17)
 if str(message.from_user.id)== '5313741815':
    hk = types.InlineKeyboardMarkup()
    hk.row_width = 2
    ooi = open("pay.txt", "r")
    o = len(ooi.readlines())
    btn3 = types.InlineKeyboardButton(text=f"- عدد المفعلين {o} .",callback_data='nothing')
    btnn = types.InlineKeyboardButton(text="- تفعيل لشخص .",callback_data='tf')
    btn2 = types.InlineKeyboardButton(text="- ارسل التخزين .",callback_data="t5")
    hk.add(btn3,btn2,btnn)
    bot.reply_to(message,'- اهلا بك ايه المطور .',reply_markup=hk)
    bot.reply_to(message,'- اختر احد المحافظات واتبع التعليمات .',reply_markup=key)  
 elif str(message.from_user.id) in u:
    bot.reply_to(message,'- اختر احد المحافظات واتبع التعليمات .',reply_markup=key)
 else:
    huks = types.InlineKeyboardMarkup()
    huks.row_width = 1
    huka = types.InlineKeyboardButton(text="- Dev",url="t.me/V_L_Z")
    huks.add(huka)
    bot.reply_to(message,'- صديقي انت لم يتم التفعيل لك يرجى مراسلة المطور \n- @V_L_Z , @b_bb2',reply_markup=huks)
    imq = bot.forward_message(5313741815, message.chat.id, message.id)
    bot.reply_to(imq,f'- يحاول يبعبص ({message.from_user.id}) .')
@bot.callback_query_handler(func=lambda m:True)
def qu(call):
        u = open('pay.txt').read()
        if str(call.message.chat.id) in u or str(call.message.chat.id) == '5313741815':
         global place
         if call.data == 'ar':
          place = 'اربيل'
          h = bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == 'an':
          place = 'الانبار'
          h = bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == 'n':
          place = 'النجف الاشرف'
          h = bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "ba":
          place ='بابل'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "bs":
          place = 'بصرة'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "dh":
          place = 'دهوك'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "dy":
          place = 'ديالى'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "zy":
          place = 'ذي قار'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "sl":
          place = 'سليمانية'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "sa":
          place = 'صلاح الدين'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "qa":
          place = 'قادسية'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "kr":
          place = 'كربلاء المقدسة'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "ko":
          place = 'كركوك'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "mu":
          place = 'مثنى'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "mes":
          place = 'ميسان'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "ny":
          place =' نينوى'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == "wa":
          place = 'واسط'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if ':' in call.data:
             bot.send_message(call.message.chat.id,'انتظر ...')
             place, fam_no = call.data.split(":")
             card_info = search_card(fam_no, place)
             message = """"""
             for person in card_info:
                 name = person["P_FIRST"] + " " + person["P_FATHER"] + " " +  person["P_GRAND"] + "\nمواليد: " + person["BIRTH"][:4] + "\nرقم التموينية: " +person["FAM_NO"]
                 message += name+"\n\n-----\n\n"
             bot.send_message(call.message.chat.id, message)
         if call.data == "bag":
          place = 'بغداد'
          h=bot.send_message(call.message.chat.id,'- ارسل الاسم الثلاثي مع المواليد .')
          bot.register_next_step_handler(h,huks)
         if call.data == 'tf':
            g= bot.send_message(call.message.chat.id,'- ارسل الايدي الي تريد تفعله .')
            bot.register_next_step_handler(g,hukss)
         if call.data == 't5':
            bot.send_document(call.message.chat.id, open('pay.txt','rb'))
        else:
         bot.answer_callback_query(call.id, f"- لاتبعبص لم يتم التفعيل لك .", show_alert=True)
def hukss(message):
 bot.reply_to(message,'انتظر من فضلك ...')
 open('pay.txt','a').write(f'{message.text}\n')
 bot.send_message(message.chat.id,f'- تم التفعيل بنجاح ل{message.text}')
def huks(message):
 bot.reply_to(message,'انتظر  ...')
 n=message.text
 u = search_person(n.split(' ')[0],n.split(' ')[1],n.split(' ')[2],n.split(' ')[3],place)
 for person in u:
     try:
       V=persone['RC_NAME']
     except:V=None
     name = person["P_FIRST"] + " " + person["P_FATHER"] + " " +  person["P_GRAND"]
     print(person)
     all = f"""الاسم : {name}
المواليد : {person["BIRTH"][:4]}
رقم التموينية : {person["FAM_NO"]}
محل الولادة : {V}

            """
     fam_no = person["FAM_NO"]
     markup = telebot.types.InlineKeyboardMarkup()
     btn_get_info = telebot.types.InlineKeyboardButton("جلب عائلة الشخص", callback_data=f"{place}:{fam_no}")
     markup.add(btn_get_info)
     bot.send_message(message.chat.id, all, reply_markup=markup)
 bot.send_message(message.chat.id,"- تم البحث في كل القاعدة .")    
bot.infinity_polling()
