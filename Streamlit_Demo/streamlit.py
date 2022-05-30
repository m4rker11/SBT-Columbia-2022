import streamlit as st
import glob 
from PIL import Image
import json
# Creating image list from source for streamlit


image_list = []
for filename in glob.glob('WAAWImages1/*.png'): #assuming png
    im=Image.open(filename)
    image_list.append(im)


# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
horses = ['American Dreaming 2017', 'American Pharoah 2015', 'Authentic 2020', 'California Chrome 2014', 'Country Horse 2019', 'Ill Have Another 2012', 'Justify 2018', 'Mandoloun 2021', 'Nyquist 2016', 'Orb 2013', 'Rich Strike 2022']

st.title("Our group")
st.markdown("### Subdescription")
st.text(" \n")


url = "https://docs.streamlit.io/library/api-reference/text/st.markdown"

st.sidebar.markdown("# Available Horses for token")

st.sidebar.markdown("## Select your Horse") 
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

st.sidebar.selectbox('Select a Horse', horses)

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

st.sidebar.markdown("Complete Your Purchase")

if st.sidebar.button(label = 'PURCHASE'):
    st.sidebar.markdown(url, unsafe_allow_html=True)
else:
        st.sidebar.write("HAPPY HORSIN' AROUND")

# Team logo
url = "https://docs.streamlit.io/library/api-reference/text/st.markdown"

st.image('banner.png', width =1450)

# Row A
a1, a2, a3, a4, a5 = st.columns(5)
a1.image(Image.open('WAAWImages1/Always Dreaming 2017.png'), caption = 'Always Dreaming 2017')
a1.write("With possibly up to six starters, leading trainer Todd Pletcher won't lack for quantity in this year's Kentucky Derby. Always Dreaming's Florida Derby (G1) victory showed he has no lack of quality either. Winless in two summer juvenile starts, Always Dreaming returned to racing as a 3-year-old with an 11-1/2 length maiden victory at Tampa Bay Downs Jan. 25. With that and a March 4 Gulfstream Park allowance victory behind the horse, Pletcher decided to send him to the Florida Derby April 1. He handled the step up in class with ease, racing outside the leader Three Rules before sprinting away to a five length victory over State of Honor and Gunnevera. Bred by Santa Rosa Partners, Always Dreaming was a $350,000 purchase at the 2015 Keeneland September yearling sale for agent Steven Young. His owners include Brooklyn Boyz Stables, MeB Racing Stable, Teresa and Vinnie Viola, West Point Thoroughbreds, and Siena Farm. Always Dreaming is from the first crop of Bodemeister, runner-up to I'll Have Another in the 2012 Kentucky Derby. He is out of the grade III-winning In Excess mare Above Perfection, whose other progeny include the Spinaway Stakes (G1) winner Hot Dixie Chick.")
a1.write("Value : 10 ETH")


a2.image(Image.open('American Pharoah 2015.png'), caption = 'American Pharoah 2015')
a2.write("American Pharoah has won the 141st Kentucky Derby before a record-setting crowd at Churchill Downs.Victor Espinoza was aboard for this second straight Derby win, and third overall.The 5-2 favorite was in contention at the top of the stretch Saturday and pulled clear at the finish for his fifth win in six starts.Hall of Fame trainer Bob Baffert got his fourth Derby win, and also sent out third-place finisher Dortmund. Firing Line was second. The time was 2:03.02 for the 1 1/4 miles. The largest Derby crowd ever - 170,513 - looked on under sunny skies.")
a2.write("Value : 5 ETH")

a3.image(Image.open('Authentic 2020.png'), caption = 'Authentic 2020')
a3.write("Authentic is by super stud of the moment, Into Mischief. Into Mischief boasts of other progeny you may hear during the First Saturday in September with Gamine, Mischevious Alex, Lucrezia, Frank's Rockette, Shoplifted and Mia Mischief. He trains under the watchful eye of high profile conditioner Bob Baffert and for a powerhouse ownership group in Spendthrift Farm, Starlight Racing, MyRaceHorse Stable and Madaket Stables. These veteran connections understand how to campaign a horse, but some question the ability to perform against top talent at a classic distance.")
a3.write("Value : 6 ETH")

