"""
QQuick3DMorphTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dmorphtarget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DMorphTarget to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DMorphTarget(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DMorphTarget: a plain Python object standing
  in front of one C++ QQuick3DMorphTarget.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DMorphTarget is
  built on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DMorphTarget that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'weight',
  'attributes', 'setWeight', 'setAttributes', 'weightChanged',
  'attributesChanged', 'updateSpatialNode', 'markAllDirty', 'numAttribs'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DMorphTarget::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DMorphTarget::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DMorphTarget::~QQuick3DMorphTarget()': the destructor:
    Python never removes a C++ QQuick3DMorphTarget.
  - Qt's 'void QQuick3DMorphTarget::markDirty(QSSGMorphTargetDirtyType
    type)': names the enum 'QQuick3DMorphTarget::QSSGMorphTargetDirtyType',
    whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DMorphTarget is created at the first use, not by
    'QQuick3DMorphTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DMorphTarget.
  - Qt tells when it has removed the C++ QQuick3DMorphTarget. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DMorphTarget that has no cute function yet,
    'markDirty', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DMorphTarget, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MorphTargetAttribute(CuteFlags, scoped=True):
    """
    The flags enum 'QQuick3DMorphTarget::MorphTargetAttribute' of Qt, with
    the 7 names Qt gives in it. Qt names the type of its combinations
    'QQuick3DMorphTarget::MorphTargetAttributes'. C++ keeps these names
    inside the enum, so the class that holds the enum does not have them.
    """

    Position = 0x1
    Normal = 0x2
    Tangent = 0x4
    Binormal = 0x8
    TexCoord0 = 0x10
    TexCoord1 = 0x20
    Color = 0x40

  MorphTargetAttributes = MorphTargetAttribute

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
    Calls Qt's 'QString QQuick3DMorphTarget::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmorphtarget.html#tr

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
    #  QString QQuick3DMorphTarget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuick3DMorphTarget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DMorphTarget'

  #  A C++ QQuick3DMorphTarget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DMorphTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DMorphTarget::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DMorphTarget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuick3DMorphTarget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def weight(self) -> float:
    """
    Calls Qt's 'float QQuick3DMorphTarget::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmorphtarget.html#weight
    """
    #  float QQuick3DMorphTarget::weight() const
    return self.uglySide.call('ritual_ZNK19QQuick3DMorphTarget6weightEv')

  def attributes(self) -> MorphTargetAttributes:
    """
    Calls Qt's 'MorphTargetAttributes QQuick3DMorphTarget::attributes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#attributes

    Returns
    -------

    MorphTargetAttributes
      The value standing for the combination Qt gave back.
    """
    #  MorphTargetAttributes QQuick3DMorphTarget::attributes() const
    return QQuick3DMorphTarget.MorphTargetAttributes(self.uglySide.call(
        'ritual_ZNK19QQuick3DMorphTarget10attributesEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWeight(self, castsShadows: float) -> None:
    """
    Calls Qt's 'void QQuick3DMorphTarget::setWeight(float castsShadows)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dmorphtarget.html#setWeight

    Parameters
    ----------

    castsShadows : float
      Passed on as it is.
    """
    #  void QQuick3DMorphTarget::setWeight(float castsShadows)
    self.uglySide.call(
        'ritual_ZN19QQuick3DMorphTarget9setWeightEf', castsShadows,
    )

  @overload(MorphTargetAttributes)
  def setAttributes(self, attributes: MorphTargetAttributes) -> None:
    """
    Calls Qt's 'void QQuick3DMorphTarget::setAttributes(QQuick3DMorphTarget::
    MorphTargetAttributes attributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#setAttributes

    Parameters
    ----------

    attributes : MorphTargetAttributes
      Passed on as its number.
    """
    #  void QQuick3DMorphTarget::setAttributes(QQuick3DMorphTarget::
    #      MorphTargetAttributes attributes)
    self.uglySide.call(
        'ritual_ZN19QQuick3DMorphTarget13setAttributesE6QFlagsINS_20MorphTa'
        'rgetAttributeEE',
        attributes.value,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DMorphTarget::QQuick3DMorphTarget(QQuick3DObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#QQuick3DMorphTarget

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DMorphTarget::QQuick3DMorphTarget(QQuick3DObject *parent)
    self._noteCreation(QQuick3DMorphTarget, lambda: Rituals.call(
        'ritual_ZN19QQuick3DMorphTargetC1EP14QQuick3DObject',
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

  def weightChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DMorphTarget::weightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#weightChanged
    """
    #  void QQuick3DMorphTarget::weightChanged()
    self.uglySide.call('ritual_ZN19QQuick3DMorphTarget13weightChangedEv')

  def attributesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DMorphTarget::attributesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#attributesChanged
    """
    #  void QQuick3DMorphTarget::attributesChanged()
    self.uglySide.call('ritual_ZN19QQuick3DMorphTarget17attributesChangedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DMorphTarget::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DMorphTarget::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN19QQuick3DMorphTarget17updateSpatialNodeEP21QSSGRenderGra'
        'phObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuick3DMorphTarget17updateSpatialNodeEP21QSSGRen'
          'derGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DMorphTarget::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#markAllDirty
    """
    #  void QQuick3DMorphTarget::markAllDirty()
    ritual = 'ritual_ZN19QQuick3DMorphTarget12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuick3DMorphTarget12markAllDirtyEv'
    self.uglySide.call(ritual)

  def numAttribs(self) -> int:
    """
    Calls Qt's 'size_t QQuick3DMorphTarget::numAttribs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dmorphtarget.html#numAttribs
    """
    #  size_t QQuick3DMorphTarget::numAttribs()
    return self.uglySide.call('ritual_ZN19QQuick3DMorphTarget10numAttribsEv')

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DMorphTarget::markDirty(QSSGMorphTargetDirtyType
    type)': names the enum 'QQuick3DMorphTarget::QSSGMorphTargetDirtyType',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DMorphTarget.markDirty' has no cute function yet. Qt's "
        "'void QQuick3DMorphTarget::markDirty(QSSGMorphTargetDirtyType "
        "type)': names the enum "
        "'QQuick3DMorphTarget::QSSGMorphTargetDirtyType', whose class "
        "cannot be named here.")
