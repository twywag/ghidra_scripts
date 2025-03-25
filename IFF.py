#TODO Count the number of times each instruction appears in a program or selection
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 
#@runtime PyGhidra


I_LIKE_TO_BROWSER = True
I_LIKE_TO_PRINT = False
I_LIKE_TO_SAVE = False

"""Return a sorted list of unique instructions given an instruction iterator"""
def get_uniq_instrs(instrIt):
    unique_instructions = {}
    while instrIt.hasNext():
        instruction = instrIt.next()
        mnemonic = instruction.getMnemonicString()
        if mnemonic in unique_instructions:
            unique_instructions[mnemonic] = unique_instructions[mnemonic] + 1
        else:
            unique_instructions[mnemonic] = 1
    return sorted(unique_instructions.items(), key=lambda item: item[1], reverse=True)


if currentSelection:
    instructionIt = currentProgram.getListing().getInstructions(currentSelection, True)
else:
    instructionIt = currentProgram.getListing().getInstructions(True)


instrDict = get_uniq_instrs(instructionIt)


if I_LIKE_TO_PRINT:
    print("Number of unique instructions: %s" % len(instrDict))
    print(instrDict)

if I_LIKE_TO_SAVE:
    """What a pythonic line below"""
    # fileName = currentProgram.name + (('_' + currentSelection.getMinAddress().toString() + '-' + currentSelection.getMaxAddress().toString()) if currentSelection else "")
    fileName = currentProgram.name
    if currentSelection:
        fileName += '_' + currentSelection.getMinAddress().toString() + '-' + currentSelection.getMaxAddress().toString()
    fileName += "_IFF"
    print(fileName)
if I_LIKE_TO_BROWSER:
    import pandas as pd
    import plotly.express as px
    print(instrDict)
    # The following displays the results on a web page
    df = pd.DataFrame(instrDict, columns=['Instruction', 'Count'])
    fig = px.bar(df, x='Instruction', y='Count', title='Instruction Occurences', labels={'Count': 'Number of Occurences', 'Instruction': 'Instruction Mnemonic'})
    fig.show()
