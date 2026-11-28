"""
PolarChartAxisRadial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/polarchartaxisradial_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means PolarChartAxisRadial to be private: it declares the class in a
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

  from ..QtCore import QMetaObject, QSizeF
  from ..QtGui import QColor, QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPen = WAIT['QPen']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PolarChartAxisRadial(PolarChartAxis):
  """
  The cute side of Qt's PolarChartAxisRadial: a plain Python object standing
  in front of one C++ PolarChartAxisRadial.

  It is built on the cute 'PolarChartAxis', as Qt's PolarChartAxisRadial is
  built on Qt's PolarChartAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's PolarChartAxisRadial that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'orientation',
  'sizeHint', 'updateGeometry', 'createItems', 'updateMinorTickItems',
  'preferredAxisRadius', 'handleArrowPenChanged', 'handleGridPenChanged',
  'handleMinorArrowPenChanged', 'handleMinorGridPenChanged',
  'handleGridLineColorChanged', 'handleMinorGridLineColorChanged',
  'updateMinorTickGeometry'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *PolarChartAxisRadial::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int PolarChartAxisRadial::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'PolarChartAxisRadial::~PolarChartAxisRadial()': the destructor:
    Python never removes a C++ PolarChartAxisRadial.

  What has no ritual
  ------------------

  3 of the 21 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ PolarChartAxisRadial is created at the first use, not by
    'PolarChartAxisRadial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ PolarChartAxisRadial.
  - Qt tells when it has removed the C++ PolarChartAxisRadial. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's PolarChartAxisRadial that has no cute function yet,
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
    Calls Qt's 'QString PolarChartAxisRadial::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxisradial.html#tr

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
    #  QString PolarChartAxisRadial::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20PolarChartAxisRadial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'PolarChartAxisRadial'

  #  A C++ PolarChartAxisRadial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_PolarChartAxisRadial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *PolarChartAxisRadial::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *PolarChartAxisRadial::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20PolarChartAxisRadial10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation PolarChartAxisRadial::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation PolarChartAxisRadial::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK20PolarChartAxisRadial11orientationEv',
    ))

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF PolarChartAxisRadial::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/polarchartaxisradial.html#sizeHint

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
    #  QSizeF PolarChartAxisRadial::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    ritual = (
        'ritual_ZNK20PolarChartAxisRadial8sizeHintEN2Qt8SizeHintERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20PolarChartAxisRadial8sizeHintEN2Qt8SizeHintERK6Q'
          'SizeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

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
    Qt's 'PolarChartAxisRadial::PolarChartAxisRadial(QAbstractAxis *axis,
    QGraphicsItem *item, bool intervalAxis)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'PolarChartAxisRadial.__init__' has no cute function yet. Qt's "
        "'PolarChartAxisRadial::PolarChartAxisRadial(QAbstractAxis *axis, "
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
    Calls Qt's 'void PolarChartAxisRadial::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#updateGeometry
    """
    #  void PolarChartAxisRadial::updateGeometry()
    ritual = 'ritual_ZN20PolarChartAxisRadial14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20PolarChartAxisRadial14updateGeometryEv'
    self.uglySide.call(ritual)

  @overload(int)
  def createItems(self, count: int) -> None:
    """
    Calls Qt's 'void PolarChartAxisRadial::createItems(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#createItems

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void PolarChartAxisRadial::createItems(int count)
    ritual = 'ritual_ZN20PolarChartAxisRadial11createItemsEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20PolarChartAxisRadial11createItemsEi'
    self.uglySide.call(ritual, count)

  def updateMinorTickItems(self) -> None:
    """
    Calls Qt's 'void PolarChartAxisRadial::updateMinorTickItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#updateMinorTickItems
    """
    #  void PolarChartAxisRadial::updateMinorTickItems()
    ritual = 'ritual_ZN20PolarChartAxisRadial20updateMinorTickItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20PolarChartAxisRadial20updateMinorTickItemsEv'
    self.uglySide.call(ritual)

  @overload(QSizeF)
  def preferredAxisRadius(self, maxSize: QSizeF) -> float:
    """
    Calls Qt's 'qreal PolarChartAxisRadial::preferredAxisRadius(const QSizeF
    &maxSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#preferredAxisRadius

    Parameters
    ----------

    maxSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  qreal PolarChartAxisRadial::preferredAxisRadius(const QSizeF &maxSize)
    ritual = 'ritual_ZN20PolarChartAxisRadial19preferredAxisRadiusERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20PolarChartAxisRadial19preferredAxisRadiusERK6QSiz'
          'eF')
    return self.uglySide.call(ritual, self._valueOf(maxSize))

  @overload(QPen)
  def handleArrowPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxisRadial::handleArrowPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#handleArrowPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxisRadial::handleArrowPenChanged(const QPen &pen)
    ritual = 'ritual_ZN20PolarChartAxisRadial21handleArrowPenChangedERK4QPen'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20PolarChartAxisRadial21handleArrowPenChangedERK4QP'
          'en')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleGridPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxisRadial::handleGridPenChanged(const QPen
    &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#handleGridPenChanged

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxisRadial::handleGridPenChanged(const QPen &pen)
    ritual = 'ritual_ZN20PolarChartAxisRadial20handleGridPenChangedERK4QPen'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20PolarChartAxisRadial20handleGridPenChangedERK4QPe'
          'n')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleMinorArrowPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxisRadial::handleMinorArrowPenChanged(const
    QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxisRadial::handleMinorArrowPenChanged(const QPen &pen)
    ritual = (
        'ritual_ZN20PolarChartAxisRadial26handleMinorArrowPenChangedERK4QPe'
        'n')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20PolarChartAxisRadial26handleMinorArrowPenChangedE'
          'RK4QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QPen)
  def handleMinorGridPenChanged(self, pen: QPen) -> None:
    """
    Calls Qt's 'void PolarChartAxisRadial::handleMinorGridPenChanged(const
    QPen &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void PolarChartAxisRadial::handleMinorGridPenChanged(const QPen &pen)
    ritual = (
        'ritual_ZN20PolarChartAxisRadial25handleMinorGridPenChangedERK4QPen')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20PolarChartAxisRadial25handleMinorGridPenChangedER'
          'K4QPen')
    self.uglySide.call(ritual, self._valueOf(pen))

  @overload(QColor)
  def handleGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void PolarChartAxisRadial::handleGridLineColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void PolarChartAxisRadial::handleGridLineColorChanged(const QColor
    #      &color)
    ritual = (
        'ritual_ZN20PolarChartAxisRadial26handleGridLineColorChangedERK6QCo'
        'lor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20PolarChartAxisRadial26handleGridLineColorChangedE'
          'RK6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  @overload(QColor)
  def handleMinorGridLineColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void
    PolarChartAxisRadial::handleMinorGridLineColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void PolarChartAxisRadial::handleMinorGridLineColorChanged(const
    #      QColor &color)
    ritual = (
        'ritual_ZN20PolarChartAxisRadial31handleMinorGridLineColorChangedER'
        'K6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20PolarChartAxisRadial31handleMinorGridLineColorCha'
          'ngedERK6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

  def updateMinorTickGeometry(self) -> None:
    """
    Calls Qt's 'void PolarChartAxisRadial::updateMinorTickGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/polarchartaxisradial.html#updateMinorTickGeometry
    """
    #  void PolarChartAxisRadial::updateMinorTickGeometry()
    self.uglySide.call(
        'ritual_ZN20PolarChartAxisRadial23updateMinorTickGeometryEv',
    )
