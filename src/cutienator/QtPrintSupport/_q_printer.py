"""
QPrinter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/qprinter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtGui import QPagedPaintDevice, QPaintDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QPaintEngine
  from . import QPrintEngine, QPrinterInfo, QPrinterPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintEngine = WAIT['QPaintEngine']
  QPrintEngine = WAIT['QPrintEngine']
  QPrinterInfo = WAIT['QPrinterInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPrinter(QPagedPaintDevice):
  """
  The cute side of Qt's QPrinter: a plain Python object standing in front of
  one C++ QPrinter.

  It is built on the cute 'QPagedPaintDevice', as Qt's QPrinter is built on
  Qt's QPagedPaintDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPrinter that has a ritual and that Python can call
  so far, 52 names in all: 'd_func', 'devType', 'setOutputFormat',
  'outputFormat', 'setPdfVersion', 'pdfVersion', 'setPrinterName',
  'printerName', 'isValid', 'setOutputFileName', 'outputFileName',
  'setPrintProgram', 'printProgram', 'setDocName', 'docName', 'setCreator',
  'creator', 'setPageOrder', 'pageOrder', 'setResolution', 'resolution',
  'setColorMode', 'colorMode', 'setCollateCopies', 'collateCopies',
  'setFullPage', 'fullPage', 'setCopyCount', 'copyCount',
  'supportsMultipleCopies', 'setPaperSource', 'paperSource', 'setDuplex',
  'duplex', 'setFontEmbeddingEnabled', 'fontEmbeddingEnabled', 'paperRect',
  'pageRect', 'printerSelectionOption', 'setPrinterSelectionOption',
  'newPage', 'abort', 'printerState', 'paintEngine', 'printEngine',
  'setFromTo', 'fromPage', 'toPage', 'setPrintRange', 'printRange', 'metric',
  'setEngines'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPrinterPrivate *QPrinter::d_func() const': takes in Python
    what 'QPrinterPrivate *QPrinter::d_func()' takes.
  - Qt's 'QPrinter::~QPrinter()': the destructor: Python never removes a C++
    QPrinter.
  - Qt's 'QList<int> QPrinter::supportedResolutions() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 59 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QPrinter is created at the first use, not by 'QPrinter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPrinter.
  - Each name of Qt's QPrinter that has no cute function yet,
    'supportedResolutions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPrinter, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ColorMode(CuteNum):
    """
    The enum 'QPrinter::ColorMode' of Qt, with the 2 names Qt gives in it.
    """

    GrayScale = Kee[int](0)
    Color = Kee[int](1)

  class DuplexMode(CuteNum):
    """
    The enum 'QPrinter::DuplexMode' of Qt, with the 4 names Qt gives in it.
    """

    DuplexNone = Kee[int](0)
    DuplexAuto = Kee[int](1)
    DuplexLongSide = Kee[int](2)
    DuplexShortSide = Kee[int](3)

  class OutputFormat(CuteNum):
    """
    The enum 'QPrinter::OutputFormat' of Qt, with the 2 names Qt gives in it.
    """

    NativeFormat = Kee[int](0)
    PdfFormat = Kee[int](1)

  class PageOrder(CuteNum):
    """
    The enum 'QPrinter::PageOrder' of Qt, with the 2 names Qt gives in it.
    """

    FirstPageFirst = Kee[int](0)
    LastPageFirst = Kee[int](1)

  class PaperSource(CuteNum):
    """
    The enum 'QPrinter::PaperSource' of Qt, with the 17 names Qt gives in it.
    """

    OnlyOne = Kee[int](0)
    Lower = Kee[int](1)
    Middle = Kee[int](2)
    Manual = Kee[int](3)
    Envelope = Kee[int](4)
    EnvelopeManual = Kee[int](5)
    Auto = Kee[int](6)
    Tractor = Kee[int](7)
    SmallFormat = Kee[int](8)
    LargeFormat = Kee[int](9)
    LargeCapacity = Kee[int](10)
    Cassette = Kee[int](11)
    FormSource = Kee[int](12)
    MaxPageSource = Kee[int](13)
    CustomSource = Kee[int](14)
    LastPaperSource = Kee[int](14)
    Upper = Kee[int](0)

  class PrintRange(CuteNum):
    """
    The enum 'QPrinter::PrintRange' of Qt, with the 4 names Qt gives in it.
    """

    AllPages = Kee[int](0)
    Selection = Kee[int](1)
    PageRange = Kee[int](2)
    CurrentPage = Kee[int](3)

  class PrinterMode(CuteNum):
    """
    The enum 'QPrinter::PrinterMode' of Qt, with the 3 names Qt gives in it.
    """

    ScreenResolution = Kee[int](0)
    PrinterResolution = Kee[int](1)
    HighResolution = Kee[int](2)

  class PrinterState(CuteNum):
    """
    The enum 'QPrinter::PrinterState' of Qt, with the 4 names Qt gives in it.
    """

    Idle = Kee[int](0)
    Active = Kee[int](1)
    Aborted = Kee[int](2)
    Error = Kee[int](3)

  class Unit(CuteNum):
    """The enum 'QPrinter::Unit' of Qt, with the 7 names Qt gives in it."""

    Millimeter = Kee[int](0)
    Point = Kee[int](1)
    Inch = Kee[int](2)
    Pica = Kee[int](3)
    Didot = Kee[int](4)
    Cicero = Kee[int](5)
    DevicePixel = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPrinter'

  #  A C++ QPrinter Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPrinter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def devType(self) -> int:
    """
    Calls Qt's 'int QPrinter::devType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#devType
    """
    #  int QPrinter::devType() const
    ritual = 'ritual_ZNK8QPrinter7devTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QPrinter7devTypeEv'
    return self.uglySide.call(ritual)

  def outputFormat(self) -> OutputFormat:
    """
    Calls Qt's 'OutputFormat QPrinter::outputFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#outputFormat

    Returns
    -------

    OutputFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OutputFormat(number)'
      gives.
    """
    #  OutputFormat QPrinter::outputFormat() const
    return QPrinter.OutputFormat(self.uglySide.call(
        'ritual_ZNK8QPrinter12outputFormatEv',
    ))

  def pdfVersion(self) -> QPagedPaintDevice.PdfVersion:
    """
    Calls Qt's 'PdfVersion QPrinter::pdfVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#pdfVersion

    Returns
    -------

    QPagedPaintDevice.PdfVersion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPagedPaintDevice.PdfVersion(number)' gives.
    """
    #  PdfVersion QPrinter::pdfVersion() const
    return QPagedPaintDevice.PdfVersion(self.uglySide.call(
        'ritual_ZNK8QPrinter10pdfVersionEv',
    ))

  def printerName(self) -> str:
    """
    Calls Qt's 'QString QPrinter::printerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#printerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinter::printerName() const
    return self.uglySide.call('ritual_ZNK8QPrinter11printerNameEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPrinter::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#isValid
    """
    #  bool QPrinter::isValid() const
    return self.uglySide.call('ritual_ZNK8QPrinter7isValidEv')

  def outputFileName(self) -> str:
    """
    Calls Qt's 'QString QPrinter::outputFileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#outputFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinter::outputFileName() const
    return self.uglySide.call('ritual_ZNK8QPrinter14outputFileNameEv')

  def printProgram(self) -> str:
    """
    Calls Qt's 'QString QPrinter::printProgram() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#printProgram

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinter::printProgram() const
    return self.uglySide.call('ritual_ZNK8QPrinter12printProgramEv')

  def docName(self) -> str:
    """
    Calls Qt's 'QString QPrinter::docName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#docName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinter::docName() const
    return self.uglySide.call('ritual_ZNK8QPrinter7docNameEv')

  def creator(self) -> str:
    """
    Calls Qt's 'QString QPrinter::creator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#creator

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinter::creator() const
    return self.uglySide.call('ritual_ZNK8QPrinter7creatorEv')

  def pageOrder(self) -> PageOrder:
    """
    Calls Qt's 'PageOrder QPrinter::pageOrder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#pageOrder

    Returns
    -------

    PageOrder
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PageOrder(number)' gives.
    """
    #  PageOrder QPrinter::pageOrder() const
    return QPrinter.PageOrder(self.uglySide.call(
        'ritual_ZNK8QPrinter9pageOrderEv',
    ))

  def resolution(self) -> int:
    """
    Calls Qt's 'int QPrinter::resolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#resolution
    """
    #  int QPrinter::resolution() const
    return self.uglySide.call('ritual_ZNK8QPrinter10resolutionEv')

  def colorMode(self) -> ColorMode:
    """
    Calls Qt's 'ColorMode QPrinter::colorMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#colorMode

    Returns
    -------

    ColorMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ColorMode(number)' gives.
    """
    #  ColorMode QPrinter::colorMode() const
    return QPrinter.ColorMode(self.uglySide.call(
        'ritual_ZNK8QPrinter9colorModeEv',
    ))

  def collateCopies(self) -> bool:
    """
    Calls Qt's 'bool QPrinter::collateCopies() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#collateCopies
    """
    #  bool QPrinter::collateCopies() const
    return self.uglySide.call('ritual_ZNK8QPrinter13collateCopiesEv')

  def fullPage(self) -> bool:
    """
    Calls Qt's 'bool QPrinter::fullPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#fullPage
    """
    #  bool QPrinter::fullPage() const
    return self.uglySide.call('ritual_ZNK8QPrinter8fullPageEv')

  def copyCount(self) -> int:
    """
    Calls Qt's 'int QPrinter::copyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#copyCount
    """
    #  int QPrinter::copyCount() const
    return self.uglySide.call('ritual_ZNK8QPrinter9copyCountEv')

  def supportsMultipleCopies(self) -> bool:
    """
    Calls Qt's 'bool QPrinter::supportsMultipleCopies() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinter.html#supportsMultipleCopies
    """
    #  bool QPrinter::supportsMultipleCopies() const
    return self.uglySide.call(
        'ritual_ZNK8QPrinter22supportsMultipleCopiesEv',
    )

  def paperSource(self) -> PaperSource:
    """
    Calls Qt's 'PaperSource QPrinter::paperSource() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#paperSource

    Returns
    -------

    PaperSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PaperSource(number)'
      gives.
    """
    #  PaperSource QPrinter::paperSource() const
    return QPrinter.PaperSource(self.uglySide.call(
        'ritual_ZNK8QPrinter11paperSourceEv',
    ))

  def duplex(self) -> DuplexMode:
    """
    Calls Qt's 'DuplexMode QPrinter::duplex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#duplex

    Returns
    -------

    DuplexMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DuplexMode(number)'
      gives.
    """
    #  DuplexMode QPrinter::duplex() const
    return QPrinter.DuplexMode(self.uglySide.call(
        'ritual_ZNK8QPrinter6duplexEv',
    ))

  def fontEmbeddingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPrinter::fontEmbeddingEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#fontEmbeddingEnabled
    """
    #  bool QPrinter::fontEmbeddingEnabled() const
    return self.uglySide.call('ritual_ZNK8QPrinter20fontEmbeddingEnabledEv')

  @overload(Unit)
  def paperRect(self, a0: Unit) -> QRectF:
    """
    Calls Qt's 'QRectF QPrinter::paperRect(Unit a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#paperRect

    Parameters
    ----------

    a0 : Unit
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPrinter::paperRect(Unit a0) const
    address = self.uglySide.call(
        'ritual_ZNK8QPrinter9paperRectENS_4UnitE', a0.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Unit)
  def pageRect(self, a0: Unit) -> QRectF:
    """
    Calls Qt's 'QRectF QPrinter::pageRect(Unit a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#pageRect

    Parameters
    ----------

    a0 : Unit
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPrinter::pageRect(Unit a0) const
    address = self.uglySide.call(
        'ritual_ZNK8QPrinter8pageRectENS_4UnitE', a0.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def printerSelectionOption(self) -> str:
    """
    Calls Qt's 'QString QPrinter::printerSelectionOption() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinter.html#printerSelectionOption

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinter::printerSelectionOption() const
    return self.uglySide.call(
        'ritual_ZNK8QPrinter22printerSelectionOptionEv',
    )

  def printerState(self) -> PrinterState:
    """
    Calls Qt's 'PrinterState QPrinter::printerState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#printerState

    Returns
    -------

    PrinterState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PrinterState(number)'
      gives.
    """
    #  PrinterState QPrinter::printerState() const
    return QPrinter.PrinterState(self.uglySide.call(
        'ritual_ZNK8QPrinter12printerStateEv',
    ))

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPrinter::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPrinter::paintEngine() const
    ritual = 'ritual_ZNK8QPrinter11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QPrinter11paintEngineEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPaintEngine
    return QPaintEngine._cuteAt(address)

  def printEngine(self) -> Optional[QPrintEngine]:
    """
    Calls Qt's 'QPrintEngine *QPrinter::printEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#printEngine

    Returns
    -------

    Optional[QPrintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrintEngine *QPrinter::printEngine() const
    address = self.uglySide.call('ritual_ZNK8QPrinter11printEngineEv')
    from . import QPrintEngine
    return QPrintEngine._cuteAt(address)

  def fromPage(self) -> int:
    """
    Calls Qt's 'int QPrinter::fromPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#fromPage
    """
    #  int QPrinter::fromPage() const
    return self.uglySide.call('ritual_ZNK8QPrinter8fromPageEv')

  def toPage(self) -> int:
    """
    Calls Qt's 'int QPrinter::toPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#toPage
    """
    #  int QPrinter::toPage() const
    return self.uglySide.call('ritual_ZNK8QPrinter6toPageEv')

  def printRange(self) -> PrintRange:
    """
    Calls Qt's 'PrintRange QPrinter::printRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#printRange

    Returns
    -------

    PrintRange
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PrintRange(number)'
      gives.
    """
    #  PrintRange QPrinter::printRange() const
    return QPrinter.PrintRange(self.uglySide.call(
        'ritual_ZNK8QPrinter10printRangeEv',
    ))

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, a0: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QPrinter::metric(PaintDeviceMetric a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#metric

    Parameters
    ----------

    a0 : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QPrinter::metric(PaintDeviceMetric a0) const
    ritual = 'ritual_ZNK8QPrinter6metricEN12QPaintDevice17PaintDeviceMetricE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QPrinter6metricEN12QPaintDevice17PaintDeviceMetri'
          'cE')
    return self.uglySide.call(ritual, a0.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(OutputFormat)
  def setOutputFormat(self, format: OutputFormat) -> None:
    """
    Calls Qt's 'void QPrinter::setOutputFormat(OutputFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setOutputFormat

    Parameters
    ----------

    format : OutputFormat
      Passed on as its number.
    """
    #  void QPrinter::setOutputFormat(OutputFormat format)
    self.uglySide.call(
        'ritual_ZN8QPrinter15setOutputFormatENS_12OutputFormatE',
        format.value,
    )

  @overload(QPagedPaintDevice.PdfVersion)
  def setPdfVersion(self, version: QPagedPaintDevice.PdfVersion) -> None:
    """
    Calls Qt's 'void QPrinter::setPdfVersion(PdfVersion version)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setPdfVersion

    Parameters
    ----------

    version : QPagedPaintDevice.PdfVersion
      Passed on as its number.
    """
    #  void QPrinter::setPdfVersion(PdfVersion version)
    self.uglySide.call(
        'ritual_ZN8QPrinter13setPdfVersionEN17QPagedPaintDevice10PdfVersion'
        'E',
        version.value,
    )

  @overload(str)
  def setPrinterName(self, a0: str) -> None:
    """
    Calls Qt's 'void QPrinter::setPrinterName(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setPrinterName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPrinter::setPrinterName(const QString &a0)
    self.uglySide.call('ritual_ZN8QPrinter14setPrinterNameERK7QString', a0)

  @overload(str)
  def setOutputFileName(self, a0: str) -> None:
    """
    Calls Qt's 'void QPrinter::setOutputFileName(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setOutputFileName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPrinter::setOutputFileName(const QString &a0)
    self.uglySide.call(
        'ritual_ZN8QPrinter17setOutputFileNameERK7QString', a0,
    )

  @overload(str)
  def setPrintProgram(self, a0: str) -> None:
    """
    Calls Qt's 'void QPrinter::setPrintProgram(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setPrintProgram

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPrinter::setPrintProgram(const QString &a0)
    self.uglySide.call('ritual_ZN8QPrinter15setPrintProgramERK7QString', a0)

  @overload(str)
  def setDocName(self, a0: str) -> None:
    """
    Calls Qt's 'void QPrinter::setDocName(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setDocName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPrinter::setDocName(const QString &a0)
    self.uglySide.call('ritual_ZN8QPrinter10setDocNameERK7QString', a0)

  @overload(str)
  def setCreator(self, a0: str) -> None:
    """
    Calls Qt's 'void QPrinter::setCreator(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setCreator

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPrinter::setCreator(const QString &a0)
    self.uglySide.call('ritual_ZN8QPrinter10setCreatorERK7QString', a0)

  @overload(PageOrder)
  def setPageOrder(self, a0: PageOrder) -> None:
    """
    Calls Qt's 'void QPrinter::setPageOrder(PageOrder a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setPageOrder

    Parameters
    ----------

    a0 : PageOrder
      Passed on as its number.
    """
    #  void QPrinter::setPageOrder(PageOrder a0)
    self.uglySide.call(
        'ritual_ZN8QPrinter12setPageOrderENS_9PageOrderE', a0.value,
    )

  @overload(int)
  def setResolution(self, a0: int) -> None:
    """
    Calls Qt's 'void QPrinter::setResolution(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setResolution

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QPrinter::setResolution(int a0)
    self.uglySide.call('ritual_ZN8QPrinter13setResolutionEi', a0)

  @overload(ColorMode)
  def setColorMode(self, a0: ColorMode) -> None:
    """
    Calls Qt's 'void QPrinter::setColorMode(ColorMode a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setColorMode

    Parameters
    ----------

    a0 : ColorMode
      Passed on as its number.
    """
    #  void QPrinter::setColorMode(ColorMode a0)
    self.uglySide.call(
        'ritual_ZN8QPrinter12setColorModeENS_9ColorModeE', a0.value,
    )

  @overload(bool)
  def setCollateCopies(self, collate: bool) -> None:
    """
    Calls Qt's 'void QPrinter::setCollateCopies(bool collate)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setCollateCopies

    Parameters
    ----------

    collate : bool
      Passed on as it is.
    """
    #  void QPrinter::setCollateCopies(bool collate)
    self.uglySide.call('ritual_ZN8QPrinter16setCollateCopiesEb', collate)

  @overload(bool)
  def setFullPage(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPrinter::setFullPage(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setFullPage

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPrinter::setFullPage(bool a0)
    self.uglySide.call('ritual_ZN8QPrinter11setFullPageEb', a0)

  @overload(int)
  def setCopyCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QPrinter::setCopyCount(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setCopyCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QPrinter::setCopyCount(int a0)
    self.uglySide.call('ritual_ZN8QPrinter12setCopyCountEi', a0)

  @overload(PaperSource)
  def setPaperSource(self, a0: PaperSource) -> None:
    """
    Calls Qt's 'void QPrinter::setPaperSource(PaperSource a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setPaperSource

    Parameters
    ----------

    a0 : PaperSource
      Passed on as its number.
    """
    #  void QPrinter::setPaperSource(PaperSource a0)
    self.uglySide.call(
        'ritual_ZN8QPrinter14setPaperSourceENS_11PaperSourceE', a0.value,
    )

  @overload(DuplexMode)
  def setDuplex(self, duplex: DuplexMode) -> None:
    """
    Calls Qt's 'void QPrinter::setDuplex(DuplexMode duplex)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setDuplex

    Parameters
    ----------

    duplex : DuplexMode
      Passed on as its number.
    """
    #  void QPrinter::setDuplex(DuplexMode duplex)
    self.uglySide.call(
        'ritual_ZN8QPrinter9setDuplexENS_10DuplexModeE', duplex.value,
    )

  @overload(bool)
  def setFontEmbeddingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QPrinter::setFontEmbeddingEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinter.html#setFontEmbeddingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QPrinter::setFontEmbeddingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN8QPrinter23setFontEmbeddingEnabledEb', enable,
    )

  @overload(str)
  def setPrinterSelectionOption(self, a0: str) -> None:
    """
    Calls Qt's 'void QPrinter::setPrinterSelectionOption(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinter.html#setPrinterSelectionOption

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPrinter::setPrinterSelectionOption(const QString &a0)
    self.uglySide.call(
        'ritual_ZN8QPrinter25setPrinterSelectionOptionERK7QString', a0,
    )

  @overload(int, int)
  def setFromTo(self, fromPage: int, toPage: int) -> None:
    """
    Calls Qt's 'void QPrinter::setFromTo(int fromPage, int toPage)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setFromTo

    Parameters
    ----------

    fromPage : int
      Passed on as it is.

    toPage : int
      Passed on as it is.
    """
    #  void QPrinter::setFromTo(int fromPage, int toPage)
    self.uglySide.call('ritual_ZN8QPrinter9setFromToEii', fromPage, toPage)

  @overload(PrintRange)
  def setPrintRange(self, range: PrintRange) -> None:
    """
    Calls Qt's 'void QPrinter::setPrintRange(PrintRange range)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setPrintRange

    Parameters
    ----------

    range : PrintRange
      Passed on as its number.
    """
    #  void QPrinter::setPrintRange(PrintRange range)
    self.uglySide.call(
        'ritual_ZN8QPrinter13setPrintRangeENS_10PrintRangeE', range.value,
    )

  @overload(QPrintEngine, QPaintEngine)
  @overload(QPrintEngine, NoneType)
  @overload(NoneType, QPaintEngine)
  @overload(NoneType, NoneType)
  def setEngines(
      self,
      printEngine: Optional[QPrintEngine],
      paintEngine: Optional[QPaintEngine],
  ) -> None:
    """
    Calls Qt's 'void QPrinter::setEngines(QPrintEngine *printEngine,
    QPaintEngine *paintEngine)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#setEngines

    Parameters
    ----------

    printEngine : Optional[QPrintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    paintEngine : Optional[QPaintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPrinter::setEngines(QPrintEngine *printEngine, QPaintEngine
    #      *paintEngine)
    self.uglySide.call(
        'ritual_ZN8QPrinter10setEnginesEP12QPrintEngineP12QPaintEngine',
        self._addressOf(printEngine, 'QPrintEngine'),
        self._addressOf(paintEngine),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(PrinterMode)
  def __init__(
      self,
      mode: PrinterMode = PrinterMode.ScreenResolution,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPrinter::QPrinter(PrinterMode mode)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#QPrinter

    Parameters
    ----------

    mode : PrinterMode
      Passed on as its number. May be left out, as in Qt: it is then
      PrinterMode.ScreenResolution.
    """
    #  QPrinter::QPrinter(PrinterMode mode)
    self._noteCreation(QPrinter, lambda: Rituals.call(
        'ritual_ZN8QPrinterC1ENS_11PrinterModeE', mode.value,
    ))

  @overload(QPrinterInfo)
  @overload(QPrinterInfo, PrinterMode)
  def __init__(
      self,
      printer: QPrinterInfo,
      mode: PrinterMode = PrinterMode.ScreenResolution,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPrinter::QPrinter(const QPrinterInfo
    &printer, PrinterMode mode)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#QPrinter

    Parameters
    ----------

    printer : QPrinterInfo
      Passed on as a value: Qt reads the C++ QPrinterInfo, which stays
      Python's own.

    mode : PrinterMode
      Passed on as its number. May be left out, as in Qt: it is then
      PrinterMode.ScreenResolution.
    """
    #  QPrinter::QPrinter(const QPrinterInfo &printer, PrinterMode mode)
    self._noteCreation(QPrinter, lambda: Rituals.call(
        'ritual_ZN8QPrinterC1ERK12QPrinterInfoNS_11PrinterModeE',
        self._valueOf(printer), mode.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_func(self) -> Optional[QPrinterPrivate]:
    """
    Calls Qt's 'QPrinterPrivate *QPrinter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#d_func

    Returns
    -------

    Optional[QPrinterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrinterPrivate *QPrinter::d_func()
    address = self.uglySide.call('ritual_ZN8QPrinter6d_funcEv')
    from . import QPrinterPrivate
    return QPrinterPrivate._cuteAt(address)

  def newPage(self) -> bool:
    """
    Calls Qt's 'bool QPrinter::newPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#newPage
    """
    #  bool QPrinter::newPage()
    ritual = 'ritual_ZN8QPrinter7newPageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QPrinter7newPageEv'
    return self.uglySide.call(ritual)

  def abort(self) -> bool:
    """
    Calls Qt's 'bool QPrinter::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qprinter.html#abort
    """
    #  bool QPrinter::abort()
    return self.uglySide.call('ritual_ZN8QPrinter5abortEv')

  @staticmethod
  def supportedResolutions(*__, **_) -> Never:
    """
    Qt's 'QList<int> QPrinter::supportedResolutions() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPrinter.supportedResolutions' has no cute function yet. Qt's "
        "'QList<int> QPrinter::supportedResolutions() const': gives a type "
        "Python has no way to take yet.")
