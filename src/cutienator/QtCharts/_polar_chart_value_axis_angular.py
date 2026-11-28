"""
PolarChartValueAxisAngular binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/polarchartvalueaxisangular_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means PolarChartValueAxisAngular to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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
  from . import QValueAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QValueAxis = WAIT['QtCharts:QValueAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PolarChartValueAxisAngular(PolarChartAxisAngular):
  """
  The cute side of Qt's PolarChartValueAxisAngular: a plain Python object
  standing in front of one C++ PolarChartValueAxisAngular.

  It is built on the cute 'PolarChartAxisAngular', as Qt's
  PolarChartValueAxisAngular is built on Qt's PolarChartAxisAngular, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's PolarChartValueAxisAngular that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'handleTickCountChanged', 'handleMinorTickCountChanged',
  'handleLabelFormatChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PolarChartValueAxisAngular::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int PolarChartValueAxisAngular::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'PolarChartValueAxisAngular::~PolarChartValueAxisAngular()': the
    destructor: Python never removes a C++ PolarChartValueAxisAngular.
  - Qt's 'QList<qreal> PolarChartValueAxisAngular::calculateLayout() const':
    gives a type Python has no way to take yet.
  - Qt's 'void PolarChartValueAxisAngular::createAxisLabels(const
    QList<qreal> &layout)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PolarChartValueAxisAngular is created at the first use, not by
    'PolarChartValueAxisAngular(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PolarChartValueAxisAngular.
  - Qt tells when it has removed the C++ PolarChartValueAxisAngular. Every
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
    Calls Qt's 'QString PolarChartValueAxisAngular::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartvalueaxisangular.html#tr

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
    #  QString PolarChartValueAxisAngular::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26PolarChartValueAxisAngular2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PolarChartValueAxisAngular'

  #  A C++ PolarChartValueAxisAngular Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PolarChartValueAxisAngular'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PolarChartValueAxisAngular::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartvalueaxisangular.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PolarChartValueAxisAngular::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26PolarChartValueAxisAngular10metaObjectEv',
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

  @overload(QValueAxis, QGraphicsItem)
  @overload(QValueAxis, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      axis: Optional[QValueAxis],
      item: Optional[QGraphicsItem],
  ) -> None:
    """
    Notes what was given, for Qt's
    'PolarChartValueAxisAngular::PolarChartValueAxisAngular(QValueAxis *axis,
    QGraphicsItem *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartvalueaxisangular.html

    Parameters
    ----------

    axis : Optional[QValueAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  PolarChartValueAxisAngular::PolarChartValueAxisAngular(QValueAxis
    #      *axis, QGraphicsItem *item)
    self._noteCreation(PolarChartValueAxisAngular, lambda: Rituals.call(
        'ritual_ZN26PolarChartValueAxisAngularC1EP10QValueAxisP13QGraphicsI'
        'tem',
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
    Calls Qt's 'void PolarChartValueAxisAngular::handleTickCountChanged(int
    tick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartvalueaxisangular.html

    Parameters
    ----------

    tick : int
      Passed on as it is.
    """
    #  void PolarChartValueAxisAngular::handleTickCountChanged(int tick)
    self.uglySide.call(
        'ritual_ZN26PolarChartValueAxisAngular22handleTickCountChangedEi',
        tick,
    )

  @overload(int)
  def handleMinorTickCountChanged(self, tick: int) -> None:
    """
    Calls Qt's 'void
    PolarChartValueAxisAngular::handleMinorTickCountChanged(int tick)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartvalueaxisangular.html

    Parameters
    ----------

    tick : int
      Passed on as it is.
    """
    #  void PolarChartValueAxisAngular::handleMinorTickCountChanged(int tick)
    self.uglySide.call(
        'ritual_ZN26PolarChartValueAxisAngular27handleMinorTickCountChanged'
        'Ei',
        tick,
    )

  @overload(str)
  def handleLabelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void
    PolarChartValueAxisAngular::handleLabelFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartvalueaxisangular.html

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void PolarChartValueAxisAngular::handleLabelFormatChanged(const
    #      QString &format)
    self.uglySide.call(
        'ritual_ZN26PolarChartValueAxisAngular24handleLabelFormatChangedERK'
        '7QString',
        format,
    )
