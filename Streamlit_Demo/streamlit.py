
### MOCK STREAMLIT FRONTEND

#This is a non-functional frontend to visually show how an NFT page may be formatted using streamlit


#Imports including Image from PIL 

import streamlit as st
from PIL import Image

# Page setting for wide layout using .css file
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Demo notes:
# 1. A functional streamlit page would read and use information provided by the json files we developed
# 2. For presentation purposes, we used the "name" characteristic to show potential sidebar interactions and layout

# For demo purposes, we used the horse names to be later used in the sidebar
horses = ['American Dreaming 2017', 'American Pharoah 2015', 'Authentic 2020', 'California Chrome 2014', 'Country Horse 2019', 'Ill Have Another 2012', 'Justify 2018', 'Mandoloun 2021', 'Nyquist 2016', 'Orb 2013', 'Rich Strike 2022',
'Aristides 1875', 'Barbaro 2006', 'Monarchos 2001', 'Ponder 1949', 'Majestic Prince 1969', 'Chateaugay 1963', 'Secretariat 1973', 'Donerail 1913', 'Dust commander 1970', 'Seattle Slew 1977', 'Sir Barton 1919', 'Gallant Fox 1930', 'Omaha 1935',
'War Admiral 1937', 'Whirlaway 1941', 'Count Fleet 1943', 'Assault 1946', 'Citation 1948']


# General title
st.title("We Are All Winners")
st.markdown("### The Kentucky Derby horse winners are meant to represent how we are all winners for getting through this bootcamp together. The SBTs are our parting gifts to our fellow classmates.")
st.text(" \n")

# Real NFT page link for demo

url = "https://sbt-columbia-2022.vercel.app/"


# Sidebar construction
st.sidebar.markdown("# Available Horses for Token")
st.sidebar.image('profile.png')


st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

st.sidebar.markdown("## Select your Horse") 
st.sidebar.write("")


st.sidebar.selectbox('Select a Horse', horses)

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

st.sidebar.markdown("Complete Your Purchase")
st.sidebar.write("")
st.sidebar.write("")

if st.sidebar.button(label = 'PURCHASE'):
    st.sidebar.markdown(url, unsafe_allow_html=True)
else:
        st.sidebar.write("HAPPY HORSIN' AROUND")

# Team logo

st.image('running-horses.png', width =1450)


# Row layout to display each NFT image
# Row A
a1, a2, a3, a4, a5 = st.columns(5)
a1.image(Image.open('We Are All Winners Images/Always Dreaming 2017.png'), caption = 'Always Dreaming 2017')
a1.write("Always Dreaming broke well and settled just behind the early leader State of Honor with good position on the rail. After half a mile, jockey John R. Velazquez moved him to the outside of State of Honor and the two raced together into the far turn. When other horses then started to challenge for the lead, Always Dreaming quickly responded by drawing away and opening a lead of several lengths in the stretch. Longshot Lookin At Lee made a late run to finish second, but Always Dreaming was never threatened, winning by 2+3⁄4 lengths. ")
a1.write("### Value : 10 ETH")
a1.write("")

a2.image(Image.open('We Are All Winners Images/American Pharoah 2015.png'), caption = 'American Pharoah 2015')
a2.write("American Pharoah has won the 141st Kentucky Derby before a record-setting crowd at Churchill Downs.Victor Espinoza was aboard for this second straight Derby win, and third overall.The 5-2 favorite was in contention at the top of the stretch Saturday and pulled clear at the finish for his fifth win in six starts.Hall of Fame trainer Bob Baffert got his fourth Derby win, and also sent out third-place finisher Dortmund. Firing Line was second. The time was 2:03.02 for the 1 1/4 miles. The largest Derby crowd ever - 170,513 - looked on under sunny skies.")
a2.write("### Value : 5 ETH")
a2.write("")

