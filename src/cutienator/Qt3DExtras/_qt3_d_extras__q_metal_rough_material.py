"""
Qt3DExtras::QMetalRoughMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qmetalroughmaterial.h, Qt 6.12.0. Changes made here are lost.
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetalRoughMaterial(Qt3DRender.QMaterial):
  """
  The cute side of Qt's Qt3DExtras::QMetalRoughMaterial: a plain Python
  object standing in front of one C++ Qt3DExtras::QMetalRoughMaterial.

  It is built on the cute 'Qt3DRender::QMaterial', as Qt's
  Qt3DExtras::QMetalRoughMaterial is built on Qt's Qt3DRender::QMaterial, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QMetalRoughMaterial that has a ritual
  and that Python can call so far, 21 names in all: 'metaObject', 'tr',
  'baseColor', 'metalness', 'roughness', 'ambientOcclusion', 'normal',
  'textureScale', 'setBaseColor', 'setMetalness', 'setRoughness',
  'setAmbientOcclusion', 'setNormal', 'setTextureScale', 'baseColorChanged',
  'metalnessChanged', 'roughnessChanged', 'ambientOcclusionChanged',
  'normalChanged', 'textureScaleChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QMetalRoughMaterial::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DExtras::QMetalRoughMaterial::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::QMetalRoughMaterial::~QMetalRoughMaterial()': the
    destructor: Python never removes a C++ Qt3DExtras::QMetalRoughMaterial.
  - Qt's 'Qt3DExtras::QMetalRoughMaterial::QMetalRoughMaterial(
    QMetalRoughMaterialPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QMetalRoughMaterialPrivate
    *Qt3DExtras::QMetalRoughMaterial::d_func() const': takes in Python what
    'QMetalRoughMaterialPrivate *Qt3DExtras::QMetalRoughMaterial::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QMetalRoughMaterial is created at the first use, not
    by 'Qt3DExtras::QMetalRoughMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QMetalRoughMaterial.
  - Qt tells when it has removed the C++ Qt3DExtras::QMetalRoughMaterial.
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
    Calls Qt's 'QString Qt3DExtras::QMetalRoughMaterial::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#tr

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
    #  QString Qt3DExtras::QMetalRoughMaterial::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QMetalRoughMaterial'

  #  A C++ Qt3DExtras::QMetalRoughMaterial Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QMetalRoughMaterial'

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
    *Qt3DExtras::QMetalRoughMaterial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::QMetalRoughMaterial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMetalRoughMaterial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def baseColor(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DExtras::QMetalRoughMaterial::baseColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#baseColor

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DExtras::QMetalRoughMaterial::baseColor() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMetalRoughMaterial9baseColorEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def metalness(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DExtras::QMetalRoughMaterial::metalness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#metalness

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DExtras::QMetalRoughMaterial::metalness() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMetalRoughMaterial9metalnessEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roughness(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DExtras::QMetalRoughMaterial::roughness() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#roughness

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DExtras::QMetalRoughMaterial::roughness() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMetalRoughMaterial9roughnessEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def ambientOcclusion(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DExtras::QMetalRoughMaterial::ambientOcclusion()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DExtras::QMetalRoughMaterial::ambientOcclusion() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMetalRoughMaterial16ambientOcclusionEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def normal(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DExtras::QMetalRoughMaterial::normal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#normal

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DExtras::QMetalRoughMaterial::normal() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMetalRoughMaterial6normalEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def textureScale(self) -> float:
    """
    Calls Qt's 'float Qt3DExtras::QMetalRoughMaterial::textureScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#textureScale
    """
    #  float Qt3DExtras::QMetalRoughMaterial::textureScale() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras19QMetalRoughMaterial12textureScaleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setBaseColor(self, baseColor: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::setBaseColor(const
    QVariant &baseColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#setBaseColor

    Parameters
    ----------

    baseColor : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::setBaseColor(const QVariant
    #      &baseColor)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial12setBaseColorERK8QVaria'
        'nt',
        self._valueOf(baseColor),
    )

  @overload(QVariant)
  def setMetalness(self, metalness: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::setMetalness(const
    QVariant &metalness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#setMetalness

    Parameters
    ----------

    metalness : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::setMetalness(const QVariant
    #      &metalness)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial12setMetalnessERK8QVaria'
        'nt',
        self._valueOf(metalness),
    )

  @overload(QVariant)
  def setRoughness(self, roughness: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::setRoughness(const
    QVariant &roughness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#setRoughness

    Parameters
    ----------

    roughness : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::setRoughness(const QVariant
    #      &roughness)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial12setRoughnessERK8QVaria'
        'nt',
        self._valueOf(roughness),
    )

  @overload(QVariant)
  def setAmbientOcclusion(self, ambientOcclusion: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMetalRoughMaterial::setAmbientOcclusion(const QVariant
    &ambientOcclusion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Parameters
    ----------

    ambientOcclusion : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::setAmbientOcclusion(const
    #      QVariant &ambientOcclusion)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial19setAmbientOcclusionERK'
        '8QVariant',
        self._valueOf(ambientOcclusion),
    )

  @overload(QVariant)
  def setNormal(self, normal: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::setNormal(const
    QVariant &normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#setNormal

    Parameters
    ----------

    normal : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::setNormal(const QVariant
    #      &normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial9setNormalERK8QVariant',
        self._valueOf(normal),
    )

  @overload(float)
  def setTextureScale(self, textureScale: float) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::setTextureScale(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::setTextureScale(float
    #      textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial15setTextureScaleEf',
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
    'Qt3DExtras::QMetalRoughMaterial::QMetalRoughMaterial(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QMetalRoughMaterial::QMetalRoughMaterial(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QMetalRoughMaterial, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterialC1EPN8Qt3DCore5QNodeE',
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

  @overload(QVariant)
  def baseColorChanged(self, baseColor: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::baseColorChanged(const
    QVariant &baseColor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Parameters
    ----------

    baseColor : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::baseColorChanged(const QVariant
    #      &baseColor)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial16baseColorChangedERK8QV'
        'ariant',
        self._valueOf(baseColor),
    )

  @overload(QVariant)
  def metalnessChanged(self, metalness: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::metalnessChanged(const
    QVariant &metalness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Parameters
    ----------

    metalness : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::metalnessChanged(const QVariant
    #      &metalness)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial16metalnessChangedERK8QV'
        'ariant',
        self._valueOf(metalness),
    )

  @overload(QVariant)
  def roughnessChanged(self, roughness: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::roughnessChanged(const
    QVariant &roughness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Parameters
    ----------

    roughness : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::roughnessChanged(const QVariant
    #      &roughness)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial16roughnessChangedERK8QV'
        'ariant',
        self._valueOf(roughness),
    )

  @overload(QVariant)
  def ambientOcclusionChanged(self, ambientOcclusion: QVariant) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMetalRoughMaterial::ambientOcclusionChanged(const QVariant
    &ambientOcclusion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Parameters
    ----------

    ambientOcclusion : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::ambientOcclusionChanged(const
    #      QVariant &ambientOcclusion)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial23ambientOcclusionChange'
        'dERK8QVariant',
        self._valueOf(ambientOcclusion),
    )

  @overload(QVariant)
  def normalChanged(self, normal: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QMetalRoughMaterial::normalChanged(const
    QVariant &normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#normalChanged

    Parameters
    ----------

    normal : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::normalChanged(const QVariant
    #      &normal)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial13normalChangedERK8QVari'
        'ant',
        self._valueOf(normal),
    )

  @overload(float)
  def textureScaleChanged(self, textureScale: float) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QMetalRoughMaterial::textureScaleChanged(float
    textureScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html

    Parameters
    ----------

    textureScale : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QMetalRoughMaterial::textureScaleChanged(float
    #      textureScale)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial19textureScaleChangedEf',
        textureScale,
    )

  def d_func(self) -> Optional[Qt3DExtras.QMetalRoughMaterialPrivate]:
    """
    Calls Qt's 'QMetalRoughMaterialPrivate
    *Qt3DExtras::QMetalRoughMaterial::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qmetalroughmaterial.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.QMetalRoughMaterialPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMetalRoughMaterialPrivate *Qt3DExtras::QMetalRoughMaterial::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras19QMetalRoughMaterial6d_funcEv',
    )
    return Qt3DExtras.QMetalRoughMaterialPrivate._cuteAt(address)
