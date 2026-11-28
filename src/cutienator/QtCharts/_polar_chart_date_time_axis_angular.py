"""
PolarChartDateTimeAxisAngular binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/polarchartdatetimeaxisangular_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means PolarChartDateTimeAxisAngular to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem
from . import PolarChartAxisAngular

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDateTimeAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTimeAxis = WAIT['QtCharts:QDateTimeAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PolarChartDateTimeAxisAngular(PolarChartAxisAngular):
  """
  The cute side of Qt's PolarChartDateTimeAxisAngular: a plain Python object
  standing in front of one C++ PolarChartDateTimeAxisAngular.

  It is built on the cute 'PolarChartAxisAngular', as Qt's
  PolarChartDateTimeAxisAngular is built on Qt's PolarChartAxisAngular, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's PolarChartDateTimeAxisAngular that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'handleTickCountChanged', 'handleFormatChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PolarChartDateTimeAxisAngular::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int PolarChartDateTimeAxisAngular::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'PolarChartDateTimeAxisAngular::~PolarChartDateTimeAxisAngular()':
    the destructor: Python never removes a C++ PolarChartDateTimeAxisAngular.
  - Qt's 'QList<qreal> PolarChartDateTimeAxisAngular::calculateLayout()
    const': gives a type Python has no way to take yet.
  - Qt's 'void PolarChartDateTimeAxisAngular::createAxisLabels(const
    QList<qreal> &layout)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PolarChartDateTimeAxisAngular is created at the first use, not by
    'PolarChartDateTimeAxisAngular(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PolarChartDateTimeAxisAngular.
  - Qt tells when it has removed the C++ PolarChartDateTimeAxisAngular. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString PolarChartDateTimeAxisAngular::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartdatetimeaxisangular.html#tr

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
    #  QString PolarChartDateTimeAxisAngular::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29PolarChartDateTimeAxisAngular2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PolarChartDateTimeAxisAngular'

  #  A C++ PolarChartDateTimeAxisAngular Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PolarChartDateTimeAxisAngular'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *PolarChartDateTimeAxisAngular::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartdatetimeaxisangular.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PolarChartDateTimeAxisAngular::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29PolarChartDateTimeAxisAngular10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QDateTimeAxis, QGraphicsItem)
  @overload(QDateTimeAxis, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      axis: Optional[QDateTimeAxis],
      item: Optional[QGraphicsItem],
  ) -> None:
    """
    Notes what was given, for Qt's
    'PolarChartDateTimeAxisAngular::PolarChartDateTimeAxisAngular(
    QDateTimeAxis *axis, QGraphicsItem *item)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartdatetimeaxisangular.html

    Parameters
    ----------

    axis : Optional[QDateTimeAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  PolarChartDateTimeAxisAngular::PolarChartDateTimeAxisAngular(
    #      QDateTimeAxis *axis, QGraphicsItem *item)
    self._noteCreation(PolarChartDateTimeAxisAngular, lambda: Rituals.call(
        'ritual_ZN29PolarChartDateTimeAxisAngularC1EP13QDateTimeAxisP13QGra'
        'phicsItem',
        self._addressOf(axis), self._addressOf(item, 'QGraphicsItem'),
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

  @overload(int)
  def handleTickCountChanged(self, tick: int) -> None:
    """
    Calls Qt's 'void
    PolarChartDateTimeAxisAngular::handleTickCountChanged(int tick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartdatetimeaxisangular.html

    Parameters
    ----------

    tick : int
      Passed on as it is.
    """
    #  void PolarChartDateTimeAxisAngular::handleTickCountChanged(int tick)
    self.uglySide.call(
        'ritual_ZN29PolarChartDateTimeAxisAngular22handleTickCountChangedEi',
        tick,
    )

  @overload(str)
  def handleFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void PolarChartDateTimeAxisAngular::handleFormatChanged(const
    QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartdatetimeaxisangular.html

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void PolarChartDateTimeAxisAngular::handleFormatChanged(const QString
    #      &format)
    self.uglySide.call(
        'ritual_ZN29PolarChartDateTimeAxisAngular19handleFormatChangedERK7Q'
        'String',
        format,
    )
