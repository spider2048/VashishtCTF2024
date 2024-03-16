from Crypto.Util.number import isPrime

flag = open("./flag.txt").read()

primes = []
last = 1
while len(primes) < len(flag):
    if isPrime(last):
        primes.append(last)
    last += 1


N = 1
lp = 0

for char in flag:
    N *= pow(primes[lp], ord(char))
    lp += 1

print(N) # 4323233879711999570304451642095862230268167705393339081599841412450161262041059649650328028111636323132889201937294115165359848863656452721724329797892320354633272679365650328679503336453398955624613566412658210623303463707879939719046895984280241436363481117739194563767490582151375891080088476557625743445957625929121636878393112004245597681528801209937629200846579187776532445843311896961007749828576834565861748191949074993464896984446502807281661237730597632521433100013948168751571092360890154690439447250916034881173115230939161252571726112292730984521761090159362509586669436717617792387271333856752172812171642187787787553874364806650444079681697231491725847604068074483656960111477032558108896731293833960200707560412062339354039404732958244486106156454983112198644165074540548872029231935943940756301536750959179562828706702129853510603890156478414981646027364309970396091910144495339078023596118960620175026263210923390624743306005353551716654770893492016831864176189846411759106539245720075963809960882974729634561073351168468342126037592578830592087875695345306463090742338121605705283342940687234183893587256394455848884663361702842359882806817437001455646749019986719611752583060800462700941786337340943594826599340609489868408783870827667379531739039481000884360306997729517571857387280182351887943208066494853203356350075624092075558336580957982755394108036439271400271507451102848156764427924121824289775516922432359344258690127538654757551135163410674034856759760701858907248056643116250204392766079487591727751620902225297681841717331217626061256416743638838990555094981416221257198602457193102902018626277085477100613007387757972411604901510020519560956306098783332773815728982520744450573095485178384236201130998940398761586739057385723828976097883369164627799690532442362422750191026453450293272062161939455888580285615154678556163180247378568786191074111149383851091356127326215013888743749288328518333830937437998268147081343306231667034630515306112431888453837987539519602253617684277653688962269750584540000000000000000000000000000000000000000000000000000000000000000000000000000000000