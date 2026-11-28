"""
QSGRenderLoop binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrenderloop_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGRenderLoop to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAnimationDriver, QMetaObject, QRunnable
  from ..QtGui import QImage
  from . import QQuickWindow, QSGContext, QSGRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']
  QRunnable = WAIT['QRunnable']
  QSGContext = WAIT['QSGContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRenderLoop(QObject):
  """
  The cute side of Qt's QSGRenderLoop: a plain Python object standing in
  front of one C++ QSGRenderLoop.

  It is built on the cute 'QObject', as Qt's QSGRenderLoop is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRenderLoop that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'show', 'hide', 'resize',
  'windowDestroyed', 'exposureChanged', 'grab', 'update', 'maybeUpdate',
  'handleUpdateRequest', 'animationDriver', 'sceneGraphContext',
  'createRenderContext', 'releaseResources', 'postJob', 'addWindow',
  'removeWindow', 'windowSurfaceType', 'instance', 'setInstance',
  'interleaveIncubation', 'flags', 'cleanup', 'handleContextCreationFailure',
  'timeToIncubate'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGRenderLoop::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSGRenderLoop::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSGRenderLoop::~QSGRenderLoop()': the destructor: Python never
    removes a C++ QSGRenderLoop.
  - Qt's 'QSet<QQuickWindow *> QSGRenderLoop::windows() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGRenderLoop is created at the first use, not by
    'QSGRenderLoop(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRenderLoop.
  - Qt tells when it has removed the C++ QSGRenderLoop. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGRenderLoop that has no cute function yet, 'windows',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QSGRenderLoop, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RenderLoopFlags(CuteNum):
    """
    The enum 'QSGRenderLoop::RenderLoopFlags' of Qt, with the 1 names Qt
    gives in it.
    """

    SupportsGrabWithoutExpose = Kee[int](1)

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
    Calls Qt's 'QString QSGRenderLoop::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#tr

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
    #  QString QSGRenderLoop::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QSGRenderLoop2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[QSGRenderLoop]:
    """
    Calls Qt's 'QSGRenderLoop *QSGRenderLoop::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#instance

    Returns
    -------

    Optional[QSGRenderLoop]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGRenderLoop *QSGRenderLoop::instance()
    address = Rituals.call('ritual_ZN13QSGRenderLoop8instanceEv')
    return QSGRenderLoop._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def setInstance(instance: Optional[QSGRenderLoop]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::setInstance(QSGRenderLoop *instance)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#setInstance

    Parameters
    ----------

    instance : Optional[QSGRenderLoop]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::setInstance(QSGRenderLoop *instance)
    Rituals.call(
        'ritual_ZN13QSGRenderLoop11setInstanceEPS_',
        CuteMixin._addressOf(instance),
    )

  @staticmethod
  def cleanup() -> None:
    """
    Calls Qt's 'void QSGRenderLoop::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#cleanup
    """
    #  void QSGRenderLoop::cleanup()
    Rituals.call('ritual_ZN13QSGRenderLoop7cleanupEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRenderLoop'

  #  A C++ QSGRenderLoop Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRenderLoop'

  #  The functions Qt calls itself that QSGRenderLoop is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'show': (
          ('_ZN13QSGRenderLoop4showEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'hide': (
          ('_ZN13QSGRenderLoop4hideEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'resize': (
          ('_ZN13QSGRenderLoop6resizeEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'windowDestroyed': (
          ('_ZN13QSGRenderLoop15windowDestroyedEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'exposureChanged': (
          ('_ZN13QSGRenderLoop15exposureChangedEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'grab': (
          ('_ZN13QSGRenderLoop4grabEP12QQuickWindow',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'update': (
          ('_ZN13QSGRenderLoop6updateEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'maybeUpdate': (
          ('_ZN13QSGRenderLoop11maybeUpdateEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'handleUpdateRequest': (
          ('_ZN13QSGRenderLoop19handleUpdateRequestEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'animationDriver': (
          ('_ZNK13QSGRenderLoop15animationDriverEv',
           ('address', 'address', 'QtCore:QAnimationDriver'),
           ()),
      ),
      'sceneGraphContext': (
          ('_ZNK13QSGRenderLoop17sceneGraphContextEv',
           ('address', 'address', 'QtQuick:QSGContext'),
           ()),
      ),
      'createRenderContext': (
          ('_ZNK13QSGRenderLoop19createRenderContextEP10QSGContext',
           ('address', 'address', 'QtQuick:QSGRenderContext'),
           (
               ('address', 'address', 'QtQuick:QSGContext'),
           )),
      ),
      'releaseResources': (
          ('_ZN13QSGRenderLoop16releaseResourcesEP12QQuickWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'postJob': (
          ('_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
               ('address', 'address', 'QtCore:QRunnable'),
           )),
      ),
      'windowSurfaceType': (
          ('_ZNK13QSGRenderLoop17windowSurfaceTypeEv',
           ('int', 'enum', 'QtGui:QSurface.SurfaceType'),
           ()),
      ),
      'interleaveIncubation': (
          ('_ZNK13QSGRenderLoop20interleaveIncubationEv',
           ('bool', 'number', ''),
           ()),
      ),
      'flags': (
          ('_ZNK13QSGRenderLoop5flagsEv',
           ('int', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSGRenderLoop::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGRenderLoop::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QSGRenderLoop10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def animationDriver(self) -> Optional[QAnimationDriver]:
    """
    Calls Qt's 'QAnimationDriver *QSGRenderLoop::animationDriver() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#animationDriver

    Returns
    -------

    Optional[QAnimationDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationDriver *QSGRenderLoop::animationDriver() const
    address = self.uglySide.call(
        'ritual_ZNK13QSGRenderLoop15animationDriverEv',
    )
    from ..QtCore import QAnimationDriver
    return QAnimationDriver._cuteAt(address)

  def sceneGraphContext(self) -> Optional[QSGContext]:
    """
    Calls Qt's 'QSGContext *QSGRenderLoop::sceneGraphContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderloop.html#sceneGraphContext

    Returns
    -------

    Optional[QSGContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGContext *QSGRenderLoop::sceneGraphContext() const
    address = self.uglySide.call(
        'ritual_ZNK13QSGRenderLoop17sceneGraphContextEv',
    )
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
    *QSGRenderLoop::createRenderContext(QSGContext *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderloop.html#createRenderContext

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
    #  QSGRenderContext *QSGRenderLoop::createRenderContext(QSGContext *a0)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QSGRenderLoop19createRenderContextEP10QSGContext',
        self._addressOf(a0),
    )
    from . import QSGRenderContext
    return QSGRenderContext._cuteAt(address)

  def windowSurfaceType(self) -> QSurface.SurfaceType:
    """
    Calls Qt's 'QSurface::SurfaceType QSGRenderLoop::windowSurfaceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderloop.html#windowSurfaceType

    Returns
    -------

    QSurface.SurfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSurface.SurfaceType(number)' gives.
    """
    #  QSurface::SurfaceType QSGRenderLoop::windowSurfaceType() const
    ritual = 'ritual_ZNK13QSGRenderLoop17windowSurfaceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSGRenderLoop17windowSurfaceTypeEv'
    return QSurface.SurfaceType(self.uglySide.call(ritual))

  def interleaveIncubation(self) -> bool:
    """
    Calls Qt's 'bool QSGRenderLoop::interleaveIncubation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderloop.html#interleaveIncubation
    """
    #  bool QSGRenderLoop::interleaveIncubation() const
    ritual = 'ritual_ZNK13QSGRenderLoop20interleaveIncubationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSGRenderLoop20interleaveIncubationEv'
    return self.uglySide.call(ritual)

  def flags(self) -> int:
    """
    Calls Qt's 'int QSGRenderLoop::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#flags
    """
    #  int QSGRenderLoop::flags() const
    ritual = 'ritual_ZNK13QSGRenderLoop5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QSGRenderLoop5flagsEv'
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
    Calls Qt's 'void QSGRenderLoop::show(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#show

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::show(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop4showEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def hide(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::hide(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#hide

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::hide(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop4hideEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def resize(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::resize(QQuickWindow *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#resize

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::resize(QQuickWindow *a0)
    ritual = 'ritual_ZN13QSGRenderLoop6resizeEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QSGRenderLoop6resizeEP12QQuickWindow'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickWindow)
  @overload(NoneType)
  def windowDestroyed(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::windowDestroyed(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#windowDestroyed

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::windowDestroyed(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop15windowDestroyedEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def exposureChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::exposureChanged(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#exposureChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::exposureChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop15exposureChangedEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def grab(self, window: Optional[QQuickWindow]) -> QImage:
    """
    Calls Qt's 'QImage QSGRenderLoop::grab(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#grab

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
    #  QImage QSGRenderLoop::grab(QQuickWindow *window)
    address = self.uglySide.call(
        'ritual_ZN13QSGRenderLoop4grabEP12QQuickWindow',
        self._addressOf(window),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(QQuickWindow)
  @overload(NoneType)
  def update(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::update(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#update

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::update(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop6updateEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def maybeUpdate(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::maybeUpdate(QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#maybeUpdate

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::maybeUpdate(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop11maybeUpdateEP12QQuickWindow',
        self._addressOf(window),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleUpdateRequest(self, a0: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::handleUpdateRequest(QQuickWindow *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderloop.html#handleUpdateRequest

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::handleUpdateRequest(QQuickWindow *a0)
    ritual = 'ritual_ZN13QSGRenderLoop19handleUpdateRequestEP12QQuickWindow'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QSGRenderLoop19handleUpdateRequestEP12QQuickWindo'
          'w')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickWindow)
  @overload(NoneType)
  def releaseResources(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::releaseResources(QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderloop.html#releaseResources

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::releaseResources(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop16releaseResourcesEP12QQuickWindow',
        self._addressOf(window),
    )

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
    Calls Qt's 'void QSGRenderLoop::postJob(QQuickWindow *window, QRunnable
    *job)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#postJob

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    job : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
    ritual = 'ritual_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable')
    self.uglySide.call(
        ritual, self._addressOf(window), self._addressOf(job, 'QRunnable'),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def addWindow(self, win: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::addWindow(QQuickWindow *win)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#addWindow

    Parameters
    ----------

    win : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::addWindow(QQuickWindow *win)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop9addWindowEP12QQuickWindow',
        self._addressOf(win),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def removeWindow(self, win: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::removeWindow(QQuickWindow *win)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#removeWindow

    Parameters
    ----------

    win : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::removeWindow(QQuickWindow *win)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop12removeWindowEP12QQuickWindow',
        self._addressOf(win),
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleContextCreationFailure(
      self,
      window: Optional[QQuickWindow],
  ) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::handleContextCreationFailure(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrenderloop.html#handleContextCreationFailure

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRenderLoop::handleContextCreationFailure(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN13QSGRenderLoop28handleContextCreationFailureEP12QQuickWi'
        'ndow',
        self._addressOf(window),
    )

  def timeToIncubate(self) -> None:
    """
    Calls Qt's 'void QSGRenderLoop::timeToIncubate()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrenderloop.html#timeToIncubate
    """
    #  void QSGRenderLoop::timeToIncubate()
    self.uglySide.call('ritual_ZN13QSGRenderLoop14timeToIncubateEv')

  @staticmethod
  def windows(*__, **_) -> Never:
    """
    Qt's 'QSet<QQuickWindow *> QSGRenderLoop::windows() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSGRenderLoop.windows' has no cute function yet. Qt's "
        "'QSet<QQuickWindow *> QSGRenderLoop::windows() const': gives a "
        "type Python has no way to take yet.")
