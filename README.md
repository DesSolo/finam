## Finam influxdb exporter

#### Example
```shell script
podman run --rm -e INFLUX_HOST=127.0.0.0.1 -e INFLUX_DATABASE=finam_db -e TARGETS=6:+МосЭнерго,1938060:MAIL-гдр dessolo/finam:latest
```
#### Env
|Name|Default|Example|
|-----|------|-----|
|USER_AGENT|`Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0`|
|INFLUX_HOST|-||
|INFLUX_PORT|8086||
|INFLUX_USERNAME|root||
|INFLUX_PASSWORD|root||
|INFLUX_DATABASE|-|finam_db|
|TARGETS|-|6:+МосЭнерго,1938060:MAIL-гдр|

#### 
|em|cn|
|---|---|
|6|+МосЭнерго|
|399716|AGRO-гдр|
|489354|ENPL-гдр|
|928412|ETLN-гдр|
|491944|FIVE-гдр|
|1938060|MAIL-гдр|
|1919466|Petropavl|
|175924|Polymetal|
|414279|RUSAL plc|
|498713|Raven|
|913710|TCS-гдр|
|388383|Yandex clA|
|181610|iQIWI|
|22843|iАвиастКао|
|74744|iДонскЗР|
|74745|iДонскЗР п|
|17137|iИСКЧ ао|
|901174|iММЦБ ао|
|81992|iНПОНаука|
|74584|iФармсинтз|
|81820|АЛРОСА ао|
|81882|АЛРОСА-Нюр|
|484229|АСКО ао|
|82460|АбрауДюрсо|
|82843|Авангрд-ао|
|17564|Акрон|
|13855|Аптеки36и6|
|19915|Арсагера|
|16452|АстрЭнСб|
|20702|АшинскийМЗ|
|29|Аэрофлот|
|20066|БСП ао|
|462599|БУДУЩЕЕ ао|
|35242|БашИнСв ао|
|35243|БашИнСв ап|
|81757|Башнефт ао|
|81758|Башнефт ап|
|21078|Белон ао|
|19651|Белуга ао|
|82616|БестЭфБ ао|
|81901|БурЗолото|
|15965|ВСМПО-АВСМ|
|19043|ВТБ ао|
|17257|ВХЗ-ао|
|16352|ВЭК 01 ао|
|81954|Варьеган|
|81955|Варьеган-п|
|17068|Возрожд-ао|
|17067|Возрожд-п|
|16456|ВолгЭнСб|
|16457|ВолгЭнСб-п|
|83251|ВыбСудЗ ао|
|83252|ВыбСудЗ ап|
|81997|ГАЗ ао|
|81998|ГАЗ ап|
|82115|ГАЗ-Тек ао|
|81399|ГАЗ-сервис|
|81398|ГАЗКОН-ао|
|16842|ГАЗПРОМ ао|
|436120|ГЕОТЕК ао|
|449114|ГИТ ао|
|795|ГМКНорНик|
|488918|ГТМ ао|
|152397|ГазпРнД ао|
|2|Газпрнефть|
|17698|Галс-Девел|
|20708|ДВМП ао|
|19724|ДЭК ао|
|16825|ДагСб ао|
|473181|ДетскийМир|
|487432|ЕвроЭлтех|
|82001|ЗВЕЗДА ао|
|81918|ЗИЛ ао|
|35363|ЗаводДИОД|
|81786|ИКРУСС-ИНВ|
|1667866|ИНГРАД ао|
|20711|ИНГРАД ао|
|15547|ИРКУТ-3|
|81887|Ижсталь ап|
|81885|Ижсталь2ао|
|409486|Инв-Девел|
|20516|ИнтерРАОао|
|9|ИркЭнерго|
|15544|КАМАЗ|
|17359|КЗМС ао|
|22525|КМЗ|
|16284|КСБ ао|
|16285|КСБ ап|
|81943|КУЗОЦМ ао|
|16329|КалужскСК|
|20030|КамчатЭ ао|
|20498|КамчатЭ ап|
|18310|Квадра|
|18391|Квадра-п|
|75094|Кокс ао|
|20710|КоршГОК ао|
|81903|КосогМЗ ао|
|511|КрасОкт-1п|
|510|КрасОкт-ао|
|20912|Красэсб ао|
|20913|Красэсб ап|
|522|Кубанэнр|
|35285|КузбТК ао|
|83165|КузнецкийБ|
|81941|Куйбазот|
|81942|Куйбазот-п|
|83261|КурганГКао|
|152350|КурганГКап|
|19736|ЛСР ао|
|8|ЛУКОЙЛ|
|16276|ЛЭСК ао|
|152517|Левенгук|
|22094|Лензол. ап|
|21004|Лензолото|
|385792|Лента др|
|542|Ленэнерг-п|
|31|Ленэнерго|
|19737|М.видео|
|12983|МГТС-4ап|
|12984|МГТС-5ао|
|20947|МЕРИДИАН|
|420694|МКБ ао|
|16782|ММК|
|16917|МОЭСК|
|20309|МРСК СЗ|
|20402|МРСК Ур|
|20107|МРСК ЦП|
|20235|МРСК Центр|
|20286|МРСКВол|
|20346|МРСКСиб|
|15523|МТС-ао|
|74562|МагадЭн ао|
|74563|МагадЭн ап|
|17086|Магнит ао|
|152516|МегаФон ао|
|30|Мегион-ао|
|51|Мегион-ап|
|20737|Медиахолд|
|21018|Мечел ао|
|80745|Мечел ап|
|16359|МордЭнСб|
|81944|Морион ао|
|152798|МосБиржа|
|82890|МосОблБанк|
|74549|Мостотрест|
|152676|МультиСис|
|20100|НКНХ ао|
|20101|НКНХ ап|
|450432|НКХП ао|
|17046|НЛМК ао|
|19629|НМТП ао|
|81929|НаукаСвяз|
|81287|Нефтекамск|
|81947|Нижкамшина|
|17370|Новатэк ао|
|414560|ОВК ао|
|18684|ОГК-2 ао|
|175781|ОКС ао|
|15844|ОМЗ-ап|
|488674|ОР ао|
|81856|ОргСинт ао|
|81857|ОргСинт ап|
|152876|ПАОДжиТиЭл|
|18654|ПИК ао|
|35247|ПРОТЕК ао|
|81896|ПавлАвт ао|
|16909|ПермьЭнС-п|
|16908|ПермьЭнСб|
|81241|Плазмек|
|17123|Полюс|
|80818|Приморье|
|74779|РБК ао|
|181934|РГС СК ао|
|181755|РДБанк ао|
|81933|РН-ЗапСиб|
|20637|РОСИНТЕРао|
|17713|Распадская|
|152677|Роллман|
|388313|Роллман-п|
|16866|Росбанк ао|
|17273|Роснефть|
|20681|РоссЮг ао|
|20412|Россети СК|
|20971|Россети ао|
|20972|Россети ап|
|7|Ростел -ао|
|15|Ростел -ап|
|35238|РусАква ао|
|20266|РусГидро|
|66893|Русгрэйн|
|181316|Русолово|
|20712|Русполимет|
|465236|РуссНфт ао|
|16455|РязЭнСб|
|491359|САФМАР ао|
|22401|СЗПароход|
|20892|СМЗ-ао|
|16080|СОЛЛЕРС|
|445|СамарЭн-ао|
|70|СамарЭн-ап|
|81891|СаратНПЗ|
|81892|СаратНПЗ-п|
|11|СаратЭн-ао|
|24|СаратЭн-ап|
|473000|Сахэнер ао|
|3|Сбербанк|
|23|Сбербанк-п|
|16136|СевСт-ао|
|81360|Селигдар|
|82610|Селигдар-п|
|436091|СибГост ао|
|19715|Система ао|
|15723|Слав-ЯНОСп|
|15722|Славн-ЯНОС|
|20087|СтаврЭнСб|
|20088|СтаврЭнСбп|
|4|Сургнфгз|
|13|Сургнфгз-п|
|81914|ТАНТАЛ ао|
|81915|ТАНТАЛ ап|
|18382|ТГК-1|
|18176|ТГК-14|
|17597|ТГК-2|
|18189|ТГК-2 ап|
|20716|ТЗА ао|
|81905|ТКЗКК ао|
|81906|ТКЗКК ап|
|74746|ТКСМ ао|
|18441|ТМК ао|
|19916|ТНСэКубань|
|16331|ТНСэМаЭл-п|
|16547|ТНСэнВор-п|
|16546|ТНСэнВорон|
|16330|ТНСэнМарЭл|
|16615|ТНСэнНН ао|
|16616|ТНСэнНН ап|
|16783|ТНСэнРст|
|16784|ТНСэнРст-п|
|16342|ТНСэнЯр|
|16343|ТНСэнЯр-п|
|420644|ТНСэнрг ао|
|16797|ТРК ао|
|16798|ТРК ап|
|16265|ТамбЭнСб|
|16266|ТамбЭнСб-п|
|825|Татнфт 3ао|
|826|Татнфт 3ап|
|18371|Таттел. ао|
|21002|Телеграф|
|81575|Телеграф-п|
|74561|ТрансК ао|
|497210|ТрансФ ао|
|1012|Транснф ап|
|82611|УрКузница|
|81953|УралСиб ао|
|19623|Уркалий-ао|
|20509|ФСК ЕЭС ао|
|81858|Физика ао|
|81114|ФосАгро ао|
|81939|Химпром ао|
|81940|Химпром ап|
|19095|ЦМТ ао|
|19096|ЦМТ ап|
|83121|ЧЗПСН ао|
|21000|ЧКПЗ ао|
|21001|ЧМК ао|
|20999|ЧТПЗ ао|
|20125|ЧеркизГ-ао|
|929597|ЭН+ГРУП ао|
|81934|Электрцинк|
|16440|ЭнелРос ао|
|20321|ЭнергияРКК|
|15522|ЮТэйр ао|
|82493|ЮУНК ао|
|20717|ЮжКузб. ао|
|18584|Юнипро ао|
|81917|ЯТЭК ао|
|81769|Якутскэн-п|
|81766|Якутскэнрг|