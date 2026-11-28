"""
Qt3DAnimation::QKeyframeAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qkeyframeanimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractAnimation, QObject
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEasingCurve, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QKeyframeAnimation(QAbstractAnimation):
  """
  The cute side of Qt's Qt3DAnimation::QKeyframeAnimation: a plain Python
  object standing in front of one C++ Qt3DAnimation::QKeyframeAnimation.

  It is built on the cute 'QAbstractAnimation', as Qt's
  Qt3DAnimation::QKeyframeAnimation is built on Qt's QAbstractAnimation, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QKeyframeAnimation that has a ritual
  and that Python can call so far, 21 names in all: 'metaObject', 'tr',
  'target', 'easing', 'targetName', 'startMode', 'endMode', 'addKeyframe',
  'removeKeyframe', 'setTarget', 'setEasing', 'setTargetName',
  'setStartMode', 'setEndMode', 'targetChanged', 'easingChanged',
  'targetNameChanged', 'startModeChanged', 'endModeChanged',
  'updateAnimation', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QKeyframeAnimation::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QKeyframeAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<float> Qt3DAnimation::QKeyframeAnimation::framePositions()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<Qt3DCore::QTransform *>
    Qt3DAnimation::QKeyframeAnimation::keyframeList() const': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DAnimation::QKeyframeAnimation::setKeyframes(const
    QList<Qt3DCore::QTransform *> &keyframes)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void Qt3DAnimation::QKeyframeAnimation::setFramePositions(const
    QList<float> &positions)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void Qt3DAnimation::QKeyframeAnimation::framePositionsChanged(const
    QList<float> &positions)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QKeyframeAnimationPrivate
    *Qt3DAnimation::QKeyframeAnimation::d_func() const': takes in Python what
    'QKeyframeAnimationPrivate *Qt3DAnimation::QKeyframeAnimation::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QKeyframeAnimation is created at the first use,
    not by 'Qt3DAnimation::QKeyframeAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QKeyframeAnimation.
  - Qt tells when it has removed the C++ Qt3DAnimation::QKeyframeAnimation.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::QKeyframeAnimation that has no cute
    function yet, 'framePositions', 'framePositionsChanged', 'keyframeList',
    'setFramePositions', 'setKeyframes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DAnimation::QKeyframeAnimation, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class RepeatMode(CuteNum):
    """
    The enum 'Qt3DAnimation::QKeyframeAnimation::RepeatMode' of Qt, with the
    3 names Qt gives in it.
    """

    NULL = Kee[int](0)
    Constant = Kee[int](1)
    Repeat = Kee[int](2)

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
    Calls Qt's 'QString Qt3DAnimation::QKeyframeAnimation::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#tr

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
    #  QString Qt3DAnimation::QKeyframeAnimation::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QKeyframeAnimation'

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
    *Qt3DAnimation::QKeyframeAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QKeyframeAnimation::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QKeyframeAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[Qt3DCore.QTransform]:
    """
    Calls Qt's 'Qt3DCore::QTransform
    *Qt3DAnimation::QKeyframeAnimation::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#target

    Returns
    -------

    Optional[Qt3DCore.QTransform]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QTransform *Qt3DAnimation::QKeyframeAnimation::target()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QKeyframeAnimation6targetEv',
    )
    return Qt3DCore.QTransform._cuteAt(address)

  def easing(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve Qt3DAnimation::QKeyframeAnimation::easing()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#easing

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve Qt3DAnimation::QKeyframeAnimation::easing() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QKeyframeAnimation6easingEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def targetName(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QKeyframeAnimation::targetName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#targetName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QKeyframeAnimation::targetName() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QKeyframeAnimation10targetNameEv',
    )

  def startMode(self) -> RepeatMode:
    """
    Calls Qt's 'RepeatMode Qt3DAnimation::QKeyframeAnimation::startMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#startMode

    Returns
    -------

    RepeatMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RepeatMode(number)'
      gives.
    """
    #  RepeatMode Qt3DAnimation::QKeyframeAnimation::startMode() const
    return QKeyframeAnimation.RepeatMode(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QKeyframeAnimation9startModeEv',
    ))

  def endMode(self) -> RepeatMode:
    """
    Calls Qt's 'RepeatMode Qt3DAnimation::QKeyframeAnimation::endMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#endMode

    Returns
    -------

    RepeatMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RepeatMode(number)'
      gives.
    """
    #  RepeatMode Qt3DAnimation::QKeyframeAnimation::endMode() const
    return QKeyframeAnimation.RepeatMode(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QKeyframeAnimation7endModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QTransform'])
  @overload(NoneType)
  def setTarget(self, target: Optional[Qt3DCore.QTransform]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyframeAnimation::setTarget(Qt3DCore::QTransform
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#setTarget

    Parameters
    ----------

    target : Optional[Qt3DCore.QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::setTarget(Qt3DCore::QTransform
    #      *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation9setTargetEPN8Qt3DCore'
        '10QTransformE',
        self._addressOf(target),
    )

  @overload(QEasingCurve)
  def setEasing(self, easing: QEasingCurve) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QKeyframeAnimation::setEasing(const
    QEasingCurve &easing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#setEasing

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::setEasing(const QEasingCurve
    #      &easing)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation9setEasingERK12QEasing'
        'Curve',
        self._valueOf(easing),
    )

  @overload(str)
  def setTargetName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QKeyframeAnimation::setTargetName(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::setTargetName(const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation13setTargetNameERK7QSt'
        'ring',
        name,
    )

  @overload(RepeatMode)
  def setStartMode(self, mode: RepeatMode) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyframeAnimation::setStartMode(RepeatMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#setStartMode

    Parameters
    ----------

    mode : RepeatMode
      Passed on as its number.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::setStartMode(RepeatMode mode)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation12setStartModeENS0_10R'
        'epeatModeE',
        mode.value,
    )

  @overload(RepeatMode)
  def setEndMode(self, mode: RepeatMode) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QKeyframeAnimation::setEndMode(RepeatMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#setEndMode

    Parameters
    ----------

    mode : RepeatMode
      Passed on as its number.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::setEndMode(RepeatMode mode)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation10setEndModeENS0_10Rep'
        'eatModeE',
        mode.value,
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
    'Qt3DAnimation::QKeyframeAnimation::QKeyframeAnimation(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QKeyframeAnimation::QKeyframeAnimation(QObject *parent)
    self._noteCreation(QKeyframeAnimation, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimationC1EP7QObject',
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

  @overload(WAIT['Qt3DCore.QTransform'])
  @overload(NoneType)
  def addKeyframe(self, keyframe: Optional[Qt3DCore.QTransform]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyframeAnimation::addKeyframe(Qt3DCore::QTransform
    *keyframe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#addKeyframe

    Parameters
    ----------

    keyframe : Optional[Qt3DCore.QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::addKeyframe(Qt3DCore::
    #      QTransform *keyframe)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation11addKeyframeEPN8Qt3DC'
        'ore10QTransformE',
        self._addressOf(keyframe),
    )

  @overload(WAIT['Qt3DCore.QTransform'])
  @overload(NoneType)
  def removeKeyframe(self, keyframe: Optional[Qt3DCore.QTransform]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyframeAnimation::removeKeyframe(Qt3DCore::QTransform
    *keyframe)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    keyframe : Optional[Qt3DCore.QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::removeKeyframe(Qt3DCore::
    #      QTransform *keyframe)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation14removeKeyframeEPN8Qt'
        '3DCore10QTransformE',
        self._addressOf(keyframe),
    )

  @overload(WAIT['Qt3DCore.QTransform'])
  @overload(NoneType)
  def targetChanged(self, target: Optional[Qt3DCore.QTransform]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyframeAnimation::targetChanged(Qt3DCore::QTransform
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    target : Optional[Qt3DCore.QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::targetChanged(Qt3DCore::
    #      QTransform *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation13targetChangedEPN8Qt3'
        'DCore10QTransformE',
        self._addressOf(target),
    )

  @overload(QEasingCurve)
  def easingChanged(self, easing: QEasingCurve) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QKeyframeAnimation::easingChanged(const
    QEasingCurve &easing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::easingChanged(const
    #      QEasingCurve &easing)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation13easingChangedERK12QE'
        'asingCurve',
        self._valueOf(easing),
    )

  @overload(str)
  def targetNameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyframeAnimation::targetNameChanged(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::targetNameChanged(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation17targetNameChangedERK'
        '7QString',
        name,
    )

  @overload(RepeatMode)
  def startModeChanged(self, startMode: RepeatMode) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyframeAnimation::startModeChanged(QKeyframeAnimation::
    RepeatMode startMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    startMode : RepeatMode
      Passed on as its number.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::startModeChanged(
    #      QKeyframeAnimation::RepeatMode startMode)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation16startModeChangedENS0'
        '_10RepeatModeE',
        startMode.value,
    )

  @overload(RepeatMode)
  def endModeChanged(self, endMode: RepeatMode) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QKeyframeAnimation::endModeChanged(QKeyframeAnimation::
    RepeatMode endMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    endMode : RepeatMode
      Passed on as its number.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::endModeChanged(
    #      QKeyframeAnimation::RepeatMode endMode)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation14endModeChangedENS0_1'
        '0RepeatModeE',
        endMode.value,
    )

  @overload(float)
  def updateAnimation(self, position: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QKeyframeAnimation::updateAnimation(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QKeyframeAnimation::updateAnimation(float
    #      position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation15updateAnimationEf',
        position,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QKeyframeAnimationPrivate]:
    """
    Calls Qt's 'QKeyframeAnimationPrivate
    *Qt3DAnimation::QKeyframeAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qkeyframeanimation.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QKeyframeAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeyframeAnimationPrivate *Qt3DAnimation::QKeyframeAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QKeyframeAnimation6d_funcEv',
    )
    return Qt3DAnimation.QKeyframeAnimationPrivate._cuteAt(address)

  @staticmethod
  def framePositions(*__, **_) -> Never:
    """
    Qt's 'QList<float> Qt3DAnimation::QKeyframeAnimation::framePositions()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QKeyframeAnimation.framePositions' has no cute "
        "function yet. Qt's 'QList<float> "
        "Qt3DAnimation::QKeyframeAnimation::framePositions() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def framePositionsChanged(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QKeyframeAnimation::framePositionsChanged(const
    QList<float> &positions)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QKeyframeAnimation.framePositionsChanged' has no "
        "cute function yet. Qt's 'void "
        "Qt3DAnimation::QKeyframeAnimation::framePositionsChanged(const "
        "QList<float> &positions)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def keyframeList(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QTransform *>
    Qt3DAnimation::QKeyframeAnimation::keyframeList() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QKeyframeAnimation.keyframeList' has no cute "
        "function yet. Qt's 'QList<Qt3DCore::QTransform *> "
        "Qt3DAnimation::QKeyframeAnimation::keyframeList() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setFramePositions(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QKeyframeAnimation::setFramePositions(const
    QList<float> &positions)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QKeyframeAnimation.setFramePositions' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::QKeyframeAnimation::setFramePositions(const "
        "QList<float> &positions)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setKeyframes(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QKeyframeAnimation::setKeyframes(const
    QList<Qt3DCore::QTransform *> &keyframes)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QKeyframeAnimation.setKeyframes' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::QKeyframeAnimation::setKeyframes(const "
        "QList<Qt3DCore::QTransform *> &keyframes)': takes a type Python "
        "has no way to hand over yet.")
