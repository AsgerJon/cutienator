"""
Qt3DExtras::QNormalDiffuseSpecularMapMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qnormaldiffusespecularmapmaterial.h, Qt 6.12.0. Changes made
#  here are lost.
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


class QNormalDiffuseSpecularMapMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QNormalDiffuseSpecularMapMaterial: a
  plain Python object standing in front of one C++
  Qt3DExtras::QNormalDiffuseSpecularMapMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QNormalDiffuseSpecularMapMaterial is built on Qt's
  Qt3DRender::QMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QNormalDiffuseSpecularMapMaterial that
  has a ritual and that Python can call so far, 21 names in all:
  'metaObject', 'tr', 'ambient', 'diffuse', 'normal', 'specular',
  'shininess', 'textureScale', 'setAmbient', 'setDiffuse', 'setNormal',
  'setSpecular', 'setShininess', 'setTextureScale', 'ambientChanged',
  'diffuseChanged', 'normalChanged', 'specularChanged', 'shininessChanged',
  'textureScaleChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QNormalDiffuseSpecularMapMaterial::
    ~QNormalDiffuseSpecularMapMaterial()': the destructor: Python never
    removes a C++ Qt3DExtras::QNormalDiffuseSpecularMapMaterial.
  - Qt's 'Qt3DExtras::QNormalDiffuseSpecularMapMaterial::
    QNormalDiffuseSpecularMapMaterial(
    QNormalDiffuseSpecularMapMaterialPrivate &dd, Qt3DCore::QNode *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QNormalDiffuseSpecularMapMaterialPrivate
    *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::d_func() const': takes in
    Python what 'QNormalDiffuseSpecularMapMaterialPrivate
    *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QNormalDiffuseSpecularMapMaterial is created at the
    first use, not by 'Qt3DExtras::QNormalDiffuseSpecularMapMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial.
  - Qt tells when it has removed the C++
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

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
    #  QString Qt3DExtras::QNormalDiffuseSpecularMapMaterial::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial2trEPKcS2_'
        'i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QNormalDiffuseSpecularMapMaterial'

  #  A C++ Qt3DExtras::QNormalDiffuseSpecularMapMaterial Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QNormalDiffuseSpecularMapMaterial'

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
    *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial10metaObj'
        'ectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def ambient(self) -> QColor:
    """
    Calls Qt's 'QColor
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::ambient() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DExtras::QNormalDiffuseSpecularMapMaterial::ambient() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial7ambientE'
        'v',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def diffuse(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::diffuse() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::diffuse() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial7diffuseE'
        'v',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def normal(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::normal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::normal() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial6normalEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def specular(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::specular() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture
    #      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::specular() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial8specular'
        'Ev',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def shininess(self) -> float:
    """
    Calls Qt's 'float
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::shininess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html
    """
    #  float Qt3DExtras::QNormalDiffuseSpecularMapMaterial::shininess() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial9shinines'
        'sEv',
    )

  def textureScale(self) -> float:
    """
    Calls Qt's 'float
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::textureScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html
    """
    #  float Qt3DExtras::QNormalDiffuseSpecularMapMaterial::textureScale()
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras33QNormalDiffuseSpecularMapMaterial12texture'
        'ScaleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setAmbient(self, ambient: QColor) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setAmbient(const QColor
    &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setAmbient(const
    #      QColor &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial10setAmbie'
        'ntERK6QColor',
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
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setDiffuse(Qt3DRender::
    QAbstractTexture *diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    diffuse : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setDiffuse(
    #      Qt3DRender::QAbstractTexture *diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial10setDiffu'
        'seEPN10Qt3DRender16QAbstractTextureE',
        self._addressOf(diffuse),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setNormal(self, normal: Optional[Qt3DRender.QAbstractTexture]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setNormal(Qt3DRender::
    QAbstractTexture *normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    normal : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setNormal(
    #      Qt3DRender::QAbstractTexture *normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial9setNormal'
        'EPN10Qt3DRender16QAbstractTextureE',
        self._addressOf(normal),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setSpecular(
      self,
      specular: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setSpecular(Qt3DRender::
    QAbstractTexture *specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    specular : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setSpecular(
    #      Qt3DRender::QAbstractTexture *specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial11setSpecu'
        'larEPN10Qt3DRender16QAbstractTextureE',
        self._addressOf(specular),
    )

  @overload(float)
  def setShininess(self, shininess: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setShininess(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setShininess(float
    #      shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial12setShini'
        'nessEf',
        shininess,
    )

  @overload(float)
  def setTextureScale(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setTextureScale(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::setTextureScale(
    #      float textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial15setTextu'
        'reScaleEf',
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
    'Qt3DExtras::QNormalDiffuseSpecularMapMaterial::
    QNormalDiffuseSpecularMapMaterial(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QNormalDiffuseSpecularMapMaterial::
    #      QNormalDiffuseSpecularMapMaterial(Qt3DCore::QNode *parent)
    self._noteCreation(
        QNormalDiffuseSpecularMapMaterial, lambda: Rituals.call(
            'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterialC1EPN8'
            'Qt3DCore5QNodeE',
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
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::ambientChanged(const
    QColor &ambient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    ambient : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::ambientChanged(
    #      const QColor &ambient)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial14ambientC'
        'hangedERK6QColor',
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
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::diffuseChanged(
    Qt3DRender::QAbstractTexture *diffuse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    diffuse : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::diffuseChanged(
    #      Qt3DRender::QAbstractTexture *diffuse)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial14diffuseC'
        'hangedEPN10Qt3DRender16QAbstractTextureE',
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
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::normalChanged(
    Qt3DRender::QAbstractTexture *normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    normal : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::normalChanged(
    #      Qt3DRender::QAbstractTexture *normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial13normalCh'
        'angedEPN10Qt3DRender16QAbstractTextureE',
        self._addressOf(normal),
    )

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def specularChanged(
      self,
      specular: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::specularChanged(
    Qt3DRender::QAbstractTexture *specular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    specular : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::specularChanged(
    #      Qt3DRender::QAbstractTexture *specular)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial15specular'
        'ChangedEPN10Qt3DRender16QAbstractTextureE',
        self._addressOf(specular),
    )

  @overload(float)
  def shininessChanged(self, shininess: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::shininessChanged(float
    shininess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    shininess : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::shininessChanged(
    #      float shininess)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial16shinines'
        'sChangedEf',
        shininess,
    )

  @overload(float)
  def textureScaleChanged(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QNormalDiffuseSpecularMapMaterial::textureScaleChanged(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QNormalDiffuseSpecularMapMaterial::
    #      textureScaleChanged(float textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial19textureS'
        'caleChangedEf',
        textureScale,
    )

  def d_func(
      self,
  ) -> Optional[Qt3DExtras.QNormalDiffuseSpecularMapMaterialPrivate]:
    """
    Calls Qt's 'QNormalDiffuseSpecularMapMaterialPrivate
    *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qnormaldiffusespecularmapmaterial.html

    Returns
    -------

    Optional[Qt3DExtras.QNormalDiffuseSpecularMapMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNormalDiffuseSpecularMapMaterialPrivate
    #      *Qt3DExtras::QNormalDiffuseSpecularMapMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras33QNormalDiffuseSpecularMapMaterial6d_funcEv',
    )
    return Qt3DExtras.QNormalDiffuseSpecularMapMaterialPrivate._cuteAt(address)
