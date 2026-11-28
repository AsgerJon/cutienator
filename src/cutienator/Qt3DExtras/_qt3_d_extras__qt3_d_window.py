"""
Qt3DExtras::Qt3DWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qt3dwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QWindow
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QResizeEvent, QScreen, QShowEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QScreen = WAIT['QScreen']
  QShowEvent = WAIT['QShowEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Qt3DWindow(QWindow):
  """
  The cute side of Qt's Qt3DExtras::Qt3DWindow: a plain Python object
  standing in front of one C++ Qt3DExtras::Qt3DWindow.

  It is built on the cute 'QWindow', as Qt's Qt3DExtras::Qt3DWindow is built
  on Qt's QWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::Qt3DWindow that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr',
  'registerAspect', 'setRootEntity', 'setActiveFrameGraph',
  'activeFrameGraph', 'defaultFrameGraph', 'camera', 'renderSettings',
  'showEvent', 'resizeEvent', 'event', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::Qt3DWindow::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DExtras::Qt3DWindow::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::Qt3DWindow::~Qt3DWindow()': the destructor: Python
    never removes a C++ Qt3DExtras::Qt3DWindow.
  - Qt's 'const Qt3DWindowPrivate *Qt3DExtras::Qt3DWindow::d_func() const':
    takes in Python what 'Qt3DWindowPrivate
    *Qt3DExtras::Qt3DWindow::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::Qt3DWindow is created at the first use, not by
    'Qt3DExtras::Qt3DWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::Qt3DWindow.
  - Qt tells when it has removed the C++ Qt3DExtras::Qt3DWindow. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DExtras::Qt3DWindow::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#tr

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
    #  QString Qt3DExtras::Qt3DWindow::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras10Qt3DWindow2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::Qt3DWindow'

  #  A C++ Qt3DExtras::Qt3DWindow Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_Qt3DWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DExtras::Qt3DWindow::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::Qt3DWindow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras10Qt3DWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeFrameGraph(self) -> Optional[Qt3DRender.QFrameGraphNode]:
    """
    Calls Qt's 'Qt3DRender::QFrameGraphNode
    *Qt3DExtras::Qt3DWindow::activeFrameGraph() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#activeFrameGraph

    Returns
    -------

    Optional[Qt3DRender.QFrameGraphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QFrameGraphNode
    #      *Qt3DExtras::Qt3DWindow::activeFrameGraph() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras10Qt3DWindow16activeFrameGraphEv',
    )
    return Qt3DRender.QFrameGraphNode._cuteAt(address)

  def defaultFrameGraph(self) -> Optional[Qt3DExtras.QForwardRenderer]:
    """
    Calls Qt's 'Qt3DExtras::QForwardRenderer
    *Qt3DExtras::Qt3DWindow::defaultFrameGraph() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#defaultFrameGraph

    Returns
    -------

    Optional[Qt3DExtras.QForwardRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DExtras::QForwardRenderer
    #      *Qt3DExtras::Qt3DWindow::defaultFrameGraph() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras10Qt3DWindow17defaultFrameGraphEv',
    )
    return Qt3DExtras.QForwardRenderer._cuteAt(address)

  def camera(self) -> Optional[Qt3DRender.QCamera]:
    """
    Calls Qt's 'Qt3DRender::QCamera *Qt3DExtras::Qt3DWindow::camera() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#camera

    Returns
    -------

    Optional[Qt3DRender.QCamera]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QCamera *Qt3DExtras::Qt3DWindow::camera() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras10Qt3DWindow6cameraEv',
    )
    return Qt3DRender.QCamera._cuteAt(address)

  def renderSettings(self) -> Optional[Qt3DRender.QRenderSettings]:
    """
    Calls Qt's 'Qt3DRender::QRenderSettings
    *Qt3DExtras::Qt3DWindow::renderSettings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#renderSettings

    Returns
    -------

    Optional[Qt3DRender.QRenderSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DRender::QRenderSettings *Qt3DExtras::Qt3DWindow::renderSettings()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras10Qt3DWindow14renderSettingsEv',
    )
    return Qt3DRender.QRenderSettings._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def setRootEntity(self, root: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Qt3DWindow::setRootEntity(Qt3DCore::QEntity
    *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#setRootEntity

    Parameters
    ----------

    root : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Qt3DWindow::setRootEntity(Qt3DCore::QEntity *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras10Qt3DWindow13setRootEntityEPN8Qt3DCore7QEnti'
        'tyE',
        self._addressOf(root),
    )

  @overload(WAIT['Qt3DRender.QFrameGraphNode'])
  @overload(NoneType)
  def setActiveFrameGraph(
      self,
      activeFrameGraph: Optional[Qt3DRender.QFrameGraphNode],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Qt3DWindow::setActiveFrameGraph(Qt3DRender::QFrameGraphNode
    *activeFrameGraph)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#setActiveFrameGraph

    Parameters
    ----------

    activeFrameGraph : Optional[Qt3DRender.QFrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Qt3DWindow::setActiveFrameGraph(Qt3DRender::
    #      QFrameGraphNode *activeFrameGraph)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras10Qt3DWindow19setActiveFrameGraphEPN10Qt3DRen'
        'der15QFrameGraphNodeE',
        self._addressOf(activeFrameGraph),
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
  @overload(QScreen)
  @overload(NoneType)
  @overload(QScreen, Qt3DRender.API)
  @overload(NoneType, Qt3DRender.API)
  def __init__(
      self,
      screen: Optional[QScreen] = None,
      a1: Qt3DRender.API = Qt3DRender.API.RHI,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::Qt3DWindow::Qt3DWindow(QScreen *screen, Qt3DRender::API
    a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#Qt3DWindow

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    a1 : Qt3DRender.API
      Passed on as its number. May be left out, as in Qt: it is then
      Qt3DRender.API.RHI.
    """
    #  Qt3DExtras::Qt3DWindow::Qt3DWindow(QScreen *screen, Qt3DRender::API
    #      a1)
    self._noteCreation(Qt3DWindow, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras10Qt3DWindowC1EP7QScreenN10Qt3DRender3APIE',
        self._addressOf(screen), a1.value,
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

  @overload(WAIT['Qt3DCore.QAbstractAspect'])
  @overload(NoneType)
  def registerAspect(
      self,
      aspect: Optional[Qt3DCore.QAbstractAspect],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Qt3DWindow::registerAspect(Qt3DCore::QAbstractAspect
    *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#registerAspect

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QAbstractAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Qt3DWindow::registerAspect(Qt3DCore::QAbstractAspect
    #      *aspect)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras10Qt3DWindow14registerAspectEPN8Qt3DCore15QAb'
        'stractAspectE',
        self._addressOf(aspect),
    )

  @overload(str)
  def registerAspect(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Qt3DWindow::registerAspect(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#registerAspect

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::Qt3DWindow::registerAspect(const QString &name)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras10Qt3DWindow14registerAspectERK7QString', name,
    )

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, e: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Qt3DWindow::showEvent(QShowEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#showEvent

    Parameters
    ----------

    e : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Qt3DWindow::showEvent(QShowEvent *e)
    ritual = 'ritual_ZN10Qt3DExtras10Qt3DWindow9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DExtras10Qt3DWindow9showEventEP10QShowEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Qt3DWindow::resizeEvent(QResizeEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Qt3DWindow::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN10Qt3DExtras10Qt3DWindow11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DExtras10Qt3DWindow11resizeEventEP12QResizeEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool Qt3DExtras::Qt3DWindow::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DExtras::Qt3DWindow::event(QEvent *e)
    ritual = 'ritual_ZN10Qt3DExtras10Qt3DWindow5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DExtras10Qt3DWindow5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  def d_func(self) -> Optional[Qt3DExtras.Qt3DWindowPrivate]:
    """
    Calls Qt's 'Qt3DWindowPrivate *Qt3DExtras::Qt3DWindow::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dextras-qt3dwindow.html#d_func

    Returns
    -------

    Optional[Qt3DExtras.Qt3DWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DWindowPrivate *Qt3DExtras::Qt3DWindow::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras10Qt3DWindow6d_funcEv',
    )
    return Qt3DExtras.Qt3DWindowPrivate._cuteAt(address)
