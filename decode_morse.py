from unidecode import unidecode

morseFile = """A   .-
B   -...
C   -.-.
D   -..
E   .
F   ..-.
G   --.
H   ....
I   ..
J   .---
K   -.-
L   .-..
M   --
N   -.
O   ---
P   .--.
Q   --.-
R   .-.
S   ...
T   -
U   ..-
V   ...-
W   .--
X   -..-
Y   -.--
Z   --..
1   .----
2   ..---
3   ...--
4   ....-
5   .....
6   -....
7   --...
8   ---..
9   ----.
0   -----"""

res = ['FIDO', 'GENE', 'TESA', 'RAVE', 'SUSO', 'CIME', 'MIII', 'NEAO', 'NERD', 'ILEX', 'ABIU', 'PINE', 'NAIA', 'EREO', 'AIDA', 'TITA', 'FERE', 'MERU', 'IANO', 'FITO', 'MANE', 'LILA', 'RUBI', 'ANIL', 'ETNO', 'MUIM', 'FILA', 'SAIS', 'DEDE', 'SAIM', 'MISO', 'JAIR', 'MADE', 'PIEN', 'MENI', 'CHAS', 'BELI', 'ADIN', 'BIRA', 'SITO', 'MIVA', 'SEGE', 'TENE', 'DNER', 'CAIR', 'SDTV', 'CUIA', 'PIER', 'SUBE', 'RATO', 'ADIL', 'CUIM', 'TAIA', 'IAIA', 'AIEA', 'IASO', 'PESA', 'JANE', 'MAIM', 'DIAS', 'PEMI', 'BERO', 'VIIA', 'PESO', 'EDMO', 'UERA', 'BUIR', 'PIDA', 'IATE', 'FELO', 'AREA', 'GADE', 'CELE', 'XAIA', 'ESAF', 'ERIX', 'GUNE', 'MAIA', 'GERU', 'DIAP', 'SUNE', 'ELAR', 'BIDA', 'ANUI', 'OTIM', 'TIAL', 'ZEFA', 'ISBA', 'TEIO', 'JIRE', 'ANER', 'AINE', 'ETES', 'VANI', 'GEAN', 'NETA', 'ANSA', 'CINE', 'SENE', 'BELA', 'TUTU', 'ETER', 'LEDS', 'UTIL', 'SADI', 'FIFE', 'SELA', 'NELE', 'NUER', 'JEEP', 'ETEU', 'IANE', 'DABU', 'FINA', 'BERU', 'AVIO', 'SAIR', 'MINI', 'ANIA', 'JATI', 'GEES', 'EFES', 'DEIA', 'CERA', 'UADI', 'GUTE', 'NAVE', 'UNIO', 'AINU', 'VERA', 'MEIO', 'EDIL', 'IRIO', 'FAIM', 'APII', 'CAVI', 'EDAZ', 'IERE', 'NDAU', 'ABEL', 'LUIA', 'XIRI', 'BLAU', 'NUNE', 'HEIN', 'IRAO', 'PIRA', 'CMII', 'BAIA', 'BEEM', 'EMIA', 'LETO', 'IRES', 'HERE', 'ZAIR', 'PELE', 'BETU', 'BADI', 'LUNI', 'NELO', 'BITE', 'RUIR', 'HELA', 'PETE', 'NEIA', 'DEDO', 'PIUI', 'BUNI', 'GETE', 'NELI', 'JINA', 'QUIE', 'BAIE', 'BITA', 'MENU', 'INES', 'BIPS', 'ADAI', 'VITE', 'CADE', 'BIDE', 'MUIA', 'ALAU', 'ILMA', 'INAM', 'CUDE', 'XIRA', 'AILO', 'IEIE', 'EMEN', 'DIDA', 'SIAU', 'DVII', 'FEPE', 'FIFI', 'IPES', 'FINS', 'SATE', 'INEP', 'GILE', 'MATE', 'MIRI', 'TIRO', 'MUTI', 'ADIR', 'ANIM', 'BEIA', 'ZILA', 'IRAR', 'VIAL', 'LINE', 'GAIA', 'NIFE', 'HETE', 'MELE', 'NITO', 'NERO', 'ELMO', 'RUDE', 'SELO', 'PHEN', 'PERE', 'ESAB', 'YEWE', 'PIRI', 'UNUE', 'EIXE', 'QUIL', 'ILEO', 'RIEL', 'LIRA', 'XATE', 'IILP', 'FITA', 'JUTI', 'ISBN', 'BEFA', 'UIAI', 'ATIA', 'PIAU', 'DIET', 'ORIX', 'DEVE', 'FINO', 'FUNE', 'TIFE', 'EZIO', 'EDRO', 'PREM', 'PEVA', 'TERA', 'ULAU', 'SEIA', 'LITE', 'PERI', 'ESBA', 'MESA', 'EUBA', 'CLAU', 'PENA', 'PEIU', 'SIGS', 'MISA', 'RENE', 'EIRU', 'BEGE', 'PUTI', 'MEUE', 'REAL', 'HEDA', 'VIAS', 'VERI', 'BERE', 'DAVI', 'IEIS', 'TEIA', 'SABE', 'SIRI', 'HEME', 'TUTA', 'EFUE', 'ILES', 'TELA', 'NEFA', 'ETIO', 'ATIO', 'LIDE', 'INAE', 'NHAS', 'SIDI', 'MELA', 'TUIM', 'PAIA', 'ATER', 'LESA', 'MITU', 'VIRA', 'SERI', 'TUVI', 'ZEDA', 'ZEUS', 'RINS', 'MADI', 'ISDB', 'AZIA', 'ITNA', 'ULEX', 'UNIX', 'ABIN', 'NENE', 'UENA', 'UBIM', 'HAIL', 'FATO', 'EDER', 'BIBE', 'TITI', 'GESO', 'BENE', 'FELA', 'TEVE', 'SEBE', 'SAVA', 'NEDA', 'ODIR', 'CDVI', 'AUTO', 'DELE', 'AILA', 'HANS', 'AVIU', 'IUIU', 'CENE', 'BELE', 'VATE', 'TUIA', 'NESE', 'PIRE', 'IVES', 'DUIM', 'PEDE', 'TIAU', 'EDEL', 'PATE', 'FUTE', 'EITA', 'RITA', 'TIPI', 'NUEL', 'JIPE', 'VEIO', 'TEIU', 'SILE', 'MATI', 'BUEM', 'NATO', 'INIO', 'IRAS', 'EDES', 'LAIS', 'SINO', 'ZERE', 'TEUS', 'EIRO', 'SINA', 'IENE', 'ITUA', 'PATI', 'TIZI', 'AIRI', 'EIDO', 'UEUA', 'IETO', 'TIRA', 'EITO', 'SIBE', 'CRUE', 'SEBA', 'IAVE', 'JILE', 'ANEM', 'ABER', 'LIRU', 'DEMI', 'ARUE', 'ERIA', 'ABIE', 'CMIV', 'EIBA', 'SEBO', 'ANHO', 'BITU', 'LEME', 'MEME', 'GUIA', 'FUIM', 'MEDA', 'ENEL', 'LEDO', 'ELEU', 'TEAR', 'MEIA', 'VERE', 'SAIA', 'PAVE', 'VIDA', 'ABIS', 'HELE', 'EZEL', 'EDIA', 'SEDA', 'LIPE', 'VIME', 'SEUS', 'JUVU', 'TETE', 'MITE', 'FEDE', 'LENS', 'ERAM', 'ITEM', 'VUVU', 'PAIM', 'CRER', 'MESO', 'DIAU', 'TIME', 'NABU', 'JABU', 'TESO', 'VIDE', 'BETI', 'MAIR', 'JADE', 'FIRA', 'ITUI', 'PIUM', 'STEP', 'AIME', 'OIDE', 'LIRI', 'ZEZE', 'JERU', 'RETA', 'RUIM', 'NADI', 'DEUS', 'MEZE', 'PIAS', 'HERA', 'XERE', 'ALEX', 'IPEA', 'OVIL', 'ANIS', 'TAIM', 'TINE', 'AVIR', 'IABA', 'FIXO', 'MESI', 'JIPI', 'UNIR', 'TIES', 'GABU', 'PITU', 'IFIS', 'CAIA', 'HENA', 'EBER', 'PEPS', 'TSUA', 'RINO', 'CREA', 'SIDA', 'FIAU', 'UNHA', 'NEEA', 'IRIS', 'PIAI', 'QUIR', 'PIPI', 'TEST', 'IERA', 'TABI', 'IDEU', 'DRAV', 'CUBU', 'RATI', 'DILO', 'TEPE', 'UEFA', 'LELE', 'GUEI', 'BIRI', 'SUIL', 'FEAO', 'LAUA', 'EZEM', 'LAIO', 'ELAO', 'FILE', 'ANHA', 'TIMO', 'OITI', 'BELO', 'CAVU', 'CUIL', 'ENIO', 'EMEU', 'MEUS', 'MMII', 'TANI', 'RAIL', 'HANI', 'CABU', 'VITU', 'SERO', 'PENI', 'REDE', 'VAEA', 'NIUE', 'JEAN', 'VINA', 'BUBU', 'INAB', 'AIRA', 'BIME', 'LAIA', 'VIES', 'CIMI', 'SEMI', 'SETE', 'BIAI', 'MILA', 'HAIA', 'ESAU', 'DVDS', 'REMA', 'AIAR', 'JENI', 'HABE', 'GIRA', 'SUVA', 'DINE', 'ABIR', 'SENA', 'CIDA', 'PELA', 'RANI', 'BADE', 'TIEM', 'SIPE', 'MIMI', 'NIVE', 'FLEX', 'CANI', 'JITI', 'ELMA', 'SITU', 'ELAU', 'CANE', 'SENO', 'ATIM', 'VADE', 'NUEZ', 'BEFE', 'TELE', 'BILE', 'EDTV', 'CHAI', 'ENEO', 'TEFE', 'ANEL', 'MEMI', 'EIRA', 'NEPE', 'INFO', 'BIAS', 'GILA', 'NEAL', 'IRUM', 'CUBE', 'TREM', 'CUTE', 'PSTU', 'FERO', 'SAVE', 'PREA', 'ADAU', 'DIRO', 'AVEL', 'SERE', 'ADIM', 'GIZE', 'MIUS', 'NETO', 'BERI', 'BEST', 'ABIO', 'BUVA', 'NERI', 'NEVE', 'OENA', 'LEIU', 'CAIM', 'XIRU', 'FAIA', 'BIFU', 'SUEZ', 'PUVI', 'ATIS', 'AVES', 'LUIR', 'HENE', 'ANUU', 'IAUO', 'TIRE', 'UNIT', 'OBUS', 'MIRA', 'JERE', 'TAVI', 'RABI', 'HILE', 'VILI', 'AIER', 'SATI', 'TUBI', 'TABE', 'SEPE', 'ABIA', 'IEBA', 'BIDU', 'RIDO', 'EDTA', 'NAIR', 'PNEE', 'ZIZI', 'BUSH', 'EVEU', 'OSTE', 'AIMA', 'AIUE', 'OFEL', 'PILE', 'TITO', 'EMIS', 'TIPE', 'IIAS', 'CINA', 'SAIL', 'FINI', 'REMO', 'MIAU', 'MABU', 'MIME', 'MIDA', 'LIVE', 'TERE', 'UMES', 'EMIR', 'BIRU', 'BUSO', 'GENI', 'LEVI', 'RESA', 'SUBU', 'MEDE', 'SINI', 'CIRA', 'LEVE', 'NATA', 'BABI', 'CATI', 'IINI', 'MDVI', 'RANE', 'VIRO', 'CERU', 'UIRA', 'TEDA', 'MISE', 'PERU', 'PADE', 'SELF', 'BATE', 'ASAS', 'CIFE', 'ILAR', 'ITEA', 'GUDE', 'MUBE', 'AIAS', 'NANI', 'CIDE', 'HEMI', 'BUIA', 'ZENA', 'FEIA', 'MUBI', 'BIBO', 'SITE', 'SADE', 'HEDU', 'PIFE', 'TABU', 'EFUM', 'SUIA', 'ERIS', 'ZIAR', 'EIXU', 'JANI', 'EMIC', 'IRIZ', 'FAIT', 'CEIA', 'RAIA', 'EIXO', 'BIDO', 'GATE', 'AFER', 'DUBU', 'PEAN', 'LAUE', 'ENEM', 'TIAS', 'EDEN', 'UBIO', 'ERIL', 'CUBI', 'SEDE', 'ZABE', 'UAIA', 'PUIA', 'IEDA', 'PEIA', 'ESTE', 'SAEL', 'MISS', 'PERA', 'VILA', 'BIBI', 'FIEL', 'DABI', 'ISTO', 'IRAI', 'IDEM', 'GADI', 'ADEL', 'IDIA', 'BRIX', 'MENA', 'ASNO', 'IATA', 'VEDA', 'EZER', 'CADI', 'ABUA', 'OTIS', 'PUIR', 'BABU', 'IATI', 'SERA', 'INAN', 'DENA', 'UADE', 'DINA', 'CILA', 'FERA', 'RETO', 'NINI', 'QUIA', 'PANI', 'DIZE', 'IRAE', 'SUSI', 'JUNE', 'MIAS', 'PITI', 'SIRE', 'ERAR', 'ZUIR', 'RITO', 'CIAS', 'MINA', 'PLEX', 'VEIA', 'CUVU', 'VINI', 'BUBI', 'TATE', 'OTIA', 'HUDE', 'INEO', 'UVEA', 'MAIL', 'FETO', 'FATE', 'BIPE', 'EGEU', 'HIEL', 'HUBI', 'PEAD', 'HEBE', 'NEMP', 'OILA', 'MUBU', 'SEPS', 'AREL', 'JABE', 'MMIV', 'JAVE', 'PEPE', 'ONIX', 'NEMO', 'GSAN', 'OVNI', 'MILE', 'VELA', 'MUNI', 'NINA', 'JERA', 'ESTO', 'NABI', 'EMEX', 'ODRE', 'DILI', 'IEPE', 'ZANE', 'ABEAU', 'TIREO', 'HUSNA', 'SAIAS', 'JUDIA', 'ELENI', 'TEATE', 'SEDAL', 'AIRAR', 'SEDAR', 'FUSTE', 'BITIA', 'SESAI', 'JANIE', 'BELEM', 'MUIRA', 'JATIS', 'MAIRE', 'IRERE', 'METIL', 'MIZEU', 'RIETE', 'NAVIM', 'GLENA', 'DIRFO', 'UBINS', 'CIVIL', 'AIMEE', 'ARITI', 'MESAO', 'PIFIO', 'INFER', 'REPES', 'DESTE', 'GLETE', 'FEREU', 'SERIU', 'LESAS', 'PEPSE', 'AUSTE', 'ASTIL', 'TATSU', 'APEIA', 'RINAL', 'MADIA', 'CISTE', 'MEIRU', 'MANES', 'DUTIS', 'MANSA', 'PILAU', 'MITIM', 'CITEU', 'SEDAO', 'PILRA', 'ODETE', 'GANES', 'VESTE', 'JATEI', 'NERES', 'UBERE', 'MISTA', 'MEIER', 'HIDRA', 'REIDE', 'BELAU', 'JEUDE', 'LIANE', 'ISELE', 'TIENA', 'ZEFIR', 'ITIEL', 'FAIRE', 'NESTO', 'VAIRA', 'NUIMA', 'USTIR', 'SERFO', 'ANEEL', 'BENIN', 'PIELO', 'BERIL', 'ANITE', 'UBELE', 'CASTI', 'NEREO', 'MERUI', 'ARITE', 'ERERE', 'SETES', 'PIERO', 'BIDAO', 'BESAI', 'SIMEI', 'ENINO', 'BUSTO', 'LIGHT', 'LENEO', 'AEEAD', 'LAITU', 'UBERO', 'BELLO', 'BAIRA', 'NAIRE', 'ABUIZ', 'EUDES', 'DETER', 'SELAR', 'SERIE', 'USTIA', 'PEPES', 'GESTO', 'CAVEA', 'AGEIA', 'ZAIRA', 'PADEU', 'NEIDE', 'ETILO', 'BABEL', 'OFITE', 'SENIL', 'NINFA', 'VRITI', 'TEMIS', 'ARITU', 'TESLA', 'MANIU', 'ASTIM', 'FINAR', 'BABER', 'TITIM', 'CISNE', 'NIELO', 'UIRAS', 'ESERE', 'SANSA', 'ELEDE', 'SELAO', 'CLETE', 'ERATO', 'STILB', 'PETIA', 'CABER', 'BEIRU', 'BANSA', 'ESDRA', 'ANSAR', 'LEUDE', 'NEERA', 'SENIR', 'PIERE', 'SEMIS', 'DEITA', 'GITEU', 'NELMA', 'BELAS', 'EDENS', 'PITEU', 'SAVEL', 'TEITE', 'ODILA', 'LIVIA', 'BETIM', 'FERAL', 'GEINA', 'BIELA', 'ERINA', 'TRERE', 'MEVIA', 'MESES', 'RITIO', 'CUDIA', 'IANSA', 'XEREM', 'VIZIR', 'FEILA', 'FERAS', 'CHAVE', 'BINUI', 'SEDAS', 'EDILA', 'MISTO', 'UZIAS', 'DAIME', 'PIUVA', 'LENAO', 'VIRAR', 'OSEAS', 'MIRUI', 'LEILA', 'ANEIA', 'GEREM', 'TUNES', 'TEINA', 'ADVIR', 'MEIRE', 'MISNA', 'TESAR', 'EUDIA', 'ZAIRE', 'TIELA', 'DEUSA', 'REGIE', 'VILMA', 'ATEIA', 'SETIA', 'LEITE', 'RABEL', 'LAUTO', 'HIDAI', 'SAIAO', 'BIENE', 'BELRO', 'MEIRI', 'TADEU', 'DIENO', 'PSETO', 'MABER', 'PIREA', 'PIADE', 'IRITE', 'TMESE', 'GETEU', 'NZILA', 'TSELA', 'INATO', 'ERINO', 'SEDEM', 'SUBER', 'HELEN', 'IBERE', 'SILEX', 'EDREI', 'PINEL', 'SABER', 'CETIL', 'PIEZE', 'HEVEU', 'ETITE', 'INITE', 'SANIE', 'GRUIM', 'FADIA', 'MERUE', 'BAIRE', 'MUDIR', 'ORITE', 'BELAO', 'PITIA', 'SEDEX', 'EANES', 'LIENE', 'MABEL', 'CETEF', 'SIDRA', 'ARERE', 'BITIS', 'ALAIM', 'IVIRO', 'VIRES', 'CUTIS', 'TEIXE', 'RIANE', 'SAIRE', 'GANSA', 'CABUI', 'ELEDA', 'IAIAS', 'EIDER', 'ENEAS', 'SINEU', 'EFETA', 'PETIM', 'LUEEA', 'ADIEL', 'MISTE', 'AVITE', 'HEIDE', 'AIRES', 'NIAIA', 'NEREU', 'BITER', 'IRINO', 'CANSA', 'AIANE', 'TIADE', 'USNEA', 'BINEA', 'ALENA', 'REINA', 'ADIAO', 'BEREU', 'TESAS', 'OESTE', 'ANIEL', 'SIDEO', 'TAIRA', 'CLENA', 'NEVES', 'SITIO', 'LENEU', 'FINAS', 'TETEU', 'LETEU', 'GAVEA', 'TESAO', 'CRINA', 'MABEA', 'ARINA', 'TIRAO', 'AVITO', 'IVIRA', 'ASNAL', 'VASTI', 'LUTSE', 'MIDAU', 'TEIUS', 'ERUIR', 'REAIS', 'ZILRO', 'DANES', 'ERATI', 'TUBEL', 'ADENA', 'RASTE', 'SIVIA', 'TESTE', 'SAVIA', 'EMESE', 'VIREO', 'AIRAO', 'OZIAS', 'LAIME', 'JEANS', 'SAVIO', 'METIM', 'IINIS', 'LESTE', 'PENEA', 'TENEA', 'EPEIA', 'DIATE', 'ENEMA', 'UNESA', 'DETEU', 'EGESA', 'UIRUU', 'CIDRA', 'NINAR', 'SAIRA', 'DEVIR', 'FERAZ', 'TUIRA', 'QUIRE', 'AIAIA', 'SIENA', 'TEIRU', 'MATES', 'BERIX', 'NESTE', 'OSELA', 'MEREM', 'LEDRA', 'IEMEN', 'BATIS', 'TIRAS', 'EFUES', 'ETIMO', 'IETIM', 'TEERA', 'FINES', 'ADILA', 'SAIAL', 'ADIAR', 'DIETA', 'TIRAZ', 'SENES', 'NADIR', 'REFEM', 'CHAIA', 'VIRAS', 'TUBER', 'TENUE', 'ASTER', 'ENITO', 'NEVIO', 'HEFER', 'SABIN', 'NENEM', 'NADIA', 'BELAZ', 'LEPES', 'MESAS', 'UNESP', 'FINAL', 'ASTUR', 'SEFEL', 'FEDRA', 'MAIRA', 'AVEAL', 'NEDAI', 'FEIAS', 'LIPSE', 'ASNAR', 'TETIM', 'ETNIA', 'CETIM', 'PETIT', 'BITIO', 'NAVEA', 'LIZIA', 'MEZEU', 'FRINE', 'TUTSI', 'ALETE', 'BADIL', 'ANSEL', 'ESTIO', 'TIETE', 'ERETO', 'SAIRI', 'SERIO', 'EUBIO', 'DIADE', 'VADEU', 'HAVER', 'UVEAL', 'CUIRA', 'NUNES', 'BERIS', 'QUBIT', 'UVITE', 'TEIXO', 'VIRAL', 'ESTER', 'VEPSA', 'CEIAS', 'JUDEU', 'BINIU', 'MIITE', 'BEENS', 'HETEU', 'HASTE', 'SENIO', 'IATIO', 'ANESA', 'LIEGE', 'NERAL', 'CIENA', 'VILTA', 'GUIRA', 'MEIAS', 'LEIDE', 'BADIA', 'URINA', 'ETUTU', 'NIVIA', 'LEEIA', 'EUBEU', 'ELETO', 'SERUM', 'TELEX', 'BABUI', 'ETITO', 'HEDRA', 'BAIAU', 'DIREM', 'CHEDE', 'VEEME', 'SETER', 'CEFET', 'SINUS', 'LIPES', 'SEPSE', 'FABER', 'TEREM', 'EMEIO', 'DIANE', 'PEDRA', 'ILENA', 'AVEAO', 'RIADE', 'MEUNS', 'PEREA', 'ILAIS', 'UABUI', 'HIENA', 'TINEA', 'NEVIS', 'OSTIA', 'FENIX', 'PIINA', 'PATIS', 'DIREI', 'TINER', 'TIREA', 'TIRAR', 'ABELA', 'EFATA', 'METIE', 'HANSA', 'ATIVO', 'MFITI', 'ADEUS', 'BUILO', 'CAIRE', 'FETIM', 'PEANE', 'TASNA', 'IRATI', 'DAIMA', 'SEMEI', 'VIENA', 'HANES', 'PESTE', 'CAIRA', 'GEENA']

