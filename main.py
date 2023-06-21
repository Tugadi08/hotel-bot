import logging

from aiogram import Bot, Dispatcher, executor, types
from button import*

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("""Assalomu aleykum.Bizning botimizga xush kelibsiz.Oldinga xarakatlanish uchun "OLDINGA" tugmasini bosing!👌""", reply_markup=oldinga_menu)


@dp.message_handler(commands=['deadlines'])
async def send_welcome(message: types.Message):
    await message.reply("""Hech qanday shartlarimiz yo'q🙃😉""", reply_markup=oldinga_menu)


@dp.message_handler(commands=['price'])
async def send_welcome(message: types.Message):
    await message.reply("""
    Hozirda bizda SKIDKA🥳🥳!!!
    Hamma mehmonxonalarimiz 800.000 UZS💸
    Shoshiling vaqti cheklangan➖🥲
    """, reply_markup=oldinga_menu)



@dp.message_handler(commands=['communication'])
async def send_welcome(message: types.Message):
    await message.reply("""@iz_Tashkenta bot bilan muammolaringiz bo'lsa shu lichkaga yozishingiz mumkin.Iljoi boricha yordam berishga harakat qilamiz✊💪""")


@dp.message_handler(commands=['examples'])
async def send_welcome(message: types.Message):
    await message.reply("""Mehmon xonalar informatsiyasidan misol""")
    await message.answer("""Diyora Hostel🤑""")
    await message.answer_photo("https://t.me/vd_uz_n1/25", caption="""Bog'ga ega Diyora Hostel Qŭyliqda joylashgan.Yotoqxonada xonalar stol bilan jihozlangan. Diyora Hostelda har bir xonada umumiy hammom va choyshab mavjud.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, turar joydan 4 km uzoqlikda joylashgan.""")
    await message.answer_location(41.26061485667236, 69.34528594371623)


@dp.callback_query_handler(text="gg")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Rayonni tanlang!😃", reply_markup=rayon_menu)

@dp.callback_query_handler(text="1")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Bektemirdagi mehmonxonalar🫡", reply_markup=bektemir_menu)


@dp.callback_query_handler(text="2")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Chilonzordagi mehmonxonalar🫡", reply_markup=chilonzor_menu)


@dp.callback_query_handler(text="3")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Miroboddagi mehmonxonalar🫡", reply_markup=mirobod_menu)


@dp.callback_query_handler(text="4")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Mirzo Ulug'bekdagi mehmonxonalar🫡", reply_markup=mirzo_ulugbek_menu)


@dp.callback_query_handler(text="5")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Olmazordagi mehmonxonalar🫡", reply_markup=olmazor_menu)


@dp.callback_query_handler(text="6")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Sergelidagi mehmonxonalar🫡", reply_markup=sergeli_menu)


@dp.callback_query_handler(text="7")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Shayxontohurdagi mehmonxonalar🫡", reply_markup=shayxontohur_menu)


@dp.callback_query_handler(text="8")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Yunusoboddagi mehmonxonalar🫡", reply_markup=yunusobod_menu)


@dp.callback_query_handler(text="9")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Yashnoboddagi mehmonxonalar🫡", reply_markup=yashnobod_menu)


@dp.callback_query_handler(text="10")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Uchtepadagi mehmonxonalar🫡", reply_markup=uchtepa_menu)


@dp.callback_query_handler(text="11")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Yakkasaroydagi mehmonxonalar🫡", reply_markup=yakkasaroy_menu)


@dp.callback_query_handler(text="12")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("Yangihaoytdagi mehmonxonalar🫡", reply_markup=yangihayot_menu)


@dp.callback_query_handler(text="13")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Diyora Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/25", caption="""Bog'ga ega Diyora Hostel Qŭyliqda joylashgan.Yotoqxonada xonalar stol bilan jihozlangan. Diyora Hostelda har bir xonada umumiy hammom va choyshab mavjud.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, turar joydan 4 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.26061485667236, 69.34528594371623)


@dp.callback_query_handler(text="14")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""RESIDENT HOTEL" MEHMONXONASI🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/22", caption="""RESIDENT HOTEL" MEHMONXONASI - Toshkent, O'zbekiston xaritadasida tashkilotning joylashuvi iloji boricha aniq ko'rsatilgan, xato 100 metrdan oshmaydi. Yaqin atrofda bir nechta tashkilotlar joylashgan: eng yaqin mo'ljal: "THE ROYAL MEZBON" MEHMONXONASI (0.03 km), shuningdek "SALON EXCLUSIVE" MEBEL SALONI (0.11 km) va USMON IBN MAZUN MASJIDI (0.14 km).""")
    await call.message.answer_location(41.267596241535834, 69.24831748875009)


@dp.callback_query_handler(text="15")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel shosh palace🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/27", caption="""Shosh saroyida Genius chegirmasini olishingiz mumkin! Bu mulkni tejash uchun hisobingizga kiring.Shosh Palace mehmonxonasi Toshkent shahrida joylashgan. Unda mavsumiy ochiq basseyn, bog' va mehmonxona bo'ylab bepul Wi-Fi mavjud. Mulk bepul shaxsiy avtoturargoh va frantsuz restoranini taklif etadi.""")
    await call.message.answer_location(41.293241611413286, 69.26637960551875)


@dp.callback_query_handler(text="16")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hayot hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/29", caption="""Hayot hosteli Toshkent shahrida, shahar markazi va vokzaldan 7 km uzoqlikda joylashgan. Bu bepul Wi-Fi va bepul mashinalar bilan jihozlangan konditsionerli xonalarni taklif etadi.Har bir xonada kabel kanallari bo'lgan televizor mavjud. Hayot hostelidagi boshqa imkoniyatlarga umumiy hammom, umumiy oshxona va ovqatlanish joyi kiradi.“Hayot” mehmonxonasida restoran joylashgan bo‘lib, u yotoqxonadan 50 metr uzoqlikda joylashgan hamkor dastur hisoblanadi.Xostelda 24 soat xizmat ko'rsatadigan resepsiyon va bagaj saqlash joyi mavjud.Toshkent xalqaro aeroporti 3 km uzoqlikda; qo'shimcha haq evaziga transport xizmati mavjud.""")
    await call.message.answer_location(41.24568822767874, 69.3148638752002)


