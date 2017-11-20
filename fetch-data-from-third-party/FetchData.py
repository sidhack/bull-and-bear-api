from nsepy import get_history
from  datetime import date

from nsepy.commons import StrDate
import talib
from utils.AlgorithmHelper import MFI

v=get_history(symbol="SBIN", start=date(2017,1,1), end=date(2017,11,19))
print(MFI(v,14))
talib.MFI()