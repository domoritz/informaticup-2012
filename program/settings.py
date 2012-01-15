
defaultSettings = {
	'algorithm': 'genetic',
	'genetic': {
		'popsize': 250,
		'childrenGroup': 50,
		'mutation': 20,
		'shortening': 10,
		'maxGenerations': 50000,
		'catastrophyAfter': 100,
		'stopAfter': 800,
		'seed': 42
	},
	'clingo': {
		'clingo': 'auto',
		'clingoArgs': '',
	}
}

import copy
settings = copy.deepcopy(defaultSettings)
