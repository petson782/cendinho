# -*- coding: utf-8 -*-
 
from sqlalchemy import create_engine

with open("text.txt", "r") as fiche:
    lecture = fiche.readlines()
    print lecture
    for line in lecture:
        line = line.strip()
        print line
        try:
            engine = create_engine("postgresql://Adm_Brutus:"+line+"@localhost:5432/Mydata")
            engine.connect()
            print "Mot de passe----->", line
                     
            break
        except:
            pass
