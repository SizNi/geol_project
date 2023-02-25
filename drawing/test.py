import drawSvg as draw

width = 100
height = 100
d = draw.Drawing(width, height, origin=(0, 0), displayInline=False)

with open("new-fill.svg", "r") as file:
    raw_svg = file.read()
    raw_latex_1 = raw_svg.replace("<?xml version='1.0'?>", "")
    raw_rendered_svg_1 = draw.Raw(raw_latex_1)
# o = draw.Image(0, 0, 100, 100, raw_rendered_svg_1)
# d.append(o)

pattern = draw.Raw(
    f"""
<defs>
  <pattern id="pattern1"
           x="0" y="0" width="100" height="100"
           patternUnits="userSpaceOnUse" >
    {raw_rendered_svg_1}
        <circle cx="10" cy="10" r="10"
            style="stroke: #0000ff; fill: url(#pattern1)"/>
  </pattern>
</defs>"""
)
d.append(pattern)
r = draw.Rectangle(0, 0, 100, 100, fill="url(#pattern1)", stroke="black")
d.append(r)
d.saveSvg("example_2.svg")
