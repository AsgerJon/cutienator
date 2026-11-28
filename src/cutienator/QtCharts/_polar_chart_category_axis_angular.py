"""
PolarChartCategoryAxisAngular binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/polarchartcategoryaxisangular_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means PolarChartCategoryAxisAngular to be private: it declares the
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
  from . import QCategoryAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCategoryAxis = WAIT['QCategoryAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PolarChartCategoryAxisAngular(PolarChartAxisAngular):
  """
  The cute side of Qt's PolarChartCategoryAxisAngular: a plain Python object
  standing in front of one C++ PolarChartCategoryAxisAngular.

  It is built on the cute 'PolarChartAxisAngular', as Qt's
  PolarChartCategoryAxisAngular is built on Qt's PolarChartAxisAngular, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's PolarChartCategoryAxisAngular that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'handleCategoriesChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PolarChartCategoryAxisAngular::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int PolarChartCategoryAxisAngular::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'PolarChartCategoryAxisAngular::~PolarChartCategoryAxisAngular()':
    the destructor: Python never removes a C++ PolarChartCategoryAxisAngular.
  - Qt's 'QList<qreal> PolarChartCategoryAxisAngular::calculateLayout()
    const': gives a type Python has no way to take yet.
  - Qt's 'void PolarChartCategoryAxisAngular::createAxisLabels(const
    QList<qreal> &layout)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ PolarChartCategoryAxisAngular is created at the first use, not by
    'PolarChartCategoryAxisAngular(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PolarChartCategoryAxisAngular.
  - Qt tells when it has removed the C++ PolarChartCategoryAxisAngular. Every
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
    Calls Qt's 'QString PolarChartCategoryAxisAngular::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartcategoryaxisangular.html#tr

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
    #  QString PolarChartCategoryAxisAngular::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29PolarChartCategoryAxisAngular2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PolarChartCategoryAxisAngular'

  #  A C++ PolarChartCategoryAxisAngular Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PolarChartCategoryAxisAngular'

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
    *PolarChartCategoryAxisAngular::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartcategoryaxisangular.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PolarChartCategoryAxisAngular::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29PolarChartCategoryAxisAngular10metaObjectEv',
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

  @overload(QCategoryAxis, QGraphicsItem)
  @overload(QCategoryAxis, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      axis: Optional[QCategoryAxis],
      item: Optional[QGraphicsItem],
  ) -> None:
    """
    Notes what was given, for Qt's
    'PolarChartCategoryAxisAngular::PolarChartCategoryAxisAngular(
    QCategoryAxis *axis, QGraphicsItem *item)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartcategoryaxisangular.html

    Parameters
    ----------

    axis : Optional[QCategoryAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  PolarChartCategoryAxisAngular::PolarChartCategoryAxisAngular(
    #      QCategoryAxis *axis, QGraphicsItem *item)
    self._noteCreation(PolarChartCategoryAxisAngular, lambda: Rituals.call(
        'ritual_ZN29PolarChartCategoryAxisAngularC1EP13QCategoryAxisP13QGra'
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

  def handleCategoriesChanged(self) -> None:
    """
    Calls Qt's 'void
    PolarChartCategoryAxisAngular::handleCategoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartcategoryaxisangular.html
    """
    #  void PolarChartCategoryAxisAngular::handleCategoriesChanged()
    self.uglySide.call(
        'ritual_ZN29PolarChartCategoryAxisAngular23handleCategoriesChangedE'
        'v',
    )
