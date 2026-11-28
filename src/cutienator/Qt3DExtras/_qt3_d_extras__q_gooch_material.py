"""
Qt3DExtras::QGoochMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qgoochmaterial.h, Qt 6.12.0. Changes made here are lost.
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


class QGoochMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QGoochMaterial: a plain Python object
  standing in front of one C++ Qt3DExtras::QGoochMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QGoochMaterial is built on Qt's Qt3DRender::QMaterial, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QGoochMaterial that has a ritual and
  that Python can call so far, 24 names in all: 'metaObject', 'tr',
  'diffuse', 'specular', 'cool', 'warm', 'alpha', 'beta', 'shininess',
  'setDiffuse', 'setSpecular', 'setCool', 'setWarm', 'setAlpha', 'setBeta',
  'setShininess', 'diffuseChanged', 'specularChanged', 'coolChanged',
  'warmChanged', 'alphaChanged', 'betaChanged', 'shininessChanged', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QGoochMaterial::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QGoochMaterial::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QGoochMaterial::~QGoochMaterial()': the destructor:
    Python never removes a C++ Qt3DExtras::QGoochMaterial.
  - Qt's 'Qt3DExtras::QGoochMaterial::QGoochMaterial(QGoochMaterialPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QGoochMaterialPrivate *Qt3DExtras::QGoochMaterial::d_func()
    const': takes in Python what 'QGoochMaterialPrivate
    *Qt3DExtras::QGoochMaterial::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QGoochMaterial is created at the first use, not by
    'Qt3DExtras::QGoochMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QGoochMaterial.
  - Qt tells when it has removed the C++ Qt3DExtras::QGoochMaterial. Every
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
    Calls Qt's 'QString Qt3DExtras::QGoochMaterial::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#tr

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
    #  QString Qt3DExtras::QGoochMaterial::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QGoochMaterial'

  #  A C++ Qt3DExtras::QGoochMaterial Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QGoochMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QGoochMaterial::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QGoochMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QGoochMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def diffuse(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QGoochMaterial::diffuse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#diffuse

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QGoochMaterial::diffuse() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QGoochMaterial7diffuseEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def specular(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QGoochMaterial::specular() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#specular

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QGoochMaterial::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QGoochMaterial8specularEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def cool(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QGoochMaterial::cool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#cool

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QGoochMaterial::cool() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QGoochMaterial4coolEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def warm(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QGoochMaterial::warm() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#warm

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QGoochMaterial::warm() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QGoochMaterial4warmEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def alpha(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QGoochMaterial::alpha() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#alpha
    """
    #  float Qt3DExtras::QGoochMaterial::alpha() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QGoochMaterial5alphaEv',
    )

  def beta(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QGoochMaterial::beta() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#beta
    """
    #  float Qt3DExtras::QGoochMaterial::beta() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QGoochMaterial4betaEv',
    )

  def shininess(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QGoochMaterial::shininess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#shininess
    """
    #  float Qt3DExtras::QGoochMaterial::shininess() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QGoochMaterial9shininessEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setDiffuse(self, diffuse: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::setDiffuse(const QColor
    &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#setDiffuse

    Parameters
    ----------

    diffuse : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterial::setDiffuse(const QColor &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial10setDiffuseERK6QColor',
        self._valueOf(diffuse),
    )

  @overload(QColor)
  def setSpecular(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::setSpecular(const QColor
    &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#setSpecular

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterial::setSpecular(const QColor &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial11setSpecularERK6QColor',
        self._valueOf(specular),
    )

  @overload(QColor)
  def setCool(self, cool: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::setCool(const QColor
    &cool)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#setCool

    Parameters
    ----------

    cool : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterial::setCool(const QColor &cool)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial7setCoolERK6QColor',
        self._valueOf(cool),
    )

  @overload(QColor)
  def setWarm(self, warm: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::setWarm(const QColor
    &warm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#setWarm

    Parameters
    ----------

    warm : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterial::setWarm(const QColor &warm)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial7setWarmERK6QColor',
        self._valueOf(warm),
    )

  @overload(float)
  def setAlpha(self, alpha: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::setAlpha(float alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#setAlpha

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QGoochMaterial::setAlpha(float alpha)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial8setAlphaEf', alpha,
    )

  @overload(float)
  def setBeta(self, beta: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::setBeta(float beta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#setBeta

    Parameters
    ----------

    beta : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QGoochMaterial::setBeta(float beta)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial7setBetaEf', beta,
    )

  @overload(float)
  def setShininess(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::setShininess(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#setShininess

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QGoochMaterial::setShininess(float shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial12setShininessEf', shininess,
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
    'Qt3DExtras::QGoochMaterial::QGoochMaterial(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#QGoochMaterial

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QGoochMaterial::QGoochMaterial(Qt3DCore::QNode *parent)
    self._noteCreation(QGoochMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterialC1EPN8Qt3DCore5QNodeE',
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
  def diffuseChanged(self, diffuse: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::diffuseChanged(const QColor
    &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#diffuseChanged

    Parameters
    ----------

    diffuse : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterial::diffuseChanged(const QColor &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial14diffuseChangedERK6QColor',
        self._valueOf(diffuse),
    )

  @overload(QColor)
  def specularChanged(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::specularChanged(const QColor
    &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#specularChanged

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterial::specularChanged(const QColor
    #      &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial15specularChangedERK6QColor',
        self._valueOf(specular),
    )

  @overload(QColor)
  def coolChanged(self, cool: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::coolChanged(const QColor
    &cool)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#coolChanged

    Parameters
    ----------

    cool : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterial::coolChanged(const QColor &cool)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial11coolChangedERK6QColor',
        self._valueOf(cool),
    )

  @overload(QColor)
  def warmChanged(self, warm: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::warmChanged(const QColor
    &warm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#warmChanged

    Parameters
    ----------

    warm : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QGoochMaterial::warmChanged(const QColor &warm)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial11warmChangedERK6QColor',
        self._valueOf(warm),
    )

  @overload(float)
  def alphaChanged(self, alpha: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::alphaChanged(float alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#alphaChanged

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QGoochMaterial::alphaChanged(float alpha)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial12alphaChangedEf', alpha,
    )

  @overload(float)
  def betaChanged(self, beta: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::betaChanged(float beta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#betaChanged

    Parameters
    ----------

    beta : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QGoochMaterial::betaChanged(float beta)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial11betaChangedEf', beta,
    )

  @overload(float)
  def shininessChanged(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QGoochMaterial::shininessChanged(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#shininessChanged

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QGoochMaterial::shininessChanged(float shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial16shininessChangedEf',
        shininess,
    )

  def d_func(self) -> Optional[Qt3DExtras.QGoochMaterialPrivate]:
    """
    Calls Qt's 'QGoochMaterialPrivate *Qt3DExtras::QGoochMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qgoochmaterial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QGoochMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGoochMaterialPrivate *Qt3DExtras::QGoochMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QGoochMaterial6d_funcEv',
    )
    return Qt3DExtras.QGoochMaterialPrivate._cuteAt(address)
