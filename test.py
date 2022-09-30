import pandas as pd
import rulesSubLib

rSL = rulesSubLib.TableModifier("table.csv", "rules/regions.csv", "rules/numbers.csv", "output.csv", "output_frequency.csv")
rSL.modifyByRules()
rSL.computeFrequency()

