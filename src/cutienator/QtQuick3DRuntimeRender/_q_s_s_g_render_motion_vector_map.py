"""
QSSGRenderMotionVectorMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermotionvectormap_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderMotionVectorMap to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderMotionVectorMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderMotionVectorMap: a plain Python object
  standing in front of one C++ QSSGRenderMotionVectorMap.

  What exists
  -----------

  Every function of Qt's QSSGRenderMotionVectorMap that has a ritual and that
  Python can call so far, 3 names in all: 'endFrame',
  'releaseCachedResources', 'cleanupStaleEntries'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderMotionVectorMap::QSSGRenderMotionVectorMap(const
    QSSGRenderContextInterface &inContext)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QSSGRenderMotionVectorMap::~QSSGRenderMotionVectorMap()': the
    destructor: Python never removes a C++ QSSGRenderMotionVectorMap.
  - Qt's 'MotionResultData QSSGRenderMotionVectorMap::trackMotionData(const
    void *modelKey, const QMatrix4x4 &currentModelViewProjection, const
    QMatrix4x4 &currentInstanceLocal, const QMatrix4x4
    &currentInstanceGlobal, QSSGRenderTextureData *currentBoneTextureData,
    QSSGRenderInstanceTable *currentInstanceTable, const QVector<float>
    &currentMorphWeights)': names 'void', which has no cute class yet.
  - Qt's 'void
    QSSGRenderMotionVectorMap::releaseEntryResources(MotionStoreData
    &entry)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRenderImageTexture
    QSSGRenderMotionVectorMap::loadAndReleaseIfNeeded(const
    std::shared_ptr<QSSGRenderTextureData> &textureData, QSize lastSize)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRenderMotionVectorMap is created at the first use, not by
    'QSSGRenderMotionVectorMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderMotionVectorMap.
  - Each name of Qt's QSSGRenderMotionVectorMap that has no cute function
    yet, '__init__', 'loadAndReleaseIfNeeded', 'releaseEntryResources',
    'trackMotionData', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QSSGRenderMotionVectorMap, each a class in
  #  here as in C++.

  class MotionResultData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderMotionVectorMap::MotionResultData: a
    plain Python object standing in front of one C++
    QSSGRenderMotionVectorMap::MotionResultData.

    C++ hands a QSSGRenderMotionVectorMap::MotionResultData around as a copy,
    so every C++ QSSGRenderMotionVectorMap::MotionResultData behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderMotionVectorMap::MotionResultData yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSSGRenderMotionVectorMap::MotionResultData::~MotionResultData()': the
      destructor: Python removes its C++
      QSSGRenderMotionVectorMap::MotionResultData by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGRenderMotionVectorMap::MotionResultData is created at the
      first use, not by 'QSSGRenderMotionVectorMap::MotionResultData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderMotionVectorMap::MotionResultData back
      gives a copy the ritual made for Python, in a new cute
      QSSGRenderMotionVectorMap::MotionResultData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderMotionVectorMap::MotionResultData'

    #  Qt's '~QSSGRenderMotionVectorMap::MotionResultData()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGRenderMotionVectorMap::MotionResultData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN25QSSGRenderMotionVectorMap16MotionResultDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderMotionVectorMap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderMotionVectorMap::QSSGRenderMotionVectorMap(const
    QSSGRenderContextInterface &inContext)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderMotionVectorMap.__init__' has no cute function yet. "
        "Qt's 'QSSGRenderMotionVectorMap::QSSGRenderMotionVectorMap(const "
        "QSSGRenderContextInterface &inContext)': takes a type Python has "
        "no way to hand over yet.")

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

  def endFrame(self) -> None:
    """
    Calls Qt's 'void QSSGRenderMotionVectorMap::endFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendermotionvectormap.html#endFrame
    """
    #  void QSSGRenderMotionVectorMap::endFrame()
    self.uglySide.call('ritual_ZN25QSSGRenderMotionVectorMap8endFrameEv')

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSSGRenderMotionVectorMap::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendermotionvectormap.html
    """
    #  void QSSGRenderMotionVectorMap::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN25QSSGRenderMotionVectorMap22releaseCachedResourcesEv',
    )

  def cleanupStaleEntries(self) -> None:
    """
    Calls Qt's 'void QSSGRenderMotionVectorMap::cleanupStaleEntries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendermotionvectormap.html#cleanupStaleEntries
    """
    #  void QSSGRenderMotionVectorMap::cleanupStaleEntries()
    self.uglySide.call(
        'ritual_ZN25QSSGRenderMotionVectorMap19cleanupStaleEntriesEv',
    )

  @staticmethod
  def loadAndReleaseIfNeeded(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderImageTexture
    QSSGRenderMotionVectorMap::loadAndReleaseIfNeeded(const
    std::shared_ptr<QSSGRenderTextureData> &textureData, QSize lastSize)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderMotionVectorMap.loadAndReleaseIfNeeded' has no cute "
        "function yet. Qt's 'QSSGRenderImageTexture "
        "QSSGRenderMotionVectorMap::loadAndReleaseIfNeeded(const "
        "std::shared_ptr<QSSGRenderTextureData> &textureData, QSize "
        "lastSize)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def releaseEntryResources(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGRenderMotionVectorMap::releaseEntryResources(MotionStoreData
    &entry)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderMotionVectorMap.releaseEntryResources' has no cute "
        "function yet. Qt's 'void "
        "QSSGRenderMotionVectorMap::releaseEntryResources(MotionStoreData "
        "&entry)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def trackMotionData(*__, **_) -> Never:
    """
    Qt's 'MotionResultData QSSGRenderMotionVectorMap::trackMotionData(const
    void *modelKey, const QMatrix4x4 &currentModelViewProjection, const
    QMatrix4x4 &currentInstanceLocal, const QMatrix4x4
    &currentInstanceGlobal, QSSGRenderTextureData *currentBoneTextureData,
    QSSGRenderInstanceTable *currentInstanceTable, const QVector<float>
    &currentMorphWeights)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRenderMotionVectorMap.trackMotionData' has no cute function "
        "yet. Qt's 'MotionResultData "
        "QSSGRenderMotionVectorMap::trackMotionData(const void *modelKey, "
        "const QMatrix4x4 &currentModelViewProjection, const QMatrix4x4 "
        "&currentInstanceLocal, const QMatrix4x4 &currentInstanceGlobal, "
        "QSSGRenderTextureData *currentBoneTextureData, "
        "QSSGRenderInstanceTable *currentInstanceTable, const "
        "QVector<float> &currentMorphWeights)': names 'void', which has no "
        "cute class yet.")
