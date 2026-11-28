"""
QPrintEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/qprintengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtGui import QPaintDevice
from . import QPrinter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QPrintEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPrintEngine: a plain Python object standing in front
  of one C++ QPrintEngine.

  What exists
  -----------

  Every function of Qt's QPrintEngine that has a ritual and that Python can
  call so far, 6 names in all: 'setProperty', 'property', 'newPage', 'abort',
  'metric', 'printerState'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPrintEngine::~QPrintEngine()': the destructor: Python never
    removes a C++ QPrintEngine.

  What to expect
  --------------

  - The C++ QPrintEngine is created at the first use, not by
    'QPrintEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPrintEngine.
  """

  #  The enums Qt writes inside QPrintEngine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PrintEnginePropertyKey(CuteNum):
    """
    The enum 'QPrintEngine::PrintEnginePropertyKey' of Qt, with the 32 names
    Qt gives in it.
    """

    PPK_CollateCopies = Kee[int](0)
    PPK_ColorMode = Kee[int](1)
    PPK_Creator = Kee[int](2)
    PPK_DocumentName = Kee[int](3)
    PPK_FullPage = Kee[int](4)
    PPK_NumberOfCopies = Kee[int](5)
    PPK_Orientation = Kee[int](6)
    PPK_OutputFileName = Kee[int](7)
    PPK_PageOrder = Kee[int](8)
    PPK_PageRect = Kee[int](9)
    PPK_PageSize = Kee[int](10)
    PPK_PaperRect = Kee[int](11)
    PPK_PaperSource = Kee[int](12)
    PPK_PrinterName = Kee[int](13)
    PPK_PrinterProgram = Kee[int](14)
    PPK_Resolution = Kee[int](15)
    PPK_SelectionOption = Kee[int](16)
    PPK_SupportedResolutions = Kee[int](17)
    PPK_WindowsPageSize = Kee[int](18)
    PPK_FontEmbedding = Kee[int](19)
    PPK_Duplex = Kee[int](20)
    PPK_PaperSources = Kee[int](21)
    PPK_CustomPaperSize = Kee[int](22)
    PPK_PageMargins = Kee[int](23)
    PPK_CopyCount = Kee[int](24)
    PPK_SupportsMultipleCopies = Kee[int](25)
    PPK_PaperName = Kee[int](26)
    PPK_QPageSize = Kee[int](27)
    PPK_QPageMargins = Kee[int](28)
    PPK_QPageLayout = Kee[int](29)
    PPK_PaperSize = Kee[int](10)
    PPK_CustomBase = Kee[int](65280)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPrintEngine'

  #  A C++ QPrintEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPrintEngine'

  #  The functions Qt calls itself that QPrintEngine is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setProperty': (
          ('_ZN12QPrintEngine11setPropertyENS_22PrintEnginePropertyKeyERK8Q'
           'Variant',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtPrintSupport:QPrintEngine.PrintEnginePropertyKey'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'property': (
          ('_ZNK12QPrintEngine8propertyENS_22PrintEnginePropertyKeyE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum',
                'QtPrintSupport:QPrintEngine.PrintEnginePropertyKey'),
           )),
      ),
      'newPage': (
          ('_ZN12QPrintEngine7newPageEv',
           ('bool', 'number', ''),
           ()),
      ),
      'abort': (
          ('_ZN12QPrintEngine5abortEv',
           ('bool', 'number', ''),
           ()),
      ),
      'metric': (
          ('_ZNK12QPrintEngine6metricEN12QPaintDevice17PaintDeviceMetricE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPaintDevice.PaintDeviceMetric'),
           )),
      ),
      'printerState': (
          ('_ZNK12QPrintEngine12printerStateEv',
           ('int', 'enum', 'QtPrintSupport:QPrinter.PrinterState'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PrintEnginePropertyKey)
  def property(self, key: PrintEnginePropertyKey) -> QVariant:
    """
    Calls Qt's 'QVariant QPrintEngine::property(PrintEnginePropertyKey key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintengine.html#property

    Parameters
    ----------

    key : PrintEnginePropertyKey
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPrintEngine::property(PrintEnginePropertyKey key) const
    address = self._callAs(
        'QPrintEngine',
        'ritual_ZNK12QPrintEngine8propertyENS_22PrintEnginePropertyKeyE',
        key.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, a0: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QPrintEngine::metric(QPaintDevice::PaintDeviceMetric a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintengine.html#metric

    Parameters
    ----------

    a0 : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QPrintEngine::metric(QPaintDevice::PaintDeviceMetric a0) const
    return self._callAs(
        'QPrintEngine',
        'ritual_ZNK12QPrintEngine6metricEN12QPaintDevice17PaintDeviceMetric'
        'E',
        a0.value,
    )

  def printerState(self) -> QPrinter.PrinterState:
    """
    Calls Qt's 'QPrinter::PrinterState QPrintEngine::printerState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintengine.html#printerState

    Returns
    -------

    QPrinter.PrinterState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPrinter.PrinterState(number)' gives.
    """
    #  QPrinter::PrinterState QPrintEngine::printerState() const
    return QPrinter.PrinterState(self._callAs(
        'QPrintEngine', 'ritual_ZNK12QPrintEngine12printerStateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PrintEnginePropertyKey, QVariant)
  def setProperty(
      self,
      key: PrintEnginePropertyKey,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QPrintEngine::setProperty(PrintEnginePropertyKey key,
    const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintengine.html#setProperty

    Parameters
    ----------

    key : PrintEnginePropertyKey
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPrintEngine::setProperty(PrintEnginePropertyKey key, const
    #      QVariant &value)
    self._callAs(
        'QPrintEngine',
        'ritual_ZN12QPrintEngine11setPropertyENS_22PrintEnginePropertyKeyER'
        'K8QVariant',
        key.value, self._valueOf(value),
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

  def newPage(self) -> bool:
    """
    Calls Qt's 'bool QPrintEngine::newPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qprintengine.html#newPage
    """
    #  bool QPrintEngine::newPage()
    return self._callAs('QPrintEngine', 'ritual_ZN12QPrintEngine7newPageEv')

  def abort(self) -> bool:
    """
    Calls Qt's 'bool QPrintEngine::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qprintengine.html#abort
    """
    #  bool QPrintEngine::abort()
    return self._callAs('QPrintEngine', 'ritual_ZN12QPrintEngine5abortEv')
