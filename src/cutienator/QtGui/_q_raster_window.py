"""
QRasterWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qrasterwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QPaintDevice, QPaintDeviceWindow, QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from . import QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRasterWindow(QPaintDeviceWindow):
  """
  The cute side of Qt's QRasterWindow: a plain Python object standing in
  front of one C++ QRasterWindow.

  It is built on the cute 'QPaintDeviceWindow', as Qt's QRasterWindow is
  built on Qt's QPaintDeviceWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRasterWindow that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'metric', 'redirected',
  'resizeEvent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRasterWindow::~QRasterWindow()': the destructor: Python never
    removes a C++ QRasterWindow.

  What has no ritual
  ------------------

  8 of the 15 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QRasterWindow is created at the first use, not by
    'QRasterWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRasterWindow.
  - Qt tells when it has removed the C++ QRasterWindow. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QRasterWindow::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterwindow.html#tr

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
    #  QString QRasterWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QRasterWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRasterWindow'

  #  A C++ QRasterWindow Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRasterWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRasterWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRasterWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QRasterWindow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPaintDevice.PaintDeviceMetric)
  def metric(self, metric: QPaintDevice.PaintDeviceMetric) -> int:
    """
    Calls Qt's 'int QRasterWindow::metric(PaintDeviceMetric metric) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterwindow.html#metric

    Parameters
    ----------

    metric : QPaintDevice.PaintDeviceMetric
      Passed on as its number.
    """
    #  int QRasterWindow::metric(PaintDeviceMetric metric) const
    return self.uglySide.call(
        'ritual_own_ZNK13QRasterWindow6metricEN12QPaintDevice17PaintDeviceM'
        'etricE',
        metric.value,
    )

  @overload(QPoint)
  @overload(NoneType)
  def redirected(self, a0: Optional[QPoint]) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QRasterWindow::redirected(QPoint *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterwindow.html#redirected

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
    #  QPaintDevice *QRasterWindow::redirected(QPoint *a0) const
    address = self.uglySide.call(
        'ritual_own_ZNK13QRasterWindow10redirectedEP6QPoint',
        self._addressOf(a0),
    )
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
  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWindow] = None) -> None:
    """
    Notes what was given, for Qt's 'QRasterWindow::QRasterWindow(QWindow
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrasterwindow.html#QRasterWindow

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRasterWindow::QRasterWindow(QWindow *parent)
    self._noteCreation(QRasterWindow, lambda: Rituals.call(
        'ritual_ZN13QRasterWindowC1EP7QWindow', self._addressOf(parent),
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
    Calls Qt's 'void QRasterWindow::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qrasterwindow.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRasterWindow::resizeEvent(QResizeEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QRasterWindow11resizeEventEP12QResizeEvent',
        self._addressOf(event),
    )
