"""
QQuick3DSceneManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenemanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DSceneManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickWindow
  from . import QQuick3DNode, QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DNode = WAIT['QQuick3DNode']
  QQuick3DObject = WAIT['QQuick3DObject']
  QQuickWindow = WAIT['QQuickWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DSceneManager(QObject):
  """
  The cute side of Qt's QQuick3DSceneManager: a plain Python object standing
  in front of one C++ QQuick3DSceneManager.

  It is built on the cute 'QObject', as Qt's QQuick3DSceneManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DSceneManager that has a ritual and that
  Python can call so far, 24 names in all: 'metaObject', 'tr', 'setWindow',
  'window', 'dirtyItem', 'requestUpdate', 'cleanup', 'polishItems',
  'forcePolish', 'sync', 'preSync', 'cleanupNodes',
  'updateDirtyResourceNodes', 'updateDirtySpatialNodes',
  'updateDiryExtensions', 'updateDirtyResourceSecondPass',
  'updateDirtyResource', 'updateDirtySpatialNode', 'lookUpNode',
  'resourceListIndex', 'nodeListIndex', 'extensionListIndex', 'needsUpdate',
  'windowChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DSceneManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DSceneManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DSceneManager::~QQuick3DSceneManager()': the destructor:
    Python never removes a C++ QQuick3DSceneManager.
  - Qt's 'void QQuick3DSceneManager::updateBoundingBoxes(QSSGBufferManager
    &mgr)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuick3DWindowAttachment
    *QQuick3DSceneManager::getOrSetWindowAttachment(QQuickWindow &window)':
    takes a type Python has no way to hand over yet.
  - Qt's 'SyncResult QQuick3DSceneManager::updateResources(QQuick3DObject
    **listHead)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuick3DSceneManager::updateNodes(QQuick3DObject **listHead)':
    takes a type Python has no way to hand over yet.
  - Qt's 'SyncResult QQuick3DSceneManager::updateExtensions(QQuick3DObject
    **listHead)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DSceneManager is created at the first use, not by
    'QQuick3DSceneManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSceneManager.
  - Qt tells when it has removed the C++ QQuick3DSceneManager. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DSceneManager that has no cute function yet,
    'getOrSetWindowAttachment', 'updateBoundingBoxes', 'updateExtensions',
    'updateNodes', 'updateResources', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DSceneManager, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ExtensionPriority(CuteNum, scoped=True):
    """
    The enum 'QQuick3DSceneManager::ExtensionPriority' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    RenderExtension = Kee[int](0)
    Count = Kee[int](1)

  class NodePriority(CuteNum, scoped=True):
    """
    The enum 'QQuick3DSceneManager::NodePriority' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Skeleton = Kee[int](0)
    Other = Kee[int](1)
    ModelWithInstanceRoot = Kee[int](2)
    Lights = Kee[int](3)
    Count = Kee[int](4)

  class ResourcePriority(CuteNum, scoped=True):
    """
    The enum 'QQuick3DSceneManager::ResourcePriority' of Qt, with the 4 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    TextureData = Kee[int](0)
    Texture = Kee[int](1)
    Other = Kee[int](2)
    Count = Kee[int](3)

  #  The classes Qt writes inside QQuick3DSceneManager, each a class in here
  #  as in C++.

  class LightmapSourceTracker(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DSceneManager::LightmapSourceTracker: a
    plain Python object standing in front of one C++
    QQuick3DSceneManager::LightmapSourceTracker.

    C++ hands a QQuick3DSceneManager::LightmapSourceTracker around as a copy,
    so every C++ QQuick3DSceneManager::LightmapSourceTracker behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuick3DSceneManager::LightmapSourceTracker yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQuick3DSceneManager::LightmapSourceTracker::~LightmapSourceTracker(
      )': the destructor: Python removes its C++
      QQuick3DSceneManager::LightmapSourceTracker by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQuick3DSceneManager::LightmapSourceTracker is created at the
      first use, not by 'QQuick3DSceneManager::LightmapSourceTracker(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DSceneManager::LightmapSourceTracker back
      gives a copy the ritual made for Python, in a new cute
      QQuick3DSceneManager::LightmapSourceTracker.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DSceneManager::LightmapSourceTracker'

    #  Qt's '~QQuick3DSceneManager::LightmapSourceTracker()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQuick3DSceneManager::LightmapSourceTracker behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN20QQuick3DSceneManager21LightmapSourceTrackerD1Ev')

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
    Calls Qt's 'QString QQuick3DSceneManager::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dscenemanager.html#tr

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
    #  QString QQuick3DSceneManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuick3DSceneManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QSSGRenderGraphObject.Type)
  def resourceListIndex(type: QSSGRenderGraphObject.Type) -> int:
    """
    Calls Qt's 'size_t
    QQuick3DSceneManager::resourceListIndex(QSSGRenderGraphObject::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#resourceListIndex

    Parameters
    ----------

    type : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  size_t QQuick3DSceneManager::resourceListIndex(QSSGRenderGraphObject::
    #      Type type)
    return Rituals.call(
        'ritual_ZN20QQuick3DSceneManager17resourceListIndexEN21QSSGRenderGr'
        'aphObject4TypeE',
        type.value,
    )

  @staticmethod
  @overload(QSSGRenderGraphObject.Type)
  def nodeListIndex(type: QSSGRenderGraphObject.Type) -> int:
    """
    Calls Qt's 'size_t
    QQuick3DSceneManager::nodeListIndex(QSSGRenderGraphObject::Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#nodeListIndex

    Parameters
    ----------

    type : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  size_t QQuick3DSceneManager::nodeListIndex(QSSGRenderGraphObject::Type
    #      type)
    return Rituals.call(
        'ritual_ZN20QQuick3DSceneManager13nodeListIndexEN21QSSGRenderGraphO'
        'bject4TypeE',
        type.value,
    )

  @staticmethod
  @overload(QSSGRenderGraphObject.Type)
  def extensionListIndex(type: QSSGRenderGraphObject.Type) -> int:
    """
    Calls Qt's 'size_t
    QQuick3DSceneManager::extensionListIndex(QSSGRenderGraphObject::Type
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#extensionListIndex

    Parameters
    ----------

    type : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  size_t
    #      QQuick3DSceneManager::extensionListIndex(QSSGRenderGraphObject::
    #      Type type)
    return Rituals.call(
        'ritual_ZN20QQuick3DSceneManager18extensionListIndexEN21QSSGRenderG'
        'raphObject4TypeE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSceneManager'

  #  A C++ QQuick3DSceneManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DSceneManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DSceneManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DSceneManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DSceneManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def lookUpNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QQuick3DObject]:
    """
    Calls Qt's 'QQuick3DObject *QQuick3DSceneManager::lookUpNode(const
    QSSGRenderGraphObject *node) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#lookUpNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuick3DObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DObject *QQuick3DSceneManager::lookUpNode(const
    #      QSSGRenderGraphObject *node) const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DSceneManager10lookUpNodeEPK21QSSGRenderGraphOb'
        'ject',
        self._addressOf(node),
    )
    from . import QQuick3DObject
    return QQuick3DObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickWindow)
  @overload(NoneType)
  def setWindow(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::setWindow(QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#setWindow

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneManager::setWindow(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager9setWindowEP12QQuickWindow',
        self._addressOf(window),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DSceneManager::QQuick3DSceneManager(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#QQuick3DSceneManager

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DSceneManager::QQuick3DSceneManager(QObject *parent)
    self._noteCreation(QQuick3DSceneManager, lambda: Rituals.call(
        'ritual_ZN20QQuick3DSceneManagerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuick3DSceneManager::window()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dscenemanager.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuick3DSceneManager::window()
    address = self.uglySide.call('ritual_ZN20QQuick3DSceneManager6windowEv')
    from ..QtQuick import QQuickWindow
    return QQuickWindow._cuteAt(address)

  @overload(QQuick3DObject)
  @overload(NoneType)
  def dirtyItem(self, item: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::dirtyItem(QQuick3DObject *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#dirtyItem

    Parameters
    ----------

    item : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneManager::dirtyItem(QQuick3DObject *item)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager9dirtyItemEP14QQuick3DObject',
        self._addressOf(item),
    )

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::requestUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#requestUpdate
    """
    #  void QQuick3DSceneManager::requestUpdate()
    self.uglySide.call('ritual_ZN20QQuick3DSceneManager13requestUpdateEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def cleanup(self, item: Optional[QSSGRenderGraphObject]) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::cleanup(QSSGRenderGraphObject
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dscenemanager.html#cleanup

    Parameters
    ----------

    item : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneManager::cleanup(QSSGRenderGraphObject *item)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager7cleanupEP21QSSGRenderGraphObject',
        self._addressOf(item),
    )

  def polishItems(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::polishItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#polishItems
    """
    #  void QQuick3DSceneManager::polishItems()
    self.uglySide.call('ritual_ZN20QQuick3DSceneManager11polishItemsEv')

  def forcePolish(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::forcePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#forcePolish
    """
    #  void QQuick3DSceneManager::forcePolish()
    self.uglySide.call('ritual_ZN20QQuick3DSceneManager11forcePolishEv')

  def sync(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dscenemanager.html#sync
    """
    #  void QQuick3DSceneManager::sync()
    self.uglySide.call('ritual_ZN20QQuick3DSceneManager4syncEv')

  def preSync(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::preSync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dscenemanager.html#preSync
    """
    #  void QQuick3DSceneManager::preSync()
    self.uglySide.call('ritual_ZN20QQuick3DSceneManager7preSyncEv')

  def cleanupNodes(self) -> int:
    """
    Calls Qt's 'SyncResult QQuick3DSceneManager::cleanupNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#cleanupNodes
    """
    #  SyncResult QQuick3DSceneManager::cleanupNodes()
    return self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager12cleanupNodesEv',
    )

  def updateDirtyResourceNodes(self) -> int:
    """
    Calls Qt's 'SyncResult QQuick3DSceneManager::updateDirtyResourceNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#updateDirtyResourceNodes
    """
    #  SyncResult QQuick3DSceneManager::updateDirtyResourceNodes()
    return self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager24updateDirtyResourceNodesEv',
    )

  def updateDirtySpatialNodes(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::updateDirtySpatialNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#updateDirtySpatialNodes
    """
    #  void QQuick3DSceneManager::updateDirtySpatialNodes()
    self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager23updateDirtySpatialNodesEv',
    )

  def updateDiryExtensions(self) -> int:
    """
    Calls Qt's 'SyncResult QQuick3DSceneManager::updateDiryExtensions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#updateDiryExtensions
    """
    #  SyncResult QQuick3DSceneManager::updateDiryExtensions()
    return self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager20updateDiryExtensionsEv',
    )

  def updateDirtyResourceSecondPass(self) -> int:
    """
    Calls Qt's 'SyncResult
    QQuick3DSceneManager::updateDirtyResourceSecondPass()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html
    """
    #  SyncResult QQuick3DSceneManager::updateDirtyResourceSecondPass()
    return self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager29updateDirtyResourceSecondPassEv',
    )

  @overload(QQuick3DObject)
  @overload(NoneType)
  def updateDirtyResource(
      self,
      resourceObject: Optional[QQuick3DObject],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::updateDirtyResource(QQuick3DObject
    *resourceObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#updateDirtyResource

    Parameters
    ----------

    resourceObject : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneManager::updateDirtyResource(QQuick3DObject
    #      *resourceObject)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager19updateDirtyResourceEP14QQuick3DOb'
        'ject',
        self._addressOf(resourceObject),
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def updateDirtySpatialNode(
      self,
      spatialNode: Optional[QQuick3DNode],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DSceneManager::updateDirtySpatialNode(QQuick3DNode *spatialNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#updateDirtySpatialNode

    Parameters
    ----------

    spatialNode : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DSceneManager::updateDirtySpatialNode(QQuick3DNode
    #      *spatialNode)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSceneManager22updateDirtySpatialNodeEP12QQuick3'
        'DNode',
        self._addressOf(spatialNode),
    )

  def needsUpdate(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::needsUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#needsUpdate
    """
    #  void QQuick3DSceneManager::needsUpdate()
    self.uglySide.call('ritual_ZN20QQuick3DSceneManager11needsUpdateEv')

  def windowChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSceneManager::windowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dscenemanager.html#windowChanged
    """
    #  void QQuick3DSceneManager::windowChanged()
    self.uglySide.call('ritual_ZN20QQuick3DSceneManager13windowChangedEv')

  @staticmethod
  def getOrSetWindowAttachment(*__, **_) -> Never:
    """
    Qt's 'QQuick3DWindowAttachment
    *QQuick3DSceneManager::getOrSetWindowAttachment(QQuickWindow &window)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneManager.getOrSetWindowAttachment' has no cute "
        "function yet. Qt's 'QQuick3DWindowAttachment "
        "*QQuick3DSceneManager::getOrSetWindowAttachment(QQuickWindow "
        "&window)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def updateBoundingBoxes(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSceneManager::updateBoundingBoxes(QSSGBufferManager
    &mgr)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneManager.updateBoundingBoxes' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DSceneManager::updateBoundingBoxes(QSSGBufferManager "
        "&mgr)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def updateExtensions(*__, **_) -> Never:
    """
    Qt's 'SyncResult QQuick3DSceneManager::updateExtensions(QQuick3DObject
    **listHead)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneManager.updateExtensions' has no cute function yet. "
        "Qt's 'SyncResult "
        "QQuick3DSceneManager::updateExtensions(QQuick3DObject "
        "**listHead)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def updateNodes(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DSceneManager::updateNodes(QQuick3DObject **listHead)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneManager.updateNodes' has no cute function yet. Qt's "
        "'void QQuick3DSceneManager::updateNodes(QQuick3DObject "
        "**listHead)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def updateResources(*__, **_) -> Never:
    """
    Qt's 'SyncResult QQuick3DSceneManager::updateResources(QQuick3DObject
    **listHead)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DSceneManager.updateResources' has no cute function yet. "
        "Qt's 'SyncResult "
        "QQuick3DSceneManager::updateResources(QQuick3DObject **listHead)': "
        "takes a type Python has no way to hand over yet.")
