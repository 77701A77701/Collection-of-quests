import sqlite3

def close():
    global connect, cursor
    connect.commit()
    cursor.close()
    connect.close()

def open():
    global connect, cursor
    connect = sqlite3.connect("text.db")
    cursor = connect.cursor()

def create():

    open()

    cursor.execute('''CREATE TABLE IF NOT EXISTS victorini
                        (id INTEGER PRIMARY KEY, name VARCHAR)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS voprosi
                        (id INTEGER PRIMARY KEY, text VARCHAR,
                        right VARCHAR, answer_1 VARCHAR, answer_2 VARCHAR,
                        answer_3 VARCHAR)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS links
                   (id INTEGER PRIMARY KEY, quiz_id INTEGER, quest_id INTEGER,
                    FOREIGN KEY (quiz_id) REFERENCES quezes(id),
                    FOREIGN KEY (quest_id) REFERENCES quises(id))''') 

    close()

def set_victorini():
    global connect, cursor
    open()

    quiz_list =[("Викторина про Анатомию тела Человека",),
                ("Викторина по игре про Хеллоувин",), 
                ("Викторина в Кальмара",),]
    cursor.executemany('''INSERT INTO victorini (name)
                        VALUES (?)''', quiz_list)
    close()




def set_voprosi():
    global connect, cursor

    quest_list =[("Сколько у человека всего органов чуств?","4","5","9","16"),
                ("Где находится сонная артерия?","вокруг шеи","по бокам шеи","сзади шеи","в спереди шеи"), 
                ("Сколько всего у человека органов?","79","45","36","92"),
                ("Как располагается костный мозг в теле?","в основном внутри тазовых костей","в спине","в шее","в задней части головы"),
                ("Где находится сонная артерия?","по бокам шеи","сзади шеи","вокруг шеи","в спереди шеи"), 
                ("Сколько всего у человека органов?","79","45","36","92"),
                ("Где находится мозг?","находится внутри черепа","в спине","вверху черепа","в низу черепа"), 
                ("Сколько всего у человека костей?","206-208","78","96","39"), 
                ("Сколько всего у человека мышц в теле?","от 639 до 850","от 610 до 725","от 366 до 455","от 230 до 345"),
                ("Сколько всего у человека зубов?","32","42","36","16"), 
                ("Сколько новых эритроцитов образуется в костном мозге каждую секунду?","Около 2,4 миллиона новых эритроцитов образуется в костном мозге каждую секунду","Около 2 миллионов новых эритроцитов образуется в костном мозге каждую секунду","Около 2,6 миллиона новых эритроцитов образуется в костном мозге каждую секунду","Около 2,5 миллиона новых эритроцитов образуется в костном мозге каждую секунду"),
                ("Где находится человеческое сердце?","слева от грудной клетки","в серидине грудной клетки","справа от грудной клетки","в спереди шеи"), 
                ("Сколько всего у человека всего годов жизни?","многие доживают до до 100 лет","многие доживают до 150 лет","многие доживают до 125 лет","многие доживают до 110 лет"),
                ("Сколько всего в крови человека хромосом?","есть всего 46 хромосом","есть всего 36 хромосом","есть всего 45 хромосом","есть всего 35 хромосом"), 
                ("Сколько всего у человека рёбер?","12 пар","16 пар","18 пар","14 пар"),
                ("В каком году впервые начали проводить хеллоувин?","было зафиксировано в начале XX века","было зафиксировано в начале XXX века","было зафиксировано в начале XXII века","было зафиксировано в начале XXI века"), 
                ("Сколько конфет могли дать?","34","45","39","92"),
                ("За что давали конфеты?","Они выпрашивают сладости в шуточно-ультимативной форме","Они традиционно танцуют танец перед дверьми в шуточно-ультимативной форме и получают сладости","Они традиционно выпрашивают сладости в шуточно-устрашающеной форме","Они традиционно вымогают сладости в устрашающей форме"), 
                ("Когда было впервые зафиксировано ношение маскарадных костюмов на Хэллоуин? И в какой стране?","было зарегистрировано в 1895 году в Шотландии","было зарегистрировано в 1905 году в Австралии","было зарегистрировано в 1835 году в Испании","было зарегистрировано в 1865 году в Исландия"),
                ("Кто именно выпрашивал сладости?","дети","взрослые","животные","и взрослые и дети"),
                ("Как именно выпрашивали сладости дети?"," с вопросом «Гадость или сладость?»","c угрозами","с мольбами","как вознагрождение за выступление в танце"),
                ("В каком возрасте выпрашивать сладости было нельзя?","старше 12 лет","старше 12 лет","36","92"),
                ("С какого часа начинался праздник?","4-5 часов вечера","4-5 часов утра","3-4 часов вечера","6-7 часов вечера"), 
                ("Какие украшения в доме делали на хеллоувин?","тыквы с вырезанными глазами,паутины и пауки,привидения и ведьмы,летучие мыши,ходячие зомби и мумии,Метлы,волшебные палочки и прочий скарб,черные кошки в любых проявлениях,свечи,сухие листья и прочие атрибуты осени","милые зверушки и мягкие диванчики","красивые подушки и яркие цветы с пушистыми пауками","самые страшные кошки,пауки и маленькие гномы с мётлами"),
                ("Были ли украшения дома обязательными?","да, это было обязательно","нет, необязательно","без разницы как нравится","Как хочется"), 
                ("До скольки длился хеллоувин?","до 7 дней","до 6 дней","до 16 дней","до 8 дней"),
                ("Наряжали ли животных на этот зловещий праздник?","да можно, но не обязательно","нет и не обязательно мучать бедное созданьеце","да но не надо мучать животное","как хочется"), 
                ("Убивали ли кого нибудь на хеллоувин?","да","нет","не знаю","наверно"),
                ("Когда хеллоувин начали проводить и другие страны?","31 октября","4 декабря","13 ноября","16 февраля"), 
                ("Сколько всего у детей получалось собрать конфет?","79 и больше","45 и меньше","36 и всё","92 и всё а то беда"),
                ("Где находиться остров где был главный герой?","остров Сап-гап-до - что находился на западе побережья корейского полуострова","остров Галинос - что находился на северной части побережья","остров Чебуджа - что находился на восточной части полуострова китай","нигде всё проходило на полуострове Корея"), 
                ("Кого из друзей убил главный герой самолично на последнем испытании?","Сон Ки Хун","Сан ки Хан","Сон ки Хён","Сэн ка хин"),
                ("Как звали дедушку?","О иль-нем","О иль-ням","О эль-ним","О ель-нам"),
                ("Почему мать главного героя погибла?","от болезни","от усталости","от радости","от старости"), 
                ("Сколько всего заработал главный герой после игры в кальмара?","45,6 млрд вон (примерно $40 млн)","40 млрд вон (примерно $37 млн)","25 млрд вон (примерно $19 млн)","57 млрд вон (примерно $52 млн)"),
                ("Из-за чего главный герой погряз в долгах?","из-за игромании и неуплаты кредиторам","из-за безработицы","из-за ","из-за опоздания с уплатой налогов"), 
                ("Сколько всего было денег у главного героя до игры?","среднее количество но он очень быстро их проиграл поэтому очень частно брал деньги у своей матери","очень мало и поэтому он очень частно брал деньги у своей матери","много но он их быстро тратил а потом и вовсе стал красть у матери","главный герой много зарабытывал но очень обажал красть у своей матери деньги"),
                ("Какая в итоге была концовка сериала?","с намёком на продолжение","грустненькая","ммм, непомню но вроде скучная","довольно спокойная"), 
                ("Почему люди добровольно участвовали в испытаниях?","они были бедны и задолжали данег другим","им было неинтересно жить и они решили умереть","ими движело желание получить деньги хотя у них уже они были","они очень захотели поиграть на смерть"),
                ("Зачем именно в игре кальмара убивали людей?","оттого что богатым было скучно","богатыми движело желания убийства","желание потратить большие суммы денег","желание побыть садистами"), 
                ("Кем в итоге оказался дедушка?","злодеем","главным героем","нейтралом","одним из участников игры"),
                ("Какие именно были участники в команде героя?","Сон Ки Хун, Чхо Сан Воо, Кан Сэ Бёк, О Иль Нам, Али Абдул","Сон Кэ Хьун, Вхо Сэн Воо, Кин Сэ Бёк, О Иль Нэм, Али Авдул","Син Кан Хун, Чво Сан Воо, Ким Сэ Бёк, Э Иль Ним, Эли Абдул","Сан Ки Хьюн, Чво Сан Фоо, Кан Са Вёк, О Эль Нэм, Али Эбдул"), 
                ("Сколько всего было участников в 3 испытании?","10","15","45","13"),
                ("Какая цифра была у главного героя и дедушки?","456,001","460,001","056,001","446,002"), 
                ("Как звали подругу главного героя и даже помощницы в испытаниях что в итоге погибла в конце сериала?","Кан Сэ Бёк","Кон са Бёк","Кэн Са Вёк","Ким Са Вёк"),]
 
    open()
    for i in quest_list:
        if len(i) != 5:
            print(i)
    cursor.executemany('''INSERT INTO voprosi (text, right, answer_1, answer_2, answer_3)
                        VALUES (?,?,?,?,?)''', quest_list)
    close()

