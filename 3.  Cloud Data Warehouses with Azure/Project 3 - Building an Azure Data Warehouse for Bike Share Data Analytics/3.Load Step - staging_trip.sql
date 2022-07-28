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

DROP EXTERNAL TABLE dbo.staging_trip

CREATE EXTERNAL TABLE dbo.staging_trip (
	trip_id VARCHAR(50), 
	rideable_type VARCHAR(75), 
	start_at VARCHAR(27), 
	ended_at VARCHAR(27), 
	start_station_id VARCHAR(100), 
	end_station_id VARCHAR(100), 
	rider_id INTEGER
	)
	WITH (
	LOCATION = 'public.trip.csv',
	DATA_SOURCE = [de-file-system_de0storage0account_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


SELECT TOP 100 * FROM dbo.staging_trip
GO