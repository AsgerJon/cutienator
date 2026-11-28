"""
QGeoSatelliteInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeosatelliteinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QGeoSatelliteInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoSatelliteInfo: a plain Python object standing in
  front of one C++ QGeoSatelliteInfo.

  C++ hands a QGeoSatelliteInfo around as a copy, so every C++
  QGeoSatelliteInfo behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoSatelliteInfo that has a ritual and that Python
  can call so far, 16 names in all: '__eq__', '__ne__', 'setSatelliteSystem',
  'satelliteSystem', 'setSatelliteIdentifier', 'satelliteIdentifier',
  'setSignalStrength', 'signalStrength', 'setAttribute', 'attribute',
  'removeAttribute', 'hasAttribute', 'detach', 'equals', '__rlshift__',
  'debugStreaming'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoSatelliteInfo::QGeoSatelliteInfo(QGeoSatelliteInfoPrivate
    &dd)': takes a type Python has no way to hand over yet.
  - Qt's 'QGeoSatelliteInfo::QGeoSatelliteInfo(QGeoSatelliteInfo &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QGeoSatelliteInfo::~QGeoSatelliteInfo()': the destructor: Python
    removes its C++ QGeoSatelliteInfo by it, and has no other use for it.
  - Qt's 'QGeoSatelliteInfo &QGeoSatelliteInfo::operator=(const
    QGeoSatelliteInfo &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QGeoSatelliteInfo &QGeoSatelliteInfo::operator=(QGeoSatelliteInfo
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoSatelliteInfo::swap(QGeoSatelliteInfo &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const
    QGeoSatelliteInfo &info)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QGeoSatelliteInfo
    &info)': an operator between other classes, written inside this one.
  - Qt's 'QDataStream &QGeoSatelliteInfo::dataStreamOut(QDataStream &stream,
    const QGeoSatelliteInfo &info)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QDataStream &QGeoSatelliteInfo::dataStreamIn(QDataStream &stream,
    QGeoSatelliteInfo &info)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  3 of the 31 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoSatelliteInfo is created at the first use, not by
    'QGeoSatelliteInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoSatelliteInfo back gives a copy the ritual made
    for Python, in a new cute QGeoSatelliteInfo.
  - Each name of Qt's QGeoSatelliteInfo that has no cute function yet,
    'dataStreamIn', 'dataStreamOut', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGeoSatelliteInfo, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Attribute(CuteNum):
    """
    The enum 'QGeoSatelliteInfo::Attribute' of Qt, with the 2 names Qt gives
    in it.
    """

    Elevation = Kee[int](0)
    Azimuth = Kee[int](1)

  class SatelliteSystem(CuteNum):
    """
    The enum 'QGeoSatelliteInfo::SatelliteSystem' of Qt, with the 10 names Qt
    gives in it.
    """

    Undefined = Kee[int](0)
    GPS = Kee[int](1)
    GLONASS = Kee[int](2)
    GALILEO = Kee[int](3)
    BEIDOU = Kee[int](4)
    QZSS = Kee[int](5)
    IRNSS = Kee[int](6)
    SBAS = Kee[int](7)
    Multiple = Kee[int](255)
    CustomType = Kee[int](256)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(lhs: QGeoSatelliteInfo, rhs: QGeoSatelliteInfo) -> bool:
    """
    Calls Qt's 'bool QGeoSatelliteInfo::equals(const QGeoSatelliteInfo &lhs,
    const QGeoSatelliteInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfo.html#equals

    Parameters
    ----------

    lhs : QGeoSatelliteInfo
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfo, which stays
      Python's own.

    rhs : QGeoSatelliteInfo
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfo, which stays
      Python's own.
    """
    #  bool QGeoSatelliteInfo::equals(const QGeoSatelliteInfo &lhs, const
    #      QGeoSatelliteInfo &rhs)
    return Rituals.call(
        'ritual_ZN17QGeoSatelliteInfo6equalsERKS_S1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(QDebug, THIS)
  def debugStreaming(dbg: QDebug, info: QGeoSatelliteInfo) -> QDebug:
    """
    Calls Qt's 'QDebug QGeoSatelliteInfo::debugStreaming(QDebug dbg, const
    QGeoSatelliteInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#debugStreaming

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    info : QGeoSatelliteInfo
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfo, which stays
      Python's own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QGeoSatelliteInfo::debugStreaming(QDebug dbg, const
    #      QGeoSatelliteInfo &info)
    address = Rituals.call(
        'ritual_ZN17QGeoSatelliteInfo14debugStreamingE6QDebugRKS_',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(info),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoSatelliteInfo'

  #  Qt's '~QGeoSatelliteInfo()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoSatelliteInfo behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QGeoSatelliteInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def satelliteSystem(self) -> SatelliteSystem:
    """
    Calls Qt's 'SatelliteSystem QGeoSatelliteInfo::satelliteSystem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#satelliteSystem

    Returns
    -------

    SatelliteSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SatelliteSystem(number)'
      gives.
    """
    #  SatelliteSystem QGeoSatelliteInfo::satelliteSystem() const
    return QGeoSatelliteInfo.SatelliteSystem(self.uglySide.call(
        'ritual_ZNK17QGeoSatelliteInfo15satelliteSystemEv',
    ))

  def satelliteIdentifier(self) -> int:
    """
    Calls Qt's 'int QGeoSatelliteInfo::satelliteIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#satelliteIdentifier
    """
    #  int QGeoSatelliteInfo::satelliteIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK17QGeoSatelliteInfo19satelliteIdentifierEv',
    )

  def signalStrength(self) -> int:
    """
    Calls Qt's 'int QGeoSatelliteInfo::signalStrength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#signalStrength
    """
    #  int QGeoSatelliteInfo::signalStrength() const
    return self.uglySide.call(
        'ritual_ZNK17QGeoSatelliteInfo14signalStrengthEv',
    )

  @overload(Attribute)
  def attribute(self, attribute: Attribute) -> float:
    """
    Calls Qt's 'qreal QGeoSatelliteInfo::attribute(Attribute attribute)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfo.html#attribute

    Parameters
    ----------

    attribute : Attribute
      Passed on as its number.
    """
    #  qreal QGeoSatelliteInfo::attribute(Attribute attribute) const
    return self.uglySide.call(
        'ritual_ZNK17QGeoSatelliteInfo9attributeENS_9AttributeE',
        attribute.value,
    )

  @overload(Attribute)
  def hasAttribute(self, attribute: Attribute) -> bool:
    """
    Calls Qt's 'bool QGeoSatelliteInfo::hasAttribute(Attribute attribute)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#hasAttribute

    Parameters
    ----------

    attribute : Attribute
      Passed on as its number.
    """
    #  bool QGeoSatelliteInfo::hasAttribute(Attribute attribute) const
    return self.uglySide.call(
        'ritual_ZNK17QGeoSatelliteInfo12hasAttributeENS_9AttributeE',
        attribute.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(SatelliteSystem)
  def setSatelliteSystem(self, system: SatelliteSystem) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfo::setSatelliteSystem(SatelliteSystem
    system)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#setSatelliteSystem

    Parameters
    ----------

    system : SatelliteSystem
      Passed on as its number.
    """
    #  void QGeoSatelliteInfo::setSatelliteSystem(SatelliteSystem system)
    self.uglySide.call(
        'ritual_ZN17QGeoSatelliteInfo18setSatelliteSystemENS_15SatelliteSys'
        'temE',
        system.value,
    )

  @overload(int)
  def setSatelliteIdentifier(self, satId: int) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfo::setSatelliteIdentifier(int satId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#setSatelliteIdentifier

    Parameters
    ----------

    satId : int
      Passed on as it is.
    """
    #  void QGeoSatelliteInfo::setSatelliteIdentifier(int satId)
    self.uglySide.call(
        'ritual_ZN17QGeoSatelliteInfo22setSatelliteIdentifierEi', satId,
    )

  @overload(int)
  def setSignalStrength(self, signalStrength: int) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfo::setSignalStrength(int
    signalStrength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#setSignalStrength

    Parameters
    ----------

    signalStrength : int
      Passed on as it is.
    """
    #  void QGeoSatelliteInfo::setSignalStrength(int signalStrength)
    self.uglySide.call(
        'ritual_ZN17QGeoSatelliteInfo17setSignalStrengthEi', signalStrength,
    )

  @overload(Attribute, float)
  def setAttribute(self, attribute: Attribute, value: float) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfo::setAttribute(Attribute attribute,
    qreal value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#setAttribute

    Parameters
    ----------

    attribute : Attribute
      Passed on as its number.

    value : float
      Passed on as it is.
    """
    #  void QGeoSatelliteInfo::setAttribute(Attribute attribute, qreal value)
    self.uglySide.call(
        'ritual_ZN17QGeoSatelliteInfo12setAttributeENS_9AttributeEd',
        attribute.value, value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoSatelliteInfo) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoSatelliteInfo &lhs, const
    QGeoSatelliteInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfo.html#operator==

    Parameters
    ----------

    rhs : QGeoSatelliteInfo
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfo, which stays
      Python's own.
    """
    #  bool operator==(const QGeoSatelliteInfo &lhs, const QGeoSatelliteInfo
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK17QGeoSatelliteInfoS1_',
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
  def __ne__(self, rhs: QGeoSatelliteInfo) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoSatelliteInfo &lhs, const
    QGeoSatelliteInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfo.html#operator!=

    Parameters
    ----------

    rhs : QGeoSatelliteInfo
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfo, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoSatelliteInfo &lhs, const QGeoSatelliteInfo
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK17QGeoSatelliteInfoS1_',
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
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QGeoSatelliteInfo
    &info)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfo.html#operator<<

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
    #  QDebug operator<<(QDebug dbg, const QGeoSatelliteInfo &info)
    address = Rituals.call(
        'ritual_Zls6QDebugRK17QGeoSatelliteInfo',
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
    Notes what was given, for Qt's 'QGeoSatelliteInfo::QGeoSatelliteInfo()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#QGeoSatelliteInfo
    """
    #  QGeoSatelliteInfo::QGeoSatelliteInfo()
    self._noteCreation(QGeoSatelliteInfo, lambda: Rituals.call(
        'ritual_ZN17QGeoSatelliteInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoSatelliteInfo) -> None:
    """
    Notes what was given, for Qt's
    'QGeoSatelliteInfo::QGeoSatelliteInfo(const QGeoSatelliteInfo &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#QGeoSatelliteInfo

    Parameters
    ----------

    other : QGeoSatelliteInfo
      Passed on as a value: Qt reads the C++ QGeoSatelliteInfo, which stays
      Python's own.
    """
    #  QGeoSatelliteInfo::QGeoSatelliteInfo(const QGeoSatelliteInfo &other)
    self._noteCreation(QGeoSatelliteInfo, lambda: Rituals.call(
        'ritual_ZN17QGeoSatelliteInfoC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QGeoSatelliteInfo::removeAttribute(Attribute
    attribute)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeosatelliteinfo.html#removeAttribute

    Parameters
    ----------

    attribute : Attribute
      Passed on as its number.
    """
    #  void QGeoSatelliteInfo::removeAttribute(Attribute attribute)
    self.uglySide.call(
        'ritual_ZN17QGeoSatelliteInfo15removeAttributeENS_9AttributeE',
        attribute.value,
    )

  def detach(self) -> None:
    """
    Calls Qt's 'void QGeoSatelliteInfo::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeosatelliteinfo.html#detach
    """
    #  void QGeoSatelliteInfo::detach()
    self.uglySide.call('ritual_ZN17QGeoSatelliteInfo6detachEv')

  @staticmethod
  def dataStreamIn(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QGeoSatelliteInfo::dataStreamIn(QDataStream &stream,
    QGeoSatelliteInfo &info)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QGeoSatelliteInfo.dataStreamIn' has no cute function yet. Qt's "
        "'QDataStream &QGeoSatelliteInfo::dataStreamIn(QDataStream &stream, "
        "QGeoSatelliteInfo &info)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def dataStreamOut(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QGeoSatelliteInfo::dataStreamOut(QDataStream &stream,
    const QGeoSatelliteInfo &info)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QGeoSatelliteInfo.dataStreamOut' has no cute function yet. Qt's "
        "'QDataStream &QGeoSatelliteInfo::dataStreamOut(QDataStream "
        "&stream, const QGeoSatelliteInfo &info)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoSatelliteInfo::swap(QGeoSatelliteInfo &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoSatelliteInfo.swap' has no cute function yet. Qt's 'void "
        "QGeoSatelliteInfo::swap(QGeoSatelliteInfo &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QGeoSatelliteInfo>': the list of QGeoSatelliteInfo, which
#  'QList[QGeoSatelliteInfo]' gives. It is made here, so that there is one as
#  soon as there can be a QGeoSatelliteInfo.
QList.createKind(
    QGeoSatelliteInfo, 'value',
    make='ritual_list_make_QGeoSatelliteInfo',
    add='ritual_list_add_QGeoSatelliteInfo',
    size='ritual_list_size_QGeoSatelliteInfo',
    at='ritual_list_at_QGeoSatelliteInfo',
    drop='ritual_list_drop_QGeoSatelliteInfo',
)
