import numpy.sqrt as NUMPYsqrt
import numpy.square as NUMPYsquare

# based on uvcdat
from EnsoToolsLib import CheckUnits,ComputeMultiply,ComputeRms,ComputeStd,SpatialAverage,TimeAverage,ReadAndSelectRegion,SeasonalMean
from EnsoToolsLib import interannual_variabilty_std_annual_cycle_removed,get_slope_linear_regression_from_anomaly









# ---------------------------------------------------------------------------------------------------------------------#
#
# Libray to compute ENSO metrics
# These functions have file names and variable names as inputs and metric as output
#


def EnsoAlphaLhf(sstfile, lhffile, sstname, lhfname, sstbox, lhfbox):
    '''
    The EnsoAlphaLhf() function computes the regression of nino3 lhfA (latent heat flux anomalies) over nino3 sstA

    Author:	Yann Planton : yann.planton@locean-ipsl.upmc.fr
    Co-author:

    Created on Thu Oct  5 2017

    Inputs:
    ------
    - sstfile   - time/lat/lon SST array using Omon values
    - lhffile   - time/lat/lon LHF array using Omon values
    - sstname   - name of sst variable (tos, ts)
    - lhfname   - name of lhf variable (lhf, hfls)
    - sstbox    - name of box ('nino3') for sst
    - lhfbox    - name of box ('nino3') for lhf

    Output:
    ------
    - alphaLhfMetric dict:
        - name, value, value_error, units, method, nyears, ref, nonlinearity, nonlinearity_error

    Method:
    -------
    - uses tools from PCMDI monthly_variability_statistics library

    '''
    # Define metric attributes
    Name = 'Latent feedback (alpha_lh)'
    Units = 'W/m2/C'
    Method = 'Regression of ' + lhfbox + ' lhfA over ' + sstbox + ' sstA'
    Ref = 'Using CDAT regression calculation'

    # Read file and select the right region
    sst = ReadAndSelectRegion(sstfile, sstname, sstbox)
    lhf = ReadAndSelectRegion(lhffile, lhfname, lhfbox)

    # Unit K to C
    sst = CheckUnits(sst, 'temperature')

    # Number of years
    yearN = sst.shape[0] / 12

    # Average and compute regression of interannual anomaly
    alphaLhfSlope = get_slope_linear_regression_from_anomaly(lhf, sst, 0, return_stderr=True)  # (all points)
    alphaLhfSlopePos = get_slope_linear_regression_from_anomaly(lhf, sst, 1,
                                                                return_stderr=True)  # (positive SSTA = El Nino)
    alphaLhfSlopeNeg = get_slope_linear_regression_from_anomaly(lhf, sst, -1,
                                                                return_stderr=True)  # (negative SSTA = La Nina)
    # Create output
    alphaLhfMetric = {'name': Name, 'value': alphaLhfSlope[0], 'value_error': alphaLhfSlope[1],
                      'units': Units, 'method': Method, 'nyears': yearN, 'ref': Ref,
                      'nonlinearity': alphaLhfSlopeNeg[0] - alphaLhfSlopePos[0],
                      'nonlinearity_error': alphaLhfSlopeNeg[1] + alphaLhfSlopePos[1]}
    return alphaLhfMetric


