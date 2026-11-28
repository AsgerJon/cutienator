"""
PolarChartAxisAngular binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/polarchartaxisangular_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means PolarChartAxisAngular to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import PolarChartAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF, QSizeF
  from ..QtGui import QColor, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPen = WAIT['QPen']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PolarChartAxisAngular(PolarChartAxis):
  """
  The cute side of Qt's PolarChartAxisAngular: a plain Python object standing
  in front of one C++ PolarChartAxisAngular.

  It is built on the cute 'PolarChartAxis', as Qt's PolarChartAxisAngular is
  built on Qt's PolarChartAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PolarChartAxisAngular that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'orientation',
  'sizeHint', 'updateGeometry', 'createItems', 'updateMinorTickItems',
  'preferredAxisRadius', 'handleArrowPenChanged', 'handleGridPenChanged',
  'handleMinorArrowPenChanged', 'handleMinorGridPenChanged',
  'handleGridLineColorChanged', 'handleMinorGridLineColorChanged',
  'moveLabelToPosition', 'updateMinorTickGeometry'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PolarChartAxisAngular::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int PolarChartAxisAngular::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'PolarChartAxisAngular::~PolarChartAxisAngular()': the destructor:
    Python never removes a C++ PolarChartAxisAngular.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ PolarChartAxisAngular is created at the first use, not by
    'PolarChartAxisAngular(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PolarChartAxisAngular.
  - Qt tells when it has removed the C++ PolarChartAxisAngular. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's PolarChartAxisAngular that has no cute function yet,
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
    Calls Qt's 'QString PolarChartAxisAngular::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxisangular.html#tr

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
    #  QString PolarChartAxisAngular::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21PolarChartAxisAngular2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PolarChartAxisAngular'

  #  A C++ PolarChartAxisAngular Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PolarChartAxisAngular'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PolarChartAxisAngular::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PolarChartAxisAngular::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21PolarChartAxisAngular10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation PolarChartAxisAngular::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation PolarChartAxisAngular::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK21PolarChartAxisAngular11orientationEv',
    ))

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF PolarChartAxisAngular::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#sizeHint

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
    #  QSizeF PolarChartAxisAngular::sizeHint(Qt::SizeHint which, const
    #      QSizeF &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    ritual = (
        'ritual_ZNK21PolarChartAxisAngular8sizeHintEN2Qt8SizeHintERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21PolarChartAxisAngular8sizeHintEN2Qt8SizeHintERK6'
          'QSizeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(float, QPointF, QRectF)
  def moveLabelToPosition(
      self,
      angularCoordinate: float,
      labelPoint: QPointF,
      labelRect: QRectF,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF PolarChartAxisAngular::moveLabelToPosition(qreal
    angularCoordinate, QPointF labelPoint, QRectF labelRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#moveLabelToPosition

    Parameters
    ----------

    angularCoordinate : float
      Passed on as it is.

    labelPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    labelRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF PolarChartAxisAngular::moveLabelToPosition(qreal
    #      angularCoordinate, QPointF labelPoint, QRectF labelRect) const
    address = self.uglySide.call(
        'ritual_ZNK21PolarChartAxisAngular19moveLabelToPositionEd7QPointF6Q'
        'RectF',
        angularCoordinate, self._valueOf(labelPoint, 'QPointF'),
        self._valueOf(labelRect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'PolarChartAxisAngular::PolarChartAxisAngular(QAbstractAxis *axis,
    QGraphicsItem *item, bool intervalAxis)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'PolarChartAxisAngular.__init__' has no cute function yet. Qt's "
        "'PolarChartAxisAngular::PolarChartAxisAngular(QAbstractAxis *axis, "
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
    Calls Qt's 'void PolarChartAxisAngular::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#updateGeometry
    """
    #  void PolarChartAxisAngular::updateGeometry()
    ritual = 'ritual_ZN21PolarChartAxisAngular14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21PolarChartAxisAngular14updateGeometryEv'
    self.uglySide.call(ritual)

  @overload(int)
  def createItems(self, count: int) -> None:
    """
    Calls Qt's 'void PolarChartAxisAngular::createItems(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#createItems

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void PolarChartAxisAngular::createItems(int count)
    ritual = 'ritual_ZN21PolarChartAxisAngular11createItemsEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21PolarChartAxisAngular11createItemsEi'
    self.uglySide.call(ritual, count)

  def updateMinorTickItems(self) -> None:
    """
    Calls Qt's 'void PolarChartAxisAngular::updateMinorTickItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#updateMinorTickItems
    """
    #  void PolarChartAxisAngular::updateMinorTickItems()
    ritual = 'ritual_ZN21PolarChartAxisAngular20updateMinorTickItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21PolarChartAxisAngular20updateMinorTickItemsEv'
    self.uglySide.call(ritual)

  @overload(QSizeF)
  def preferredAxisRadius(self, maxSize: QSizeF) -> float:
    """
    Calls Qt's 'qreal PolarChartAxisAngular::preferredAxisRadius(const QSizeF
    &maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#preferredAxisRadius

    Parameters
    ----------

    maxSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  qreal PolarChartAxisAngular::preferredAxisRadius(const QSizeF
    #      &maxSize)
    ritual = (
        'ritual_ZN21PolarChartAxisAngular19preferredAxisRadiusERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21PolarChartAxisAngular19preferredAxisRadiusERK6QSi'
          'zeF')
    return self.uglySide.call(ritual, self._valueOf(maxSize))

  @overload(QPen)
  def handleArrowPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxisAngular::handleArrowPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#handleArrowPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxisAngular::handleArrowPenChanged(const QPen &pen)
    ritual = (
        'ritual_ZN21PolarChartAxisAngular21handleArrowPenChangedERK4QPen')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21PolarChartAxisAngular21handleArrowPenChangedERK4Q'
          'Pen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleGridPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxisAngular::handleGridPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#handleGridPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxisAngular::handleGridPenChanged(const QPen &pen)
    ritual = 'ritual_ZN21PolarChartAxisAngular20handleGridPenChangedERK4QPen'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21PolarChartAxisAngular20handleGridPenChangedERK4QP'
          'en')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleMinorArrowPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxisAngular::handleMinorArrowPenChanged(const
    QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxisAngular::handleMinorArrowPenChanged(const QPen
    #      &pen)
    ritual = (
        'ritual_ZN21PolarChartAxisAngular26handleMinorArrowPenChangedERK4QP'
        'en')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21PolarChartAxisAngular26handleMinorArrowPenChanged'
          'ERK4QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleMinorGridPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxisAngular::handleMinorGridPenChanged(const
    QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxisAngular::handleMinorGridPenChanged(const QPen &pen)
    ritual = (
        'ritual_ZN21PolarChartAxisAngular25handleMinorGridPenChangedERK4QPe'
        'n')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21PolarChartAxisAngular25handleMinorGridPenChangedE'
          'RK4QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QColor)
  def handleGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void PolarChartAxisAngular::handleGridLineColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void PolarChartAxisAngular::handleGridLineColorChanged(const QColor
    #      &color)
    ritual = (
        'ritual_ZN21PolarChartAxisAngular26handleGridLineColorChangedERK6QC'
        'olor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21PolarChartAxisAngular26handleGridLineColorChanged'
          'ERK6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QColor)
  def handleMinorGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    PolarChartAxisAngular::handleMinorGridLineColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void PolarChartAxisAngular::handleMinorGridLineColorChanged(const
    #      QColor &color)
    ritual = (
        'ritual_ZN21PolarChartAxisAngular31handleMinorGridLineColorChangedE'
        'RK6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21PolarChartAxisAngular31handleMinorGridLineColorCh'
          'angedERK6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  def updateMinorTickGeometry(self) -> None:
    """
    Calls Qt's 'void PolarChartAxisAngular::updateMinorTickGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisangular.html#updateMinorTickGeometry
    """
    #  void PolarChartAxisAngular::updateMinorTickGeometry()
    self.uglySide.call(
        'ritual_ZN21PolarChartAxisAngular23updateMinorTickGeometryEv',
    )
