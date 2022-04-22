from neuron import h, gui
h.load_file('import3d.hoc')

# Cell morphology from
# https://microcircuits.epfl.ch/#/animal/8ed14526-b2d2-11e4-9fa5-6003088da632

class MyCell:
    def __init__(self, file):
        morph_reader = h.Import3d_Neurolucida3()
        morph_reader.input(file)
        i3d = h.Import3d_GUI(morph_reader, 0)
        i3d.instantiate(self)
        asc_secs = i3d.asc.sections
        asc_secs = [asc_secs.object(i) for i in range(int(asc_secs.count()))]

file = 'data/C060600A2.ASC'
m = MyCell(file)
sp = h.PlotShape()
sp.show(0)  
input("Press <enter> to continue")