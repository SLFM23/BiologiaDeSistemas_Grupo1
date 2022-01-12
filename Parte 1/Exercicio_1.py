from cobra.io import read_sbml_model

#Importar o modelo utilizando Cobrapy
model = read_sbml_model('iML1515.xml')

#Condições ambientais definidas
envcond = {'EX_glc__D_e': (-15.0, 100000.0),
           'EX_o2_e':(0,1000)}

#EX_mal__L_e -> L-malate
#EX_mal__D_e -> D-malate

from mewpy.simulation import get_simulator

#Realização do FBA
simul = get_simulator(model, envcond=envcond)
result = simul.simulate(method='FBA')

print(simul.reactions)

#Obtenção do valor dos fluxos WT
print('L-Lactate wild type flux: ', result.fluxes['EX_lac__L_e'])
print('D-Lactate wild type flux: ',result.fluxes['EX_lac__D_e'])
