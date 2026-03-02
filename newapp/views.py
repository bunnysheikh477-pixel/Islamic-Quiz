from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request,'index.html')


def list(request):
    lists=[
        {"(Qur’an 65:3) : And whoever puts his trust in Allah, then He will suffice him."},
        {"(Qur’an 2:286) : Allah does not burden a soul beyond what it can bear."},
        {"When you rely upon Allah, you rely upon the One who never fails."},
        {"Tie your camel and trust in Allah. (Prophet Muhammad ﷺ – Hadith)"},
        {"No matter how heavy your heart feels, Allah is closer than your worries."},
        {"(Qur’an 94:6):Indeed, with hardship comes ease."},
        {"Patience is not the absence of hardship, but faith during hardship."},
        {"Allah tests those whom He loves.__(Hadith)"},
        {"Every difficulty is a doorway to a greater reward from Allah."},
        {"Be patient; what is written for you will never miss you."},
        {"The best of you are the best to their families.(Prophet Muhammad ﷺ)"},
        {"A strong family is built on prayer, patience, and mercy."},
        {"Kindness in the home is a form of worship."}, 
        {"Teach your children Islam not only with words, but with your actions."}, 
        {"A peaceful home begins with remembrance of Allah."}, 
        {"Allah’s mercy is greater than any sin."}, 
        {"When you make duʿā, believe that Allah is listening."}, 
        {"Live for Allah, and Allah will take care of your life."},
        {"Prepare for the Akhirah as if you will meet Allah tomorrow."},     
        {"Prophet Muhammad ﷺ said:Beware! The Fire has been surrounded by desires and the Paradise by difficulties."},     
    ]
    
    quote=random.choice(lists)
    return render(request,'index.html',{'quote':quote})


    