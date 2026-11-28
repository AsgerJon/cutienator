"""
AbstractChartLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/abstractchartlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means AbstractChartLayout to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QList
from ..QtWidgets import QGraphicsLayout, QGraphicsLayoutItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMargins, QRectF, QSizeF
  from . import ChartAxisElement, ChartBackground, ChartTitle, QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ChartAxisElement = WAIT['ChartAxisElement']
  ChartBackground = WAIT['ChartBackground']
  ChartTitle = WAIT['ChartTitle']
  QLegend = WAIT['QLegend']
  QMargins = WAIT['QMargins']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AbstractChartLayout(QGraphicsLayout):
  """
  The cute side of Qt's AbstractChartLayout: a plain Python object standing
  in front of one C++ AbstractChartLayout.

  It is built on the cute 'QGraphicsLayout', as Qt's AbstractChartLayout is
  built on Qt's QGraphicsLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AbstractChartLayout that has a ritual and that
  Python can call so far, 17 names in all: 'setMargins', 'margins',
  'setGeometry', 'calculateBackgroundGeometry', 'calculateBackgroundMinimum',
  'calculateContentGeometry', 'calculateContentMinimum',
  'calculateTitleGeometry', 'calculateTitleMinimum',
  'calculateLegendGeometry', 'calculateLegendMinimum',
  'calculateAxisGeometry', 'calculateAxisMinimum', 'sizeHint', 'count',
  'itemAt', 'removeAt'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'AbstractChartLayout::~AbstractChartLayout()': the destructor:
    Python never removes a C++ AbstractChartLayout.

  What has no ritual
  ------------------

  1 of the 19 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ AbstractChartLayout is created at the first use, not by
    'AbstractChartLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AbstractChartLayout.
  - Each name of Qt's AbstractChartLayout that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AbstractChartLayout'

  #  A C++ AbstractChartLayout Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AbstractChartLayout'

  #  The functions Qt calls itself that AbstractChartLayout is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'calculateAxisGeometry': (
          'QRectF AbstractChartLayout::calculateAxisGeometry(const QRectF '
          '&, const QList<ChartAxisElement *> &, bool) const',
      ),
      'calculateAxisMinimum': (
          'QRectF AbstractChartLayout::calculateAxisMinimum(const QRectF '
          '&, const QList<ChartAxisElement *> &) const',
      ),
  }

  #  The functions Qt calls itself that AbstractChartLayout is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setMargins': (
          ('_ZN19AbstractChartLayout10setMarginsERK8QMargins',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMargins'),
           )),
      ),
      'margins': (
          ('_ZNK19AbstractChartLayout7marginsEv',
           ('address', 'value', 'QtCore:QMargins'),
           ()),
      ),
      'calculateBackgroundGeometry': (
          ('_ZNK19AbstractChartLayout27calculateBackgroundGeometryERK6QRect'
           'FP15ChartBackgroundb',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'address', 'QtCharts:ChartBackground'),
               ('bool', 'number', ''),
           )),
      ),
      'calculateBackgroundMinimum': (
          ('_ZNK19AbstractChartLayout26calculateBackgroundMinimumERK6QRectF',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'calculateContentGeometry': (
          ('_ZNK19AbstractChartLayout24calculateContentGeometryERK6QRectF',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'calculateContentMinimum': (
          ('_ZNK19AbstractChartLayout23calculateContentMinimumERK6QRectF',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'calculateTitleGeometry': (
          ('_ZNK19AbstractChartLayout22calculateTitleGeometryERK6QRectFP10C'
           'hartTitleb',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'address', 'QtCharts:ChartTitle'),
               ('bool', 'number', ''),
           )),
      ),
      'calculateTitleMinimum': (
          ('_ZNK19AbstractChartLayout21calculateTitleMinimumERK6QRectFP10Ch'
           'artTitle',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'address', 'QtCharts:ChartTitle'),
           )),
      ),
      'calculateLegendGeometry': (
          ('_ZNK19AbstractChartLayout23calculateLegendGeometryERK6QRectFP7Q'
           'Legendb',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'address', 'QtCharts:QLegend'),
               ('bool', 'number', ''),
           )),
      ),
      'calculateLegendMinimum': (
          ('_ZNK19AbstractChartLayout22calculateLegendMinimumERK6QRectFP7QL'
           'egend',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'address', 'QtCharts:QLegend'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def margins(self) -> QMargins:
    """
    Calls Qt's 'QMargins AbstractChartLayout::margins() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractchartlayout.html#margins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins AbstractChartLayout::margins() const
    ritual = 'ritual_ZNK19AbstractChartLayout7marginsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19AbstractChartLayout7marginsEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  @overload(QRectF, ChartBackground)
  @overload(QRectF, NoneType)
  @overload(QRectF, ChartBackground, bool)
  @overload(QRectF, NoneType, bool)
  def calculateBackgroundGeometry(
      self,
      geometry: QRectF,
      background: Optional[ChartBackground],
      update: bool = True,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateBackgroundGeometry(const
    QRectF &geometry, ChartBackground *background, bool update) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html

    Parameters
    ----------

    geometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    background : Optional[ChartBackground]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateBackgroundGeometry(const QRectF
    #      &geometry, ChartBackground *background, bool update) const
    ritual = (
        'ritual_ZNK19AbstractChartLayout27calculateBackgroundGeometryERK6QR'
        'ectFP15ChartBackgroundb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout27calculateBackgroundGeometry'
          'ERK6QRectFP15ChartBackgroundb')
    address = self.uglySide.call(
        ritual, self._valueOf(geometry), self._addressOf(background), update,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def calculateBackgroundMinimum(self, minimum: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateBackgroundMinimum(const
    QRectF &minimum) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html

    Parameters
    ----------

    minimum : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateBackgroundMinimum(const QRectF
    #      &minimum) const
    ritual = (
        'ritual_ZNK19AbstractChartLayout26calculateBackgroundMinimumERK6QRe'
        'ctF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout26calculateBackgroundMinimumE'
          'RK6QRectF')
    address = self.uglySide.call(ritual, self._valueOf(minimum))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def calculateContentGeometry(self, geometry: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateContentGeometry(const
    QRectF &geometry) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#calculateContentGeometry

    Parameters
    ----------

    geometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateContentGeometry(const QRectF
    #      &geometry) const
    ritual = (
        'ritual_ZNK19AbstractChartLayout24calculateContentGeometryERK6QRect'
        'F')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout24calculateContentGeometryERK'
          '6QRectF')
    address = self.uglySide.call(ritual, self._valueOf(geometry))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def calculateContentMinimum(self, minimum: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateContentMinimum(const
    QRectF &minimum) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#calculateContentMinimum

    Parameters
    ----------

    minimum : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateContentMinimum(const QRectF
    #      &minimum) const
    ritual = (
        'ritual_ZNK19AbstractChartLayout23calculateContentMinimumERK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout23calculateContentMinimumERK6'
          'QRectF')
    address = self.uglySide.call(ritual, self._valueOf(minimum))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF, ChartTitle)
  @overload(QRectF, NoneType)
  @overload(QRectF, ChartTitle, bool)
  @overload(QRectF, NoneType, bool)
  def calculateTitleGeometry(
      self,
      geometry: QRectF,
      title: Optional[ChartTitle],
      update: bool = True,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateTitleGeometry(const
    QRectF &geometry, ChartTitle *title, bool update) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#calculateTitleGeometry

    Parameters
    ----------

    geometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    title : Optional[ChartTitle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateTitleGeometry(const QRectF
    #      &geometry, ChartTitle *title, bool update) const
    ritual = (
        'ritual_ZNK19AbstractChartLayout22calculateTitleGeometryERK6QRectFP'
        '10ChartTitleb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout22calculateTitleGeometryERK6Q'
          'RectFP10ChartTitleb')
    address = self.uglySide.call(
        ritual, self._valueOf(geometry), self._addressOf(title), update,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF, ChartTitle)
  @overload(QRectF, NoneType)
  def calculateTitleMinimum(
      self,
      minimum: QRectF,
      title: Optional[ChartTitle],
  ) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateTitleMinimum(const
    QRectF &minimum, ChartTitle *title) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#calculateTitleMinimum

    Parameters
    ----------

    minimum : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    title : Optional[ChartTitle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateTitleMinimum(const QRectF
    #      &minimum, ChartTitle *title) const
    ritual = (
        'ritual_ZNK19AbstractChartLayout21calculateTitleMinimumERK6QRectFP1'
        '0ChartTitle')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout21calculateTitleMinimumERK6QR'
          'ectFP10ChartTitle')
    address = self.uglySide.call(
        ritual, self._valueOf(minimum), self._addressOf(title),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF, QLegend)
  @overload(QRectF, NoneType)
  @overload(QRectF, QLegend, bool)
  @overload(QRectF, NoneType, bool)
  def calculateLegendGeometry(
      self,
      geometry: QRectF,
      legend: Optional[QLegend],
      update: bool = True,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateLegendGeometry(const
    QRectF &geometry, QLegend *legend, bool update) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#calculateLegendGeometry

    Parameters
    ----------

    geometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateLegendGeometry(const QRectF
    #      &geometry, QLegend *legend, bool update) const
    ritual = (
        'ritual_ZNK19AbstractChartLayout23calculateLegendGeometryERK6QRectF'
        'P7QLegendb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout23calculateLegendGeometryERK6'
          'QRectFP7QLegendb')
    address = self.uglySide.call(
        ritual, self._valueOf(geometry), self._addressOf(legend), update,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF, QLegend)
  @overload(QRectF, NoneType)
  def calculateLegendMinimum(
      self,
      minimum: QRectF,
      legend: Optional[QLegend],
  ) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateLegendMinimum(const
    QRectF &minimum, QLegend *legend) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#calculateLegendMinimum

    Parameters
    ----------

    minimum : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateLegendMinimum(const QRectF
    #      &minimum, QLegend *legend) const
    ritual = (
        'ritual_ZNK19AbstractChartLayout22calculateLegendMinimumERK6QRectFP'
        '7QLegend')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout22calculateLegendMinimumERK6Q'
          'RectFP7QLegend')
    address = self.uglySide.call(
        ritual, self._valueOf(minimum), self._addressOf(legend),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF, QList[ChartAxisElement])
  @overload(QRectF, QList[ChartAxisElement], bool)
  def calculateAxisGeometry(
      self,
      geometry: QRectF,
      axes: QList[ChartAxisElement],
      update: bool = True,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateAxisGeometry(const
    QRectF &geometry, const QList<ChartAxisElement *> &axes, bool update)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#calculateAxisGeometry

    Parameters
    ----------

    geometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    axes : QList[ChartAxisElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateAxisGeometry(const QRectF
    #      &geometry, const QList<ChartAxisElement *> &axes, bool update)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19AbstractChartLayout21calculateAxisGeometryERK6QRectFRK'
        '5QListIP16ChartAxisElementEb',
        self._valueOf(geometry), self._valueOf(axes), update,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF, QList[ChartAxisElement])
  def calculateAxisMinimum(
      self,
      minimum: QRectF,
      axes: QList[ChartAxisElement],
  ) -> QRectF:
    """
    Calls Qt's 'QRectF AbstractChartLayout::calculateAxisMinimum(const QRectF
    &minimum, const QList<ChartAxisElement *> &axes) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#calculateAxisMinimum

    Parameters
    ----------

    minimum : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    axes : QList[ChartAxisElement]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF AbstractChartLayout::calculateAxisMinimum(const QRectF
    #      &minimum, const QList<ChartAxisElement *> &axes) const
    address = self.uglySide.call(
        'ritual_ZNK19AbstractChartLayout20calculateAxisMinimumERK6QRectFRK5'
        'QListIP16ChartAxisElementE',
        self._valueOf(minimum), self._valueOf(axes),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF AbstractChartLayout::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractchartlayout.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF()' is then passed on.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF AbstractChartLayout::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    ritual = (
        'ritual_ZNK19AbstractChartLayout8sizeHintEN2Qt8SizeHintERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19AbstractChartLayout8sizeHintEN2Qt8SizeHintERK6QS'
          'izeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int AbstractChartLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractchartlayout.html#count
    """
    #  int AbstractChartLayout::count() const
    ritual = 'ritual_ZNK19AbstractChartLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19AbstractChartLayout5countEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def itemAt(self, a0: int) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *AbstractChartLayout::itemAt(int a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractchartlayout.html#itemAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *AbstractChartLayout::itemAt(int a0) const
    ritual = 'ritual_ZNK19AbstractChartLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19AbstractChartLayout6itemAtEi'
    address = self.uglySide.call(ritual, a0)
    return QGraphicsLayoutItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMargins)
  def setMargins(self, margins: QMargins) -> None:
    """
    Calls Qt's 'void AbstractChartLayout::setMargins(const QMargins
    &margins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#setMargins

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void AbstractChartLayout::setMargins(const QMargins &margins)
    ritual = 'ritual_ZN19AbstractChartLayout10setMarginsERK8QMargins'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19AbstractChartLayout10setMarginsERK8QMargins'
    self.uglySide.call(ritual, self._valueOf(margins, 'QMargins'))

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void AbstractChartLayout::setGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractchartlayout.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void AbstractChartLayout::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN19AbstractChartLayout11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19AbstractChartLayout11setGeometryERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

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
    Qt's 'AbstractChartLayout::AbstractChartLayout(ChartPresenter
    *presenter)': the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'AbstractChartLayout.__init__' has no cute function yet. Qt's "
        "'AbstractChartLayout::AbstractChartLayout(ChartPresenter "
        "*presenter)': the class is abstract, so C++ cannot make one, and "
        "the C++ class of ours does not fill in every function it leaves "
        "open.")

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
  def removeAt(self, a0: int) -> None:
    """
    Calls Qt's 'void AbstractChartLayout::removeAt(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/abstractchartlayout.html#removeAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void AbstractChartLayout::removeAt(int a0)
    ritual = 'ritual_ZN19AbstractChartLayout8removeAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19AbstractChartLayout8removeAtEi'
    self.uglySide.call(ritual, a0)
