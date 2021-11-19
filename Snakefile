# Render the config file
import jinja2
with open("showyourwork.yml", "w") as f:
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    print(env.get_template("showyourwork.yml.jinja").render(), file=f)


# User config
configfile: "showyourwork.yml"
    

# Import the showyourwork module
module showyourwork:
    snakefile:
        "showyourwork/workflow/Snakefile"
    config:
        config


# Use all default rules
use rule * from showyourwork


# Run a simulation to generate a 
# results file for a given value in [0, 10),
rule analysis:
    input:
        "src/data/run_simulation.py"
    output:
        "src/data/results_{value}.dat"
    shell:
        "python {input[0]} {wildcards.value}"
    conda:
        "environment.yml"
