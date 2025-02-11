'''
Please read the documentation of the Hilltop library stored within \\hilltop02.internal.###.###.### for more information.
it outlines built in python functions, such as PDist etc. that can be used to interact with the Hilltop server.

The functions within this script have been taken out of the Hilltop Scripting Guide and modified into a class for ease of use.

Example use:

    hts = r"\\Hilltop02\Data\###\###.hts"
    site = 'SQ00108'
    param = r'WQ Sample [WQ Sample]'
    start_date = "1-Jan-2010"
    end_date = "1-Jan-2020"

    import ecan_hilltop as ecan

    measurements = ecan.measurement_list(hts, site)
    sites = ecan.site_list(hts)
    data = ecan.get_data(hts, site, param, start_date, end_date)
    pdist = ecan.Pdist(hts, site, param, start_date, end_date)
    collection = ecan.get_collection(hts, param)
    #COM = ecan.get_COM(hts, site, param)
    conda create --name <env> --file requirements.txt

NOTE: This script requires an environment with numpy 1.X and you will need to create a new environment for this

'''

try:
    import sys
    sys.path.append(r"\\Hilltop02\Hilltop\x64")
    import Hilltop
    #import win32com.client #REMOVED AS COM DOESNT WORK AS EXPECTED
    #import pythoncom #REMOVED AS COM DOESNT WORK AS EXPECTED
except ImportError:
    print('Hilltop library not found')

class Ecan_Hilltop():
    def __init__(self):
        pass

    def measurement_list(self, hts, site):
        dfile = Hilltop.Connect(hts)
        measurements = Hilltop.MeasurementList(dfile, site)
        print(measurements)
        return measurements

    def site_list(self, hts):
        dfile = Hilltop.Connect(hts)
        sites = Hilltop.SiteList(dfile)
        print(sites)
        return sites

    def get_data(self, hts, site, param, start_date, end_date):
        dfile = Hilltop.Connect(hts)
        data = Hilltop.GetData(dfile, site, param, start_date, end_date)
        print(data)
        return data

    def Pdist(self, hts, site, param,  startTime, finishTime):

        '''
        The tuple that holds the results has two objects in it.
        The first object is a numpy array that holds the 99 percentiles from 1 to 99 inclusive.
        The second object is a Python dictionary that holds the extrema.
        '''

        dfile = Hilltop.Connect(hts)
        pdist = Hilltop.PDist(dfile, site, param, startTime, finishTime, method="", interval="", alignment = "",
		gapTolerance="")
        print(pdist)
        return pdist

    def get_collection(self, hts, param):
        dfile = Hilltop.Connect(hts)
        collection  = Hilltop.GetCollection(dfile, hts, param)
        print(collection)
        return collection

    #def get_COM(self, hts, site, param): #REMOVED AS COM DOESNT WORK AS EXPECTED
        dfile = win32com.client.Dispatch("Hilltop.DataFile")
        if not dfile.Open(hts):
            print (dfile.errormsg)
            exit

        wqdata = dfile.FromWQSite(site, param)
        print(wqdata.units)
        print(wqdata.DataEndTime)

        COM = wqdata.FromTimeRange(wqdata.DataEndTime, wqdata.DataEndTime)
        wqdata.getnext
        print(wqdata.value)
        return COM