def EnsoAlphaLwr(sstfile, lwrfile, sstname, lwrname, sstbox, lwrbox):
    '''
    The EnsoAlphaLwr() function computes the regression of nino3 lwrA (net surface longwave radiation anomalies)
    over nino3 sstA

    The net surface longwave radiation is not a CMIP5 variable.
    Either the user computes it and sends the filename and the varname or he feeds into swrfile and swrname of this
    function a list() of downward and upward radiations files and variable names (CMIP5: rlds and rlus)

    Author:	Yann Planton : yann.planton@locean-ipsl.upmc.fr
    Co-author:

    Created on Thu Oct  5 2017

    Inputs:
    ------
    - sstfile   - time/lat/lon SST array using Omon values
    - lwrfile   - time/lat/lon LWR array using Omon values (may be a list of files)
    - sstname   - name of sst variable (tos, ts)
    - lwrname   - name of lwr variable (lwr, rlds - rlus) (may be a list of variables)
    - sstbox    - name of box ('nino3') for sst
    - lwrbox    - name of box ('nino3') for lwr

    Output:
    ------
    - alphaLwrMetric dict:
        - name, value, value_error, units, method, nyears, ref, nonlinearity, nonlinearity_error

    Method:
    -------
    - uses tools from PCMDI monthly_variability_statistics library

    '''
    # Define metric attributes
    Name = 'Longwave feedback (alpha_lwr)'
    Units = 'W/m2/C'
    Method = 'Regression of ' + lwrbox + ' lwrA over ' + sstbox + ' sstA'
    Ref = 'Using CDAT regression calculation'

    # Read file and select the right region
    sst = ReadAndSelectRegion(sstfile, sstname, sstbox)
    sst = CheckUnits(sst, 'temperature')

    if isinstance(lwrfile, basestring):
        lwr = ReadAndSelectRegion(lwrfile, lwrname, lwrbox)
        lwr = CheckUnits(lwr, 'heat flux')
    elif isinstance(lwrfile, list):
        rlds = ReadAndSelectRegion(lwrfile[0], lwrname[0], lwrbox)
        rlds = CheckUnits(rlds, 'heat flux')
        rlus = ReadAndSelectRegion(lwrfile[1], lwrname[1], lwrbox)
        rlus = CheckUnits(rlus, 'heat flux')
        lwr = rlds - rlus

    # Number of years
    yearN = sst.shape[0] / 12

    # Average and compute regression of interannual anomaly
    alphaLwrSlope = get_slope_linear_regression_from_anomaly(lwr, sst, 0, return_stderr=True)  # (all points)
    alphaLwrSlopePos = get_slope_linear_regression_from_anomaly(lwr, sst, 1,
                                                                return_stderr=True)  # (positive SSTA = El Nino)
    alphaLwrSlopeNeg = get_slope_linear_regression_from_anomaly(lwr, sst, -1,
                                                                return_stderr=True)  # (negative SSTA = La Nina)

    # Create output
    alphaLwrMetric = {'name': Name, 'value': alphaLwrSlope[0], 'value_error': alphaLwrSlope[1],
                      'units': Units, 'method': Method, 'nyears': yearN, 'ref': Ref,
                      'nonlinearity': alphaLwrSlopeNeg[0] - alphaLwrSlopePos[0],
                      'nonlinearity_error': alphaLwrSlopeNeg[1] + alphaLwrSlopePos[1]}

    return alphaLwrMetric


