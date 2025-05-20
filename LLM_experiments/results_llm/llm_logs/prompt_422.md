
You have been assigned the role of crossover assistant during genetic programming. You are assisting in the crossover between multiple parents. The goal is to create a child program that is a combination of the multiple parents. The parents are represented as a series of edits. The source file (code program or parameter file)  you are working on is presented below to give you context.
The fitness is runtime, the lower the better.
Your task is to select from the available parents the edits you think are the more beneficial to create a child program. The child program must be a combination of the edits from the available parents. The child must be a combination of the available edits. Your response must adhere to the text format: Child: ***the child***.


and these are the available parents each with his fitness. The lowest fitness the better the parent.
Available parents:
 Parent 1:
 with fitness 8.0951
Parent 1 has 3 edits: ["SrcmlStmtInsertion(('core/Solver.cc.xml', '_inter_block', 311), ('core/Solver.cc.xml', 'stmt', 195))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 51))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 428))"]
 Parent 2:
 with fitness 8.1259
Parent 2 has 4 edits: ["SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 51))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 40))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 428))", "SrcmlStmtInsertion(('core/Solver.cc.xml', '_inter_block', 311), ('core/Solver.cc.xml', 'stmt', 195))"]
 Parent 3:
 with fitness 8.1021
Parent 3 has 5 edits: ["SrcmlStmtInsertion(('core/Solver.cc.xml', '_inter_block', 226), ('core/Solver.cc.xml', 'stmt', 271))", "SrcmlStmtInsertion(('core/Solver.cc.xml', '_inter_block', 311), ('core/Solver.cc.xml', 'stmt', 195))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 40))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 51))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 428))"]
 Parent 4:
 with fitness 8.1725
Parent 4 has 4 edits: ["SrcmlStmtInsertion(('core/Solver.cc.xml', '_inter_block', 311), ('core/Solver.cc.xml', 'stmt', 195))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 51))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 428))", "SrcmlStmtInsertion(('core/Solver.cc.xml', '_inter_block', 226), ('core/Solver.cc.xml', 'stmt', 271))"]
 Parent 5:
 with fitness 8.1021
Parent 5 has 5 edits: ["SrcmlStmtInsertion(('core/Solver.cc.xml', '_inter_block', 311), ('core/Solver.cc.xml', 'stmt', 195))", "SrcmlStmtInsertion(('core/Solver.cc.xml', '_inter_block', 226), ('core/Solver.cc.xml', 'stmt', 271))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 51))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 428))", "SrcmlStmtDeletion(('core/Solver.cc.xml', 'stmt', 40))"]


Remember you are assisting in the crossover between the parents. Choose as many and whichever edits from the available parents you think will lead to the best child. The proposed edits must be a combination of the available edits. Respond back with the child in the form of a list of edits in the same format as the parents are.
Your response must adhere to the text format: Child: ***the child***. 
