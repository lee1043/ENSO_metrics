# -*- coding:UTF-8 -*-
#
# Define ENSO metrics collections as a function of science question/realm
#
# Draft version
#


# Define metrics collections
def defCollection(mc=True):
    # Name, list of metrics
    metrics_collection = {
        'ENSO_perf': {
            'long_name': 'Metrics Collection for ENSO performance',
            'metrics_list': {
                'BiasPrLatRmse': {
                    'variables': ['pr'],
                    'regions': {'pr': 'nino3_LatExt'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasPrLonRmse': {
                    'variables': ['pr'],
                    'regions': {'pr': 'equatorial_pacific'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                # 'BiasSshLatRmse': {
                #     'variables': ['ssh'],
                #     'regions': {'ssh': 'nino3_LatExt'},
                #     'obs_name': {'ssh': ['AVISO']},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                # 'BiasSshLonRmse': {
                #     'variables': ['ssh'],
                #     'regions': {'ssh': 'equatorial_pacific'},
                #     'obs_name': {'ssh': ['AVISO']},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                # 'BiasSstLatRmse': {
                #     'variables': ['sst'],
                #     'regions': {'sst': 'nino3_LatExt'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                'BiasSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                # 'BiasTauxLatRmse': {
                #     'variables': ['taux'],
                #     'regions': {'taux': 'equatorial_pacific_LatExt'},
                #     'obs_name': {'taux': ['ERA-Interim', 'Tropflux']},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                'BiasTauxLonRmse': {
                    'variables': ['taux'],
                    'regions': {'taux': 'equatorial_pacific'},
                    'obs_name': {'taux': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalPrLatRmse': {
                    'variables': ['pr'],
                    'regions': {'pr': 'nino3_LatExt'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalPrLonRmse': {
                    'variables': ['pr'],
                    'regions': {'pr': 'equatorial_pacific'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                # 'SeasonalSshLatRmse': {
                #     'variables': ['ssh'],
                #     'regions': {'ssh': 'nino3_LatExt'},
                #     'obs_name': {'ssh': ['AVISO']},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                # 'SeasonalSshLonRmse': {
                #     'variables': ['ssh'],
                #     'regions': {'ssh': 'equatorial_pacific'},
                #     'obs_name': {'ssh': ['AVISO']},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                # 'SeasonalSstLatRmse': {
                #     'variables': ['sst'],
                #     'regions': {'sst': 'nino3_LatExt'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                'SeasonalSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                # 'SeasonalTauxLatRmse': {
                #     'variables': ['taux'],
                #     'regions': {'taux': 'equatorial_pacific_LatExt'},
                #     'obs_name': {'taux': ['ERA-Interim', 'Tropflux']},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                'SeasonalTauxLonRmse': {
                    'variables': ['taux'],
                    'regions': {'taux': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoAmpl': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoDuration': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'nbr_years_window': 6,
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoSeasonality': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                # 'EnsoSstDiversity_1': {
                #     'variables': ['sst'],
                #     'regions': {'sst': 'equatorial_pacific'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                #     'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                #                          'normalization': False},
                #     'smoothing': {'window': 5, 'method': 'triangle'},
                #     'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                #                    'newgrid_name': 'generic_1x1deg'},
                #     'metric_computation': 'abs_relative_difference',
                # },
                'EnsoSstDiversity_2': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoSstSkew': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                # 'EnsoPrTsRmse': {
                #     'variables': ['sst', 'pr'],
                #     'regions': {'sst': 'nino3.4', 'pr': 'nino3'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'pr': ['ERA-Interim', 'GPCPv2.3']},
                #     'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                #                          'normalization': True},
                #     'nbr_years_window': 6,
                #     'smoothing': {'window': 5, 'method': 'triangle'},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                'EnsoSstTsRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'nbr_years_window': 6,
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                # 'EnsoTauxTsRmse': {
                #     'variables': ['sst', 'taux'],
                #     'regions': {'sst': 'nino3.4', 'taux': 'nino4'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'taux': ['ERA-Interim', 'Tropflux']},
                #     'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                #                          'normalization': True},
                #     'nbr_years_window': 6,
                #     'smoothing': {'window': 5, 'method': 'triangle'},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                # },
                # 'NinoSstDiversity_1': {
                #     'variables': ['sst'],
                #     'regions': {'sst': 'equatorial_pacific'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                #     'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                #                          'normalization': False},
                #     'smoothing': {'window': 5, 'method': 'triangle'},
                #     'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                #                    'newgrid_name': 'generic_1x1deg'},
                #     'metric_computation': 'abs_relative_difference',
                # },
                # 'NinoSstDiversity_2': {
                #     'variables': ['sst'],
                #     'regions': {'sst': 'equatorial_pacific'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                #     'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                #                          'normalization': True},
                #     'smoothing': {'window': 5, 'method': 'triangle'},
                #     'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                #                    'newgrid_name': 'generic_1x1deg'},
                #     'metric_computation': 'abs_relative_difference',
                # },
            },
            'common_collection_parameters': {
                'detrending': {'method': 'linear'},
                'frequency': 'monthly',
                'min_time_steps': 12,
                'normalization': False,
                'project_interpreter': 'CMIP',
                'observed_period': ("1850-01-01 00:00:00", "2018-12-31 23:59:60.0"),
                'modeled_period': ("1850-01-01 00:00:00", "2015-12-31 23:59:60.0"),
            },
            'plot_order': ['BiasPrLatRmse', 'BiasPrLonRmse', 'BiasSstLonRmse', 'BiasTauxLonRmse',
                           'SeasonalPrLatRmse', 'SeasonalPrLonRmse', 'SeasonalSstLonRmse', 'SeasonalTauxLonRmse',
                           'EnsoSstLonRmse', 'EnsoSstTsRmse', 'EnsoAmpl', 'EnsoSeasonality', 'EnsoSstSkew',
                           'EnsodDuration', 'EnsoSstDiversity_2'],
            'description': 'Describe which science question this collection is about',
        },
        'ENSO_tel': {
            'long_name': 'Metrics Collection for ENSO teleconnections',
            'metrics_list': {
                'EnsoAmpl': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoSeasonality': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoPrMapDjf': {
                    'variables': ['sst', 'pr'],
                    'regions': {'pr': 'global', 'sst': 'nino3.4'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3'], 'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                'EnsoPrMapJja': {
                    'variables': ['sst', 'pr'],
                    'regions': {'pr': 'global', 'sst': 'nino3.4'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3'], 'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                # 'EnsoSlpMapDjf': {
                #     'variables': ['sst', 'slp'],
                #     'regions': {'slp': 'global', 'sst': 'nino3.4'},
                #     'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                #                          'normalization': False},
                #     'smoothing': {'window': 5, 'method': 'triangle'},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                #     'obs_name': {'slp': ['AVISO'], 'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                # },
                # 'EnsoSlpMapJja': {
                #     'variables': ['sst', 'slp'],
                #     'regions': {'slp': 'global', 'sst': 'nino3.4'},
                #     'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                #                          'normalization': False},
                #     'smoothing': {'window': 5, 'method': 'triangle'},
                #     'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                #                    'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                #     'obs_name': {'slp': ['AVISO'], 'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                # },
                'EnsoSstMapDjf': {
                    'variables': ['sst'],
                    'regions': {'sst': 'global'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                'EnsoSstMapJja': {
                    'variables': ['sst'],
                    'regions': {'sst': 'global'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
            },
            'common_collection_parameters': {
                'detrending': {'method': 'linear'},
                'frequency': 'monthly',
                'min_time_steps': 12,
                'normalization': False,
                'project_interpreter': 'CMIP',
                'observed_period': ("1850-01-01 00:00:00", "2018-12-31 23:59:60.0"),
                'modeled_period': ("1850-01-01 00:00:00", "2015-12-31 23:59:60.0"),
            },
            'plot_order': ['EnsoSstLonRmse', 'EnsoAmpl', 'EnsoSeasonality', 'EnsoPrMapDjfRmse', 'EnsoPrMapJjaRmse',
                           'EnsoSstMapDjfRmse', 'EnsoSstMapJjaRmse'],
            'description': 'Describe which science question this collection is about',
        },
        'ENSO_proc': {
            'long_name': 'Metrics Collection for ENSO processes',
            'metrics_list': {
                'BiasSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasTauxLonRmse': {
                    'variables': ['taux'],
                    'regions': {'taux': 'equatorial_pacific'},
                    'obs_name': {'taux': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoAmpl': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoSeasonality': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoSstSkew': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                # 'EnsodSstOce_1': {
                #     'variables': ['sst', 'thf'],
                #     'regions': {'sst': 'nino3', 'thf': 'nino3'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'thf': ['ERA-Interim', 'Tropflux']},
                #     'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                #                          'normalization': False},
                #     'smoothing': {'window': 5, 'method': 'triangle'},
                #     'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                #                    'newgrid_name': 'generic_1x1deg'},
                #     'metric_computation': 'abs_relative_difference',
                # },
                'EnsodSstOce_2': {
                    'variables': ['sst', 'thf'],
                    'regions': {'sst': 'nino3', 'thf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'thf': ['ERA-Interim', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSshSst': {
                    'variables': ['sst', 'ssh'],
                    'regions': {'sst': 'nino3', 'ssh': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'ssh': ['AVISO']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                # 'EnsoFbSstLhf': {
                #     'variables': ['sst', 'lhf'],
                #     'regions': {'sst': 'nino3', 'lhf': 'nino3'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'lhf': ['ERA-Interim', 'Tropflux']},
                #     'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                #                    'newgrid_name': 'generic_1x1deg'},
                #     'metric_computation': 'abs_relative_difference',
                # },
                # 'EnsoFbSstLwr': {
                #     'variables': ['sst', 'lwr'],
                #     'regions': {'sst': 'nino3', 'lwr': 'nino3'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'lwr': ['ERA-Interim', 'Tropflux']},
                #     'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                #                    'newgrid_name': 'generic_1x1deg'},
                #     'metric_computation': 'abs_relative_difference',
                # },
                # 'EnsoFbSstShf': {
                #     'variables': ['sst', 'shf'],
                #     'regions': {'sst': 'nino3', 'shf': 'nino3'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'shf': ['ERA-Interim', 'Tropflux']},
                #     'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                #                    'newgrid_name': 'generic_1x1deg'},
                #     'metric_computation': 'abs_relative_difference',
                # },
                # 'EnsoFbSstSwr': {
                #     'variables': ['sst', 'swr'],
                #     'regions': {'sst': 'nino3', 'swr': 'nino3'},
                #     'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'swr': ['ERA-Interim', 'Tropflux']},
                #     'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                #                    'newgrid_name': 'generic_1x1deg'},
                #     'metric_computation': 'abs_relative_difference',
                # },
                'EnsoFbSstTaux': {
                    'variables': ['sst', 'taux'],
                    'regions': {'sst': 'nino3', 'taux': 'nino4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'taux': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstThf': {
                    'variables': ['sst', 'thf'],
                    'regions': {'sst': 'nino3', 'thf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'thf': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbTauxSsh': {
                    'variables': ['taux', 'ssh'],
                    'regions': {'ssh': 'nino3', 'taux': 'nino4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'ssh': ['AVISO']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
            },
            'common_collection_parameters': {
                'detrending': {'method': 'linear'},
                'frequency': 'monthly',
                'min_time_steps': 12,
                'normalization': False,
                'project_interpreter': 'CMIP',
                'observed_period': ("1850-01-01 00:00:00", "2018-12-31 23:59:60.0"),
                'modeled_period': ("1850-01-01 00:00:00", "2015-12-31 23:59:60.0"),
            },
            'plot_order': ['BiasSstLonRmse', 'BiasTauxLonRmse', 'EnsoSstLonRmse', 'EnsoAmpl', 'EnsoSeasonality',
                           'EnsoSstSkew', 'EnsodSstOce_2', 'EnsoFbSstThf', 'EnsoFbSstTaux', 'EnsoFbTauxSsh',
                           'EnsoFbSshSst'],
            'description': 'Describe which science question this collection is about',
        },
        'all_metrics': {
            'long_name': 'Metrics Collection for ENSO performance',
            'metrics_list': {
                'BiasPrLatRmse': {
                    'variables': ['pr'],
                    'regions': {'pr': 'nino3_LatExt'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasPrLonRmse': {
                    'variables': ['pr'],
                    'regions': {'pr': 'equatorial_pacific'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasSshLatRmse': {
                    'variables': ['ssh'],
                    'regions': {'ssh': 'nino3_LatExt'},
                    'obs_name': {'ssh': ['AVISO']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasSshLonRmse': {
                    'variables': ['ssh'],
                    'regions': {'ssh': 'equatorial_pacific'},
                    'obs_name': {'ssh': ['AVISO']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasSstLatRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3_LatExt'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasTauxLatRmse': {
                    'variables': ['taux'],
                    'regions': {'taux': 'equatorial_pacific_LatExt'},
                    'obs_name': {'taux': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasTauxLonRmse': {
                    'variables': ['taux'],
                    'regions': {'taux': 'equatorial_pacific'},
                    'obs_name': {'taux': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoAmpl': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoDuration': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'nbr_years_window': 6,
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsodSstOce_1': {
                    'variables': ['sst', 'thf'],
                    'regions': {'sst': 'nino3', 'thf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'thf': ['ERA-Interim', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsodSstOce_2': {
                    'variables': ['sst', 'thf'],
                    'regions': {'sst': 'nino3', 'thf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'thf': ['ERA-Interim', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSshSst': {
                    'variables': ['sst', 'ssh'],
                    'regions': {'sst': 'nino3', 'ssh': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'ssh': ['AVISO']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstLhf': {
                    'variables': ['sst', 'lhf'],
                    'regions': {'sst': 'nino3', 'lhf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'lhf': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstLwr': {
                    'variables': ['sst', 'lwr'],
                    'regions': {'sst': 'nino3', 'lwr': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'lwr': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstShf': {
                    'variables': ['sst', 'shf'],
                    'regions': {'sst': 'nino3', 'shf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'shf': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstSwr': {
                    'variables': ['sst', 'swr'],
                    'regions': {'sst': 'nino3', 'swr': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'swr': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstTaux': {
                    'variables': ['sst', 'taux'],
                    'regions': {'sst': 'nino3', 'taux': 'nino4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'taux': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstThf': {
                    'variables': ['sst', 'thf'],
                    'regions': {'sst': 'nino3', 'thf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'thf': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbTauxSsh': {
                    'variables': ['taux', 'ssh'],
                    'regions': {'ssh': 'nino3', 'taux': 'nino4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'ssh': ['AVISO']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoPrMapDjf': {
                    'variables': ['sst', 'pr'],
                    'regions': {'pr': 'global', 'sst': 'nino3.4'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3'], 'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                'EnsoPrMapJja': {
                    'variables': ['sst', 'pr'],
                    'regions': {'pr': 'global', 'sst': 'nino3.4'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3'], 'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                'EnsoSeasonality': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoSlpMapDjf': {
                    'variables': ['sst', 'slp'],
                    'regions': {'slp': 'global', 'sst': 'nino3.4'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'slp': ['AVISO'], 'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                'EnsoSlpMapJja': {
                    'variables': ['sst', 'slp'],
                    'regions': {'slp': 'global', 'sst': 'nino3.4'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'slp': ['AVISO'], 'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                'EnsoSstDiversity_1': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoSstDiversity_2': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoSstMapDjf': {
                    'variables': ['sst'],
                    'regions': {'sst': 'global'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                'EnsoSstMapJja': {
                    'variables': ['sst'],
                    'regions': {'sst': 'global'},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': False},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                },
                'EnsoSstSkew': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'metric_computation': 'abs_relative_difference',
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoSstTsRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3.4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'nbr_years_window': 6,
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalPrLatRmse': {
                    'variables': ['pr'],
                    'regions': {'pr': 'nino3_LatExt'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalPrLonRmse': {
                    'variables': ['pr'],
                    'regions': {'pr': 'equatorial_pacific'},
                    'obs_name': {'pr': ['ERA-Interim', 'GPCPv2.3']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalSshLatRmse': {
                    'variables': ['ssh'],
                    'regions': {'ssh': 'nino3_LatExt'},
                    'obs_name': {'ssh': ['AVISO']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalSshLonRmse': {
                    'variables': ['ssh'],
                    'regions': {'ssh': 'equatorial_pacific'},
                    'obs_name': {'ssh': ['AVISO']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalSstLatRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'nino3_LatExt'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalSstLonRmse': {
                    'variables': ['sst'],
                    'regions': {'sst': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalTauxLatRmse': {
                    'variables': ['taux'],
                    'regions': {'taux': 'equatorial_pacific_LatExt'},
                    'obs_name': {'taux': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'SeasonalTauxLonRmse': {
                    'variables': ['taux'],
                    'regions': {'taux': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
            },
            'common_collection_parameters': {
                'detrending': {'method': 'linear'},
                'frequency': 'monthly',
                'min_time_steps': 12,
                'normalization': False,
                'project_interpreter': 'CMIP',
                'observed_period': ("1850-01-01 00:00:00", "2018-12-31 23:59:60.0"),
                'modeled_period': ("1850-01-01 00:00:00", "2015-12-31 23:59:60.0"),
            },
            'plot_order': ['BiasPrLatRmse', 'BiasPrLonRmse', 'BiasSstLonRmse', 'BiasTauxLonRmse',
                           'SeasonalPrLatRmse', 'SeasonalPrLonRmse', 'SeasonalSstLonRmse', 'SeasonalTauxLonRmse',
                           'EnsoSstLonRmse', 'EnsoSstTsRmse', 'EnsoAmpl', 'EnsoSeasonality', 'EnsoSstSkew',
                           'EnsodDuration', 'EnsoSstDiversity_2'],
            'description': 'Describe which science question this collection is about',
        },
        'ENSO_THF': {
            'long_name': 'Metrics Collection for ENSO performance',
            'metrics_list': {
                'EnsoFbSstLhf': {
                    'variables': ['sst', 'lhf'],
                    'regions': {'sst': 'nino3', 'lhf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'lhf': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstLwr': {
                    'variables': ['sst', 'lwr'],
                    'regions': {'sst': 'nino3', 'lwr': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'lwr': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstShf': {
                    'variables': ['sst', 'shf'],
                    'regions': {'sst': 'nino3', 'shf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'shf': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstSwr': {
                    'variables': ['sst', 'swr'],
                    'regions': {'sst': 'nino3', 'swr': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'swr': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
                'EnsoFbSstThf': {
                    'variables': ['sst', 'thf'],
                    'regions': {'sst': 'nino3', 'thf': 'nino3'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'],
                                 'thf': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'regridder': 'cdms', 'regridTool': 'esmf', 'regridMethod': 'linear',
                                   'newgrid_name': 'generic_1x1deg'},
                    'metric_computation': 'abs_relative_difference',
                },
            },
            'common_collection_parameters': {
                'detrending': {'method': 'linear'},
                'frequency': 'monthly',
                'min_time_steps': 12,
                'normalization': False,
                'project_interpreter': 'CMIP',
                'observed_period': ("1850-01-01 00:00:00", "2018-12-31 23:59:60.0"),
                'modeled_period': ("1850-01-01 00:00:00", "2015-12-31 23:59:60.0"),
            },
            'plot_order': ['EnsoFbSstThf'],
            'description': 'Describe which science question this collection is about',
        },
        'ENSO_tau': {
            'long_name': 'Metrics Collection for ENSO performance',
            'metrics_list': {
                'BiasMldLonRmse': {
                    'variables': ['mld'],
                    'regions': {'mld': 'equatorial_pacific'},
                    'obs_name': {'mld': ['Boyer', 'Sallee']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasTauxLonRmse': {
                    'variables': ['taux'],
                    'regions': {'taux': 'equatorial_pacific'},
                    'obs_name': {'taux': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'BiasTauyLonRmse': {
                    'variables': ['tauy'],
                    'regions': {'tauy': 'equatorial_pacific'},
                    'obs_name': {'tauy': ['ERA-Interim', 'Tropflux']},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoMldLonRmse': {
                    'variables': ['sst', 'mld'],
                    'regions': {'sst': 'equatorial_pacific', 'mld': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'mld': ['Boyer', 'Sallee']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoMldTsRmse': {
                    'variables': ['sst', 'mld'],
                    'regions': {'sst': 'nino3.4', 'mld': 'nino4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'mld': ['Boyer', 'Sallee']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'nbr_years_window': 6,
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoTauxLonRmse': {
                    'variables': ['sst', 'taux'],
                    'regions': {'sst': 'equatorial_pacific', 'taux': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'taux': ['ERA-Interim', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoTauxTsRmse': {
                    'variables': ['sst', 'taux'],
                    'regions': {'sst': 'nino3.4', 'taux': 'nino4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'taux': ['ERA-Interim', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'nbr_years_window': 6,
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoTauyLonRmse': {
                    'variables': ['sst', 'tauy'],
                    'regions': {'sst': 'equatorial_pacific', 'tauy': 'equatorial_pacific'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'tauy': ['ERA-Interim', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
                'EnsoTauyTsRmse': {
                    'variables': ['sst', 'tauy'],
                    'regions': {'sst': 'nino3.4', 'tauy': 'nino4'},
                    'obs_name': {'sst': ['ERA-Interim', 'HadISST', 'Tropflux'], 'tauy': ['ERA-Interim', 'Tropflux']},
                    'event_definition': {'region_ev': 'nino3.4', 'season_ev': 'DEC', 'threshold': 0.75,
                                         'normalization': True},
                    'nbr_years_window': 6,
                    'smoothing': {'window': 5, 'method': 'triangle'},
                    'regridding': {'model_orand_obs': 2, 'regridder': 'cdms', 'regridTool': 'esmf',
                                   'regridMethod': 'linear', 'newgrid_name': 'generic_1x1deg'},
                },
            },
            'common_collection_parameters': {
                'detrending': {'method': 'linear'},
                'frequency': 'monthly',
                'min_time_steps': 12,
                'normalization': False,
                'project_interpreter': 'CMIP',
                'observed_period': ("1850-01-01 00:00:00", "2018-12-31 23:59:60.0"),
                'modeled_period': ("1850-01-01 00:00:00", "2015-12-31 23:59:60.0"),
            },
            'plot_order': ['BiasMldLonRmse', 'BiasTauxLonRmse', 'BiasTauyLonRmse',
                           'EnsoMldLonRmse', 'EnsoMldTsRmse',
                           'EnsoTauxLonRmse', 'EnsoTauxTsRmse',
                           'EnsoTauyLonRmse', 'EnsoTauyTsRmse'],
            'description': 'Describe which science question this collection is about',
        },
    }
    if mc is True:
        return metrics_collection
    else:
        return metrics_collection[mc]


# List of reference observations for each variables
def ReferenceObservations(dataset=True):
    dict_ref_obs = {
        '20CRv2c': {
            'website': 'https://aims2.llnl.gov/search?project=CREATE-IP&activeFacets=%7B%22realm%22%3A%22atmos%22%2C%22time_frequency%22%3A%22mon%22%2C%22product%22%3A%22reanalysis%22%2C%22source_id%22%3A%2220CRv2c%22%7D',
            'file_name': '<var_name>' + '_Amon_reanalysis_20CRv2c_185101-201212.nc',
            'variable_name_in_file': {
                'lhf': {'var_name': 'hfls'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = rlds - rlus
                'lwr': {'var_name': ['rlds', 'rlus'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'pr'},
                'shf': {'var_name': 'hfss'},
                'sst': {'var_name': 'ts'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                'swr': {'var_name': ['rsds', 'rsus'], 'algebric_calculation': ['plus', 'minus']},
                'taux': {'var_name': 'tauu'},
                'tauy': {'var_name': 'tauv'},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = hfls + hfss + rlds - rlus + rsds - rsus
                'thf': {
                    'var_name': ['hfls', 'hfss', 'rlds', 'rlus', 'rsds', 'rsus'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
                'ts': {'var_name': 'ts'},
            },
        },
        '20CRv3': {
            'website': 'https://www.esrl.noaa.gov/psd/data/gridded/data.20thC_ReanV3.monolevel.html',
            'file_name': '<var_name>' + '*.mon.mean.nc',
            'variable_name_in_file': {
                'landmask': {'var_name': 'land'},
                'lhf': {'var_name': 'lhtfl'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = dlwrf - ulwrf
                'lwr': {'var_name': ['dlwrf', 'ulwrf'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'prate'},
                'slp': {'var_name': 'prmsl'},
                'shf': {'var_name': 'shtfl'},
                'sst': {'var_name': 'skt'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = dswrf - uswrf
                'swr': {'var_name': ['dswrf', 'uswrf'], 'algebric_calculation': ['plus', 'minus']},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = lhtfl + shtfl + dlwrf - ulwrf + dswrf - uswrf
                'thf': {
                    'var_name': ['lhtfl', 'shtfl', 'dlwrf', 'ulwrf', 'dswrf', 'uswrf'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
            },
        },
        'AVISO': {
            'website': 'https://www.aviso.altimetry.fr/en/data/products/sea-surface-height-products/global.html',
            'file_name': 'dt_global_allsat_msla_h_y????_m??.nc',
            'variable_name_in_file': {'ssh': {'var_name': 'sla'}, },
        },
        'CERA-20C': {
            'website': 'https://aims2.llnl.gov/search?project=CREATE-IP&activeFacets=%7B%22time_frequency%22%3A%22mon%22%2C%22product%22%3A%5B%22ORAreanalysis%22%2C%22reanalysis%22%5D%2C%22realm%22%3A%5B%22ocean%22%2C%22atmos%22%5D%2C%22experiment%22%3A%22CERA-20C%22%7D',
            'file_name': '<var_name>' + '_Amon_reanalysis_CERA-20C_190101-201012.nc',
            'variable_name_in_file': {
                'lhf': {'var_name': 'hfls'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = rlds - rlus
                'lwr': {'var_name': ['rlds', 'rlus'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'pr'},
                'shf': {'var_name': 'hfss'},
                'sst': {'var_name': 'ts'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                'swr': {'var_name': ['rsds', 'rsus'], 'algebric_calculation': ['plus', 'minus']},
                'taux': {'var_name': 'tauu'},
                'tauy': {'var_name': 'tauv'},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = hfls + hfss + rlds - rlus + rsds - rsus
                'thf': {
                    'var_name': ['hfls', 'hfss', 'rlds', 'rlus', 'rsds', 'rsus'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
                'ts': {'var_name': 'ts'},
            },
        },
        'CFSR': {
            'website': 'see https://aims2.llnl.gov/search?project=CREATE-IP&activeFacets=%7B%22experiment%22%3A%22CFSR%22%2C%22realm%22%3A%5B%22atmos%22%2C%22ocean%22%5D%2C%22time_frequency%22%3A%22mon%22%2C%22product%22%3A%22reanalysis%22%7D',
            'file_name': '<var_name>' + '_?mon_reanalysis_CFSR_197901-201912.nc',
            'variable_name_in_file': {
                "lhf": {"var_name": "hfls"},
                # longwave radiation computed from these variables IN THAT ORDER (on ocean grid or ocean points only)
                # lwr = rlds - rlus
                "lwr": {"var_name": ["rlds", "rlus"], "algebric_calculation": ["plus", "minus"]},
                "pr": {"var_name": "pr"},
                "shf": {"var_name": "hfss"},
                "slp": {"var_name": "psl"},
                "ssh": {"var_name": "zos"},
                "sst": {"var_name": "ts"},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                "swr": {"var_name": ["rsds", "rsus"], "algebric_calculation": ["plus", "minus"]},
                "taux": {"var_name": "tauu"},
                "tauy": {"var_name": "tauv"},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = hfls + hfss + rlds - rlus + rsds - rsus
                "thf": {
                    "var_name": ["hfls", "hfss", "rlds", "rlus", "rsds", "rsus"],
                    "algebric_calculation": ["plus", "plus", "plus", "minus", "plus", "minus"],
                },
                "ts": {"var_name": "ts"},
            },
        },
        'CMAP': {
            'website': 'https://www.esrl.noaa.gov/psd/data/gridded/data.cmap.html',
            'file_name': '<var_name>' + '.mon.mean.nc',
            'variable_name_in_file': {
                'pr': {'var_name': 'precip'},
            },
        },
        'ERA-Interim': {
            'website': 'https://aims2.llnl.gov/search?project=CREATE-IP&activeFacets=%7B%22source_id%22%3A%22ERA-Interim%22%2C%22time_frequency%22%3A%22mon%22%2C%22product%22%3A%22reanalysis%22%7D',
            'file_name': '<var_name>' + '_Amon_reanalysis_ERA-Interim_197901-201908.nc',
            'variable_name_in_file': {
                'lhf': {'var_name': 'hfls'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = rlds - rlus
                'lwr': {'var_name': ['rlds', 'rlus'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'pr'},
                'shf': {'var_name': 'hfss'},
                'sst': {'var_name': 'ts'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                'swr': {'var_name': ['rsds', 'rsus'], 'algebric_calculation': ['plus', 'minus']},
                'taux': {'var_name': 'tauu'},
                'tauy': {'var_name': 'tauv'},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = hfls + hfss + rlds - rlus + rsds - rsus
                'thf': {
                    'var_name': ['hfls', 'hfss', 'rlds', 'rlus', 'rsds', 'rsus'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
                'ts': {'var_name': 'ts'},
            },
        },
        'ERA5': {
            'website': 'https://aims2.llnl.gov/search?project=CREATE-IP&activeFacets=%7B%22realm%22%3A%22atmos%22%2C%22time_frequency%22%3A%22mon%22%2C%22product%22%3A%22reanalysis%22%2C%22experiment%22%3A%22ERA5%22%7D',
            'file_name': '<var_name>' + '_Amon_reanalysis_ERA5_197901-202012.nc',
            'variable_name_in_file': {
                'lhf': {'var_name': 'hfls'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = rlds - rlus
                'lwr': {'var_name': ['rlds', 'rlus'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'pr'},
                'shf': {'var_name': 'hfss'},
                'sst': {'var_name': 'ts'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                'swr': {'var_name': ['rsds', 'rsus'], 'algebric_calculation': ['plus', 'minus']},
                'taux': {'var_name': 'tauu'},
                'tauy': {'var_name': 'tauv'},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = hfls + hfss + rlds - rlus + rsds - rsus
                'thf': {
                    'var_name': ['hfls', 'hfss', 'rlds', 'rlus', 'rsds', 'rsus'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
                'ts': {'var_name': 'ts'},
            },
        },
        'ERSSTv5': {
            'website': 'https://www1.ncdc.noaa.gov/pub/data/cmb/ersst/v5/netcdf/',
            'file_name': 'ersst.v5.' + '<YYYYMM>' + '.nc',
            'variable_name_in_file': {
                'sst': {'var_name': 'sst'},
            },
        },
        'ESA-CCI-SST-v2-1': {
            'website': 'https://aims2.llnl.gov/search?project=obs4MIPs&activeFacets=%7B%22variable%22%3A%5B%22pr%22%2C%22rlds%22%2C%22rlus%22%2C%22rsds%22%2C%22rsus%22%2C%22tos%22%5D%2C%22frequency%22%3A%22mon%22%2C%22source_id%22%3A%22ESA-CCI-SST-v2-1%22%7D',
            'file_name': 'tos_mon_ESA-CCI-SST-v2-1_BE_gn_198109-201712.nc',
            'variable_name_in_file': {
                'sst': {'var_name': 'tos'},
            },
        },
        'GPCP-Monthly-3-2': {
            'website': 'https://aims2.llnl.gov/search?project=obs4MIPs&activeFacets=%7B%22variable%22%3A%5B%22pr%22%2C%22rlds%22%2C%22rlus%22%2C%22rsds%22%2C%22rsus%22%2C%22tos%22%5D%2C%22frequency%22%3A%22mon%22%2C%22source_id%22%3A%22GPCP-Monthly-3-2%22%7D',
            'file_name': 'pr_mon_GPCP-Monthly-3-2_RSS_gn_????01-????12.nc',
            'variable_name_in_file': {
                'pr': {'var_name': 'pr'},
            },
        },
        'HadISST': {
            'website': 'https://www.metoffice.gov.uk/hadobs/hadisst/data/download.html',
            'file_name': 'HadISST_' + '<var_name>' + '.nc',
            'variable_name_in_file': {
                'sst': {'var_name': 'sst'},
            },
        },
        'JRA-55-mdl-iso': {
            'website': 'https://aims2.llnl.gov/search?project=CREATE-IP&activeFacets=%7B%22realm%22%3A%22atmos%22%2C%22time_frequency%22%3A%22mon%22%2C%22product%22%3A%22reanalysis%22%2C%22source_id%22%3A%22JRA-55-mdl-iso%22%7D',
            'file_name': '<var_name>' + '_Amon_reanalysis_JRA-55-mdl-iso_195801-201912.nc',
            'variable_name_in_file': {
                'lhf': {'var_name': 'hfls'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = rlds - rlus
                'lwr': {'var_name': ['rlds', 'rlus'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'pr'},
                'shf': {'var_name': 'hfss'},
                'sst': {'var_name': 'ts'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                'swr': {'var_name': ['rsds', 'rsus'], 'algebric_calculation': ['plus', 'minus']},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = hfls + hfss + rlds - rlus + rsds - rsus
                'thf': {
                    'var_name': ['hfls', 'hfss', 'rlds', 'rlus', 'rsds', 'rsus'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
                'ts': {'var_name': 'ts'},
            },
        },
        'MERRA': {
            'website': 'https://aims2.llnl.gov/search?project=CREATE-IP&activeFacets=%7B%22realm%22%3A%22atmos%22%2C%22time_frequency%22%3A%22mon%22%2C%22product%22%3A%22reanalysis%22%2C%22experiment%22%3A%22MERRA%22%7D',
            'file_name': '<var_name>' + '_Amon_reanalysis_MERRA_197901-201602.nc',
            'variable_name_in_file': {
                'lhf': {'var_name': 'hfls'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = rlds - rlus
                'lwr': {'var_name': ['rlds', 'rlus'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'pr'},
                'shf': {'var_name': 'hfss'},
                'sst': {'var_name': 'ts'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                'swr': {'var_name': ['rsds', 'rsus'], 'algebric_calculation': ['plus', 'minus']},
                'taux': {'var_name': 'tauu'},
                'tauy': {'var_name': 'tauv'},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = hfls + hfss + rlds - rlus + rsds - rsus
                'thf': {
                    'var_name': ['hfls', 'hfss', 'rlds', 'rlus', 'rsds', 'rsus'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
                'ts': {'var_name': 'ts'},
            },
        },
        'MERRA2': {
            'website': 'https://aims2.llnl.gov/search?project=CREATE-IP&activeFacets=%7B%22realm%22%3A%22atmos%22%2C%22time_frequency%22%3A%22mon%22%2C%22product%22%3A%22reanalysis%22%2C%22experiment%22%3A%22MERRA-2%22%7D',
            'file_name': '<var_name>' + '_Amon_reanalysis_MERRA2_198001-202012.nc',
            'variable_name_in_file': {
                'lhf': {'var_name': 'hfls'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = rlds - rlus
                'lwr': {'var_name': ['rlds', 'rlus'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'pr'},
                'shf': {'var_name': 'hfss'},
                'sst': {'var_name': 'ts'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                'swr': {'var_name': ['rsds', 'rsus'], 'algebric_calculation': ['plus', 'minus']},
                'taux': {'var_name': 'tauu'},
                'tauy': {'var_name': 'tauv'},
                # total heat flux computed from these variables IN THAT ORDER
                # tfh = hfls + hfss + rlds - rlus + rsds - rsus
                'thf': {
                    'var_name': ['hfls', 'hfss', 'rlds', 'rlus', 'rsds', 'rsus'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
                'ts': {'var_name': 'ts'},
            },
        },
        'NCEP2': {
            'website': 'https://www.esrl.noaa.gov/psd/data/gridded/data.ncep.reanalysis2.gaussian.html',
            'file_name': '<var_name>' + '.sfc.mon.mean.nc',
            'variable_name_in_file': {
                'landmask': {'var_name': 'land'},
                'lhf': {'var_name': 'lhtfl'},
                # longwave radiation computed from these variables IN THAT ORDER
                # lwr = rlds - rlus
                'lwr': {'var_name': ['dlwrf', 'ulwrf'], 'algebric_calculation': ['plus', 'minus']},
                'pr': {'var_name': 'prate'},
                'shf': {'var_name': 'shtfl'},
                'slp': {'var_name': 'pres'},
                'sst': {'var_name': 'skt'},
                # shortwave radiation computed from these variables IN THAT ORDER
                # swr = rsds - rsus
                'swr': {'var_name': ['dswrf', 'uswrf'], 'algebric_calculation': ['plus', 'minus']},
                'taux': {'var_name': 'uflx'},
                'tauy': {'var_name': 'vflx'},
                'thf': {
                    'var_name': ['lhtfl', 'shtfl', 'dlwrf', 'ulwrf', 'dswrf', 'uswrf'],
                    'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus'],
                },
            },
        },
        'Tropflux': {
            'website': 'https://incois.gov.in/tropflux/tf_products.jsp',
            'file_name': '<var_name>' + '_tropflux_1m_*.nc',
            'variable_name_in_file': {
                'lhf': {'var_name': 'lhf'},
                'lwr': {'var_name': 'lwr'},
                'shf': {'var_name': 'shf'},
                'sst': {'var_name': 'sst'},
                'swr': {'var_name': 'swr'},
                'taux': {'var_name': 'taux'},
                'tauy': {'var_name': 'tauy'},
                'thf': {'var_name': 'netflux'},
            },
        },
    }
    if dataset is True:
        return dict_ref_obs
    else:
        return dict_ref_obs[dataset]


def ReferenceRegions(region=True):
    dict_reference_regions = {
        'global': {'long_name': 'Global 60S-60N', 'latitude': (-60., 60.), 'longitude': (0., 360.)},
        'global2': {'long_name': 'Global', 'latitude': (-90., 90.), 'longitude': (0., 360.)},
        'tropical_pacific': {
            'long_name': 'Tropical Pacific (TP)', 'latitude': (-30., 30.), 'longitude': (120., 280.),
        },
        'equatorial_pacific': {
            'long_name': 'Equatorial Pacific (EP)', 'latitude': (-5., 5.), 'longitude': (150., 270.),
        },
        'equatorial_pacific_LatExt': {
            'long_name': 'Equatorial Pacific (EP)', 'latitude': (-15., 15.), 'longitude': (150., 270.),
        },
        'equatorial_pacific_LatExt2': {
            'long_name': 'Equatorial Pacific extended in latitude', 'latitude': (-15., 15.), 'longitude': (120., 285.),
        },
        'eastern_equatorial_pacific': {
            'long_name': 'Western Equatorial Pacific (WEP)', 'latitude': (-5., 5.), 'longitude': (205., 280.),
        },
        'western_equatorial_pacific': {
            'long_name': 'Eastern Equatorial Pacific (EEP)', 'latitude': (-5., 5.), 'longitude': (120., 205.),
        },
        'nino1+2': {'long_name': 'Niño 1+2', 'latitude': (-10., 0.), 'longitude': (270., 280.)},
        'nino3': {'long_name': 'Niño 3', 'latitude': (-5., 5.), 'longitude': (210., 270.)},
        'nino3_LatExt': {
            'long_name': 'Niño 3 extended in latitude', 'latitude': (-15., 15.), 'longitude': (210., 270.)
        },
        'nino3.4': {'long_name': 'Niño 3.4', 'latitude': (-5., 5.), 'longitude': (190., 240.)},
        'nino4': {'long_name': 'Niño 4', 'latitude': (-5., 5.), 'longitude': (160., 210.)},
        # AR5 reference regions
        'ALA': {'long_name': 'Alaska/N.W. Canada', 'latitude': (60., 72.6), 'longitude': (192., 255.),
                'maskland': False, 'maskocean': True},
        # 'AMZ': {'long_name': 'Amazon', 'polygon shaped region, I do not know how to select it'},
        # 'CAM': {'long_name': 'Central America/Mexico', 'polygon shaped region, I do not know how to select it'},
        'CAS': {'long_name': 'Central Asia', 'latitude': (30., 50.), 'longitude': (60., 75.), 'maskland': False,
                'maskocean': True},
        # 'CEU': {'long_name': 'Central Europe', 'polygon shaped region, I do not know how to select it'},
        'CGI': {'long_name': 'Canada/Greenland/Iceland', 'latitude': (50., 85.), 'longitude': (255., 350.),
                'maskland': False, 'maskocean': True},
        'CNA': {'long_name': 'Central North America', 'latitude': (28.6, 50.), 'longitude': (255., 275.),
                'maskland': False, 'maskocean': True},
        'EAF': {'long_name': 'East Africa', 'latitude': (-11.4, 15.), 'longitude': (25., 52.), 'maskland': False,
                'maskocean': True},
        'EAS': {'long_name': 'East Asia', 'latitude': (20., 50.), 'longitude': (100., 145.), 'maskland': False,
                'maskocean': True},
        'ENA': {'long_name': 'East North America', 'latitude': (25., 50.), 'longitude': (275., 300.), 'maskland': False,
                'maskocean': True},
        'MED': {'long_name': 'South Europe/Mediterranean', 'latitude': (30., 45.), 'longitude': (350., 400.),
                'maskland': False, 'maskocean': True},
        'NAS': {'long_name': 'North Asia', 'latitude': (50., 70.), 'longitude': (40., 180.), 'maskland': False,
                'maskocean': True},
        'NAU': {'long_name': 'North Australia', 'latitude': (-30., -10.), 'longitude': (110., 155.), 'maskland': False,
                'maskocean': True},
        'NEB': {'long_name': 'North-East Brazil', 'latitude': (-20., 0.), 'longitude': (310., 326.), 'maskland': False,
                'maskocean': True},
        # 'NEU': {'long_name': 'North Europe', 'polygon shaped region, I do not know how to select it'},
        'SAF': {'long_name': 'Southern Africa', 'latitude': (-35., -11.4), 'longitude': (350., 412.), 'maskland': False,
                'maskocean': True},
        'SAH': {'long_name': 'Sahara', 'latitude': (15., 30.), 'longitude': (340., 400.), 'maskland': False,
                'maskocean': True},
        # 'SAS': {'long_name': 'South Asia', 'polygon shaped region, I do not know how to select it'},
        'SAU': {'long_name': 'South Australia/New Zealand', 'latitude': (-50., -30.), 'longitude': (110., 180.),
                'maskland': False, 'maskocean': True},
        'SEA': {'long_name': 'Southeast Asia', 'latitude': (-10., 20.), 'longitude': (95., 155.), 'maskland': False,
                'maskocean': False},
        # 'SSA': {'long_name': 'Southeastern South America', 'polygon shaped region, I do not know how to select it'},
        'TIB': {'long_name': 'Tibetan Plateau', 'latitude': (30., 50.), 'longitude': (75., 100.), 'maskland': False,
                'maskocean': True},
        'WAF': {'long_name': 'West Africa', 'latitude': (-11.4, 15.), 'longitude': (340., 385.), 'maskland': False,
                'maskocean': True},
        'WAS': {'long_name': 'West Asia', 'latitude': (15., 50.), 'longitude': (40., 60.), 'maskland': False,
                'maskocean': True},
        'WNA': {'long_name': 'West North America', 'latitude': (28.6, 60.), 'longitude': (230., 255.),
                'maskland': False, 'maskocean': True},
        # 'WSA': {'long_name': 'West Coast South America', 'polygon shaped region, I do not know how to select it'},
        # non-SREX reference regions
        'ANT': {'long_name': 'Antarctica', 'latitude': (-90., -50.), 'longitude': (0., 360.), 'maskland': False,
                'maskocean': False},
        'ARC': {'long_name': 'Arctic', 'latitude': (67.5, 90.), 'longitude': (0., 360.), 'maskland': False,
                'maskocean': False},
        # 'CAR': {
        #     'long_name': 'Caribbean', 'polygon shaped region, I do not know how to select it'
        # },
        'NTP': {'long_name': 'Northern Tropical Pacific', 'latitude': (5., 25.), 'longitude': (155., 210.)},
        'STP': {'long_name': 'Southern Topical Pacific', 'latitude': (-25., -5.), 'longitude': (155., 230.)},
        'ETP': {'long_name': 'Equatorial Tropical Pacific', 'latitude': (-5., 5.), 'longitude': (155., 210.)},
        'WIO': {'long_name': 'West Indian Ocean', 'latitude': (-25., 5.), 'longitude': (52., 75.), 'maskland': False,
                'maskocean': False},
        # Power and Delage's (2018) oceanic regions
        'CEP': {'long_name': 'Central Equatorial Pacific', 'latitude': (-5., 5.), 'longitude': (180., 220.),
                'maskland': True, 'maskocean': False},
        'CNP': {'long_name': 'Central Northern Tropical Pacific', 'latitude': (5., 15.), 'longitude': (180., 220.),
                'maskland': True, 'maskocean': False},
        'CSP': {'long_name': 'Central Southern Tropical Pacific', 'latitude': (-15., -5.), 'longitude': (180., 220.),
                'maskland': True, 'maskocean': False},
        'INO': {'long_name': 'Indian Ocean', 'latitude': (-25., 0.), 'longitude': (55., 95.), 'maskland': True,
                'maskocean': False},
        # YYP regions
        'africaSE': {'long_name': 'South and East Africa', 'latitude': (-40, 15.), 'longitude': (0., 55.),
                     'maskland': False, 'maskocean': True},
        'americaN': {'long_name': 'North America', 'latitude': (10., 60.), 'longitude': (235., 300.),
                     'maskland': False, 'maskocean': True},
        'americaS': {'long_name': 'South America', 'latitude': (-60., 15.), 'longitude': (275., 330.),
                     'maskland': False, 'maskocean': True},
        'asiaS': {'long_name': 'South Asia', 'latitude': (-10., 30.), 'longitude': (65., 130.),
                  'maskland': False, 'maskocean': True},
        'oceania': {'long_name': 'oceania', 'latitude': (-50., 0.), 'longitude': (110., 180.), 'maskland': False,
                    'maskocean': True},
    }
    if region is True:
        return dict_reference_regions
    else:
        return dict_reference_regions[region]


def CmipVariables():
    dict_cmip_variables = {
        'reference': 'http://cfconventions.org/Data/cf-standard-names/46/build/cf-standard-name-table.html',
        'variable_name_in_file': {
            # line keys:
            # '<internal_metrics_variable_name>':{'var_name':'<var_name_in_file>','cf_name':<as per ref above>,
            #                                     'cf_unit':'<unit_in_file>'}
            # areacell
            'areacell': {'var_name': 'areacella', 'cf_name': 'cell_area', 'cf_units': 'm2'},
            # landmask
            'landmask': {'var_name': 'sftlf', 'cf_name': 'cell_area', 'cf_units': '1'},
            # latent heat flux
            'lhf': {'var_name': 'hfls', 'cf_name': 'land_area_fraction', 'cf_units': 'W m-2'},
            # longwave radiation computed from these variables IN THAT ORDER
            # lwr = rlds - rlus
            # sometimes lwr is included in the datasets in a variable called 'rls'
            'lwr': {
                'var_name': ['rlds', 'rlus'],
                'cf_name': ['surface_downwelling_longwave_flux_in_air', 'surface_upwelling_longwave_flux_in_air'],
                'cf_units': 'W m-2', 'algebric_calculation': ['plus', 'minus']},
            # Rainfall Flux
            'pr': {'var_name': 'pr', 'cf_name': 'rainfall_flux', 'cf_units': 'kg m-2 s-1'},
            # Sea Level Pressure
            'slp': {'var_name': 'psl', 'cf_name': 'air_pressure_at_mean_sea_level', 'cf_units': 'Pa'},
            # sensible heat flux (on ocean grid or ocean points only)
            'shf': {'var_name': 'hfss', 'cf_name': 'surface_upward_sensible_heat_flux', 'cf_units': 'W m-2'},
            # sea surface height
            'ssh': {'var_name': 'zos', 'cf_name': 'sea_surface_height_above_geoid', 'cf_units': 'm'},
            # sea surface temperature
            'sst': {'var_name': 'ts', 'cf_name': 'sea_surface_temperature', 'cf_units': 'K'},
            # shortwave radiation computed from these variables IN THAT ORDER
            # swr = rsds - rsus
            # sometimes swr is included in the datasets in a variable called 'rss'
            'swr': {
                'var_name': ['rsds', 'rsus'],
                'cf_name': ['surface_downwelling_shortwave_flux_in_air', 'surface_upwelling_shortwave_flux_in_air'],
                'cf_units': 'W m-2', 'algebric_calculation': ['plus', 'minus']
            },
            # zonal surface wind stress
            'taux': {'var_name': 'tauu', 'cf_name': 'surface_downward_eastward_stress', 'cf_units': 'Pa'},
            # meridional surface wind stress
            'tauy': {'var_name': 'tauv', 'cf_name': 'surface_downward_northward_stress', 'cf_units': 'Pa'},
            # total heat flux computed from these variables IN THAT ORDER
            # tfh = hfls + hfss + rlds - rlus + rsds - rsus
            # sometimes rls = rlds - rlus and rss = rsds - rsus
            # sometimes thf is included in the datasets in a variable called 'hfds', 'netflux', 'thflx',...
            'thf': {
                'var_name': ['hfls', 'hfss', 'rlds', 'rlus', 'rsds', 'rsus'],
                'cf_name': ['surface_upward_latent_heat_flux', 'surface_upward_sensible_heat_flux',
                            'surface_downwelling_longwave_flux_in_air', 'surface_upwelling_longwave_flux_in_air',
                            'surface_downwelling_shortwave_flux_in_air', 'surface_upwelling_shortwave_flux_in_air'],
                'cf_units': 'W m-2', 'algebric_calculation': ['plus', 'plus', 'plus', 'minus', 'plus', 'minus']
            },
        },
    }
    return dict_cmip_variables
