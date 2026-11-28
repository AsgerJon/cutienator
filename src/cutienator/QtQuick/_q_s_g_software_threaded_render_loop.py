"""
QSGSoftwareThreadedRenderLoop binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarethreadedrenderloop_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGSoftwareThreadedRenderLoop to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QSurface
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


class QSGSoftwareThreadedRenderLoop(QSGRenderLoop):
  """
  The cute side of Qt's QSGSoftwareThreadedRenderLoop: a plain Python object
  standing in front of one C++ QSGSoftwareThreadedRenderLoop.

  It is built on the cute 'QSGRenderLoop', as Qt's
  QSGSoftwareThreadedRenderLoop is built on Qt's QSGRenderLoop, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareThreadedRenderLoop that has a ritual and
  that Python can call so far, 22 names in all: 'metaObject', 'show', 'hide',
  'resize', 'windowDestroyed', 'exposureChanged', 'grab', 'update',
  'maybeUpdate', 'handleUpdateRequest', 'animationDriver',
  'sceneGraphContext', 'createRenderContext', 'releaseResources', 'postJob',
  'windowSurfaceType', 'interleaveIncubation', 'flags', 'event',
  'onAnimationStarted', 'onAnimationStopped', 'startOrStopAnimationTimer'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGSoftwareThreadedRenderLoop::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QSGSoftwareThreadedRenderLoop::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'WindowData *QSGSoftwareThreadedRenderLoop::windowFor(QQuickWindow
    *window)': gives 'QSGSoftwareThreadedRenderLoop::WindowData', which has
    no cute class yet.

  What has no ritual
  ------------------

  10 of the 35 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QSGSoftwareThreadedRenderLoop.

  What to expect
  --------------

  - The C++ QSGSoftwareThreadedRenderLoop is created at the first use, not by
    'QSGSoftwareThreadedRenderLoop(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareThreadedRenderLoop.
  - Qt tells when it has removed the C++ QSGSoftwareThreadedRenderLoop. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGSoftwareThreadedRenderLoop that has no cute function
    yet, '__init__', 'handleExposure', 'handleObscurity',
    'handleResourceRelease', 'polishAndSync', 'scheduleUpdate', 'windowFor',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareThreadedRenderLoop'

  #  A C++ QSGSoftwareThreadedRenderLoop Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwareThreadedRenderLoop'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QSGSoftwareThreadedRenderLoop::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGSoftwareThreadedRenderLoop::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QSGSoftwareThreadedRenderLoop10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def animationDriver(self) -> Optional[QAnimationDriver]:
    """
    Calls Qt's 'QAnimationDriver
    *QSGSoftwareThreadedRenderLoop::animationDriver() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#animationDriver

    Returns
    -------

    Optional[QAnimationDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationDriver *QSGSoftwareThreadedRenderLoop::animationDriver()
    #      const
    ritual = 'ritual_ZNK29QSGSoftwareThreadedRenderLoop15animationDriverEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSGSoftwareThreadedRenderLoop15animationDriverEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QAnimationDriver
    return QAnimationDriver._cuteAt(address)

  def sceneGraphContext(self) -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext
    *QSGSoftwareThreadedRenderLoop::sceneGraphContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QSGSoftwareThreadedRenderLoop::sceneGraphContext() const
    ritual = 'ritual_ZNK29QSGSoftwareThreadedRenderLoop17sceneGraphContextEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSGSoftwareThreadedRenderLoop17sceneGraphContext'
          'Ev')
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
    *QSGSoftwareThreadedRenderLoop::createRenderContext(QSGContext *a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html

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
    #      *QSGSoftwareThreadedRenderLoop::createRenderContext(QSGContext
    #      *a0) const
    ritual = (
        'ritual_ZNK29QSGSoftwareThreadedRenderLoop19createRenderContextEP10'
        'QSGContext')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSGSoftwareThreadedRenderLoop19createRenderConte'
          'xtEP10QSGContext')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

  def windowSurfaceType(self) -> QSurface.SurfaceType:
    """
    Calls Qt's 'QSurface::SurfaceType
    QSGSoftwareThreadedRenderLoop::windowSurfaceType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html

    Returns
    -------

    QSurface.SurfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSurface.SurfaceType(number)' gives.
    """
    #  QSurface::SurfaceType
    #      QSGSoftwareThreadedRenderLoop::windowSurfaceType() const
    ritual = 'ritual_ZNK29QSGSoftwareThreadedRenderLoop17windowSurfaceTypeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSGSoftwareThreadedRenderLoop17windowSurfaceType'
          'Ev')
    return QSurface.SurfaceType(self.uglySide.call(ritual))

  def interleaveIncubation(self) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareThreadedRenderLoop::interleaveIncubation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html
    """
    #  bool QSGSoftwareThreadedRenderLoop::interleaveIncubation() const
    ritual = (
        'ritual_ZNK29QSGSoftwareThreadedRenderLoop20interleaveIncubationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QSGSoftwareThreadedRenderLoop20interleaveIncubat'
          'ionEv')
    return self.uglySide.call(ritual)

  def flags(self) -> int:
    """
    Calls Qt's 'int QSGSoftwareThreadedRenderLoop::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#flags
    """
    #  int QSGSoftwareThreadedRenderLoop::flags() const
    ritual = 'ritual_ZNK29QSGSoftwareThreadedRenderLoop5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QSGSoftwareThreadedRenderLoop5flagsEv'
    return self.uglySide.call(ritual)

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
    Qt's 'QSGSoftwareThreadedRenderLoop::QSGSoftwareThreadedRenderLoop()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'QSG_RASTER_LOG_RENDERLOOP'; did you mean 'QSG_LOG_RENDERLOOP'?.
    """
    raise NotImplementedError(
        "'QSGSoftwareThreadedRenderLoop.__init__' has no cute function yet. "
        "Qt's "
        "'QSGSoftwareThreadedRenderLoop::QSGSoftwareThreadedRenderLoop()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QSG_RASTER_LOG_RENDERLOOP'; did you mean 'QSG_LOG_RENDERLOOP'?.")

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
  def show(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareThreadedRenderLoop::show(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#show

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::show(QQuickWindow *window)
    ritual = 'ritual_ZN29QSGSoftwareThreadedRenderLoop4showEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGSoftwareThreadedRenderLoop4showEP12QQuickWindo'
          'w')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def hide(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareThreadedRenderLoop::hide(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#hide

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::hide(QQuickWindow *window)
    ritual = 'ritual_ZN29QSGSoftwareThreadedRenderLoop4hideEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGSoftwareThreadedRenderLoop4hideEP12QQuickWindo'
          'w')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def resize(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareThreadedRenderLoop::resize(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#resize

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::resize(QQuickWindow *window)
    ritual = (
        'ritual_ZN29QSGSoftwareThreadedRenderLoop6resizeEP12QQuickWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGSoftwareThreadedRenderLoop6resizeEP12QQuickWin'
          'dow')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowDestroyed(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareThreadedRenderLoop::windowDestroyed(QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#windowDestroyed

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::windowDestroyed(QQuickWindow
    #      *window)
    ritual = (
        'ritual_ZN29QSGSoftwareThreadedRenderLoop15windowDestroyedEP12QQuic'
        'kWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGSoftwareThreadedRenderLoop15windowDestroyedEP1'
          '2QQuickWindow')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def exposureChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareThreadedRenderLoop::exposureChanged(QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#exposureChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::exposureChanged(QQuickWindow
    #      *window)
    self.uglySide.call(
        'ritual_ZN29QSGSoftwareThreadedRenderLoop15exposureChangedEP12QQuic'
        'kWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def grab(self, window: Optional[QQuickWindow]) -> QImage:
    """
    Calls Qt's 'QImage QSGSoftwareThreadedRenderLoop::grab(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#grab

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGSoftwareThreadedRenderLoop::grab(QQuickWindow *window)
    address = self.uglySide.call(
        'ritual_ZN29QSGSoftwareThreadedRenderLoop4grabEP12QQuickWindow',
        self._addressOf(window),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(QQuickWindow)
  @overload(NoneType)
  def update(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareThreadedRenderLoop::update(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#update

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::update(QQuickWindow *window)
    ritual = (
        'ritual_ZN29QSGSoftwareThreadedRenderLoop6updateEP12QQuickWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGSoftwareThreadedRenderLoop6updateEP12QQuickWin'
          'dow')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def maybeUpdate(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareThreadedRenderLoop::maybeUpdate(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#maybeUpdate

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
    ritual = (
        'ritual_ZN29QSGSoftwareThreadedRenderLoop11maybeUpdateEP12QQuickWin'
        'dow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGSoftwareThreadedRenderLoop11maybeUpdateEP12QQu'
          'ickWindow')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleUpdateRequest(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareThreadedRenderLoop::handleUpdateRequest(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::handleUpdateRequest(QQuickWindow
    #      *window)
    self.uglySide.call(
        'ritual_ZN29QSGSoftwareThreadedRenderLoop19handleUpdateRequestEP12Q'
        'QuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def releaseResources(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareThreadedRenderLoop::releaseResources(QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::releaseResources(QQuickWindow
    #      *window)
    ritual = (
        'ritual_ZN29QSGSoftwareThreadedRenderLoop16releaseResourcesEP12QQui'
        'ckWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGSoftwareThreadedRenderLoop16releaseResourcesEP'
          '12QQuickWindow')
    self.uglySide.call(ritual, self._addressOf(window))

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
    Calls Qt's 'void QSGSoftwareThreadedRenderLoop::postJob(QQuickWindow
    *window, QRunnable *job)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#postJob

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    job : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareThreadedRenderLoop::postJob(QQuickWindow *window,
    #      QRunnable *job)
    ritual = (
        'ritual_ZN29QSGSoftwareThreadedRenderLoop7postJobEP12QQuickWindowP9'
        'QRunnable')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QSGSoftwareThreadedRenderLoop7postJobEP12QQuickWi'
          'ndowP9QRunnable')
    self.uglySide.call(
        ritual, self._addressOf(window), self._addressOf(job, 'QRunnable'),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSGSoftwareThreadedRenderLoop::event(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGSoftwareThreadedRenderLoop::event(QEvent *e)
    ritual = 'ritual_ZN29QSGSoftwareThreadedRenderLoop5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QSGSoftwareThreadedRenderLoop5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  def onAnimationStarted(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareThreadedRenderLoop::onAnimationStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html
    """
    #  void QSGSoftwareThreadedRenderLoop::onAnimationStarted()
    self.uglySide.call(
        'ritual_ZN29QSGSoftwareThreadedRenderLoop18onAnimationStartedEv',
    )

  def onAnimationStopped(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareThreadedRenderLoop::onAnimationStopped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html
    """
    #  void QSGSoftwareThreadedRenderLoop::onAnimationStopped()
    self.uglySide.call(
        'ritual_ZN29QSGSoftwareThreadedRenderLoop18onAnimationStoppedEv',
    )

  def startOrStopAnimationTimer(self) -> None:
    """
    Calls Qt's 'void
    QSGSoftwareThreadedRenderLoop::startOrStopAnimationTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarethreadedrenderloop.html
    """
    #  void QSGSoftwareThreadedRenderLoop::startOrStopAnimationTimer()
    self.uglySide.call(
        'ritual_ZN29QSGSoftwareThreadedRenderLoop25startOrStopAnimationTime'
        'rEv',
    )

  @staticmethod
  def handleExposure(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareThreadedRenderLoop::handleExposure(QQuickWindow
    *window)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'QSG_RASTER_LOG_RENDERLOOP'; did you mean 'QSG_LOG_RENDERLOOP'?.
    """
    raise NotImplementedError(
        "'QSGSoftwareThreadedRenderLoop.handleExposure' has no cute "
        "function yet. Qt's 'void "
        "QSGSoftwareThreadedRenderLoop::handleExposure(QQuickWindow "
        "*window)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QSG_RASTER_LOG_RENDERLOOP'; did you mean "
        "'QSG_LOG_RENDERLOOP'?.")

  @staticmethod
  def handleObscurity(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareThreadedRenderLoop::handleObscurity(WindowData
    *w)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'QSG_RASTER_LOG_RENDERLOOP'; did you mean 'QSG_LOG_RENDERLOOP'?.
    """
    raise NotImplementedError(
        "'QSGSoftwareThreadedRenderLoop.handleObscurity' has no cute "
        "function yet. Qt's 'void "
        "QSGSoftwareThreadedRenderLoop::handleObscurity(WindowData *w)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'QSG_RASTER_LOG_RENDERLOOP'; did you mean 'QSG_LOG_RENDERLOOP'?.")

  @staticmethod
  def handleResourceRelease(*__, **_) -> Never:
    """
    Qt's 'void
    QSGSoftwareThreadedRenderLoop::handleResourceRelease(WindowData *w, bool
    destroying)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QSG_RASTER_LOG_RENDERLOOP'; did you mean 'QSG_LOG_RENDERLOOP'?.
    """
    raise NotImplementedError(
        "'QSGSoftwareThreadedRenderLoop.handleResourceRelease' has no cute "
        "function yet. Qt's 'void "
        "QSGSoftwareThreadedRenderLoop::handleResourceRelease(WindowData "
        "*w, bool destroying)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QSG_RASTER_LOG_RENDERLOOP'; did you mean "
        "'QSG_LOG_RENDERLOOP'?.")

  @staticmethod
  def polishAndSync(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareThreadedRenderLoop::polishAndSync(WindowData *w,
    bool inExpose)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QSG_RASTER_LOG_RENDERLOOP'; did you mean 'QSG_LOG_RENDERLOOP'?.
    """
    raise NotImplementedError(
        "'QSGSoftwareThreadedRenderLoop.polishAndSync' has no cute function "
        "yet. Qt's 'void "
        "QSGSoftwareThreadedRenderLoop::polishAndSync(WindowData *w, bool "
        "inExpose)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QSG_RASTER_LOG_RENDERLOOP'; did you mean "
        "'QSG_LOG_RENDERLOOP'?.")

  @staticmethod
  def scheduleUpdate(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareThreadedRenderLoop::scheduleUpdate(WindowData *w)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: comparison of distinct pointer types
    ('QThread *' and 'QSGSoftwareRenderThread *').
    """
    raise NotImplementedError(
        "'QSGSoftwareThreadedRenderLoop.scheduleUpdate' has no cute "
        "function yet. Qt's 'void "
        "QSGSoftwareThreadedRenderLoop::scheduleUpdate(WindowData *w)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: comparison of distinct pointer "
        "types ('QThread *' and 'QSGSoftwareRenderThread *').")

  @staticmethod
  def windowFor(*__, **_) -> Never:
    """
    Qt's 'WindowData *QSGSoftwareThreadedRenderLoop::windowFor(QQuickWindow
    *window)': gives 'QSGSoftwareThreadedRenderLoop::WindowData', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QSGSoftwareThreadedRenderLoop.windowFor' has no cute function "
        "yet. Qt's 'WindowData "
        "*QSGSoftwareThreadedRenderLoop::windowFor(QQuickWindow *window)': "
        "gives 'QSGSoftwareThreadedRenderLoop::WindowData', which has no "
        "cute class yet.")
