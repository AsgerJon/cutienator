"""
QSvgFeComposite binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgFeComposite to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QMap
from . import QtSvg, QSvgFeFilterPrimitive, QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QImage, QPainter, QVector4D
  from . import QSvgRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QSvgRectF = WAIT['QSvgRectF']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgFeComposite(QSvgFeFilterPrimitive):
  """
  The cute side of Qt's QSvgFeComposite: a plain Python object standing in
  front of one C++ QSvgFeComposite.

  It is built on the cute 'QSvgFeFilterPrimitive', as Qt's QSvgFeComposite is
  built on Qt's QSvgFeFilterPrimitive, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgFeComposite that has a ritual and that Python
  can call so far, 6 names in all: 'type', 'apply', 'requiresSourceAlpha',
  'input2', 'compositionOperator', 'k'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgFeComposite::~QSvgFeComposite()': the destructor: Python never
    removes a C++ QSvgFeComposite.

  What to expect
  --------------

  - The C++ QSvgFeComposite is created at the first use, not by
    'QSvgFeComposite(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgFeComposite.
  """

  #  The enums Qt writes inside QSvgFeComposite, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Operator(CuteNum, scoped=True):
    """
    The enum 'QSvgFeComposite::Operator' of Qt, with the 7 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Over = Kee[int](0)
    In = Kee[int](1)
    Out = Kee[int](2)
    Atop = Kee[int](3)
    Xor = Kee[int](4)
    Lighter = Kee[int](5)
    Arithmetic = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgFeComposite'

  #  A C++ QSvgFeComposite Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgFeComposite'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgFeComposite::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfecomposite.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgFeComposite::type() const
    ritual = 'ritual_ZNK15QSvgFeComposite4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSvgFeComposite4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  @overload(
      QMap[str, QImage], QPainter, QRectF, QRectF, QtSvg.UnitTypes,
      QtSvg.UnitTypes,
  )
  @overload(
      QMap[str, QImage], NoneType, QRectF, QRectF, QtSvg.UnitTypes,
      QtSvg.UnitTypes,
  )
  def apply(
      self,
      sources: QMap[str, QImage],
      p: Optional[QPainter],
      itemBounds: QRectF,
      filterBounds: QRectF,
      primitiveUnits: QtSvg.UnitTypes,
      filterUnits: QtSvg.UnitTypes,
  ) -> QImage:
    """
    Calls Qt's 'QImage QSvgFeComposite::apply(const QMap<QString, QImage>
    &sources, QPainter *p, const QRectF &itemBounds, const QRectF
    &filterBounds, QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes
    filterUnits) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfecomposite.html#apply

    Parameters
    ----------

    sources : QMap[str, QImage]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    itemBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    filterBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    primitiveUnits : QtSvg.UnitTypes
      Passed on as its number.

    filterUnits : QtSvg.UnitTypes
      Passed on as its number.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSvgFeComposite::apply(const QMap<QString, QImage> &sources,
    #      QPainter *p, const QRectF &itemBounds, const QRectF &filterBounds,
    #      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QSvgFeComposite5applyERK4QMapI7QString6QImageEP8QPaint'
        'erRK6QRectFSA_N5QtSvg9UnitTypesESC_',
        self._valueOf(sources), self._addressOf(p),
        self._valueOf(itemBounds), self._valueOf(filterBounds),
        primitiveUnits.value, filterUnits.value,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def requiresSourceAlpha(self) -> bool:
    """
    Calls Qt's 'bool QSvgFeComposite::requiresSourceAlpha() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfecomposite.html#requiresSourceAlpha
    """
    #  bool QSvgFeComposite::requiresSourceAlpha() const
    ritual = 'ritual_ZNK15QSvgFeComposite19requiresSourceAlphaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSvgFeComposite19requiresSourceAlphaEv'
    return self.uglySide.call(ritual)

  def input2(self) -> str:
    """
    Calls Qt's 'QString QSvgFeComposite::input2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfecomposite.html#input2

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgFeComposite::input2() const
    return self.uglySide.call('ritual_ZNK15QSvgFeComposite6input2Ev')

  def compositionOperator(self) -> Operator:
    """
    Calls Qt's 'Operator QSvgFeComposite::compositionOperator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfecomposite.html#compositionOperator

    Returns
    -------

    Operator
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Operator(number)' gives.
    """
    #  Operator QSvgFeComposite::compositionOperator() const
    return QSvgFeComposite.Operator(self.uglySide.call(
        'ritual_ZNK15QSvgFeComposite19compositionOperatorEv',
    ))

  def k(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QSvgFeComposite::k() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfecomposite.html#k

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QSvgFeComposite::k() const
    address = self.uglySide.call('ritual_ZNK15QSvgFeComposite1kEv')
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

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

  @overload(QSvgNode, str, str, QSvgRectF, str, Operator, QVector4D)
  @overload(NoneType, str, str, QSvgRectF, str, Operator, QVector4D)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      input: str,
      result: str,
      rect: QSvgRectF,
      input2: str,
      op: Operator,
      k: QVector4D,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgFeComposite::QSvgFeComposite(QSvgNode
    *parent, const QString &input, const QString &result, const QSvgRectF
    &rect, const QString &input2, Operator op, const QVector4D &k)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfecomposite.html#QSvgFeComposite

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    input : str
      Passed on as it is: a QString is made of it for the call.

    result : str
      Passed on as it is: a QString is made of it for the call.

    rect : QSvgRectF
      Passed on as a value: Qt reads the C++ QSvgRectF, which stays Python's
      own.

    input2 : str
      Passed on as it is: a QString is made of it for the call.

    op : Operator
      Passed on as its number.

    k : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QSvgFeComposite::QSvgFeComposite(QSvgNode *parent, const QString
    #      &input, const QString &result, const QSvgRectF &rect, const
    #      QString &input2, Operator op, const QVector4D &k)
    self._noteCreation(QSvgFeComposite, lambda: Rituals.call(
        'ritual_ZN15QSvgFeCompositeC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectFS4'
        '_NS_8OperatorERK9QVector4D',
        self._addressOf(parent), input, result, self._valueOf(rect), input2,
        op.value, self._valueOf(k),
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
