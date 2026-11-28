"""
QPolarChart binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/qpolarchart.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from ..QtWidgets import QGraphicsItem
from . import QChart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAbstractAxis, QAbstractSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAxis = WAIT['QtCharts:QAbstractAxis']
  QAbstractSeries = WAIT['QtCharts:QAbstractSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPolarChart(QChart):
  """
  The cute side of Qt's QPolarChart: a plain Python object standing in front
  of one C++ QPolarChart.

  It is built on the cute 'QChart', as Qt's QPolarChart is built on Qt's
  QChart, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPolarChart that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'addAxis', 'axes',
  'axisPolarOrientation'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPolarChart::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPolarChart::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPolarChart::~QPolarChart()': the destructor: Python never removes
    a C++ QPolarChart.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QPolarChart is created at the first use, not by
    'QPolarChart(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPolarChart.
  - Qt tells when it has removed the C++ QPolarChart. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QPolarChart, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PolarOrientation(CuteFlags):
    """
    The flags enum 'QPolarChart::PolarOrientation' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QPolarChart::PolarOrientations'.
    """

    PolarOrientationRadial = 0x1
    PolarOrientationAngular = 0x2

  PolarOrientations = PolarOrientation

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
    Calls Qt's 'QString QPolarChart::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolarchart.html#tr

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
    #  QString QPolarChart::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QPolarChart2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QAbstractAxis)
  @overload(NoneType)
  def axisPolarOrientation(
      axis: Optional[QAbstractAxis],
  ) -> PolarOrientation:
    """
    Calls Qt's 'PolarOrientation
    QPolarChart::axisPolarOrientation(QAbstractAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpolarchart.html#axisPolarOrientation

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    PolarOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PolarOrientation(number)'
      gives.
    """
    #  PolarOrientation QPolarChart::axisPolarOrientation(QAbstractAxis
    #      *axis)
    return QPolarChart.PolarOrientation(Rituals.call(
        'ritual_ZN11QPolarChart20axisPolarOrientationEP13QAbstractAxis',
        CuteMixin._addressOf(axis),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPolarChart'

  #  A C++ QPolarChart Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPolarChart'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPolarChart::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolarchart.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPolarChart::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QPolarChart10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(PolarOrientations)
  @overload(PolarOrientations, QAbstractSeries)
  @overload(PolarOrientations, NoneType)
  def axes(
      self,
      polarOrientation: PolarOrientations = (
          PolarOrientations.PolarOrientationRadial |
          PolarOrientations.PolarOrientationAngular),
      series: Optional[QAbstractSeries] = None,
  ) -> QList[QAbstractAxis]:
    """
    Calls Qt's 'QList<QAbstractAxis *> QPolarChart::axes(PolarOrientations
    polarOrientation, QAbstractSeries *series) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpolarchart.html#axes

    Parameters
    ----------

    polarOrientation : PolarOrientations
      Passed on as its number. May be left out, as in Qt: it is then
      PolarOrientations.PolarOrientationRadial |
      PolarOrientations.PolarOrientationAngular.

    series : Optional[QAbstractSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QList[QAbstractAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractAxis *> QPolarChart::axes(PolarOrientations
    #      polarOrientation, QAbstractSeries *series) const
    address = self.uglySide.call(
        'ritual_ZNK11QPolarChart4axesE6QFlagsINS_16PolarOrientationEEP15QAb'
        'stractSeries',
        polarOrientation.value, self._addressOf(series),
    )
    from . import QAbstractAxis
    return QList[QAbstractAxis]._cuteOwning(address)

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
  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QGraphicsItem] = None,
      wFlags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QPolarChart::QPolarChart(QGraphicsItem
    *parent, Qt::WindowFlags wFlags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpolarchart.html#QPolarChart

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    wFlags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QPolarChart::QPolarChart(QGraphicsItem *parent, Qt::WindowFlags
    #      wFlags)
    self._noteCreation(QPolarChart, lambda: Rituals.call(
        'ritual_ZN11QPolarChartC1EP13QGraphicsItem6QFlagsIN2Qt10WindowTypeE'
        'E',
        self._addressOf(parent, 'QGraphicsItem'), wFlags.value,
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

  @overload(QAbstractAxis, PolarOrientation)
  @overload(NoneType, PolarOrientation)
  def addAxis(
      self,
      axis: Optional[QAbstractAxis],
      polarOrientation: PolarOrientation,
  ) -> None:
    """
    Calls Qt's 'void QPolarChart::addAxis(QAbstractAxis *axis,
    PolarOrientation polarOrientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qpolarchart.html#addAxis

    Parameters
    ----------

    axis : Optional[QAbstractAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    polarOrientation : PolarOrientation
      Passed on as its number.
    """
    #  void QPolarChart::addAxis(QAbstractAxis *axis, PolarOrientation
    #      polarOrientation)
    self.uglySide.call(
        'ritual_ZN11QPolarChart7addAxisEP13QAbstractAxisNS_16PolarOrientati'
        'onE',
        self._addressOf(axis), polarOrientation.value,
    )
