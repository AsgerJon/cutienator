"""
QQuick3DRuntimeLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qquick3druntimeloader_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DRuntimeLoader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QMimeType, QUrl
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from ..QtQuick3D import QQuick3DBounds3, QQuick3DInstancing, QQuick3DNode
  from ..QtQuick3D import QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DInstancing = WAIT['QQuick3DInstancing']
  QQuick3DNode = WAIT['QQuick3DNode']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DRuntimeLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DRuntimeLoader: a plain Python object standing
  in front of one C++ QQuick3DRuntimeLoader.

  What exists
  -----------

  Every function of Qt's QQuick3DRuntimeLoader that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'componentComplete', 'supportedExtensions',
  'supportedMimeTypes', 'status', 'errorString', 'bounds', 'instancing',
  'setInstancing', 'query', 'queryAll', 'sourceChanged', 'statusChanged',
  'errorStringChanged', 'boundsChanged', 'instancingChanged',
  'updateSpatialNode', 'calculateBounds', 'loadSource', 'updateModels'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DRuntimeLoader::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DRuntimeLoader::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DRuntimeLoader is created at the first use, not by
    'QQuick3DRuntimeLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DRuntimeLoader.
  - Qt tells when it has removed the C++ QQuick3DRuntimeLoader. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DRuntimeLoader, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class QueryFilter(CuteNum, scoped=True):
    """
    The enum 'QQuick3DRuntimeLoader::QueryFilter' of Qt, with the 6 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Textures = Kee[int](0)
    Materials = Kee[int](1)
    Nodes = Kee[int](2)
    Cameras = Kee[int](3)
    Lights = Kee[int](4)
    Models = Kee[int](5)

  class Status(CuteNum, scoped=True):
    """
    The enum 'QQuick3DRuntimeLoader::Status' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Empty = Kee[int](0)
    Success = Kee[int](1)
    Error = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DRuntimeLoader::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3druntimeloader.html#tr

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
    #  QString QQuick3DRuntimeLoader::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DRuntimeLoader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def supportedExtensions() -> QStringList:
    """
    Calls Qt's 'QStringList QQuick3DRuntimeLoader::supportedExtensions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#supportedExtensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuick3DRuntimeLoader::supportedExtensions()
    address = Rituals.call(
        'ritual_ZN21QQuick3DRuntimeLoader19supportedExtensionsEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def supportedMimeTypes() -> QList[QMimeType]:
    """
    Calls Qt's 'QList<QMimeType>
    QQuick3DRuntimeLoader::supportedMimeTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#supportedMimeTypes

    Returns
    -------

    QList[QMimeType]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QMimeType> QQuick3DRuntimeLoader::supportedMimeTypes()
    address = Rituals.call(
        'ritual_ZN21QQuick3DRuntimeLoader18supportedMimeTypesEv',
    )
    from ..QtCore import QMimeType
    return QList[QMimeType]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DRuntimeLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DRuntimeLoader::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DRuntimeLoader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DRuntimeLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DRuntimeLoader::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3druntimeloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DRuntimeLoader::source() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DRuntimeLoader6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuick3DRuntimeLoader::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3druntimeloader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuick3DRuntimeLoader::status() const
    return QQuick3DRuntimeLoader.Status(self.uglySide.call(
        'ritual_ZNK21QQuick3DRuntimeLoader6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QQuick3DRuntimeLoader::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DRuntimeLoader::errorString() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DRuntimeLoader11errorStringEv',
    )

  def bounds(self) -> QQuick3DBounds3:
    """
    Calls Qt's 'const QQuick3DBounds3 &QQuick3DRuntimeLoader::bounds()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3druntimeloader.html#bounds

    Returns
    -------

    QQuick3DBounds3
      A new cute QQuick3DBounds3 around the copy Qt gave back. Python owns
      it.
    """
    #  const QQuick3DBounds3 &QQuick3DRuntimeLoader::bounds() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DRuntimeLoader6boundsEv',
    )
    from ..QtQuick3D import QQuick3DBounds3
    return QQuick3DBounds3._cuteOwning(address)

  def instancing(self) -> Optional[QQuick3DInstancing]:
    """
    Calls Qt's 'QQuick3DInstancing *QQuick3DRuntimeLoader::instancing()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#instancing

    Returns
    -------

    Optional[QQuick3DInstancing]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstancing *QQuick3DRuntimeLoader::instancing() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DRuntimeLoader10instancingEv',
    )
    from ..QtQuick3D import QQuick3DInstancing
    return QQuick3DInstancing._cuteAt(address)

  @overload(str)
  def query(self, name: str) -> Optional[QQuick3DObject]:
    """
    Calls Qt's 'QQuick3DObject *QQuick3DRuntimeLoader::query(const QString
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3druntimeloader.html#query

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQuick3DObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DObject *QQuick3DRuntimeLoader::query(const QString &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DRuntimeLoader5queryERK7QString', name,
    )
    from ..QtQuick3D import QQuick3DObject
    return QQuick3DObject._cuteAt(address)

  @overload(QueryFilter)
  def queryAll(self, filter: QueryFilter) -> QList[QQuick3DObject]:
    """
    Calls Qt's 'QList<QQuick3DObject *>
    QQuick3DRuntimeLoader::queryAll(QueryFilter filter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#queryAll

    Parameters
    ----------

    filter : QueryFilter
      Passed on as its number.

    Returns
    -------

    QList[QQuick3DObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DObject *> QQuick3DRuntimeLoader::queryAll(QueryFilter
    #      filter) const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DRuntimeLoader8queryAllENS_11QueryFilterE',
        filter.value,
    )
    from ..QtQuick3D import QQuick3DObject
    return QList[QQuick3DObject]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, newSource: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::setSource(const QUrl
    &newSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#setSource

    Parameters
    ----------

    newSource : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DRuntimeLoader::setSource(const QUrl &newSource)
    self.uglySide.call(
        'ritual_ZN21QQuick3DRuntimeLoader9setSourceERK4QUrl',
        self._valueOf(newSource),
    )

  @overload(QQuick3DInstancing)
  @overload(NoneType)
  def setInstancing(
      self,
      newInstancing: Optional[QQuick3DInstancing],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::setInstancing(QQuick3DInstancing
    *newInstancing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#setInstancing

    Parameters
    ----------

    newInstancing : Optional[QQuick3DInstancing]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DRuntimeLoader::setInstancing(QQuick3DInstancing
    #      *newInstancing)
    self.uglySide.call(
        'ritual_ZN21QQuick3DRuntimeLoader13setInstancingEP18QQuick3DInstanc'
        'ing',
        self._addressOf(newInstancing),
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DRuntimeLoader::QQuick3DRuntimeLoader(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#QQuick3DRuntimeLoader

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DRuntimeLoader::QQuick3DRuntimeLoader(QQuick3DNode *parent)
    self._noteCreation(QQuick3DRuntimeLoader, lambda: Rituals.call(
        'ritual_ZN21QQuick3DRuntimeLoaderC1EP12QQuick3DNode',
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#componentComplete
    """
    #  void QQuick3DRuntimeLoader::componentComplete()
    ritual = 'ritual_ZN21QQuick3DRuntimeLoader17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuick3DRuntimeLoader17componentCompleteEv'
    self.uglySide.call(ritual)

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#sourceChanged
    """
    #  void QQuick3DRuntimeLoader::sourceChanged()
    self.uglySide.call('ritual_ZN21QQuick3DRuntimeLoader13sourceChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#statusChanged
    """
    #  void QQuick3DRuntimeLoader::statusChanged()
    self.uglySide.call('ritual_ZN21QQuick3DRuntimeLoader13statusChangedEv')

  def errorStringChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::errorStringChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#errorStringChanged
    """
    #  void QQuick3DRuntimeLoader::errorStringChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DRuntimeLoader18errorStringChangedEv',
    )

  def boundsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::boundsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#boundsChanged
    """
    #  void QQuick3DRuntimeLoader::boundsChanged()
    self.uglySide.call('ritual_ZN21QQuick3DRuntimeLoader13boundsChangedEv')

  def instancingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::instancingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#instancingChanged
    """
    #  void QQuick3DRuntimeLoader::instancingChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DRuntimeLoader17instancingChangedEv',
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DRuntimeLoader::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#updateSpatialNode

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
    #      *QQuick3DRuntimeLoader::updateSpatialNode(QSSGRenderGraphObject
    #      *node)
    ritual = (
        'ritual_ZN21QQuick3DRuntimeLoader17updateSpatialNodeEP21QSSGRenderG'
        'raphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuick3DRuntimeLoader17updateSpatialNodeEP21QSSGR'
          'enderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def calculateBounds(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::calculateBounds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#calculateBounds
    """
    #  void QQuick3DRuntimeLoader::calculateBounds()
    self.uglySide.call('ritual_ZN21QQuick3DRuntimeLoader15calculateBoundsEv')

  def loadSource(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::loadSource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#loadSource
    """
    #  void QQuick3DRuntimeLoader::loadSource()
    self.uglySide.call('ritual_ZN21QQuick3DRuntimeLoader10loadSourceEv')

  def updateModels(self) -> None:
    """
    Calls Qt's 'void QQuick3DRuntimeLoader::updateModels()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3druntimeloader.html#updateModels
    """
    #  void QQuick3DRuntimeLoader::updateModels()
    self.uglySide.call('ritual_ZN21QQuick3DRuntimeLoader12updateModelsEv')
