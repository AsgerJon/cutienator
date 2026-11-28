"""
Qt3DExtras::QPhongMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qphongmaterial.h, Qt 6.12.0. Changes made here are lost.
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


class QPhongMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QPhongMaterial: a plain Python object
  standing in front of one C++ Qt3DExtras::QPhongMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QPhongMaterial is built on Qt's Qt3DRender::QMaterial, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QPhongMaterial that has a ritual and
  that Python can call so far, 15 names in all: 'metaObject', 'tr',
  'ambient', 'diffuse', 'specular', 'shininess', 'setAmbient', 'setDiffuse',
  'setSpecular', 'setShininess', 'ambientChanged', 'diffuseChanged',
  'specularChanged', 'shininessChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QPhongMaterial::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QPhongMaterial::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QPhongMaterial::~QPhongMaterial()': the destructor:
    Python never removes a C++ Qt3DExtras::QPhongMaterial.
  - Qt's 'const QPhongMaterialPrivate *Qt3DExtras::QPhongMaterial::d_func()
    const': takes in Python what 'QPhongMaterialPrivate
    *Qt3DExtras::QPhongMaterial::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QPhongMaterial is created at the first use, not by
    'Qt3DExtras::QPhongMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QPhongMaterial.
  - Qt tells when it has removed the C++ Qt3DExtras::QPhongMaterial. Every
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
    Calls Qt's 'QString Qt3DExtras::QPhongMaterial::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#tr

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
    #  QString Qt3DExtras::QPhongMaterial::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QPhongMaterial'

  #  A C++ Qt3DExtras::QPhongMaterial Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QPhongMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QPhongMaterial::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QPhongMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPhongMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ambient(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QPhongMaterial::ambient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#ambient

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QPhongMaterial::ambient() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPhongMaterial7ambientEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def diffuse(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QPhongMaterial::diffuse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#diffuse

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QPhongMaterial::diffuse() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPhongMaterial7diffuseEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def specular(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DExtras::QPhongMaterial::specular() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#specular

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QPhongMaterial::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPhongMaterial8specularEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def shininess(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QPhongMaterial::shininess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#shininess
    """
    #  float Qt3DExtras::QPhongMaterial::shininess() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras14QPhongMaterial9shininessEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setAmbient(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongMaterial::setAmbient(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#setAmbient

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongMaterial::setAmbient(const QColor &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial10setAmbientERK6QColor',
        self._valueOf(ambient),
    )

  @overload(QColor)
  def setDiffuse(self, diffuse: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongMaterial::setDiffuse(const QColor
    &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#setDiffuse

    Parameters
    ----------

    diffuse : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongMaterial::setDiffuse(const QColor &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial10setDiffuseERK6QColor',
        self._valueOf(diffuse),
    )

  @overload(QColor)
  def setSpecular(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongMaterial::setSpecular(const QColor
    &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#setSpecular

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongMaterial::setSpecular(const QColor &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial11setSpecularERK6QColor',
        self._valueOf(specular),
    )

  @overload(float)
  def setShininess(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongMaterial::setShininess(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#setShininess

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPhongMaterial::setShininess(float shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial12setShininessEf', shininess,
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
    'Qt3DExtras::QPhongMaterial::QPhongMaterial(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#QPhongMaterial

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QPhongMaterial::QPhongMaterial(Qt3DCore::QNode *parent)
    self._noteCreation(QPhongMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterialC1EPN8Qt3DCore5QNodeE',
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
    Calls Qt's 'void Qt3DExtras::QPhongMaterial::ambientChanged(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#ambientChanged

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongMaterial::ambientChanged(const QColor &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial14ambientChangedERK6QColor',
        self._valueOf(ambient),
    )

  @overload(QColor)
  def diffuseChanged(self, diffuse: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongMaterial::diffuseChanged(const QColor
    &diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#diffuseChanged

    Parameters
    ----------

    diffuse : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongMaterial::diffuseChanged(const QColor &diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial14diffuseChangedERK6QColor',
        self._valueOf(diffuse),
    )

  @overload(QColor)
  def specularChanged(self, specular: QColor) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongMaterial::specularChanged(const QColor
    &specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#specularChanged

    Parameters
    ----------

    specular : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QPhongMaterial::specularChanged(const QColor
    #      &specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial15specularChangedERK6QColor',
        self._valueOf(specular),
    )

  @overload(float)
  def shininessChanged(self, shininess: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QPhongMaterial::shininessChanged(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#shininessChanged

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QPhongMaterial::shininessChanged(float shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial16shininessChangedEf',
        shininess,
    )

  def d_func(self) -> Optional[Qt3DExtras.QPhongMaterialPrivate]:
    """
    Calls Qt's 'QPhongMaterialPrivate *Qt3DExtras::QPhongMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qphongmaterial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QPhongMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPhongMaterialPrivate *Qt3DExtras::QPhongMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras14QPhongMaterial6d_funcEv',
    )
    return Qt3DExtras.QPhongMaterialPrivate._cuteAt(address)
