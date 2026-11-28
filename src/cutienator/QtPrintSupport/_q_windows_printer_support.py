"""
QWindowsPrinterSupport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/private/qwindowsprintersupport_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWindowsPrinterSupport to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QPlatformPrinterSupport, QPrinter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QPaintEngine
  from . import QPrintEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrintEngine = WAIT['QPrintEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowsPrinterSupport(QPlatformPrinterSupport):
  """
  The cute side of Qt's QWindowsPrinterSupport: a plain Python object
  standing in front of one C++ QWindowsPrinterSupport.

  It is built on the cute 'QPlatformPrinterSupport', as Qt's
  QWindowsPrinterSupport is built on Qt's QPlatformPrinterSupport, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowsPrinterSupport that has a ritual and that
  Python can call so far, 4 names in all: 'createNativePrintEngine',
  'createPaintEngine', 'availablePrintDeviceIds', 'defaultPrintDeviceId'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWindowsPrinterSupport::~QWindowsPrinterSupport()': the destructor:
    Python never removes a C++ QWindowsPrinterSupport.
  - Qt's 'QPrintDevice QWindowsPrinterSupport::createPrintDevice(const
    QString &id)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QWindowsPrinterSupport is created at the first use, not by
    'QWindowsPrinterSupport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowsPrinterSupport.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowsPrinterSupport'

  #  A C++ QWindowsPrinterSupport Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowsPrinterSupport'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def availablePrintDeviceIds(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWindowsPrinterSupport::availablePrintDeviceIds()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsprintersupport.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWindowsPrinterSupport::availablePrintDeviceIds() const
    address = self.uglySide.call(
        'ritual_ZNK22QWindowsPrinterSupport23availablePrintDeviceIdsEv',
    )
    return QStringList._cuteOwning(address)

  def defaultPrintDeviceId(self) -> str:
    """
    Calls Qt's 'QString QWindowsPrinterSupport::defaultPrintDeviceId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsprintersupport.html#defaultPrintDeviceId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWindowsPrinterSupport::defaultPrintDeviceId() const
    ritual = 'ritual_ZNK22QWindowsPrinterSupport20defaultPrintDeviceIdEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QWindowsPrinterSupport20defaultPrintDeviceIdEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWindowsPrinterSupport::QWindowsPrinterSupport()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsprintersupport.html#QWindowsPrinterSupport
    """
    #  QWindowsPrinterSupport::QWindowsPrinterSupport()
    self._noteCreation(QWindowsPrinterSupport, lambda: Rituals.call(
        'ritual_ZN22QWindowsPrinterSupportC1Ev',
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

  @overload(QPrinter.PrinterMode)
  @overload(QPrinter.PrinterMode, str)
  def createNativePrintEngine(
      self,
      printerMode: QPrinter.PrinterMode,
      deviceId: str = '',
  ) -> Optional[QPrintEngine]:
    """
    Calls Qt's 'QPrintEngine
    *QWindowsPrinterSupport::createNativePrintEngine(QPrinter::PrinterMode
    printerMode, const QString &deviceId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsprintersupport.html

    Parameters
    ----------

    printerMode : QPrinter.PrinterMode
      Passed on as its number.

    deviceId : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QPrintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrintEngine
    #      *QWindowsPrinterSupport::createNativePrintEngine(QPrinter::
    #      PrinterMode printerMode, const QString &deviceId)
    ritual = (
        'ritual_ZN22QWindowsPrinterSupport23createNativePrintEngineEN8QPrin'
        'ter11PrinterModeERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QWindowsPrinterSupport23createNativePrintEngineEN'
          '8QPrinter11PrinterModeERK7QString')
    address = self.uglySide.call(ritual, printerMode.value, deviceId)
    from . import QPrintEngine
    return QPrintEngine._cuteAt(address)

  @overload(QPrintEngine, QPrinter.PrinterMode)
  @overload(NoneType, QPrinter.PrinterMode)
  def createPaintEngine(
      self,
      printEngine: Optional[QPrintEngine],
      a1: QPrinter.PrinterMode,
  ) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine
    *QWindowsPrinterSupport::createPaintEngine(QPrintEngine *printEngine,
    QPrinter::PrinterMode a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowsprintersupport.html#createPaintEngine

    Parameters
    ----------

    printEngine : Optional[QPrintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QPrinter.PrinterMode
      Passed on as its number.

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QWindowsPrinterSupport::createPaintEngine(QPrintEngine
    #      *printEngine, QPrinter::PrinterMode a1)
    ritual = (
        'ritual_ZN22QWindowsPrinterSupport17createPaintEngineEP12QPrintEngi'
        'neN8QPrinter11PrinterModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QWindowsPrinterSupport17createPaintEngineEP12QPri'
          'ntEngineN8QPrinter11PrinterModeE')
    address = self.uglySide.call(
        ritual, self._addressOf(printEngine, 'QPrintEngine'), a1.value,
    )
    from ..QtGui import QPaintEngine
    return QPaintEngine._cuteAt(address)
