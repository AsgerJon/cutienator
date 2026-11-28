"""
QSGRhiShaderEffectNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhishadereffectnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGRhiShaderEffectNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QSGShaderEffectNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRhiShaderEffectNode(QSGShaderEffectNode):
  """
  The cute side of Qt's QSGRhiShaderEffectNode: a plain Python object
  standing in front of one C++ QSGRhiShaderEffectNode.

  It is built on the cute 'QSGShaderEffectNode', as Qt's
  QSGRhiShaderEffectNode is built on Qt's QSGShaderEffectNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiShaderEffectNode that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject',
  'updateNormalizedTextureSubRect', 'syncMaterial', 'preprocess',
  'handleTextureChange'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGRhiShaderEffectNode::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSGRhiShaderEffectNode::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  the compiler refuses its ritual as it would be written here; 1 leans on
  'QSGRhiShaderEffectNode; 1 leans on 'vtable for QSGRhiShaderEffectNode',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ QSGRhiShaderEffectNode is created at the first use, not by
    'QSGRhiShaderEffectNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiShaderEffectNode.
  - Qt tells when it has removed the C++ QSGRhiShaderEffectNode. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGRhiShaderEffectNode that has no cute function yet,
    '__init__', 'garbageCollectMaterialTypeCache',
    'handleTextureProviderDestroyed', 'resetMaterialTypeCache', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiShaderEffectNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGRhiShaderEffectNode::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGRhiShaderEffectNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QSGRhiShaderEffectNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's
    'QSGRhiShaderEffectNode::QSGRhiShaderEffectNode(QSGDefaultRenderContext
    *rc)': leans on 'vtable for QSGRhiShaderEffectNode', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QSGRhiShaderEffectNode.__init__' has no cute function yet. Qt's "
        "'QSGRhiShaderEffectNode::QSGRhiShaderEffectNode(QSGDefaultRenderCon"
        "text *rc)': leans on 'vtable for QSGRhiShaderEffectNode', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(bool)
  def updateNormalizedTextureSubRect(
      self,
      supportsAtlasTextures: bool,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF
    QSGRhiShaderEffectNode::updateNormalizedTextureSubRect(bool
    supportsAtlasTextures)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectnode.html

    Parameters
    ----------

    supportsAtlasTextures : bool
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGRhiShaderEffectNode::updateNormalizedTextureSubRect(bool
    #      supportsAtlasTextures)
    ritual = (
        'ritual_ZN22QSGRhiShaderEffectNode30updateNormalizedTextureSubRectE'
        'b')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSGRhiShaderEffectNode30updateNormalizedTextureSu'
          'bRectEb')
    address = self.uglySide.call(ritual, supportsAtlasTextures)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QSGShaderEffectNode.SyncData)
  @overload(NoneType)
  def syncMaterial(
      self,
      syncData: Optional[QSGShaderEffectNode.SyncData],
  ) -> None:
    """
    Calls Qt's 'void QSGRhiShaderEffectNode::syncMaterial(SyncData
    *syncData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectnode.html#syncMaterial

    Parameters
    ----------

    syncData : Optional[QSGShaderEffectNode.SyncData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiShaderEffectNode::syncMaterial(SyncData *syncData)
    self.uglySide.call(
        'ritual_ZN22QSGRhiShaderEffectNode12syncMaterialEPN19QSGShaderEffec'
        'tNode8SyncDataE',
        self._addressOf(syncData),
    )

  def preprocess(self) -> None:
    """
    Calls Qt's 'void QSGRhiShaderEffectNode::preprocess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectnode.html#preprocess
    """
    #  void QSGRhiShaderEffectNode::preprocess()
    ritual = 'ritual_ZN22QSGRhiShaderEffectNode10preprocessEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSGRhiShaderEffectNode10preprocessEv'
    self.uglySide.call(ritual)

  def handleTextureChange(self) -> None:
    """
    Calls Qt's 'void QSGRhiShaderEffectNode::handleTextureChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhishadereffectnode.html#handleTextureChange
    """
    #  void QSGRhiShaderEffectNode::handleTextureChange()
    self.uglySide.call(
        'ritual_ZN22QSGRhiShaderEffectNode19handleTextureChangeEv',
    )

  @staticmethod
  def garbageCollectMaterialTypeCache(*__, **_) -> Never:
    """
    Qt's 'void QSGRhiShaderEffectNode::garbageCollectMaterialTypeCache(void
    *materialTypeCacheKey)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'shaderMaterialTypeCacheMutex'.
    """
    raise NotImplementedError(
        "'QSGRhiShaderEffectNode.garbageCollectMaterialTypeCache' has no "
        "cute function yet. Qt's 'void "
        "QSGRhiShaderEffectNode::garbageCollectMaterialTypeCache(void "
        "*materialTypeCacheKey)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'shaderMaterialTypeCacheMutex'.")

  @staticmethod
  def handleTextureProviderDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QSGRhiShaderEffectNode::handleTextureProviderDestroyed(QObject
    *object)': the compiler refuses its ritual as it would be written here:
    redefinition of 'object' with a different type: 'const QObject *' vs
    'QObject *'.
    """
    raise NotImplementedError(
        "'QSGRhiShaderEffectNode.handleTextureProviderDestroyed' has no "
        "cute function yet. Qt's 'void "
        "QSGRhiShaderEffectNode::handleTextureProviderDestroyed(QObject "
        "*object)': the compiler refuses its ritual as it would be written "
        "here: redefinition of 'object' with a different type: 'const "
        "QObject *' vs 'QObject *'.")

  @staticmethod
  def resetMaterialTypeCache(*__, **_) -> Never:
    """
    Qt's 'void QSGRhiShaderEffectNode::resetMaterialTypeCache(void
    *materialTypeCacheKey)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'shaderMaterialTypeCacheMutex'.
    """
    raise NotImplementedError(
        "'QSGRhiShaderEffectNode.resetMaterialTypeCache' has no cute "
        "function yet. Qt's 'void "
        "QSGRhiShaderEffectNode::resetMaterialTypeCache(void "
        "*materialTypeCacheKey)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'shaderMaterialTypeCacheMutex'.")
