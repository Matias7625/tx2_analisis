import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from PIL import Image
image = Image.open("345c9c23f8ac9ba092aa634edea5b83f.jpg")
translator = Translator()
st.markdown(
    """
    <h1 style='text-align: center; color: red;'>¡Estas siendo juzgado por la calaca!.</h1>
   
    """,
    unsafe_allow_html=True
)

st.image(image, width=350)
st.subheader("Te cuidado con lo que dices si no le gusta a la calac te va a decir cosas feas")
with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                La calaca te juzgara por los siguientes valores ten cuidado....
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 


with st.expander('Preparte para ser juzgado en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:

        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        #blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( """
            'Le agradaste a la calasa 😊'
            'Y mira te va invitar a tomar algo'
            """)
            st.image("skull-hand-with-beer-vector.jpg")
        elif x <= -0.5:
            st.write( """
                'Enojate a la calaca... 😔'
                'Pinche desgraciado ya te las veras comingo cuando te vea'
                """)
            st.image("skeleton-meme-skeleton.gif")
        else:
            st.write( 'La calaca esta neutral 😐 eso no suele pasar.....')

with st.expander('Traducerlo al idioma de la calaca'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct())) 
