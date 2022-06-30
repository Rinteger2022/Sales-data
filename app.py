import numpy as np
#df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
#df

#your_name = st.text_input("Number")
#if your_name:
#  df[df['phone'] == your_name]
    #st.write("There is some value. Processing...")
    
 
    

st.markdown(
    """
<style>
  .reportview-container{
  background-image: url('img_girl.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;}
  </style>
  """,
 unsafe_allow_html=True
)    


#d1=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=1840897213&single=true&output=csv")
d2=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=604274609&single=true&output=csv")
#d3=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=1840897213&single=true&output=csv")
d4=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=189972757&single=true&output=csv")
d5=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=0&single=true&output=csv")
d6=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=545326512&single=true&output=csv")
d7=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=626795613&single=true&output=csv")
d8=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=521357564&single=true&output=csv")
d9=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=1735847115&single=true&output=csv")
d10=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRNTvR7paMyOTqyYXKBHkdi2iblvneADoeYC3UVMyYVoRPKmQ4EjLBsokFIS0pR1jbHSvTvSGgelI1j/pub?gid=624737364&single=true&output=csv")
d11=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRNTvR7paMyOTqyYXKBHkdi2iblvneADoeYC3UVMyYVoRPKmQ4EjLBsokFIS0pR1jbHSvTvSGgelI1j/pub?gid=61883879&single=true&output=csv")
d12=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQH85ss7_XlhuYEwAINi-nf96t6lWR1ycPIW2JiI35kBh62YWXY_oY_yaHAC9QAlor3ifgy7WOKULDf/pub?gid=426118619&single=true&output=csv")
d13=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-A7r3gghDrZeDSQKaA7KbuUhmztbVgav7K5rRwHhIVvfNX_iiQaE_aQceOgCeWOHDcvjZWvjxl7gM/pub?gid=1980744699&single=true&output=csv")
d14=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-A7r3gghDrZeDSQKaA7KbuUhmztbVgav7K5rRwHhIVvfNX_iiQaE_aQceOgCeWOHDcvjZWvjxl7gM/pub?gid=1630254723&single=true&output=csv")
d15=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSUSE-qH0Pqj8howIN6nLJVB73Rm7OEXXzKkF852cirDAN6oqekM-5fJFsLk0UF2yMvANPH1tHg7ZYD/pub?gid=413396191&single=true&output=csv")
d16=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSIvqGl_K7klS7GFJbH4PSx_WB_dg9cPtlqIoylWRujDSbMzOrAHkjIMq7gNObvFIgrTfTFXsQD5bev/pub?gid=0&single=true&output=csv")
d17=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTaLGuDu1F1It4PnX3pzxSIUku12jTCBnxcKhBCYq2J23yOANrrFV6O-Vw82Ij4tg/pub?gid=1061174711&single=true&output=csv")
d18=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTdLqSAoPgTONPSnZizTz_JlWv3NYeYowrJ7025d3iB9XdPVihFclgiCDyaSL721Q/pub?gid=2002081334&single=true&output=csv")
d19=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1114960471&single=true&output=csv")
d20=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1591696538&single=true&output=csv")
d21=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=2139327695&single=true&output=csv")
d22=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1584923803&single=true&output=csv")
d23=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1239734051&single=true&output=csv")
d24=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1518273264&single=true&output=csv")
d25=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=26635528&single=true&output=csv")
d26=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=596298606&single=true&output=csv")
d27=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=642433762&single=true&output=csv")
d28=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=849610673&single=true&output=csv")
d29=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1701301425&single=true&output=csv")
d30=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=252046113&single=true&output=csv")
d31=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=861787622&single=true&output=csv")
d32=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=761036551&single=true&output=csv")
d33=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1838378944&single=true&output=csv")
d34=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1125510532&single=true&output=csv")
d35=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSOgtXR4WBKKi3JZlsYsnWBj5N4TwySNeTlXMLT07cKpqWV_7J1iUBfydGZqloLRQ/pub?gid=1333070184&single=true&output=csv")
d36=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vTvjmT79X4qi5lARzUZoCZLwS7uShtJVLQ6pq2Zsf51fQwUmaNKYAiRT0HAQ6IIiw/pub?gid=1094974181&single=true&output=csv")

result = d2.append([d2, d4 ,d5 ,d6 ,d7 ,d8 ,d9 , d11, d12 ,d13 ,d14 ,d15 ,d16 ,d17 ,d18 ,d19 ,d20 ,d21 ,d22 ,d23 ,d24 ,d25 ,d26 ,d27 ,d28 ,d29 ,d30 ,d31 ,d32 ,d33 ,d34 ,d35 ,d36])





st.markdown('''
    <div>
    <h4 style="color:#33D1FF" "font-size:200%" align="center" >Enter Phone Number</h4>
    </div>
  ''', unsafe_allow_html=True);
if __name__ == '__main__':
    input = st.empty()    
    txt = input.text_input(" ")
    
    st.markdown('''
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    align="center";
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>
''', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

# this will put a button in the middle column
with col2:
    bt = st.button("Search")



    if bt:
        #txt = "txt"
        #input.text_input("Insert Number:", value=txt)
        res = result.isin([txt]).any().any()
        if res :
            st.markdown('''
<div>
  <h3 style="color:red" "font-size:200%" align="center" >This value exists in Dataframe</h3>
</div>
 ''', unsafe_allow_html=True);
           #st.write("This value exists in Dataframe")
        else :
            st.markdown('''
<div>
  <h3 style="color:green" "font-size:200%" align="center" >not exists in Dataframe</h3>
</div>
 ''', unsafe_allow_html=True);

          #st.write("This value does not exists in Dataframe")
    
    
    
#CompanyName=st.text_input("Company")
#Brandname=st.text_input("Brand")
#ContactNumber=st.text_input("Number")
