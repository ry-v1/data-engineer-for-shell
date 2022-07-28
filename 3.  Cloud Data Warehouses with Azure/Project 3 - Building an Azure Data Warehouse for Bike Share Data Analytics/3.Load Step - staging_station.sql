IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
	CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
	WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
	       FORMAT_OPTIONS (
			 FIELD_TERMINATOR = ',',
			 USE_TYPE_DEFAULT = FALSE
			))
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'de-file-system_de0storage0account_dfs_core_windows_net') 
	CREATE EXTERNAL DATA SOURCE [de-file-system_de0storage0account_dfs_core_windows_net] 
	WITH (
		LOCATION = 'abfss://de-file-system@de0storage0account.dfs.core.windows.net', 
		TYPE = HADOOP 
	)
GO

DROP EXTERNAL TABLE dbo.staging_station

CREATE EXTERNAL TABLE dbo.staging_station (
	[station_id] varchar(100),
	[name] varchar(200),
	[latitude] float,
	[longitude] float
	)
	WITH (
	LOCATION = 'public.station.csv',
	DATA_SOURCE = [de-file-system_de0storage0account_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


SELECT TOP 100 * FROM dbo.staging_station
GO