@dp.callback_query_handler(text="17")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Ayva hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/30", caption="""“Ayva” mehmonxonasi sizga Toshkentdagi eng qulay va keng mehmon xonalarini, shuningdek, turli turdagi biznes uchrashuvlarini o‘tkazish, tadbirlarni tashkil etish va mehmonxonada mehmonlarni joylashtirish uchun barcha qulayliklarni taklif etadi. Mehmonxona aeroportdan 15 daqiqa, temir yo'l vokzalidan esa 10 daqiqalik masofada joylashgan...""")
    await call.message.answer_location(41.247951518403205, 69.30681983760024)


@dp.callback_query_handler(text="18")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""MR hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/32", caption="""Yotoqxonadagi xonalar yashash maydoni, sun'iy yo'ldosh kanallari bilan tekis ekranli televizor, seyf kassasi va dushli umumiy hammom bilan jihozlangan. Barcha birliklarda shkaf mavjud.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, MR hosteldan 9 km uzoqlikda.""")
    await call.message.answer_location(41.25719176717334, 69.20789706968739)


@dp.callback_query_handler(text="19")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""GREENWAY HOTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/35", caption="""GREENWAY HOTEL Toshkent shahrida joylashgan. Mehmonxonada 24 soatlik resepsiyon, transport xizmati, xona xizmati va bepul Wi-Fi mavjud.Mehmonxonada xonalar garderob bilan jihozlangan. GREENWAY HOTEL mehmonxonasining har bir xonasida choyshab va sochiq mavjud.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, turar joydan 7 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.307428100567115, 69.23517858986921)


@dp.callback_query_handler(text="20")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""SHUHRAT HOTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/37", caption="""Sizning xizmatingizda: qabulxona kechayu kunduz ishlaydi, xonada ovqat va ichimliklarga buyurtma berish, aeroportdan / aeroportga o'tkazish, avtoturargoh, Internetga kirish, qulay restoran.Xizmat ko'rsatish xodimlari rus tilida gaplashadi.""")
    await call.message.answer_location(41.28130230822939, 69.19675096152709)


@dp.callback_query_handler(text="21")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel Art Palace🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/40", caption="""Palace Tashkent mehmonxonasi Toshkent shahrida joylashgan. Mulkda bog ', umumiy dam olish xonasi, teras va bar mavjud. Mehmonxonada velosipedlarni bepul ijaraga olish mumkin. Imkoniyatlar orasida restoran, yopiq basseyn va fitnes markazi mavjud. Resepsiyon kuniga 24 soat ochiq va xona xizmati mavjud. Mehmonxonada valyuta ayirboshlash xizmati mavjud.Barcha konditsionerli xonalar muzlatgich, qahva mashinasi va sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. Dush, bepul hojatxona jihozlari va ish stoli ham mavjud. Har bir xonada seyf va bepul Wi-Fi mavjud. Ba'zi xonalar shahar manzarasini taqdim etadi. Barcha xonalarda sochiq va choyshablar mavjud.""")
    await call.message.answer_location(41.31189203784186, 69.31780559884542)


@dp.callback_query_handler(text="22")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Guesto Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/41", caption="""GUESTO HOSTELda Genius chegirmalariga ega bo'lishingiz mumkin! Bu mulkni tejash uchun hisobingizga kiring.GUESTO hosteli Toshkent shahrida joylashgan. Unda bog', umumiy dam olish xonasi va bepul Wi-Fi mavjud.Islom Karimov Toshkent xalqaro aeroporti 5 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.3001990540847, 69.26106893050101)


@dp.callback_query_handler(text="23")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Uzbekistan Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/42", caption="""Ushbu mehmonxona Toshkent markazidagi Amir Temur maydonidan atigi 100 metr uzoqlikda joylashgan. U sport zali, sauna va tekis ekranli televizor bilan jihozlangan konditsionerli xonalarni taklif etadi. Bepul avtoturargoh mavjud va hududda ajoyib transport aloqalari mavjud.Hotel Uzbekistan klassik tarzda jihozlangan xonalar va minibar bilan jihozlangan suitlarni taklif etadi. Ichki makonlar quyuq yog'och mebellar va oqlangan matolar bilan bezatilgan. Har bir hammomda sochlarini fen mashinasi mavjud.""")
    await call.message.answer_location(41.312775185856125, 69.28319232855132)


@dp.callback_query_handler(text="24")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Comfort Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/43", caption="""Comfort Hotel Tashkent mehmonxonasi Toshkent shahrida joylashgan bo'lib, bog'ga ega. Teras va bepul shaxsiy avtoturargohni taklif etadi. Bepul Wi-Fi mavjud.Mehmonxonaning barcha xonalari tekis ekranli televizor bilan jihozlangan. Bundan tashqari, oshxona mavjud. Maxsus hammom dush va fen bilan jihozlangan. Comfort Tashkent mehmonxonasining barcha xonalari konditsioner bilan jihozlangan. Mehmonlar umumiy hammomdan foydalanishlari mumkin.""")
    await call.message.answer_location(41.2850330717665, 69.26046085666972)


@dp.callback_query_handler(text="25")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Gallery Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/46", caption="""Gallery Hostel Toshkent shahrida joylashgan. Unda bog' va umumiy dam olish xonasi mavjud. Saytda bepul shaxsiy avtoturargoh mavjud. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.Har kuni ertalab bufet, kontinental va halol nonushta variantlari mavjud.24 soatlik resepsiyon xodimlari ingliz, fors, yapon va rus tillarida gaplashadi.""")
    await call.message.answer_location(41.29140263528017, 69.26640882747098)


