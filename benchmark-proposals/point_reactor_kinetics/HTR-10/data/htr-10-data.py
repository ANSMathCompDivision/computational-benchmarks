import pickle

'''
 Data
'''
kinetics_data_documentation = \
                {"n_delay_groups" : "Number of delay groups",\
                 "lambdas"  : "Precursor decay constants for each group",\
                 "betas"    : "Fraction of neutrons born delayed in each group",\
                 "lifetime" : "The neutron lifetime usually denoted capital lambda",
                 "initial_neutron_population" : "Initial number of neutrons in the reactor"}

kinetics_data = {"n_delay_groups" : 6,\
                 "lambdas"  : [0.0127, 0.0317, 0.115, 0.311, 1.40, 3.87],\
                 "betas"    : [0.000285, 0.0015975, 0.001410, 0.0030525,0.00096,0.000195],\
                 "lifetime" :  0.00168,
                 "initial_neutron_population" : 10.0e6}

thermal_data_documentation = \
               {"fuel_mass" : "Mass of the fuel",\
                "graphite_mass" : "Mass of the graphite",\
                "cp_fuel" : "Specific heat capacity of the fuel",\
                "cp_graphite" : "Specific heat capacity of the graphite",\
                "heat_transfer_fuel_to_graphite" : "Heat transfer coefficient from fuel to graphite",\
                "heat_transfer_graphite_to_helium" : "Heat transfer coefficient from graphite to fuel",\
                "helium_temperature" : "The helium coolant temperature (constant)",\
                "initial_fuel_temperature" : "Initial fuel temperature",\
                "initial_graphite_temperature" : "Initial graphite temperature"}

thermal_data = {"fuel_mass" : 54.613581,\
                "graphite_mass" : 3304.2788981,\
                "cp_fuel" : 316.1063,\
                "cp_graphite" : 1855.9,\
                "heat_transfer_fuel_to_graphite" : 393700.78740157513,\
                "heat_transfer_graphite_to_helium" : 125628.14070351755,\
                "helium_temperature" : 748,\
                "initial_fuel_temperature" : 853,\
                "initial_mod_temperature" : 827.6}

feedback_data_documentation = {"initial_reactivity_insertion_dollar" : "Initial reactivity insertion in $",\
                               "initial_reactivity_insertion" : "Initial reactivity insertion = initial_reactivity_insertion_dollar * beta",\
                               "fuel_temperature_coefficient" : "Feedback coefficient from the fuel drho = coeff * (T-T0)",\
                               "graphite_temperature_coefficient" : "Feedback coefficient from the graphite drho = coeff * (T-T0)"}

feedback_data = {"initial_reactivity_insertion_dollar" : 0.05,\
                 "initial_reactivity_insertion" : 0.000375,\
                 "fuel_temperature_coefficient" : -1.9e-5,\
                 "graphite_temperature_coefficient" : -15.7e-5}

'''
 Pickle the data
'''
output = open('htr-10-data.pkl', 'wb')
pickle.dump(kinetics_data_documentation, output)
pickle.dump(kinetics_data, output)
pickle.dump(thermal_data_documentation, output)
pickle.dump(feedback_data_documentation, output)
pickle.dump(feedback_data, output)
pickle.dump(thermal_data, output)
output.close()
