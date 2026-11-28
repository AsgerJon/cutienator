"""
Qt3DAnimation::QAnimationController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qanimationcontroller.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAnimationController(QObject):
  """
  The cute side of Qt's Qt3DAnimation::QAnimationController: a plain Python
  object standing in front of one C++ Qt3DAnimation::QAnimationController.

  It is built on the cute 'QObject', as Qt's
  Qt3DAnimation::QAnimationController is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAnimationController that has a
  ritual and that Python can call so far, 25 names in all: 'metaObject',
  'tr', 'activeAnimationGroup', 'position', 'positionScale',
  'positionOffset', 'entity', 'recursive', 'addAnimationGroup',
  'removeAnimationGroup', 'getAnimationIndex', 'getGroup',
  'setActiveAnimationGroup', 'setPosition', 'setPositionScale',
  'setPositionOffset', 'setEntity', 'setRecursive',
  'activeAnimationGroupChanged', 'positionChanged', 'positionScaleChanged',
  'positionOffsetChanged', 'entityChanged', 'recursiveChanged', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QAnimationController::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QAnimationController::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<Qt3DAnimation::QAnimationGroup *>
    Qt3DAnimation::QAnimationController::animationGroupList()': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DAnimation::QAnimationController::setAnimationGroups(const
    QList<Qt3DAnimation::QAnimationGroup *> &animationGroups)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QAnimationControllerPrivate
    *Qt3DAnimation::QAnimationController::d_func() const': takes in Python
    what 'QAnimationControllerPrivate
    *Qt3DAnimation::QAnimationController::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAnimationController is created at the first use,
    not by 'Qt3DAnimation::QAnimationController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAnimationController.
  - Qt tells when it has removed the C++ Qt3DAnimation::QAnimationController.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::QAnimationController that has no cute
    function yet, 'animationGroupList', 'setAnimationGroups', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QAnimationController::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QAnimationController::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAnimationController'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DAnimation::QAnimationController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QAnimationController::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeAnimationGroup(self) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::QAnimationController::activeAnimationGroup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html
    """
    #  int Qt3DAnimation::QAnimationController::activeAnimationGroup() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController20activeAnimationGr'
        'oupEv',
    )

  def position(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAnimationController::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html#position
    """
    #  float Qt3DAnimation::QAnimationController::position() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController8positionEv',
    )

  def positionScale(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAnimationController::positionScale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html
    """
    #  float Qt3DAnimation::QAnimationController::positionScale() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController13positionScaleEv',
    )

  def positionOffset(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAnimationController::positionOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html
    """
    #  float Qt3DAnimation::QAnimationController::positionOffset() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController14positionOffsetEv',
    )

  def entity(self) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity
    *Qt3DAnimation::QAnimationController::entity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html#entity

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DAnimation::QAnimationController::entity() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController6entityEv',
    )
    return Qt3DCore.QEntity._cuteAt(address)

  def recursive(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::QAnimationController::recursive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html#recursive
    """
    #  bool Qt3DAnimation::QAnimationController::recursive() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController9recursiveEv',
    )

  @overload(str)
  def getAnimationIndex(self, name: str) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::QAnimationController::getAnimationIndex(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int Qt3DAnimation::QAnimationController::getAnimationIndex(const
    #      QString &name) const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController17getAnimationIndex'
        'ERK7QString',
        name,
    )

  @overload(int)
  def getGroup(self, index: int) -> Optional[Qt3DAnimation.QAnimationGroup]:
    """
    Calls Qt's 'Qt3DAnimation::QAnimationGroup
    *Qt3DAnimation::QAnimationController::getGroup(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html#getGroup

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DAnimation::QAnimationGroup
    #      *Qt3DAnimation::QAnimationController::getGroup(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationController8getGroupEi', index,
    )
    return Qt3DAnimation.QAnimationGroup._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setActiveAnimationGroup(self, index: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::setActiveAnimationGroup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::setActiveAnimationGroup(int
    #      index)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController23setActiveAnimation'
        'GroupEi',
        index,
    )

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationController::setPosition(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::setPosition(float position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController11setPositionEf',
        position,
    )

  @overload(float)
  def setPositionScale(self, scale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::setPositionScale(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::setPositionScale(float
    #      scale)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController16setPositionScaleEf',
        scale,
    )

  @overload(float)
  def setPositionOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::setPositionOffset(float offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::setPositionOffset(float
    #      offset)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController17setPositionOffsetE'
        'f',
        offset,
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def setEntity(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::setEntity(Qt3DCore::QEntity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html#setEntity

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAnimationController::setEntity(Qt3DCore::QEntity
    #      *entity)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController9setEntityEPN8Qt3DCo'
        're7QEntityE',
        self._addressOf(entity),
    )

  @overload(bool)
  def setRecursive(self, recursive: bool) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationController::setRecursive(bool
    recursive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    recursive : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::setRecursive(bool recursive)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController12setRecursiveEb',
        recursive,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QAnimationController::QAnimationController(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QAnimationController::QAnimationController(QObject
    #      *parent)
    self._noteCreation(QAnimationController, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation20QAnimationControllerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(WAIT['Qt3DAnimation.QAnimationGroup'])
  @overload(NoneType)
  def addAnimationGroup(
      self,
      animationGroups: Optional[Qt3DAnimation.QAnimationGroup],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::addAnimationGroup(Qt3DAnimation::
    QAnimationGroup *animationGroups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    animationGroups : Optional[Qt3DAnimation.QAnimationGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAnimationController::addAnimationGroup(
    #      Qt3DAnimation::QAnimationGroup *animationGroups)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController17addAnimationGroupE'
        'PNS_15QAnimationGroupE',
        self._addressOf(animationGroups),
    )

  @overload(WAIT['Qt3DAnimation.QAnimationGroup'])
  @overload(NoneType)
  def removeAnimationGroup(
      self,
      animationGroups: Optional[Qt3DAnimation.QAnimationGroup],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::removeAnimationGroup(
    Qt3DAnimation::QAnimationGroup *animationGroups)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    animationGroups : Optional[Qt3DAnimation.QAnimationGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAnimationController::removeAnimationGroup(
    #      Qt3DAnimation::QAnimationGroup *animationGroups)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController20removeAnimationGro'
        'upEPNS_15QAnimationGroupE',
        self._addressOf(animationGroups),
    )

  @overload(int)
  def activeAnimationGroupChanged(self, index: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::activeAnimationGroupChanged(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::activeAnimationGroupChanged(
    #      int index)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController27activeAnimationGro'
        'upChangedEi',
        index,
    )

  @overload(float)
  def positionChanged(self, position: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::positionChanged(float position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::positionChanged(float
    #      position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController15positionChangedEf',
        position,
    )

  @overload(float)
  def positionScaleChanged(self, scale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::positionScaleChanged(float scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    scale : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::positionScaleChanged(float
    #      scale)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController20positionScaleChang'
        'edEf',
        scale,
    )

  @overload(float)
  def positionOffsetChanged(self, offset: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::positionOffsetChanged(float
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::positionOffsetChanged(float
    #      offset)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController21positionOffsetChan'
        'gedEf',
        offset,
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def entityChanged(self, entity: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::entityChanged(Qt3DCore::QEntity
    *entity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    entity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAnimationController::entityChanged(Qt3DCore::
    #      QEntity *entity)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController13entityChangedEPN8Q'
        't3DCore7QEntityE',
        self._addressOf(entity),
    )

  @overload(bool)
  def recursiveChanged(self, recursive: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationController::recursiveChanged(bool recursive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html

    Parameters
    ----------

    recursive : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationController::recursiveChanged(bool
    #      recursive)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController16recursiveChangedEb',
        recursive,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QAnimationControllerPrivate]:
    """
    Calls Qt's 'QAnimationControllerPrivate
    *Qt3DAnimation::QAnimationController::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontroller.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationControllerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationControllerPrivate
    #      *Qt3DAnimation::QAnimationController::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationController6d_funcEv',
    )
    return Qt3DAnimation.QAnimationControllerPrivate._cuteAt(address)

  @staticmethod
  def animationGroupList(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DAnimation::QAnimationGroup *>
    Qt3DAnimation::QAnimationController::animationGroupList()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationController.animationGroupList' has no "
        "cute function yet. Qt's 'QList<Qt3DAnimation::QAnimationGroup *> "
        "Qt3DAnimation::QAnimationController::animationGroupList()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setAnimationGroups(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QAnimationController::setAnimationGroups(const
    QList<Qt3DAnimation::QAnimationGroup *> &animationGroups)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationController.setAnimationGroups' has no "
        "cute function yet. Qt's 'void "
        "Qt3DAnimation::QAnimationController::setAnimationGroups(const "
        "QList<Qt3DAnimation::QAnimationGroup *> &animationGroups)': takes "
        "a type Python has no way to hand over yet.")