@dp.callback_query_handler(text="26")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Safarova Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/47", caption="""Safarovning oilaviy yotoqxonasi Toshkent shahrida joylashgan. Unda umumiy dam olish xonasi, teras, bar va butun mulk bo'ylab bepul Wi-Fi mavjud. Aeroportga transport xizmati taqdim etiladi. Velosiped ijarasi do'koni mavjud.Ba'zi xonalarda muzlatgich, mikroto'lqinli pech va minibar bilan jihozlangan oshxona mavjud.Hostel mehmonlari kontinental nonushta qilishlari mumkin.Siz Safarov's Family Hostelda dart o'ynashingiz mumkin. Hudud piyoda yurish va velosipedda sayr qilish uchun mashhur.""")
    await call.message.answer_location(41.35552071392737, 69.38468055087985)


@dp.callback_query_handler(text="27")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""BLUE SKY HOTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/51", caption="""Qo‘shqo‘rg‘onda joylashgan Bluesky bog‘ va umumiy dam olish maskaniga ega. Bepul shaxsiy avtoturargoh mavjud va mehmonxona pullik aeroport xizmatini taklif qiladi.Mehmonxona mehmonlari Osiyo nonushtasidan bahramand bo'lishlari mumkin.Ingliz, fors va rus tillarida so'zlashadigan xodimlar bilan resepsiyonda kechayu kunduz ma'lumotlar mavjud.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, Bluesky dan 3 km uzoqlikda.""")
    await call.message.answer_location(41.27874598629179, 69.28532277041573)


@dp.callback_query_handler(text="28")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Sofiya Hotel Tashkent🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/52", caption="""Sofiya Tashkent” mehmonxonasi Toshkentning shimoliy-sharqiy qismida joylashgan. U bog ', bepul Wi-Fi va bepul shaxsiy avtoturargohni taklif etadi. Kechqurun ko'ngilochar dastur mavjud.Konditsionerli xonalar sun'iy yo'ldosh televideniesi va choy-qahva tayyorlash uchun jihozlar bilan jihozlangan. Hammomlarda fen va shippak mavjud.""")
    await call.message.answer_location(41.314936471009666, 69.33180722200163)


@dp.callback_query_handler(text="29")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Kamal Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/53", caption="""KAMAL mehmonxonasi Toshkent shahrida joylashgan. U konditsionerli xonalarni taklif etadi. Ushbu 1 yulduzli mehmonxonada 24 soat xizmat ko'rsatish bo'limi mavjud. Xona xizmati so'rov bo'yicha mavjud. Xohlovchilar oilaviy xonalarni bron qilishlari mumkin.Islom Karimov nomidagi Toshkent xalqaro aeroporti mehmonxonadan 12 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.3343211275041, 69.34876044045248)


@dp.callback_query_handler(text="30")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""The Top Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/54", caption="""Bog' va barbekyu jihozlari bilan jihozlangan The Top Hostel Toshkentda joylashgan. Qabulxona 24/7 ishlaydi. Imkoniyatlar umumiy oshxona va butun bo'ylab bepul Wi-Fi o'z ichiga oladi. Mehmonxona aeroportdan va aeroportgacha transport xizmatini taklif qiladi.Siz yotoqxonada stol tennisi o'ynashingiz mumkin. Bu hudud piyoda sayr qilish uchun mashhur.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, The Top Hosteldan 10 km uzoqlikda.""")
    await call.message.answer_location(41.326072968023816, 69.31995271289001)


@dp.callback_query_handler(text="31")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Asli Makon Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/55", caption="""Toshkentda joylashgan Asli Makon mehmonxonasida bar mavjud. Qabulxona 24/7 ishlaydi. Mehmonlar restoranga tashrif buyurishlari yoki ovqat va ichimliklar uchun xona xizmatiga buyurtma berishlari mumkin. Bepul Wi-Fi mavjud. Binoda bankomat mavjud. Konsyerj va valyuta ayirboshlash xizmatlari ko'rsatiladi.Konditsionerli xonalar shkaf, choynak, minibar, seyf, tekis ekranli televizor va dushli xususiy hammom bilan jihozlangan.Har kuni ertalab alakart va halol variantlari bilan birga bufet nonushtasi taqdim etiladi""")
    await call.message.answer_location(41.32795987916482, 69.3441490256166)


@dp.callback_query_handler(text="32")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""National Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/58", caption="""Milliy hostel Toshkent shahrida joylashgan bo'lib, umumiy dam olish xonasiga ega. Xonalar dush va fen bilan jihozlangan umumiy hammom bilan jihozlangan, yotoqxonaning ba'zi xonalarida esa teras mavjud.""")
    await call.message.answer_location(41.31655026910663, 69.30219516794274)


@dp.callback_query_handler(text="33")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Budget Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/59", caption="""Budget Hostelda Toshkentda bar, umumiy dam olish xonasi, bog' va teras mavjud. U 24 soatlik resepsiyon va umumiy oshxonani taklif etadi.Yotoqxonadagi barcha xonalar choynak bilan jihozlangan. Budjet yotoqxonasidagi xonalar konditsioner va stol bilan jihozlangan.Mehmonlar kontinental nonushta qilishlari mumkin.Qum Budget Hosteldan 18 km uzoqlikda joylashgan. Toshkent xalqaro aeroporti 11 km uzoqlikda joylashgan. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""")
    await call.message.answer_location(41.34754397505469, 69.21446414282036)


@dp.callback_query_handler(text="34")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel OK🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/607", caption="""OK mehmonxonasi Toshkent shahrida joylashgan. U 24 soatlik resepsiyon, butun mulk bo'ylab bepul Wi-Fi va xona xizmatini taklif etadi. Mehmonxona shahar manzarasida.Barcha xonalarda choynak bor. OK mehmonxonasining konditsionerli xonalari tekis ekranli televizor bilan jihozlangan.Islom Karimov nomidagi Toshkent xalqaro aeroporti 15 km masofada joylashgan.""")
    await call.message.answer_location(41.36318471158257, 69.18425119476674)


