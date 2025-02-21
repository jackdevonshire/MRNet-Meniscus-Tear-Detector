Quick Notes (will update after project completion):

Data stored in /data.

MRnet data available to download at: https://stanfordaimi.azurewebsites.net/datasets/bface6fc-7859-47d7-a1c8-022cd6b17419
Mrnet dataset goes under directory /mrnet and should be in same structure as downloaded zip, so:
data/mrnet/train
data/mrnet/valid
data/mrnet/train-meniscus.csv etc etc

Your own MRI scan dicom slice files go in:
data/myscan/axial/FILES_FOR_SLICES_OF_SCAN
data/myscan/coronal/FILES_FOR_SLICES_OF_SCAN
data/myscan/sagittal/FILES_FOR_SLICES_OF_SCAN