def EnsoAlphaSwr(sstfile, swrfile, sstname, swrname, sstbox, swrbox):
    '''
    The EnsoAlphaSwr() function computes the regression of nino3 swrA (net surface shortwave radiation anomalies)
    over nino3 sstA

    The net surface shortwave radiation is not a CMIP5 variable.
    Either the user computes it and sends the filename and the varname or he feeds into swrfile and swrname of this
    function a list() of downward and upward radiations files and variable names (CMIP5: rsds and rsus)

    Author:	Yann Planton : yann.planton@locean-ipsl.upmc.fr
    Co-author:

    Created on Thu Oct  5 2017

    Inputs:
    ------
    - sstfile   - time/lat/lon SST array using Omon values
    - swrfile   - time/lat/lon SWR array using Omon values (may be a list of files)
    - sstname   - name of sst variable (tos, ts)
    - swrname   - name of swr variable (swr, rss, rsds - rsus) (may be a list of variables)
    - sstbox    - name of box ('nino3') for sst
    - swrbox    - name of box ('nino3') for swr

    Output:
    ------
    - alphaSwrMetric dict:
        - name, value, value_error, units, method, nyears, ref, nonlinearity, nonlinearity_error

    Method:
    -------
    - uses tools from PCMDI monthly_variability_statistics library

    '''
    # Define metric attributes
    Name = 'Shortwave feedback (alpha_sw)'
    Units = 'W/m2/C'
    Method = 'Regression of ' + swrbox + ' swrA over ' + sstbox + ' sstA'
    Ref = 'Using CDAT regression calculation'

    # Read file and select the right region
    sst = ReadAndSelectRegion(sstfile, sstname, sstbox)
    sst = CheckUnits(sst, 'temperature')

    if isinstance(swrfile, basestring):
        swr = ReadAndSelectRegion(swrfile, swrname, swrbox)
        swr = CheckUnits(swr, 'heat flux')
    elif isinstance(swrfile, list):
        rsds = ReadAndSelectRegion(swrfile[0], swrname[0], swrbox)
        rsds = CheckUnits(rsds, 'heat flux')
        rsus = ReadAndSelectRegion(swrfile[1], swrname[1], swrbox)
        rsus = CheckUnits(rsus, 'heat flux')
        swr = rsds - rsus

    # Number of years
    yearN = sst.shape[0] / 12

    # Average and compute regression of interannual anomaly
    alphaSwrSlope = get_slope_linear_regression_from_anomaly(swr, sst, 0, return_stderr=True)  # (all points)
    alphaSwrSlopePos = get_slope_linear_regression_from_anomaly(swr, sst, 1,
                                                                return_stderr=True)  # (positive SSTA = El Nino)
    alphaSwrSlopeNeg = get_slope_linear_regression_from_anomaly(swr, sst, -1,
                                                                return_stderr=True)  # (negative SSTA = La Nina)

    # Create output
    alphaSwrMetric = {'name': Name, 'value': alphaSwrSlope[0], 'value_error': alphaSwrSlope[1],
                      'units': Units, 'method': Method, 'nyears': yearN, 'ref': Ref,
                      'nonlinearity': alphaSwrSlopeNeg[0] - alphaSwrSlopePos[0],
                      'nonlinearity_error': alphaSwrSlopeNeg[1] + alphaSwrSlopePos[1]}

    return alphaSwrMetric


def EnsoAlphaThf(sstfile, thffile, sstname, thfname, sstbox, thfbox):
    '''
    The EnsoAlphaThf() function computes the regression of nino3 thfA (total heat flux anomalies) over nino3 sstA
    The total heat flux is the sum of four term:
         - net surface shortwave radiation,
         - net surface longwave radiation,
         - latent heat flux,
         - sensible heat flux

    The total heat flux is not always available is models or observations.
    Either the user computes it and sends the filename and the varname or he feeds into thffile and thfname of this
    function a list() of the four needed files and variable names (CMIP5: rsds-rsus, rlds-rlus, hfls, hfss)

    Author:	Yann Planton : yann.planton@locean-ipsl.upmc.fr
    Co-author:

    Created on Thu Oct  5 2017

    Inputs:
    ------
    - sstfile   - time/lat/lon SST array using Omon values
    - thffile   - time/lat/lon THF array using Omon values (may be a list of files)
    - sstname   - name of sst variable (tos, ts)
    - thfname   - name of thf variable (thf, netflux, thflx, swr + lwr + lhf + shf) (may be a list of variables)
    - sstbox    - name of box ('nino3') for sst
    - thfbox    - name of box ('nino3') for thf

    Output:
    ------
    - alphaMetric dict:
        - name, value, value_error, units, method, nyears, ref, nonlinearity, nonlinearity_error

    Method:
    -------
    - uses tools from PCMDI monthly_variability_statistics library

    '''
    # Define metric attributes
    Name = 'Heat flux feedback (alpha)'
    Units = 'W/m2/C'
    Method = 'Regression of ' + thfbox + ' thfA over ' + sstbox + ' sstA'
    Ref = 'Using CDAT regression calculation'

    # Read file and select the right region
    sst = ReadAndSelectRegion(sstfile, sstname, sstbox)
    sst = CheckUnits(sst, 'temperature')

    if isinstance(thffile, basestring):
        thf = ReadAndSelectRegion(thffile, thfname, thfbox)
        thf = CheckUnits(thf, 'heat flux')
    elif isinstance(thffile, list):
        tmp = list()
        for ii in range(len(thffile)):
            val = ReadAndSelectRegion(thffile[ii], thfname[ii], thfbox)
            val = CheckUnits(val, 'heat flux')
            tmp.append(val)
        try:
            del thf
        except:
            pass
        for ii in range(len(thffile)):
            try:
                thf
            except:
                thf = tmp[ii]
            else:
                thf = thf + tmp[ii]

    # Number of years
    yearN = sst.shape[0] / 12

    # Average and compute regression of interannual anomaly
    alphaSlope = get_slope_linear_regression_from_anomaly(thf, sst, 0, return_stderr=True)  # (all points)
    alphaSlopePos = get_slope_linear_regression_from_anomaly(thf, sst, 1,
                                                             return_stderr=True)  # (positive SSTA = El Nino)
    alphaSlopeNeg = get_slope_linear_regression_from_anomaly(thf, sst, -1,
                                                             return_stderr=True)  # (negative SSTA = La Nina)

    # Create output
    alphaMetric = {'name': Name, 'value': alphaSlope[0], 'value_error': alphaSlope[1],
                   'units': Units, 'method': Method, 'nyears': yearN, 'ref': Ref,
                   'nonlinearity': alphaSlopeNeg[0] - alphaSlopePos[0],
                   'nonlinearity_error': alphaSlopeNeg[1] + alphaSlopePos[1]}

    return alphaMetric


