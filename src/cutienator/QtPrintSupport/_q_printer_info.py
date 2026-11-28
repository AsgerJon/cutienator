"""
QPrinterInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/qprinterinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QPrinter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
  from ..QtGui import QPageSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QPrinterInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPrinterInfo: a plain Python object standing in front
  of one C++ QPrinterInfo.

  C++ hands a QPrinterInfo around as a copy, so every C++ QPrinterInfo behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPrinterInfo that has a ritual and that Python can
  call so far, 21 names in all: 'printerName', 'description', 'location',
  'makeAndModel', 'isNull', 'isDefault', 'isRemote', 'state',
  'supportedPageSizes', 'defaultPageSize', 'supportsCustomPageSizes',
  'minimumPhysicalPageSize', 'maximumPhysicalPageSize', 'defaultDuplexMode',
  'defaultColorMode', 'availablePrinterNames', 'availablePrinters',
  'defaultPrinterName', 'defaultPrinter', 'printerInfo', '__rlshift__'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPrinterInfo::QPrinterInfo(const QPrinter &printer)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QPrinterInfo::~QPrinterInfo()': the destructor: Python removes its
    C++ QPrinterInfo by it, and has no other use for it.
  - Qt's 'QPrinterInfo &QPrinterInfo::operator=(const QPrinterInfo &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QList<int> QPrinterInfo::supportedResolutions() const': gives a
    type Python has no way to take yet.
  - Qt's 'QList<QPrinter::DuplexMode> QPrinterInfo::supportedDuplexModes()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<QPrinter::ColorMode> QPrinterInfo::supportedColorModes()
    const': gives a type Python has no way to take yet.
  - Qt's 'QPrinterInfoPrivate *QPrinterInfo::d_func()': gives
    'QPrinterInfoPrivate', which has no cute class yet.
  - Qt's 'const QPrinterInfoPrivate *QPrinterInfo::d_func() const': gives
    'QPrinterInfoPrivate', which has no cute class yet.

  What to expect
  --------------

  - The C++ QPrinterInfo is created at the first use, not by
    'QPrinterInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPrinterInfo back gives a copy the ritual made for
    Python, in a new cute QPrinterInfo.
  - Each name of Qt's QPrinterInfo that has no cute function yet, 'd_func',
    'supportedColorModes', 'supportedDuplexModes', 'supportedResolutions',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def availablePrinterNames() -> QStringList:
    """
    Calls Qt's 'QStringList QPrinterInfo::availablePrinterNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterinfo.html#availablePrinterNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPrinterInfo::availablePrinterNames()
    address = Rituals.call(
        'ritual_ZN12QPrinterInfo21availablePrinterNamesEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def availablePrinters() -> QList[QPrinterInfo]:
    """
    Calls Qt's 'QList<QPrinterInfo> QPrinterInfo::availablePrinters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterinfo.html#availablePrinters

    Returns
    -------

    QList[QPrinterInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPrinterInfo> QPrinterInfo::availablePrinters()
    address = Rituals.call('ritual_ZN12QPrinterInfo17availablePrintersEv')
    return QList[QPrinterInfo]._cuteOwning(address)

  @staticmethod
  def defaultPrinterName() -> str:
    """
    Calls Qt's 'QString QPrinterInfo::defaultPrinterName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterinfo.html#defaultPrinterName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinterInfo::defaultPrinterName()
    return Rituals.call('ritual_ZN12QPrinterInfo18defaultPrinterNameEv')

  @staticmethod
  def defaultPrinter() -> QPrinterInfo:
    """
    Calls Qt's 'QPrinterInfo QPrinterInfo::defaultPrinter()'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#defaultPrinter

    Returns
    -------

    QPrinterInfo
      A new cute QPrinterInfo around the copy Qt gave back. Python owns it.
    """
    #  QPrinterInfo QPrinterInfo::defaultPrinter()
    address = Rituals.call('ritual_ZN12QPrinterInfo14defaultPrinterEv')
    return QPrinterInfo._cuteOwning(address)

  @staticmethod
  @overload(str)
  def printerInfo(printerName: str) -> QPrinterInfo:
    """
    Calls Qt's 'QPrinterInfo QPrinterInfo::printerInfo(const QString
    &printerName)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#printerInfo

    Parameters
    ----------

    printerName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPrinterInfo
      A new cute QPrinterInfo around the copy Qt gave back. Python owns it.
    """
    #  QPrinterInfo QPrinterInfo::printerInfo(const QString &printerName)
    address = Rituals.call(
        'ritual_ZN12QPrinterInfo11printerInfoERK7QString', printerName,
    )
    return QPrinterInfo._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPrinterInfo'

  #  Qt's '~QPrinterInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QPrinterInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QPrinterInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def printerName(self) -> str:
    """
    Calls Qt's 'QString QPrinterInfo::printerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#printerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinterInfo::printerName() const
    return self.uglySide.call('ritual_ZNK12QPrinterInfo11printerNameEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QPrinterInfo::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinterInfo::description() const
    return self.uglySide.call('ritual_ZNK12QPrinterInfo11descriptionEv')

  def location(self) -> str:
    """
    Calls Qt's 'QString QPrinterInfo::location() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#location

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinterInfo::location() const
    return self.uglySide.call('ritual_ZNK12QPrinterInfo8locationEv')

  def makeAndModel(self) -> str:
    """
    Calls Qt's 'QString QPrinterInfo::makeAndModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#makeAndModel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPrinterInfo::makeAndModel() const
    return self.uglySide.call('ritual_ZNK12QPrinterInfo12makeAndModelEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QPrinterInfo::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#isNull
    """
    #  bool QPrinterInfo::isNull() const
    return self.uglySide.call('ritual_ZNK12QPrinterInfo6isNullEv')

  def isDefault(self) -> bool:
    """
    Calls Qt's 'bool QPrinterInfo::isDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#isDefault
    """
    #  bool QPrinterInfo::isDefault() const
    return self.uglySide.call('ritual_ZNK12QPrinterInfo9isDefaultEv')

  def isRemote(self) -> bool:
    """
    Calls Qt's 'bool QPrinterInfo::isRemote() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#isRemote
    """
    #  bool QPrinterInfo::isRemote() const
    return self.uglySide.call('ritual_ZNK12QPrinterInfo8isRemoteEv')

  def state(self) -> QPrinter.PrinterState:
    """
    Calls Qt's 'QPrinter::PrinterState QPrinterInfo::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#state

    Returns
    -------

    QPrinter.PrinterState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPrinter.PrinterState(number)' gives.
    """
    #  QPrinter::PrinterState QPrinterInfo::state() const
    return QPrinter.PrinterState(self.uglySide.call(
        'ritual_ZNK12QPrinterInfo5stateEv',
    ))

  def supportedPageSizes(self) -> QList[QPageSize]:
    """
    Calls Qt's 'QList<QPageSize> QPrinterInfo::supportedPageSizes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterinfo.html#supportedPageSizes

    Returns
    -------

    QList[QPageSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPageSize> QPrinterInfo::supportedPageSizes() const
    address = self.uglySide.call(
        'ritual_ZNK12QPrinterInfo18supportedPageSizesEv',
    )
    from ..QtGui import QPageSize
    return QList[QPageSize]._cuteOwning(address)

  def defaultPageSize(self) -> QPageSize:
    """
    Calls Qt's 'QPageSize QPrinterInfo::defaultPageSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#defaultPageSize

    Returns
    -------

    QPageSize
      A new cute QPageSize around the copy Qt gave back. Python owns it.
    """
    #  QPageSize QPrinterInfo::defaultPageSize() const
    address = self.uglySide.call(
        'ritual_ZNK12QPrinterInfo15defaultPageSizeEv',
    )
    from ..QtGui import QPageSize
    return QPageSize._cuteOwning(address)

  def supportsCustomPageSizes(self) -> bool:
    """
    Calls Qt's 'bool QPrinterInfo::supportsCustomPageSizes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterinfo.html#supportsCustomPageSizes
    """
    #  bool QPrinterInfo::supportsCustomPageSizes() const
    return self.uglySide.call(
        'ritual_ZNK12QPrinterInfo23supportsCustomPageSizesEv',
    )

  def minimumPhysicalPageSize(self) -> QPageSize:
    """
    Calls Qt's 'QPageSize QPrinterInfo::minimumPhysicalPageSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterinfo.html#minimumPhysicalPageSize

    Returns
    -------

    QPageSize
      A new cute QPageSize around the copy Qt gave back. Python owns it.
    """
    #  QPageSize QPrinterInfo::minimumPhysicalPageSize() const
    address = self.uglySide.call(
        'ritual_ZNK12QPrinterInfo23minimumPhysicalPageSizeEv',
    )
    from ..QtGui import QPageSize
    return QPageSize._cuteOwning(address)

  def maximumPhysicalPageSize(self) -> QPageSize:
    """
    Calls Qt's 'QPageSize QPrinterInfo::maximumPhysicalPageSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterinfo.html#maximumPhysicalPageSize

    Returns
    -------

    QPageSize
      A new cute QPageSize around the copy Qt gave back. Python owns it.
    """
    #  QPageSize QPrinterInfo::maximumPhysicalPageSize() const
    address = self.uglySide.call(
        'ritual_ZNK12QPrinterInfo23maximumPhysicalPageSizeEv',
    )
    from ..QtGui import QPageSize
    return QPageSize._cuteOwning(address)

  def defaultDuplexMode(self) -> QPrinter.DuplexMode:
    """
    Calls Qt's 'QPrinter::DuplexMode QPrinterInfo::defaultDuplexMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprinterinfo.html#defaultDuplexMode

    Returns
    -------

    QPrinter.DuplexMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPrinter.DuplexMode(number)' gives.
    """
    #  QPrinter::DuplexMode QPrinterInfo::defaultDuplexMode() const
    return QPrinter.DuplexMode(self.uglySide.call(
        'ritual_ZNK12QPrinterInfo17defaultDuplexModeEv',
    ))

  def defaultColorMode(self) -> QPrinter.ColorMode:
    """
    Calls Qt's 'QPrinter::ColorMode QPrinterInfo::defaultColorMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#defaultColorMode

    Returns
    -------

    QPrinter.ColorMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPrinter.ColorMode(number)' gives.
    """
    #  QPrinter::ColorMode QPrinterInfo::defaultColorMode() const
    return QPrinter.ColorMode(self.uglySide.call(
        'ritual_ZNK12QPrinterInfo16defaultColorModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QPrinterInfo &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QPrinterInfo &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK12QPrinterInfo',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPrinterInfo::QPrinterInfo()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#QPrinterInfo
    """
    #  QPrinterInfo::QPrinterInfo()
    self._noteCreation(QPrinterInfo, lambda: Rituals.call(
        'ritual_ZN12QPrinterInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPrinterInfo) -> None:
    """
    Notes what was given, for Qt's 'QPrinterInfo::QPrinterInfo(const
    QPrinterInfo &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#QPrinterInfo

    Parameters
    ----------

    other : QPrinterInfo
      Passed on as a value: Qt reads the C++ QPrinterInfo, which stays
      Python's own.
    """
    #  QPrinterInfo::QPrinterInfo(const QPrinterInfo &other)
    self._noteCreation(QPrinterInfo, lambda: Rituals.call(
        'ritual_ZN12QPrinterInfoC1ERKS_', self._valueOf(other),
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QPrinterInfo::QPrinterInfo(const QString
    &name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprinterinfo.html#QPrinterInfo

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QPrinterInfo::QPrinterInfo(const QString &name)
    self._noteCreation(QPrinterInfo, lambda: Rituals.call(
        'ritual_ZN12QPrinterInfoC1ERK7QString', name,
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

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QPrinterInfoPrivate *QPrinterInfo::d_func()': gives
      'QPrinterInfoPrivate', which has no cute class yet.
    - Qt's 'const QPrinterInfoPrivate *QPrinterInfo::d_func() const': gives
      'QPrinterInfoPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPrinterInfo.d_func' has no cute function yet. Qt's "
        "'QPrinterInfoPrivate *QPrinterInfo::d_func()': gives "
        "'QPrinterInfoPrivate', which has no cute class yet. Qt's 'const "
        "QPrinterInfoPrivate *QPrinterInfo::d_func() const': gives "
        "'QPrinterInfoPrivate', which has no cute class yet.")

  @staticmethod
  def supportedColorModes(*__, **_) -> Never:
    """
    Qt's 'QList<QPrinter::ColorMode> QPrinterInfo::supportedColorModes()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPrinterInfo.supportedColorModes' has no cute function yet. Qt's "
        "'QList<QPrinter::ColorMode> QPrinterInfo::supportedColorModes() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def supportedDuplexModes(*__, **_) -> Never:
    """
    Qt's 'QList<QPrinter::DuplexMode> QPrinterInfo::supportedDuplexModes()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPrinterInfo.supportedDuplexModes' has no cute function yet. Qt's "
        "'QList<QPrinter::DuplexMode> QPrinterInfo::supportedDuplexModes() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def supportedResolutions(*__, **_) -> Never:
    """
    Qt's 'QList<int> QPrinterInfo::supportedResolutions() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPrinterInfo.supportedResolutions' has no cute function yet. Qt's "
        "'QList<int> QPrinterInfo::supportedResolutions() const': gives a "
        "type Python has no way to take yet.")


#  Qt's 'QList<QPrinterInfo>': the list of QPrinterInfo, which
#  'QList[QPrinterInfo]' gives. It is made here, so that there is one as soon
#  as there can be a QPrinterInfo.
QList.createKind(
    QPrinterInfo, 'value',
    make='ritual_list_make_QPrinterInfo',
    add='ritual_list_add_QPrinterInfo',
    size='ritual_list_size_QPrinterInfo',
    at='ritual_list_at_QPrinterInfo',
    drop='ritual_list_drop_QPrinterInfo',
)
