
You have been assigned the role of crossover assistant during genetic programming. You are assisting in the crossover between multiple parents. The goal is to create a child program that is a combination of the multiple parents. The parents are represented as a series of edits. The source file (code program or parameter file)  you are working on is presented below to give you context.
The fitness is runtime, the lower the better.
Your task is to select from the available parents the edits you think are the more beneficial to create a child program. The child program must be a combination of the edits from the available parents. The child must be a combination of the available edits. Your response must adhere to the text format: Child: ***the child***.

The source file

and these are the available parents each with his fitness. The lowest fitness the better the parent.
Available parents:
 Parent 1:
 with fitness 1.6965
Parent 1 has 4 edits: ["SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 346))", "SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 464))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 620), ('sources/core/Solver.cc.xml', 'stmt', 315))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 523), ('sources/core/Solver.cc.xml', 'stmt', 375))"]
 Parent 2:
 with fitness 1.7732
Parent 2 has 5 edits: ["SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 346))", "SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 464))", "SrcmlStmtReplacement(('sources/core/Solver.cc.xml', 'stmt', 44), ('sources/core/Solver.cc.xml', 'stmt', 38))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 147), ('sources/core/Solver.cc.xml', 'stmt', 211))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 620), ('sources/core/Solver.cc.xml', 'stmt', 315))"]
 Parent 3:
 with fitness 1.7531
Parent 3 has 5 edits: ["SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 346))", "SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 464))", "SrcmlStmtReplacement(('sources/core/Solver.cc.xml', 'stmt', 44), ('sources/core/Solver.cc.xml', 'stmt', 38))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 620), ('sources/core/Solver.cc.xml', 'stmt', 315))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 523), ('sources/core/Solver.cc.xml', 'stmt', 375))"]
 Parent 4:
 with fitness 1.7531
Parent 4 has 5 edits: ["SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 346))", "SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 464))", "SrcmlStmtReplacement(('sources/core/Solver.cc.xml', 'stmt', 44), ('sources/core/Solver.cc.xml', 'stmt', 38))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 523), ('sources/core/Solver.cc.xml', 'stmt', 375))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 620), ('sources/core/Solver.cc.xml', 'stmt', 315))"]
 Parent 5:
 with fitness 1.7354
Parent 5 has 4 edits: ["SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 346))", "SrcmlStmtDeletion(('sources/core/Solver.cc.xml', 'stmt', 464))", "SrcmlStmtReplacement(('sources/core/Solver.cc.xml', 'stmt', 44), ('sources/core/Solver.cc.xml', 'stmt', 38))", "SrcmlStmtInsertion(('sources/core/Solver.cc.xml', '_inter_block', 620), ('sources/core/Solver.cc.xml', 'stmt', 315))"]


Remember you are assisting in the crossover between the parents. Choose as many and whichever edits from the available parents you think will lead to the best child. The proposed edits must be a combination of the available edits. Respond back with the child in the form of a list of edits in the same format as the parents are.
Your response must adhere to the text format: Child: ***the child***. 
