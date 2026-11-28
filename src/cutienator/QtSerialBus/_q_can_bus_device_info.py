"""
QCanBusDeviceInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcanbusdeviceinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QCanBusDeviceInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanBusDeviceInfo: a plain Python object standing in
  front of one C++ QCanBusDeviceInfo.

  C++ hands a QCanBusDeviceInfo around as a copy, so every C++
  QCanBusDeviceInfo behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanBusDeviceInfo that has a ritual and that Python
  can call so far, 8 names in all: 'plugin', 'name', 'description',
  'serialNumber', 'alias', 'channel', 'hasFlexibleDataRate', 'isVirtual'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanBusDeviceInfo::QCanBusDeviceInfo(QCanBusDeviceInfo &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCanBusDeviceInfo::~QCanBusDeviceInfo()': the destructor: Python
    removes its C++ QCanBusDeviceInfo by it, and has no other use for it.
  - Qt's 'void QCanBusDeviceInfo::swap(QCanBusDeviceInfo &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QCanBusDeviceInfo &QCanBusDeviceInfo::operator=(const
    QCanBusDeviceInfo &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCanBusDeviceInfo &QCanBusDeviceInfo::operator=(QCanBusDeviceInfo
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanBusDeviceInfo::QCanBusDeviceInfo(QCanBusDeviceInfoPrivate
    &dd)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QCanBusDeviceInfo is created at the first use, not by
    'QCanBusDeviceInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanBusDeviceInfo back gives a copy the ritual made
    for Python, in a new cute QCanBusDeviceInfo.
  - Each name of Qt's QCanBusDeviceInfo that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanBusDeviceInfo'

  #  Qt's '~QCanBusDeviceInfo()'. Naming it makes this a value class: Python
  #  owns every C++ QCanBusDeviceInfo behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QCanBusDeviceInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def plugin(self) -> str:
    """
    Calls Qt's 'QString QCanBusDeviceInfo::plugin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#plugin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanBusDeviceInfo::plugin() const
    return self.uglySide.call('ritual_ZNK17QCanBusDeviceInfo6pluginEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QCanBusDeviceInfo::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanBusDeviceInfo::name() const
    return self.uglySide.call('ritual_ZNK17QCanBusDeviceInfo4nameEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QCanBusDeviceInfo::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanBusDeviceInfo::description() const
    return self.uglySide.call('ritual_ZNK17QCanBusDeviceInfo11descriptionEv')

  def serialNumber(self) -> str:
    """
    Calls Qt's 'QString QCanBusDeviceInfo::serialNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#serialNumber

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanBusDeviceInfo::serialNumber() const
    return self.uglySide.call(
        'ritual_ZNK17QCanBusDeviceInfo12serialNumberEv',
    )

  def alias(self) -> str:
    """
    Calls Qt's 'QString QCanBusDeviceInfo::alias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#alias

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanBusDeviceInfo::alias() const
    return self.uglySide.call('ritual_ZNK17QCanBusDeviceInfo5aliasEv')

  def channel(self) -> int:
    """
    Calls Qt's 'int QCanBusDeviceInfo::channel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#channel
    """
    #  int QCanBusDeviceInfo::channel() const
    return self.uglySide.call('ritual_ZNK17QCanBusDeviceInfo7channelEv')

  def hasFlexibleDataRate(self) -> bool:
    """
    Calls Qt's 'bool QCanBusDeviceInfo::hasFlexibleDataRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#hasFlexibleDataRate
    """
    #  bool QCanBusDeviceInfo::hasFlexibleDataRate() const
    return self.uglySide.call(
        'ritual_ZNK17QCanBusDeviceInfo19hasFlexibleDataRateEv',
    )

  def isVirtual(self) -> bool:
    """
    Calls Qt's 'bool QCanBusDeviceInfo::isVirtual() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#isVirtual
    """
    #  bool QCanBusDeviceInfo::isVirtual() const
    return self.uglySide.call('ritual_ZNK17QCanBusDeviceInfo9isVirtualEv')

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

  @overload(THIS)
  def __init__(self, other: QCanBusDeviceInfo) -> None:
    """
    Notes what was given, for Qt's
    'QCanBusDeviceInfo::QCanBusDeviceInfo(const QCanBusDeviceInfo &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdeviceinfo.html#QCanBusDeviceInfo

    Parameters
    ----------

    other : QCanBusDeviceInfo
      Passed on as a value: Qt reads the C++ QCanBusDeviceInfo, which stays
      Python's own.
    """
    #  QCanBusDeviceInfo::QCanBusDeviceInfo(const QCanBusDeviceInfo &other)
    self._noteCreation(QCanBusDeviceInfo, lambda: Rituals.call(
        'ritual_ZN17QCanBusDeviceInfoC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanBusDeviceInfo::swap(QCanBusDeviceInfo &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanBusDeviceInfo.swap' has no cute function yet. Qt's 'void "
        "QCanBusDeviceInfo::swap(QCanBusDeviceInfo &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QCanBusDeviceInfo>': the list of QCanBusDeviceInfo, which
#  'QList[QCanBusDeviceInfo]' gives. It is made here, so that there is one as
#  soon as there can be a QCanBusDeviceInfo.
QList.createKind(
    QCanBusDeviceInfo, 'value',
    make='ritual_list_make_QCanBusDeviceInfo',
    add='ritual_list_add_QCanBusDeviceInfo',
    size='ritual_list_size_QCanBusDeviceInfo',
    at='ritual_list_at_QCanBusDeviceInfo',
    drop='ritual_list_drop_QCanBusDeviceInfo',
)
