"""
Qt3DExtras::QTextureMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qtexturematerial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextureMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QTextureMaterial: a plain Python object
  standing in front of one C++ Qt3DExtras::QTextureMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QTextureMaterial is built on Qt's Qt3DRender::QMaterial, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QTextureMaterial that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'texture', 'textureOffset', 'isAlphaBlendingEnabled', 'setTexture',
  'setTextureOffset', 'setAlphaBlendingEnabled', 'textureChanged',
  'textureOffsetChanged', 'alphaBlendingEnabledChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QTextureMaterial::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QTextureMaterial::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QTextureMaterial::~QTextureMaterial()': the destructor:
    Python never removes a C++ Qt3DExtras::QTextureMaterial.
  - Qt's 'QMatrix3x3 Qt3DExtras::QTextureMaterial::textureTransform() const':
    gives a type Python has no way to take yet.
  - Qt's 'void Qt3DExtras::QTextureMaterial::setTextureTransform(const
    QMatrix3x3 &matrix)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DExtras::QTextureMaterial::textureTransformChanged(const
    QMatrix3x3 &textureTransform)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QTextureMaterialPrivate
    *Qt3DExtras::QTextureMaterial::d_func() const': takes in Python what
    'QTextureMaterialPrivate *Qt3DExtras::QTextureMaterial::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QTextureMaterial is created at the first use, not by
    'Qt3DExtras::QTextureMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QTextureMaterial.
  - Qt tells when it has removed the C++ Qt3DExtras::QTextureMaterial. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DExtras::QTextureMaterial that has no cute function
    yet, 'setTextureTransform', 'textureTransform',
    'textureTransformChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DExtras::QTextureMaterial::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#tr

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
    #  QString Qt3DExtras::QTextureMaterial::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QTextureMaterial'

  #  A C++ Qt3DExtras::QTextureMaterial Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QTextureMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::QTextureMaterial::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QTextureMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QTextureMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def texture(self) -> Optional[Qt3DRender.QAbstractTexture]:
    """
    Calls Qt's 'Qt3DRender::QAbstractTexture
    *Qt3DExtras::QTextureMaterial::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#texture

    Returns
    -------

    Optional[Qt3DRender.QAbstractTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QAbstractTexture *Qt3DExtras::QTextureMaterial::texture()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QTextureMaterial7textureEv',
    )
    return Qt3DRender.QAbstractTexture._cuteAt(address)

  def textureOffset(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D Qt3DExtras::QTextureMaterial::textureOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#textureOffset

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D Qt3DExtras::QTextureMaterial::textureOffset() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QTextureMaterial13textureOffsetEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def isAlphaBlendingEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::QTextureMaterial::isAlphaBlendingEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html
    """
    #  bool Qt3DExtras::QTextureMaterial::isAlphaBlendingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras16QTextureMaterial22isAlphaBlendingEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def setTexture(
      self,
      texture: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QTextureMaterial::setTexture(Qt3DRender::QAbstractTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#setTexture

    Parameters
    ----------

    texture : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QTextureMaterial::setTexture(Qt3DRender::
    #      QAbstractTexture *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterial10setTextureEPN10Qt3DRender'
        '16QAbstractTextureE',
        self._addressOf(texture),
    )

  @overload(QVector2D)
  def setTextureOffset(self, textureOffset: QVector2D) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QTextureMaterial::setTextureOffset(QVector2D
    textureOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#setTextureOffset

    Parameters
    ----------

    textureOffset : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void Qt3DExtras::QTextureMaterial::setTextureOffset(QVector2D
    #      textureOffset)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterial16setTextureOffsetE9QVector'
        '2D',
        self._valueOf(textureOffset),
    )

  @overload(bool)
  def setAlphaBlendingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QTextureMaterial::setAlphaBlendingEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QTextureMaterial::setAlphaBlendingEnabled(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterial23setAlphaBlendingEnabledEb',
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
    'Qt3DExtras::QTextureMaterial::QTextureMaterial(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#QTextureMaterial

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QTextureMaterial::QTextureMaterial(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QTextureMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterialC1EPN8Qt3DCore5QNodeE',
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
  def textureChanged(
      self,
      texture: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QTextureMaterial::textureChanged(Qt3DRender::QAbstractTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#textureChanged

    Parameters
    ----------

    texture : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QTextureMaterial::textureChanged(Qt3DRender::
    #      QAbstractTexture *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterial14textureChangedEPN10Qt3DRe'
        'nder16QAbstractTextureE',
        self._addressOf(texture),
    )

  @overload(QVector2D)
  def textureOffsetChanged(self, textureOffset: QVector2D) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QTextureMaterial::textureOffsetChanged(QVector2D
    textureOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html

    Parameters
    ----------

    textureOffset : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void Qt3DExtras::QTextureMaterial::textureOffsetChanged(QVector2D
    #      textureOffset)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterial20textureOffsetChangedE9QVe'
        'ctor2D',
        self._valueOf(textureOffset),
    )

  @overload(bool)
  def alphaBlendingEnabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QTextureMaterial::alphaBlendingEnabledChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DExtras::QTextureMaterial::alphaBlendingEnabledChanged(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterial27alphaBlendingEnabledChang'
        'edEb',
        enabled,
    )

  def d_func(self) -> Optional[Qt3DExtras.QTextureMaterialPrivate]:
    """
    Calls Qt's 'QTextureMaterialPrivate
    *Qt3DExtras::QTextureMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qtexturematerial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QTextureMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureMaterialPrivate *Qt3DExtras::QTextureMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras16QTextureMaterial6d_funcEv',
    )
    return Qt3DExtras.QTextureMaterialPrivate._cuteAt(address)

  @staticmethod
  def setTextureTransform(*__, **_) -> Never:
    """
    Qt's 'void Qt3DExtras::QTextureMaterial::setTextureTransform(const
    QMatrix3x3 &matrix)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QTextureMaterial.setTextureTransform' has no cute "
        "function yet. Qt's 'void "
        "Qt3DExtras::QTextureMaterial::setTextureTransform(const QMatrix3x3 "
        "&matrix)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def textureTransform(*__, **_) -> Never:
    """
    Qt's 'QMatrix3x3 Qt3DExtras::QTextureMaterial::textureTransform() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QTextureMaterial.textureTransform' has no cute "
        "function yet. Qt's 'QMatrix3x3 "
        "Qt3DExtras::QTextureMaterial::textureTransform() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def textureTransformChanged(*__, **_) -> Never:
    """
    Qt's 'void Qt3DExtras::QTextureMaterial::textureTransformChanged(const
    QMatrix3x3 &textureTransform)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QTextureMaterial.textureTransformChanged' has no cute "
        "function yet. Qt's 'void "
        "Qt3DExtras::QTextureMaterial::textureTransformChanged(const "
        "QMatrix3x3 &textureTransform)': takes a type Python has no way to "
        "hand over yet.")
