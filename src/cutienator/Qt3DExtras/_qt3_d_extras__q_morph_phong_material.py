"""
Qt3DExtras::QMorphPhongMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qmorphphongmaterial.h, Qt 6.12.0. Changes made here are lost.
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


class QMorphPhongMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QMorphPhongMaterial: a plain Python
  object standing in front of one C++ Qt3DExtras::QMorphPhongMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QMorphPhongMaterial is built on Qt's Qt3DRender::QMaterial, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QMorphPhongMaterial that has a ritual
  and that Python can call so far, 18 names in all: 'metaObject', 'tr',
  'ambient', 'diffuse', 'specular', 'shininess', 'interpolator',
  'setAmbient', 'setDiffuse', 'setSpecular', 'setShininess',
  'setInterpolator', 'ambientChanged', 'diffuseChanged', 'specularChanged',
  'shininessChanged', 'interpolatorChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QMorphPhongMaterial::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QMorphPhongMaterial::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QMorphPhongMaterial::~QMorphPhongMaterial()': the
    destructor: Python never removes a C++ Qt3DExtras::QMorphPhongMaterial.
  - Qt's 'const QMorphPhongMaterialPrivate
    *Qt3DExtras::QMorphPhongMaterial::d_func() const': takes in Python what
    'QMorphPhongMaterialPrivate *Qt3DExtras::QMorphPhongMaterial::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QMorphPhongMaterial is created at the first use, not
    by 'Qt3DExtras::QMorphPhongMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QMorphPhongMaterial.
  - Qt tells when it has removed the C++ Qt3DExtras::QMorphPhongMaterial.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DExtras::QMorphPhongMaterial::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#tr

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
    #  QString Qt3DExtras::QMorphPhongMaterial::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QMorphPhongMaterial'

  #  A C++ Qt3DExtras::QMorphPhongMaterial Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QMorphPhongMaterial'

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
    *Qt3DExtras::QMorphPhongMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QMorphPhongMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMorphPhongMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ambient(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QMorphPhongMaterial::ambient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#ambient

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QMorphPhongMaterial::ambient() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMorphPhongMaterial7ambientEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def diffuse(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QMorphPhongMaterial::diffuse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#diffuse

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QMorphPhongMaterial::diffuse() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMorphPhongMaterial7diffuseEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def specular(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QMorphPhongMaterial::specular() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#specular

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QMorphPhongMaterial::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMorphPhongMaterial8specularEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shininess(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QMorphPhongMaterial::shininess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#shininess
    """
    #  float Qt3DExtras::QMorphPhongMaterial::shininess() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMorphPhongMaterial9shininessEv',
    )

  def interpolator(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QMorphPhongMaterial::interpolator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#interpolator
    """
    #  float Qt3DExtras::QMorphPhongMaterial::interpolator() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMorphPhongMaterial12interpolatorEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setAmbient(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::setAmbient(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#setAmbient

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::setAmbient(const QColor
    #      &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial10setAmbientERK6QColor',
        self._valueOf(ambient),
    )

  @overload(QColor)
  def setDiffuse(self, diffuse: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::setDiffuse(const QColor
    &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#setDiffuse

    Parameters
    ----------

    diffuse : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::setDiffuse(const QColor
    #      &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial10setDiffuseERK6QColor',
        self._valueOf(diffuse),
    )

  @overload(QColor)
  def setSpecular(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::setSpecular(const
    QColor &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#setSpecular

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::setSpecular(const QColor
    #      &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial11setSpecularERK6QColor',
        self._valueOf(specular),
    )

  @overload(float)
  def setShininess(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::setShininess(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#setShininess

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::setShininess(float shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial12setShininessEf',
        shininess,
    )

  @overload(float)
  def setInterpolator(self, interpolator: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::setInterpolator(float
    interpolator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html

    Parameters
    ----------

    interpolator : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::setInterpolator(float
    #      interpolator)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial15setInterpolatorEf',
        interpolator,
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
    'Qt3DExtras::QMorphPhongMaterial::QMorphPhongMaterial(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QMorphPhongMaterial::QMorphPhongMaterial(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QMorphPhongMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterialC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::ambientChanged(const
    QColor &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#ambientChanged

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::ambientChanged(const QColor
    #      &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial14ambientChangedERK6QCol'
        'or',
        self._valueOf(ambient),
    )

  @overload(QColor)
  def diffuseChanged(self, diffuse: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::diffuseChanged(const
    QColor &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#diffuseChanged

    Parameters
    ----------

    diffuse : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::diffuseChanged(const QColor
    #      &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial14diffuseChangedERK6QCol'
        'or',
        self._valueOf(diffuse),
    )

  @overload(QColor)
  def specularChanged(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::specularChanged(const
    QColor &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::specularChanged(const QColor
    #      &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial15specularChangedERK6QCo'
        'lor',
        self._valueOf(specular),
    )

  @overload(float)
  def shininessChanged(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMorphPhongMaterial::shininessChanged(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::shininessChanged(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial16shininessChangedEf',
        shininess,
    )

  @overload(float)
  def interpolatorChanged(self, interpolator: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMorphPhongMaterial::interpolatorChanged(float
    interpolator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html

    Parameters
    ----------

    interpolator : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QMorphPhongMaterial::interpolatorChanged(float
    #      interpolator)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial19interpolatorChangedEf',
        interpolator,
    )

  def d_func(self) -> Optional[Qt3DExtras.QMorphPhongMaterialPrivate]:
    """
    Calls Qt's 'QMorphPhongMaterialPrivate
    *Qt3DExtras::QMorphPhongMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmorphphongmaterial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QMorphPhongMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMorphPhongMaterialPrivate *Qt3DExtras::QMorphPhongMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMorphPhongMaterial6d_funcEv',
    )
    return Qt3DExtras.QMorphPhongMaterialPrivate._cuteAt(address)
