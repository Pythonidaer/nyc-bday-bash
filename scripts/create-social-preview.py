"""Rebuild the social cover and browser icons with Pillow and the local font."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
root=Path(__file__).resolve().parents[1]
a=root/'dist/assets'; pink='#ff35c9';cyan='#31edfa';dark='#10071c'
im=Image.new('RGB',(1200,630),dark);d=ImageDraw.Draw(im)
font=lambda n:ImageFont.truetype(str(a/'press-start.ttf'),n)
for x in range(-630,1200,24): d.line((x,0,x+630,630),fill='#261032',width=2)
d.rectangle((18,18,1181,611),outline=pink,width=4)
d.rectangle((36,36,1163,593),outline='#65395f',width=2)
d.text((65,66),'NYC BDAY BASH',font=font(49),fill=pink)
d.text((68,145),"RA'S 44TH / NOV 20–22, 2026",font=font(22),fill=cyan)
people=['RA','ZS','JH','MH','CF','MM','PH','JP','JC','DA'];colors=['#74C8FF','#FF8C00','#FF3B30','#1E6B3A','#8B45E8','#B6E82E','#1A3F9C','#FF7F6A','#FFE135','#FF5CA8'];inks=['#120d20','#120d20','#120d20','#F4FFF7','#F7F3FF','#120d20','#F3F7FF','#120d20','#120d20','#120d20']
for i,(name,color,ink) in enumerate(zip(people,colors,inks)):
 x=68+(i%5)*216;y=220+(i//5)*145
 d.rounded_rectangle((x,y,x+198,y+128),radius=9,fill='#757087',outline='#bcb5cc',width=3)
 d.rectangle((x+10,y+10,x+188,y+118),fill=color,outline='#292035',width=4)
 d.text((x+99,y+66),name,font=font(43),fill=ink,anchor='mm')
 if i==0:d.rounded_rectangle((x-3,y-3,x+201,y+131),radius=10,outline=cyan,width=3)
d.text((68,550),'10 FRIENDS + MUNROE',font=font(21),fill=cyan)
d.text((1130,554),'NYC / 2026',font=font(16),fill='#fff09c',anchor='ra')
im.save(a/'social-preview-v1.png',optimize=True)
icon=Image.new('RGB',(180,180),dark);q=ImageDraw.Draw(icon);q.rectangle((6,6,173,173),outline=pink,width=7);q.text((90,70),'NYC',font=font(36),fill=pink,anchor='mm');q.text((90,120),'44',font=font(40),fill=cyan,anchor='mm');icon.save(a/'apple-touch-icon.png');icon.resize((32,32)).save(a/'favicon.png')
