"""
Qt3DRender::QPointLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qpointlight.h, Qt 6.12.0. Changes made here are lost.
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPointLight(Qt3DRender.QAbstractLight):
  """
  The cute side of Qt's Qt3DRender::QPointLight: a plain Python object
  standing in front of one C++ Qt3DRender::QPointLight.

  It is built on the cute 'Qt3DRender::QAbstractLight', as Qt's
  Qt3DRender::QPointLight is built on Qt's Qt3DRender::QAbstractLight, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QPointLight that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr',
  'constantAttenuation', 'linearAttenuation', 'quadraticAttenuation',
  'setConstantAttenuation', 'setLinearAttenuation',
  'setQuadraticAttenuation', 'constantAttenuationChanged',
  'linearAttenuationChanged', 'quadraticAttenuationChanged', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QPointLight::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QPointLight::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QPointLight::~QPointLight()': the destructor: Python
    never removes a C++ Qt3DRender::QPointLight.
  - Qt's 'const QPointLightPrivate *Qt3DRender::QPointLight::d_func() const':
    takes in Python what 'QPointLightPrivate
    *Qt3DRender::QPointLight::d_func()' takes.
  - Qt's 'Qt3DRender::QPointLight::QPointLight(QPointLightPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QPointLight is created at the first use, not by
    'Qt3DRender::QPointLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QPointLight.
  - Qt tells when it has removed the C++ Qt3DRender::QPointLight. Every call
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
    Calls Qt's 'QString Qt3DRender::QPointLight::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qpointlight.html#tr

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
    #  QString Qt3DRender::QPointLight::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender11QPointLight2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QPointLight'

  #  A C++ Qt3DRender::QPointLight Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QPointLight'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QPointLight::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QPointLight::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QPointLight10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def constantAttenuation(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QPointLight::constantAttenuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html#constantAttenuation
    """
    #  float Qt3DRender::QPointLight::constantAttenuation() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QPointLight19constantAttenuationEv',
    )

  def linearAttenuation(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QPointLight::linearAttenuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html#linearAttenuation
    """
    #  float Qt3DRender::QPointLight::linearAttenuation() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QPointLight17linearAttenuationEv',
    )

  def quadraticAttenuation(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QPointLight::quadraticAttenuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html#quadraticAttenuation
    """
    #  float Qt3DRender::QPointLight::quadraticAttenuation() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QPointLight20quadraticAttenuationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setConstantAttenuation(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPointLight::setConstantAttenuation(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html#setConstantAttenuation

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DRender::QPointLight::setConstantAttenuation(float value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QPointLight22setConstantAttenuationEf',
        value,
    )

  @overload(float)
  def setLinearAttenuation(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPointLight::setLinearAttenuation(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html#setLinearAttenuation

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DRender::QPointLight::setLinearAttenuation(float value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QPointLight20setLinearAttenuationEf', value,
    )

  @overload(float)
  def setQuadraticAttenuation(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPointLight::setQuadraticAttenuation(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DRender::QPointLight::setQuadraticAttenuation(float value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QPointLight23setQuadraticAttenuationEf',
        value,
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
    'Qt3DRender::QPointLight::QPointLight(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html#QPointLight

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QPointLight::QPointLight(Qt3DCore::QNode *parent)
    self._noteCreation(QPointLight, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender11QPointLightC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void
    Qt3DRender::QPointLight::constantAttenuationChanged(float
    constantAttenuation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html

    Parameters
    ----------

    constantAttenuation : float
      Passed on as it is.
    """
    #  void Qt3DRender::QPointLight::constantAttenuationChanged(float
    #      constantAttenuation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QPointLight26constantAttenuationChangedEf',
        constantAttenuation,
    )

  @overload(float)
  def linearAttenuationChanged(self, linearAttenuation: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QPointLight::linearAttenuationChanged(float
    linearAttenuation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html

    Parameters
    ----------

    linearAttenuation : float
      Passed on as it is.
    """
    #  void Qt3DRender::QPointLight::linearAttenuationChanged(float
    #      linearAttenuation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QPointLight24linearAttenuationChangedEf',
        linearAttenuation,
    )

  @overload(float)
  def quadraticAttenuationChanged(self, quadraticAttenuation: float) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QPointLight::quadraticAttenuationChanged(float
    quadraticAttenuation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qpointlight.html

    Parameters
    ----------

    quadraticAttenuation : float
      Passed on as it is.
    """
    #  void Qt3DRender::QPointLight::quadraticAttenuationChanged(float
    #      quadraticAttenuation)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QPointLight27quadraticAttenuationChangedEf',
        quadraticAttenuation,
    )

  def d_func(self) -> Optional[Qt3DRender.QPointLightPrivate]:
    """
    Calls Qt's 'QPointLightPrivate *Qt3DRender::QPointLight::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qpointlight.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QPointLightPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPointLightPrivate *Qt3DRender::QPointLight::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender11QPointLight6d_funcEv',
    )
    return Qt3DRender.QPointLightPrivate._cuteAt(address)