@dp.callback_query_handler(text="35")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""HostelPoint🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/61", caption="""HostelPoint Toshkent shahrida joylashgan. U konditsionerli xonalarni taklif etadi. Boshqa imkoniyatlarga umumiy oshxona, umumiy dam olish xonasi va butun mulk bo'ylab bepul Wi-Fi kiradi. Qabulxona 24/7 ishlaydi. Mehmonlar konsyerj xizmatlaridan va bagajni saqlashdan foydalanishlari mumkin.Barcha xonalarda choyshablar mavjud.Islom Karimov nomidagi Toshkent xalqaro aeroporti 11 km.""")
    await call.message.answer_location(41.34603886144716, 69.27723408143446)


@dp.callback_query_handler(text="36")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""PARADISE HOSTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/62", caption="""Toshkentda joylashgan Paradise Inn Hostel bog'ga ega. Imkoniyatlarga konsyerj xizmatlari, bolalar o'yin maydonchasi, umumiy dam olish xonasi va 24 soatlik resepsiyon kiradi. Mehmonxona transport xizmatlari va butun bo'ylab bepul Wi-Fi taklif qiladi.Konditsionerli xonalar dush kabinasi, ish stoli, mikroto'lqinli pech, muzlatgich, choynak va fen bilan jihozlangan. Yotoqxona xonalarida sochiq va choyshablar mavjud.Paradise inn'da siz mashina ijaraga olishingiz yoki hududda piyoda yurishingiz mumkin.""")
    await call.message.answer_location(41.31881368667223, 69.2749099660866)


@dp.callback_query_handler(text="37")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""MASKAN HOTEL""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/22", caption="""Oqtepa-Chig'atoyda joylashgan MASKAN HOTEL bog'i, terasi va restoraniga ega 4 yulduzli turar joyni taklif etadi. Ushbu 4 yulduzli mehmonxona xona xizmati va 24 soatlik resepsiyonni taklif etadi. Mehmonxonada oilaviy xonalar mavjud.Ushbu 4 yulduzli mehmonxonada stol tennisi o'ynashingiz mumkin.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, mehmonxonadan 10 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.345897089137395, 69.20969199863723)


@dp.callback_query_handler(text="38")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel Empire🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/64", caption="""U juda qulay joyda, katta ko'chaning yonida joylashgan, ammo ikkinchi qatorda, bu tufayli shovqinli emas. Booking.com orqali ikki kishilik xonani bron qildik. Biroq, xonada faqat bitta karavot borligi va u unchalik keng emasligi ma'lum bo'ldi.""")
    await call.message.answer_location(41.282423848242196, 69.2620963366734)


@dp.callback_query_handler(text="39")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Sulaymon hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/65", caption="""Sulaymon mehmon uyi Toshkent shahridagi konditsionerli turar joylarga ega.Mehmonxonada xonalar shkaf, tekis ekranli televizor, xususiy hammom, choyshab va sochiqlar bilan jihozlangan.Mehmonxonada har kuni ertalab alakart, osiyo yoki vegetarian nonushtasi mavjud.""")
    await call.message.answer_location(41.216044976716475, 69.21622299677412)


@dp.callback_query_handler(text="40")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Daniel HillI🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/66", caption="""Daniel Hill mehmonxonasi Toshkent shahrida joylashgan. Mehmonlar umumiy dam olish xonasi, teras, bar va suv sporti inshootlaridan foydalanishlari mumkin.""")
    await call.message.answer_location(41.2530688592442, 69.30563149491982)


@dp.callback_query_handler(text="41")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Atlantis Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/68", caption="""Atlantis mehmonxonasi Toshkent shahrida joylashgan. Mulk umumiy dam olish xonasi, suv parki va mavsumiy ochiq basseynni, shuningdek, bepul shaxsiy avtoturargohni taklif etadi. Bepul Wi-Fi mavjud.Mehmonxonadagi konditsionerli xonalar tekis ekranli televizor, ish stoli va seyf kassasi bilan jihozlangan. Dushli maxsus hammom mavjud. Ba'zi xonalarda mikroto'lqinli pech bilan jihozlangan oshxona mavjud. Atlantis mehmonxonasining xonalari sochiq va choyshablar bilan jihozlangan.""")
    await call.message.answer_location(41.21621318224051, 69.21970901212063)


@dp.callback_query_handler(text="42")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""South Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/69", caption="""Janubiy mehmonxona Toshkent shahrida joylashgan. Unda restoran, bar, teras va bog' mavjud. Resepsiyon kuniga 24 soat ochiq va xona xizmati mavjud. Mehmonlar uchun aeroport xizmati tashkil etilishi mumkin. Mehmonxonada bepul Wi-Fi mavjud.Xonalar konditsioner, sun'iy yo'ldosh kanallari bilan tekis ekranli televizor, minibar, choynak, ish stoli, bide va bepul hojatxona jihozlari bilan jihozlangan. Sochiq va choyshab bilan ta'minlangan.""")
    await call.message.answer_location(41.25806833666005, 69.2276244391032)


@dp.callback_query_handler(text="43")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Jules Verne Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/70", caption="""Umumiy dam olish xonasiga ega Jules Verne Hostel Toshkentda joylashgan. Mehmonxonada 24 soatlik resepsiyon va umumiy oshxona mavjud. Mehmonlar uchun aeroport xizmati tashkil etilishi mumkin. Bepul Wi-Fi mavjud.Umumiy hammom dush va fen bilan jihozlangan.Hostelda har kuni kontinental nonushta taqdim etiladi.Hostelda har kuni kontinental nonushta taqdim etiladi.""")
    await call.message.answer_location(41.334484298432535, 69.27131496608736)


@dp.callback_query_handler(text="44")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Palma🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/71", caption="""Mehmonlarga quyidagi xizmatlar taklif etiladi: xonada ovqat va ichimliklar buyurtma qilish, to'xtash joyi, qulay restoran.Mehmonxona xodimlari rus tilini yaxshi biladi.Palma to'rt kishilik, uch kishilik, ikki kishilik, bir kishilik, ikki kishilik yoki egizaklik kabi toifadagi jami 5 ta xonani turli narxlardagi turar joy variantlarini taklif etadi.Palma Toshkentning Olmazor tumani Farobiy 448 V manzilida joylashgan. Shahar markazidan 7,1 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.348524327100094, 69.16557162174188)


