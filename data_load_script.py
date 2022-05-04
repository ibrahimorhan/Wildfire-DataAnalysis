import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type': 'monthly_averaged_reanalysis',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
            '2m_temperature', 'convective_rain_rate',
        ],
        'year': [
            '2017', '2018', '2019',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'time': '00:00',
        'area': [
            38, 27, 36,
            29,
        ],
        'format': 'netcdf',
    },
    'cds_climate.nc')
for el in ['2017', '2018', '2019']:
    c.retrieve(
        'satellite-fire-burned-area',
        {
            'origin': 'esa_cci',
            'sensor': 'modis',
            'variable': 'grid_variables',
            'version': '5_1_1cds',
            'year': el,
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'nominal_day': '01',
            'format': 'zip',
        },
        'BA{year}.zip'.format(year = el))