def EnsoAmpl(sstfile, sstname, ninobox):
    '''
    The EnsoAmpl() function computes the sstA standard deviation in a ninobox

    Author:	Eric Guilyardi : Eric.Guilyardi@locean-ipsl.upmc.fr
    Co-author: Yann Planton : yann.planton@locean-ipsl.upmc.fr

    Created on Mon Jan  9 11:05:18 CET 2017

    Inputs:
    ------
    - sstfile	- time/lat/lon SST array using Omon values
    - sstname	- name of sst variable (tos, ts)
    - ninobox	- name of box ('nino3','nino3.4','nino4')

    Output:
    ------
    - amplMetric dict:
        - name, value, value_error, units, method, nyears, ref

    Method:
    -------
    - uses tools from PCMDI monthly_variability_statistics library

    '''
    # Define metric attributes
    Name = 'ENSO amplitude'
    Units = 'C'
    Method = 'Standard deviation of SSTA in ' + ninobox
    Ref = 'Using CDAT std dev calculation'

    # Read file and select the right region
    sst = ReadAndSelectRegion(sstfile, sstname, ninobox)
    sst = CheckUnits(sst, 'temperature')

    # Number of years
    yearN = sst.shape[0] / 12

    # Average, in box, compute anomaly wrt annual cycle and std dev
    sstStd = interannual_variabilty_std_annual_cycle_removed(sst)

    # Standard Error of the Standard Deviation (function of nyears)
    sstStdErr = sstStd / NUMPYsqrt(yearN)

    # Create output
    amplMetric = {'name': Name, 'value': sstStd, 'value_error': sstStdErr, 'units': Units, 'method': Method,
                  'nyears': yearN, 'ref': Ref}

    return amplMetric