@dp.callback_query_handler(text="45")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Friday Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/72", caption="""Friday Hotel Toshkent shahrida joylashgan. U 24 soatlik resepsiyon, aeroport transferlari, xona xizmati va bepul Wi-Fi xizmatlarini taklif etadi.Mehmonxonaning har bir xonasida choynak mavjud. Friday Hotel mehmonxonasidagi xonalar shahar manzarasini taqdim etadi. Xususiy hammomda dush va bepul hojatxona jihozlari mavjud. Har bir xonada konditsioner va tekis ekranli televizor mavjud.Friday Hotel alakart nonushta taklif qiladi.Islom Karimov Toshkent xalqaro aeroporti 10 km masofada joylashgan.""")
    await call.message.answer_location(41.33909772324412, 69.2937406832904)


@dp.callback_query_handler(text="46")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Mulberry Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/73", caption="""3 yulduzli Mulberry mehmonxonasi Xoja Ahror Valiy masjidi yaqinida, Koʻkeldosh madrasasidan 5 daqiqalik masofada joylashgan. Qo'shimcha qulaylik uchun sayt ichida bepul to'xtash joyi mavjud.Mehmonxona Abdulla Murodjaev 17a dan 1,7 km dan kamroq masofada joylashgan. Chorsu metro bekati 300 metr masofada joylashgan. Mehmonlar mehmonxonadan bir necha daqiqalik masofada joylashgan O‘zbekiston Davlat amaliy san’at muzeyiga tashrif buyurishlari mumkin. "Hadra maydoni" avtobus bekati 5 daqiqalik piyoda.""")
    await call.message.answer_location(41.32524946960978, 69.24002890841363)


@dp.callback_query_handler(text="47")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""ART B&B HOTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/74", caption="""Hudud obodonlashtirilgan va obodonlashtirilgan. Internetga kirish ta'minlandi.Mehmonxona xodimlari turk, rus, ingliz tillarida gaplashadi.ART B&B Hostel — Toshkentdagi yotoqxona boʻlib, oʻz mehmonlarini Kichik Xalqa Yoʻli, X. Irgashev 80, Toshkent, Oʻzbekiston manzilida kutmoqda. Shahar markazi 4 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.30283959356487, 69.24030700585979)


@dp.callback_query_handler(text="48")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Eurolux Boutique🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/75", caption="""Eurolux Boutique-Hotel Toshkent shahrida joylashgan. Hududda bog' mavjud. Mehmonxonada Wi-Fi-dan bepul foydalanish mumkin va mehmonxonada bepul shaxsiy avtoturargoh mavjud.Mehmonxonaning har bir xonasi ish stoli bilan jihozlangan. Konditsionerli xonalar tekis ekranli televizor bilan jihozlangan. Xususiy hammomda dush va bepul hojatxona jihozlari mavjud. Ba'zi xonalarda balkon mavjud. Barcha xonalar muzlatgich bilan jihozlangan.Islom Karimov Toshkent xalqaro aeroporti 8 km masofada joylashgan.""")
    await call.message.answer_location(41.312120160406906, 69.30879367568971)


@dp.callback_query_handler(text="49")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel IRIS🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/76", caption="""IRIS mehmonxonasi Toshkent shahrida joylashgan. Saytda pullik shaxsiy avtoturargoh va bepul Wi-Fi mavjud.Mehmonxonadagi barcha xonalar sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. IRIS mehmonxonasining har bir xonasida konditsioner va ish stoli mavjud.Har kuni ertalab kontinental nonushta beriladi.Qabulxona xodimlari rus va ingliz tillarida gaplashadi va kunning istalgan vaqtida mehmonlarga yordam berishga tayyor.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, IRIS mehmonxonasidan 6 km uzoqlikda. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""")
    await call.message.answer_location(41.29449968889708, 69.33292451026838)


@dp.callback_query_handler(text="50")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Safarova Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/77", caption="""Safarovning oilaviy yotoqxonasi Toshkent shahrida joylashgan. Unda umumiy dam olish xonasi, teras, bar va butun mulk bo'ylab bepul Wi-Fi mavjud. Aeroportga transport xizmati taqdim etiladi. Velosiped ijarasi do'koni mavjud.Ba'zi xonalarda muzlatgich, mikroto'lqinli pech va minibar bilan jihozlangan oshxona mavjud.Hostel mehmonlari kontinental nonushta qilishlari mumkin.Siz Safarov's Family Hostelda dart o'ynashingiz mumkin. Hudud piyoda yurish va velosipedda sayr qilish uchun mashhur.Mehmonxonada dazmollash moslamalari, bepul shaxsiy avtoturargoh, biznes markazi va 24 soatlik resepsiyon mavjud.Islom Karimov Toshkent xalqaro aeroporti 3 km masofada joylashgan.""")
    await call.message.answer_location(41.28283294108688, 69.30435891212409)


@dp.callback_query_handler(text="51")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Khan Palace hostelI🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/78", caption="""Khan Palace mehmonxonasi Yakkasaroyda joylashgan. Mehmonxonada 24 soatlik resepsiyon, aeroport transferlari, umumiy dam olish xonasi va butun mulk bo'ylab bepul Wi-Fi mavjud.Mehmon xonalari konditsioner, kabel kanalli tekis ekranli televizor, muzlatgich, choynak, dush, bepul hojatxona jihozlari va stol bilan jihozlangan. Har bir xona seyf bilan jihozlangan, ba'zi xonalar esa balkon bilan jihozlangan. Birliklarga garderob kiradi.Mehmonxonada har kuni bufet nonushtasi mavjud.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, Khan Palace mehmonxonasidan 2 km uzoqlikda.""")
    await call.message.answer_location(41.27284440574145, 69.31148633334942)


@dp.callback_query_handler(text="52")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Harmony Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/79", caption="""Harmony Tashkent mehmonxonasi Toshkent shahrida joylashgan. Unda bar va butun bo'ylab bepul Wi-Fi mavjud. Mehmonlar mahalliy taomlarni taklif qiluvchi restoranga tashrif buyurishlari mumkin. Siz mashinangizni bepul shaxsiy avtoturargohda qoldirishingiz mumkin.Xonalar konditsioner bilan jihozlangan. Unda stol, choynak, minibar, seyf, tekis ekranli televizor va bidetli xususiy hammom mavjud. Harmony Tashkent mehmonxonasi xonalarida sochiq va choyshablar mavjud.Islom Karimov Toshkent xalqaro aeroporti 2 km masofada joylashgan. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""")
    await call.message.answer_location(41.266579883923995, 69.31523640636684)