a3.image(Image.open('We Are All Winners Images/Authentic 2020.png'), caption = 'Authentic 2020')
a3.write("Authentic is by super stud of the moment, Into Mischief. Into Mischief boasts of other progeny you may hear during the First Saturday in September with Gamine, Mischevious Alex, Lucrezia, Frank's Rockette, Shoplifted and Mia Mischief. He trains under the watchful eye of high profile conditioner Bob Baffert and for a powerhouse ownership group in Spendthrift Farm, Starlight Racing, MyRaceHorse Stable and Madaket Stables. These veteran connections understand how to campaign a horse, but some question the ability to perform against top talent at a classic distance.")
a3.write("### Value : 6 ETH")
a3.write("")

a4.image(Image.open('We Are All Winners Images/California Chrome 2014.png'), caption = 'California Chrome 2014')
a4.write("For decades it was California dreamin’ to think that a horse from the Left Coast could win the Kentucky Derby. Only three had — Morvich in 1922, Swaps in 1955, and Decidedly in 1962. The way his co-owner saw it, his three-year-old colt had no idea where he’d been born. “He didn’t know he’s a California-bred,” Steve Coburn said Saturday evening after 5-2 favorite California Chrome ran away from 18 rivals to win the 140th Run for the Roses by a length and three-quarters in 2 minutes, 3.66 seconds over 37-1 longshot Commanding Curve, as Danza outran Wicked Strong from Beverly-based Centennial Farms for third.")
a4.write("### Value : 7 ETH")
a4.write("")

a5.image(Image.open('We Are All Winners Images/Country House 2019.png'), caption = 'Country Horse 2019')
a5.write("Country House has faced several of his Kentucky Derby (G1) rivals in his past three races. The Bill Mott-trained son of Lookin at Lucky broke his maiden at Gulfstream Park in January and made his stakes debut in the Risen Star Stakes (G2) at Fair Grounds. Following a runner-up effort in that contest, Country House ran fourth in the Louisiana Derby (G2) in New Orleans and then shipped to Oaklawn Park for a third-place effort in the Arkansas Derby (G1).")
a5.write("### Value : 7 ETH")
a5.write("")

# Row B
b1, b2, b3, b4, b5 = st.columns(5)

b1.image(Image.open("We Are All Winners Images/I'll Have Another 2012.png"), caption = "I'll Have Another")
b1.write("Canadian-owned I’ll Have Another ran down Bodemeister in the final furlong Saturday to win the Kentucky Derby. 'He’s an amazing horse. I kept telling everybody, from the first time I met him, I knew he was the one. I knew he was good,' Gutierrez said. 'I said in an interview, even if they allowed me to pick from the whole rest of the field, I would have stayed with him, 100 percent, no doubt about it.' But a record crowd of 165,307 looking on didn’t know 15-1 shot I’ll Have Another had the goods until the 20-horse field turned for home. That’s when Gutierrez, who moved up between horses around the final turn, positioned his colt not far from the rail and set him down to run. I’ll Have Another, owned by J. Paul Reddam of Windsor, Ont., overhauled a tiring Bodemeister to win by 1 1-2 lengths.")
b1.write("### Value : 5 ETH")
b1.write("")

b2.image(Image.open('We Are All Winners Images/Justify 2018.png'), caption = 'Justify 2018')
b2.write("Justify (foaled March 28, 2015) is an American Thoroughbred racehorse who is known for being the thirteenth winner of the American Triple Crown. He also was the first horse since Apollo in 1882 to win the Kentucky Derby without racing as a two-year-old. Justify first attracted attention with a win in his debut race on February 18, 2018. He followed up with two more victories, including the Grade One Santa Anita Derby that qualified him for the 2018 Kentucky Derby. Justify then won that race and the 2018 Preakness Stakes and 2018 Belmont Stakes to win the Triple Crown.")
b2.write("### Value : 5 ETH")
b2.write("")

