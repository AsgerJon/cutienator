"""
QSSGRenderableObjectFlags binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderableObjectFlags to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class QSSGRenderableObjectFlags(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderableObjectFlags: a plain Python object
  standing in front of one C++ QSSGRenderableObjectFlags.

  C++ hands a QSSGRenderableObjectFlags around as a copy, so every C++
  QSSGRenderableObjectFlags behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderableObjectFlags that has a ritual and that
  Python can call so far, 46 names in all: 'setHasTransparency',
  'hasTransparency', 'setCompletelyTransparent', 'isCompletelyTransparent',
  'setDirty', 'isDirty', 'setCastsShadows', 'castsShadows',
  'setReceivesShadows', 'receivesShadows', 'setReceivesReflections',
  'receivesReflections', 'setCastsReflections', 'castsReflections',
  'setUsedInBakedLighting', 'usedInBakedLighting', 'setRendersWithLightmap',
  'rendersWithLightmap', 'setHasAttributePosition', 'hasAttributePosition',
  'setHasAttributeNormal', 'hasAttributeNormal', 'setHasAttributeTexCoord0',
  'hasAttributeTexCoord0', 'setHasAttributeTexCoord1',
  'hasAttributeTexCoord1', 'setHasAttributeTexCoordLightmap',
  'hasAttributeTexCoordLightmap', 'setHasAttributeTangent',
  'hasAttributeTangent', 'setHasAttributeBinormal', 'hasAttributeBinormal',
  'setHasAttributeColor', 'hasAttributeColor',
  'setHasAttributeJointAndWeight', 'hasAttributeJointAndWeight',
  'setHasAttributeMorphTarget', 'hasAttributeMorphTarget',
  'setPointsTopology', 'isPointsTopology', 'setRequiresScreenTexture',
  'requiresScreenTexture', 'setRequiresNormalTexture',
  'requiresNormalTexture', 'setMotionVectorParticipant',
  'isMotionVectorParticipant'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderableObjectFlags::~QSSGRenderableObjectFlags()': the
    destructor: Python removes its C++ QSSGRenderableObjectFlags by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderableObjectFlags is created at the first use, not by
    'QSSGRenderableObjectFlags(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderableObjectFlags back gives a copy the
    ritual made for Python, in a new cute QSSGRenderableObjectFlags.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderableObjectFlags'

  #  Qt's '~QSSGRenderableObjectFlags()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRenderableObjectFlags behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QSSGRenderableObjectFlagsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasTransparency(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasTransparency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#hasTransparency
    """
    #  bool QSSGRenderableObjectFlags::hasTransparency() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags15hasTransparencyEv',
    )

  def isCompletelyTransparent(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::isCompletelyTransparent()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::isCompletelyTransparent() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags23isCompletelyTransparentEv',
    )

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#isDirty
    """
    #  bool QSSGRenderableObjectFlags::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags7isDirtyEv',
    )

  def castsShadows(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::castsShadows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#castsShadows
    """
    #  bool QSSGRenderableObjectFlags::castsShadows() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags12castsShadowsEv',
    )

  def receivesShadows(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::receivesShadows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#receivesShadows
    """
    #  bool QSSGRenderableObjectFlags::receivesShadows() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags15receivesShadowsEv',
    )

  def receivesReflections(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::receivesReflections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#receivesReflections
    """
    #  bool QSSGRenderableObjectFlags::receivesReflections() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags19receivesReflectionsEv',
    )

  def castsReflections(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::castsReflections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#castsReflections
    """
    #  bool QSSGRenderableObjectFlags::castsReflections() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags16castsReflectionsEv',
    )

  def usedInBakedLighting(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::usedInBakedLighting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#usedInBakedLighting
    """
    #  bool QSSGRenderableObjectFlags::usedInBakedLighting() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags19usedInBakedLightingEv',
    )

  def rendersWithLightmap(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::rendersWithLightmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#rendersWithLightmap
    """
    #  bool QSSGRenderableObjectFlags::rendersWithLightmap() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags19rendersWithLightmapEv',
    )

  def hasAttributePosition(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributePosition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::hasAttributePosition() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags20hasAttributePositionEv',
    )

  def hasAttributeNormal(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributeNormal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#hasAttributeNormal
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeNormal() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags18hasAttributeNormalEv',
    )

  def hasAttributeTexCoord0(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributeTexCoord0()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeTexCoord0() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags21hasAttributeTexCoord0Ev',
    )

  def hasAttributeTexCoord1(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributeTexCoord1()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeTexCoord1() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags21hasAttributeTexCoord1Ev',
    )

  def hasAttributeTexCoordLightmap(self) -> bool:
    """
    Calls Qt's 'bool
    QSSGRenderableObjectFlags::hasAttributeTexCoordLightmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeTexCoordLightmap() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags28hasAttributeTexCoordLightma'
        'pEv',
    )

  def hasAttributeTangent(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributeTangent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#hasAttributeTangent
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeTangent() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags19hasAttributeTangentEv',
    )

  def hasAttributeBinormal(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributeBinormal()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeBinormal() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags20hasAttributeBinormalEv',
    )

  def hasAttributeColor(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributeColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#hasAttributeColor
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeColor() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags17hasAttributeColorEv',
    )

  def hasAttributeJointAndWeight(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributeJointAndWeight()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeJointAndWeight() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags26hasAttributeJointAndWeightE'
        'v',
    )

  def hasAttributeMorphTarget(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::hasAttributeMorphTarget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::hasAttributeMorphTarget() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags23hasAttributeMorphTargetEv',
    )

  def isPointsTopology(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::isPointsTopology() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#isPointsTopology
    """
    #  bool QSSGRenderableObjectFlags::isPointsTopology() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags16isPointsTopologyEv',
    )

  def requiresScreenTexture(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::requiresScreenTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::requiresScreenTexture() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags21requiresScreenTextureEv',
    )

  def requiresNormalTexture(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::requiresNormalTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::requiresNormalTexture() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags21requiresNormalTextureEv',
    )

  def isMotionVectorParticipant(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableObjectFlags::isMotionVectorParticipant()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html
    """
    #  bool QSSGRenderableObjectFlags::isMotionVectorParticipant() const
    return self.uglySide.call(
        'ritual_ZNK25QSSGRenderableObjectFlags25isMotionVectorParticipantEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setHasTransparency(self, inHasTransparency: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setHasTransparency(bool
    inHasTransparency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#setHasTransparency

    Parameters
    ----------

    inHasTransparency : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasTransparency(bool
    #      inHasTransparency)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags18setHasTransparencyEb',
        inHasTransparency,
    )

  @overload(bool)
  def setCompletelyTransparent(self, inTransparent: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setCompletelyTransparent(bool
    inTransparent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    inTransparent : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setCompletelyTransparent(bool
    #      inTransparent)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags24setCompletelyTransparentEb',
        inTransparent,
    )

  @overload(bool)
  def setDirty(self, inDirty: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setDirty(bool inDirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#setDirty

    Parameters
    ----------

    inDirty : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setDirty(bool inDirty)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags8setDirtyEb', inDirty,
    )

  @overload(bool)
  def setCastsShadows(self, inCastsShadows: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setCastsShadows(bool
    inCastsShadows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#setCastsShadows

    Parameters
    ----------

    inCastsShadows : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setCastsShadows(bool inCastsShadows)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags15setCastsShadowsEb',
        inCastsShadows,
    )

  @overload(bool)
  def setReceivesShadows(self, inReceivesShadows: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setReceivesShadows(bool
    inReceivesShadows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#setReceivesShadows

    Parameters
    ----------

    inReceivesShadows : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setReceivesShadows(bool
    #      inReceivesShadows)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags18setReceivesShadowsEb',
        inReceivesShadows,
    )

  @overload(bool)
  def setReceivesReflections(self, inReceivesReflections: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setReceivesReflections(bool
    inReceivesReflections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    inReceivesReflections : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setReceivesReflections(bool
    #      inReceivesReflections)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags22setReceivesReflectionsEb',
        inReceivesReflections,
    )

  @overload(bool)
  def setCastsReflections(self, inCastsReflections: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setCastsReflections(bool
    inCastsReflections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#setCastsReflections

    Parameters
    ----------

    inCastsReflections : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setCastsReflections(bool
    #      inCastsReflections)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags19setCastsReflectionsEb',
        inCastsReflections,
    )

  @overload(bool)
  def setUsedInBakedLighting(self, inUsedInBakedLighting: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setUsedInBakedLighting(bool
    inUsedInBakedLighting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    inUsedInBakedLighting : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setUsedInBakedLighting(bool
    #      inUsedInBakedLighting)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags22setUsedInBakedLightingEb',
        inUsedInBakedLighting,
    )

  @overload(bool)
  def setRendersWithLightmap(self, inRendersWithLightmap: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setRendersWithLightmap(bool
    inRendersWithLightmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    inRendersWithLightmap : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setRendersWithLightmap(bool
    #      inRendersWithLightmap)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags22setRendersWithLightmapEb',
        inRendersWithLightmap,
    )

  @overload(bool)
  def setHasAttributePosition(self, b: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setHasAttributePosition(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributePosition(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags23setHasAttributePositionEb', b,
    )

  @overload(bool)
  def setHasAttributeNormal(self, b: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setHasAttributeNormal(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeNormal(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags21setHasAttributeNormalEb', b,
    )

  @overload(bool)
  def setHasAttributeTexCoord0(self, b: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setHasAttributeTexCoord0(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeTexCoord0(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags24setHasAttributeTexCoord0Eb',
        b,
    )

  @overload(bool)
  def setHasAttributeTexCoord1(self, b: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setHasAttributeTexCoord1(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeTexCoord1(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags24setHasAttributeTexCoord1Eb',
        b,
    )

  @overload(bool)
  def setHasAttributeTexCoordLightmap(self, b: bool) -> None:
    """
    Calls Qt's 'void
    QSSGRenderableObjectFlags::setHasAttributeTexCoordLightmap(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeTexCoordLightmap(bool
    #      b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags31setHasAttributeTexCoordLight'
        'mapEb',
        b,
    )

  @overload(bool)
  def setHasAttributeTangent(self, b: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setHasAttributeTangent(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeTangent(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags22setHasAttributeTangentEb', b,
    )

  @overload(bool)
  def setHasAttributeBinormal(self, b: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setHasAttributeBinormal(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeBinormal(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags23setHasAttributeBinormalEb', b,
    )

  @overload(bool)
  def setHasAttributeColor(self, b: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setHasAttributeColor(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeColor(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags20setHasAttributeColorEb', b,
    )

  @overload(bool)
  def setHasAttributeJointAndWeight(self, b: bool) -> None:
    """
    Calls Qt's 'void
    QSSGRenderableObjectFlags::setHasAttributeJointAndWeight(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeJointAndWeight(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags29setHasAttributeJointAndWeigh'
        'tEb',
        b,
    )

  @overload(bool)
  def setHasAttributeMorphTarget(self, b: bool) -> None:
    """
    Calls Qt's 'void
    QSSGRenderableObjectFlags::setHasAttributeMorphTarget(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setHasAttributeMorphTarget(bool b)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags26setHasAttributeMorphTargetEb',
        b,
    )

  @overload(bool)
  def setPointsTopology(self, v: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setPointsTopology(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html#setPointsTopology

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setPointsTopology(bool v)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags17setPointsTopologyEb', v,
    )

  @overload(bool)
  def setRequiresScreenTexture(self, v: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setRequiresScreenTexture(bool
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setRequiresScreenTexture(bool v)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags24setRequiresScreenTextureEb',
        v,
    )

  @overload(bool)
  def setRequiresNormalTexture(self, v: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderableObjectFlags::setRequiresNormalTexture(bool
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setRequiresNormalTexture(bool v)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags24setRequiresNormalTextureEb',
        v,
    )

  @overload(bool)
  def setMotionVectorParticipant(self, v: bool) -> None:
    """
    Calls Qt's 'void
    QSSGRenderableObjectFlags::setMotionVectorParticipant(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjectflags.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QSSGRenderableObjectFlags::setMotionVectorParticipant(bool v)
    self.uglySide.call(
        'ritual_ZN25QSSGRenderableObjectFlags26setMotionVectorParticipantEb',
        v,
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