@dp.callback_query_handler(text="53")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""BoloXona🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/80", caption="""Hostel BoloXona Toshkentda restoran, bar, umumiy dam olish maskani va bog'ga ega. Old stol 24/7 ochiq. Mehmonlar umumiy oshxona, bepul Wi-Fi va aeroportga transport xizmatidan foydalanishlari mumkin.Xonalarda shkaf mavjud. Mehmonlar umumiy hammomdan foydalanishlari mumkin. Terlik va choyshab bilan ta'minlangan.Har kuni ertalab alakart nonushta beriladi.Qum qishlogʻi 16 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.28378692009303, 69.17890981212419)


@dp.callback_query_handler(text="54")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""RD HOSTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/81", caption="""RD-HOSTEL Toshkent shahrida joylashgan. Mulkning ba'zi xonalarida shahar manzarali balkon mavjud.Yotoqxonada har bir xona shkaf bilan jihozlangan.RD-HOSTEL mehmonlarga hududni aylanib chiqishda yordam berish uchun resepsiyonda qulay ma'lumotlarni taqdim etishi mumkin.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, turar joydan 15 km uzoqlikda.""")
    await call.message.answer_location(41.29440395892875, 69.17399351085913)


@dp.callback_query_handler(text="55")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Vatan Plaza Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/82", caption="""“Vatan Plaza” mehmonxonasi Toshkent shahrida joylashgan. Unda bar va yevropa taomlarini taklif qiluvchi restoran mavjud. Imkoniyatlar orasida 24 soatlik resepsiyon, umumiy dam olish xonasi va bepul Wi-Fi mavjud. Mehmonlar uchun aeroport xizmati tashkil etilishi mumkin.Har bir xonada shkaf mavjud. Konditsionerli xonalar tekis ekranli televizor va seyf bilan jihozlangan.Har kuni bufet, kontinental yoki to'liq ingliz/irland nonushtasi taqdim etiladi.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, Vatan Plaza mehmonxonasidan 13 km uzoqlikda.""")
    await call.message.answer_location(41.279400675199184, 69.1768098139803)


@dp.callback_query_handler(text="56")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Sanor Capsule Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/83", caption="""Mehmonlarga taqdim etiladigan xizmatlar: bog ', aeroportdan / aeroportga o'tkazish, avtoulovlar uchun to'xtash joyi, tungi klub, oshxona, yo'lda tushlik qilish, malakali bolalar parvarishi, tennis korti, old stol kechayu kunduz ochiq.Chet ellik mehmonlar uchun turk, rus, ingliz tillarini biladigan xodimlar mavjud.Hostel SANOR Capsule Hotel Toshkent shahrida, Mirzo Ulug‘bek shoh ko‘chasi 73-uyda, markazdan 7,1 km uzoqlikda joylashgan. Ushbu mulk sport bilan shug'ullanish uchun javob beradi.""")
    await call.message.answer_location(41.33229782031418, 69.33199404096324)


@dp.callback_query_handler(text="57")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""AKA Hostel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/84", caption="""Yakkasaroyda joylashgan AKA Hostel umumiy zal va bepul Wi-Fi-ni taklif etadi.Yotoqxonadagi barcha xonalar dushli umumiy hammomni o'z ichiga oladi.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, AKA Hosteldan 8 km uzoqlikda.""")
    await call.message.answer_location(41.28291013569229, 69.2259690458522)


@dp.callback_query_handler(text="58")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Panarams Hotel Tashkent🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/85", caption="""Radisson Individuals dasturida ishtirok etuvchi Panarams Tashkent – ​​Toshkent shahrida joylashgan 4 yulduzli mehmonxona. U teras, restoran, bar, umumiy dam olish xonasi, bepul Wi-Fi va xususiy hammom bilan jihozlangan konditsioner xonalar taklif etadi. Mehmonlar yopiq basseyn, fitness markazi va saunaga ega spa va sog'lomlashtirish markazidan foydalanishlari mumkin. Bepul velosiped ijarasi taqdim etiladi.Standart qulayliklar qatoriga seyf va tekis ekranli televizor kiradi. Panarams Tashkentning barcha xonalarida sochiq va choyshablar mavjud.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, Panarams Tashkent mehmonxonasidan 8 km uzoqlikda. Mehmonxona aeroportga bepul transport xizmatini taklif qiladi.""")
    await call.message.answer_location(41.310757348708066, 69.31310642561571)


