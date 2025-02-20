import pandas as pd
import streamlit as st
import pickle


st.title('players market value predictor')
model=pickle.load(open('fifa_model.sav','rb'))
# ['age', 'height_cm', 'weight_kgs', 'positions', 'potential',
#        'international_reputation(1-5)', 'weak_foot(1-5)', 'reactions',
#        'balance', 'jumping', 'stamina', 'strength', 'vision', 'penalties',
#        'composure', 'sliding_tackle']

pos=['GK', 'CAM', 'CDM', 'LW', 'ST', 'CB', 'LB', 'RW', 'CM', 'RM', 'LM','RB', 'CF', 'LWB', 'RWB']
col1,col2,col3=st.columns(3)
with col1:
    position=st.selectbox('Position',sorted(pos))
with col2:
    ovr=st.number_input('Overall Rating',min_value=45,max_value=95,step=1)
with col3:
    ag=st.number_input("Age",min_value=18,max_value=40,step=1)

st.markdown("<h3 style='font-size:20px;'>Attributes</h3>", unsafe_allow_html=True)
col1,col2,col3=st.columns(3)
with col1:
    bal=st.number_input('Balance',min_value=10,max_value=100,step=1)
with col2:
    jump=st.number_input('Jumping',min_value=10,max_value=100,step=1)
with col3:
    react=st.number_input("Reaction",min_value=10,max_value=100,step=1)
col1,col2,col3=st.columns(3)
with col1:
    vis=st.number_input('Vision',min_value=10,max_value=100,step=1)
with col2:
    pen=st.number_input('Penalties',min_value=10,max_value=100,step=1)
with col3:
    comp=st.number_input("Composure",min_value=10,max_value=100,step=1)
col1,col2,col3=st.columns(3)
with col1:
    tack=st.number_input('Tackling',min_value=10,max_value=100,step=1)
with col2:
    foot=st.number_input('Weak Foot',min_value=1,max_value=5,step=1)
with col3:
    national=st.number_input("International Reputation",min_value=1,max_value=5,step=1)
st.markdown("<h3 style='font-size:20px;'>Physical Details</h3>", unsafe_allow_html=True)
col1,col2,col3,col4=st.columns(4)
with col1:
    height=st.number_input('Height in CM',min_value=135,max_value=217)
with col2:
    weight=st.number_input('Wight in KG',min_value=54,max_value=98)
with col3:
    stamina=st.number_input("Stamina",min_value=20,max_value=100,step=1)
with col4:
    strength=st.number_input("Strength",min_value=10,max_value=100,step=1)


if st.button("Expected Market Value"):

    df=pd.DataFrame({'age':[ag],
                     'height_cm':[height],
                     'weight_kgs':[weight],
                     'positions':[position],
                     'potential':[ovr],
                     'international_reputation(1-5)':[national],
                     'weak_foot(1-5)':[foot],
                     'reactions':[react],
                     'balance':[bal],
                     'jumping':[jump],
                     'stamina':[stamina],
                     'strength':[strength],
                     'vision':[vis],
                     'penalties':[pen],
                     'composure':[comp],
                     'sliding_tackle':[tack]
    })

    result=model.predict(df)
    value=round(result[0],1)
    st.text(f"Expected Market value of Player is {value} Million Euros")