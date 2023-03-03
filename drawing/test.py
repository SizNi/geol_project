import drawSvg as draw

width = 100
height = 100
d = draw.Drawing(width, height, origin=(0, 0), displayInline=False)
c = draw.Ellipse(50, 50, 20, 15, fill="green", stroke="black", transform="skewY(-30)")
d.append(c)

d.savePng("example_2.png")
