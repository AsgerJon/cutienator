"""
Qt3DAnimation::QMorphingAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qmorphinganimation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractAnimation, QObject
from ..Qt3DRender import Qt3DRender
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


class QMorphingAnimation(QAbstractAnimation):
  """
  The cute side of Qt's Qt3DAnimation::QMorphingAnimation: a plain Python
  object standing in front of one C++ Qt3DAnimation::QMorphingAnimation.

  It is built on the cute 'QAbstractAnimation', as Qt's
  Qt3DAnimation::QMorphingAnimation is built on Qt's QAbstractAnimation, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QMorphingAnimation that has a ritual
  and that Python can call so far, 20 names in all: 'metaObject', 'tr',
  'interpolator', 'target', 'targetName', 'method', 'easing',
  'addMorphTarget', 'removeMorphTarget', 'setTarget', 'setTargetName',
  'setMethod', 'setEasing', 'interpolatorChanged', 'targetChanged',
  'targetNameChanged', 'methodChanged', 'easingChanged', 'updateAnimation',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QMorphingAnimation::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QMorphingAnimation::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QVector<float> Qt3DAnimation::QMorphingAnimation::targetPositions()
    const': gives a type Python has no way to take yet.
  - Qt's 'void Qt3DAnimation::QMorphingAnimation::setMorphTargets(const
    QVector<Qt3DAnimation::QMorphTarget *> &targets)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void Qt3DAnimation::QMorphingAnimation::setWeights(int
    positionIndex, const QVector<float> &weights)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QVector<float> Qt3DAnimation::QMorphingAnimation::getWeights(int
    positionIndex)': gives a type Python has no way to take yet.
  - Qt's 'QVector<Qt3DAnimation::QMorphTarget *>
    Qt3DAnimation::QMorphingAnimation::morphTargetList()': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DAnimation::QMorphingAnimation::setTargetPositions(const
    QVector<float> &targetPositions)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    Qt3DAnimation::QMorphingAnimation::targetPositionsChanged(const
    QVector<float> &targetPositions)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QMorphingAnimationPrivate
    *Qt3DAnimation::QMorphingAnimation::d_func() const': takes in Python what
    'QMorphingAnimationPrivate *Qt3DAnimation::QMorphingAnimation::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QMorphingAnimation is created at the first use,
    not by 'Qt3DAnimation::QMorphingAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QMorphingAnimation.
  - Qt tells when it has removed the C++ Qt3DAnimation::QMorphingAnimation.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::QMorphingAnimation that has no cute
    function yet, 'getWeights', 'morphTargetList', 'setMorphTargets',
    'setTargetPositions', 'setWeights', 'targetPositions',
    'targetPositionsChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DAnimation::QMorphingAnimation, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Method(CuteNum):
    """
    The enum 'Qt3DAnimation::QMorphingAnimation::Method' of Qt, with the 2
    names Qt gives in it.
    """

    Normalized = Kee[int](0)
    Relative = Kee[int](1)

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
    Calls Qt's 'QString Qt3DAnimation::QMorphingAnimation::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#tr

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
    #  QString Qt3DAnimation::QMorphingAnimation::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QMorphingAnimation'

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
    *Qt3DAnimation::QMorphingAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QMorphingAnimation::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QMorphingAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def interpolator(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QMorphingAnimation::interpolator()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#interpolator
    """
    #  float Qt3DAnimation::QMorphingAnimation::interpolator() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QMorphingAnimation12interpolatorEv',
    )

  def target(self) -> Optional[Qt3DRender.QGeometryRenderer]:
    """
    Calls Qt's 'Qt3DRender::QGeometryRenderer
    *Qt3DAnimation::QMorphingAnimation::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#target

    Returns
    -------

    Optional[Qt3DRender.QGeometryRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QGeometryRenderer
    #      *Qt3DAnimation::QMorphingAnimation::target() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QMorphingAnimation6targetEv',
    )
    return Qt3DRender.QGeometryRenderer._cuteAt(address)

  def targetName(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QMorphingAnimation::targetName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#targetName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QMorphingAnimation::targetName() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QMorphingAnimation10targetNameEv',
    )

  def method(self) -> Method:
    """
    Calls Qt's 'QMorphingAnimation::Method
    Qt3DAnimation::QMorphingAnimation::method() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#method

    Returns
    -------

    Method
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Method(number)' gives.
    """
    #  QMorphingAnimation::Method Qt3DAnimation::QMorphingAnimation::method()
    #      const
    return QMorphingAnimation.Method(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QMorphingAnimation6methodEv',
    ))

  def easing(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve Qt3DAnimation::QMorphingAnimation::easing()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#easing

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve Qt3DAnimation::QMorphingAnimation::easing() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation18QMorphingAnimation6easingEv',
    )
    from ..QtCore import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QGeometryRenderer'])
  @overload(NoneType)
  def setTarget(
      self,
      target: Optional[Qt3DRender.QGeometryRenderer],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimation::setTarget(Qt3DRender::
    QGeometryRenderer *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#setTarget

    Parameters
    ----------

    target : Optional[Qt3DRender.QGeometryRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QMorphingAnimation::setTarget(Qt3DRender::
    #      QGeometryRenderer *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation9setTargetEPN10Qt3DRen'
        'der17QGeometryRendererE',
        self._addressOf(target),
    )

  @overload(str)
  def setTargetName(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QMorphingAnimation::setTargetName(const
    QString name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QMorphingAnimation::setTargetName(const QString
    #      name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation13setTargetNameE7QStri'
        'ng',
        name,
    )

  @overload(Method)
  def setMethod(self, method: Method) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimation::setMethod(QMorphingAnimation::Method
    method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#setMethod

    Parameters
    ----------

    method : Method
      Passed on as its number.
    """
    #  void Qt3DAnimation::QMorphingAnimation::setMethod(QMorphingAnimation::
    #      Method method)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation9setMethodENS0_6Method'
        'E',
        method.value,
    )

  @overload(QEasingCurve)
  def setEasing(self, easing: QEasingCurve) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QMorphingAnimation::setEasing(const
    QEasingCurve &easing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#setEasing

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void Qt3DAnimation::QMorphingAnimation::setEasing(const QEasingCurve
    #      &easing)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation9setEasingERK12QEasing'
        'Curve',
        self._valueOf(easing),
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
    'Qt3DAnimation::QMorphingAnimation::QMorphingAnimation(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QMorphingAnimation::QMorphingAnimation(QObject *parent)
    self._noteCreation(QMorphingAnimation, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimationC1EP7QObject',
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

  @overload(WAIT['Qt3DAnimation.QMorphTarget'])
  @overload(NoneType)
  def addMorphTarget(
      self,
      target: Optional[Qt3DAnimation.QMorphTarget],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimation::addMorphTarget(Qt3DAnimation::
    QMorphTarget *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    target : Optional[Qt3DAnimation.QMorphTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QMorphingAnimation::addMorphTarget(Qt3DAnimation::
    #      QMorphTarget *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation14addMorphTargetEPNS_1'
        '2QMorphTargetE',
        self._addressOf(target),
    )

  @overload(WAIT['Qt3DAnimation.QMorphTarget'])
  @overload(NoneType)
  def removeMorphTarget(
      self,
      target: Optional[Qt3DAnimation.QMorphTarget],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimation::removeMorphTarget(Qt3DAnimation::
    QMorphTarget *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    target : Optional[Qt3DAnimation.QMorphTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QMorphingAnimation::removeMorphTarget(
    #      Qt3DAnimation::QMorphTarget *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation17removeMorphTargetEPN'
        'S_12QMorphTargetE',
        self._addressOf(target),
    )

  @overload(float)
  def interpolatorChanged(self, interpolator: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimation::interpolatorChanged(float
    interpolator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    interpolator : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QMorphingAnimation::interpolatorChanged(float
    #      interpolator)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation19interpolatorChangedE'
        'f',
        interpolator,
    )

  @overload(WAIT['Qt3DRender.QGeometryRenderer'])
  @overload(NoneType)
  def targetChanged(
      self,
      target: Optional[Qt3DRender.QGeometryRenderer],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimation::targetChanged(Qt3DRender::
    QGeometryRenderer *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    target : Optional[Qt3DRender.QGeometryRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QMorphingAnimation::targetChanged(Qt3DRender::
    #      QGeometryRenderer *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation13targetChangedEPN10Qt'
        '3DRender17QGeometryRendererE',
        self._addressOf(target),
    )

  @overload(str)
  def targetNameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimation::targetNameChanged(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QMorphingAnimation::targetNameChanged(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation17targetNameChangedERK'
        '7QString',
        name,
    )

  @overload(Method)
  def methodChanged(self, method: Method) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimation::methodChanged(QMorphingAnimation::
    Method method)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    method : Method
      Passed on as its number.
    """
    #  void Qt3DAnimation::QMorphingAnimation::methodChanged(
    #      QMorphingAnimation::Method method)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation13methodChangedENS0_6M'
        'ethodE',
        method.value,
    )

  @overload(QEasingCurve)
  def easingChanged(self, easing: QEasingCurve) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QMorphingAnimation::easingChanged(const
    QEasingCurve &easing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    easing : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void Qt3DAnimation::QMorphingAnimation::easingChanged(const
    #      QEasingCurve &easing)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation13easingChangedERK12QE'
        'asingCurve',
        self._valueOf(easing),
    )

  @overload(float)
  def updateAnimation(self, position: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QMorphingAnimation::updateAnimation(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QMorphingAnimation::updateAnimation(float
    #      position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation15updateAnimationEf',
        position,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QMorphingAnimationPrivate]:
    """
    Calls Qt's 'QMorphingAnimationPrivate
    *Qt3DAnimation::QMorphingAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimation.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QMorphingAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMorphingAnimationPrivate *Qt3DAnimation::QMorphingAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation18QMorphingAnimation6d_funcEv',
    )
    return Qt3DAnimation.QMorphingAnimationPrivate._cuteAt(address)

  @staticmethod
  def getWeights(*__, **_) -> Never:
    """
    Qt's 'QVector<float> Qt3DAnimation::QMorphingAnimation::getWeights(int
    positionIndex)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphingAnimation.getWeights' has no cute function "
        "yet. Qt's 'QVector<float> "
        "Qt3DAnimation::QMorphingAnimation::getWeights(int positionIndex)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def morphTargetList(*__, **_) -> Never:
    """
    Qt's 'QVector<Qt3DAnimation::QMorphTarget *>
    Qt3DAnimation::QMorphingAnimation::morphTargetList()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphingAnimation.morphTargetList' has no cute "
        "function yet. Qt's 'QVector<Qt3DAnimation::QMorphTarget *> "
        "Qt3DAnimation::QMorphingAnimation::morphTargetList()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setMorphTargets(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QMorphingAnimation::setMorphTargets(const
    QVector<Qt3DAnimation::QMorphTarget *> &targets)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphingAnimation.setMorphTargets' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::QMorphingAnimation::setMorphTargets(const "
        "QVector<Qt3DAnimation::QMorphTarget *> &targets)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setTargetPositions(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QMorphingAnimation::setTargetPositions(const
    QVector<float> &targetPositions)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphingAnimation.setTargetPositions' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::QMorphingAnimation::setTargetPositions(const "
        "QVector<float> &targetPositions)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def setWeights(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QMorphingAnimation::setWeights(int
    positionIndex, const QVector<float> &weights)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphingAnimation.setWeights' has no cute function "
        "yet. Qt's 'void Qt3DAnimation::QMorphingAnimation::setWeights(int "
        "positionIndex, const QVector<float> &weights)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def targetPositions(*__, **_) -> Never:
    """
    Qt's 'QVector<float> Qt3DAnimation::QMorphingAnimation::targetPositions()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphingAnimation.targetPositions' has no cute "
        "function yet. Qt's 'QVector<float> "
        "Qt3DAnimation::QMorphingAnimation::targetPositions() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def targetPositionsChanged(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::QMorphingAnimation::targetPositionsChanged(const
    QVector<float> &targetPositions)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QMorphingAnimation.targetPositionsChanged' has no "
        "cute function yet. Qt's 'void "
        "Qt3DAnimation::QMorphingAnimation::targetPositionsChanged(const "
        "QVector<float> &targetPositions)': takes a type Python has no way "
        "to hand over yet.")
