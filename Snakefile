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


rule answer:
    input:
        "src/answer.py"
    output:
        "src/answer.tex"
    conda:
        "environment.yml"
    shell:
        "cd src && python answer.py"