def set_links():
    global connect, cursor
    open()
    links = [(1,1),
            (1,2),
            (1,3),
            (1,4),
            (1,5),
            (1,6),
            (1,7),
            (1,8),
            (1,9),
            (1,10),
            (1,11),
            (1,12),
            (1,13),
            (1,14),
            (1,15),
            (2,16),
            (2,17),
            (2,18),
            (2,19),
            (2,20),
            (2,21),
            (2,22),
            (2,23),
            (2,24),
            (2,25),
            (2,26),
            (2,27),
            (2,28),
            (2,29),
            (2,30),
            (3,31),
            (3,32),
            (3,33),
            (3,34),
            (3,35),
            (3,36),
            (3,37),
            (3,38),
            (3,39),
            (3,40),
            (3,41),
            (3,42),
            (3,43),
            (3,44),
            (3,45)
            ]
    cursor.executemany('''INSERT INTO links (quiz_id,quest_id) 
                            VALUES (?,?)''',links)
    close()
            
def clear():
    global connect, cursor
    open()
    cursor.execute('''DROP TABLE IF EXISTS victorini''')
    cursor.execute('''DROP TABLE IF EXISTS voprosi''')
    cursor.execute('''DROP TABLE IF EXISTS links''')
    close()

def get_next_question(n_victoriny,now_question):
    global connect, cursor
    open()
    cursor.execute('''SELECT quest_id FROM links WHERE quiz_id==(?) AND
                                                           quest_id > (?)''',
                                                [n_victoriny, now_question])
    data = cursor.fetchall()
    return data[now_question][0]

def get_max_question(n_victoriny):
    global connect, cursor
    open()
    cursor.execute('''SELECT quest_id FROM links WHERE quiz_id==(?)''',
                                                [n_victoriny])
    data = cursor.fetchall()
    return len(data)

def get_vopros_by_id(id):
    global connect, cursor
    open()
    cursor.execute('''SELECT * FROM voprosi WHERE id==(?)''',
                                                [id])
    data = cursor.fetchone()
    return data

def get_all_quischen():
    global connect, cursor
    open()
    cursor.execute('''SELECT * FROM victorini''') 
    data = cursor.fetchall()
    return data

if __name__ == "__main__":
    clear()
    create()
    set_victorini()
    set_voprosi()
    set_links()
    get_next_question(1,4)
    print(get_all_quischen())