def EnsoMu(sstfile, tauxfile, sstname, tauxname, sstbox, tauxbox):
    '''
    The EnsoMu() function computes the regression of nino4 tauxA over nino3 sstA

    Author:	Eric Guilyardi : Eric.Guilyardi@locean-ipsl.upmc.fr
    Co-author: Yann Planton : yann.planton@locean-ipsl.upmc.fr

    Created on Mon Jan  9 11:05:18 CET 2017

    Inputs:
    ------
    - sstfile	- time/lat/lon SST array using Omon values
    - tauxfile   - time/lat/lon Taux array using Omon values
    - sstname	- name of sst variable (tos, ts)
    - tauxname   - name of taux variable (taux, tauu)
    - sstbox	 - name of box ('nino3') for sst
    - tauxbox	- name of box ('nino4') for taux

    Output:
    ------
    - muMetric dict:
        - name, value, value_error, units, method, nyears, ref, nonlinearity, nonlinearity_error

    Method:
    -------
    - uses tools from PCMDI monthly_variability_statistics library

    '''
    # Define metric attributes
    Name = 'Bjerknes feedback (mu)'
    Units = '10-3 N/m2/C'
    Method = 'Regression of ' + tauxbox + ' tauxA over ' + sstbox + ' sstA'
    Ref = 'Using CDAT regression calculation'

    # Read file and select the right region
    sst = ReadAndSelectRegion(sstfile, sstname, sstbox)
    sst = CheckUnits(sst, 'temperature')
    taux = ReadAndSelectRegion(tauxfile, tauxname, tauxbox)
    taux = CheckUnits(taux, 'wind stress')

    # Match time if different between sst and taux
    if sst.shape[0] != taux.shape[0]: 
        sst, taux = MatchTimeDimension(sst, taux)

    # Number of years
    yearN = sst.shape[0] / 12

    # Average and compute regression of interannual anomaly
    muSlope = get_slope_linear_regression_from_anomaly(taux, sst, 0, return_stderr=True)  # (all points)
    muSlopePos = get_slope_linear_regression_from_anomaly(taux, sst, 1, return_stderr=True)  # (positive SSTA = El Nino)
    muSlopeNeg = get_slope_linear_regression_from_anomaly(taux, sst, -1,
                                                          return_stderr=True)  # (negative SSTA = La Nina)
    # Change units
    muSlope = ComputeMultiply(muSlope, 1000.)
    muSlopePos = ComputeMultiply(muSlopePos, 1000.)
    muSlopeNeg = ComputeMultiply(muSlopeNeg, 1000.)
    # Create output
    muMetric = {'name': Name, 'value': muSlope[0], 'value_error': muSlope[1],
                'units': Units, 'method': Method, 'nyears': yearN, 'ref': Ref,
                'nonlinearity': muSlopeNeg[0] - muSlopePos[0], 'nonlinearity_error': muSlopeNeg[1] + muSlopePos[1]}

    return muMetric


def EnsoRMSE(sstfilemodel, sstnamemodel, sstfileobs, sstnameobs, ninobox, centered_rmse=0):
    '''
    The EnsoRMSE() function computes the SST spatial root mean square error (RMSE) in a ninobox

    Author:	Yann Planton : yann.planton@locean-ipsl.upmc.fr
    Co-author:

    Created on Thu Oct  5 2017

    Inputs:
    ------
    - sstfilemodel  - time/lat/lon SST array using Omon values
    - sstfileobs    - time/lat/lon SST array using Omon values
    - sstnamemodel  - name of sst variable (tos, ts)
    - sstnameobs    - name of sst variable (tos, ts)
    - ninobox       - name of box ('nino3','nino3.4','nino4')

    Output:
    ------
    - rmseMetric dict:
        - name, value, units, method, nyears_model, nyears_observation, ref

    Method:
    -------
    - uses tools from PCMDI monthly_variability_statistics library

    Notes:
    -----
    - TODO: add error calculation to rmse (function of nyears)

    '''
    # Define metric attributes
    Name = 'ENSO RMSE'
    Units = 'C'
    Method = 'Spatial root mean square error SST in ' + ninobox
    Ref = 'Using CDAT regriding and rms (uncentered and biased) calculation'

    # Read file and select the right region
    sst_model = ReadAndSelectRegion(sstfilemodel, sstnamemodel, ninobox)
    sst_model = CheckUnits(sst_model, 'temperature')
    sst_observation = ReadAndSelectRegion(sstfileobs, sstnameobs, ninobox)
    sst_observation = CheckUnits(sst_observation, 'temperature')

    # Number of years
    yearN_model = sst_model.shape[0] / 12
    yearN_observation = sst_model.shape[0] / 12

    # Time average
    sst_model = TimeAverage(sst_model)
    sst_observation = TimeAverage(sst_observation)

    # Regrid model SST on observation grid
    sst_model = sst_model.regrid(sst_observation.getGrid(), regridTool='regrid2')

    # Average, in box, compute anomaly wrt annual cycle and std dev
    sstRmse = ComputeRms(sst_model, sst_observation, axis='xy', weights='weighted', centered=centered_rmse)

    # Create output
    rmseMetric = {'name': Name, 'value': sstRmse, 'value_error': None, 'units': Units, 'method': Method,
                  'nyears_model': yearN_model,
                  'nyears_obs': yearN_observation, 'ref': Ref}
    return rmseMetric


