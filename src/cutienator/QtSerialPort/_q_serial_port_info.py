"""
QSerialPortInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialPort/qserialportinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QSerialPortInfoPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSerialPortInfoPrivate = WAIT['QSerialPortInfoPrivate']


class QSerialPortInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSerialPortInfo: a plain Python object standing in
  front of one C++ QSerialPortInfo.

  C++ hands a QSerialPortInfo around as a copy, so every C++ QSerialPortInfo
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSerialPortInfo that has a ritual and that Python
  can call so far, 12 names in all: 'd_func', 'portName', 'systemLocation',
  'description', 'manufacturer', 'serialNumber', 'vendorIdentifier',
  'productIdentifier', 'hasVendorIdentifier', 'hasProductIdentifier',
  'isNull', 'availablePorts'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSerialPortInfoPrivate *QSerialPortInfo::d_func() const':
    takes in Python what 'QSerialPortInfoPrivate *QSerialPortInfo::d_func()'
    takes.
  - Qt's 'QSerialPortInfo::QSerialPortInfo(const QSerialPort &port)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QSerialPortInfo::~QSerialPortInfo()': the destructor: Python
    removes its C++ QSerialPortInfo by it, and has no other use for it.
  - Qt's 'QSerialPortInfo &QSerialPortInfo::operator=(const QSerialPortInfo
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QSerialPortInfo::swap(QSerialPortInfo &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QList<qint32> QSerialPortInfo::standardBaudRates()': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QSerialPortInfo is created at the first use, not by
    'QSerialPortInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSerialPortInfo back gives a copy the ritual made for
    Python, in a new cute QSerialPortInfo.
  - Each name of Qt's QSerialPortInfo that has no cute function yet,
    'standardBaudRates', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def availablePorts() -> QList[QSerialPortInfo]:
    """
    Calls Qt's 'QList<QSerialPortInfo> QSerialPortInfo::availablePorts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#availablePorts

    Returns
    -------

    QList[QSerialPortInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSerialPortInfo> QSerialPortInfo::availablePorts()
    address = Rituals.call('ritual_ZN15QSerialPortInfo14availablePortsEv')
    return QList[QSerialPortInfo]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSerialPortInfo'

  #  Qt's '~QSerialPortInfo()'. Naming it makes this a value class: Python
  #  owns every C++ QSerialPortInfo behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSerialPortInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def portName(self) -> str:
    """
    Calls Qt's 'QString QSerialPortInfo::portName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialportinfo.html#portName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSerialPortInfo::portName() const
    return self.uglySide.call('ritual_ZNK15QSerialPortInfo8portNameEv')

  def systemLocation(self) -> str:
    """
    Calls Qt's 'QString QSerialPortInfo::systemLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#systemLocation

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSerialPortInfo::systemLocation() const
    return self.uglySide.call(
        'ritual_ZNK15QSerialPortInfo14systemLocationEv',
    )

  def description(self) -> str:
    """
    Calls Qt's 'QString QSerialPortInfo::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialportinfo.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSerialPortInfo::description() const
    return self.uglySide.call('ritual_ZNK15QSerialPortInfo11descriptionEv')

  def manufacturer(self) -> str:
    """
    Calls Qt's 'QString QSerialPortInfo::manufacturer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialportinfo.html#manufacturer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSerialPortInfo::manufacturer() const
    return self.uglySide.call('ritual_ZNK15QSerialPortInfo12manufacturerEv')

  def serialNumber(self) -> str:
    """
    Calls Qt's 'QString QSerialPortInfo::serialNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialportinfo.html#serialNumber

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSerialPortInfo::serialNumber() const
    return self.uglySide.call('ritual_ZNK15QSerialPortInfo12serialNumberEv')

  def vendorIdentifier(self) -> int:
    """
    Calls Qt's 'quint16 QSerialPortInfo::vendorIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#vendorIdentifier
    """
    #  quint16 QSerialPortInfo::vendorIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK15QSerialPortInfo16vendorIdentifierEv',
    )

  def productIdentifier(self) -> int:
    """
    Calls Qt's 'quint16 QSerialPortInfo::productIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#productIdentifier
    """
    #  quint16 QSerialPortInfo::productIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK15QSerialPortInfo17productIdentifierEv',
    )

  def hasVendorIdentifier(self) -> bool:
    """
    Calls Qt's 'bool QSerialPortInfo::hasVendorIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#hasVendorIdentifier
    """
    #  bool QSerialPortInfo::hasVendorIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK15QSerialPortInfo19hasVendorIdentifierEv',
    )

  def hasProductIdentifier(self) -> bool:
    """
    Calls Qt's 'bool QSerialPortInfo::hasProductIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#hasProductIdentifier
    """
    #  bool QSerialPortInfo::hasProductIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK15QSerialPortInfo20hasProductIdentifierEv',
    )

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSerialPortInfo::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qserialportinfo.html#isNull
    """
    #  bool QSerialPortInfo::isNull() const
    return self.uglySide.call('ritual_ZNK15QSerialPortInfo6isNullEv')

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
    Notes what was given, for Qt's 'QSerialPortInfo::QSerialPortInfo()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#QSerialPortInfo
    """
    #  QSerialPortInfo::QSerialPortInfo()
    self._noteCreation(QSerialPortInfo, lambda: Rituals.call(
        'ritual_ZN15QSerialPortInfoC1Ev',
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QSerialPortInfo::QSerialPortInfo(const
    QString &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#QSerialPortInfo

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSerialPortInfo::QSerialPortInfo(const QString &name)
    self._noteCreation(QSerialPortInfo, lambda: Rituals.call(
        'ritual_ZN15QSerialPortInfoC1ERK7QString', name,
    ))

  @overload(THIS)
  def __init__(self, other: QSerialPortInfo) -> None:
    """
    Notes what was given, for Qt's 'QSerialPortInfo::QSerialPortInfo(const
    QSerialPortInfo &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#QSerialPortInfo

    Parameters
    ----------

    other : QSerialPortInfo
      Passed on as a value: Qt reads the C++ QSerialPortInfo, which stays
      Python's own.
    """
    #  QSerialPortInfo::QSerialPortInfo(const QSerialPortInfo &other)
    self._noteCreation(QSerialPortInfo, lambda: Rituals.call(
        'ritual_ZN15QSerialPortInfoC1ERKS_', self._valueOf(other),
    ))

  @overload(QSerialPortInfoPrivate)
  def __init__(self, dd: QSerialPortInfoPrivate) -> None:
    """
    Notes what was given, for Qt's 'QSerialPortInfo::QSerialPortInfo(const
    QSerialPortInfoPrivate &dd)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialportinfo.html#QSerialPortInfo

    Parameters
    ----------

    dd : QSerialPortInfoPrivate
      Passed on as a value: Qt reads the C++ QSerialPortInfoPrivate, which
      stays Python's own.
    """
    #  QSerialPortInfo::QSerialPortInfo(const QSerialPortInfoPrivate &dd)
    self._noteCreation(QSerialPortInfo, lambda: Rituals.call(
        'ritual_ZN15QSerialPortInfoC1ERK22QSerialPortInfoPrivate',
        self._valueOf(dd),
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

  def d_func(self) -> Optional[QSerialPortInfoPrivate]:
    """
    Calls Qt's 'QSerialPortInfoPrivate *QSerialPortInfo::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qserialportinfo.html#d_func

    Returns
    -------

    Optional[QSerialPortInfoPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSerialPortInfoPrivate *QSerialPortInfo::d_func()
    address = self.uglySide.call('ritual_ZN15QSerialPortInfo6d_funcEv')
    from . import QSerialPortInfoPrivate
    return QSerialPortInfoPrivate._cuteAt(address)

  @staticmethod
  def standardBaudRates(*__, **_) -> Never:
    """
    Qt's 'QList<qint32> QSerialPortInfo::standardBaudRates()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSerialPortInfo.standardBaudRates' has no cute function yet. Qt's "
        "'QList<qint32> QSerialPortInfo::standardBaudRates()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSerialPortInfo::swap(QSerialPortInfo &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSerialPortInfo.swap' has no cute function yet. Qt's 'void "
        "QSerialPortInfo::swap(QSerialPortInfo &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QSerialPortInfo>': the list of QSerialPortInfo, which
#  'QList[QSerialPortInfo]' gives. It is made here, so that there is one as
#  soon as there can be a QSerialPortInfo.
QList.createKind(
    QSerialPortInfo, 'value',
    make='ritual_list_make_QSerialPortInfo',
    add='ritual_list_add_QSerialPortInfo',
    size='ritual_list_size_QSerialPortInfo',
    at='ritual_list_at_QSerialPortInfo',
    drop='ritual_list_drop_QSerialPortInfo',
)
