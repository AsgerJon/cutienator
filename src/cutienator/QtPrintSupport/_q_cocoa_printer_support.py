"""
QCocoaPrinterSupport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/private/qcocoaprintersupport_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QCocoaPrinterSupport to be private: it declares the class in a
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


class QCocoaPrinterSupport(QPlatformPrinterSupport):
  """
  The cute side of Qt's QCocoaPrinterSupport: a plain Python object standing
  in front of one C++ QCocoaPrinterSupport.

  It is built on the cute 'QPlatformPrinterSupport', as Qt's
  QCocoaPrinterSupport is built on Qt's QPlatformPrinterSupport, and has
  everything that class has.

  C++ hands a QCocoaPrinterSupport around as a copy, so every C++
  QCocoaPrinterSupport behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCocoaPrinterSupport that has a ritual and that
  Python can call so far, 4 names in all: 'createNativePrintEngine',
  'createPaintEngine', 'availablePrintDeviceIds', 'defaultPrintDeviceId'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCocoaPrinterSupport::~QCocoaPrinterSupport()': the destructor:
    Python removes its C++ QCocoaPrinterSupport by it, and has no other use
    for it.
  - Qt's 'QPrintDevice QCocoaPrinterSupport::createPrintDevice(const QString
    &id)': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QCocoaPrinterSupport is created at the first use, not by
    'QCocoaPrinterSupport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCocoaPrinterSupport back gives a copy the ritual
    made for Python, in a new cute QCocoaPrinterSupport.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCocoaPrinterSupport'

  #  A C++ QCocoaPrinterSupport Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCocoaPrinterSupport'

  #  Qt's '~QCocoaPrinterSupport()'. Naming it makes this a value class:
  #  Python owns every C++ QCocoaPrinterSupport behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QCocoaPrinterSupportD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def availablePrintDeviceIds(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCocoaPrinterSupport::availablePrintDeviceIds()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcocoaprintersupport.html#availablePrintDeviceIds

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCocoaPrinterSupport::availablePrintDeviceIds() const
    address = self.uglySide.call(
        'ritual_ZNK20QCocoaPrinterSupport23availablePrintDeviceIdsEv',
    )
    return QStringList._cuteOwning(address)

  def defaultPrintDeviceId(self) -> str:
    """
    Calls Qt's 'QString QCocoaPrinterSupport::defaultPrintDeviceId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcocoaprintersupport.html#defaultPrintDeviceId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCocoaPrinterSupport::defaultPrintDeviceId() const
    ritual = 'ritual_ZNK20QCocoaPrinterSupport20defaultPrintDeviceIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QCocoaPrinterSupport20defaultPrintDeviceIdEv'
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
    'QCocoaPrinterSupport::QCocoaPrinterSupport()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcocoaprintersupport.html#QCocoaPrinterSupport
    """
    #  QCocoaPrinterSupport::QCocoaPrinterSupport()
    self._noteCreation(QCocoaPrinterSupport, lambda: Rituals.call(
        'ritual_ZN20QCocoaPrinterSupportC1Ev',
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
    *QCocoaPrinterSupport::createNativePrintEngine(QPrinter::PrinterMode
    printerMode, const QString &deviceId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcocoaprintersupport.html#createNativePrintEngine

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
    #  QPrintEngine *QCocoaPrinterSupport::createNativePrintEngine(QPrinter::
    #      PrinterMode printerMode, const QString &deviceId)
    ritual = (
        'ritual_ZN20QCocoaPrinterSupport23createNativePrintEngineEN8QPrinte'
        'r11PrinterModeERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCocoaPrinterSupport23createNativePrintEngineEN8Q'
          'Printer11PrinterModeERK7QString')
    address = self.uglySide.call(ritual, printerMode.value, deviceId)
    from . import QPrintEngine
    return QPrintEngine._cuteAt(address)

  @overload(QPrintEngine, QPrinter.PrinterMode)
  @overload(NoneType, QPrinter.PrinterMode)
  def createPaintEngine(
      self,
      a0: Optional[QPrintEngine],
      printerMode: QPrinter.PrinterMode,
  ) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine
    *QCocoaPrinterSupport::createPaintEngine(QPrintEngine *a0,
    QPrinter::PrinterMode printerMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcocoaprintersupport.html#createPaintEngine

    Parameters
    ----------

    a0 : Optional[QPrintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    printerMode : QPrinter.PrinterMode
      Passed on as its number.

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QCocoaPrinterSupport::createPaintEngine(QPrintEngine
    #      *a0, QPrinter::PrinterMode printerMode)
    ritual = (
        'ritual_ZN20QCocoaPrinterSupport17createPaintEngineEP12QPrintEngine'
        'N8QPrinter11PrinterModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCocoaPrinterSupport17createPaintEngineEP12QPrint'
          'EngineN8QPrinter11PrinterModeE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QPrintEngine'), printerMode.value,
    )
    from ..QtGui import QPaintEngine
    return QPaintEngine._cuteAt(address)
