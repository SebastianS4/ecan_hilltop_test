# ecan_hilltop_test
WIP Hilltop connection based on hilltop documentation 

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

NOTE: This script requires an environment with numpy 1.X and you will need to create a new environment for this
