"""
PolarChartLogValueAxisAngular binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/polarchartlogvalueaxisangular_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means PolarChartLogValueAxisAngular to be private: it declares the
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
  from . import QLogValueAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLogValueAxis = WAIT['QtCharts:QLogValueAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PolarChartLogValueAxisAngular(PolarChartAxisAngular):
  """
  The cute side of Qt's PolarChartLogValueAxisAngular: a plain Python object
  standing in front of one C++ PolarChartLogValueAxisAngular.

  It is built on the cute 'PolarChartAxisAngular', as Qt's
  PolarChartLogValueAxisAngular is built on Qt's PolarChartAxisAngular, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's PolarChartLogValueAxisAngular that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'handleBaseChanged', 'handleLabelFormatChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PolarChartLogValueAxisAngular::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int PolarChartLogValueAxisAngular::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'PolarChartLogValueAxisAngular::~PolarChartLogValueAxisAngular()':
    the destructor: Python never removes a C++ PolarChartLogValueAxisAngular.
  - Qt's 'QList<qreal> PolarChartLogValueAxisAngular::calculateLayout()
    const': gives a type Python has no way to take yet.
  - Qt's 'void PolarChartLogValueAxisAngular::createAxisLabels(const
    QList<qreal> &layout)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PolarChartLogValueAxisAngular is created at the first use, not by
    'PolarChartLogValueAxisAngular(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PolarChartLogValueAxisAngular.
  - Qt tells when it has removed the C++ PolarChartLogValueAxisAngular. Every
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
    Calls Qt's 'QString PolarChartLogValueAxisAngular::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartlogvalueaxisangular.html#tr

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
    #  QString PolarChartLogValueAxisAngular::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29PolarChartLogValueAxisAngular2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PolarChartLogValueAxisAngular'

  #  A C++ PolarChartLogValueAxisAngular Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PolarChartLogValueAxisAngular'

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
    *PolarChartLogValueAxisAngular::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartlogvalueaxisangular.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PolarChartLogValueAxisAngular::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29PolarChartLogValueAxisAngular10metaObjectEv',
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

  @overload(QLogValueAxis, QGraphicsItem)
  @overload(QLogValueAxis, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      axis: Optional[QLogValueAxis],
      item: Optional[QGraphicsItem],
  ) -> None:
    """
    Notes what was given, for Qt's
    'PolarChartLogValueAxisAngular::PolarChartLogValueAxisAngular(
    QLogValueAxis *axis, QGraphicsItem *item)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartlogvalueaxisangular.html

    Parameters
    ----------

    axis : Optional[QLogValueAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  PolarChartLogValueAxisAngular::PolarChartLogValueAxisAngular(
    #      QLogValueAxis *axis, QGraphicsItem *item)
    self._noteCreation(PolarChartLogValueAxisAngular, lambda: Rituals.call(
        'ritual_ZN29PolarChartLogValueAxisAngularC1EP13QLogValueAxisP13QGra'
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

  @overload(float)
  def handleBaseChanged(self, base: float) -> None:
    """
    Calls Qt's 'void PolarChartLogValueAxisAngular::handleBaseChanged(qreal
    base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartlogvalueaxisangular.html

    Parameters
    ----------

    base : float
      Passed on as it is.
    """
    #  void PolarChartLogValueAxisAngular::handleBaseChanged(qreal base)
    self.uglySide.call(
        'ritual_ZN29PolarChartLogValueAxisAngular17handleBaseChangedEd',
        base,
    )

  @overload(str)
  def handleLabelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void
    PolarChartLogValueAxisAngular::handleLabelFormatChanged(const QString
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartlogvalueaxisangular.html

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void PolarChartLogValueAxisAngular::handleLabelFormatChanged(const
    #      QString &format)
    self.uglySide.call(
        'ritual_ZN29PolarChartLogValueAxisAngular24handleLabelFormatChanged'
        'ERK7QString',
        format,
    )
