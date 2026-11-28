"""
Qt3DAnimation::QAnimationGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qanimationgroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAnimationGroup(QObject):
  """
  The cute side of Qt's Qt3DAnimation::QAnimationGroup: a plain Python object
  standing in front of one C++ Qt3DAnimation::QAnimationGroup.

  It is built on the cute 'QObject', as Qt's Qt3DAnimation::QAnimationGroup
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAnimationGroup that has a ritual and
  that Python can call so far, 13 names in all: 'metaObject', 'tr', 'name',
  'position', 'duration', 'addAnimation', 'removeAnimation', 'setName',
  'setPosition', 'nameChanged', 'positionChanged', 'durationChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QAnimationGroup::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DAnimation::QAnimationGroup::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<Qt3DAnimation::QAbstractAnimation *>
    Qt3DAnimation::QAnimationGroup::animationList()': gives a type Python has
    no way to take yet.
  - Qt's 'void Qt3DAnimation::QAnimationGroup::setAnimations(const
    QList<Qt3DAnimation::QAbstractAnimation *> &animations)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QAnimationGroupPrivate
    *Qt3DAnimation::QAnimationGroup::d_func() const': takes in Python what
    'QAnimationGroupPrivate *Qt3DAnimation::QAnimationGroup::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAnimationGroup is created at the first use, not
    by 'Qt3DAnimation::QAnimationGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAnimationGroup.
  - Qt tells when it has removed the C++ Qt3DAnimation::QAnimationGroup.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::QAnimationGroup that has no cute
    function yet, 'animationList', 'setAnimations', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DAnimation::QAnimationGroup::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#tr

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
    #  QString Qt3DAnimation::QAnimationGroup::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAnimationGroup'

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
    *Qt3DAnimation::QAnimationGroup::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QAnimationGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation15QAnimationGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QAnimationGroup::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QAnimationGroup::name() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation15QAnimationGroup4nameEv',
    )

  def position(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAnimationGroup::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#position
    """
    #  float Qt3DAnimation::QAnimationGroup::position() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation15QAnimationGroup8positionEv',
    )

  def duration(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QAnimationGroup::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#duration
    """
    #  float Qt3DAnimation::QAnimationGroup::duration() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation15QAnimationGroup8durationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationGroup::setName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QAnimationGroup::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup7setNameERK7QString', name,
    )

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationGroup::setPosition(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationGroup::setPosition(float position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup11setPositionEf', position,
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
    'Qt3DAnimation::QAnimationGroup::QAnimationGroup(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#QAnimationGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QAnimationGroup::QAnimationGroup(QObject *parent)
    self._noteCreation(QAnimationGroup, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroupC1EP7QObject',
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

  @overload(WAIT['Qt3DAnimation.QAbstractAnimation'])
  @overload(NoneType)
  def addAnimation(
      self,
      animation: Optional[Qt3DAnimation.QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationGroup::addAnimation(Qt3DAnimation::
    QAbstractAnimation *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#addAnimation

    Parameters
    ----------

    animation : Optional[Qt3DAnimation.QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAnimationGroup::addAnimation(Qt3DAnimation::
    #      QAbstractAnimation *animation)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup12addAnimationEPNS_18QAbs'
        'tractAnimationE',
        self._addressOf(animation),
    )

  @overload(WAIT['Qt3DAnimation.QAbstractAnimation'])
  @overload(NoneType)
  def removeAnimation(
      self,
      animation: Optional[Qt3DAnimation.QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationGroup::removeAnimation(Qt3DAnimation::
    QAbstractAnimation *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#removeAnimation

    Parameters
    ----------

    animation : Optional[Qt3DAnimation.QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QAnimationGroup::removeAnimation(Qt3DAnimation::
    #      QAbstractAnimation *animation)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup15removeAnimationEPNS_18Q'
        'AbstractAnimationE',
        self._addressOf(animation),
    )

  @overload(str)
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationGroup::nameChanged(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QAnimationGroup::nameChanged(const QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup11nameChangedERK7QString',
        name,
    )

  @overload(float)
  def positionChanged(self, position: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationGroup::positionChanged(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#positionChanged

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationGroup::positionChanged(float position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup15positionChangedEf',
        position,
    )

  @overload(float)
  def durationChanged(self, duration: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationGroup::durationChanged(float
    duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#durationChanged

    Parameters
    ----------

    duration : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationGroup::durationChanged(float duration)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup15durationChangedEf',
        duration,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QAnimationGroupPrivate]:
    """
    Calls Qt's 'QAnimationGroupPrivate
    *Qt3DAnimation::QAnimationGroup::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroup.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationGroupPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationGroupPrivate *Qt3DAnimation::QAnimationGroup::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QAnimationGroup6d_funcEv',
    )
    return Qt3DAnimation.QAnimationGroupPrivate._cuteAt(address)

  @staticmethod
  def animationList(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DAnimation::QAbstractAnimation *>
    Qt3DAnimation::QAnimationGroup::animationList()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationGroup.animationList' has no cute function "
        "yet. Qt's 'QList<Qt3DAnimation::QAbstractAnimation *> "
        "Qt3DAnimation::QAnimationGroup::animationList()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setAnimations(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QAnimationGroup::setAnimations(const
    QList<Qt3DAnimation::QAbstractAnimation *> &animations)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAnimationGroup.setAnimations' has no cute function "
        "yet. Qt's 'void "
        "Qt3DAnimation::QAnimationGroup::setAnimations(const "
        "QList<Qt3DAnimation::QAbstractAnimation *> &animations)': takes a "
        "type Python has no way to hand over yet.")
