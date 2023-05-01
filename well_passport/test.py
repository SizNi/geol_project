a = {2: 'well_passport/results/gis.pdf', 3: 'well_passport/results/generated_cross.pdf', 4: 'well_passport/results/analyses.pdf', 1: 'well_passport/results/generated_doc.pdf'}
sorted_a = dict(sorted(a.items(), key=lambda x: x[0]))
print(sorted_a)
sorted_list = list(sorted_a.values())
print(sorted_list)