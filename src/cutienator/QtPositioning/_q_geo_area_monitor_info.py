"""
QGeoAreaMonitorInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeoareamonitorinfo.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDateTime, QDebug, QVariant
  from . import QGeoShape
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QDebug = WAIT['QDebug']
  QGeoShape = WAIT['QGeoShape']
  QVariant = WAIT['QVariant']


class QGeoAreaMonitorInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoAreaMonitorInfo: a plain Python object standing
  in front of one C++ QGeoAreaMonitorInfo.

  C++ hands a QGeoAreaMonitorInfo around as a copy, so every C++
  QGeoAreaMonitorInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoAreaMonitorInfo that has a ritual and that
  Python can call so far, 18 names in all: '__eq__', '__ne__', 'name',
  'setName', 'identifier', 'isValid', 'area', 'setArea', 'expiration',
  'setExpiration', 'isPersistent', 'setPersistent', 'notificationParameters',
  'setNotificationParameters', 'detach', 'equals', '__rlshift__',
  'debugStreaming'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoAreaMonitorInfo::QGeoAreaMonitorInfo(QGeoAreaMonitorInfo
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QGeoAreaMonitorInfo::~QGeoAreaMonitorInfo()': the destructor:
    Python removes its C++ QGeoAreaMonitorInfo by it, and has no other use
    for it.
  - Qt's 'QGeoAreaMonitorInfo &QGeoAreaMonitorInfo::operator=(const
    QGeoAreaMonitorInfo &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QGeoAreaMonitorInfo
    &QGeoAreaMonitorInfo::operator=(QGeoAreaMonitorInfo &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoAreaMonitorInfo::swap(QGeoAreaMonitorInfo &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &ds, const QGeoAreaMonitorInfo
    &monitor)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &ds, QGeoAreaMonitorInfo
    &monitor)': an operator between other classes, written inside this one.
  - Qt's 'QDataStream &QGeoAreaMonitorInfo::dataStreamOut(QDataStream &ds,
    const QGeoAreaMonitorInfo &monitor)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QDataStream &QGeoAreaMonitorInfo::dataStreamIn(QDataStream &ds,
    QGeoAreaMonitorInfo &monitor)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QGeoAreaMonitorInfo is created at the first use, not by
    'QGeoAreaMonitorInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoAreaMonitorInfo back gives a copy the ritual made
    for Python, in a new cute QGeoAreaMonitorInfo.
  - Each name of Qt's QGeoAreaMonitorInfo that has no cute function yet,
    'dataStreamIn', 'dataStreamOut', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(lhs: QGeoAreaMonitorInfo, rhs: QGeoAreaMonitorInfo) -> bool:
    """
    Calls Qt's 'bool QGeoAreaMonitorInfo::equals(const QGeoAreaMonitorInfo
    &lhs, const QGeoAreaMonitorInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#equals

    Parameters
    ----------

    lhs : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.

    rhs : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.
    """
    #  bool QGeoAreaMonitorInfo::equals(const QGeoAreaMonitorInfo &lhs, const
    #      QGeoAreaMonitorInfo &rhs)
    return Rituals.call(
        'ritual_ZN19QGeoAreaMonitorInfo6equalsERKS_S1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(QDebug, THIS)
  def debugStreaming(dbg: QDebug, monitor: QGeoAreaMonitorInfo) -> QDebug:
    """
    Calls Qt's 'QDebug QGeoAreaMonitorInfo::debugStreaming(QDebug dbg, const
    QGeoAreaMonitorInfo &monitor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#debugStreaming

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    monitor : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QGeoAreaMonitorInfo::debugStreaming(QDebug dbg, const
    #      QGeoAreaMonitorInfo &monitor)
    address = Rituals.call(
        'ritual_ZN19QGeoAreaMonitorInfo14debugStreamingE6QDebugRKS_',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(monitor),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoAreaMonitorInfo'

  #  Qt's '~QGeoAreaMonitorInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoAreaMonitorInfo behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QGeoAreaMonitorInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QGeoAreaMonitorInfo::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAreaMonitorInfo::name() const
    return self.uglySide.call('ritual_ZNK19QGeoAreaMonitorInfo4nameEv')

  def identifier(self) -> str:
    """
    Calls Qt's 'QString QGeoAreaMonitorInfo::identifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#identifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoAreaMonitorInfo::identifier() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoAreaMonitorInfo10identifierEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoAreaMonitorInfo::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#isValid
    """
    #  bool QGeoAreaMonitorInfo::isValid() const
    return self.uglySide.call('ritual_ZNK19QGeoAreaMonitorInfo7isValidEv')

  def area(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QGeoAreaMonitorInfo::area() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#area

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QGeoAreaMonitorInfo::area() const
    address = self.uglySide.call('ritual_ZNK19QGeoAreaMonitorInfo4areaEv')
    from . import QGeoShape
    return QGeoShape._cuteOwning(address)

  def expiration(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QGeoAreaMonitorInfo::expiration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#expiration

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QGeoAreaMonitorInfo::expiration() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoAreaMonitorInfo10expirationEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def isPersistent(self) -> bool:
    """
    Calls Qt's 'bool QGeoAreaMonitorInfo::isPersistent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#isPersistent
    """
    #  bool QGeoAreaMonitorInfo::isPersistent() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoAreaMonitorInfo12isPersistentEv',
    )

  def notificationParameters(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QGeoAreaMonitorInfo::notificationParameters()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#notificationParameters

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QGeoAreaMonitorInfo::notificationParameters() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoAreaMonitorInfo22notificationParametersEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorInfo::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoAreaMonitorInfo::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN19QGeoAreaMonitorInfo7setNameERK7QString', name,
    )

  @overload(QGeoShape)
  def setArea(self, newShape: QGeoShape) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorInfo::setArea(const QGeoShape
    &newShape)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#setArea

    Parameters
    ----------

    newShape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QGeoAreaMonitorInfo::setArea(const QGeoShape &newShape)
    self.uglySide.call(
        'ritual_ZN19QGeoAreaMonitorInfo7setAreaERK9QGeoShape',
        self._valueOf(newShape),
    )

  @overload(QDateTime)
  def setExpiration(self, expiry: QDateTime) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorInfo::setExpiration(const QDateTime
    &expiry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#setExpiration

    Parameters
    ----------

    expiry : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QGeoAreaMonitorInfo::setExpiration(const QDateTime &expiry)
    self.uglySide.call(
        'ritual_ZN19QGeoAreaMonitorInfo13setExpirationERK9QDateTime',
        self._valueOf(expiry),
    )

  @overload(bool)
  def setPersistent(self, isPersistent: bool) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorInfo::setPersistent(bool isPersistent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#setPersistent

    Parameters
    ----------

    isPersistent : bool
      Passed on as it is.
    """
    #  void QGeoAreaMonitorInfo::setPersistent(bool isPersistent)
    self.uglySide.call(
        'ritual_ZN19QGeoAreaMonitorInfo13setPersistentEb', isPersistent,
    )

  @overload(QMap[str, QVariant])
  def setNotificationParameters(
      self,
      parameters: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorInfo::setNotificationParameters(const
    QVariantMap &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#setNotificationParameters

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QGeoAreaMonitorInfo::setNotificationParameters(const QVariantMap
    #      &parameters)
    self.uglySide.call(
        'ritual_ZN19QGeoAreaMonitorInfo25setNotificationParametersERK4QMapI'
        '7QString8QVariantE',
        self._valueOf(parameters),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoAreaMonitorInfo) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoAreaMonitorInfo &lhs, const
    QGeoAreaMonitorInfo &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#operator==

    Parameters
    ----------

    rhs : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.
    """
    #  bool operator==(const QGeoAreaMonitorInfo &lhs, const
    #      QGeoAreaMonitorInfo &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QGeoAreaMonitorInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QGeoAreaMonitorInfo) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoAreaMonitorInfo &lhs, const
    QGeoAreaMonitorInfo &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#operator!=

    Parameters
    ----------

    rhs : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoAreaMonitorInfo &lhs, const
    #      QGeoAreaMonitorInfo &rhs)
    return Rituals.call(
        'ritual_ZneRK19QGeoAreaMonitorInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QGeoAreaMonitorInfo
    &monitor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QGeoAreaMonitorInfo &monitor)
    address = Rituals.call(
        'ritual_Zls6QDebugRK19QGeoAreaMonitorInfo',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
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
  @overload(str)
  def __init__(self, name: str = '') -> None:
    """
    Notes what was given, for Qt's
    'QGeoAreaMonitorInfo::QGeoAreaMonitorInfo(const QString &name)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#QGeoAreaMonitorInfo

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QGeoAreaMonitorInfo::QGeoAreaMonitorInfo(const QString &name)
    self._noteCreation(QGeoAreaMonitorInfo, lambda: Rituals.call(
        'ritual_ZN19QGeoAreaMonitorInfoC1ERK7QString', name,
    ))

  @overload(THIS)
  def __init__(self, other: QGeoAreaMonitorInfo) -> None:
    """
    Notes what was given, for Qt's
    'QGeoAreaMonitorInfo::QGeoAreaMonitorInfo(const QGeoAreaMonitorInfo
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#QGeoAreaMonitorInfo

    Parameters
    ----------

    other : QGeoAreaMonitorInfo
      Passed on as a value: Qt reads the C++ QGeoAreaMonitorInfo, which stays
      Python's own.
    """
    #  QGeoAreaMonitorInfo::QGeoAreaMonitorInfo(const QGeoAreaMonitorInfo
    #      &other)
    self._noteCreation(QGeoAreaMonitorInfo, lambda: Rituals.call(
        'ritual_ZN19QGeoAreaMonitorInfoC1ERKS_', self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QGeoAreaMonitorInfo::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoareamonitorinfo.html#detach
    """
    #  void QGeoAreaMonitorInfo::detach()
    self.uglySide.call('ritual_ZN19QGeoAreaMonitorInfo6detachEv')

  @staticmethod
  def dataStreamIn(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QGeoAreaMonitorInfo::dataStreamIn(QDataStream &ds,
    QGeoAreaMonitorInfo &monitor)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QGeoAreaMonitorInfo.dataStreamIn' has no cute function yet. Qt's "
        "'QDataStream &QGeoAreaMonitorInfo::dataStreamIn(QDataStream &ds, "
        "QGeoAreaMonitorInfo &monitor)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def dataStreamOut(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QGeoAreaMonitorInfo::dataStreamOut(QDataStream &ds,
    const QGeoAreaMonitorInfo &monitor)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QGeoAreaMonitorInfo.dataStreamOut' has no cute function yet. Qt's "
        "'QDataStream &QGeoAreaMonitorInfo::dataStreamOut(QDataStream &ds, "
        "const QGeoAreaMonitorInfo &monitor)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoAreaMonitorInfo::swap(QGeoAreaMonitorInfo &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoAreaMonitorInfo.swap' has no cute function yet. Qt's 'void "
        "QGeoAreaMonitorInfo::swap(QGeoAreaMonitorInfo &other)': takes a "
        "type Python has no way to hand over yet.")


#  Qt's 'QList<QGeoAreaMonitorInfo>': the list of QGeoAreaMonitorInfo, which
#  'QList[QGeoAreaMonitorInfo]' gives. It is made here, so that there is one
#  as soon as there can be a QGeoAreaMonitorInfo.
QList.createKind(
    QGeoAreaMonitorInfo, 'value',
    make='ritual_list_make_QGeoAreaMonitorInfo',
    add='ritual_list_add_QGeoAreaMonitorInfo',
    size='ritual_list_size_QGeoAreaMonitorInfo',
    at='ritual_list_at_QGeoAreaMonitorInfo',
    drop='ritual_list_drop_QGeoAreaMonitorInfo',
)
