"""
QQuick3DPickResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dpickresult_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DPickResult to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQuick3DPickResultEnums

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QVector2D, QVector3D
  from ..QtQuick import QQuickItem
  from . import QQuick3DModel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DModel = WAIT['QQuick3DModel']
  QQuickItem = WAIT['QQuickItem']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DPickResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DPickResult: a plain Python object standing in
  front of one C++ QQuick3DPickResult.

  C++ hands a QQuick3DPickResult around as a copy, so every C++
  QQuick3DPickResult behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuick3DPickResult that has a ritual and that Python
  can call so far, 10 names in all: 'objectHit', 'distance', 'uvPosition',
  'scenePosition', 'position', 'normal', 'sceneNormal', 'instanceIndex',
  'itemHit', 'hitType'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DPickResult::~QQuick3DPickResult()': the destructor: Python
    removes its C++ QQuick3DPickResult by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DPickResult is created at the first use, not by
    'QQuick3DPickResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DPickResult back gives a copy the ritual made
    for Python, in a new cute QQuick3DPickResult.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DPickResult'

  #  Qt's '~QQuick3DPickResult()'. Naming it makes this a value class: Python
  #  owns every C++ QQuick3DPickResult behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuick3DPickResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def objectHit(self) -> Optional[QQuick3DModel]:
    """
    Calls Qt's 'QQuick3DModel *QQuick3DPickResult::objectHit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpickresult.html#objectHit

    Returns
    -------

    Optional[QQuick3DModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DModel *QQuick3DPickResult::objectHit() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DPickResult9objectHitEv',
    )
    from . import QQuick3DModel
    return QQuick3DModel._cuteAt(address)

  def distance(self) -> float:
    """
    Calls Qt's 'float QQuick3DPickResult::distance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpickresult.html#distance
    """
    #  float QQuick3DPickResult::distance() const
    return self.uglySide.call('ritual_ZNK18QQuick3DPickResult8distanceEv')

  def uvPosition(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuick3DPickResult::uvPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpickresult.html#uvPosition

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuick3DPickResult::uvPosition() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DPickResult10uvPositionEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def scenePosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DPickResult::scenePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpickresult.html#scenePosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DPickResult::scenePosition() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DPickResult13scenePositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DPickResult::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpickresult.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DPickResult::position() const
    address = self.uglySide.call('ritual_ZNK18QQuick3DPickResult8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def normal(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DPickResult::normal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpickresult.html#normal

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DPickResult::normal() const
    address = self.uglySide.call('ritual_ZNK18QQuick3DPickResult6normalEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sceneNormal(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DPickResult::sceneNormal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpickresult.html#sceneNormal

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DPickResult::sceneNormal() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuick3DPickResult11sceneNormalEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def instanceIndex(self) -> int:
    """
    Calls Qt's 'int QQuick3DPickResult::instanceIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpickresult.html#instanceIndex
    """
    #  int QQuick3DPickResult::instanceIndex() const
    return self.uglySide.call(
        'ritual_ZNK18QQuick3DPickResult13instanceIndexEv',
    )

  def itemHit(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuick3DPickResult::itemHit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpickresult.html#itemHit

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuick3DPickResult::itemHit() const
    address = self.uglySide.call('ritual_ZNK18QQuick3DPickResult7itemHitEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def hitType(self) -> QQuick3DPickResultEnums.HitType:
    """
    Calls Qt's 'QQuick3DPickResultEnums::HitType
    QQuick3DPickResult::hitType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dpickresult.html#hitType

    Returns
    -------

    QQuick3DPickResultEnums.HitType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DPickResultEnums.HitType(number)' gives.
    """
    #  QQuick3DPickResultEnums::HitType QQuick3DPickResult::hitType() const
    return QQuick3DPickResultEnums.HitType(self.uglySide.call(
        'ritual_ZNK18QQuick3DPickResult7hitTypeEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DPickResult::QQuick3DPickResult()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpickresult.html#QQuick3DPickResult
    """
    #  QQuick3DPickResult::QQuick3DPickResult()
    self._noteCreation(QQuick3DPickResult, lambda: Rituals.call(
        'ritual_ZN18QQuick3DPickResultC1Ev',
    ))

  @overload(
      QQuick3DModel, float, QVector2D, QVector3D, QVector3D, QVector3D,
      QVector3D, int,
  )
  @overload(
      NoneType, float, QVector2D, QVector3D, QVector3D, QVector3D, QVector3D,
      int,
  )
  @overload(
      QQuick3DModel, float, QVector2D, QVector3D, QVector3D, QVector3D,
      QVector3D, int, QQuickItem,
  )
  @overload(
      QQuick3DModel, float, QVector2D, QVector3D, QVector3D, QVector3D,
      QVector3D, int, NoneType,
  )
  @overload(
      NoneType, float, QVector2D, QVector3D, QVector3D, QVector3D, QVector3D,
      int, QQuickItem,
  )
  @overload(
      NoneType, float, QVector2D, QVector3D, QVector3D, QVector3D, QVector3D,
      int, NoneType,
  )
  def __init__(
      self,
      hitObject: Optional[QQuick3DModel],
      distanceFromCamera: float,
      uvPosition: QVector2D,
      scenePosition: QVector3D,
      position: QVector3D,
      normal: QVector3D,
      sceneNormal: QVector3D,
      instanceIndex: int,
      itemHit: Optional[QQuickItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DPickResult::QQuick3DPickResult(QQuick3DModel *hitObject, float
    distanceFromCamera, const QVector2D &uvPosition, const QVector3D
    &scenePosition, const QVector3D &position, const QVector3D &normal, const
    QVector3D &sceneNormal, int instanceIndex, QQuickItem *itemHit)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpickresult.html#QQuick3DPickResult

    Parameters
    ----------

    hitObject : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    distanceFromCamera : float
      Passed on as it is.

    uvPosition : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    scenePosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    normal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    sceneNormal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    instanceIndex : int
      Passed on as it is.

    itemHit : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DPickResult::QQuick3DPickResult(QQuick3DModel *hitObject, float
    #      distanceFromCamera, const QVector2D &uvPosition, const QVector3D
    #      &scenePosition, const QVector3D &position, const QVector3D
    #      &normal, const QVector3D &sceneNormal, int instanceIndex,
    #      QQuickItem *itemHit)
    self._noteCreation(QQuick3DPickResult, lambda: Rituals.call(
        'ritual_ZN18QQuick3DPickResultC1EP13QQuick3DModelfRK9QVector2DRK9QV'
        'ector3DS7_S7_S7_iP10QQuickItem',
        self._addressOf(hitObject), distanceFromCamera,
        self._valueOf(uvPosition), self._valueOf(scenePosition),
        self._valueOf(position), self._valueOf(normal),
        self._valueOf(sceneNormal), instanceIndex, self._addressOf(itemHit),
    ))

  @overload(QQuickItem, float, QVector2D, QVector3D, QVector3D, QVector3D)
  @overload(NoneType, float, QVector2D, QVector3D, QVector3D, QVector3D)
  def __init__(
      self,
      itemHit: Optional[QQuickItem],
      distanceFromCamera: float,
      uvPosition: QVector2D,
      scenePosition: QVector3D,
      position: QVector3D,
      sceneNormal: QVector3D,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DPickResult::QQuick3DPickResult(QQuickItem *itemHit, float
    distanceFromCamera, const QVector2D &uvPosition, const QVector3D
    &scenePosition, const QVector3D &position, const QVector3D
    &sceneNormal)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpickresult.html#QQuick3DPickResult

    Parameters
    ----------

    itemHit : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    distanceFromCamera : float
      Passed on as it is.

    uvPosition : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    scenePosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    sceneNormal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QQuick3DPickResult::QQuick3DPickResult(QQuickItem *itemHit, float
    #      distanceFromCamera, const QVector2D &uvPosition, const QVector3D
    #      &scenePosition, const QVector3D &position, const QVector3D
    #      &sceneNormal)
    self._noteCreation(QQuick3DPickResult, lambda: Rituals.call(
        'ritual_ZN18QQuick3DPickResultC1EP10QQuickItemfRK9QVector2DRK9QVect'
        'or3DS7_S7_',
        self._addressOf(itemHit), distanceFromCamera,
        self._valueOf(uvPosition), self._valueOf(scenePosition),
        self._valueOf(position), self._valueOf(sceneNormal),
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


#  Qt's 'QList<QQuick3DPickResult>': the list of QQuick3DPickResult, which
#  'QList[QQuick3DPickResult]' gives. It is made here, so that there is one
#  as soon as there can be a QQuick3DPickResult.
QList.createKind(
    QQuick3DPickResult, 'value',
    make='ritual_list_make_QQuick3DPickResult',
    add='ritual_list_add_QQuick3DPickResult',
    size='ritual_list_size_QQuick3DPickResult',
    at='ritual_list_at_QQuick3DPickResult',
    drop='ritual_list_drop_QQuick3DPickResult',
)
