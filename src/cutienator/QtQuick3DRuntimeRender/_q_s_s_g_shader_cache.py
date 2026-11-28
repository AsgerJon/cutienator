"""
QSSGShaderCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderCache to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick3DUtils import QQsbCollection
from . import QSSGRhiShaderPipeline

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtGui import QRhi
  from ..QtShaderTools import QShaderBaker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']
  QShaderBaker = WAIT['QShaderBaker']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGShaderCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderCache: a plain Python object standing in
  front of one C++ QSSGShaderCache.

  What exists
  -----------

  Every function of Qt's QSSGShaderCache that has a ritual and that Python
  can call so far, 5 names in all: 'releaseCachedResources',
  'resourceFolder', 'shaderCollectionFile', 'particleShaderCollectionFile',
  'initBakerForPersistentUse'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRhiShaderPipelinePtr QSSGShaderCache::loadBuiltinUncached(const
    QByteArray &inKey, int viewCount, QSSGRhiShaderPipeline::StageFlags
    vertexStageFlags)': gives a type Python has no way to take yet.
  - Qt's 'void QSSGShaderCache::addShaderPreprocessor(QByteArray &str, const
    QByteArray &inKey, ShaderType shaderType, const QSSGShaderFeatures
    &inFeatures, const QSSGUserShaderAugmentation &shaderAugmentation, int
    viewCount)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGShaderCache::~QSSGShaderCache()': the destructor: Python never
    removes a C++ QSSGShaderCache.
  - Qt's 'QSSGRhiContext &QSSGShaderCache::rhiContext()': gives a type Python
    has no way to take yet.
  - Qt's 'QQsbInMemoryCollection
    &QSSGShaderCache::persistentShaderBakingCache()': gives a type Python has
    no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGShaderCache::tryGetRhiShaderPipeline(const QByteArray &inKey, const
    QSSGShaderFeatures &inFeatures)': gives a type Python has no way to take
    yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGShaderCache::tryNewPipelineFromPersistentCache(const QByteArray
    &qsbcKey, const QByteArray &inKey, const QSSGShaderFeatures &inFeatures,
    QSSGRhiShaderPipeline::StageFlags stageFlags)': gives a type Python has
    no way to take yet.
  - Qt's 'QSSGRhiShaderPipelinePtr
    QSSGShaderCache::newPipelineFromPregenerated(const QByteArray &inKey,
    const QSSGShaderFeatures &inFeatures, QQsbCollection::Entry entry, const
    QSSGRenderGraphObject &obj, QSSGRhiShaderPipeline::StageFlags
    stageFlags)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRhiShaderPipelinePtr QSSGShaderCache::compileForRhi(const
    QByteArray &inKey, const QByteArray &inVert, const QByteArray &inFrag,
    const QSSGShaderFeatures &inFeatures, QSSGRhiShaderPipeline::StageFlags
    stageFlags, const QSSGUserShaderAugmentation &shaderAugmentation, int
    viewCount, bool perTargetCompilation)': gives a type Python has no way to
    take yet.
  - Qt's 'QSSGBuiltInRhiShaderCache
    &QSSGShaderCache::getBuiltInRhiShaders()': gives a type Python has no way
    to take yet.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 2 forbidden; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QSSGShaderCache is created at the first use, not by
    'QSSGShaderCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGShaderCache.
  - Each name of Qt's QSSGShaderCache that has no cute function yet,
    '__init__', 'addShaderPreprocessor', 'compileForRhi',
    'getBuiltInRhiShaders', 'loadBuiltinUncached',
    'newPipelineFromPregenerated', 'persistentShaderBakingCache',
    'rhiContext', 'tryGetRhiShaderPipeline',
    'tryNewPipelineFromPersistentCache', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGShaderCache, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ShaderType(CuteNum, scoped=True):
    """
    The enum 'QSSGShaderCache::ShaderType' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Vertex = Kee[int](0)
    Fragment = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def resourceFolder() -> QByteArray:
    """
    Calls Qt's 'QByteArray QSSGShaderCache::resourceFolder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercache.html#resourceFolder

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSSGShaderCache::resourceFolder()
    address = Rituals.call('ritual_ZN15QSSGShaderCache14resourceFolderEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def shaderCollectionFile() -> QByteArray:
    """
    Calls Qt's 'QByteArray QSSGShaderCache::shaderCollectionFile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercache.html#shaderCollectionFile

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSSGShaderCache::shaderCollectionFile()
    address = Rituals.call(
        'ritual_ZN15QSSGShaderCache20shaderCollectionFileEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def particleShaderCollectionFile() -> QByteArray:
    """
    Calls Qt's 'QByteArray QSSGShaderCache::particleShaderCollectionFile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercache.html#particleShaderCollectionFile

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSSGShaderCache::particleShaderCollectionFile()
    address = Rituals.call(
        'ritual_ZN15QSSGShaderCache28particleShaderCollectionFileEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QShaderBaker, QRhi)
  @overload(QShaderBaker, NoneType)
  @overload(NoneType, QRhi)
  @overload(NoneType, NoneType)
  def initBakerForPersistentUse(
      baker: Optional[QShaderBaker],
      rhi: Optional[QRhi],
  ) -> None:
    """
    Calls Qt's 'void QSSGShaderCache::initBakerForPersistentUse(QShaderBaker
    *baker, QRhi *rhi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercache.html#initBakerForPersistentUse

    Parameters
    ----------

    baker : Optional[QShaderBaker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGShaderCache::initBakerForPersistentUse(QShaderBaker *baker,
    #      QRhi *rhi)
    Rituals.call(
        'ritual_ZN15QSSGShaderCache25initBakerForPersistentUseEP12QShaderBa'
        'kerP4QRhi',
        CuteMixin._addressOf(baker), CuteMixin._addressOf(rhi),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderCache'

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
    Qt's 'QSSGShaderCache::QSSGShaderCache(QSSGRhiContext &ctx, const
    InitBakerFunc initBakeFn)': takes or gives a type that cannot be passed
    yet: void (*const)(QShaderBaker *, QRhi *).
    """
    raise NotImplementedError(
        "'QSSGShaderCache.__init__' has no cute function yet. Qt's "
        "'QSSGShaderCache::QSSGShaderCache(QSSGRhiContext &ctx, const "
        "InitBakerFunc initBakeFn)': takes or gives a type that cannot be "
        "passed yet: void (*const)(QShaderBaker *, QRhi *).")

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

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QSSGShaderCache::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadercache.html#releaseCachedResources
    """
    #  void QSSGShaderCache::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN15QSSGShaderCache22releaseCachedResourcesEv',
    )

  @staticmethod
  def addShaderPreprocessor(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderCache::addShaderPreprocessor(QByteArray &str, const
    QByteArray &inKey, ShaderType shaderType, const QSSGShaderFeatures
    &inFeatures, const QSSGUserShaderAugmentation &shaderAugmentation, int
    viewCount)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.addShaderPreprocessor' has no cute function yet. "
        "Qt's 'void QSSGShaderCache::addShaderPreprocessor(QByteArray &str, "
        "const QByteArray &inKey, ShaderType shaderType, const "
        "QSSGShaderFeatures &inFeatures, const QSSGUserShaderAugmentation "
        "&shaderAugmentation, int viewCount)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def compileForRhi(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr QSSGShaderCache::compileForRhi(const
    QByteArray &inKey, const QByteArray &inVert, const QByteArray &inFrag,
    const QSSGShaderFeatures &inFeatures, QSSGRhiShaderPipeline::StageFlags
    stageFlags, const QSSGUserShaderAugmentation &shaderAugmentation, int
    viewCount, bool perTargetCompilation)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.compileForRhi' has no cute function yet. Qt's "
        "'QSSGRhiShaderPipelinePtr QSSGShaderCache::compileForRhi(const "
        "QByteArray &inKey, const QByteArray &inVert, const QByteArray "
        "&inFrag, const QSSGShaderFeatures &inFeatures, "
        "QSSGRhiShaderPipeline::StageFlags stageFlags, const "
        "QSSGUserShaderAugmentation &shaderAugmentation, int viewCount, "
        "bool perTargetCompilation)': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def getBuiltInRhiShaders(*__, **_) -> Never:
    """
    Qt's 'QSSGBuiltInRhiShaderCache
    &QSSGShaderCache::getBuiltInRhiShaders()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.getBuiltInRhiShaders' has no cute function yet. "
        "Qt's 'QSSGBuiltInRhiShaderCache "
        "&QSSGShaderCache::getBuiltInRhiShaders()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def loadBuiltinUncached(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr QSSGShaderCache::loadBuiltinUncached(const
    QByteArray &inKey, int viewCount, QSSGRhiShaderPipeline::StageFlags
    vertexStageFlags)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.loadBuiltinUncached' has no cute function yet. "
        "Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGShaderCache::loadBuiltinUncached(const QByteArray &inKey, int "
        "viewCount, QSSGRhiShaderPipeline::StageFlags vertexStageFlags)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def newPipelineFromPregenerated(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGShaderCache::newPipelineFromPregenerated(const QByteArray &inKey,
    const QSSGShaderFeatures &inFeatures, QQsbCollection::Entry entry, const
    QSSGRenderGraphObject &obj, QSSGRhiShaderPipeline::StageFlags
    stageFlags)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.newPipelineFromPregenerated' has no cute function "
        "yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGShaderCache::newPipelineFromPregenerated(const QByteArray "
        "&inKey, const QSSGShaderFeatures &inFeatures, "
        "QQsbCollection::Entry entry, const QSSGRenderGraphObject &obj, "
        "QSSGRhiShaderPipeline::StageFlags stageFlags)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def persistentShaderBakingCache(*__, **_) -> Never:
    """
    Qt's 'QQsbInMemoryCollection
    &QSSGShaderCache::persistentShaderBakingCache()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.persistentShaderBakingCache' has no cute function "
        "yet. Qt's 'QQsbInMemoryCollection "
        "&QSSGShaderCache::persistentShaderBakingCache()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def rhiContext(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiContext &QSSGShaderCache::rhiContext()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.rhiContext' has no cute function yet. Qt's "
        "'QSSGRhiContext &QSSGShaderCache::rhiContext()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def tryGetRhiShaderPipeline(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGShaderCache::tryGetRhiShaderPipeline(const QByteArray &inKey, const
    QSSGShaderFeatures &inFeatures)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.tryGetRhiShaderPipeline' has no cute function "
        "yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGShaderCache::tryGetRhiShaderPipeline(const QByteArray &inKey, "
        "const QSSGShaderFeatures &inFeatures)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def tryNewPipelineFromPersistentCache(*__, **_) -> Never:
    """
    Qt's 'QSSGRhiShaderPipelinePtr
    QSSGShaderCache::tryNewPipelineFromPersistentCache(const QByteArray
    &qsbcKey, const QByteArray &inKey, const QSSGShaderFeatures &inFeatures,
    QSSGRhiShaderPipeline::StageFlags stageFlags)': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGShaderCache.tryNewPipelineFromPersistentCache' has no cute "
        "function yet. Qt's 'QSSGRhiShaderPipelinePtr "
        "QSSGShaderCache::tryNewPipelineFromPersistentCache(const "
        "QByteArray &qsbcKey, const QByteArray &inKey, const "
        "QSSGShaderFeatures &inFeatures, QSSGRhiShaderPipeline::StageFlags "
        "stageFlags)': gives a type Python has no way to take yet.")
