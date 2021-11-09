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


# Run an expensive simulation to generate a 
# results file for a given value in [0, 10),
# but only if we're not on GitHub Actions
if not config["CI"]:
    rule analysis:
        input:
            "src/data/run_simulation.py"
        output:
            "src/data/results_{value}.dat"
        shell:
            "python {input[0]} {wildcards.value}"