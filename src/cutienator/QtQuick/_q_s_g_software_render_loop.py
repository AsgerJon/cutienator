"""
QSGSoftwareRenderLoop binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderloop_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwareRenderLoop to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtGui import QSurface
from . import QSGRenderLoop

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAnimationDriver, QMetaObject
  from ..QtGui import QImage
  from . import QQuickWindow, QSGContext, QSGRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']
  QSGContext = WAIT['QSGContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareRenderLoop(QSGRenderLoop):
  """
  The cute side of Qt's QSGSoftwareRenderLoop: a plain Python object standing
  in front of one C++ QSGSoftwareRenderLoop.

  It is built on the cute 'QSGRenderLoop', as Qt's QSGSoftwareRenderLoop is
  built on Qt's QSGRenderLoop, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareRenderLoop that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'show', 'hide',
  'windowDestroyed', 'exposureChanged', 'grab', 'maybeUpdate', 'update',
  'handleUpdateRequest', 'releaseResources', 'windowSurfaceType',
  'animationDriver', 'sceneGraphContext', 'createRenderContext'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGSoftwareRenderLoop::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSGSoftwareRenderLoop::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGSoftwareRenderLoop::~QSGSoftwareRenderLoop()': the destructor:
    Python never removes a C++ QSGSoftwareRenderLoop.

  What has no ritual
  ------------------

  5 of the 22 functions Qt declares: 2 not a gap; 2 leans on
  'QSGSoftwareRenderLoop; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSGSoftwareRenderLoop is created at the first use, not by
    'QSGSoftwareRenderLoop(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareRenderLoop.
  - Qt tells when it has removed the C++ QSGSoftwareRenderLoop. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGSoftwareRenderLoop that has no cute function yet,
    '__init__', 'renderWindow', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSGSoftwareRenderLoop, each a class in here
  #  as in C++.

  class WindowData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGSoftwareRenderLoop::WindowData: a plain Python
    object standing in front of one C++ QSGSoftwareRenderLoop::WindowData.

    C++ hands a QSGSoftwareRenderLoop::WindowData around as a copy, so every
    C++ QSGSoftwareRenderLoop::WindowData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSGSoftwareRenderLoop::WindowData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGSoftwareRenderLoop::WindowData::~WindowData()': the
      destructor: Python removes its C++ QSGSoftwareRenderLoop::WindowData by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSGSoftwareRenderLoop::WindowData is created at the first use,
      not by 'QSGSoftwareRenderLoop::WindowData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGSoftwareRenderLoop::WindowData back gives a copy
      the ritual made for Python, in a new cute
      QSGSoftwareRenderLoop::WindowData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGSoftwareRenderLoop::WindowData'

    #  Qt's '~QSGSoftwareRenderLoop::WindowData()'. Naming it makes this a
    #  value class: Python owns every C++ QSGSoftwareRenderLoop::WindowData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QSGSoftwareRenderLoop10WindowDataD1Ev'

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
  __qt_class__ = 'QSGSoftwareRenderLoop'

  #  A C++ QSGSoftwareRenderLoop Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwareRenderLoop'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGSoftwareRenderLoop::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGSoftwareRenderLoop::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QSGSoftwareRenderLoop10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def windowSurfaceType(self) -> QSurface.SurfaceType:
    """
    Calls Qt's 'QSurface::SurfaceType
    QSGSoftwareRenderLoop::windowSurfaceType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#windowSurfaceType

    Returns
    -------

    QSurface.SurfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSurface.SurfaceType(number)' gives.
    """
    #  QSurface::SurfaceType QSGSoftwareRenderLoop::windowSurfaceType() const
    ritual = 'ritual_ZNK21QSGSoftwareRenderLoop17windowSurfaceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGSoftwareRenderLoop17windowSurfaceTypeEv'
    return QSurface.SurfaceType(self.uglySide.call(ritual))

  def animationDriver(self) -> Optional[QAnimationDriver]:
    """
    Calls Qt's 'QAnimationDriver *QSGSoftwareRenderLoop::animationDriver()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#animationDriver

    Returns
    -------

    Optional[QAnimationDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationDriver *QSGSoftwareRenderLoop::animationDriver() const
    ritual = 'ritual_ZNK21QSGSoftwareRenderLoop15animationDriverEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGSoftwareRenderLoop15animationDriverEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QAnimationDriver
    return QAnimationDriver._cuteAt(address)

  def sceneGraphContext(self) -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext *QSGSoftwareRenderLoop::sceneGraphContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#sceneGraphContext

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QSGSoftwareRenderLoop::sceneGraphContext() const
    ritual = 'ritual_ZNK21QSGSoftwareRenderLoop17sceneGraphContextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QSGSoftwareRenderLoop17sceneGraphContextEv'
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
    *QSGSoftwareRenderLoop::createRenderContext(QSGContext *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#createRenderContext

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
    #      *QSGSoftwareRenderLoop::createRenderContext(QSGContext *a0) const
    ritual = (
        'ritual_ZNK21QSGSoftwareRenderLoop19createRenderContextEP10QSGConte'
        'xt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QSGSoftwareRenderLoop19createRenderContextEP10QS'
          'GContext')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

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
    Qt's 'QSGSoftwareRenderLoop::QSGSoftwareRenderLoop()': leans on
    'QSGSoftwareRenderLoop::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QSGSoftwareRenderLoop.__init__' has no cute function yet. Qt's "
        "'QSGSoftwareRenderLoop::QSGSoftwareRenderLoop()': leans on "
        "'QSGSoftwareRenderLoop::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
    Calls Qt's 'void QSGSoftwareRenderLoop::show(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#show

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderLoop::show(QQuickWindow *window)
    ritual = 'ritual_ZN21QSGSoftwareRenderLoop4showEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareRenderLoop4showEP12QQuickWindow'
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def hide(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderLoop::hide(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#hide

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderLoop::hide(QQuickWindow *window)
    ritual = 'ritual_ZN21QSGSoftwareRenderLoop4hideEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareRenderLoop4hideEP12QQuickWindow'
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowDestroyed(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderLoop::windowDestroyed(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#windowDestroyed

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderLoop::windowDestroyed(QQuickWindow *window)
    ritual = (
        'ritual_ZN21QSGSoftwareRenderLoop15windowDestroyedEP12QQuickWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGSoftwareRenderLoop15windowDestroyedEP12QQuickW'
          'indow')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def exposureChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderLoop::exposureChanged(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#exposureChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderLoop::exposureChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN21QSGSoftwareRenderLoop15exposureChangedEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def grab(self, window: Optional[QQuickWindow]) -> QImage:
    """
    Calls Qt's 'QImage QSGSoftwareRenderLoop::grab(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#grab

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
    #  QImage QSGSoftwareRenderLoop::grab(QQuickWindow *window)
    address = self.uglySide.call(
        'ritual_ZN21QSGSoftwareRenderLoop4grabEP12QQuickWindow',
        self._addressOf(window),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(QQuickWindow)
  @overload(NoneType)
  def maybeUpdate(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderLoop::maybeUpdate(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#maybeUpdate

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderLoop::maybeUpdate(QQuickWindow *window)
    ritual = 'ritual_ZN21QSGSoftwareRenderLoop11maybeUpdateEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGSoftwareRenderLoop11maybeUpdateEP12QQuickWindo'
          'w')
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def update(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderLoop::update(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#update

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderLoop::update(QQuickWindow *window)
    ritual = 'ritual_ZN21QSGSoftwareRenderLoop6updateEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QSGSoftwareRenderLoop6updateEP12QQuickWindow'
    self.uglySide.call(ritual, self._addressOf(window))

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleUpdateRequest(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderLoop::handleUpdateRequest(QQuickWindow
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#handleUpdateRequest

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderLoop::handleUpdateRequest(QQuickWindow *a0)
    self.uglySide.call(
        'ritual_ZN21QSGSoftwareRenderLoop19handleUpdateRequestEP12QQuickWin'
        'dow',
        self._addressOf(a0),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def releaseResources(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderLoop::releaseResources(QQuickWindow
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderloop.html#releaseResources

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderLoop::releaseResources(QQuickWindow *a0)
    ritual = (
        'ritual_ZN21QSGSoftwareRenderLoop16releaseResourcesEP12QQuickWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QSGSoftwareRenderLoop16releaseResourcesEP12QQuick'
          'Window')
    self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def renderWindow(*__, **_) -> Never:
    """
    Qt's 'void QSGSoftwareRenderLoop::renderWindow(QQuickWindow *window, bool
    isNewExpose)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QSG_renderWindow'; did you mean 'renderWindow'?.
    """
    raise NotImplementedError(
        "'QSGSoftwareRenderLoop.renderWindow' has no cute function yet. "
        "Qt's 'void QSGSoftwareRenderLoop::renderWindow(QQuickWindow "
        "*window, bool isNewExpose)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'QSG_renderWindow'; did you mean "
        "'renderWindow'?.")