b3.image(Image.open('We Are All Winners Images/Mandoloun 2021.png'), caption = 'Mandoloun 2021')
b3.write("Mandaloun is a bay colt by Into Mischief and out of Brooch, who is by Empire Maker. A strong family pedigree and led by even more talent with his human connections. Conditioner Brad Cox and jockey Florent Geroux lead the Juddmonte Farms, Inc. Kentucky Derby hopeful's path towards his start on the First Saturday in May.")
b3.write("### Value : 5 ETH")
b3.write("")

b4.image(Image.open('We Are All Winners Images/Nyquist 2016.png'), caption = 'Nyquist 2016')
b4.write("Nyquist is the second Derby winner to win the race as an undefeated two-year-old season champion. The 2016 Kentucky Derby, which Nyquist won by 1¼ lengths, was the horse's last win. Nyquist is a 5th generation descendant of Secretariat. He is a champion American Thoroughbred racehorse who won both the 2016 Kentucky Derby and 2015 Breeders' Cup Juvenile, only the second horse to complete the Juvenile-Derby double.[3] He became the eighth undefeated winner of the Kentucky Derby, and the first since Big Brown in 2008. He received the 2015 Eclipse Award for Champion Two-Year-Old. He is the second Kentucky Derby winner after Morvich to win the race while undefeated after winning Champion Two Year Old the year")
b4.write("### Value : 5 ETH")
b4.write("")

b5.image(Image.open('We Are All Winners Images/Orb 2013.png'), caption = 'Orb 2013')
b5.write("The revelers were sloppy, the grounds were sloppy and the racetrack was sloppy, but Orb apparently did not mind much, and afterward his owners and trainer could not have been happier with the way the day played out.The late-closing Orb, ridden by the red-hot Joel Rosario, found a way to win despite his lack of experience on a wet track, trudging to victory in the 139th running of the Kentucky Derby on Saturday at Churchill Downs.")
b5.write("### Value : 5 ETH")
b5.write("")

# Row C

c1, c2, c3, c4, c5 = st.columns(5)
c1.image(Image.open('We Are All Winners Images/Lawrin 1938.png'), caption = 'Lawrin 1938')
c1.write("Lawrin was an American thoroughbred racehorse owned by Herbert M. Woolf who won the 1938 Kentucky Derby. He was the son of Insco. He is the only Kansas-bred winner of the Kentucky Derby and the first Kentucky Derby winner ridden by the great jockey Eddie Arcaro.")
c1.write("### Value : 5 ETH")
c1.write("")

c2.image(Image.open('We Are All Winners Images/Barbaro 2006.png'), caption = 'Barbaro 2006')
c2.write("Barbaro is known for one of the largest margins of victory at the Kentucky Derby– 6 ½ lengths: The horses that shared the fifth-largest winning margin had very different tales to tell. Barbaro started the Derby as second favorite and maintained his unbeaten record in the Run for the Roses with his outstanding victory.")
c2.write("### Value : 5 ETH")
c2.write("")

c3.image(Image.open('We Are All Winners Images/Monarchos 2001.png'), caption = 'Monarchos 2001')
c3.write("In 2001, Monarchos won the Kentucky Derby. He was only the second horse, after Secretariat, to run the Derby in under 2:00. The gray son of Maria's Mon and Regal Band by Dixieland Band won four races with a second and three thirds in 10 starts from 2000-2002 and earned more than $1.72 million. Monarchos' greatest triumph came in the 2001 Derby at Churchill Downs, where he was bumped by Point Given at the start and came from the outside at the stretch to catch Congaree and win by 4 3/4 lengths over Invisible Ink with Congaree third. His time of 1:59.97 with Jorge Chavez aboard was just behind the 1973 Triple Crown champion's record 1:59.40.")
c3.write("### Value : 5 ETH")
c3.write("")