a4.image(Image.open('California Chrome 2014.png'), caption = 'California Chrome 2014')
a4.write("For decades it was California dreamin’ to think that a horse from the Left Coast could win the Kentucky Derby. Only three had — Morvich in 1922, Swaps in 1955, and Decidedly in 1962. The way his co-owner saw it, his three-year-old colt had no idea where he’d been born. “He didn’t know he’s a California-bred,” Steve Coburn said Saturday evening after 5-2 favorite California Chrome ran away from 18 rivals to win the 140th Run for the Roses by a length and three-quarters in 2 minutes, 3.66 seconds over 37-1 longshot Commanding Curve, as Danza outran Wicked Strong from Beverly-based Centennial Farms for third.")
a4.write("Value : 7 ETH")

a5.image(Image.open('Country Horse 2019.png'), caption = 'Country Horse 2019')
a5.write("Country House has faced several of his Kentucky Derby (G1) rivals in his past three races. The Bill Mott-trained son of Lookin at Lucky broke his maiden at Gulfstream Park in January and made his stakes debut in the Risen Star Stakes (G2) at Fair Grounds. Following a runner-up effort in that contest, Country House ran fourth in the Louisiana Derby (G2) in New Orleans and then shipped to Oaklawn Park for a third-place effort in the Arkansas Derby (G1).")
a5.write("Value : 7 ETH")

# Row B
b1, b2, b3, b4, b5 = st.columns(5)

b1.image(Image.open('Ill Have Another 2012.png'), caption = "I'll Have Another")
b1.write("Canadian-owned I'll Have Another ran down Bodemeister in the final furlong Saturday tot been terrific")
b1.write("Value : 5 ETH")

b2.image(Image.open('Justify 2018.png'), caption = 'Justify 2018')
b2.write("Racing in his third career start, which began at age 3, Justify lived up to anticipated hype in his stakes debut, capturing the $1 million Santa Anita Derby (G1)")
b2.write("Value : 5 ETH")

b3.image(Image.open('Mandoloun 2021.png'), caption = 'Mandoloun 2021')
b3.write("Mandaloun is a bay colt by Into Mischief and out of Brooch, who is by Empire Maker. A strong family pedigree and led by even more talent with his human connections. Conditioner Brad Cox and jockey Florent Geroux lead the Juddmonte Farms, Inc. Kentucky Derby hopeful's path towards his start on the First Saturday in May.")
b3.write("Value : 5 ETH")

b4.image(Image.open('Nyquist 2016.png'), caption = 'Nyquist 2016')
b4.write("FINISH		RACE	GRADE	DISTANCE	SURFACE	DATE")
b4.write("Value : 5 ETH")


b5.image(Image.open('Orb 2013.png'), caption = 'Orb 2013')
b5.write("The revelers were sloppy, the grounds were sloppy and the racetrack was sloppy, but Orb apparently did not mind much, and afterward his owners and trainer could not have been happier with the way the day played out.The late-closing Orb, ridden by the red-hot Joel Rosario, found a way to win despite his lack of experience on a wet track, trudging to victory in the 139th running of the Kentucky Derby on Saturday at Churchill Downs.")
b5.write("Value : 5 ETH")
# Row C

c1, c2, c3, c4, c5 = st.columns(5)
c1.image(Image.open('Rich Strike 2022.png'), caption = 'Rich Strike 2022')
c1.write("Kentucky Derby winner Rich Strike returned to the Churchill Downs work tab with a swift half-mile move in 47.2 seconds in preparation for the $1.5 million Belmont Stakes. The 80-1 upset winner of this year's $3 million Kentucky Derby presented by Woodford Reserve breezed with rider Gabe Lagunes in the saddle through an opening quarter-mile fraction of 22.8 seconds and galloped out five furlongs in 1:00.6.")
c1.write("Value : 5 ETH")
c1.button("CLICK TO PURCHASE")


## THIS IS VERSION