"""
QChartView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qchartview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMouseEvent, QResizeEvent
  from . import QChart
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChart = WAIT['QChart']
  QMouseEvent = WAIT['QMouseEvent']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChartView(QGraphicsView):
  """
  The cute side of Qt's QChartView: a plain Python object standing in front
  of one C++ QChartView.

  It is built on the cute 'QGraphicsView', as Qt's QChartView is built on
  Qt's QGraphicsView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QChartView that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'rubberBand', 'chart',
  'setChart', 'resizeEvent', 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QChartView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QChartView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QChartView::~QChartView()': the destructor: Python never removes a
    C++ QChartView.
  - Qt's 'void QChartView::setRubberBand(const RubberBands &rubberBands)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QChartView is created at the first use, not by 'QChartView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QChartView.
  - Qt tells when it has removed the C++ QChartView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QChartView that has no cute function yet,
    'setRubberBand', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QChartView, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class RubberBand(CuteFlags):
    """
    The flags enum 'QChartView::RubberBand' of Qt, with the 5 names Qt gives
    in it. Qt names the type of its combinations 'QChartView::RubberBands'.
    """

    NoRubberBand = 0x0
    VerticalRubberBand = 0x1
    HorizontalRubberBand = 0x2
    RectangleRubberBand = 0x3
    ClickThroughRubberBand = 0x80

  RubberBands = RubberBand

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
    Calls Qt's 'QString QChartView::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#tr

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
    #  QString QChartView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QChartView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChartView'

  #  A C++ QChartView Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QChartView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QChartView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QChartView::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QChartView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rubberBand(self) -> RubberBands:
    """
    Calls Qt's 'RubberBands QChartView::rubberBand() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#rubberBand

    Returns
    -------

    RubberBands
      The value standing for the combination Qt gave back.
    """
    #  RubberBands QChartView::rubberBand() const
    return QChartView.RubberBands(self.uglySide.call(
        'ritual_ZNK10QChartView10rubberBandEv',
    ))

  def chart(self) -> Optional[QChart]:
    """
    Calls Qt's 'QChart *QChartView::chart() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#chart

    Returns
    -------

    Optional[QChart]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChart *QChartView::chart() const
    address = self.uglySide.call('ritual_ZNK10QChartView5chartEv')
    from . import QChart
    return QChart._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QChart)
  @overload(NoneType)
  def setChart(self, chart: Optional[QChart]) -> None:
    """
    Calls Qt's 'void QChartView::setChart(QChart *chart)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#setChart

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChartView::setChart(QChart *chart)
    self.uglySide.call(
        'ritual_ZN10QChartView8setChartEP6QChart', self._addressOf(chart),
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
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QChartView::QChartView(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#QChartView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QChartView::QChartView(QWidget *parent)
    self._noteCreation(QChartView, lambda: Rituals.call(
        'ritual_ZN10QChartViewC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QChart)
  @overload(QChart, QWidget)
  @overload(QChart, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      chart: Optional[QChart],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QChartView::QChartView(QChart *chart,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#QChartView

    Parameters
    ----------

    chart : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QChartView::QChartView(QChart *chart, QWidget *parent)
    self._noteCreation(QChartView, lambda: Rituals.call(
        'ritual_ZN10QChartViewC1EP6QChartP7QWidget',
        self._addressOf(chart), self._addressOf(parent),
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

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QChartView::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChartView::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN10QChartView11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QChartView11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QChartView::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChartView::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QChartView15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QChartView15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QChartView::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChartView::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QChartView14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QChartView14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QChartView::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartview.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChartView::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QChartView17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QChartView17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def setRubberBand(*__, **_) -> Never:
    """
    Qt's 'void QChartView::setRubberBand(const RubberBands &rubberBands)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QChartView.setRubberBand' has no cute function yet. Qt's 'void "
        "QChartView::setRubberBand(const RubberBands &rubberBands)': takes "
        "a type Python has no way to hand over yet.")
