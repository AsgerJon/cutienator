"""
Qt3DExtras::QDiffuseSpecularMapMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qdiffusespecularmapmaterial.h, Qt 6.12.0. Changes made here are
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


class QDiffuseSpecularMapMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QDiffuseSpecularMapMaterial: a plain
  Python object standing in front of one C++
  Qt3DExtras::QDiffuseSpecularMapMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QDiffuseSpecularMapMaterial is built on Qt's
  Qt3DRender::QMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QDiffuseSpecularMapMaterial that has a
  ritual and that Python can call so far, 18 names in all: 'metaObject',
  'tr', 'ambient', 'diffuse', 'specular', 'shininess', 'textureScale',
  'setAmbient', 'setDiffuse', 'setSpecular', 'setShininess',
  'setTextureScale', 'ambientChanged', 'diffuseChanged', 'specularChanged',
  'shininessChanged', 'textureScaleChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QDiffuseSpecularMapMaterial::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::QDiffuseSpecularMapMaterial::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DExtras::QDiffuseSpecularMapMaterial::~QDiffuseSpecularMapMaterial(
    )': the destructor: Python never removes a C++
    Qt3DExtras::QDiffuseSpecularMapMaterial.
  - Qt's 'const QDiffuseSpecularMapMaterialPrivate
    *Qt3DExtras::QDiffuseSpecularMapMaterial::d_func() const': takes in
    Python what 'QDiffuseSpecularMapMaterialPrivate
    *Qt3DExtras::QDiffuseSpecularMapMaterial::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QDiffuseSpecularMapMaterial is created at the first
    use, not by 'Qt3DExtras::QDiffuseSpecularMapMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QDiffuseSpecularMapMaterial.
  - Qt tells when it has removed the C++
    Qt3DExtras::QDiffuseSpecularMapMaterial. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString Qt3DExtras::QDiffuseSpecularMapMaterial::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html#tr

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
    #  QString Qt3DExtras::QDiffuseSpecularMapMaterial::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QDiffuseSpecularMapMaterial'

  #  A C++ Qt3DExtras::QDiffuseSpecularMapMaterial Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QDiffuseSpecularMapMaterial'

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
    *Qt3DExtras::QDiffuseSpecularMapMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DExtras::QDiffuseSpecularMapMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras27QDiffuseSpecularMapMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ambient(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QDiffuseSpecularMapMaterial::ambient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QDiffuseSpecularMapMaterial::ambient() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras27QDiffuseSpecularMapMaterial7ambientEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def diffuse(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DExtras::QDiffuseSpecularMapMaterial::diffuse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DExtras::QDiffuseSpecularMapMaterial::diffuse() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras27QDiffuseSpecularMapMaterial7diffuseEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def specular(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DExtras::QDiffuseSpecularMapMaterial::specular() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DExtras::QDiffuseSpecularMapMaterial::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras27QDiffuseSpecularMapMaterial8specularEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def shininess(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QDiffuseSpecularMapMaterial::shininess()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html
    """
    #  float Qt3DExtras::QDiffuseSpecularMapMaterial::shininess() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras27QDiffuseSpecularMapMaterial9shininessEv',
    )

  def textureScale(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QDiffuseSpecularMapMaterial::textureScale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html
    """
    #  float Qt3DExtras::QDiffuseSpecularMapMaterial::textureScale() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras27QDiffuseSpecularMapMaterial12textureScaleE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setAmbient(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMapMaterial::setAmbient(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::setAmbient(const QColor
    #      &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial10setAmbientERK6'
        'QColor',
        self._valueOf(ambient),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setDiffuse(
      self,
      diffuse: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMapMaterial::setDiffuse(Qt3DRender::
    QAbstractTexture *diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    diffuse : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::setDiffuse(Qt3DRender::
    #      QAbstractTexture *diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial10setDiffuseEPN1'
        '0Qt3DRender16QAbstractTextureE',
        self._addressOf(diffuse),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setSpecular(
      self,
      specular: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMapMaterial::setSpecular(Qt3DRender::
    QAbstractTexture *specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    specular : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::setSpecular(Qt3DRender::
    #      QAbstractTexture *specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial11setSpecularEPN'
        '10Qt3DRender16QAbstractTextureE',
        self._addressOf(specular),
    )

  @overload(float)
  def setShininess(self, shininess: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMapMaterial::setShininess(float shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::setShininess(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial12setShininessEf',
        shininess,
    )

  @overload(float)
  def setTextureScale(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMapMaterial::setTextureScale(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::setTextureScale(float
    #      textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial15setTextureScal'
        'eEf',
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
    'Qt3DExtras::QDiffuseSpecularMapMaterial::QDiffuseSpecularMapMaterial(
    Qt3DCore::QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QDiffuseSpecularMapMaterial::
    #      QDiffuseSpecularMapMaterial(Qt3DCore::QNode *parent)
    self._noteCreation(QDiffuseSpecularMapMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterialC1EPN8Qt3DCore5Q'
        'NodeE',
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
    Qt3DExtras::QDiffuseSpecularMapMaterial::ambientChanged(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::ambientChanged(const
    #      QColor &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial14ambientChanged'
        'ERK6QColor',
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
    Qt3DExtras::QDiffuseSpecularMapMaterial::diffuseChanged(Qt3DRender::
    QAbstractTexture *diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    diffuse : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::diffuseChanged(
    #      Qt3DRender::QAbstractTexture *diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial14diffuseChanged'
        'EPN10Qt3DRender16QAbstractTextureE',
        self._addressOf(diffuse),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def specularChanged(
      self,
      specular: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMapMaterial::specularChanged(Qt3DRender::
    QAbstractTexture *specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    specular : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::specularChanged(
    #      Qt3DRender::QAbstractTexture *specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial15specularChange'
        'dEPN10Qt3DRender16QAbstractTextureE',
        self._addressOf(specular),
    )

  @overload(float)
  def shininessChanged(self, shininess: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMapMaterial::shininessChanged(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QDiffuseSpecularMapMaterial::shininessChanged(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial16shininessChang'
        'edEf',
        shininess,
    )

  @overload(float)
  def textureScaleChanged(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMapMaterial::textureScaleChanged(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void
    #      Qt3DExtras::QDiffuseSpecularMapMaterial::textureScaleChanged(float
    #      textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial19textureScaleCh'
        'angedEf',
        textureScale,
    )

  def d_func(
      self,
  ) -> Optional[Qt3DExtras.QDiffuseSpecularMapMaterialPrivate]:
    """
    Calls Qt's 'QDiffuseSpecularMapMaterialPrivate
    *Qt3DExtras::QDiffuseSpecularMapMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmapmaterial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QDiffuseSpecularMapMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDiffuseSpecularMapMaterialPrivate
    #      *Qt3DExtras::QDiffuseSpecularMapMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial6d_funcEv',
    )
    return Qt3DExtras.QDiffuseSpecularMapMaterialPrivate._cuteAt(address)
