import hashlib
from re import compile as re_compile


words = ( 'aaa','aah','aas','aba','abc','abs','aby','acc','ace','act','ada','add','ade','ado','adp','ads','adz','aft','aga','age','ago','aid','ail','aim','ain','air','aix','aku','ala',
          'alb','ale','all','alp','als','alt','ana','and','ane','ani','ans','ant','any','ape','apr','apt','ara','arb','arc','are','ark','arm','ars','art','ash','ask','asp','ass','ate',
          'atm','aug','auk','aum','aus','avo','awe','awl','awn','axe','azo','baa','bad','bag','bai','bam','ban','bap','bar','bas','bat','bay','bbl','bbs','bed','bee','beg','bel','ben',
          'bet','bey','bib','bid','big','bin','bit','biz','boa','bob','bod','bog','boo','bop','bos','bot','bow','box','boy','bpi','bps','bra','btu','bud','bug','bum','bun','bur','bus',
          'but','buy','bye','bys','cab','cad','cam','can','cap','car','cat','caw','cay','cfs','cgs','chi','cia','cid','cis','cli','cob','cod','cog','col','con','coo','cop','cos','cot',
          'cow','cox','coy','cpi','cps','cpu','cro','crs','cry','cst','cub','cud','cue','cul','cum','cup','cur','cut','cwm','cwt','dab','dad','dag','dah','dak','dal','dam','das','dat',
          'daw','day','ddt','dea','deb','dec','den','des','dew','dia','die','dig','dim','din','dip','dis','dit','dix','dkg','dkl','dkm','doc','dod','doe','dog','doh','dol','don','dos',
          'dot','dry','dub','dud','due','dug','dun','duo','dye','dys','ear','eat','ebb','edo','edp','eds','eel','eff','eft','egg','ego','ela','eld','elf','elk','ell','elm','els','emf',
          'emu','end','enl','eon','eos','epa','epi','era','erg','ern','err','ese','esp','esq','est','eta','eve','ewe','eye','fab','fad','fae','fag','fan','faq','far','fas','fat','fax',
          'fay','fbi','fcs','fed','fee','fen','fet','few','fey','fez','fib','fig','fin','fir','fit','fix','flu','fly','fob','foe','fog','fop','for','fox','fps','frs','fry','fug','fun',
          'fur','gab','gad','gag','gal','gam','gap','gar','gas','gat','gay','geb','gee','gel','gem','gen','ges','get','gib','gig','gin','gip','gis','git','gnu','goa','gob','god','goo',
          'gos','goy','gps','gum','gun','gur','gut','guy','gym','gyp','hag','haj','ham','han','hao','hap','hat','haw','hay','hel','hem','hen','hep','her','hes','het','hew','hex','hie',
          'him','hin','hip','hit','hob','hod','hoe','hog','hop','hot','hoy','hrs','hub','hud','hue','hug','hum','hun','hut','ice','icy','ida','ido','ids','iii','ike','ilk','ill','imp',
          'imu','inc','ink','inn','ins','ion','iou','ips','iqs','ira','ire','irk','irs','ism','isn','iud','iva','ivy','jab','jag','jak','jam','jan','jap','jar','jat','jaw','jay','jem',
          'jet','jew','jib','jig','jnd','job','jog','jot','joy','jug','jut','kat','kea','keb','keg','ken','key','khi','kid','kin','kip','kit','kob','kor','kos','kph','krs','kui','kyd',
          'lab','lac','lad','lag','lah','lam','lan','lao','lap','las','lat','lav','law','lax','lay','lbs','lcd','lcm','lea','led','lee','leg','lei','lek','leo','ler','les','let','leu',
          'lev','ley','lid','lie','lin','lip','lir','lis','lit','liv','llb','lob','log','loo','lop','lot','low','lox','lug','luo','lux','lxx','lye','mac','mad','mag','mam','man','mao',
          'map','mar','mas','mat','maw','max','may','mbd','mcg','med','meg','mem','men','meq','mes','mew','mho','mhz','mib','mid','mil','min','mit','mix','moa','mob','mod','mol','mom',
          'mon','moo','mop','mot','mow','mph','mrs','msg','mts','mud','mug','mum','mus','mya','myg','mym','nab','nad','nag','nan','nap','nay','neb','nee','neo','net','new','nib','nil',
          'nim','nip','nis','nit','nix','nob','nod','nog','non','nor','not','nov','now','nox','nth','nub','nun','nut','oaf','oak','oar','oat','obi','oca','oct','odd','ode','ods','off',
          'ofo','oft','ohm','ohs','oil','oka','ola','old','olm','one','oni','ono','ons','ooh','ops','opt','orb','ore','ors','otc','oto','our','out','owe','owl','own','pac','pad','pal',
          'pan','pap','par','pas','pat','paw','pax','pay','pct','pdl','pea','pee','peg','pen','pep','per','pes','pet','pew','pfc','phi','pia','pic','pie','pig','pin','pip','pit','pix',
          'plf','ply','poa','pob','pod','poe','poi','pol','pom','pop','pot','pow','pox','prn','pro','pry','psf','psi','pst','pub','pud','pug','pul','pun','pup','pus','put','pwr','pya',
          'pyx','qat','qed','rad','rag','raj','ram','rap','ras','rat','raw','ray','reb','red','ref','rem','rep','res','ret','rev','rex','rfs','rhd','rho','rib','rid','rig','rim','rio',
          'rip','rob','roc','rod','roe','roi','rom','ron','rot','row','rpm','rub','rue','rug','rum','run','rus','rut','rya','rye','sac','sad','sag','sam','sap','sat','saw','sax','say',
          'sds','sea','sec','see','sen','sep','set','sew','sex','she','shy','sib','sic','sin','sip','sir','sis','sit','six','ski','sky','sly','sob','sod','soh','sol','son','sop','sos',
          'sot','sou','sow','soy','spa','spy','std','stm','sty','sub','sue','sum','sun','sup','sur','sus','tab','tad','tag','tai','tam','tan','tao','tap','tar','tat','tau','taw','tax',
          'tay','tea','tec','ted','tee','teg','ten','the','tho','tib','tic','tie','tin','tip','tis','tit','tiu','tnt','tod','toe','tog','tom','ton','too','top','tor','tot','tow','toy',
          'trf','try','tsk','tss','tub','tug','tum','tun','tup','tut','tux','two','tyr','uca','ufo','uke','ull','ult','ump','UNI','uns','ups','urd','urn','urs','usa','use','uta','ute',
          'uts','utu','vac','van','var','vas','vat','veg','vet','vex','via','vie','vii','vim','vip','vow','vox','wac','wad','wag','wan','war','waw','wax','way','web','wed','wee','wei',
          'wen','wet','who','why','wig','win','wit','wiz','woe','wog','wok','won','woo','wop','wow','wpm','wry','wye','xcl','xii','xiv','xix','xvi','xxi','xxv','xxx','yak','yam','yap',
          'yaw','yay','yea','yen','yes','yet','yew','yid','yin','yip','yis','yob','yon','you','zag','zap','zea','zed','zee','zen','zep','zig','zip','zit','zoo','b2b','cfg','cgi','css',
          'csv','gpl','jit','mmx','p2p','pid','pnp','ppp','rle','rtc','ssd','uml','aye','yo','a','sheep','eats','some','food','sometimes','sandwich','others','dump','boar','jelly',
          'ai','twiddle','thumb','maniac','frantic','happy','joyful','giddy','true','false','bent','thick','thicc','think','basic','epic','elite','goat','salty','savage','groovy',
          'hand','dude','dudester','grand','ball','sick','cool','swag','dough','bear','beer','deer','moose','salmon','crow','crayon','space','lore','geek','nerd','super','on','rare',
          'seldom','potato','neat','nuts','cheese','deep','icky','stump','seven','nation','army','ftw','ditch','guts','goof','hustle','grub','crap','whiz','of','up','down','near',
          'behind','glory','to','ukraine' )

email_regex = re_compile('^[a-z0-9.!#$%&’*+/=?^_`{|}~-]+@([a-z0-9-]{2,30}\.)+[a-z]{2,3}$')


def hash(s):
    h = hashlib.md5(s.encode()).digest()
    p = []
    for i in range(4):
        q = 0
        for j in range(2):
            q = q*256 + h[i*2+j]
        p.append(q & 0x3ff)
    return '-'.join([words[q] for q in p])


def hash_email(e):
    e = e.lower()
    assert email_regex.match(e)
    return hash(e)


if __name__ == '__main__':
    while True:
        print(hash_email(input('Enter email: ')))
