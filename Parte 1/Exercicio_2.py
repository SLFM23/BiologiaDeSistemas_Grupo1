def teste():
    from cobra.io import read_sbml_model
    model = read_sbml_model('iML1515.xml')


    print('------------------------------------------')
    print('Implementação no Mewpy: ')
    print('------------------------------------------')

    #Definir condições ambientais
    envcond = {'EX_glc__D_e': (-15.0, 100000.0),
               'EX_o2_e':(0,1000)}

    #Carregar modelo no Mewpy
    from mewpy.simulation import get_simulator
    simul = get_simulator(model, envcond=envcond)

    print(model.summary())
    #Realizar FVA no Mewpy
    print(simul.FVA(reactions=['EX_lac__L_e', 'EX_lac__D_e'], format=('df')))

if __name__ == '__main__':
    teste()