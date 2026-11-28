"""
QOpenGLWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGLWidgets/qopenglwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QPaintDevice
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint
  from ..QtGui import QImage, QOpenGLContext, QPaintEngine, QPaintEvent
  from ..QtGui import QResizeEvent, QSurfaceFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QResizeEvent = WAIT['QResizeEvent']
  QSurfaceFormat = WAIT['QSurfaceFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLWidget(QWidget):
  """
  The cute side of Qt's QOpenGLWidget: a plain Python object standing in
  front of one C++ QOpenGLWidget.

  It is built on the cute 'QWidget', as Qt's QOpenGLWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLWidget that has a ritual and that Python can
  call so far, 28 names in all: 'metaObject', 'tr', 'setUpdateBehavior',
  'updateBehavior', 'setFormat', 'format', 'textureFormat',
  'setTextureFormat', 'isValid', 'makeCurrent', 'doneCurrent', 'context',
  'defaultFramebufferObject', 'grabFramebuffer', 'currentTargetBuffer',
  'aboutToCompose', 'frameSwapped', 'aboutToResize', 'resized',
  'initializeGL', 'resizeGL', 'paintGL', 'paintEvent', 'resizeEvent',
  'event', 'metric', 'redirected', 'paintEngine'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLWidget::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QOpenGLWidget::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLWidgetPrivate *QOpenGLWidget::d_func()': gives
    'QOpenGLWidgetPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLWidgetPrivate *QOpenGLWidget::d_func() const': gives
    'QOpenGLWidgetPrivate', which has no cute class yet.
  - Qt's 'QOpenGLWidget::~QOpenGLWidget()': the destructor: Python never
    removes a C++ QOpenGLWidget.

  What has no ritual
  ------------------

  4 of the 41 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLWidget is created at the first use, not by
    'QOpenGLWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLWidget.
  - Qt tells when it has removed the C++ QOpenGLWidget. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QOpenGLWidget, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class TargetBuffer(CuteNum):
    """
    The enum 'QOpenGLWidget::TargetBuffer' of Qt, with the 2 names Qt gives
    in it.
    """

    LeftBuffer = Kee[int](0)
    RightBuffer = Kee[int](1)

  class UpdateBehavior(CuteNum):
    """
    The enum 'QOpenGLWidget::UpdateBehavior' of Qt, with the 2 names Qt gives
    in it.
    """

    NoPartialUpdate = Kee[int](0)
    PartialUpdate = Kee[int](1)

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
    Calls Qt's 'QString QOpenGLWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#tr

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
    #  QString QOpenGLWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QOpenGLWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLWidget'

  #  A C++ QOpenGLWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLWidget'

  #  The functions Qt calls itself that QOpenGLWidget is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initializeGL': (
          ('_ZN13QOpenGLWidget12initializeGLEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resizeGL': (
          ('_ZN13QOpenGLWidget8resizeGLEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'paintGL': (
          ('_ZN13QOpenGLWidget7paintGLEv',
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
    Calls Qt's 'const QMetaObject *QOpenGLWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QOpenGLWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def updateBehavior(self) -> UpdateBehavior:
    """
    Calls Qt's 'UpdateBehavior QOpenGLWidget::updateBehavior() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#updateBehavior

    Returns
    -------

    UpdateBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'UpdateBehavior(number)'
      gives.
    """
    #  UpdateBehavior QOpenGLWidget::updateBehavior() const
    return QOpenGLWidget.UpdateBehavior(self.uglySide.call(
        'ritual_ZNK13QOpenGLWidget14updateBehaviorEv',
    ))

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QOpenGLWidget::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QOpenGLWidget::format() const
    address = self.uglySide.call('ritual_ZNK13QOpenGLWidget6formatEv')
    from ..QtGui import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def textureFormat(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLWidget::textureFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#textureFormat
    """
    #  GLenum QOpenGLWidget::textureFormat() const
    return self.uglySide.call('ritual_ZNK13QOpenGLWidget13textureFormatEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLWidget::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#isValid
    """
    #  bool QOpenGLWidget::isValid() const
    return self.uglySide.call('ritual_ZNK13QOpenGLWidget7isValidEv')

  def context(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLWidget::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#context

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLWidget::context() const
    address = self.uglySide.call('ritual_ZNK13QOpenGLWidget7contextEv')
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  @overload()
  def defaultFramebufferObject(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLWidget::defaultFramebufferObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglwidget.html#defaultFramebufferObject
    """
    #  GLuint QOpenGLWidget::defaultFramebufferObject() const
    return self.uglySide.call(
        'ritual_ZNK13QOpenGLWidget24defaultFramebufferObjectEv',
    )

  @overload(TargetBuffer)
  def defaultFramebufferObject(self, targetBuffer: TargetBuffer) -> int:
    """
    Calls Qt's 'GLuint QOpenGLWidget::defaultFramebufferObject(TargetBuffer
    targetBuffer) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglwidget.html#defaultFramebufferObject

    Parameters
    ----------

    targetBuffer : TargetBuffer
      Passed on as its number.
    """
    #  GLuint QOpenGLWidget::defaultFramebufferObject(TargetBuffer
    #      targetBuffer) const
    return self.uglySide.call(
        'ritual_ZNK13QOpenGLWidget24defaultFramebufferObjectENS_12TargetBuf'
        'ferE',
        targetBuffer.value,
    )

  def currentTargetBuffer(self) -> TargetBuffer:
    """
    Calls Qt's 'TargetBuffer QOpenGLWidget::currentTargetBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglwidget.html#currentTargetBuffer

    Returns
    -------

    TargetBuffer
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TargetBuffer(number)'
      gives.
    """
    #  TargetBuffer QOpenGLWidget::currentTargetBuffer() const
    return QOpenGLWidget.TargetBuffer(self.uglySide.call(
        'ritual_ZNK13QOpenGLWidget19currentTargetBufferEv',
    ))

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QOpenGLWidget::metric(QPaintDevice::PaintDeviceMetric
    metric) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QOpenGLWidget::metric(QPaintDevice::PaintDeviceMetric metric)
    #      const
    ritual = (
        'ritual_ZNK13QOpenGLWidget6metricEN12QPaintDevice17PaintDeviceMetri'
        'cE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13QOpenGLWidget6metricEN12QPaintDevice17PaintDevic'
          'eMetricE')
    return self.uglySide.call(ritual, metric.value)

  @overload(QPoint)
  @overload(NoneType)
  def redirected(self, p: Optional[QPoint]) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QOpenGLWidget::redirected(QPoint *p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#redirected

    Parameters
    ----------

    p : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QOpenGLWidget::redirected(QPoint *p) const
    ritual = 'ritual_ZNK13QOpenGLWidget10redirectedEP6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QOpenGLWidget10redirectedEP6QPoint'
    address = self.uglySide.call(ritual, self._addressOf(p))
    return QPaintDevice._cuteAt(address)

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QOpenGLWidget::paintEngine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QOpenGLWidget::paintEngine() const
    ritual = 'ritual_ZNK13QOpenGLWidget11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QOpenGLWidget11paintEngineEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPaintEngine
    return QPaintEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(UpdateBehavior)
  def setUpdateBehavior(self, updateBehavior: UpdateBehavior) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::setUpdateBehavior(UpdateBehavior
    updateBehavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglwidget.html#setUpdateBehavior

    Parameters
    ----------

    updateBehavior : UpdateBehavior
      Passed on as its number.
    """
    #  void QOpenGLWidget::setUpdateBehavior(UpdateBehavior updateBehavior)
    self.uglySide.call(
        'ritual_ZN13QOpenGLWidget17setUpdateBehaviorENS_14UpdateBehaviorE',
        updateBehavior.value,
    )

  @overload(QSurfaceFormat)
  def setFormat(self, format: QSurfaceFormat) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::setFormat(const QSurfaceFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#setFormat

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  void QOpenGLWidget::setFormat(const QSurfaceFormat &format)
    self.uglySide.call(
        'ritual_ZN13QOpenGLWidget9setFormatERK14QSurfaceFormat',
        self._valueOf(format),
    )

  @overload(int)
  def setTextureFormat(self, texFormat: int) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::setTextureFormat(GLenum texFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglwidget.html#setTextureFormat

    Parameters
    ----------

    texFormat : int
      Passed on as it is.
    """
    #  void QOpenGLWidget::setTextureFormat(GLenum texFormat)
    self.uglySide.call(
        'ritual_ZN13QOpenGLWidget16setTextureFormatEj', texFormat,
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
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLWidget::QOpenGLWidget(QWidget
    *parent, Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#QOpenGLWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QOpenGLWidget::QOpenGLWidget(QWidget *parent, Qt::WindowFlags f)
    self._noteCreation(QOpenGLWidget, lambda: Rituals.call(
        'ritual_ZN13QOpenGLWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
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

  @overload()
  def makeCurrent(self) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::makeCurrent()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#makeCurrent
    """
    #  void QOpenGLWidget::makeCurrent()
    self.uglySide.call('ritual_ZN13QOpenGLWidget11makeCurrentEv')

  @overload(TargetBuffer)
  def makeCurrent(self, targetBuffer: TargetBuffer) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::makeCurrent(TargetBuffer targetBuffer)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#makeCurrent

    Parameters
    ----------

    targetBuffer : TargetBuffer
      Passed on as its number.
    """
    #  void QOpenGLWidget::makeCurrent(TargetBuffer targetBuffer)
    self.uglySide.call(
        'ritual_ZN13QOpenGLWidget11makeCurrentENS_12TargetBufferE',
        targetBuffer.value,
    )

  def doneCurrent(self) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::doneCurrent()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#doneCurrent
    """
    #  void QOpenGLWidget::doneCurrent()
    self.uglySide.call('ritual_ZN13QOpenGLWidget11doneCurrentEv')

  @overload()
  def grabFramebuffer(self) -> QImage:
    """
    Calls Qt's 'QImage QOpenGLWidget::grabFramebuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#grabFramebuffer

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QOpenGLWidget::grabFramebuffer()
    address = self.uglySide.call(
        'ritual_ZN13QOpenGLWidget15grabFramebufferEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(TargetBuffer)
  def grabFramebuffer(self, targetBuffer: TargetBuffer) -> QImage:
    """
    Calls Qt's 'QImage QOpenGLWidget::grabFramebuffer(TargetBuffer
    targetBuffer)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#grabFramebuffer

    Parameters
    ----------

    targetBuffer : TargetBuffer
      Passed on as its number.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QOpenGLWidget::grabFramebuffer(TargetBuffer targetBuffer)
    address = self.uglySide.call(
        'ritual_ZN13QOpenGLWidget15grabFramebufferENS_12TargetBufferE',
        targetBuffer.value,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def aboutToCompose(self) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::aboutToCompose()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#aboutToCompose
    """
    #  void QOpenGLWidget::aboutToCompose()
    self.uglySide.call('ritual_ZN13QOpenGLWidget14aboutToComposeEv')

  def frameSwapped(self) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::frameSwapped()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#frameSwapped
    """
    #  void QOpenGLWidget::frameSwapped()
    self.uglySide.call('ritual_ZN13QOpenGLWidget12frameSwappedEv')

  def aboutToResize(self) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::aboutToResize()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#aboutToResize
    """
    #  void QOpenGLWidget::aboutToResize()
    self.uglySide.call('ritual_ZN13QOpenGLWidget13aboutToResizeEv')

  def resized(self) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::resized()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#resized
    """
    #  void QOpenGLWidget::resized()
    self.uglySide.call('ritual_ZN13QOpenGLWidget7resizedEv')

  def initializeGL(self) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::initializeGL()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#initializeGL
    """
    #  void QOpenGLWidget::initializeGL()
    ritual = 'ritual_ZN13QOpenGLWidget12initializeGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWidget12initializeGLEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def resizeGL(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::resizeGL(int w, int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#resizeGL

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QOpenGLWidget::resizeGL(int w, int h)
    ritual = 'ritual_ZN13QOpenGLWidget8resizeGLEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWidget8resizeGLEii'
    self.uglySide.call(ritual, w, h)

  def paintGL(self) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::paintGL()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#paintGL
    """
    #  void QOpenGLWidget::paintGL()
    ritual = 'ritual_ZN13QOpenGLWidget7paintGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWidget7paintGLEv'
    self.uglySide.call(ritual)

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLWidget::paintEvent(QPaintEvent *e)
    ritual = 'ritual_ZN13QOpenGLWidget10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWidget10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QOpenGLWidget::resizeEvent(QResizeEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLWidget::resizeEvent(QResizeEvent *e)
    ritual = 'ritual_ZN13QOpenGLWidget11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWidget11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QOpenGLWidget::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglwidget.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLWidget::event(QEvent *e)
    ritual = 'ritual_ZN13QOpenGLWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QOpenGLWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))
