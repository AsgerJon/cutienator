"""
QQuick3DResourceLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dresourceloader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DResourceLoader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DSceneManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DResourceLoader(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DResourceLoader: a plain Python object
  standing in front of one C++ QQuick3DResourceLoader.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DResourceLoader is
  built on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DResourceLoader that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'meshSources',
  'setMeshSources', 'meshSourcesChanged', 'onGeometryDestroyed',
  'onTextureDestroyed', 'updateSpatialNode', 'markAllDirty', 'itemChange',
  'updateSceneManager'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DResourceLoader::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DResourceLoader::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QQuick3DGeometry>
    QQuick3DResourceLoader::geometries()': gives a type Python has no way to
    take yet.
  - Qt's 'QQmlListProperty<QQuick3DTexture>
    QQuick3DResourceLoader::textures()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuick3DResourceLoader::qmlAppendGeometry(
    QQmlListProperty<QQuick3DGeometry> *list, QQuick3DGeometry *geometry)':
    names 'QQmlListProperty<QQuick3DGeometry>', which has no cute class yet.
  - Qt's 'QQuick3DGeometry
    *QQuick3DResourceLoader::qmlGeometryAt(QQmlListProperty<QQuick3DGeometry>
    *list, qsizetype index)': names 'QQmlListProperty<QQuick3DGeometry>',
    which has no cute class yet.
  - Qt's 'qsizetype QQuick3DResourceLoader::qmlGeometriesCount(
    QQmlListProperty<QQuick3DGeometry> *list)': names
    'QQmlListProperty<QQuick3DGeometry>', which has no cute class yet.
  - Qt's 'void QQuick3DResourceLoader::qmlClearGeometries(
    QQmlListProperty<QQuick3DGeometry> *list)': names
    'QQmlListProperty<QQuick3DGeometry>', which has no cute class yet.
  - Qt's 'void QQuick3DResourceLoader::qmlAppendTexture(
    QQmlListProperty<QQuick3DTexture> *list, QQuick3DTexture *texture)':
    names 'QQmlListProperty<QQuick3DTexture>', which has no cute class yet.
  - Qt's 'QQuick3DTexture
    *QQuick3DResourceLoader::qmlTextureAt(QQmlListProperty<QQuick3DTexture>
    *list, qsizetype index)': names 'QQmlListProperty<QQuick3DTexture>',
    which has no cute class yet.
  - Qt's 'qsizetype QQuick3DResourceLoader::qmlTexturesCount(
    QQmlListProperty<QQuick3DTexture> *list)': names
    'QQmlListProperty<QQuick3DTexture>', which has no cute class yet.
  - Qt's 'void QQuick3DResourceLoader::qmlClearTextures(
    QQmlListProperty<QQuick3DTexture> *list)': names
    'QQmlListProperty<QQuick3DTexture>', which has no cute class yet.
  - Qt's 'void QQuick3DResourceLoader::markDirty(ResourceLoaderDirtyType
    type)': names the enum 'QQuick3DResourceLoader::ResourceLoaderDirtyType',
    whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DResourceLoader is created at the first use, not by
    'QQuick3DResourceLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DResourceLoader.
  - Qt tells when it has removed the C++ QQuick3DResourceLoader. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DResourceLoader that has no cute function yet,
    'geometries', 'markDirty', 'qmlAppendGeometry', 'qmlAppendTexture',
    'qmlClearGeometries', 'qmlClearTextures', 'qmlGeometriesCount',
    'qmlGeometryAt', 'qmlTextureAt', 'qmlTexturesCount', 'textures', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuick3DResourceLoader::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dresourceloader.html#tr

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
    #  QString QQuick3DResourceLoader::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuick3DResourceLoader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DResourceLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DResourceLoader::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DResourceLoader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DResourceLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def meshSources(self) -> QList[QUrl]:
    """
    Calls Qt's 'const QList<QUrl> &QQuick3DResourceLoader::meshSources()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#meshSources

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QUrl> &QQuick3DResourceLoader::meshSources() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DResourceLoader11meshSourcesEv',
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QUrl])
  def setMeshSources(self, newMeshSources: QList[QUrl]) -> None:
    """
    Calls Qt's 'void QQuick3DResourceLoader::setMeshSources(const QList<QUrl>
    &newMeshSources)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#setMeshSources

    Parameters
    ----------

    newMeshSources : QList[QUrl]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuick3DResourceLoader::setMeshSources(const QList<QUrl>
    #      &newMeshSources)
    self.uglySide.call(
        'ritual_ZN22QQuick3DResourceLoader14setMeshSourcesERK5QListI4QUrlE',
        self._valueOf(newMeshSources),
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
    'QQuick3DResourceLoader::QQuick3DResourceLoader(QQuick3DObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#QQuick3DResourceLoader

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DResourceLoader::QQuick3DResourceLoader(QQuick3DObject *parent)
    self._noteCreation(QQuick3DResourceLoader, lambda: Rituals.call(
        'ritual_ZN22QQuick3DResourceLoaderC1EP14QQuick3DObject',
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

  def meshSourcesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DResourceLoader::meshSourcesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#meshSourcesChanged
    """
    #  void QQuick3DResourceLoader::meshSourcesChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DResourceLoader18meshSourcesChangedEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def onGeometryDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DResourceLoader::onGeometryDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#onGeometryDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DResourceLoader::onGeometryDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN22QQuick3DResourceLoader19onGeometryDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def onTextureDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DResourceLoader::onTextureDestroyed(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#onTextureDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DResourceLoader::onTextureDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN22QQuick3DResourceLoader18onTextureDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DResourceLoader::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#updateSpatialNode

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
    #      *QQuick3DResourceLoader::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN22QQuick3DResourceLoader17updateSpatialNodeEP21QSSGRender'
        'GraphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuick3DResourceLoader17updateSpatialNodeEP21QSSG'
          'RenderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DResourceLoader::markAllDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#markAllDirty
    """
    #  void QQuick3DResourceLoader::markAllDirty()
    ritual = 'ritual_ZN22QQuick3DResourceLoader12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuick3DResourceLoader12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      change: QQuick3DObject.ItemChange,
      value: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DResourceLoader::itemChange(ItemChange change,
    const ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#itemChange

    Parameters
    ----------

    change : QQuick3DObject.ItemChange
      Passed on as its number.

    value : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DResourceLoader::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN22QQuick3DResourceLoader10itemChangeEN14QQuick3DObject10I'
        'temChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuick3DResourceLoader10itemChangeEN14QQuick3DObj'
          'ect10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QQuick3DSceneManager)
  @overload(NoneType)
  def updateSceneManager(
      self,
      sceneManager: Optional[QQuick3DSceneManager],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DResourceLoader::updateSceneManager(QQuick3DSceneManager
    *sceneManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dresourceloader.html#updateSceneManager

    Parameters
    ----------

    sceneManager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DResourceLoader::updateSceneManager(QQuick3DSceneManager
    #      *sceneManager)
    self.uglySide.call(
        'ritual_ZN22QQuick3DResourceLoader18updateSceneManagerEP20QQuick3DS'
        'ceneManager',
        self._addressOf(sceneManager),
    )

  @staticmethod
  def geometries(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DGeometry>
    QQuick3DResourceLoader::geometries()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.geometries' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DGeometry> "
        "QQuick3DResourceLoader::geometries()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DResourceLoader::markDirty(ResourceLoaderDirtyType
    type)': names the enum 'QQuick3DResourceLoader::ResourceLoaderDirtyType',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.markDirty' has no cute function yet. Qt's "
        "'void QQuick3DResourceLoader::markDirty(ResourceLoaderDirtyType "
        "type)': names the enum "
        "'QQuick3DResourceLoader::ResourceLoaderDirtyType', whose class "
        "cannot be named here.")

  @staticmethod
  def qmlAppendGeometry(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DResourceLoader::qmlAppendGeometry(
    QQmlListProperty<QQuick3DGeometry> *list, QQuick3DGeometry *geometry)':
    names 'QQmlListProperty<QQuick3DGeometry>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.qmlAppendGeometry' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DResourceLoader::qmlAppendGeometry(QQmlListProperty<QQuick3D"
        "Geometry> *list, QQuick3DGeometry *geometry)': names "
        "'QQmlListProperty<QQuick3DGeometry>', which has no cute class yet.")

  @staticmethod
  def qmlAppendTexture(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DResourceLoader::qmlAppendTexture(
    QQmlListProperty<QQuick3DTexture> *list, QQuick3DTexture *texture)':
    names 'QQmlListProperty<QQuick3DTexture>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.qmlAppendTexture' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DResourceLoader::qmlAppendTexture(QQmlListProperty<QQuick3DT"
        "exture> *list, QQuick3DTexture *texture)': names "
        "'QQmlListProperty<QQuick3DTexture>', which has no cute class yet.")

  @staticmethod
  def qmlClearGeometries(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DResourceLoader::qmlClearGeometries(
    QQmlListProperty<QQuick3DGeometry> *list)': names
    'QQmlListProperty<QQuick3DGeometry>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.qmlClearGeometries' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DResourceLoader::qmlClearGeometries(QQmlListProperty<QQuick3"
        "DGeometry> *list)': names 'QQmlListProperty<QQuick3DGeometry>', "
        "which has no cute class yet.")

  @staticmethod
  def qmlClearTextures(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DResourceLoader::qmlClearTextures(
    QQmlListProperty<QQuick3DTexture> *list)': names
    'QQmlListProperty<QQuick3DTexture>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.qmlClearTextures' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DResourceLoader::qmlClearTextures(QQmlListProperty<QQuick3DT"
        "exture> *list)': names 'QQmlListProperty<QQuick3DTexture>', which "
        "has no cute class yet.")

  @staticmethod
  def qmlGeometriesCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DResourceLoader::qmlGeometriesCount(
    QQmlListProperty<QQuick3DGeometry> *list)': names
    'QQmlListProperty<QQuick3DGeometry>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.qmlGeometriesCount' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuick3DResourceLoader::qmlGeometriesCount(QQmlListProperty<QQuick3"
        "DGeometry> *list)': names 'QQmlListProperty<QQuick3DGeometry>', "
        "which has no cute class yet.")

  @staticmethod
  def qmlGeometryAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DGeometry
    *QQuick3DResourceLoader::qmlGeometryAt(QQmlListProperty<QQuick3DGeometry>
    *list, qsizetype index)': names 'QQmlListProperty<QQuick3DGeometry>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.qmlGeometryAt' has no cute function yet. "
        "Qt's 'QQuick3DGeometry "
        "*QQuick3DResourceLoader::qmlGeometryAt(QQmlListProperty<QQuick3DGeo"
        "metry> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DGeometry>', which has no cute class yet.")

  @staticmethod
  def qmlTextureAt(*__, **_) -> Never:
    """
    Qt's 'QQuick3DTexture
    *QQuick3DResourceLoader::qmlTextureAt(QQmlListProperty<QQuick3DTexture>
    *list, qsizetype index)': names 'QQmlListProperty<QQuick3DTexture>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.qmlTextureAt' has no cute function yet. "
        "Qt's 'QQuick3DTexture "
        "*QQuick3DResourceLoader::qmlTextureAt(QQmlListProperty<QQuick3DText"
        "ure> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuick3DTexture>', which has no cute class yet.")

  @staticmethod
  def qmlTexturesCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuick3DResourceLoader::qmlTexturesCount(
    QQmlListProperty<QQuick3DTexture> *list)': names
    'QQmlListProperty<QQuick3DTexture>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.qmlTexturesCount' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuick3DResourceLoader::qmlTexturesCount(QQmlListProperty<QQuick3DT"
        "exture> *list)': names 'QQmlListProperty<QQuick3DTexture>', which "
        "has no cute class yet.")

  @staticmethod
  def textures(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DTexture>
    QQuick3DResourceLoader::textures()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuick3DResourceLoader.textures' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuick3DTexture> "
        "QQuick3DResourceLoader::textures()': gives a type Python has no "
        "way to take yet.")
