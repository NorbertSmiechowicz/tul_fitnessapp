# GEN AI MODEL Input/Output structure
Model can be used in two variants, depending on which info is provided:
- desired gains mode: provided are Biometrics and Qualifiers
- routine prediction mode: provided are Biometrics and 2 weeks worth of Day Summary
## Biometrics <- user account
- age
- sex
- height
- weight

## Qualifiers
- cumulative weight difference 
- cumulative cardio difference
- cumulative strength arms difference
- cumulative strength legs difference
- cumulative strength core difference
- cumulative strength chest difference

## List 42 of: Day Summary
- protein
- fats
- carbs
- weight difference
- strength difference
## Paired Methods
- Day Summary Extraction Algorithm:
    - raw user DB dump filtered by date -> (List of) Day Summary
- Day Diet Generation Algorithm 
    - Day Summary -> List of recommended meals for the day
- Day Exercise Generation Algorithm
    - Day Summary -> List of recommended exercises for the day
- Qualifiers Calculator Algorithm:
    - List of Day Summary -> Qualifiers
