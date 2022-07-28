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

DROP EXTERNAL TABLE dbo.staging_rider

CREATE EXTERNAL TABLE dbo.staging_rider (
	[rider_id] int,
	[first_name] varchar(30),
	[last_name] varchar(30),
	[address] varchar(4000),
	[birthday] varchar(27),
	[account_start_date] varchar(27),
	[account_end_date] varchar(27),
	[is_member] bit
	)
	WITH (
	LOCATION = 'public.rider.csv',
	DATA_SOURCE = [de-file-system_de0storage0account_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


SELECT TOP 100 * FROM dbo.staging_rider
GO