def EnsoSeasonality(sstfile, sstname, ninobox):
    '''
    The EnsoSeasonality() function computes ratio between the November-December-January (NDJ)
    and March-April-May (MAM) average standard deviation of sstA in a ninobox

    Author:	Yann Planton : yann.planton@locean-ipsl.upmc.fr
    Co-author:

    Created on Thu Oct  5 2017

    Inputs:
    ------
    - sstfile	- time/lat/lon SST array using Omon values
    - sstname	- name of sst variable (tos, ts)
    - ninobox	- name of box ('nino3','nino3.4','nino4')

    Output:
    ------
    - SeaMetric dict:
        - name, value, value_error, units, method, nyears, ref

    Method:
    -------
    - uses tools from PCMDI monthly_variability_statistics library

    '''
    # Define metric attributes
    Name = 'ENSO Seasonality'
    Units = ''
    Method = 'Ratio between NDJ and MAM standard deviation of SSTA in ' + ninobox
    Ref = 'Using CDAT std dev calculation'
    # Read file and select the right region
    sst = ReadAndSelectRegion(sstfile, sstname, ninobox)
    sst = CheckUnits(sst, 'temperature')

    # Number of years
    yearN = sst.shape[0] / 12

    # Seasonal ans Spatial average
    sst_NDJ = SpatialAverage(SeasonalMean(sst, 'NDJ'))
    sst_MAM = SpatialAverage(SeasonalMean(sst, 'MAM'))

    # Compute std dev and ratio
    sst_NDJ_std = ComputeStd(sst_NDJ)
    sst_MAM_std = ComputeStd(sst_MAM)
    ratioStd = float(sst_NDJ_std / sst_MAM_std)

    # Standard Error of the Standard Deviation (function of nyears)
    sst_NDJ_std_err = sst_NDJ_std / NUMPYsqrt(yearN - 1)
    sst_MAM_std_err = sst_MAM_std / NUMPYsqrt(yearN)

    # The error 'dy' on a division 'y = x/z' is: dy = (z*dx + x*dz) / z2
    ratio_std_err = float((sst_MAM_std * sst_NDJ_std_err + sst_NDJ_std * sst_MAM_std_err)
                          / NUMPYsquare(sst_MAM_std_err))
    # Create output
    seaMetric = {'name': Name, 'value': ratioStd, 'value_error': ratio_std_err, 'units': Units, 'method': Method,
                 'nyears': yearN, 'ref': Ref}
    return seaMetric


# ---------------------------------------------------------------------------------------------------------------------#










# ---------------------------------------------------------------------------------------------------------------------#
#
# This function has the metrics collection, model name, model file names and model variable names as inputs and metric
# as output
#


dict_oneVar_modelAndObs = {'EnsoRMSE': EnsoRMSE,
                           }

dict_oneVar = {'EnsoAmpl': EnsoAmpl, 'EnsoSeasonality': EnsoSeasonality,
               }

dict_twoVar = {'EnsoAlphaLhf': EnsoAlphaLhf, 'EnsoAlphaLwr': EnsoAlphaLwr, 'EnsoAlphaSwr': EnsoAlphaSwr,
               'EnsoAlphaThf': EnsoAlphaThf,
               'EnsoMu': EnsoMu,
               }