@dp.callback_query_handler(text="59")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""BEST GUESTHOUSE🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/86", caption="""BEST mehmon uyi Toshkent shahrida joylashgan. Saytda teras mavjud. Qabulxona 24/7 ishlaydi. Mehmonxonada umumiy oshxona mavjud. Mehmonlar valyuta ayirboshlash va xona xizmatidan foydalanishlari mumkin.Mehmonxonaning barcha xonalari shkaf va tekis ekranli televizor bilan jihozlangan. BEST Guesthouse mehmonxonasining har bir xonasi konditsioner va stol bilan jihozlangan.Islom Karimov Toshkent xalqaro aeroporti 5 km uzoqlikda joylashgan. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""")
    await call.message.answer_location(41.300787411688034, 69.25518631212502)


@dp.callback_query_handler(text="60")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Sevinch Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/87", caption="""“Sevinch” mehmonxonasi Oqtepa shahrida joylashgan. Bog', restoran va butun bo'ylab bepul Wi-Fi mavjud. Qabulxona 24/7 ishlaydi. Shuningdek, valyuta ayirboshlash shoxobchasi ham mavjud.Konditsionerli xonalar kabel kanallari bilan tekis ekranli televizor, ish stoli, mikroto'lqinli pech, choynak, shuningdek dush va bepul hojatxona jihozlari bilan jihozlangan. Maxsus hammom hammom, fen va shippak bilan jihozlangan. Sochiq va choyshab bilan ta'minlangan.Sevinch mehmonxonasida alakart yoki halol nonushta taklif etiladi.Islom Karimov Toshkent xalqaro aeroporti 5 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.28085508519233, 69.27032765259442)

@dp.callback_query_handler(text="61")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Orient Grand Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/88", caption="""Orient Grand mehmonxonasi Toshkent shahrida joylashgan. Mehmonxonada bankomat va restoran mavjud. Qabulxona 24/7 ishlaydi. So'rov bo'yicha aeroport transferlari va xona xizmati mavjud. Bepul Wi-Fi mavjud.Bu dush va bepul hojatxonalar bilan jihozlangan xususiy hammom, tekis ekranli televizor va konditsionerga ega. Ba'zi xonalarda yashash maydoni mavjud. Barcha xonalarda shkaf va choynak mavjud.Orient Grand mehmonxonasi mehmonlari bufet yoki kontinental nonushtadan bahramand bo'lishlari mumkin.Islom Karimov Toshkent xalqaro aeroporti 4 km masofada joylashgan.""")
    await call.message.answer_location(41.28729760096161, 69.24349114096098)


@dp.callback_query_handler(text="62")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Demure Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/89", caption="""Demure inn Toshkentda joylashgan bo'lib, bog' va terastaga ega. U 24 soatlik resepsiyon va bagajni saqlashni taklif etadi. Xona xizmati mavjud.Barcha xonalar konditsioner va sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. Choynak, dush, fen va ish stoli ham mavjud. Barcha xonalarda shkaf mavjud.Mehmonlar ertalab bufet, osiyo yoki halol nonushtani tanlashlari mumkin.Islom Karimov nomidagi Toshkent xalqaro aeroporti mehmonxonadan 9 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.28103476006766, 69.24179186979721)


@dp.callback_query_handler(text="63")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Yangi hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/90", caption="""Restoranga ega “Yangi” mehmonxonasi Yakkasaroyda joylashgan. Toshkent mehmonxonadan 3,2 milya, Qum esa 6 milya masofada joylashgan.""")
    await call.message.answer_location(41.27040010655858, 69.2521478353912)


@dp.callback_query_handler(text="64")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel Hon Saroy🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/91", caption="""Teras va saunaga ega Xon Saroy mehmonxonasi Toshkentda joylashgan. U bepul Wi-Fi va saytdagi bepul shaxsiy avtoturargohni taklif etadi.Barcha xonalar sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. Ba'zi xonalarda yashash maydoni mavjud. Boshqa qulayliklar orasida choynak mavjud. Dush va bide bilan jihozlangan maxsus hammom ham mavjud. Xonalarda xalat, shippak va bepul hojatxona jihozlari mavjud.Mehmonxona mehmonlari velosipedni bepul ijaraga olishlari mumkin. “Xon Saroy” mehmonxonasi Toshkent xalqaro aeroportidan 6 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.29130259679881, 69.26010746608516)


@dp.callback_query_handler(text="65")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""City Hotel 🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/97", caption="""CITY mehmonxonasi Toshkent shahrida joylashgan. Unda bog' va bar mavjud. Bepul Wi-Fi mavjud. Maxsus to'xtash joylari qo'shimcha haq evaziga mavjud.Bu konditsioner xonada kabel kanallari bilan tekis ekranli televizor, minibar, choynak, stol, dush va bepul hojatxona jihozlari mavjud. Maxsus hammom hammom, fen va shippak bilan jihozlangan. Barcha xonalar sochiq va choyshablar bilan jihozlangan.Islom Karimov nomidagi Toshkent xalqaro aeroporti 3 km.""")
    await call.message.answer_location(41.285413017316245, 69.25594140451717)



