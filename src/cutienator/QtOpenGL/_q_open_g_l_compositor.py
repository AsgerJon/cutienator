"""
QOpenGLCompositor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositor_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QOpenGLCompositor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QOpenGLTextureBlitter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect
  from ..QtGui import QImage, QOpenGLContext, QWindow
  from . import QOpenGLCompositorWindow, QOpenGLFramebufferObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLCompositorWindow = WAIT['QOpenGLCompositorWindow']
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLFramebufferObject = WAIT['QOpenGLFramebufferObject']
  QRect = WAIT['QRect']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLCompositor(QObject):
  """
  The cute side of Qt's QOpenGLCompositor: a plain Python object standing in
  front of one C++ QOpenGLCompositor.

  It is built on the cute 'QObject', as Qt's QOpenGLCompositor is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLCompositor that has a ritual and that Python
  can call so far, 23 names in all: 'metaObject', 'tr', 'instance',
  'destroy', 'setTargetWindow', 'setTargetContext', 'setRotation', 'context',
  'targetWindow', 'nativeTargetGeometry', 'update', 'grab',
  'grabToFrameBufferObject', 'windows', 'addWindow', 'removeWindow',
  'moveToTop', 'changeWindowIndex', 'topWindowChanged',
  'handleRenderAllRequest', 'renderAll', 'render', 'ensureCorrectZOrder'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLCompositor::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QOpenGLCompositor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLCompositor::~QOpenGLCompositor()': the destructor: Python
    never removes a C++ QOpenGLCompositor.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QOpenGLCompositor is created at the first use, not by
    'QOpenGLCompositor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLCompositor.
  - Qt tells when it has removed the C++ QOpenGLCompositor. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QOpenGLCompositor, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class GrabOrientation(CuteNum):
    """
    The enum 'QOpenGLCompositor::GrabOrientation' of Qt, with the 2 names Qt
    gives in it.
    """

    Flipped = Kee[int](0)
    NotFlipped = Kee[int](1)

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
    Calls Qt's 'QString QOpenGLCompositor::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#tr

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
    #  QString QOpenGLCompositor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QOpenGLCompositor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[QOpenGLCompositor]:
    """
    Calls Qt's 'QOpenGLCompositor *QOpenGLCompositor::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#instance

    Returns
    -------

    Optional[QOpenGLCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLCompositor *QOpenGLCompositor::instance()
    address = Rituals.call('ritual_ZN17QOpenGLCompositor8instanceEv')
    return QOpenGLCompositor._cuteAt(address)

  @staticmethod
  def destroy() -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#destroy
    """
    #  void QOpenGLCompositor::destroy()
    Rituals.call('ritual_ZN17QOpenGLCompositor7destroyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLCompositor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLCompositor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLCompositor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpenGLCompositor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def context(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLCompositor::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#context

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLCompositor::context() const
    address = self.uglySide.call('ritual_ZNK17QOpenGLCompositor7contextEv')
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  def targetWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QOpenGLCompositor::targetWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#targetWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QOpenGLCompositor::targetWindow() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpenGLCompositor12targetWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def nativeTargetGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QOpenGLCompositor::nativeTargetGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#nativeTargetGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QOpenGLCompositor::nativeTargetGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK17QOpenGLCompositor20nativeTargetGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def windows(self) -> QList[QOpenGLCompositorWindow]:
    """
    Calls Qt's 'QList<QOpenGLCompositorWindow *> QOpenGLCompositor::windows()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#windows

    Returns
    -------

    QList[QOpenGLCompositorWindow]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpenGLCompositorWindow *> QOpenGLCompositor::windows() const
    address = self.uglySide.call('ritual_ZNK17QOpenGLCompositor7windowsEv')
    from . import QOpenGLCompositorWindow
    return QList[QOpenGLCompositorWindow]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWindow, QRect)
  @overload(NoneType, QRect)
  def setTargetWindow(
      self,
      window: Optional[QWindow],
      nativeTargetGeometry: QRect,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::setTargetWindow(QWindow *window,
    const QRect &nativeTargetGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#setTargetWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    nativeTargetGeometry : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QOpenGLCompositor::setTargetWindow(QWindow *window, const QRect
    #      &nativeTargetGeometry)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor15setTargetWindowEP7QWindowRK5QRect',
        self._addressOf(window), self._valueOf(nativeTargetGeometry),
    )

  @overload(QOpenGLContext)
  @overload(NoneType)
  def setTargetContext(self, context: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::setTargetContext(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#setTargetContext

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLCompositor::setTargetContext(QOpenGLContext *context)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor16setTargetContextEP14QOpenGLContext',
        self._addressOf(context),
    )

  @overload(int)
  def setRotation(self, degrees: int) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::setRotation(int degrees)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#setRotation

    Parameters
    ----------

    degrees : int
      Passed on as it is.
    """
    #  void QOpenGLCompositor::setRotation(int degrees)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor11setRotationEi', degrees,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLCompositor::QOpenGLCompositor()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#QOpenGLCompositor
    """
    #  QOpenGLCompositor::QOpenGLCompositor()
    self._noteCreation(QOpenGLCompositor, lambda: Rituals.call(
        'ritual_ZN17QOpenGLCompositorC1Ev',
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

  def update(self) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#update
    """
    #  void QOpenGLCompositor::update()
    self.uglySide.call('ritual_ZN17QOpenGLCompositor6updateEv')

  def grab(self) -> QImage:
    """
    Calls Qt's 'QImage QOpenGLCompositor::grab()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#grab

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QOpenGLCompositor::grab()
    address = self.uglySide.call('ritual_ZN17QOpenGLCompositor4grabEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(QOpenGLFramebufferObject)
  @overload(NoneType)
  @overload(QOpenGLFramebufferObject, GrabOrientation)
  @overload(NoneType, GrabOrientation)
  def grabToFrameBufferObject(
      self,
      fbo: Optional[QOpenGLFramebufferObject],
      orientation: GrabOrientation = GrabOrientation.Flipped,
  ) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLCompositor::grabToFrameBufferObject(QOpenGLFramebufferObject *fbo,
    GrabOrientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#grabToFrameBufferObject

    Parameters
    ----------

    fbo : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : GrabOrientation
      Passed on as its number. May be left out, as in Qt: it is then
      GrabOrientation.Flipped.
    """
    #  bool QOpenGLCompositor::grabToFrameBufferObject(
    #      QOpenGLFramebufferObject *fbo, GrabOrientation orientation)
    return self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor23grabToFrameBufferObjectEP24QOpenGLFr'
        'amebufferObjectNS_15GrabOrientationE',
        self._addressOf(fbo), orientation.value,
    )

  @overload(QOpenGLCompositorWindow)
  @overload(NoneType)
  def addWindow(self, window: Optional[QOpenGLCompositorWindow]) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::addWindow(QOpenGLCompositorWindow
    *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#addWindow

    Parameters
    ----------

    window : Optional[QOpenGLCompositorWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLCompositor::addWindow(QOpenGLCompositorWindow *window)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor9addWindowEP23QOpenGLCompositorWindow',
        self._addressOf(window),
    )

  @overload(QOpenGLCompositorWindow)
  @overload(NoneType)
  def removeWindow(self, window: Optional[QOpenGLCompositorWindow]) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::removeWindow(QOpenGLCompositorWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#removeWindow

    Parameters
    ----------

    window : Optional[QOpenGLCompositorWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLCompositor::removeWindow(QOpenGLCompositorWindow *window)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor12removeWindowEP23QOpenGLCompositorWin'
        'dow',
        self._addressOf(window),
    )

  @overload(QOpenGLCompositorWindow)
  @overload(NoneType)
  def moveToTop(self, window: Optional[QOpenGLCompositorWindow]) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::moveToTop(QOpenGLCompositorWindow
    *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#moveToTop

    Parameters
    ----------

    window : Optional[QOpenGLCompositorWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLCompositor::moveToTop(QOpenGLCompositorWindow *window)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor9moveToTopEP23QOpenGLCompositorWindow',
        self._addressOf(window),
    )

  @overload(QOpenGLCompositorWindow, int)
  @overload(NoneType, int)
  def changeWindowIndex(
      self,
      window: Optional[QOpenGLCompositorWindow],
      newIdx: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLCompositor::changeWindowIndex(QOpenGLCompositorWindow *window, int
    newIdx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#changeWindowIndex

    Parameters
    ----------

    window : Optional[QOpenGLCompositorWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newIdx : int
      Passed on as it is.
    """
    #  void QOpenGLCompositor::changeWindowIndex(QOpenGLCompositorWindow
    #      *window, int newIdx)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor17changeWindowIndexEP23QOpenGLComposit'
        'orWindowi',
        self._addressOf(window), newIdx,
    )

  @overload(QOpenGLCompositorWindow)
  @overload(NoneType)
  def topWindowChanged(
      self,
      window: Optional[QOpenGLCompositorWindow],
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLCompositor::topWindowChanged(QOpenGLCompositorWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#topWindowChanged

    Parameters
    ----------

    window : Optional[QOpenGLCompositorWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLCompositor::topWindowChanged(QOpenGLCompositorWindow
    #      *window)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor16topWindowChangedEP23QOpenGLComposito'
        'rWindow',
        self._addressOf(window),
    )

  def handleRenderAllRequest(self) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::handleRenderAllRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#handleRenderAllRequest
    """
    #  void QOpenGLCompositor::handleRenderAllRequest()
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor22handleRenderAllRequestEv',
    )

  @overload(QOpenGLFramebufferObject)
  @overload(NoneType)
  @overload(QOpenGLFramebufferObject, QOpenGLTextureBlitter.Origin)
  @overload(NoneType, QOpenGLTextureBlitter.Origin)
  def renderAll(
      self,
      fbo: Optional[QOpenGLFramebufferObject],
      origin: QOpenGLTextureBlitter.Origin = (
          QOpenGLTextureBlitter.Origin.OriginTopLeft),
  ) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::renderAll(QOpenGLFramebufferObject
    *fbo, QOpenGLTextureBlitter::Origin origin)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#renderAll

    Parameters
    ----------

    fbo : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    origin : QOpenGLTextureBlitter.Origin
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLTextureBlitter.Origin.OriginTopLeft.
    """
    #  void QOpenGLCompositor::renderAll(QOpenGLFramebufferObject *fbo,
    #      QOpenGLTextureBlitter::Origin origin)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor9renderAllEP24QOpenGLFramebufferObject'
        'N21QOpenGLTextureBlitter6OriginE',
        self._addressOf(fbo), origin.value,
    )

  @overload(QOpenGLCompositorWindow)
  @overload(NoneType)
  @overload(QOpenGLCompositorWindow, QOpenGLTextureBlitter.Origin)
  @overload(NoneType, QOpenGLTextureBlitter.Origin)
  def render(
      self,
      window: Optional[QOpenGLCompositorWindow],
      origin: QOpenGLTextureBlitter.Origin = (
          QOpenGLTextureBlitter.Origin.OriginTopLeft),
  ) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::render(QOpenGLCompositorWindow
    *window, QOpenGLTextureBlitter::Origin origin)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcompositor.html#render

    Parameters
    ----------

    window : Optional[QOpenGLCompositorWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    origin : QOpenGLTextureBlitter.Origin
      Passed on as its number. May be left out, as in Qt: it is then
      QOpenGLTextureBlitter.Origin.OriginTopLeft.
    """
    #  void QOpenGLCompositor::render(QOpenGLCompositorWindow *window,
    #      QOpenGLTextureBlitter::Origin origin)
    self.uglySide.call(
        'ritual_ZN17QOpenGLCompositor6renderEP23QOpenGLCompositorWindowN21Q'
        'OpenGLTextureBlitter6OriginE',
        self._addressOf(window), origin.value,
    )

  def ensureCorrectZOrder(self) -> None:
    """
    Calls Qt's 'void QOpenGLCompositor::ensureCorrectZOrder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositor.html#ensureCorrectZOrder
    """
    #  void QOpenGLCompositor::ensureCorrectZOrder()
    self.uglySide.call('ritual_ZN17QOpenGLCompositor19ensureCorrectZOrderEv')
