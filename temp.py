
totaljson="fiscalCode(ajifjshkahskjln()ssjkdjskjd()jdkfajlkjlfksa)"
fiscal="fiscalCode("
indexOfFiscal=totaljson.find(fiscal)


relevantjson=totaljson[indexOfFiscal+len(fiscal):]
relevantjson=relevantjson[:-1]
print(relevantjson)
 