res.sort()

print("Matches já calculadas:\n")

for item in res:
	print(item)

morse = {code:letter for line in morseFile.split("\n") for letter,code in [line.split()]}

def decode(coded, maxLen=10):
    if not maxLen: return
    for size in range(1,min(5,len(coded))+1):
        code = coded[:size]
        if code not in morse: continue
        remaining = coded[size:]
        if not remaining: yield morse[code]
        for rest in decode(remaining, maxLen-1):
            yield morse[code] + rest

code = "...--.....-...-..--"

allMorse = []
for string in decode(code, maxLen=100):
	allMorse.append(string)

print(f"Possibilidades: {len(allMorse)}")

maxSize = len(max(allMorse, key=len)) // 2

dicionario = []
with open('palavras.txt', 'r', encoding='utf-8') as file:
	for line in file:
		lineStrip = line.strip()

		if (len(lineStrip)>3) and ("-" not in lineStrip) and ("." not in lineStrip) and (len(lineStrip)<=maxSize):
			dicionario.append(unidecode(lineStrip).upper())


dicionario = sorted(dicionario, key=len)
allMorse = sorted(allMorse, key=len)

match = []
for word in dicionario:
	for m in allMorse:
		if len(word)>len(m):
			break
		if (word in m) or (word[1:] in m) or (word[:-1] in m):
			if word not in match:
				match.append(word)

print(f"Matches pós calculo: {match}")