"""
QSGThreadedRenderLoop binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgthreadedrenderloop_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGThreadedRenderLoop to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QSGRenderLoop

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAnimationDriver, QEvent, QMetaObject, QRunnable
  from ..QtGui import QImage
  from . import QQuickWindow, QSGContext, QSGRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQuickWindow = WAIT['QQuickWindow']
  QRunnable = WAIT['QRunnable']
  QSGContext = WAIT['QSGContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGThreadedRenderLoop(QSGRenderLoop):
  """
  The cute side of Qt's QSGThreadedRenderLoop: a plain Python object standing
  in front of one C++ QSGThreadedRenderLoop.

  It is built on the cute 'QSGRenderLoop', as Qt's QSGThreadedRenderLoop is
  built on Qt's QSGRenderLoop, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGThreadedRenderLoop that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'show', 'hide',
  'resize', 'windowDestroyed', 'exposureChanged', 'grab', 'update',
  'maybeUpdate', 'handleUpdateRequest', 'sceneGraphContext',
  'createRenderContext', 'animationDriver', 'releaseResources', 'event',
  'postJob', 'interleaveIncubation', 'animationStarted', 'animationStopped',
  'anyoneShowing', 'startOrStopAnimationTimer', 'releaseSwapchain',
  'eventFilter'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGThreadedRenderLoop::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSGThreadedRenderLoop::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGThreadedRenderLoop::~QSGThreadedRenderLoop()': the destructor:
    Python never removes a C++ QSGThreadedRenderLoop.
  - Qt's 'Window *QSGThreadedRenderLoop::windowFor(QQuickWindow *window)':
    gives 'QSGThreadedRenderLoop::Window', which has no cute class yet.
  - Qt's 'void QSGThreadedRenderLoop::postUpdateRequest(Window *w)': names
    'QSGThreadedRenderLoop::Window', which has no cute class yet.

  What has no ritual
  ------------------

  12 of the 40 functions Qt declares: 5 not a gap; 5 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QSGThreadedRenderLoop.

  What to expect
  --------------

  - The C++ QSGThreadedRenderLoop is created at the first use, not by
    'QSGThreadedRenderLoop(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGThreadedRenderLoop.
  - Qt tells when it has removed the C++ QSGThreadedRenderLoop. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGThreadedRenderLoop that has no cute function yet,
    '__init__', 'handleExposure', 'handleObscurity', 'polishAndSync',
    'postUpdateRequest', 'windowFor', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGThreadedRenderLoop'

  #  A C++ QSGThreadedRenderLoop Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGThreadedRenderLoop'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGThreadedRenderLoop::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGThreadedRenderLoop::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QSGThreadedRenderLoop10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sceneGraphContext(self) -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext *QSGThreadedRenderLoop::sceneGraphContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#sceneGraphContext

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QSGThreadedRenderLoop::sceneGraphContext() const
    ritual = 'ritual_ZNK21QSGThreadedRenderLoop17sceneGraphContextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGThreadedRenderLoop17sceneGraphContextEv'
    address = self.uglySide.call(ritual)
    from . import QSGContext
    return QSGContext._cuteAt(address)

  @overload(QSGContext)
  @overload(NoneType)
  def createRenderContext(
      self,
      a0: Optional[QSGContext],
  ) -> Optional[QSGRenderContext]:
    """
    Calls Qt's 'QSGRenderContext
    *QSGThreadedRenderLoop::createRenderContext(QSGContext *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#createRenderContext

    Parameters
    ----------

    a0 : Optional[QSGContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGRenderContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderContext
    #      *QSGThreadedRenderLoop::createRenderContext(QSGContext *a0) const
    ritual = (
        'ritual_ZNK21QSGThreadedRenderLoop19createRenderContextEP10QSGConte'
        'xt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QSGThreadedRenderLoop19createRenderContextEP10QS'
          'GContext')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

  def animationDriver(self) -> Optional[QAnimationDriver]:
    """
    Calls Qt's 'QAnimationDriver *QSGThreadedRenderLoop::animationDriver()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#animationDriver

    Returns
    -------

    Optional[QAnimationDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationDriver *QSGThreadedRenderLoop::animationDriver() const
    ritual = 'ritual_ZNK21QSGThreadedRenderLoop15animationDriverEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGThreadedRenderLoop15animationDriverEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QAnimationDriver
    return QAnimationDriver._cuteAt(address)

  def interleaveIncubation(self) -> bool:
    """
    Calls Qt's 'bool QSGThreadedRenderLoop::interleaveIncubation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#interleaveIncubation
    """
    #  bool QSGThreadedRenderLoop::interleaveIncubation() const
    ritual = 'ritual_ZNK21QSGThreadedRenderLoop20interleaveIncubationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QSGThreadedRenderLoop20interleaveIncubationEv')
    return self.uglySide.call(ritual)

  def anyoneShowing(self) -> bool:
    """
    Calls Qt's 'bool QSGThreadedRenderLoop::anyoneShowing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#anyoneShowing
    """
    #  bool QSGThreadedRenderLoop::anyoneShowing() const
    return self.uglySide.call(
        'ritual_ZNK21QSGThreadedRenderLoop13anyoneShowingEv',
    )

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
    Qt's 'QSGThreadedRenderLoop::QSGThreadedRenderLoop()': leans on
    'QSGThreadedRenderLoop::maybeUpdate(QQuickWindow*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QSGThreadedRenderLoop.__init__' has no cute function yet. Qt's "
        "'QSGThreadedRenderLoop::QSGThreadedRenderLoop()': leans on "
        "'QSGThreadedRenderLoop::maybeUpdate(QQuickWindow*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(QQuickWindow)
  @overload(NoneType)
  def show(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::show(QQuickWindow *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#show

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::show(QQuickWindow *a0)
    ritual = 'ritual_ZN21QSGThreadedRenderLoop4showEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGThreadedRenderLoop4showEP12QQuickWindow'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickWindow)
  @overload(NoneType)
  def hide(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::hide(QQuickWindow *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#hide

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::hide(QQuickWindow *a0)
    ritual = 'ritual_ZN21QSGThreadedRenderLoop4hideEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGThreadedRenderLoop4hideEP12QQuickWindow'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickWindow)
  @overload(NoneType)
  def resize(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::resize(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#resize

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::resize(QQuickWindow *window)
    ritual = 'ritual_ZN21QSGThreadedRenderLoop6resizeEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGThreadedRenderLoop6resizeEP12QQuickWindow'
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowDestroyed(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::windowDestroyed(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#windowDestroyed

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::windowDestroyed(QQuickWindow *window)
    ritual = (
        'ritual_ZN21QSGThreadedRenderLoop15windowDestroyedEP12QQuickWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGThreadedRenderLoop15windowDestroyedEP12QQuickW'
          'indow')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def exposureChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::exposureChanged(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#exposureChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::exposureChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN21QSGThreadedRenderLoop15exposureChangedEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def grab(self, a0: Optional[QQuickWindow]) -> QImage:
    """
    Calls Qt's 'QImage QSGThreadedRenderLoop::grab(QQuickWindow *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#grab

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGThreadedRenderLoop::grab(QQuickWindow *a0)
    ritual = 'ritual_ZN21QSGThreadedRenderLoop4grabEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGThreadedRenderLoop4grabEP12QQuickWindow'
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(QQuickWindow)
  @overload(NoneType)
  def update(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::update(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#update

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::update(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN21QSGThreadedRenderLoop6updateEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def maybeUpdate(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::maybeUpdate(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#maybeUpdate

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN21QSGThreadedRenderLoop11maybeUpdateEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleUpdateRequest(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::handleUpdateRequest(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#handleUpdateRequest

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::handleUpdateRequest(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN21QSGThreadedRenderLoop19handleUpdateRequestEP12QQuickWin'
        'dow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def releaseResources(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::releaseResources(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#releaseResources

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::releaseResources(QQuickWindow *window)
    ritual = (
        'ritual_ZN21QSGThreadedRenderLoop16releaseResourcesEP12QQuickWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGThreadedRenderLoop16releaseResourcesEP12QQuick'
          'Window')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSGThreadedRenderLoop::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGThreadedRenderLoop::event(QEvent *a0)
    ritual = 'ritual_ZN21QSGThreadedRenderLoop5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGThreadedRenderLoop5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickWindow, QRunnable)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QRunnable)
  @overload(NoneType, NoneType)
  def postJob(
      self,
      window: Optional[QQuickWindow],
      job: Optional[QRunnable],
  ) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::postJob(QQuickWindow *window,
    QRunnable *job)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#postJob

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    job : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::postJob(QQuickWindow *window, QRunnable
    #      *job)
    ritual = (
        'ritual_ZN21QSGThreadedRenderLoop7postJobEP12QQuickWindowP9QRunnabl'
        'e')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGThreadedRenderLoop7postJobEP12QQuickWindowP9QR'
          'unnable')
    self.uglySide.call(
        ritual, self._addressOf(window), self._addressOf(job, 'QRunnable'),
    )

  def animationStarted(self) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::animationStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#animationStarted
    """
    #  void QSGThreadedRenderLoop::animationStarted()
    self.uglySide.call(
        'ritual_ZN21QSGThreadedRenderLoop16animationStartedEv',
    )

  def animationStopped(self) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::animationStopped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#animationStopped
    """
    #  void QSGThreadedRenderLoop::animationStopped()
    self.uglySide.call(
        'ritual_ZN21QSGThreadedRenderLoop16animationStoppedEv',
    )

  def startOrStopAnimationTimer(self) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::startOrStopAnimationTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html
    """
    #  void QSGThreadedRenderLoop::startOrStopAnimationTimer()
    self.uglySide.call(
        'ritual_ZN21QSGThreadedRenderLoop25startOrStopAnimationTimerEv',
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def releaseSwapchain(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGThreadedRenderLoop::releaseSwapchain(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#releaseSwapchain

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGThreadedRenderLoop::releaseSwapchain(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN21QSGThreadedRenderLoop16releaseSwapchainEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QSGThreadedRenderLoop::eventFilter(QObject *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgthreadedrenderloop.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGThreadedRenderLoop::eventFilter(QObject *watched, QEvent
    #      *event)
    ritual = (
        'ritual_ZN21QSGThreadedRenderLoop11eventFilterEP7QObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGThreadedRenderLoop11eventFilterEP7QObjectP6QEv'
          'ent')
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  @staticmethod
  def handleExposure(*__, **_) -> Never:
    """
    Qt's 'void QSGThreadedRenderLoop::handleExposure(QQuickWindow *w)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: allocation of incomplete type 'QSGRenderThread'.
    """
    raise NotImplementedError(
        "'QSGThreadedRenderLoop.handleExposure' has no cute function yet. "
        "Qt's 'void QSGThreadedRenderLoop::handleExposure(QQuickWindow "
        "*w)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: allocation of incomplete "
        "type 'QSGRenderThread'.")

  @staticmethod
  def handleObscurity(*__, **_) -> Never:
    """
    Qt's 'void QSGThreadedRenderLoop::handleObscurity(Window *w)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QSGRenderThread'.
    """
    raise NotImplementedError(
        "'QSGThreadedRenderLoop.handleObscurity' has no cute function yet. "
        "Qt's 'void QSGThreadedRenderLoop::handleObscurity(Window *w)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QSGRenderThread'.")

  @staticmethod
  def polishAndSync(*__, **_) -> Never:
    """
    Qt's 'void QSGThreadedRenderLoop::polishAndSync(Window *w, bool
    inExpose)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QSGRenderThread'.
    """
    raise NotImplementedError(
        "'QSGThreadedRenderLoop.polishAndSync' has no cute function yet. "
        "Qt's 'void QSGThreadedRenderLoop::polishAndSync(Window *w, bool "
        "inExpose)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QSGRenderThread'.")

  @staticmethod
  def postUpdateRequest(*__, **_) -> Never:
    """
    Qt's 'void QSGThreadedRenderLoop::postUpdateRequest(Window *w)': names
    'QSGThreadedRenderLoop::Window', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGThreadedRenderLoop.postUpdateRequest' has no cute function "
        "yet. Qt's 'void QSGThreadedRenderLoop::postUpdateRequest(Window "
        "*w)': names 'QSGThreadedRenderLoop::Window', which has no cute "
        "class yet.")

  @staticmethod
  def windowFor(*__, **_) -> Never:
    """
    Qt's 'Window *QSGThreadedRenderLoop::windowFor(QQuickWindow *window)':
    gives 'QSGThreadedRenderLoop::Window', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGThreadedRenderLoop.windowFor' has no cute function yet. Qt's "
        "'Window *QSGThreadedRenderLoop::windowFor(QQuickWindow *window)': "
        "gives 'QSGThreadedRenderLoop::Window', which has no cute class yet."
    )
