import pandas as pd

lists = [['N9 切後', '刷鍑前', '刷鍑後', 'COB 後'], ['VDD', 'Vbc', 'Vss2', 'VGL', 'VGH']]

index = pd.MultiIndex.from_product(lists, names=['first', 'second'])

cols = pd.MultiIndex.from_tuples(['No', 'Notes', '刮刀下壓', 'Panel ID', '出貨', '洗淨方式', '破片', '可剝膠', 'DB',
                                   'VDD', 'Vbc', 'Vss2', 'VGL', 'VGH', 
				  				   'VDD', 'Vbc', 'Vss2', 'VGL', 'VGH', 
								   'VDD', 'Vbc', 'Vss2', 'VGL', 'VGH',  
								   'VDD', 'Vbc', 'Vss2', 'VGL', 'VGH', 
								   'VDD', 'Vbc', 'Vss2', 'VGL', 'VGH', 

								  #("Gasoline", "Toyoto"), 
								  #("Gasoline", "Ford"), 	
								  #("Electric", "Tesla"),
								  #("Electric", "Nio")   	
								  ])
