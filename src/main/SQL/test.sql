SELECT IdWorkOrder, NbUnitsToDo FROM promon.workorders WHERE workorders.Name = "test_prod1_2023-05-05_10h07m14s";
SELECT (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS carte FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder WHERE w.Name = "";

SELECT MAX(wrms.ExpectedCycleTime) 
FROM workorders w
JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder
JOIN workorderrecipemachinestages wrms ON wrm.IdWorkOrderRecipeMachine = wrms.IdWorkOrderRecipeMachine
WHERE w.Name = 'test_prod1_2023-05-05_10h07m14s';


SELECT MAX(wrms.ExpectedCycleTime), (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS cartes FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder JOIN workorderrecipemachinestages wrms ON wrm.IdWorkOrderRecipeMachine = wrms.IdWorkOrderRecipeMachine WHERE w.Name = "all_test_2023-05-09_16h30m45s";