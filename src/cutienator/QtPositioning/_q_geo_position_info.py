"""
QGeoPositionInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeopositioninfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDateTime, QDebug
  from . import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QDebug = WAIT['QDebug']
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoPositionInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoPositionInfo: a plain Python object standing in
  front of one C++ QGeoPositionInfo.

  C++ hands a QGeoPositionInfo around as a copy, so every C++
  QGeoPositionInfo behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoPositionInfo that has a ritual and that Python
  can call so far, 15 names in all: '__eq__', '__ne__', 'isValid',
  'setTimestamp', 'timestamp', 'setCoordinate', 'coordinate', 'setAttribute',
  'attribute', 'removeAttribute', 'hasAttribute', 'detach', 'equals',
  '__rlshift__', 'debugStreaming'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoPositionInfo::QGeoPositionInfo(QGeoPositionInfo &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QGeoPositionInfo::QGeoPositionInfo(QGeoPositionInfoPrivate &dd)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QGeoPositionInfo::~QGeoPositionInfo()': the destructor: Python
    removes its C++ QGeoPositionInfo by it, and has no other use for it.
  - Qt's 'QGeoPositionInfo &QGeoPositionInfo::operator=(const
    QGeoPositionInfo &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QGeoPositionInfo &QGeoPositionInfo::operator=(QGeoPositionInfo
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoPositionInfo::swap(QGeoPositionInfo &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const QGeoPositionInfo
    &info)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QGeoPositionInfo
    &info)': an operator between other classes, written inside this one.
  - Qt's 'QDataStream &QGeoPositionInfo::dataStreamOut(QDataStream &stream,
    const QGeoPositionInfo &info)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QDataStream &QGeoPositionInfo::dataStreamIn(QDataStream &stream,
    QGeoPositionInfo &info)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QDataStream &operator<<(QDataStream &stream,
    QGeoPositionInfo::Attribute attr)': an operator between other classes,
    written inside this one.
  - Qt's 'QDataStream &operator>>(QDataStream &stream,
    QGeoPositionInfo::Attribute &attr)': an operator between other classes,
    written inside this one.
  - Qt's 'QDataStream &QGeoPositionInfo::dataStreamOut(QDataStream &stream,
    QGeoPositionInfo::Attribute attr)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QDataStream &QGeoPositionInfo::dataStreamIn(QDataStream &stream,
    QGeoPositionInfo::Attribute &attr)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QGeoPositionInfo is created at the first use, not by
    'QGeoPositionInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoPositionInfo back gives a copy the ritual made
    for Python, in a new cute QGeoPositionInfo.
  - Each name of Qt's QGeoPositionInfo that has no cute function yet,
    'dataStreamIn', 'dataStreamOut', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGeoPositionInfo, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Attribute(CuteNum):
    """
    The enum 'QGeoPositionInfo::Attribute' of Qt, with the 7 names Qt gives
    in it.
    """

    Direction = Kee[int](0)
    GroundSpeed = Kee[int](1)
    VerticalSpeed = Kee[int](2)
    MagneticVariation = Kee[int](3)
    HorizontalAccuracy = Kee[int](4)
    VerticalAccuracy = Kee[int](5)
    DirectionAccuracy = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(lhs: QGeoPositionInfo, rhs: QGeoPositionInfo) -> bool:
    """
    Calls Qt's 'bool QGeoPositionInfo::equals(const QGeoPositionInfo &lhs,
    const QGeoPositionInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#equals

    Parameters
    ----------

    lhs : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.

    rhs : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  bool QGeoPositionInfo::equals(const QGeoPositionInfo &lhs, const
    #      QGeoPositionInfo &rhs)
    return Rituals.call(
        'ritual_ZN16QGeoPositionInfo6equalsERKS_S1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(QDebug, THIS)
  def debugStreaming(dbg: QDebug, info: QGeoPositionInfo) -> QDebug:
    """
    Calls Qt's 'QDebug QGeoPositionInfo::debugStreaming(QDebug dbg, const
    QGeoPositionInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfo.html#debugStreaming

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    info : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QGeoPositionInfo::debugStreaming(QDebug dbg, const
    #      QGeoPositionInfo &info)
    address = Rituals.call(
        'ritual_ZN16QGeoPositionInfo14debugStreamingE6QDebugRKS_',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(info),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoPositionInfo'

  #  Qt's '~QGeoPositionInfo()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoPositionInfo behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QGeoPositionInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoPositionInfo::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#isValid
    """
    #  bool QGeoPositionInfo::isValid() const
    return self.uglySide.call('ritual_ZNK16QGeoPositionInfo7isValidEv')

  def timestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QGeoPositionInfo::timestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#timestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QGeoPositionInfo::timestamp() const
    address = self.uglySide.call('ritual_ZNK16QGeoPositionInfo9timestampEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def coordinate(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoPositionInfo::coordinate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#coordinate

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoPositionInfo::coordinate() const
    address = self.uglySide.call(
        'ritual_ZNK16QGeoPositionInfo10coordinateEv',
    )
    from . import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(Attribute)
  def attribute(self, attribute: Attribute) -> float:
    """
    Calls Qt's 'qreal QGeoPositionInfo::attribute(Attribute attribute)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#attribute

    Parameters
    ----------

    attribute : Attribute
      Passed on as its number.
    """
    #  qreal QGeoPositionInfo::attribute(Attribute attribute) const
    return self.uglySide.call(
        'ritual_ZNK16QGeoPositionInfo9attributeENS_9AttributeE',
        attribute.value,
    )

  @overload(Attribute)
  def hasAttribute(self, attribute: Attribute) -> bool:
    """
    Calls Qt's 'bool QGeoPositionInfo::hasAttribute(Attribute attribute)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#hasAttribute

    Parameters
    ----------

    attribute : Attribute
      Passed on as its number.
    """
    #  bool QGeoPositionInfo::hasAttribute(Attribute attribute) const
    return self.uglySide.call(
        'ritual_ZNK16QGeoPositionInfo12hasAttributeENS_9AttributeE',
        attribute.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setTimestamp(self, timestamp: QDateTime) -> None:
    """
    Calls Qt's 'void QGeoPositionInfo::setTimestamp(const QDateTime
    &timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#setTimestamp

    Parameters
    ----------

    timestamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QGeoPositionInfo::setTimestamp(const QDateTime &timestamp)
    self.uglySide.call(
        'ritual_ZN16QGeoPositionInfo12setTimestampERK9QDateTime',
        self._valueOf(timestamp),
    )

  @overload(QGeoCoordinate)
  def setCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoPositionInfo::setCoordinate(const QGeoCoordinate
    &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfo.html#setCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoPositionInfo::setCoordinate(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN16QGeoPositionInfo13setCoordinateERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(Attribute, float)
  def setAttribute(self, attribute: Attribute, value: float) -> None:
    """
    Calls Qt's 'void QGeoPositionInfo::setAttribute(Attribute attribute,
    qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#setAttribute

    Parameters
    ----------

    attribute : Attribute
      Passed on as its number.

    value : float
      Passed on as it is.
    """
    #  void QGeoPositionInfo::setAttribute(Attribute attribute, qreal value)
    self.uglySide.call(
        'ritual_ZN16QGeoPositionInfo12setAttributeENS_9AttributeEd',
        attribute.value, value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoPositionInfo) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoPositionInfo &lhs, const
    QGeoPositionInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#operator==

    Parameters
    ----------

    rhs : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  bool operator==(const QGeoPositionInfo &lhs, const QGeoPositionInfo
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QGeoPositionInfoS1_',
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
  def __ne__(self, rhs: QGeoPositionInfo) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoPositionInfo &lhs, const
    QGeoPositionInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#operator!=

    Parameters
    ----------

    rhs : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoPositionInfo &lhs, const QGeoPositionInfo
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QGeoPositionInfoS1_',
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
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QGeoPositionInfo &info)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#operator<<

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
    #  QDebug operator<<(QDebug dbg, const QGeoPositionInfo &info)
    address = Rituals.call(
        'ritual_Zls6QDebugRK16QGeoPositionInfo',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGeoPositionInfo::QGeoPositionInfo()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfo.html#QGeoPositionInfo
    """
    #  QGeoPositionInfo::QGeoPositionInfo()
    self._noteCreation(QGeoPositionInfo, lambda: Rituals.call(
        'ritual_ZN16QGeoPositionInfoC1Ev',
    ))

  @overload(QGeoCoordinate, QDateTime)
  def __init__(
      self,
      coordinate: QGeoCoordinate,
      updateTime: QDateTime,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoPositionInfo::QGeoPositionInfo(const
    QGeoCoordinate &coordinate, const QDateTime &updateTime)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfo.html#QGeoPositionInfo

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    updateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  QGeoPositionInfo::QGeoPositionInfo(const QGeoCoordinate &coordinate,
    #      const QDateTime &updateTime)
    self._noteCreation(QGeoPositionInfo, lambda: Rituals.call(
        'ritual_ZN16QGeoPositionInfoC1ERK14QGeoCoordinateRK9QDateTime',
        self._valueOf(coordinate), self._valueOf(updateTime),
    ))

  @overload(THIS)
  def __init__(self, other: QGeoPositionInfo) -> None:
    """
    Notes what was given, for Qt's 'QGeoPositionInfo::QGeoPositionInfo(const
    QGeoPositionInfo &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfo.html#QGeoPositionInfo

    Parameters
    ----------

    other : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  QGeoPositionInfo::QGeoPositionInfo(const QGeoPositionInfo &other)
    self._noteCreation(QGeoPositionInfo, lambda: Rituals.call(
        'ritual_ZN16QGeoPositionInfoC1ERKS_', self._valueOf(other),
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

  @overload(Attribute)
  def removeAttribute(self, attribute: Attribute) -> None:
    """
    Calls Qt's 'void QGeoPositionInfo::removeAttribute(Attribute attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeopositioninfo.html#removeAttribute

    Parameters
    ----------

    attribute : Attribute
      Passed on as its number.
    """
    #  void QGeoPositionInfo::removeAttribute(Attribute attribute)
    self.uglySide.call(
        'ritual_ZN16QGeoPositionInfo15removeAttributeENS_9AttributeE',
        attribute.value,
    )

  def detach(self) -> None:
    """
    Calls Qt's 'void QGeoPositionInfo::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeopositioninfo.html#detach
    """
    #  void QGeoPositionInfo::detach()
    self.uglySide.call('ritual_ZN16QGeoPositionInfo6detachEv')

  @staticmethod
  def dataStreamIn(*__, **_) -> Never:
    """
    - Qt's 'QDataStream &QGeoPositionInfo::dataStreamIn(QDataStream &stream,
      QGeoPositionInfo &info)': takes a type Python has no way to hand over
      yet.
    - Qt's 'QDataStream &QGeoPositionInfo::dataStreamIn(QDataStream &stream,
      QGeoPositionInfo::Attribute &attr)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QGeoPositionInfo.dataStreamIn' has no cute function yet. Qt's "
        "'QDataStream &QGeoPositionInfo::dataStreamIn(QDataStream &stream, "
        "QGeoPositionInfo &info)': takes a type Python has no way to hand "
        "over yet. Qt's 'QDataStream "
        "&QGeoPositionInfo::dataStreamIn(QDataStream &stream, "
        "QGeoPositionInfo::Attribute &attr)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def dataStreamOut(*__, **_) -> Never:
    """
    - Qt's 'QDataStream &QGeoPositionInfo::dataStreamOut(QDataStream &stream,
      const QGeoPositionInfo &info)': takes a type Python has no way to hand
      over yet.
    - Qt's 'QDataStream &QGeoPositionInfo::dataStreamOut(QDataStream &stream,
      QGeoPositionInfo::Attribute attr)': takes a type Python has no way to
      hand over yet.
    """
    raise NotImplementedError(
        "'QGeoPositionInfo.dataStreamOut' has no cute function yet. Qt's "
        "'QDataStream &QGeoPositionInfo::dataStreamOut(QDataStream &stream, "
        "const QGeoPositionInfo &info)': takes a type Python has no way to "
        "hand over yet. Qt's 'QDataStream "
        "&QGeoPositionInfo::dataStreamOut(QDataStream &stream, "
        "QGeoPositionInfo::Attribute attr)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoPositionInfo::swap(QGeoPositionInfo &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoPositionInfo.swap' has no cute function yet. Qt's 'void "
        "QGeoPositionInfo::swap(QGeoPositionInfo &other)': takes a type "
        "Python has no way to hand over yet.")
