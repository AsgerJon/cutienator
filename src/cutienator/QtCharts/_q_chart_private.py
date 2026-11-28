"""
QChartPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/qchart_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QChartPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChartPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QChartPrivate: a plain Python object standing in
  front of one C++ QChartPrivate.

  C++ hands a QChartPrivate around as a copy, so every C++ QChartPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QChartPrivate that has a ritual and that Python can
  call so far, 6 names in all: 'init', 'zoomIn', 'zoomOut', 'zoomReset',
  'isZoomed', 'scroll'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QChartPrivate::~QChartPrivate()': the destructor: Python removes
    its C++ QChartPrivate by it, and has no other use for it.
  - Qt's 'QPen &QChartPrivate::defaultPen()': gives a type Python has no way
    to take yet.
  - Qt's 'QBrush &QChartPrivate::defaultBrush()': gives a type Python has no
    way to take yet.
  - Qt's 'QFont &QChartPrivate::defaultFont()': gives a type Python has no
    way to take yet.

  What to expect
  --------------

  - The C++ QChartPrivate is created at the first use, not by
    'QChartPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QChartPrivate back gives a copy the ritual made for
    Python, in a new cute QChartPrivate.
  - Each name of Qt's QChartPrivate that has no cute function yet,
    'defaultBrush', 'defaultFont', 'defaultPen', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChartPrivate'

  #  Qt's '~QChartPrivate()'. Naming it makes this a value class: Python owns
  #  every C++ QChartPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QChartPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QChart, QChart.ChartType)
  @overload(NoneType, QChart.ChartType)
  def __init__(self, q: Optional[QChart], type: QChart.ChartType) -> None:
    """
    Notes what was given, for Qt's 'QChartPrivate::QChartPrivate(QChart *q,
    QChart::ChartType type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qchartprivate.html#QChartPrivate

    Parameters
    ----------

    q : Optional[QChart]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QChart.ChartType
      Passed on as its number.
    """
    #  QChartPrivate::QChartPrivate(QChart *q, QChart::ChartType type)
    self._noteCreation(QChartPrivate, lambda: Rituals.call(
        'ritual_ZN13QChartPrivateC1EP6QChartNS0_9ChartTypeE',
        self._addressOf(q), type.value,
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

  def init(self) -> None:
    """
    Calls Qt's 'void QChartPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qchartprivate.html#init
    """
    #  void QChartPrivate::init()
    self.uglySide.call('ritual_ZN13QChartPrivate4initEv')

  @overload(float)
  def zoomIn(self, factor: float) -> None:
    """
    Calls Qt's 'void QChartPrivate::zoomIn(qreal factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartprivate.html#zoomIn

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QChartPrivate::zoomIn(qreal factor)
    self.uglySide.call('ritual_ZN13QChartPrivate6zoomInEd', factor)

  @overload(QRectF)
  def zoomIn(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QChartPrivate::zoomIn(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartprivate.html#zoomIn

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QChartPrivate::zoomIn(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN13QChartPrivate6zoomInERK6QRectF', self._valueOf(rect),
    )

  @overload(float)
  def zoomOut(self, factor: float) -> None:
    """
    Calls Qt's 'void QChartPrivate::zoomOut(qreal factor)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartprivate.html#zoomOut

    Parameters
    ----------

    factor : float
      Passed on as it is.
    """
    #  void QChartPrivate::zoomOut(qreal factor)
    self.uglySide.call('ritual_ZN13QChartPrivate7zoomOutEd', factor)

  def zoomReset(self) -> None:
    """
    Calls Qt's 'void QChartPrivate::zoomReset()'.

    Qt's own words: https://doc.qt.io/qt-6/qchartprivate.html#zoomReset
    """
    #  void QChartPrivate::zoomReset()
    self.uglySide.call('ritual_ZN13QChartPrivate9zoomResetEv')

  def isZoomed(self) -> bool:
    """
    Calls Qt's 'bool QChartPrivate::isZoomed()'.

    Qt's own words: https://doc.qt.io/qt-6/qchartprivate.html#isZoomed
    """
    #  bool QChartPrivate::isZoomed()
    return self.uglySide.call('ritual_ZN13QChartPrivate8isZoomedEv')

  @overload(float, float)
  def scroll(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QChartPrivate::scroll(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qchartprivate.html#scroll

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QChartPrivate::scroll(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN13QChartPrivate6scrollEdd', dx, dy)

  @staticmethod
  def defaultBrush(*__, **_) -> Never:
    """
    Qt's 'QBrush &QChartPrivate::defaultBrush()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QChartPrivate.defaultBrush' has no cute function yet. Qt's "
        "'QBrush &QChartPrivate::defaultBrush()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def defaultFont(*__, **_) -> Never:
    """
    Qt's 'QFont &QChartPrivate::defaultFont()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QChartPrivate.defaultFont' has no cute function yet. Qt's 'QFont "
        "&QChartPrivate::defaultFont()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def defaultPen(*__, **_) -> Never:
    """
    Qt's 'QPen &QChartPrivate::defaultPen()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QChartPrivate.defaultPen' has no cute function yet. Qt's 'QPen "
        "&QChartPrivate::defaultPen()': gives a type Python has no way to "
        "take yet.")
