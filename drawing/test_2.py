import drawSvg as draw

d = draw.Drawing(1.5, 0.8, origin='center')

d = draw.Drawing(200, 100, origin='center', displayInline=False)

# Draw an irregular polygon
d.append(draw.Lines(-80, -45,
                    70, -49,
                    95, 49,
                    -90, 40,
                    close=False,
            fill='#eeee00',
            stroke='black'))
# Display
d.setRenderSize(w=600)
d.saveSvg('ex.svg')