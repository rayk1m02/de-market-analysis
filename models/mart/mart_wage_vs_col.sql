/**
core
- DE-adjacent wages adjusted for cost of living, per metro
    fct_occupation x fct_cost_of_living

other
- correlation between annual mean wage and location quotient (fct_occupation). 
    does higher wage concentration track with higher ocupational density?
- correlation between annual mean wage and employment, factoring in location quotient
    does a larger occupational workforce relate to wage level, and does concentration change that relationship?
- employment percentage per occupation, per metro
    fct_occupation.employment / fct_labor_market.labor_force
    note - grain mismatch (monthly vs. annual snapshot) needs a decision on which labor_force month to use before building this
*/