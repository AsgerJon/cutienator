"""
CartesianChartAxis binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/cartesianchartaxis_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means CartesianChartAxis to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import ChartAxisElement

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSizeF
  from ..QtGui import QBrush, QColor, QPen
  from . import QValueAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QPen = WAIT['QPen']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QValueAxis = WAIT['QtCharts:QValueAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CartesianChartAxis(ChartAxisElement):
  """
  The cute side of Qt's CartesianChartAxis: a plain Python object standing in
  front of one C++ CartesianChartAxis.

  It is built on the cute 'ChartAxisElement', as Qt's CartesianChartAxis is
  built on Qt's ChartAxisElement, and has everything that class has.

  What exists
  -----------

  Every function of Qt's CartesianChartAxis that has a ritual and that Python
  can call so far, 21 names in all: 'metaObject', 'tr', 'setGeometry',
  'gridGeometry', 'emptyAxis', 'sizeHint', 'setDateTimeLabelsFormat',
  'updateGeometry', 'handleArrowPenChanged', 'handleGridPenChanged',
  'handleShadesBrushChanged', 'handleShadesPenChanged',
  'handleMinorArrowPenChanged', 'handleMinorGridPenChanged',
  'handleGridLineColorChanged', 'handleMinorGridLineColorChanged',
  'updateLabelsValues', 'updateLabelsDateTimes', 'createItems',
  'deleteItems', 'updateMinorTickItems'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *CartesianChartAxis::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int CartesianChartAxis::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'CartesianChartAxis::~CartesianChartAxis()': the destructor: Python
    never removes a C++ CartesianChartAxis.
  - Qt's 'void CartesianChartAxis::updateLayout(const QList<qreal> &layout)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 29 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ CartesianChartAxis is created at the first use, not by
    'CartesianChartAxis(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ CartesianChartAxis.
  - Qt tells when it has removed the C++ CartesianChartAxis. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's CartesianChartAxis that has no cute function yet,
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
    Calls Qt's 'QString CartesianChartAxis::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/cartesianchartaxis.html#tr

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
    #  QString CartesianChartAxis::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18CartesianChartAxis2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'CartesianChartAxis'

  #  A C++ CartesianChartAxis Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_CartesianChartAxis'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *CartesianChartAxis::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/cartesianchartaxis.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *CartesianChartAxis::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18CartesianChartAxis10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def gridGeometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF CartesianChartAxis::gridGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#gridGeometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF CartesianChartAxis::gridGeometry() const
    ritual = 'ritual_ZNK18CartesianChartAxis12gridGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18CartesianChartAxis12gridGeometryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def emptyAxis(self) -> bool:
    """
    Calls Qt's 'bool CartesianChartAxis::emptyAxis() const'.

    Qt's own words: https://doc.qt.io/qt-6/cartesianchartaxis.html#emptyAxis
    """
    #  bool CartesianChartAxis::emptyAxis() const
    ritual = 'ritual_ZNK18CartesianChartAxis9emptyAxisEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18CartesianChartAxis9emptyAxisEv'
    return self.uglySide.call(ritual)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF CartesianChartAxis::sizeHint(Qt::SizeHint which, const
    QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/cartesianchartaxis.html#sizeHint

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
    #  QSizeF CartesianChartAxis::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    ritual = (
        'ritual_ZNK18CartesianChartAxis8sizeHintEN2Qt8SizeHintERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18CartesianChartAxis8sizeHintEN2Qt8SizeHintERK6QSi'
          'zeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF, QRectF)
  def setGeometry(self, axis: QRectF, grid: QRectF) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::setGeometry(const QRectF &axis,
    const QRectF &grid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#setGeometry

    Parameters
    ----------

    axis : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    grid : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void CartesianChartAxis::setGeometry(const QRectF &axis, const QRectF
    #      &grid)
    ritual = 'ritual_ZN18CartesianChartAxis11setGeometryERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18CartesianChartAxis11setGeometryERK6QRectFS2_'
    self.uglySide.call(ritual, self._valueOf(axis), self._valueOf(grid))

  @overload(QRectF)
  def setGeometry(self, size: QRectF) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::setGeometry(const QRectF &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#setGeometry

    Parameters
    ----------

    size : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void CartesianChartAxis::setGeometry(const QRectF &size)
    ritual = 'ritual_ZN18CartesianChartAxis11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18CartesianChartAxis11setGeometryERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(str)
  def setDateTimeLabelsFormat(self, format: str) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::setDateTimeLabelsFormat(const
    QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#setDateTimeLabelsFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void CartesianChartAxis::setDateTimeLabelsFormat(const QString
    #      &format)
    self.uglySide.call(
        'ritual_ZN18CartesianChartAxis23setDateTimeLabelsFormatERK7QString',
        format,
    )

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
    Qt's 'CartesianChartAxis::CartesianChartAxis(QAbstractAxis *axis,
    QGraphicsItem *item, bool intervalAxis)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'CartesianChartAxis.__init__' has no cute function yet. Qt's "
        "'CartesianChartAxis::CartesianChartAxis(QAbstractAxis *axis, "
        "QGraphicsItem *item, bool intervalAxis)': the class is abstract, "
        "so C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#updateGeometry
    """
    #  void CartesianChartAxis::updateGeometry()
    self.uglySide.call('ritual_ZN18CartesianChartAxis14updateGeometryEv')

  @overload(QPen)
  def handleArrowPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::handleArrowPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#handleArrowPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void CartesianChartAxis::handleArrowPenChanged(const QPen &pen)
    ritual = 'ritual_ZN18CartesianChartAxis21handleArrowPenChangedERK4QPen'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18CartesianChartAxis21handleArrowPenChangedERK4QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleGridPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::handleGridPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#handleGridPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void CartesianChartAxis::handleGridPenChanged(const QPen &pen)
    ritual = 'ritual_ZN18CartesianChartAxis20handleGridPenChangedERK4QPen'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18CartesianChartAxis20handleGridPenChangedERK4QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QBrush)
  def handleShadesBrushChanged(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::handleShadesBrushChanged(const
    QBrush &brush)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#handleShadesBrushChanged

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void CartesianChartAxis::handleShadesBrushChanged(const QBrush &brush)
    ritual = (
        'ritual_ZN18CartesianChartAxis24handleShadesBrushChangedERK6QBrush')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18CartesianChartAxis24handleShadesBrushChangedERK6Q'
          'Brush')
    self.uglySide.call(ritual, self._valueOf(brush))

  @overload(QPen)
  def handleShadesPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::handleShadesPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#handleShadesPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void CartesianChartAxis::handleShadesPenChanged(const QPen &pen)
    ritual = 'ritual_ZN18CartesianChartAxis22handleShadesPenChangedERK4QPen'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18CartesianChartAxis22handleShadesPenChangedERK4QPe'
          'n')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleMinorArrowPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::handleMinorArrowPenChanged(const
    QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#handleMinorArrowPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void CartesianChartAxis::handleMinorArrowPenChanged(const QPen &pen)
    ritual = (
        'ritual_ZN18CartesianChartAxis26handleMinorArrowPenChangedERK4QPen')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18CartesianChartAxis26handleMinorArrowPenChangedERK'
          '4QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleMinorGridPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::handleMinorGridPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#handleMinorGridPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void CartesianChartAxis::handleMinorGridPenChanged(const QPen &pen)
    ritual = (
        'ritual_ZN18CartesianChartAxis25handleMinorGridPenChangedERK4QPen')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18CartesianChartAxis25handleMinorGridPenChangedERK4'
          'QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QColor)
  def handleGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::handleGridLineColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#handleGridLineColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void CartesianChartAxis::handleGridLineColorChanged(const QColor
    #      &color)
    ritual = (
        'ritual_ZN18CartesianChartAxis26handleGridLineColorChangedERK6QColo'
        'r')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18CartesianChartAxis26handleGridLineColorChangedERK'
          '6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QColor)
  def handleMinorGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    CartesianChartAxis::handleMinorGridLineColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void CartesianChartAxis::handleMinorGridLineColorChanged(const QColor
    #      &color)
    ritual = (
        'ritual_ZN18CartesianChartAxis31handleMinorGridLineColorChangedERK6'
        'QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18CartesianChartAxis31handleMinorGridLineColorChang'
          'edERK6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QValueAxis)
  @overload(NoneType)
  def updateLabelsValues(self, axis: Optional[QValueAxis]) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::updateLabelsValues(QValueAxis
    *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#updateLabelsValues

    Parameters
    ----------

    axis : Optional[QValueAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void CartesianChartAxis::updateLabelsValues(QValueAxis *axis)
    self.uglySide.call(
        'ritual_ZN18CartesianChartAxis18updateLabelsValuesEP10QValueAxis',
        self._addressOf(axis),
    )

  def updateLabelsDateTimes(self) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::updateLabelsDateTimes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#updateLabelsDateTimes
    """
    #  void CartesianChartAxis::updateLabelsDateTimes()
    self.uglySide.call(
        'ritual_ZN18CartesianChartAxis21updateLabelsDateTimesEv',
    )

  @overload(int)
  def createItems(self, count: int) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::createItems(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#createItems

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void CartesianChartAxis::createItems(int count)
    self.uglySide.call('ritual_ZN18CartesianChartAxis11createItemsEi', count)

  @overload(int)
  def deleteItems(self, count: int) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::deleteItems(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#deleteItems

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void CartesianChartAxis::deleteItems(int count)
    self.uglySide.call('ritual_ZN18CartesianChartAxis11deleteItemsEi', count)

  def updateMinorTickItems(self) -> None:
    """
    Calls Qt's 'void CartesianChartAxis::updateMinorTickItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/cartesianchartaxis.html#updateMinorTickItems
    """
    #  void CartesianChartAxis::updateMinorTickItems()
    self.uglySide.call(
        'ritual_ZN18CartesianChartAxis20updateMinorTickItemsEv',
    )
