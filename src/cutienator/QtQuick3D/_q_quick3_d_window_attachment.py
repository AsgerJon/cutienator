"""
QQuick3DWindowAttachment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenemanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DWindowAttachment to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickWindow
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject, QSSGRenderLayer
  from ..QtQuick3DRuntimeRender import QSSGRenderRoot
  from . import QQuick3DSceneManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DSceneManager = WAIT['QQuick3DSceneManager']
  QQuickWindow = WAIT['QQuickWindow']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QSSGRenderLayer = WAIT['QSSGRenderLayer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DWindowAttachment(QObject):
  """
  The cute side of Qt's QQuick3DWindowAttachment: a plain Python object
  standing in front of one C++ QQuick3DWindowAttachment.

  It is built on the cute 'QObject', as Qt's QQuick3DWindowAttachment is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DWindowAttachment that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'preSync',
  'cleanupResources', 'requestUpdate', 'evaluateEol', 'window', 'rootNode',
  'queueForCleanup', 'releaseCachedResources',
  'renderContextInterfaceChanged', 'onReleaseCachedResources',
  'onInvalidated'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DWindowAttachment::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DWindowAttachment::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DWindowAttachment::~QQuick3DWindowAttachment()': the
    destructor: Python never removes a C++ QQuick3DWindowAttachment.
  - Qt's 'SyncResult
    QQuick3DWindowAttachment::synchronize(QSet<QSSGRenderGraphObject *>
    &resourceLoaders)': takes a type Python has no way to hand over yet.
  - Qt's 'const std::shared_ptr<QSSGRenderContextInterface>
    &QQuick3DWindowAttachment::rci() const': gives a type Python has no way
    to take yet.
  - Qt's 'void QQuick3DWindowAttachment::setRci(const
    std::shared_ptr<QSSGRenderContextInterface> &rciptr)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QQuick3DWindowAttachment::registerSceneManager(QQuick3DSceneManager
    &manager)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QQuick3DWindowAttachment::unregisterSceneManager(QQuick3DSceneManager
    &manager)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DWindowAttachment is created at the first use, not by
    'QQuick3DWindowAttachment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DWindowAttachment.
  - Qt tells when it has removed the C++ QQuick3DWindowAttachment. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DWindowAttachment that has no cute function yet,
    'rci', 'registerSceneManager', 'setRci', 'synchronize',
    'unregisterSceneManager', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DWindowAttachment, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SyncResultFlag(CuteNum):
    """
    The enum 'QQuick3DWindowAttachment::SyncResultFlag' of Qt, with the 3
    names Qt gives in it.
    """

    NULL = Kee[int](0)
    SharedResourcesDirty = Kee[int](1)
    ExtensionsDiry = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DWindowAttachment::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dwindowattachment.html#tr

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
    #  QString QQuick3DWindowAttachment::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuick3DWindowAttachment2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DWindowAttachment'

  #  A C++ QQuick3DWindowAttachment Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DWindowAttachment'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DWindowAttachment::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DWindowAttachment::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DWindowAttachment10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuick3DWindowAttachment::window() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuick3DWindowAttachment::window() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DWindowAttachment6windowEv',
    )
    from ..QtQuick import QQuickWindow
    return QQuickWindow._cuteAt(address)

  def rootNode(self) -> Optional[QSSGRenderRoot]:
    """
    Calls Qt's 'QSSGRenderRoot *QQuick3DWindowAttachment::rootNode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#rootNode

    Returns
    -------

    Optional[QSSGRenderRoot]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderRoot *QQuick3DWindowAttachment::rootNode() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuick3DWindowAttachment8rootNodeEv',
    )
    from ..QtQuick3DRuntimeRender import QSSGRenderRoot
    return QSSGRenderRoot._cuteAt(address)

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

  @overload(QQuickWindow)
  @overload(NoneType)
  def __init__(self, window: Optional[QQuickWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DWindowAttachment::QQuick3DWindowAttachment(QQuickWindow
    *window)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuick3DWindowAttachment::QQuick3DWindowAttachment(QQuickWindow
    #      *window)
    self._noteCreation(QQuick3DWindowAttachment, lambda: Rituals.call(
        'ritual_ZN24QQuick3DWindowAttachmentC1EP12QQuickWindow',
        self._addressOf(window),
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

  def preSync(self) -> None:
    """
    Calls Qt's 'void QQuick3DWindowAttachment::preSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#preSync
    """
    #  void QQuick3DWindowAttachment::preSync()
    self.uglySide.call('ritual_ZN24QQuick3DWindowAttachment7preSyncEv')

  def cleanupResources(self) -> None:
    """
    Calls Qt's 'void QQuick3DWindowAttachment::cleanupResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#cleanupResources
    """
    #  void QQuick3DWindowAttachment::cleanupResources()
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment16cleanupResourcesEv',
    )

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void QQuick3DWindowAttachment::requestUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#requestUpdate
    """
    #  void QQuick3DWindowAttachment::requestUpdate()
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment13requestUpdateEv',
    )

  def evaluateEol(self) -> None:
    """
    Calls Qt's 'void QQuick3DWindowAttachment::evaluateEol()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#evaluateEol
    """
    #  void QQuick3DWindowAttachment::evaluateEol()
    self.uglySide.call('ritual_ZN24QQuick3DWindowAttachment11evaluateEolEv')

  @overload(QSSGRenderLayer)
  def queueForCleanup(self, layer: Optional[QSSGRenderLayer]) -> None:
    """
    Calls Qt's 'void
    QQuick3DWindowAttachment::queueForCleanup(QSSGRenderLayer *layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#queueForCleanup

    Parameters
    ----------

    layer : Optional[QSSGRenderLayer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DWindowAttachment::queueForCleanup(QSSGRenderLayer *layer)
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment15queueForCleanupEP15QSSGRender'
        'Layer',
        self._addressOf(layer),
    )

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def queueForCleanup(self, obj: Optional[QSSGRenderGraphObject]) -> None:
    """
    Calls Qt's 'void
    QQuick3DWindowAttachment::queueForCleanup(QSSGRenderGraphObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#queueForCleanup

    Parameters
    ----------

    obj : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DWindowAttachment::queueForCleanup(QSSGRenderGraphObject
    #      *obj)
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment15queueForCleanupEP21QSSGRender'
        'GraphObject',
        self._addressOf(obj),
    )

  @overload(QQuick3DSceneManager)
  def queueForCleanup(self, manager: Optional[QQuick3DSceneManager]) -> None:
    """
    Calls Qt's 'void
    QQuick3DWindowAttachment::queueForCleanup(QQuick3DSceneManager
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#queueForCleanup

    Parameters
    ----------

    manager : Optional[QQuick3DSceneManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DWindowAttachment::queueForCleanup(QQuick3DSceneManager
    #      *manager)
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment15queueForCleanupEP20QQuick3DSc'
        'eneManager',
        self._addressOf(manager),
    )

  def releaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QQuick3DWindowAttachment::releaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html
    """
    #  void QQuick3DWindowAttachment::releaseCachedResources()
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment22releaseCachedResourcesEv',
    )

  def renderContextInterfaceChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DWindowAttachment::renderContextInterfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html
    """
    #  void QQuick3DWindowAttachment::renderContextInterfaceChanged()
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment29renderContextInterfaceChanged'
        'Ev',
    )

  def onReleaseCachedResources(self) -> None:
    """
    Calls Qt's 'void QQuick3DWindowAttachment::onReleaseCachedResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html
    """
    #  void QQuick3DWindowAttachment::onReleaseCachedResources()
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment24onReleaseCachedResourcesEv',
    )

  def onInvalidated(self) -> None:
    """
    Calls Qt's 'void QQuick3DWindowAttachment::onInvalidated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dwindowattachment.html#onInvalidated
    """
    #  void QQuick3DWindowAttachment::onInvalidated()
    self.uglySide.call(
        'ritual_ZN24QQuick3DWindowAttachment13onInvalidatedEv',
    )

  @staticmethod
  def rci(*__, **_) -> Never:
    """
    Qt's 'const std::shared_ptr<QSSGRenderContextInterface>
    &QQuick3DWindowAttachment::rci() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DWindowAttachment.rci' has no cute function yet. Qt's "
        "'const std::shared_ptr<QSSGRenderContextInterface> "
        "&QQuick3DWindowAttachment::rci() const': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def registerSceneManager(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DWindowAttachment::registerSceneManager(QQuick3DSceneManager
    &manager)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DWindowAttachment.registerSceneManager' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DWindowAttachment::registerSceneManager(QQuick3DSceneManager"
        " &manager)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setRci(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DWindowAttachment::setRci(const
    std::shared_ptr<QSSGRenderContextInterface> &rciptr)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DWindowAttachment.setRci' has no cute function yet. Qt's "
        "'void QQuick3DWindowAttachment::setRci(const "
        "std::shared_ptr<QSSGRenderContextInterface> &rciptr)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def synchronize(*__, **_) -> Never:
    """
    Qt's 'SyncResult
    QQuick3DWindowAttachment::synchronize(QSet<QSSGRenderGraphObject *>
    &resourceLoaders)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DWindowAttachment.synchronize' has no cute function yet. "
        "Qt's 'SyncResult "
        "QQuick3DWindowAttachment::synchronize(QSet<QSSGRenderGraphObject "
        "*> &resourceLoaders)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def unregisterSceneManager(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DWindowAttachment::unregisterSceneManager(QQuick3DSceneManager
    &manager)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DWindowAttachment.unregisterSceneManager' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DWindowAttachment::unregisterSceneManager(QQuick3DSceneManag"
        "er &manager)': takes a type Python has no way to hand over yet.")