c4.image(Image.open('We Are All Winners Images/Ponder 1949.png'), caption = 'Ponder 1949')
c4.write("The American Derby was perhaps his most shining performance. Victory came as it usually does to him. He let the pack take off in full cry, and when he got ready with his late run, nothing could stay in front of him. But this race he won in what may be called the hard way. He was, to all appearances, securely boxed in on the rail as the field rounded the far turn. But he seems to be an easy colt to handle during a race, and Jockey Steve Brooks was able to take him back and send him around the outside. Once clear, he took off with the rush that had gained the Kentucky Derby for him, and won by 2 1/4 lengths drawing away.")
c4.write("### Value : 5 ETH")
c4.write("")

c5.image(Image.open('We Are All Winners Images/Majestic Prince 1969.png'), caption = 'Majestic Prince 1969')
c5.write("Given his regal name by McMahon, Majestic Prince was turned over to trainer Johnny Longden, who was racetrack nobility himself. In 1966, Longden had retired as the sport's all-time winningest jockey. When he made it to the racetrack in November of 1968, Majestic Prince ran like his name by winning his two starts at 2. He triumphed in his career debut at Bay Meadows by 2 ¾ lengths but prevailed by only a nose at Santa Anita in his second start. At 3, he became dominant. He began his 1969 campaign by reeling off wins in the Los Feliz, San Vicente and San Jacinto Stakes and then cemented his status as the West’s best 3-year-old by romping to an scintillating eight-length victory under regular rider Bill Hartack in the Santa Anita Derby over what was described in Sports Illustrated as “nine hopelessly outclassed rivals.” In an era marked by short rest between races, he was then shipped to Kentucky and just a week before the Kentucky Derby notched a six-length win in the Stepping Stone Purse in the stakes-record time of 1:21 3/5 for seven furlongs.")
c5.write("### Value : 5 ETH")
c5.write("")


# Row D 
d1, d2, d3, d4, d5 = st.columns(5)
d1.image(Image.open('We Are All Winners Images/Rich Strike 2022.png'), caption = 'Rich Strike 2022')
d1.write("Rich Strike broke poorly from the outside post position and raced well back. He was in eighteenth place after the first half mile, seventeen lengths behind the leaders. He began to make up ground on the final turn, while shifting out four wide. Rich Strike was only 4+3⁄4 lengths behind leader Epicenter at the one mile mark but was in heavy traffic. In the stretch, he found racing room near the rail, weaved around a tiring Messier and then launched a sustained drive to the inside of Epicenter, drawing clear in the final strides to win by three-quarters of a length, with an 80-1 Longshot upset.")
d1.write("### Value : 5 ETH")
d1.write("")

d2.image(Image.open('We Are All Winners Images/Aristides 1875.png'), caption = 'Aristides 1875')
d2.write("1875 was the first year of the Kentucky Derby. Oliver Lewis (1856-1924), the Black American jockey who rode the colt Aristides, won the first Kentucky Derby on May 17, 1875. His time of two minutes 37.75 seconds set an American record over the mile and a half distance, earning a purse of just $2,850. The winning thoroughbred was trained by renowned Black American trainer Ansel Williamson.")
d2.write("### Value : 5 ETH")
d2.write("")


d3.image(Image.open('We Are All Winners Images/Chateaugay 1963.png'), caption = 'Chateaugay 1963')
d3.write("Panamanian jockey Braulio Baeza won the Kentucky Derby in 1963 with winning horse Chateaugay, a horse from Lexington’s Darby Dan Farm. He was the first Latino jockey to win the Run for the Roses. When the gate opened, Never Bend quickly took the lead and by the 1⁄4 mile mark No Robbery had moved into second place along the inside rail with Candy Spots sitting third. After running in sixth place through the first three-quarters of a mile, coming out of the backstretch, Chateaugay moved to the far outside and raced into fourth place behind the three leaders. As they turned for home, jockey Braulio Baeza spotted an opening between the second- and third-place horses. He raced through it to pull alongside Never Bend and then moved ahead to win the race by 1+1⁄4 lengths.")
d3.write("### Value : 5 ETH")
d3.write("")

