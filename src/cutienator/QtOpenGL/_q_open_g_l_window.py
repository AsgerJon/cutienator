"""
QOpenGLWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtGui import QPaintDevice, QPaintDeviceWindow, QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QImage, QOpenGLContext, QPaintEvent, QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLWindow(QPaintDeviceWindow):
  """
  The cute side of Qt's QOpenGLWindow: a plain Python object standing in
  front of one C++ QOpenGLWindow.

  It is built on the cute 'QPaintDeviceWindow', as Qt's QOpenGLWindow is
  built on Qt's QPaintDeviceWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLWindow that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'updateBehavior',
  'isValid', 'makeCurrent', 'doneCurrent', 'context', 'shareContext',
  'defaultFramebufferObject', 'grabFramebuffer', 'frameSwapped',
  'initializeGL', 'resizeGL', 'paintGL', 'paintUnderGL', 'paintOverGL',
  'paintEvent', 'resizeEvent', 'metric', 'redirected'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLWindow::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QOpenGLWindow::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLWindowPrivate *QOpenGLWindow::d_func()': gives
    'QOpenGLWindowPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLWindowPrivate *QOpenGLWindow::d_func() const': gives
    'QOpenGLWindowPrivate', which has no cute class yet.
  - Qt's 'QOpenGLWindow::~QOpenGLWindow()': the destructor: Python never
    removes a C++ QOpenGLWindow.

  What has no ritual
  ------------------

  4 of the 31 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLWindow is created at the first use, not by
    'QOpenGLWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLWindow.
  - Qt tells when it has removed the C++ QOpenGLWindow. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QOpenGLWindow, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class UpdateBehavior(CuteNum):
    """
    The enum 'QOpenGLWindow::UpdateBehavior' of Qt, with the 3 names Qt gives
    in it.
    """

    NoPartialUpdate = Kee[int](0)
    PartialUpdateBlit = Kee[int](1)
    PartialUpdateBlend = Kee[int](2)

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
    Calls Qt's 'QString QOpenGLWindow::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#tr

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
    #  QString QOpenGLWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QOpenGLWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLWindow'

  #  A C++ QOpenGLWindow Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLWindow'

  #  The functions Qt calls itself that QOpenGLWindow is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initializeGL': (
          ('_ZN13QOpenGLWindow12initializeGLEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resizeGL': (
          ('_ZN13QOpenGLWindow8resizeGLEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'paintGL': (
          ('_ZN13QOpenGLWindow7paintGLEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'paintUnderGL': (
          ('_ZN13QOpenGLWindow12paintUnderGLEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'paintOverGL': (
          ('_ZN13QOpenGLWindow11paintOverGLEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject *QOpenGLWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QOpenGLWindow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def updateBehavior(self) -> UpdateBehavior:
    """
    Calls Qt's 'UpdateBehavior QOpenGLWindow::updateBehavior() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#updateBehavior

    Returns
    -------

    UpdateBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UpdateBehavior(number)'
      gives.
    """
    #  UpdateBehavior QOpenGLWindow::updateBehavior() const
    return QOpenGLWindow.UpdateBehavior(self.uglySide.call(
        'ritual_ZNK13QOpenGLWindow14updateBehaviorEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLWindow::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#isValid
    """
    #  bool QOpenGLWindow::isValid() const
    return self.uglySide.call('ritual_ZNK13QOpenGLWindow7isValidEv')

  def context(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLWindow::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#context

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLWindow::context() const
    address = self.uglySide.call('ritual_ZNK13QOpenGLWindow7contextEv')
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  def shareContext(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLWindow::shareContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#shareContext

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLWindow::shareContext() const
    address = self.uglySide.call('ritual_ZNK13QOpenGLWindow12shareContextEv')
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  def defaultFramebufferObject(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLWindow::defaultFramebufferObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglwindow.html#defaultFramebufferObject
    """
    #  GLuint QOpenGLWindow::defaultFramebufferObject() const
    return self.uglySide.call(
        'ritual_ZNK13QOpenGLWindow24defaultFramebufferObjectEv',
    )

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QOpenGLWindow::metric(PaintDeviceMetric metric) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QOpenGLWindow::metric(PaintDeviceMetric metric) const
    ritual = (
        'ritual_ZNK13QOpenGLWindow6metricEN12QPaintDevice17PaintDeviceMetri'
        'cE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QOpenGLWindow6metricEN12QPaintDevice17PaintDevic'
          'eMetricE')
    return self.uglySide.call(ritual, metric.value)

  @overload(QPoint)
  @overload(NoneType)
  def redirected(self, a0: Optional[QPoint]) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QOpenGLWindow::redirected(QPoint *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#redirected

    Parameters
    ----------

    a0 : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QOpenGLWindow::redirected(QPoint *a0) const
    ritual = 'ritual_ZNK13QOpenGLWindow10redirectedEP6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QOpenGLWindow10redirectedEP6QPoint'
    address = self.uglySide.call(ritual, self._addressOf(a0))
    return QPaintDevice._cuteAt(address)

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

  @overload()
  @overload(UpdateBehavior)
  @overload(UpdateBehavior, QWindow)
  @overload(UpdateBehavior, NoneType)
  def __init__(
      self,
      updateBehavior: UpdateBehavior = UpdateBehavior.NoPartialUpdate,
      parent: Optional[QWindow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLWindow::QOpenGLWindow(UpdateBehavior updateBehavior, QWindow
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#QOpenGLWindow

    Parameters
    ----------

    updateBehavior : UpdateBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      UpdateBehavior.NoPartialUpdate.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLWindow::QOpenGLWindow(UpdateBehavior updateBehavior, QWindow
    #      *parent)
    self._noteCreation(QOpenGLWindow, lambda: Rituals.call(
        'ritual_ZN13QOpenGLWindowC1ENS_14UpdateBehaviorEP7QWindow',
        updateBehavior.value, self._addressOf(parent),
    ))

  @overload(QOpenGLContext)
  @overload(NoneType)
  @overload(QOpenGLContext, UpdateBehavior)
  @overload(NoneType, UpdateBehavior)
  @overload(QOpenGLContext, UpdateBehavior, QWindow)
  @overload(QOpenGLContext, UpdateBehavior, NoneType)
  @overload(NoneType, UpdateBehavior, QWindow)
  @overload(NoneType, UpdateBehavior, NoneType)
  def __init__(
      self,
      shareContext: Optional[QOpenGLContext],
      updateBehavior: UpdateBehavior = UpdateBehavior.NoPartialUpdate,
      parent: Optional[QWindow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLWindow::QOpenGLWindow(QOpenGLContext *shareContext,
    UpdateBehavior updateBehavior, QWindow *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#QOpenGLWindow

    Parameters
    ----------

    shareContext : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    updateBehavior : UpdateBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      UpdateBehavior.NoPartialUpdate.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLWindow::QOpenGLWindow(QOpenGLContext *shareContext,
    #      UpdateBehavior updateBehavior, QWindow *parent)
    self._noteCreation(QOpenGLWindow, lambda: Rituals.call(
        'ritual_ZN13QOpenGLWindowC1EP14QOpenGLContextNS_14UpdateBehaviorEP7'
        'QWindow',
        self._addressOf(shareContext), updateBehavior.value,
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

  def makeCurrent(self) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::makeCurrent()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#makeCurrent
    """
    #  void QOpenGLWindow::makeCurrent()
    self.uglySide.call('ritual_ZN13QOpenGLWindow11makeCurrentEv')

  def doneCurrent(self) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::doneCurrent()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#doneCurrent
    """
    #  void QOpenGLWindow::doneCurrent()
    self.uglySide.call('ritual_ZN13QOpenGLWindow11doneCurrentEv')

  def grabFramebuffer(self) -> QImage:
    """
    Calls Qt's 'QImage QOpenGLWindow::grabFramebuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#grabFramebuffer

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QOpenGLWindow::grabFramebuffer()
    address = self.uglySide.call(
        'ritual_ZN13QOpenGLWindow15grabFramebufferEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def frameSwapped(self) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::frameSwapped()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#frameSwapped
    """
    #  void QOpenGLWindow::frameSwapped()
    self.uglySide.call('ritual_ZN13QOpenGLWindow12frameSwappedEv')

  def initializeGL(self) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::initializeGL()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#initializeGL
    """
    #  void QOpenGLWindow::initializeGL()
    ritual = 'ritual_ZN13QOpenGLWindow12initializeGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWindow12initializeGLEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def resizeGL(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::resizeGL(int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#resizeGL

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QOpenGLWindow::resizeGL(int w, int h)
    ritual = 'ritual_ZN13QOpenGLWindow8resizeGLEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWindow8resizeGLEii'
    self.uglySide.call(ritual, w, h)

  def paintGL(self) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::paintGL()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#paintGL
    """
    #  void QOpenGLWindow::paintGL()
    ritual = 'ritual_ZN13QOpenGLWindow7paintGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWindow7paintGLEv'
    self.uglySide.call(ritual)

  def paintUnderGL(self) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::paintUnderGL()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#paintUnderGL
    """
    #  void QOpenGLWindow::paintUnderGL()
    ritual = 'ritual_ZN13QOpenGLWindow12paintUnderGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWindow12paintUnderGLEv'
    self.uglySide.call(ritual)

  def paintOverGL(self) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::paintOverGL()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#paintOverGL
    """
    #  void QOpenGLWindow::paintOverGL()
    ritual = 'ritual_ZN13QOpenGLWindow11paintOverGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWindow11paintOverGLEv'
    self.uglySide.call(ritual)

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLWindow::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN13QOpenGLWindow10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWindow10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QOpenGLWindow::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwindow.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLWindow::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN13QOpenGLWindow11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWindow11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))
