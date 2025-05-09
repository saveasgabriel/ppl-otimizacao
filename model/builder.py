from pyomo.environ import ConcreteModel, Set, Var, NonNegativeReals, NonNegativeIntegers, Objective, ConstraintList, maximize, minimize

def build_model(df, config):
    df = df.set_index('Produto') 
    model = ConcreteModel()
    produtos = list(df.index)
    model.P = Set(initialize=produtos)
    model.x = Var(model.P, domain=NonNegativeReals)

    # domínios inteiros e limites
    for p in produtos:
        if df.loc[p, 'Tipo'] == 'Inteira':
            model.x[p].domain = NonNegativeIntegers
        model.x[p].setlb(df.loc[p, 'Min'])
        model.x[p].setub(df.loc[p, 'Max'])

    # objetivo
    sense = maximize if config['opt_type']=='Maximização' else minimize
    coef = df[config['obj_name']].to_dict()
    model.obj = Objective(expr=sum(coef[p]*model.x[p] for p in produtos), sense=sense)

    # restrições
    model.res = ConstraintList()
    for r in config['resource_names']:
        uso = df[r].to_dict()
        model.res.add(sum(uso[p]*model.x[p] for p in produtos) <= config['disponibilidade'][r])
    model.res.add(sum(model.x[p] for p in produtos) >= config['demanda_min'])
    model.res.add(sum(model.x[p] for p in produtos) <= config['demanda_max'])

    return model