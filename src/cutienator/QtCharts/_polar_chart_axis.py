"""
PolarChartAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/polarchartaxis_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means PolarChartAxis to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import ChartAxisElement

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSizeF
  from ..QtGui import QBrush, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QPen = WAIT['QPen']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PolarChartAxis(ChartAxisElement):
  """
  The cute side of Qt's PolarChartAxis: a plain Python object standing in
  front of one C++ PolarChartAxis.

  It is built on the cute 'ChartAxisElement', as Qt's PolarChartAxis is built
  on Qt's ChartAxisElement, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PolarChartAxis that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'setGeometry',
  'preferredAxisRadius', 'tickWidth', 'gridGeometry', 'emptyAxis',
  'createItems', 'updateMinorTickItems', 'handleShadesBrushChanged',
  'handleShadesPenChanged', 'deleteItems'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PolarChartAxis::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int PolarChartAxis::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'PolarChartAxis::~PolarChartAxis()': the destructor: Python never
    removes a C++ PolarChartAxis.
  - Qt's 'void PolarChartAxis::updateLayout(const QList<qreal> &layout)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void PolarChartAxis::createAxisLabels(const QList<qreal> &layout)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ PolarChartAxis is created at the first use, not by
    'PolarChartAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PolarChartAxis.
  - Qt tells when it has removed the C++ PolarChartAxis. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's PolarChartAxis that has no cute function yet,
    '__init__', 'createAxisLabels', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString PolarChartAxis::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxis.html#tr

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
    #  QString PolarChartAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14PolarChartAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PolarChartAxis'

  #  A C++ PolarChartAxis Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PolarChartAxis'

  #  The functions Qt calls itself that PolarChartAxis is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createAxisLabels': (
          'void PolarChartAxis::createAxisLabels(const QList<qreal> &)',
      ),
  }

  #  The functions Qt calls itself that PolarChartAxis is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'preferredAxisRadius': (
          ('_ZN14PolarChartAxis19preferredAxisRadiusERK6QSizeF',
           ('double', 'number', ''),
           (
               ('address', 'value', 'QtCore:QSizeF'),
           )),
      ),
      'createItems': (
          ('_ZN14PolarChartAxis11createItemsEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'updateMinorTickItems': (
          ('_ZN14PolarChartAxis20updateMinorTickItemsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
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
    Calls Qt's 'const QMetaObject *PolarChartAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PolarChartAxis::metaObject() const
    address = self.uglySide.call('ritual_ZNK14PolarChartAxis10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def gridGeometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF PolarChartAxis::gridGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxis.html#gridGeometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF PolarChartAxis::gridGeometry() const
    ritual = 'ritual_ZNK14PolarChartAxis12gridGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14PolarChartAxis12gridGeometryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def emptyAxis(self) -> bool:
    """
    Calls Qt's 'bool PolarChartAxis::emptyAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxis.html#emptyAxis
    """
    #  bool PolarChartAxis::emptyAxis() const
    ritual = 'ritual_ZNK14PolarChartAxis9emptyAxisEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14PolarChartAxis9emptyAxisEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF, QRectF)
  def setGeometry(self, axis: QRectF, grid: QRectF) -> None:
    """
    Calls Qt's 'void PolarChartAxis::setGeometry(const QRectF &axis, const
    QRectF &grid)'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxis.html#setGeometry

    Parameters
    ----------

    axis : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    grid : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void PolarChartAxis::setGeometry(const QRectF &axis, const QRectF
    #      &grid)
    ritual = 'ritual_ZN14PolarChartAxis11setGeometryERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14PolarChartAxis11setGeometryERK6QRectFS2_'
    self.uglySide.call(ritual, self._valueOf(axis), self._valueOf(grid))

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
    Qt's 'PolarChartAxis::PolarChartAxis(QAbstractAxis *axis, QGraphicsItem
    *item, bool intervalAxis)': the class is abstract, so C++ cannot make
    one, and the C++ class of ours does not fill in every function it leaves
    open.
    """
    raise NotImplementedError(
        "'PolarChartAxis.__init__' has no cute function yet. Qt's "
        "'PolarChartAxis::PolarChartAxis(QAbstractAxis *axis, QGraphicsItem "
        "*item, bool intervalAxis)': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  @overload(QSizeF)
  def preferredAxisRadius(self, maxSize: QSizeF) -> float:
    """
    Calls Qt's 'qreal PolarChartAxis::preferredAxisRadius(const QSizeF
    &maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxis.html#preferredAxisRadius

    Parameters
    ----------

    maxSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  qreal PolarChartAxis::preferredAxisRadius(const QSizeF &maxSize)
    return self.uglySide.call(
        'ritual_ZN14PolarChartAxis19preferredAxisRadiusERK6QSizeF',
        self._valueOf(maxSize),
    )

  def tickWidth(self) -> int:
    """
    Calls Qt's 'int PolarChartAxis::tickWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxis.html#tickWidth
    """
    #  int PolarChartAxis::tickWidth()
    return self.uglySide.call('ritual_ZN14PolarChartAxis9tickWidthEv')

  @overload(int)
  def createItems(self, count: int) -> None:
    """
    Calls Qt's 'void PolarChartAxis::createItems(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxis.html#createItems

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void PolarChartAxis::createItems(int count)
    self.uglySide.call('ritual_ZN14PolarChartAxis11createItemsEi', count)

  def updateMinorTickItems(self) -> None:
    """
    Calls Qt's 'void PolarChartAxis::updateMinorTickItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxis.html#updateMinorTickItems
    """
    #  void PolarChartAxis::updateMinorTickItems()
    self.uglySide.call('ritual_ZN14PolarChartAxis20updateMinorTickItemsEv')

  @overload(QBrush)
  def handleShadesBrushChanged(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void PolarChartAxis::handleShadesBrushChanged(const QBrush
    &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxis.html#handleShadesBrushChanged

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void PolarChartAxis::handleShadesBrushChanged(const QBrush &brush)
    ritual = 'ritual_ZN14PolarChartAxis24handleShadesBrushChangedERK6QBrush'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14PolarChartAxis24handleShadesBrushChangedERK6QBrus'
          'h')
    self.uglySide.call(ritual, self._valueOf(brush))

  @overload(QPen)
  def handleShadesPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxis::handleShadesPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxis.html#handleShadesPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxis::handleShadesPenChanged(const QPen &pen)
    ritual = 'ritual_ZN14PolarChartAxis22handleShadesPenChangedERK4QPen'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14PolarChartAxis22handleShadesPenChangedERK4QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(int)
  def deleteItems(self, count: int) -> None:
    """
    Calls Qt's 'void PolarChartAxis::deleteItems(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxis.html#deleteItems

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void PolarChartAxis::deleteItems(int count)
    self.uglySide.call('ritual_ZN14PolarChartAxis11deleteItemsEi', count)

  @staticmethod
  def createAxisLabels(*__, **_) -> Never:
    """
    Qt's 'void PolarChartAxis::createAxisLabels(const QList<qreal> &layout)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'PolarChartAxis.createAxisLabels' has no cute function yet. Qt's "
        "'void PolarChartAxis::createAxisLabels(const QList<qreal> "
        "&layout)': takes a type Python has no way to hand over yet.")
