"""
Qt3DExtras::QDiffuseSpecularMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qdiffusespecularmaterial.h, Qt 6.12.0. Changes made here are
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

  from ..QtCore import QMetaObject, QVariant
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDiffuseSpecularMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QDiffuseSpecularMaterial: a plain Python
  object standing in front of one C++ Qt3DExtras::QDiffuseSpecularMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QDiffuseSpecularMaterial is built on Qt's
  Qt3DRender::QMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QDiffuseSpecularMaterial that has a
  ritual and that Python can call so far, 24 names in all: 'metaObject',
  'tr', 'ambient', 'diffuse', 'specular', 'shininess', 'normal',
  'textureScale', 'isAlphaBlendingEnabled', 'setAmbient', 'setDiffuse',
  'setSpecular', 'setShininess', 'setNormal', 'setTextureScale',
  'setAlphaBlendingEnabled', 'ambientChanged', 'diffuseChanged',
  'specularChanged', 'shininessChanged', 'normalChanged',
  'textureScaleChanged', 'alphaBlendingEnabledChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QDiffuseSpecularMaterial::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::QDiffuseSpecularMaterial::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QDiffuseSpecularMaterial::~QDiffuseSpecularMaterial()':
    the destructor: Python never removes a C++
    Qt3DExtras::QDiffuseSpecularMaterial.
  - Qt's 'const QDiffuseSpecularMaterialPrivate
    *Qt3DExtras::QDiffuseSpecularMaterial::d_func() const': takes in Python
    what 'QDiffuseSpecularMaterialPrivate
    *Qt3DExtras::QDiffuseSpecularMaterial::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QDiffuseSpecularMaterial is created at the first use,
    not by 'Qt3DExtras::QDiffuseSpecularMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QDiffuseSpecularMaterial.
  - Qt tells when it has removed the C++
    Qt3DExtras::QDiffuseSpecularMaterial. Every call on the cute object, and
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
    Calls Qt's 'QString Qt3DExtras::QDiffuseSpecularMaterial::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html#tr

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
    #  QString Qt3DExtras::QDiffuseSpecularMaterial::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QDiffuseSpecularMaterial'

  #  A C++ Qt3DExtras::QDiffuseSpecularMaterial Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QDiffuseSpecularMaterial'

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
    *Qt3DExtras::QDiffuseSpecularMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QDiffuseSpecularMaterial::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ambient(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QDiffuseSpecularMaterial::ambient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html#ambient

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QDiffuseSpecularMaterial::ambient() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial7ambientEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def diffuse(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DExtras::QDiffuseSpecularMaterial::diffuse()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html#diffuse

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DExtras::QDiffuseSpecularMaterial::diffuse() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial7diffuseEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def specular(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DExtras::QDiffuseSpecularMaterial::specular()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html#specular

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DExtras::QDiffuseSpecularMaterial::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial8specularEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def shininess(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QDiffuseSpecularMaterial::shininess()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html#shininess
    """
    #  float Qt3DExtras::QDiffuseSpecularMaterial::shininess() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial9shininessEv',
    )

  def normal(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DExtras::QDiffuseSpecularMaterial::normal()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html#normal

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DExtras::QDiffuseSpecularMaterial::normal() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial6normalEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def textureScale(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QDiffuseSpecularMaterial::textureScale()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html
    """
    #  float Qt3DExtras::QDiffuseSpecularMaterial::textureScale() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial12textureScaleEv',
    )

  def isAlphaBlendingEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DExtras::QDiffuseSpecularMaterial::isAlphaBlendingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html
    """
    #  bool Qt3DExtras::QDiffuseSpecularMaterial::isAlphaBlendingEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras24QDiffuseSpecularMaterial22isAlphaBlendingE'
        'nabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setAmbient(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QDiffuseSpecularMaterial::setAmbient(const
    QColor &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::setAmbient(const QColor
    #      &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial10setAmbientERK6QCo'
        'lor',
        self._valueOf(ambient),
    )

  @overload(QVariant)
  def setDiffuse(self, diffuse: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QDiffuseSpecularMaterial::setDiffuse(const
    QVariant &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    diffuse : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::setDiffuse(const QVariant
    #      &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial10setDiffuseERK8QVa'
        'riant',
        self._valueOf(diffuse),
    )

  @overload(QVariant)
  def setSpecular(self, specular: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QDiffuseSpecularMaterial::setSpecular(const
    QVariant &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    specular : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::setSpecular(const QVariant
    #      &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial11setSpecularERK8QV'
        'ariant',
        self._valueOf(specular),
    )

  @overload(float)
  def setShininess(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QDiffuseSpecularMaterial::setShininess(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::setShininess(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial12setShininessEf',
        shininess,
    )

  @overload(QVariant)
  def setNormal(self, normal: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QDiffuseSpecularMaterial::setNormal(const
    QVariant &normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html#setNormal

    Parameters
    ----------

    normal : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::setNormal(const QVariant
    #      &normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial9setNormalERK8QVari'
        'ant',
        self._valueOf(normal),
    )

  @overload(float)
  def setTextureScale(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMaterial::setTextureScale(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::setTextureScale(float
    #      textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial15setTextureScaleEf',
        textureScale,
    )

  @overload(bool)
  def setAlphaBlendingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMaterial::setAlphaBlendingEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void
    #      Qt3DExtras::QDiffuseSpecularMaterial::setAlphaBlendingEnabled(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial23setAlphaBlendingE'
        'nabledEb',
        enabled,
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
    'Qt3DExtras::QDiffuseSpecularMaterial::QDiffuseSpecularMaterial(
    Qt3DCore::QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QDiffuseSpecularMaterial::QDiffuseSpecularMaterial(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QDiffuseSpecularMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterialC1EPN8Qt3DCore5QNod'
        'eE',
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
    Qt3DExtras::QDiffuseSpecularMaterial::ambientChanged(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::ambientChanged(const QColor
    #      &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial14ambientChangedERK'
        '6QColor',
        self._valueOf(ambient),
    )

  @overload(QVariant)
  def diffuseChanged(self, diffuse: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMaterial::diffuseChanged(const QVariant
    &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    diffuse : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::diffuseChanged(const
    #      QVariant &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial14diffuseChangedERK'
        '8QVariant',
        self._valueOf(diffuse),
    )

  @overload(QVariant)
  def specularChanged(self, specular: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMaterial::specularChanged(const QVariant
    &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    specular : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::specularChanged(const
    #      QVariant &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial15specularChangedER'
        'K8QVariant',
        self._valueOf(specular),
    )

  @overload(float)
  def shininessChanged(self, shininess: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMaterial::shininessChanged(float shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::shininessChanged(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial16shininessChangedE'
        'f',
        shininess,
    )

  @overload(QVariant)
  def normalChanged(self, normal: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMaterial::normalChanged(const QVariant
    &normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    normal : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::normalChanged(const
    #      QVariant &normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial13normalChangedERK8'
        'QVariant',
        self._valueOf(normal),
    )

  @overload(float)
  def textureScaleChanged(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMaterial::textureScaleChanged(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QDiffuseSpecularMaterial::textureScaleChanged(float
    #      textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial19textureScaleChang'
        'edEf',
        textureScale,
    )

  @overload(bool)
  def alphaBlendingEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QDiffuseSpecularMaterial::alphaBlendingEnabledChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void
    #      Qt3DExtras::QDiffuseSpecularMaterial::alphaBlendingEnabledChanged(
    #      bool enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial27alphaBlendingEnab'
        'ledChangedEb',
        enabled,
    )

  def d_func(self) -> Optional[Qt3DExtras.QDiffuseSpecularMaterialPrivate]:
    """
    Calls Qt's 'QDiffuseSpecularMaterialPrivate
    *Qt3DExtras::QDiffuseSpecularMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qdiffusespecularmaterial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QDiffuseSpecularMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDiffuseSpecularMaterialPrivate
    #      *Qt3DExtras::QDiffuseSpecularMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QDiffuseSpecularMaterial6d_funcEv',
    )
    return Qt3DExtras.QDiffuseSpecularMaterialPrivate._cuteAt(address)
