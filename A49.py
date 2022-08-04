#python program to enter basic salary and calculate gross salary of an employee
gvn_basc_sal = 23000

gvn_da = (float)(15 * gvn_basc_sal) / 100.0

gvn_hr = (float)(10 * gvn_basc_sal) / 100.0

gvn_da_on_ta = (float)(3 * gvn_basc_sal) / 100.0
gros_sal = gvn_basc_sal + gvn_da + gvn_hr + gvn_da_on_ta
print("The Employee's Gross salary from the given basic salary {", gvn_basc_sal, "} =", gros_sal)
