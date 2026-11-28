"""
Qt3DRender::QEnvironmentLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qenvironmentlight.h, Qt 6.12.0. Changes made here are lost.
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


class QEnvironmentLight(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QEnvironmentLight: a plain Python object
  standing in front of one C++ Qt3DRender::QEnvironmentLight.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QEnvironmentLight is built on Qt's Qt3DCore::QComponent, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QEnvironmentLight that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'irradiance', 'specular', 'setIrradiance', 'setSpecular',
  'irradianceChanged', 'specularChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QEnvironmentLight::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QEnvironmentLight::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QEnvironmentLight::~QEnvironmentLight()': the
    destructor: Python never removes a C++ Qt3DRender::QEnvironmentLight.
  - Qt's 'Qt3DRender::QEnvironmentLight::QEnvironmentLight(
    QEnvironmentLightPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QEnvironmentLightPrivate
    *Qt3DRender::QEnvironmentLight::d_func() const': takes in Python what
    'QEnvironmentLightPrivate *Qt3DRender::QEnvironmentLight::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QEnvironmentLight is created at the first use, not by
    'Qt3DRender::QEnvironmentLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QEnvironmentLight.
  - Qt tells when it has removed the C++ Qt3DRender::QEnvironmentLight. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DRender::QEnvironmentLight::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html#tr

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
    #  QString Qt3DRender::QEnvironmentLight::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender17QEnvironmentLight2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QEnvironmentLight'

  #  A C++ Qt3DRender::QEnvironmentLight Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QEnvironmentLight'

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
    *Qt3DRender::QEnvironmentLight::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QEnvironmentLight::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QEnvironmentLight10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def irradiance(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DRender::QEnvironmentLight::irradiance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html#irradiance

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DRender::QEnvironmentLight::irradiance() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QEnvironmentLight10irradianceEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def specular(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DRender::QEnvironmentLight::specular() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html#specular

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DRender::QEnvironmentLight::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17QEnvironmentLight8specularEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setIrradiance(
      self,
      irradiance: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QEnvironmentLight::setIrradiance(Qt3DRender::QAbstractTexture
    *irradiance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html#setIrradiance

    Parameters
    ----------

    irradiance : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QEnvironmentLight::setIrradiance(Qt3DRender::
    #      QAbstractTexture *irradiance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QEnvironmentLight13setIrradianceEPNS_16QAbs'
        'tractTextureE',
        self._addressOf(irradiance),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setSpecular(
      self,
      specular: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QEnvironmentLight::setSpecular(Qt3DRender::QAbstractTexture
    *specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html#setSpecular

    Parameters
    ----------

    specular : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QEnvironmentLight::setSpecular(Qt3DRender::
    #      QAbstractTexture *specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QEnvironmentLight11setSpecularEPNS_16QAbstr'
        'actTextureE',
        self._addressOf(specular),
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
    'Qt3DRender::QEnvironmentLight::QEnvironmentLight(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QEnvironmentLight::QEnvironmentLight(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QEnvironmentLight, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender17QEnvironmentLightC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def irradianceChanged(
      self,
      environmentIrradiance: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QEnvironmentLight::irradianceChanged(Qt3DRender::
    QAbstractTexture *environmentIrradiance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html

    Parameters
    ----------

    environmentIrradiance : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QEnvironmentLight::irradianceChanged(Qt3DRender::
    #      QAbstractTexture *environmentIrradiance)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QEnvironmentLight17irradianceChangedEPNS_16'
        'QAbstractTextureE',
        self._addressOf(environmentIrradiance),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def specularChanged(
      self,
      environmentSpecular: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QEnvironmentLight::specularChanged(Qt3DRender::
    QAbstractTexture *environmentSpecular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html#specularChanged

    Parameters
    ----------

    environmentSpecular : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QEnvironmentLight::specularChanged(Qt3DRender::
    #      QAbstractTexture *environmentSpecular)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17QEnvironmentLight15specularChangedEPNS_16QA'
        'bstractTextureE',
        self._addressOf(environmentSpecular),
    )

  def d_func(self) -> Optional[Qt3DRender.QEnvironmentLightPrivate]:
    """
    Calls Qt's 'QEnvironmentLightPrivate
    *Qt3DRender::QEnvironmentLight::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qenvironmentlight.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QEnvironmentLightPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QEnvironmentLightPrivate *Qt3DRender::QEnvironmentLight::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender17QEnvironmentLight6d_funcEv',
    )
    return Qt3DRender.QEnvironmentLightPrivate._cuteAt(address)
