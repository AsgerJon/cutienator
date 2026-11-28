"""
Qt3DRender::QRayCasterHit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qraycasterhit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRayCasterHit(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QRayCasterHit: a plain Python object
  standing in front of one C++ Qt3DRender::QRayCasterHit.

  C++ hands a Qt3DRender::QRayCasterHit around as a copy, so every C++
  Qt3DRender::QRayCasterHit behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRayCasterHit that has a ritual and that
  Python can call so far, 12 names in all: 'type', 'entityId', 'entity',
  'distance', 'localIntersection', 'worldIntersection', 'primitiveIndex',
  'vertex1Index', 'vertex2Index', 'vertex3Index', 'toString', 'setEntity'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QRayCasterHit::~QRayCasterHit()': the destructor:
    Python removes its C++ Qt3DRender::QRayCasterHit by it, and has no other
    use for it.
  - Qt's 'QRayCasterHit &Qt3DRender::QRayCasterHit::operator=(const
    QRayCasterHit &other)': assignment: Python binds a name and has no
    operator for it.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRayCasterHit is created at the first use, not by
    'Qt3DRender::QRayCasterHit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QRayCasterHit back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::QRayCasterHit.
  """

  #  The enums Qt writes inside Qt3DRender::QRayCasterHit, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class HitType(CuteNum):
    """
    The enum 'Qt3DRender::QRayCasterHit::HitType' of Qt, with the 4 names Qt
    gives in it.
    """

    TriangleHit = Kee[int](0)
    LineHit = Kee[int](1)
    PointHit = Kee[int](2)
    EntityHit = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRayCasterHit'

  #  Qt's '~Qt3DRender::QRayCasterHit()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DRender::QRayCasterHit behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender13QRayCasterHitD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> HitType:
    """
    Calls Qt's 'HitType Qt3DRender::QRayCasterHit::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#type

    Returns
    -------

    HitType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HitType(number)' gives.
    """
    #  HitType Qt3DRender::QRayCasterHit::type() const
    return QRayCasterHit.HitType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit4typeEv',
    ))

  def entityId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId Qt3DRender::QRayCasterHit::entityId()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#entityId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::QRayCasterHit::entityId() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit8entityIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def entity(self) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity *Qt3DRender::QRayCasterHit::entity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#entity

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DRender::QRayCasterHit::entity() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit6entityEv',
    )
    return Qt3DCore.QEntity._cuteAt(address)

  def distance(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QRayCasterHit::distance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#distance
    """
    #  float Qt3DRender::QRayCasterHit::distance() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit8distanceEv',
    )

  def localIntersection(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QRayCasterHit::localIntersection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#localIntersection

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QRayCasterHit::localIntersection() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit17localIntersectionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def worldIntersection(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QRayCasterHit::worldIntersection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#worldIntersection

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QRayCasterHit::worldIntersection() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit17worldIntersectionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def primitiveIndex(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QRayCasterHit::primitiveIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#primitiveIndex
    """
    #  uint Qt3DRender::QRayCasterHit::primitiveIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit14primitiveIndexEv',
    )

  def vertex1Index(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QRayCasterHit::vertex1Index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#vertex1Index
    """
    #  uint Qt3DRender::QRayCasterHit::vertex1Index() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit12vertex1IndexEv',
    )

  def vertex2Index(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QRayCasterHit::vertex2Index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#vertex2Index
    """
    #  uint Qt3DRender::QRayCasterHit::vertex2Index() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit12vertex2IndexEv',
    )

  def vertex3Index(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QRayCasterHit::vertex3Index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#vertex3Index
    """
    #  uint Qt3DRender::QRayCasterHit::vertex3Index() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit12vertex3IndexEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def setEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRayCasterHit::setEntity(Qt3DCore::QEntity
    *entity) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#setEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QRayCasterHit::setEntity(Qt3DCore::QEntity *entity)
    #      const
    self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QRayCasterHit9setEntityEPN8Qt3DCore7QEntit'
        'yE',
        self._addressOf(entity),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRayCasterHit::QRayCasterHit()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#QRayCasterHit
    """
    #  Qt3DRender::QRayCasterHit::QRayCasterHit()
    self._noteCreation(QRayCasterHit, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QRayCasterHitC1Ev',
    ))

  @overload(
      HitType, WAIT['Qt3DCore.QNodeId'], float, QVector3D, QVector3D, int,
      int, int, int,
  )
  def __init__(
      self,
      type: HitType,
      id: Qt3DCore.QNodeId,
      distance: float,
      localIntersect: QVector3D,
      worldIntersect: QVector3D,
      primitiveIndex: int,
      v1: int,
      v2: int,
      v3: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRayCasterHit::QRayCasterHit(QRayCasterHit::HitType type,
    Qt3DCore::QNodeId id, float distance, const QVector3D &localIntersect,
    const QVector3D &worldIntersect, uint primitiveIndex, uint v1, uint v2,
    uint v3)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#QRayCasterHit

    Parameters
    ----------

    type : HitType
      Passed on as its number.

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    distance : float
      Passed on as it is.

    localIntersect : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    worldIntersect : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    primitiveIndex : int
      Passed on as it is.

    v1 : int
      Passed on as it is.

    v2 : int
      Passed on as it is.

    v3 : int
      Passed on as it is.
    """
    #  Qt3DRender::QRayCasterHit::QRayCasterHit(QRayCasterHit::HitType type,
    #      Qt3DCore::QNodeId id, float distance, const QVector3D
    #      &localIntersect, const QVector3D &worldIntersect, uint
    #      primitiveIndex, uint v1, uint v2, uint v3)
    self._noteCreation(QRayCasterHit, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QRayCasterHitC1ENS0_7HitTypeEN8Qt3DCore7QNo'
        'deIdEfRK9QVector3DS6_jjjj',
        type.value, self._valueOf(id), distance,
        self._valueOf(localIntersect), self._valueOf(worldIntersect),
        primitiveIndex, v1, v2, v3,
    ))

  @overload(THIS)
  def __init__(self, other: QRayCasterHit) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRayCasterHit::QRayCasterHit(const QRayCasterHit &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#QRayCasterHit

    Parameters
    ----------

    other : QRayCasterHit
      Passed on as a value: Qt reads the C++ Qt3DRender::QRayCasterHit, which
      stays Python's own.
    """
    #  Qt3DRender::QRayCasterHit::QRayCasterHit(const QRayCasterHit &other)
    self._noteCreation(QRayCasterHit, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QRayCasterHitC1ERKS0_', self._valueOf(other),
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

  def toString(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QRayCasterHit::toString()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qraycasterhit.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QRayCasterHit::toString()
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender13QRayCasterHit8toStringEv',
    )
