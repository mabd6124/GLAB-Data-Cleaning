use RVMonthlyReporting

create table tblVehicleDataCleaned(
	cVehicleCode varchar(10),
	vcMake varchar(30),
	vcModel varchar(30),
	vcVariant varchar(30),
	mRetailPrice int,
	vcBodyStyle varchar(30),
	vcTransmissionType varchar(30),
	vcDriveType varchar(30),
	vcFuelType varchar(30),
	vcEngineSize varchar(10),
	cCylinders varchar(10),
	dtReleaseDate datetime,
	nodeKey varchar(60)
)
--drop table tblVehicleDataCleaned
select * from tblVehicleDataCleaned

--truncate table tblVehicleDataCleaned