d4.image(Image.open('We Are All Winners Images/Secretariat 1973.png'), caption = 'Secretariat 1973')
d4.write("Probably the most recognizable name of all the horses that have participated in the Kentucky Derby, Secretariat won in 1973, which was the 99th running of the race. Secretariat is still a household name because this horse went on to win the Triple Crown and still holds the Derby record, completing the course in 1:59:40. Secretariat still holds the stakes records for all three of the Triple Crown races.")
d4.write("### Value : 5 ETH")
d4.write("")

d5.image(Image.open('We Are All Winners Images/Donerail 1913.png'), caption = 'Donerail 1913')
d5.write("Donerail was the biggest upset in Derby history, he ran down the favorite, Ten Point on the home stretch and clocked the fastest time in history. Donerail went off at a 91-1 longshot to win the Kentucky Derby. Donerail was, by far, the biggest long-shot to ever win the Derby. Bred, owned and trained by Tom P. Hayes of Scott County, who named the colt for a settlement on the Fayette-Scott County line that no longer exists")
d5.write("### Value : 5 ETH")
d5.write("")


# Row E

e1, e2, e3, e4, e5 = st.columns(5)
e1.image(Image.open('We Are All Winners Images/Dust Commander 1970.png'), caption = 'Dust Commander 1970')
e1.write("Hunter S. Thompson's seminal 1970 essay 'The Kentucky Derby is Decadent and Depraved' detailed the running of the Derby won by Dust Commander. The name 'Dust Commander' is derived from his dam, Dust Storm, and his sire, Bold Commander. A descendant of Nearco, Dust Commander was bred by the Pullen brothers. He was owned by Robert E. Lehmann and trained by Don Combs. His dam Dust Storm was descended from the American broodmare Laughing Queen who was also the female-line ancestor of Tom Fool.")
e1.write("### Value : 5 ETH")
e1.write("")

e2.image(Image.open('We Are All Winners Images/Seattle Slew 1977.png'), caption = 'Seattle Slew 1977')
e2.write("Seattle Slew won the Derby in 1977 but didn't stop there. This horse went on to win the Triple Crown and was the 10th horse to do so. At the time, Seattle Slew became the only undefeated Triple Crown winner. This horse's undefeated career has gone down in racing history as one of the most impressive of all.")
e2.write("### Value : 5 ETH")
e2.write("")


e3.image(Image.open('We Are All Winners Images/Sir Barton 1919.png'), caption = 'Sir Barton 1919')
e3.write("The Kentucky thoroughbred Sir Barton was the first horse to win the Kentucky Derby, Preakness Stakes and Belmont Stakes – now known as the Triple Crown – in 1919, inspiring the yearly pursuit of racing glory that continues to fascinate us. For nearly a century, however, achievements by Man o’ War and other great horses of the era overshadowed those of Sir Barton")
e3.write("### Value : 5 ETH")
e3.write("")

e4.image(Image.open('We Are All Winners Images/Gallant Fox 1930.png'), caption = 'Gallant Fox 1930')
e4.write("Winning the Triple Crown is the most coveted accomplishment in the sport of horse racing. It takes a super horse to sweep the Kentucky Derby, the Preakness Stakes, and the Belmont Stakes because of the proximity of their dates and because the horses running in them are the best of the best. Though Sir Barton was the first horse to win all three in 1919, the term “Triple Crown” wasn’t around until Gallant Fox won it in 1930. Because of that, he is known as “The Father of the Triple Crown”.")
e4.write("### Value : 5 ETH")
e4.write("")

e5.image(Image.open('We Are All Winners Images/Omaha 1935.png'), caption = 'Omaha 1935')
e5.write("Omaha, (foaled 1932), American racehorse (Thoroughbred) who in 1935 became the third winner of the American Triple Crown—the Kentucky Derby, the Preakness Stakes, and the Belmont Stakes. He was sired by Gallant Fox (winner of the Triple Crown in 1930) and was the only Triple Crown winner sired by a Triple Crown winner.")
e5.write("### Value : 5 ETH")
e5.write("")