def ComputeMetric(MetricCollection, metric, modelName, modelFile1, modelVarName1, obsName, obsFile1, obsVarName1,
                  regionVar1='', regionVar2='', modelFile2='', modelVarName2='', obsFile2='', obsVarName2=''):
    '''
    The ComputeMetric() function computes the given metric for the given model and observations

    Author:	Yann Planton : yann.planton@locean-ipsl.upmc.fr
    Co-author:

    Created on Thu Oct  5 2017

    Inputs:
    ------
    - ???		- ???

    Output:
    ------
    - ???

    Method:
    -------
    - ???

    '''
    dict_regions = defCollection(MetricCollection)['dict_of_regions'][metric]
    var_names = metricReqs(metric)['var_names']
    if not regionVar1:
        regionVar1 = dict_regions[var_names[0]]
    if not regionVar2:
        try: regionVar2 = dict_regions[var_names[2]]
        except: pass

    if metric in dict_oneVar_modelAndObs.keys():
        metric_mod_obs = dict_oneVar_modelAndObs[metric](modelFile1, modelVarName1, obsFile1, obsVarName1, region1)
        metric_val = {'name': metric_mod_obs['name'], 'metric': metric_mod_obs['value'],
                      'metric_error': metric_mod_obs['value_error'],
                      'comment': "The metric is the statistical value between the model and the observations",
                      'model': modelName, 'nyears_model': metric_mod_obs['nyears_model'],
                      'observations': obsName, 'nyears_observations': metric_mod_obs['nyears_obs'],
                      'units': metric_mod_obs['units'], 'method': metric_mod_obs['method'], 'ref': Ref}
    else:
        if metric in dict_oneVar.keys():
            metric_mod = dict_oneVar[metric](modelFile1, modelVarName1, region1)
            metric_obs = dict_oneVar[metric](obsFile1, obsVarName1, region1)
        elif metric in dict_twoVar.keys():
            metric_mod = dict_twoVar[metric](modelFile1, modelFile2, modelVarName1, modelVarName2, region1, region2)
            metric_obs = dict_twoVar[metric](obsFile1, obsFile2, obsVarName1, obsVarName2, region1, region2)
        v1, v2, err1, err2 = metric_mod['value'], metric_obs['value'], metric_mod['value_error'], metric_obs[
            'value_error']
        val1 = metric_mod['value'] / metric_obs['value']
        val1_err = (v1 * err2 + v2 * err1) / NUMPYsquare(v2)
        metric_val = {'name': metric_mod['name'], 'metric': val1, 'metric_error': val1_err,
                      'comment': "The metric is the ratio value_model / value_observations",
                      'model': modelName,
                      'nyears_model': metric['nyears_model'], 'value_model':v1, 'value_error_model':err1,
                                      'observations':obsName, 'nyears_observations':metric['nyears_obs'],
                                      'value_observations':v2, 'value_error_observations':err2,
                                      'units':metric_mod['units'], 'method':metric_mod['method'],
                                      'ref':metric_mod['ref']}
        try:
            metric_mod['nonlinearity']
        except:
            pass
        else:
            v1, v2 = metric_mod['nonlinearity'], metric_obs['nonlinearity']
            err1, err2 = metric_mod['nonlinearity_error'], metric_obs['nonlinearity_error']
            val2 = metric_mod['value'] / metric_obs['value']
            val2_err = (v1 * err2 + v2 * err1) / NUMPYsquare(v2)
            metric_val['nonlinearity_model'], metric_val['nonlinearity_error_model'] = v1, err1
            metric_val['nonlinearity_observations'], metric_val['nonlinearity_error_observations'] = v2, err2
            metric_val['metric_nonlinearity'], metric_val['metric_nonlinearity_error'] = val2, val2_err
    return metric_val

# ---------------------------------------------------------------------------------------------------------------------#