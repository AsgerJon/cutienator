"""
Qt3DExtras::QNormalDiffuseMapMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qnormaldiffusemapmaterial.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNormalDiffuseMapMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QNormalDiffuseMapMaterial: a plain Python
  object standing in front of one C++ Qt3DExtras::QNormalDiffuseMapMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QNormalDiffuseMapMaterial is built on Qt's
  Qt3DRender::QMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QNormalDiffuseMapMaterial that has a
  ritual and that Python can call so far, 21 names in all: 'metaObject',
  'tr', 'ambient', 'specular', 'diffuse', 'normal', 'shininess',
  'textureScale', 'setAmbient', 'setSpecular', 'setDiffuse', 'setNormal',
  'setShininess', 'setTextureScale', 'ambientChanged', 'diffuseChanged',
  'normalChanged', 'specularChanged', 'shininessChanged',
  'textureScaleChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QNormalDiffuseMapMaterial::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::QNormalDiffuseMapMaterial::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DExtras::QNormalDiffuseMapMaterial::~QNormalDiffuseMapMaterial()':
    the destructor: Python never removes a C++
    Qt3DExtras::QNormalDiffuseMapMaterial.
  - Qt's 'Qt3DExtras::QNormalDiffuseMapMaterial::QNormalDiffuseMapMaterial(
    QNormalDiffuseMapMaterialPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QNormalDiffuseMapMaterialPrivate
    *Qt3DExtras::QNormalDiffuseMapMaterial::d_func() const': takes in Python
    what 'QNormalDiffuseMapMaterialPrivate
    *Qt3DExtras::QNormalDiffuseMapMaterial::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QNormalDiffuseMapMaterial is created at the first
    use, not by 'Qt3DExtras::QNormalDiffuseMapMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QNormalDiffuseMapMaterial.
  - Qt tells when it has removed the C++
    Qt3DExtras::QNormalDiffuseMapMaterial. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
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
    Calls Qt's 'QString Qt3DExtras::QNormalDiffuseMapMaterial::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html#tr

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
    #  QString Qt3DExtras::QNormalDiffuseMapMaterial::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QNormalDiffuseMapMaterial'

  #  A C++ Qt3DExtras::QNormalDiffuseMapMaterial Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QNormalDiffuseMapMaterial'

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
    *Qt3DExtras::QNormalDiffuseMapMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QNormalDiffuseMapMaterial::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ambient(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QNormalDiffuseMapMaterial::ambient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html#ambient

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QNormalDiffuseMapMaterial::ambient() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial7ambientEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def specular(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QNormalDiffuseMapMaterial::specular()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html#specular

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QNormalDiffuseMapMaterial::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial8specularEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def diffuse(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DExtras::QNormalDiffuseMapMaterial::diffuse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html#diffuse

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DExtras::QNormalDiffuseMapMaterial::diffuse() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial7diffuseEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def normal(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DExtras::QNormalDiffuseMapMaterial::normal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html#normal

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DExtras::QNormalDiffuseMapMaterial::normal() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial6normalEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def shininess(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QNormalDiffuseMapMaterial::shininess()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html
    """
    #  float Qt3DExtras::QNormalDiffuseMapMaterial::shininess() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial9shininessEv',
    )

  def textureScale(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QNormalDiffuseMapMaterial::textureScale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html
    """
    #  float Qt3DExtras::QNormalDiffuseMapMaterial::textureScale() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras25QNormalDiffuseMapMaterial12textureScaleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setAmbient(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QNormalDiffuseMapMaterial::setAmbient(const
    QColor &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::setAmbient(const QColor
    #      &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial10setAmbientERK6QC'
        'olor',
        self._valueOf(ambient),
    )

  @overload(QColor)
  def setSpecular(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QNormalDiffuseMapMaterial::setSpecular(const
    QColor &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::setSpecular(const QColor
    #      &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial11setSpecularERK6Q'
        'Color',
        self._valueOf(specular),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setDiffuse(
      self,
      diffuse: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::setDiffuse(Qt3DRender::
    QAbstractTexture *diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    diffuse : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::setDiffuse(Qt3DRender::
    #      QAbstractTexture *diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial10setDiffuseEPN10Q'
        't3DRender16QAbstractTextureE',
        self._addressOf(diffuse),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setNormal(self, normal: Optional[Qt3DRender.QAbstractTexture]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::setNormal(Qt3DRender::
    QAbstractTexture *normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    normal : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::setNormal(Qt3DRender::
    #      QAbstractTexture *normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial9setNormalEPN10Qt3'
        'DRender16QAbstractTextureE',
        self._addressOf(normal),
    )

  @overload(float)
  def setShininess(self, shininess: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::setShininess(float shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::setShininess(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial12setShininessEf',
        shininess,
    )

  @overload(float)
  def setTextureScale(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::setTextureScale(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::setTextureScale(float
    #      textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial15setTextureScaleE'
        'f',
        textureScale,
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
    'Qt3DExtras::QNormalDiffuseMapMaterial::QNormalDiffuseMapMaterial(
    Qt3DCore::QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QNormalDiffuseMapMaterial::QNormalDiffuseMapMaterial(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QNormalDiffuseMapMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterialC1EPN8Qt3DCore5QNo'
        'deE',
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

  @overload(QColor)
  def ambientChanged(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::ambientChanged(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::ambientChanged(const
    #      QColor &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial14ambientChangedER'
        'K6QColor',
        self._valueOf(ambient),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def diffuseChanged(
      self,
      diffuse: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::diffuseChanged(Qt3DRender::
    QAbstractTexture *diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    diffuse : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::diffuseChanged(
    #      Qt3DRender::QAbstractTexture *diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial14diffuseChangedEP'
        'N10Qt3DRender16QAbstractTextureE',
        self._addressOf(diffuse),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def normalChanged(
      self,
      normal: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::normalChanged(Qt3DRender::
    QAbstractTexture *normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    normal : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::normalChanged(Qt3DRender::
    #      QAbstractTexture *normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial13normalChangedEPN'
        '10Qt3DRender16QAbstractTextureE',
        self._addressOf(normal),
    )

  @overload(QColor)
  def specularChanged(self, specular: QColor) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::specularChanged(const QColor
    &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::specularChanged(const
    #      QColor &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial15specularChangedE'
        'RK6QColor',
        self._valueOf(specular),
    )

  @overload(float)
  def shininessChanged(self, shininess: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::shininessChanged(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::shininessChanged(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial16shininessChanged'
        'Ef',
        shininess,
    )

  @overload(float)
  def textureScaleChanged(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseMapMaterial::textureScaleChanged(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QNormalDiffuseMapMaterial::textureScaleChanged(float
    #      textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial19textureScaleChan'
        'gedEf',
        textureScale,
    )

  def d_func(self) -> Optional[Qt3DExtras.QNormalDiffuseMapMaterialPrivate]:
    """
    Calls Qt's 'QNormalDiffuseMapMaterialPrivate
    *Qt3DExtras::QNormalDiffuseMapMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusemapmaterial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QNormalDiffuseMapMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNormalDiffuseMapMaterialPrivate
    #      *Qt3DExtras::QNormalDiffuseMapMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras25QNormalDiffuseMapMaterial6d_funcEv',
    )
    return Qt3DExtras.QNormalDiffuseMapMaterialPrivate._cuteAt(address)