# Row F

f1, f2, f3, f4, f5 = st.columns(5)
f1.image(Image.open('We Are All Winners Images/War Admiral 1937.png'), caption = 'War Admiral 1937')
f1.write("In 1937, War Admiral, an American Thoroughbred racehorse became the fourth winner of the American Triple Crown—the Kentucky Derby, the Preakness Stakes, and the Belmont Stakes. His dramatic 1938 race against Seabiscuit, the leading money winner of 1937 and a fan favorite, captured the imagination of Americans during the Great Depression. Seabiscuit never won a Kentucky Derby because of War Admiral’s challenge. ")
f1.write("### Value : 5 ETH")
f1.write("")

f2.image(Image.open('We Are All Winners Images/Whirlaway 1941.png'), caption = 'Whirlaway 1941')
f2.write("Whirlaway was a champion American Thoroughbred racehorse who is the fifth winner of the American Triple Crown. He also won the Travers Stakes after his Triple Crown sweep to become the first and only horse to win all four races. He holds the record for the longest winning margin in the Kentucky Derby with fellow Triple Crown winner Assault, as they both won the Derby by 8 lengths. Whirlaway was widely known as 'Mr. Longtail' because his tail was especially long and thick and it would blow far out behind him during races, flowing dramatically in the wind.")
f2.write("### Value : 5 ETH")
f2.write("")

f3.image(Image.open('We Are All Winners Images/Count Fleet 1946.png'), caption = 'Count Fleet 1943')
f3.write("Count Fleet was a champion American Thoroughbred racehorse who is the sixth winner of the American Triple Crown. He won the Belmont Stakes by a then record margin of twenty-five lengths. After an undefeated season, he was named the 1943 Horse of the Year and champion three-year-old. Also a champion at age two, he is ranked as one of the greatest American racehorses of the twentieth century, ranking fifth on the Top 100 Racehorses of the 20th Century. He was inducted into the National Museum of Racing and Hall of Fame in 1961.")
f3.write("### Value : 5 ETH")
f3.write("")

f4.image(Image.open('We Are All Winners Images/Assault 1946.png'), caption = 'Assault 1946')
f4.write("Early life wasn’t kind to Assault. He suffered an assortment of illness and injuries, including stepping on a surveyor's spike, leaving his hoof deformed and the horse crippled. They worked on the hoof to the point where he walked with just a limp. In 1946, Assault was listed as the fourth choice among bettors at the Derby. Spy Song was the early leader as Assault raced in midpack. Heading into the top of the stretch with 25-year-old Warren Mehrtens aboard, Assault burst through on the rail and rolled home to a stunning eight-length victory. It equaled the largest winning margin in Derby history. His time of 2:06 3/5 was comparatively slow, five seconds off the great Whirlaway’s then track record.")
f4.write("### Value : 5 ETH")
f4.write("")

f5.image(Image.open('We Are All Winners Images/Citation 1948.png'), caption = 'Citation 1948')
f5.write("When thinking of Triple Crown winners, the mind often travels to those of the 1970s, namely Secretariat. But a quarter of a century before the big red colt hailing from Meadow Stud took the world by storm, there was a horse who had just the same become a household name; not for his fiery coat or an indelible 31-length romp in the Belmont Stakes, but for a rare grit and dominance displayed by few throughout the long and storied annals of racing. His name was Citation. Over a fast track at Belmont Park on June 12, 1948, Citation powered to an eight-length win, capturing racing’s grandest prize while tying fellow Triple Crown winner Count Fleet’s stakes record of 2:28 1/5. But his story didn’t end with a win in the elusive Triple Crown; his accomplishments had only just begun. Citation would then win nine more starts as a 3-year-old before being named 1948’s Horse of the Year. With 1949 marred by injury, the strapping colt would take the year off. Returning a winner in 1950, he established a modern record 16 consecutive wins")
f5.write("### Value : 5 ETH")
f5.write("")


