SELECT IdWorkOrder, NbUnitsToDo FROM promon.workorders WHERE workorders.Name = "test_prod1_2023-05-05_10h07m14s";

/* Nombre de cartes */
SELECT (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS carte FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder WHERE w.Name = "";

/* Temps prod max avec nb carte */
SELECT MAX(wrms.ExpectedCycleTime), (w.NbUnitsToDo div wrm.NbUnitsPerWork) AS cartes FROM workorders w JOIN workorderrecipemachines wrm ON w.IdWorkOrder = wrm.IdWorkOrder JOIN workorderrecipemachinestages wrms ON wrm.IdWorkOrderRecipeMachine = wrms.IdWorkOrderRecipeMachine WHERE w.Name = "all_test_2023-05-09_16h30m45s";

/* Suppression des tuples dans les tables */
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM activities;
DELETE FROM components;
DELETE FROM cumulatedatamachine;
DELETE FROM cumulatedatamachinestage;
DELETE FROM electricaltestdetails;
DELETE FROM endpoints;
DELETE FROM endpointstateshistory;
DELETE FROM endpointversionshistory;
DELETE FROM errors;
DELETE FROM faults;
DELETE FROM internalerrorlogs;
DELETE FROM items;
DELETE FROM machinestages;
DELETE FROM materialcarriers;
DELETE FROM operatorlogshistory;
DELETE FROM operators;
DELETE FROM statistics;
DELETE FROM workorderactivationshistory;
DELETE FROM workorderrecipemachines;
DELETE FROM workorderrecipemachinestages;
DELETE FROM workorders;
DELETE FROM workorderstatushistory;
DELETE FROM works;
SET FOREIGN_KEY_CHECKS = 1;

/* nombre de carte "faites" */
SELECT COUNT(*) FROM (workorders wo JOIN workorderrecipemachines worm ON wo.IdWorkOrder = worm.IdWorkOrder) JOIN works w ON worm.IdWorkOrderRecipeMachine = w.IdWorkOrderRecipeMachine WHERE wo.Name = "test8";

/* datecréation */

SELECT DateCreation FROM workorders WHERE NAME = "test4_2023-05-10_16h35m27s";