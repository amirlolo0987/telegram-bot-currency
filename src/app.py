import telebot
import base
import currency as cvt

bot = telebot.TeleBot(base.TOKEN)

print('bot created')

base_currency=''
target_currency=''

@bot.message_handler(commands=['start'])
def say_hello(message):#esm ekhtiary
    # print((message))
    bot.send_message(message.chat.id,'به ربات ما خوش امدید')

@bot.message_handler(commands=['help','contact'])
def show_help(message):
    bot.reply_to(message,'در صورت نیاز بخ پشتیبانی با شماره 061332 تماس بگیرید')

@bot.message_handler(commands=['news'])
def get_news(message):
    maerkup=telebot.types.InlineKeyboardMarkup()
    btn1=telebot.types.InlineKeyboardButton(text='اخبار ورزشی', url='https://varzesh3.com')
    btn2=telebot.types.InlineKeyboardButton(text='اخبار روز',url='https://tabnak.ir')
    maerkup.add(btn1,btn2)
    bot.send_message(message.chat.id,text='یکی از گزینه ها را انتخاب کنید',reply_markup=maerkup)


@bot.message_handler(commands=['menu'])
def show_menu(message):
    maerkup=telebot.types.ReplyKeyboardMarkup()
    btn1=telebot.types.KeyboardButton(text='تماس با ما')
    btn2=telebot.types.KeyboardButton(text='درباه ما')
    btn3=telebot.types.KeyboardButton(text='عضویت')
    btn4=telebot.types.KeyboardButton(text='بازگشت')


    maerkup.add(btn1,btn2,btn3,btn4)
    bot.send_message(message.chat.id,text='یکی از گزینه ها را انتخاب کنید',reply_markup=maerkup)

@bot.message_handler(commands=['convert'])
def exchange(message):
    msg=bot.send_message(message.chat.id,text='ارز مبدا را وارد کنید ')
    bot.register_next_step_handler(msg,get_base_currency)

def get_base_currency(message):
    global base_currency
    base_currency=message.text.upper()
    msg=bot.send_message(message.chat.id,text='ارز مقصد را وارد کنید')
    bot.register_next_step_handler(msg,get_target_currency)

def get_target_currency(message):
    global target_currency

    target_currency=message.text.upper()

    rate=cvt.exchange_rate(base_currency,target_currency)

    bot.send_message(message.chat.id,f'نرخ تبدیل ارز برابر است : {rate}')




@bot.message_handler(func=lambda message:True)
def show_message(message):
    if message.text == 'تماس با ما':
        phone='0923233'
        email='owwww@gmail.com'
        info=f'ایمیل : {email} - شماره تماس  : {phone}'
        bot.send_message(message.chat.id,info)
    elif message.text == 'درباه ما':
        bot.reply_to(message,"این یک ربات طراحی شده توسط من است")
    elif message.text == 'عضویت':
        pass
    elif message.text =='بازگشت':
        markup=telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,'بازگشت به صفحه چت',reply_markup=markup)

if __name__=='__main__':
    bot.infinity_polling()