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

DROP EXTERNAL TABLE dbo.staging_payment

CREATE EXTERNAL TABLE dbo.staging_payment (
	[payment_id] int,
	[payment_date] VARCHAR(27),
	[amount] float,
	[rider_id] int
	)
	WITH (
	LOCATION = 'public.payment.csv',
	DATA_SOURCE = [de-file-system_de0storage0account_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


SELECT TOP 10 * FROM dbo.staging_payment
GO