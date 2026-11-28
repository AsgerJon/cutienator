"""
QPaintDeviceWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpaintdevicewindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QPaintDevice, QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QRect
  from . import QExposeEvent, QPaintDeviceWindowPrivate, QPaintEngine
  from . import QPaintEvent, QRegion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QExposeEvent = WAIT['QExposeEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPaintDeviceWindow(QWindow, QPaintDevice):
  """
  The cute side of Qt's QPaintDeviceWindow: a plain Python object standing in
  front of one C++ QPaintDeviceWindow.

  It is built on the cute 'QWindow', as Qt's QPaintDeviceWindow is built on
  Qt's QWindow, and has everything that class has. It is built on the cute
  'QPaintDevice' as well, as Qt's QPaintDeviceWindow is built on Qt's
  QPaintDevice too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPaintDeviceWindow that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'd_func', 'update',
  'exposeEvent', 'paintEvent', 'metric', 'event', 'paintEngine'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPaintDeviceWindow::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPaintDeviceWindow::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QPaintDeviceWindowPrivate *QPaintDeviceWindow::d_func()
    const': takes in Python what 'QPaintDeviceWindowPrivate
    *QPaintDeviceWindow::d_func()' takes.
  - Qt's 'QPaintDeviceWindow::QPaintDeviceWindow(QPaintDeviceWindowPrivate
    &dd, QWindow *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPaintDeviceWindow is created at the first use, not by
    'QPaintDeviceWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPaintDeviceWindow.
  - Qt tells when it has removed the C++ QPaintDeviceWindow. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPaintDeviceWindow that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QPaintDeviceWindow::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#tr

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
    #  QString QPaintDeviceWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QPaintDeviceWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintDeviceWindow'

  #  Qt's QPaintDeviceWindow is built on more than one class. The part of a
  #  C++ QPaintDeviceWindow that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QPaintDevice': 'ritual_cast_QPaintDeviceWindow_QPaintDevice',
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
    Calls Qt's 'const QMetaObject *QPaintDeviceWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPaintDeviceWindow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QPaintDeviceWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QPaintDeviceWindow::metric(PaintDeviceMetric metric)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QPaintDeviceWindow::metric(PaintDeviceMetric metric) const
    ritual = (
        'ritual_ZNK18QPaintDeviceWindow6metricEN12QPaintDevice17PaintDevice'
        'MetricE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QPaintDeviceWindow6metricEN12QPaintDevice17Paint'
          'DeviceMetricE')
    return self.uglySide.call(ritual, metric.value)

  def paintEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPaintDeviceWindow::paintEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindow.html#paintEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPaintDeviceWindow::paintEngine() const
    ritual = 'ritual_ZNK18QPaintDeviceWindow11paintEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QPaintDeviceWindow11paintEngineEv'
    address = self.uglySide.call(ritual)
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

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
    Qt's 'QPaintDeviceWindow::QPaintDeviceWindow(QPaintDeviceWindowPrivate
    &dd, QWindow *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPaintDeviceWindow.__init__' has no cute function yet. Qt's "
        "'QPaintDeviceWindow::QPaintDeviceWindow(QPaintDeviceWindowPrivate "
        "&dd, QWindow *parent)': takes a type Python has no way to hand "
        "over yet.")

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

  def d_func(self) -> Optional[QPaintDeviceWindowPrivate]:
    """
    Calls Qt's 'QPaintDeviceWindowPrivate *QPaintDeviceWindow::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#d_func

    Returns
    -------

    Optional[QPaintDeviceWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDeviceWindowPrivate *QPaintDeviceWindow::d_func()
    address = self.uglySide.call('ritual_ZN18QPaintDeviceWindow6d_funcEv')
    from . import QPaintDeviceWindowPrivate
    return QPaintDeviceWindowPrivate._cuteAt(address)

  @overload(QRect)
  def update(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindow::update(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#update

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPaintDeviceWindow::update(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN18QPaintDeviceWindow6updateERK5QRect', self._valueOf(rect),
    )

  @overload(QRegion)
  def update(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindow::update(const QRegion &region)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#update

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPaintDeviceWindow::update(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN18QPaintDeviceWindow6updateERK7QRegion',
        self._valueOf(region),
    )

  @overload()
  def update(self) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindow::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#update
    """
    #  void QPaintDeviceWindow::update()
    self.uglySide.call('ritual_ZN18QPaintDeviceWindow6updateEv')

  @overload(QExposeEvent)
  @overload(NoneType)
  def exposeEvent(self, a0: Optional[QExposeEvent]) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindow::exposeEvent(QExposeEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintdevicewindow.html#exposeEvent

    Parameters
    ----------

    a0 : Optional[QExposeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPaintDeviceWindow::exposeEvent(QExposeEvent *a0)
    ritual = 'ritual_ZN18QPaintDeviceWindow11exposeEventEP12QExposeEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QPaintDeviceWindow11exposeEventEP12QExposeEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QPaintDeviceWindow::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPaintDeviceWindow::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN18QPaintDeviceWindow10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPaintDeviceWindow10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QPaintDeviceWindow::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintdevicewindow.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPaintDeviceWindow::event(QEvent *event)
    ritual = 'ritual_ZN18QPaintDeviceWindow5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPaintDeviceWindow5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))