# Row G 

g1, g2, g3, g4, g5 = st.columns(5)
g1.image(Image.open('We Are All Winners Images/Affirmed 1978.png'), caption = 'Affirmed 1978')
g1.write("The 1978 Kentucky Derby was the 104th running of the Kentucky Derby. Affirmed, under jockey Steve Cauthen, won the race by 1 1/2 lengths over Alydar. Believe It finished 3rd, 1 1/4 lengths behind Alydar, and 30-1 longshot Darby Creek Road finished 4th. In 1978, Affirmed became the 11th winner of the Triple Crown of American horse racing—the Kentucky Derby, the Preakness Stakes, and the Belmont Stakes.")
g1.write("### Value : 5 ETH")
g1.write("")

g2.image(Image.open('We Are All Winners Images/Smarty Jones 2004.png'), caption = 'Smarty Jones 2004')
g2.write("Smarty Jones won the Kentucky Derby in 2004 (as well as the Preakness Stakes). This horse ended a decades-long wait when he became the first undefeated horse to win the Derby since Seattle Slew's 1977 win. The jockey, Stewart Elliott, became the first jockey to win a Kentucky Derby debut since Ronnie Franklin won with Spectacular Bid in the 1979 Derby. On a rainy May 1, 2004, Smarty Jones entered the Kentucky Derby, where he became the post time favorite, and won. Servis and Elliott became the first trainer/jockey combination in 25 years to win the Kentucky Derby in their debut appearance.")
g2.write("### Value : 5 ETH")
g2.write("")


g3.image(Image.open('We Are All Winners Images/Spectacular Bid 1979.png'), caption = 'Spectacular Bid 1979')
g3.write("This horse was a champion throughout its 1978 two-year-old season, and it also won the 1979 Kentucky Derby, a race for three-year-old horses. Spectacular Bid's jockey, Ronnie Franklin, won the race in his Kentucky Derby debut. Spectacular Bid raced 30 times and won 26 of those races. He finished second twice, third once, and fourth in the other race. (He was a 2-year-old and didn’t like the slop at Monmouth Park.) That’s an 86.1% winning percentage, third only to Native Dancer and Man O’ War among the top tier of horses of the 20th century, according to the Blood-Horse magazine")
g3.write("### Value : 5 ETH")
g3.write("")

g4.image(Image.open('We Are All Winners Images/Genuine Risk 1980.png'), caption = 'Genuine Risk 1980')
g4.write("Genuine Risk took the roses in 1980 and is one of only three fillies to win the Kentucky Derby. The others were Regret in 1915 and Winning Colors in 1988. Genuine Risk was a chestnut filly bred in Kentucky by Sally Humphrey. She was sired by Exclusive Native, a top-class track performer who was even better as a breeding stallion, siring the Triple Crown winner Affirmed. Her dam Virtuous was descended from the British broodmare Iona, a half-sister to Ocean Swell and the grandmother of Tomy Lee.")
g4.write("### Value : 5 ETH")
g4.write("")

g5.image(Image.open('We Are All Winners Images/Regret 1915.png'), caption = 'Regret 2015')
g5.write("Regret's victory brought an avalanche of newspaper coverage to Churchill Downs' signature race. Her victory against males was a turning point in elevating the race’s popularity nationwide, and since then the Kentucky Derby has enjoyed a prestige equal to any sporting event in the world. Regret was the first filly (female young horse) to win the Kentucky Derby against males colts. 'The race needed only a victory by Regret to create some more coast-to-coast publicity to really put it over. She did not fail us. Regret made the Kentucky Derby an American institution.'")
g5.write("### Value : 5 ETH")
g5.write("")


