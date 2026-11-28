"""
Qt3DRender::QSpotLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qspotlight.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpotLight(Qt3DRender.QAbstractLight):
  """
  The cute side of Qt's Qt3DRender::QSpotLight: a plain Python object
  standing in front of one C++ Qt3DRender::QSpotLight.

  It is built on the cute 'Qt3DRender::QAbstractLight', as Qt's
  Qt3DRender::QSpotLight is built on Qt's Qt3DRender::QAbstractLight, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QSpotLight that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr',
  'localDirection', 'cutOffAngle', 'constantAttenuation',
  'linearAttenuation', 'quadraticAttenuation', 'setConstantAttenuation',
  'setLinearAttenuation', 'setQuadraticAttenuation', 'setLocalDirection',
  'setCutOffAngle', 'constantAttenuationChanged', 'linearAttenuationChanged',
  'quadraticAttenuationChanged', 'localDirectionChanged',
  'cutOffAngleChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QSpotLight::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QSpotLight::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QSpotLight::~QSpotLight()': the destructor: Python
    never removes a C++ Qt3DRender::QSpotLight.
  - Qt's 'Qt3DRender::QSpotLight::QSpotLight(QSpotLightPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QSpotLightPrivate *Qt3DRender::QSpotLight::d_func() const':
    takes in Python what 'QSpotLightPrivate
    *Qt3DRender::QSpotLight::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QSpotLight is created at the first use, not by
    'Qt3DRender::QSpotLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QSpotLight.
  - Qt tells when it has removed the C++ Qt3DRender::QSpotLight. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DRender::QSpotLight::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qspotlight.html#tr

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
    #  QString Qt3DRender::QSpotLight::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QSpotLight2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QSpotLight'

  #  A C++ Qt3DRender::QSpotLight Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QSpotLight'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QSpotLight::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QSpotLight::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QSpotLight10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def localDirection(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D Qt3DRender::QSpotLight::localDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#localDirection

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D Qt3DRender::QSpotLight::localDirection() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QSpotLight14localDirectionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def cutOffAngle(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QSpotLight::cutOffAngle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#cutOffAngle
    """
    #  float Qt3DRender::QSpotLight::cutOffAngle() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QSpotLight11cutOffAngleEv',
    )

  def constantAttenuation(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QSpotLight::constantAttenuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#constantAttenuation
    """
    #  float Qt3DRender::QSpotLight::constantAttenuation() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QSpotLight19constantAttenuationEv',
    )

  def linearAttenuation(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QSpotLight::linearAttenuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#linearAttenuation
    """
    #  float Qt3DRender::QSpotLight::linearAttenuation() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QSpotLight17linearAttenuationEv',
    )

  def quadraticAttenuation(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QSpotLight::quadraticAttenuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#quadraticAttenuation
    """
    #  float Qt3DRender::QSpotLight::quadraticAttenuation() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QSpotLight20quadraticAttenuationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setConstantAttenuation(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::setConstantAttenuation(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#setConstantAttenuation

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DRender::QSpotLight::setConstantAttenuation(float value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight22setConstantAttenuationEf', value,
    )

  @overload(float)
  def setLinearAttenuation(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::setLinearAttenuation(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#setLinearAttenuation

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DRender::QSpotLight::setLinearAttenuation(float value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight20setLinearAttenuationEf', value,
    )

  @overload(float)
  def setQuadraticAttenuation(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::setQuadraticAttenuation(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#setQuadraticAttenuation

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DRender::QSpotLight::setQuadraticAttenuation(float value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight23setQuadraticAttenuationEf',
        value,
    )

  @overload(QVector3D)
  def setLocalDirection(self, localDirection: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::setLocalDirection(const
    QVector3D &localDirection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#setLocalDirection

    Parameters
    ----------

    localDirection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QSpotLight::setLocalDirection(const QVector3D
    #      &localDirection)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight17setLocalDirectionERK9QVector3D',
        self._valueOf(localDirection),
    )

  @overload(float)
  def setCutOffAngle(self, cutOffAngle: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::setCutOffAngle(float
    cutOffAngle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#setCutOffAngle

    Parameters
    ----------

    cutOffAngle : float
      Passed on as it is.
    """
    #  void Qt3DRender::QSpotLight::setCutOffAngle(float cutOffAngle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight14setCutOffAngleEf', cutOffAngle,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QSpotLight::QSpotLight(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#QSpotLight

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QSpotLight::QSpotLight(Qt3DCore::QNode *parent)
    self._noteCreation(QSpotLight, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QSpotLightC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(float)
  def constantAttenuationChanged(self, constantAttenuation: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::constantAttenuationChanged(float
    constantAttenuation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html

    Parameters
    ----------

    constantAttenuation : float
      Passed on as it is.
    """
    #  void Qt3DRender::QSpotLight::constantAttenuationChanged(float
    #      constantAttenuation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight26constantAttenuationChangedEf',
        constantAttenuation,
    )

  @overload(float)
  def linearAttenuationChanged(self, linearAttenuation: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::linearAttenuationChanged(float
    linearAttenuation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html

    Parameters
    ----------

    linearAttenuation : float
      Passed on as it is.
    """
    #  void Qt3DRender::QSpotLight::linearAttenuationChanged(float
    #      linearAttenuation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight24linearAttenuationChangedEf',
        linearAttenuation,
    )

  @overload(float)
  def quadraticAttenuationChanged(self, quadraticAttenuation: float) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QSpotLight::quadraticAttenuationChanged(float
    quadraticAttenuation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html

    Parameters
    ----------

    quadraticAttenuation : float
      Passed on as it is.
    """
    #  void Qt3DRender::QSpotLight::quadraticAttenuationChanged(float
    #      quadraticAttenuation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight27quadraticAttenuationChangedEf',
        quadraticAttenuation,
    )

  @overload(QVector3D)
  def localDirectionChanged(self, localDirection: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::localDirectionChanged(const
    QVector3D &localDirection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#localDirectionChanged

    Parameters
    ----------

    localDirection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::QSpotLight::localDirectionChanged(const QVector3D
    #      &localDirection)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight21localDirectionChangedERK9QVecto'
        'r3D',
        self._valueOf(localDirection),
    )

  @overload(float)
  def cutOffAngleChanged(self, cutOffAngle: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSpotLight::cutOffAngleChanged(float
    cutOffAngle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qspotlight.html#cutOffAngleChanged

    Parameters
    ----------

    cutOffAngle : float
      Passed on as it is.
    """
    #  void Qt3DRender::QSpotLight::cutOffAngleChanged(float cutOffAngle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight18cutOffAngleChangedEf',
        cutOffAngle,
    )

  def d_func(self) -> Optional[Qt3DRender.QSpotLightPrivate]:
    """
    Calls Qt's 'QSpotLightPrivate *Qt3DRender::QSpotLight::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qspotlight.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QSpotLightPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSpotLightPrivate *Qt3DRender::QSpotLight::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QSpotLight6d_funcEv',
    )
    return Qt3DRender.QSpotLightPrivate._cuteAt(address)
