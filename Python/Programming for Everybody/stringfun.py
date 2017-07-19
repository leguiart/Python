text = "X-DSPAM-Confidence:    0.8475"
npos=text.find(" ")
ypos=text.find("5")
s=text[npos:ypos+1]
s=s.lstrip()
s=float(s)
print s
    
        
        
        
        