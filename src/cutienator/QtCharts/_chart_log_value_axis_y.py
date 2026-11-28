"""
ChartLogValueAxisY binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/chartlogvalueaxisy_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means ChartLogValueAxisY to be private: it declares the class in a
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
  from typing import Optional

  from ..QtCore import QMetaObject, QSizeF
  from . import QLogValueAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLogValueAxis = WAIT['QtCharts:QLogValueAxis']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChartLogValueAxisY(VerticalAxis):
  """
  The cute side of Qt's ChartLogValueAxisY: a plain Python object standing in
  front of one C++ ChartLogValueAxisY.

  It is built on the cute 'VerticalAxis', as Qt's ChartLogValueAxisY is built
  on Qt's VerticalAxis, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ChartLogValueAxisY that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'sizeHint',
  'updateGeometry', 'handleBaseChanged', 'handleLabelFormatChanged'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ChartLogValueAxisY::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int ChartLogValueAxisY::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'ChartLogValueAxisY::~ChartLogValueAxisY()': the destructor: Python
    never removes a C++ ChartLogValueAxisY.
  - Qt's 'QList<qreal> ChartLogValueAxisY::calculateLayout() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ChartLogValueAxisY is created at the first use, not by
    'ChartLogValueAxisY(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ChartLogValueAxisY.
  - Qt tells when it has removed the C++ ChartLogValueAxisY. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString ChartLogValueAxisY::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/chartlogvalueaxisy.html#tr

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
    #  QString ChartLogValueAxisY::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18ChartLogValueAxisY2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ChartLogValueAxisY'

  #  A C++ ChartLogValueAxisY Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ChartLogValueAxisY'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ChartLogValueAxisY::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/chartlogvalueaxisy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ChartLogValueAxisY::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18ChartLogValueAxisY10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(self, which: Qt.SizeHint, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF ChartLogValueAxisY::sizeHint(Qt::SizeHint which, const
    QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/chartlogvalueaxisy.html#sizeHint

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
    #  QSizeF ChartLogValueAxisY::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    ritual = (
        'ritual_ZNK18ChartLogValueAxisY8sizeHintEN2Qt8SizeHintERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18ChartLogValueAxisY8sizeHintEN2Qt8SizeHintERK6QSi'
          'zeF')
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
    'ChartLogValueAxisY::ChartLogValueAxisY(QLogValueAxis *axis,
    QGraphicsItem *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/chartlogvalueaxisy.html#ChartLogValueAxisY

    Parameters
    ----------

    axis : Optional[QLogValueAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ChartLogValueAxisY::ChartLogValueAxisY(QLogValueAxis *axis,
    #      QGraphicsItem *item)
    self._noteCreation(ChartLogValueAxisY, lambda: Rituals.call(
        'ritual_ZN18ChartLogValueAxisYC1EP13QLogValueAxisP13QGraphicsItem',
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
    Calls Qt's 'void ChartLogValueAxisY::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartlogvalueaxisy.html#updateGeometry
    """
    #  void ChartLogValueAxisY::updateGeometry()
    ritual = 'ritual_ZN18ChartLogValueAxisY14updateGeometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18ChartLogValueAxisY14updateGeometryEv'
    self.uglySide.call(ritual)

  @overload(float)
  def handleBaseChanged(self, base: float) -> None:
    """
    Calls Qt's 'void ChartLogValueAxisY::handleBaseChanged(qreal base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartlogvalueaxisy.html#handleBaseChanged

    Parameters
    ----------

    base : float
      Passed on as it is.
    """
    #  void ChartLogValueAxisY::handleBaseChanged(qreal base)
    self.uglySide.call(
        'ritual_ZN18ChartLogValueAxisY17handleBaseChangedEd', base,
    )

  @overload(str)
  def handleLabelFormatChanged(self, format: str) -> None:
    """
    Calls Qt's 'void ChartLogValueAxisY::handleLabelFormatChanged(const
    QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/chartlogvalueaxisy.html#handleLabelFormatChanged

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ChartLogValueAxisY::handleLabelFormatChanged(const QString
    #      &format)
    self.uglySide.call(
        'ritual_ZN18ChartLogValueAxisY24handleLabelFormatChangedERK7QString',
        format,
    )
