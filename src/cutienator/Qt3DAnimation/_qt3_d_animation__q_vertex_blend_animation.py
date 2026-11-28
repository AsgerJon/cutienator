"""
Qt3DAnimation::QVertexBlendAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qvertexblendanimation.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractAnimation, QObject
from ..Qt3DRender import Qt3DRender
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVertexBlendAnimation(QAbstractAnimation):
  """
  The cute side of Qt's Qt3DAnimation::QVertexBlendAnimation: a plain Python
  object standing in front of one C++ Qt3DAnimation::QVertexBlendAnimation.

  It is built on the cute 'QAbstractAnimation', as Qt's
  Qt3DAnimation::QVertexBlendAnimation is built on Qt's QAbstractAnimation,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QVertexBlendAnimation that has a
  ritual and that Python can call so far, 14 names in all: 'metaObject',
  'tr', 'interpolator', 'target', 'targetName', 'addMorphTarget',
  'removeMorphTarget', 'setTarget', 'setTargetName', 'interpolatorChanged',
  'targetChanged', 'targetNameChanged', 'updateAnimation', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QVertexBlendAnimation::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QVertexBlendAnimation::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<float>
    Qt3DAnimation::QVertexBlendAnimation::targetPositions() const': gives a
    type Python has no way to take yet.
  - Qt's 'void Qt3DAnimation::QVertexBlendAnimation::setMorphTargets(const
    QList<Qt3DAnimation::QMorphTarget *> &targets)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QList<Qt3DAnimation::QMorphTarget *>
    Qt3DAnimation::QVertexBlendAnimation::morphTargetList()': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DAnimation::QVertexBlendAnimation::setTargetPositions(const
    QList<float> &targetPositions)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    Qt3DAnimation::QVertexBlendAnimation::targetPositionsChanged(const
    QList<float> &targetPositions)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QVertexBlendAnimationPrivate
    *Qt3DAnimation::QVertexBlendAnimation::d_func() const': takes in Python
    what 'QVertexBlendAnimationPrivate
    *Qt3DAnimation::QVertexBlendAnimation::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QVertexBlendAnimation is created at the first use,
    not by 'Qt3DAnimation::QVertexBlendAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QVertexBlendAnimation.
  - Qt tells when it has removed the C++
    Qt3DAnimation::QVertexBlendAnimation. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's Qt3DAnimation::QVertexBlendAnimation that has no cute
    function yet, 'morphTargetList', 'setMorphTargets', 'setTargetPositions',
    'targetPositions', 'targetPositionsChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DAnimation::QVertexBlendAnimation::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html#tr

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
    #  QString Qt3DAnimation::QVertexBlendAnimation::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QVertexBlendAnimation'

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
    *Qt3DAnimation::QVertexBlendAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QVertexBlendAnimation::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def interpolator(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::QVertexBlendAnimation::interpolator()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html
    """
    #  float Qt3DAnimation::QVertexBlendAnimation::interpolator() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation12interpolatorEv',
    )

  def target(self) -> Optional[Qt3DRender.QGeometryRenderer]:
    """
    Calls Qt's 'Qt3DRender::QGeometryRenderer
    *Qt3DAnimation::QVertexBlendAnimation::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html#target

    Returns
    -------

    Optional[Qt3DRender.QGeometryRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QGeometryRenderer
    #      *Qt3DAnimation::QVertexBlendAnimation::target() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation6targetEv',
    )
    return Qt3DRender.QGeometryRenderer._cuteAt(address)

  def targetName(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QVertexBlendAnimation::targetName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QVertexBlendAnimation::targetName() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation21QVertexBlendAnimation10targetNameEv',
    )

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
    Qt3DAnimation::QVertexBlendAnimation::setTarget(Qt3DRender::
    QGeometryRenderer *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html#setTarget

    Parameters
    ----------

    target : Optional[Qt3DRender.QGeometryRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QVertexBlendAnimation::setTarget(Qt3DRender::
    #      QGeometryRenderer *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation9setTargetEPN10Qt3D'
        'Render17QGeometryRendererE',
        self._addressOf(target),
    )

  @overload(str)
  def setTargetName(self, name: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QVertexBlendAnimation::setTargetName(const QString name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QVertexBlendAnimation::setTargetName(const QString
    #      name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation13setTargetNameE7QS'
        'tring',
        name,
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
    'Qt3DAnimation::QVertexBlendAnimation::QVertexBlendAnimation(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QVertexBlendAnimation::QVertexBlendAnimation(QObject
    #      *parent)
    self._noteCreation(QVertexBlendAnimation, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimationC1EP7QObject',
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
    Qt3DAnimation::QVertexBlendAnimation::addMorphTarget(Qt3DAnimation::
    QMorphTarget *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Parameters
    ----------

    target : Optional[Qt3DAnimation.QMorphTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QVertexBlendAnimation::addMorphTarget(
    #      Qt3DAnimation::QMorphTarget *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation14addMorphTargetEPN'
        'S_12QMorphTargetE',
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
    Qt3DAnimation::QVertexBlendAnimation::removeMorphTarget(Qt3DAnimation::
    QMorphTarget *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Parameters
    ----------

    target : Optional[Qt3DAnimation.QMorphTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QVertexBlendAnimation::removeMorphTarget(
    #      Qt3DAnimation::QMorphTarget *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation17removeMorphTarget'
        'EPNS_12QMorphTargetE',
        self._addressOf(target),
    )

  @overload(float)
  def interpolatorChanged(self, interpolator: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QVertexBlendAnimation::interpolatorChanged(float
    interpolator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Parameters
    ----------

    interpolator : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QVertexBlendAnimation::interpolatorChanged(float
    #      interpolator)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation19interpolatorChang'
        'edEf',
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
    Qt3DAnimation::QVertexBlendAnimation::targetChanged(Qt3DRender::
    QGeometryRenderer *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Parameters
    ----------

    target : Optional[Qt3DRender.QGeometryRenderer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QVertexBlendAnimation::targetChanged(Qt3DRender::
    #      QGeometryRenderer *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation13targetChangedEPN1'
        '0Qt3DRender17QGeometryRendererE',
        self._addressOf(target),
    )

  @overload(str)
  def targetNameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QVertexBlendAnimation::targetNameChanged(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QVertexBlendAnimation::targetNameChanged(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation17targetNameChanged'
        'ERK7QString',
        name,
    )

  @overload(float)
  def updateAnimation(self, position: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QVertexBlendAnimation::updateAnimation(float position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QVertexBlendAnimation::updateAnimation(float
    #      position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation15updateAnimationEf',
        position,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QVertexBlendAnimationPrivate]:
    """
    Calls Qt's 'QVertexBlendAnimationPrivate
    *Qt3DAnimation::QVertexBlendAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qvertexblendanimation.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QVertexBlendAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVertexBlendAnimationPrivate
    #      *Qt3DAnimation::QVertexBlendAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation21QVertexBlendAnimation6d_funcEv',
    )
    return Qt3DAnimation.QVertexBlendAnimationPrivate._cuteAt(address)

  @staticmethod
  def morphTargetList(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DAnimation::QMorphTarget *>
    Qt3DAnimation::QVertexBlendAnimation::morphTargetList()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QVertexBlendAnimation.morphTargetList' has no cute "
        "function yet. Qt's 'QList<Qt3DAnimation::QMorphTarget *> "
        "Qt3DAnimation::QVertexBlendAnimation::morphTargetList()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setMorphTargets(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QVertexBlendAnimation::setMorphTargets(const
    QList<Qt3DAnimation::QMorphTarget *> &targets)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QVertexBlendAnimation.setMorphTargets' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::QVertexBlendAnimation::setMorphTargets(const "
        "QList<Qt3DAnimation::QMorphTarget *> &targets)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setTargetPositions(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::QVertexBlendAnimation::setTargetPositions(const
    QList<float> &targetPositions)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QVertexBlendAnimation.setTargetPositions' has no "
        "cute function yet. Qt's 'void "
        "Qt3DAnimation::QVertexBlendAnimation::setTargetPositions(const "
        "QList<float> &targetPositions)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def targetPositions(*__, **_) -> Never:
    """
    Qt's 'QList<float>
    Qt3DAnimation::QVertexBlendAnimation::targetPositions() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QVertexBlendAnimation.targetPositions' has no cute "
        "function yet. Qt's 'QList<float> "
        "Qt3DAnimation::QVertexBlendAnimation::targetPositions() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def targetPositionsChanged(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::QVertexBlendAnimation::targetPositionsChanged(const
    QList<float> &targetPositions)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QVertexBlendAnimation.targetPositionsChanged' has "
        "no cute function yet. Qt's 'void "
        "Qt3DAnimation::QVertexBlendAnimation::targetPositionsChanged(const "
        "QList<float> &targetPositions)': takes a type Python has no way to "
        "hand over yet.")