@dp.callback_query_handler(text="66")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Hotel Palace🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/92", caption="""Palace Tashkent mehmonxonasi Toshkent shahrida joylashgan. Mulkda bog ', umumiy dam olish xonasi, teras va bar mavjud. Mehmonxonada velosipedlarni bepul ijaraga olish mumkin. Imkoniyatlar orasida restoran, yopiq basseyn va fitnes markazi mavjud. Resepsiyon kuniga 24 soat ochiq va xona xizmati mavjud. Mehmonxonada valyuta ayirboshlash xizmati mavjud.Barcha konditsionerli xonalar muzlatgich, qahva mashinasi va sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. Dush, bepul hojatxona jihozlari va ish stoli ham mavjud. Har bir xonada seyf va bepul Wi-Fi mavjud. Ba'zi xonalar shahar manzarasini taqdim etadi. Barcha xonalarda sochiq va choyshablar mavjud.Islom Karimov Toshkent xalqaro aeroporti 9 km masofada joylashgan.""")
    await call.message.answer_location(41.31115787374183, 69.31838578917957)


@dp.callback_query_handler(text="67")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""UNIQUE HOTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/93", caption="""UNIQUE mehmonxonasi Chilonzor aholi punktida joylashgan. Mehmonlar umumiy dam olish xonasi, yopiq basseyn, hamam, teras va bog'dan foydalanishlari mumkin. Resepsiyon 24/7 ochiq; bepul Wi-Fi mavjud.Har bir konditsioner xonada shkaf, ish stoli, muzlatgich va tekis ekranli televizor mavjud. UNIQUE mehmonxonasining ba'zi xonalarida balkon ham mavjud.Mehmonlar har kuni ertalab kontinental, halol yoki bufet nonushtasidan birini tanlashlari mumkin.Boshqa narsalar qatorida, UNIQUE Hotel spa markazini taklif etadi. Chilonzor va uning atrofida sayr qilish va ochiq havoda sayr qilish uchun barcha sharoit yaratilgan.Islom Karimov nomidagi Toshkent xalqaro aeroporti 5 km masofada joylashgan.""")
    await call.message.answer_location(41.27887347880058, 69.23926468143098)


@dp.callback_query_handler(text="68")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""Taht Hotel🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/94", caption="""Taxt mehmonxonasi Toshkent shahrida joylashgan. Teras mavjud va mehmonlar bepul Wi-Fi va bepul shaxsiy avtoturargohdan foydalanishlari mumkin.Mehmonxonada xonalar garderob bilan jihozlangan. Har bir xonada konditsioner, seyf kassasi va tekis ekranli televizor, Hotel Tahtning ayrim xonalarida esa balkon mavjud. Mehmonxonada har bir xonada choyshab va sochiqlar mavjud.Hotel Tahtda har kuni bufet nonushtasi mavjud.Ingliz, fors, frantsuz va rus tilida so'zlashadigan 24 soatlik resepsiyon xodimlari sizning turar joyingizni rejalashtirishda yordam beradi.Eng yaqin aeroport Islom Karimov nomidagi Toshkent xalqaro aeroporti, mehmonxonadan 11 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.342788894904764, 69.2570011256174)


@dp.callback_query_handler(text="69")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""CITY VIEW HOSTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/95", caption="""Mehmonlar uchun quyidagi xizmatlar mavjud: yaxshi ishlangan bog ', to'xtash joyi.Bu yerda biz har doim chet ellik sayyohlarni qabul qilishdan xursandmiz, xodimlar rus va ingliz tillarini biladi.“City View Hostel” mehmonxonasi Toshkent shahridagi “Tafakkur koʻchasi” 45-uyda joylashgan. Shahar markazi 2,7 km uzoqlikda joylashgan. Bu joy oilaviy dam olish va chang'i dam olish uchun ideal.""")
    await call.message.answer_location(41.29373975175906, 69.25978468885701)


@dp.callback_query_handler(text="70")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""THE ELEMENTS HOTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/96", caption="""THE ELEMENTS Toshkent shahrida joylashgan. Unda fitnes markazi, bog‘, teras va restoran mavjud. Qo'shimcha haq evaziga aeroportga transport xizmati taklif qilinishi mumkin. Bepul Wi-Fi mavjud.Konditsionerli xonalar ish stoli, choynak, muzlatgich, seyf, tekis ekranli televizor va dushli xususiy hammom bilan jihozlangan. Shkaf ham mavjud.THE ELEMENTSda har kuni ertalab bufet nonushtasi taqdim etiladi.Qabulxona 24/7 ishlaydi. Biznes markaz xizmatlari ko'rsatiladi. Saytda bepul shaxsiy avtoturargoh mavjud.Islom Karimov Toshkent xalqaro aeroporti 12 km uzoqlikda joylashgan.""")
    await call.message.answer_location(41.36151177576237, 69.2896420832915)


@dp.callback_query_handler(text="71")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""VELARA HOTEL🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/98", caption="""VELARA mehmonxonasi Toshkent shahrida joylashgan. Unda fitness markazi, umumiy dam olish xonasi va restoran mavjud. Derazalari shaharga qaraydi. Bepul Wi-Fi va bepul shaxsiy avtoturargoh mavjud.Har bir xonada dush, konditsioner, tekis ekranli televizor va muzlatgichli maxsus hammom mavjud. Boshqa qulayliklar orasida minibar va choynak mavjud.Mehmonxonada qolish vaqtida mehmonlar yopiq basseyn, sauna va hammomga ega spa va sog'lomlashtirish markazidan foydalanishlari mumkin.Eng yaqin aeroport - Islom Karimov nomidagi Toshkent xalqaro aeroporti, VELARA mehmonxonasidan 12 km uzoqlikda. Qo'shimcha to'lov evaziga aeroportga transferni tashkil qilish mumkin.""")
    await call.message.answer_location(41.356102576733925, 69.28485209492516)


@dp.callback_query_handler(text="72")
async def send_welcome(call: types.CallbackQuery):
    await call.message.answer("""ROADSIDE HOTE🤑""")
    await call.message.answer_photo("https://t.me/vd_uz_n1/99", caption="""Barga ega Roadside by Khorrot Toshkentda joylashgan. Unda restoran, fitness markazi, sauna va yopiq basseyn mavjud. Mehmonlar terasta va bepul shaxsiy avtoturargohdan foydalanishadi. Bepul Wi-Fi mavjud.Dush, fen va bepul hojatxona jihozlari bilan jihozlangan maxsus hammom va yashash maydoni mavjud. Konditsionerli xonalar seyf va sun'iy yo'ldosh kanallari bilan tekis ekranli televizor bilan jihozlangan. Roadside by Khorrot mehmonxonasining ba'zi xonalarida balkon mavjud. Qulayliklarga choynak kiradi. Har bir xona uchun choyshab va sochiqlar mavjud.Resepsiyon xodimlari ingliz, koreys, rus va turk tillarida gaplashadi.Islom Karimov nomidagi Toshkent xalqaro aeroporti 12 km. Qo'shimcha haq evaziga aeroportga xizmat ko'rsatish mumkin.""")
    await call.message.answer_location(41.3347455452997, 69.31266126980002)




@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)