# Row H

h1, h2, h3, h4, h5 = st.columns(5)
h1.image(Image.open('We Are All Winners Images/Winning Colors 1988.png'), caption = 'Winning Colors 2015')
h1.write("Winning Colors was an American Hall of Fame Champion Thoroughbred racehorse and one of only three fillies to ever win the Kentucky Derby. Winning Colors was bred by Echo Valley Farm near Georgetown, Kentucky owned by Donald & Shirley Sucher. The couple had previously bred the Hall of Fame filly, Chris Evert. During her racing career she was owned by Eugene V. Klein and trained by D. Wayne Lukas. Her sire, Caro, was a top-class performer (rated 133 by Timeform), whose wins included the Poule d'Essai des Poulains, Prix Ganay and Prix d'Ispahan, before becoming a very successful breeding stallion. Caro's other progeny included Madelia, Crystal Palace, Cozzene Theia and Siberian Express. Winning Colors dam, All Rainbows won seven races and finished third in the Delaware Oaks and was also a half-sister to Chris Evert.")
h1.write("### Value : 5 ETH")
h1.write("")

h2.image(Image.open('We Are All Winners Images/Mint That Bird 2009.png'), caption = 'Mint That Bird 2009')
h2.write("Mine That Bird is known for one of the largest margins of victory at the Kentucky Derby– 6 ½ lengths: He has the fifth-largest winning margin. Mine That Bird was the classic rags-to-riches tale. The $9,000 purchase ran well as a 2-year-old in Canada but failed in the Breeders’ Cup Juvenile and, after switching stables to Chip Woolley, he was driven across the country after finishing fourth in the Sunland Derby. On a wet track, Mine That Bird was lengths behind the field early but was guided along the fence by Calvin Borel and surged away to his big victory at odds of 50-1. He showed that effort was no fluke when finishing second in the Preakness to Rachel Alexandra and third in the Belmont, but didn’t regain the same level of form again.")
h2.write("### Value : 5 ETH")
h2.write("")


h3.image(Image.open('We Are All Winners Images/Kingman 1891.png'), caption = 'Kingman 1891')
h3.write("Kingman was an American Thoroughbred racehorse owned by Kinzea Stone of Georgetown, Kentucky and the winner of the 1891 Kentucky Derby, Phoenix Stakes and Latonia Derby. He holds the record for the slowest winning time ever recorded at a Kentucky Derby, at 2:52:25. ")
h3.write("### Value : 5 ETH")
h3.write("")

h4.image(Image.open('We Are All Winners Images/Johnstown 1939.png'), caption = 'Johnstown 1939')
h4.write("Johnstown is known for one of the largest margins of victory at the Kentucky Derby– 8 lengths: A winner of seven of his 12 juvenile starts, Johnstown arrived at Churchill Downs a heavy favorite after winning the Wood Memorial. He didn’t get out of the gate well, but had found the lead by a mile and romped away to his eight-length triumph. Big things were expected in the Preakness, but he didn’t handle the muddy conditions and finished fifth. He returned to win the Belmont and went on to win seven of his nine starts that year.")
h4.write("### Value : 5 ETH")
h4.write("")

h5.image(Image.open('We Are All Winners Images/Old Rosebud 1914.png'), caption = 'Old Rosebud 1914')
h5.write("Old Rosebud is known for one of the largest margins of victory at the Kentucky Derby– 8 lengths: The first of four horses to win the Kentucky Derby by eight lengths, Old Rosebud is one of the most remarkable and arguably most underappreciated horses in the U.S. Thoroughbred racing history. The Derby, won in track record time, was his 11th consecutive victory. An injury in his next start looked to have ended the gelding’s career, but he returned nearly three years later and won 15 of his 21 starts as a 7-year-old, including many of the major handicap prizes. He was still in training as an 11-year-old when he was euthanized after another injury.")
h5.write("### Value : 5 ETH")
h5.write("")










