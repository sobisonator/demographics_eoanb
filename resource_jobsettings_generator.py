# Use this script to quickly generate a set of scripted effects
# These are used to update variables in states when resources change in them

resources = [
    "wood",
    "coal",
    "cotton",
    "fabric",
    "iron",
    "steel",
    "rubber",
    "oil",
    "plastics",
    "aluminium",
    "tungsten",
    "chromium",
    "titanium",
    "silicates",
    "ceramics",
    "machine_parts",
    "rare_earth_metals",
    "eletronics",
    "portable_power"
    ]

for RESOURCE in resources:
    print(
        "#Values in thousands of available jobs\n"
        "set_variable = {\n"
            "var = available_"+RESOURCE+"_labourer_jobs\n"
	    "value = r_"+RESOURCE+"_available\n"
	"}\n"
        "multiply_variable = {\n"
            "var = available_"+RESOURCE+"_labourer_jobs\n"
            "value = 25\n"
        "}\n"
        "set_variable = {\n"
            "var = available_"+RESOURCE+"_foreman_jobs\n"
	    "value = r_"+RESOURCE+"_available\n"
	"}\n"
        "multiply_variable = {\n"
            "var = available_"+RESOURCE+"_foreman_jobs\n"
            "value = 2\n"
        "}\n"
    )
