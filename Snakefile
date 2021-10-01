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


# Subclass the `figure` rule to specify that the inline figure
# `figures/inline.pdf` is generated from the script `figures/inline.py`
use rule figure from showyourwork as inline_figure with:
    input:
        "src/figures/inline.py",
        "environment.yml"
    output:
        report("src/figures/inline.pdf", category="Figure")
