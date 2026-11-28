"""
GLWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/glwidget_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means GLWidget to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QOpenGLFunctions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMouseEvent
  from . import QXYSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QXYSeries = WAIT['QtCharts:QXYSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GLWidget(QOpenGLFunctions):
  """
  The cute side of Qt's GLWidget: a plain Python object standing in front of
  one C++ GLWidget.

  What exists
  -----------

  Every function of Qt's GLWidget that has a ritual and that Python can call
  so far, 15 names in all: 'metaObject', 'needsReset', 'cleanup',
  'cleanXYSeriesResources', 'initializeGL', 'paintGL', 'resizeGL',
  'mouseDoubleClickEvent', 'mouseMoveEvent', 'mousePressEvent',
  'mouseReleaseEvent', 'findSeriesAtEvent', 'render', 'recreateSelectionFbo',
  'chartSeries'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *GLWidget::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int GLWidget::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'GLWidget::~GLWidget()': the destructor: Python never removes a C++
    GLWidget.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 leans on 'GLWidget.

  What to expect
  --------------

  - The C++ GLWidget is created at the first use, not by 'GLWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ GLWidget.
  - Qt tells when it has removed the C++ GLWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's GLWidget that has no cute function yet, '__init__',
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
  __qt_class__ = 'GLWidget'

  #  Qt's GLWidget is built on more than one class. The part of a C++
  #  GLWidget that belongs to a class after the first begins somewhere inside
  #  the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QOpenGLFunctions': 'ritual_cast_GLWidget_QOpenGLFunctions',
  }

  #  A C++ GLWidget Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_GLWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *GLWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *GLWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK8GLWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def needsReset(self) -> bool:
    """
    Calls Qt's 'bool GLWidget::needsReset() const'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#needsReset
    """
    #  bool GLWidget::needsReset() const
    return self.uglySide.call('ritual_ZNK8GLWidget10needsResetEv')

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
    Qt's 'GLWidget::GLWidget(GLXYSeriesDataManager *xyDataManager, QChart
    *chart, QGraphicsView *parent)': leans on
    'GLWidget::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'GLWidget.__init__' has no cute function yet. Qt's "
        "'GLWidget::GLWidget(GLXYSeriesDataManager *xyDataManager, QChart "
        "*chart, QGraphicsView *parent)': leans on "
        "'GLWidget::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void GLWidget::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#cleanup
    """
    #  void GLWidget::cleanup()
    self.uglySide.call('ritual_ZN8GLWidget7cleanupEv')

  @overload(QXYSeries)
  @overload(NoneType)
  def cleanXYSeriesResources(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void GLWidget::cleanXYSeriesResources(const QXYSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/glwidget.html#cleanXYSeriesResources

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void GLWidget::cleanXYSeriesResources(const QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN8GLWidget22cleanXYSeriesResourcesEPK9QXYSeries',
        self._addressOf(series),
    )

  def initializeGL(self) -> None:
    """
    Calls Qt's 'void GLWidget::initializeGL()'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#initializeGL
    """
    #  void GLWidget::initializeGL()
    self.uglySide.call('ritual_ZN8GLWidget12initializeGLEv')

  def paintGL(self) -> None:
    """
    Calls Qt's 'void GLWidget::paintGL()'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#paintGL
    """
    #  void GLWidget::paintGL()
    ritual = 'ritual_ZN8GLWidget7paintGLEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8GLWidget7paintGLEv'
    self.uglySide.call(ritual)

  @overload(int, int)
  def resizeGL(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void GLWidget::resizeGL(int width, int height)'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#resizeGL

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void GLWidget::resizeGL(int width, int height)
    ritual = 'ritual_ZN8GLWidget8resizeGLEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8GLWidget8resizeGLEii'
    self.uglySide.call(ritual, width, height)

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void GLWidget::mouseDoubleClickEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/glwidget.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void GLWidget::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = 'ritual_ZN8GLWidget21mouseDoubleClickEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8GLWidget21mouseDoubleClickEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void GLWidget::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void GLWidget::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN8GLWidget14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8GLWidget14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void GLWidget::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void GLWidget::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN8GLWidget15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8GLWidget15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void GLWidget::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void GLWidget::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN8GLWidget17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8GLWidget17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def findSeriesAtEvent(
      self,
      event: Optional[QMouseEvent],
  ) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *GLWidget::findSeriesAtEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#findSeriesAtEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *GLWidget::findSeriesAtEvent(QMouseEvent *event)
    address = self.uglySide.call(
        'ritual_ZN8GLWidget17findSeriesAtEventEP11QMouseEvent',
        self._addressOf(event),
    )
    from . import QXYSeries
    return QXYSeries._cuteAt(address)

  @overload(bool)
  def render(self, selection: bool) -> None:
    """
    Calls Qt's 'void GLWidget::render(bool selection)'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#render

    Parameters
    ----------

    selection : bool
      Passed on as it is.
    """
    #  void GLWidget::render(bool selection)
    self.uglySide.call('ritual_ZN8GLWidget6renderEb', selection)

  def recreateSelectionFbo(self) -> None:
    """
    Calls Qt's 'void GLWidget::recreateSelectionFbo()'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#recreateSelectionFbo
    """
    #  void GLWidget::recreateSelectionFbo()
    self.uglySide.call('ritual_ZN8GLWidget20recreateSelectionFboEv')

  @overload(QXYSeries)
  @overload(NoneType)
  def chartSeries(self, cSeries: Optional[QXYSeries]) -> Optional[QXYSeries]:
    """
    Calls Qt's 'QXYSeries *GLWidget::chartSeries(const QXYSeries *cSeries)'.

    Qt's own words: https://doc.qt.io/qt-6/glwidget.html#chartSeries

    Parameters
    ----------

    cSeries : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXYSeries *GLWidget::chartSeries(const QXYSeries *cSeries)
    address = self.uglySide.call(
        'ritual_ZN8GLWidget11chartSeriesEPK9QXYSeries',
        self._addressOf(cSeries),
    )
    from . import QXYSeries
    return QXYSeries._cuteAt(address)
