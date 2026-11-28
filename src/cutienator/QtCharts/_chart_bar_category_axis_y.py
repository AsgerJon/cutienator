"""
ChartBarCategoryAxisY binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartbarcategoryaxisy_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means ChartBarCategoryAxisY to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QGraphicsItem
from . import VerticalAxis

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSizeF
  from . import QBarCategoryAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBarCategoryAxis = WAIT['QtCharts:QBarCategoryAxis']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartBarCategoryAxisY(VerticalAxis):
  """
  The cute side of Qt's ChartBarCategoryAxisY: a plain Python object standing
  in front of one C++ ChartBarCategoryAxisY.

  It is built on the cute 'VerticalAxis', as Qt's ChartBarCategoryAxisY is
  built on Qt's VerticalAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartBarCategoryAxisY that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'tr', 'sizeHint',
  'updateGeometry', 'handleCategoriesChanged'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ChartBarCategoryAxisY::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int ChartBarCategoryAxisY::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'ChartBarCategoryAxisY::~ChartBarCategoryAxisY()': the destructor:
    Python never removes a C++ ChartBarCategoryAxisY.
  - Qt's 'QList<qreal> ChartBarCategoryAxisY::calculateLayout() const': gives
    a type Python has no way to take yet.
  - Qt's 'QStringList ChartBarCategoryAxisY::createCategoryLabels(const
    QList<qreal> &layout) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ChartBarCategoryAxisY is created at the first use, not by
    'ChartBarCategoryAxisY(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartBarCategoryAxisY.
  - Qt tells when it has removed the C++ ChartBarCategoryAxisY. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ChartBarCategoryAxisY that has no cute function yet,
    'createCategoryLabels', holds a function that raises
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
    Calls Qt's 'QString ChartBarCategoryAxisY::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/chartbarcategoryaxisy.html#tr

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
    #  QString ChartBarCategoryAxisY::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21ChartBarCategoryAxisY2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartBarCategoryAxisY'

  #  A C++ ChartBarCategoryAxisY Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ChartBarCategoryAxisY'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ChartBarCategoryAxisY::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartbarcategoryaxisy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ChartBarCategoryAxisY::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21ChartBarCategoryAxisY10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(self, which: Qt.SizeHint, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF ChartBarCategoryAxisY::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartbarcategoryaxisy.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF ChartBarCategoryAxisY::sizeHint(Qt::SizeHint which, const
    #      QSizeF &constraint) const
    ritual = (
        'ritual_ZNK21ChartBarCategoryAxisY8sizeHintEN2Qt8SizeHintERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21ChartBarCategoryAxisY8sizeHintEN2Qt8SizeHintERK6'
          'QSizeF')
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

  @overload(QBarCategoryAxis)
  @overload(NoneType)
  @overload(QBarCategoryAxis, QGraphicsItem)
  @overload(QBarCategoryAxis, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      axis: Optional[QBarCategoryAxis],
      item: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'ChartBarCategoryAxisY::ChartBarCategoryAxisY(QBarCategoryAxis *axis,
    QGraphicsItem *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/chartbarcategoryaxisy.html#ChartBarCategoryAxisY

    Parameters
    ----------

    axis : Optional[QBarCategoryAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  ChartBarCategoryAxisY::ChartBarCategoryAxisY(QBarCategoryAxis *axis,
    #      QGraphicsItem *item)
    self._noteCreation(ChartBarCategoryAxisY, lambda: Rituals.call(
        'ritual_ZN21ChartBarCategoryAxisYC1EP16QBarCategoryAxisP13QGraphics'
        'Item',
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

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void ChartBarCategoryAxisY::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartbarcategoryaxisy.html#updateGeometry
    """
    #  void ChartBarCategoryAxisY::updateGeometry()
    ritual = 'ritual_ZN21ChartBarCategoryAxisY14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21ChartBarCategoryAxisY14updateGeometryEv'
    self.uglySide.call(ritual)

  def handleCategoriesChanged(self) -> None:
    """
    Calls Qt's 'void ChartBarCategoryAxisY::handleCategoriesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartbarcategoryaxisy.html#handleCategoriesChanged
    """
    #  void ChartBarCategoryAxisY::handleCategoriesChanged()
    self.uglySide.call(
        'ritual_ZN21ChartBarCategoryAxisY23handleCategoriesChangedEv',
    )

  @staticmethod
  def createCategoryLabels(*__, **_) -> Never:
    """
    Qt's 'QStringList ChartBarCategoryAxisY::createCategoryLabels(const
    QList<qreal> &layout) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'ChartBarCategoryAxisY.createCategoryLabels' has no cute function "
        "yet. Qt's 'QStringList "
        "ChartBarCategoryAxisY::createCategoryLabels(const QList<qreal> "
        "&layout) const': takes a type Python has no way to hand over yet.")
