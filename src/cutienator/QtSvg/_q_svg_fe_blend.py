"""
QSvgFeBlend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgFeBlend to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
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
  from ..QtGui import QImage, QPainter
  from . import QSvgRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QSvgRectF = WAIT['QSvgRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgFeBlend(QSvgFeFilterPrimitive):
  """
  The cute side of Qt's QSvgFeBlend: a plain Python object standing in front
  of one C++ QSvgFeBlend.

  It is built on the cute 'QSvgFeFilterPrimitive', as Qt's QSvgFeBlend is
  built on Qt's QSvgFeFilterPrimitive, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgFeBlend that has a ritual and that Python can
  call so far, 5 names in all: 'type', 'apply', 'requiresSourceAlpha',
  'input2', 'mode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgFeBlend::~QSvgFeBlend()': the destructor: Python never removes
    a C++ QSvgFeBlend.

  What to expect
  --------------

  - The C++ QSvgFeBlend is created at the first use, not by
    'QSvgFeBlend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgFeBlend.
  """

  #  The enums Qt writes inside QSvgFeBlend, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum, scoped=True):
    """
    The enum 'QSvgFeBlend::Mode' of Qt, with the 5 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Normal = Kee[int](0)
    Multiply = Kee[int](1)
    Screen = Kee[int](2)
    Darken = Kee[int](3)
    Lighten = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgFeBlend'

  #  A C++ QSvgFeBlend Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgFeBlend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgFeBlend::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeblend.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgFeBlend::type() const
    ritual = 'ritual_ZNK11QSvgFeBlend4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSvgFeBlend4typeEv'
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
    Calls Qt's 'QImage QSvgFeBlend::apply(const QMap<QString, QImage>
    &sources, QPainter *p, const QRectF &itemBounds, const QRectF
    &filterBounds, QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes
    filterUnits) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeblend.html#apply

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
    #  QImage QSvgFeBlend::apply(const QMap<QString, QImage> &sources,
    #      QPainter *p, const QRectF &itemBounds, const QRectF &filterBounds,
    #      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QSvgFeBlend5applyERK4QMapI7QString6QImageEP8QPainterRK'
        '6QRectFSA_N5QtSvg9UnitTypesESC_',
        self._valueOf(sources), self._addressOf(p),
        self._valueOf(itemBounds), self._valueOf(filterBounds),
        primitiveUnits.value, filterUnits.value,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def requiresSourceAlpha(self) -> bool:
    """
    Calls Qt's 'bool QSvgFeBlend::requiresSourceAlpha() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgfeblend.html#requiresSourceAlpha
    """
    #  bool QSvgFeBlend::requiresSourceAlpha() const
    ritual = 'ritual_ZNK11QSvgFeBlend19requiresSourceAlphaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QSvgFeBlend19requiresSourceAlphaEv'
    return self.uglySide.call(ritual)

  def input2(self) -> str:
    """
    Calls Qt's 'QString QSvgFeBlend::input2() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeblend.html#input2

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSvgFeBlend::input2() const
    return self.uglySide.call('ritual_ZNK11QSvgFeBlend6input2Ev')

  def mode(self) -> Mode:
    """
    Calls Qt's 'Mode QSvgFeBlend::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeblend.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode QSvgFeBlend::mode() const
    return QSvgFeBlend.Mode(self.uglySide.call(
        'ritual_ZNK11QSvgFeBlend4modeEv',
    ))

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

  @overload(QSvgNode, str, str, QSvgRectF, str, Mode)
  @overload(NoneType, str, str, QSvgRectF, str, Mode)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      input: str,
      result: str,
      rect: QSvgRectF,
      input2: str,
      mode: Mode,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgFeBlend::QSvgFeBlend(QSvgNode
    *parent, const QString &input, const QString &result, const QSvgRectF
    &rect, const QString &input2, Mode mode)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgfeblend.html#QSvgFeBlend

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

    mode : Mode
      Passed on as its number.
    """
    #  QSvgFeBlend::QSvgFeBlend(QSvgNode *parent, const QString &input, const
    #      QString &result, const QSvgRectF &rect, const QString &input2,
    #      Mode mode)
    self._noteCreation(QSvgFeBlend, lambda: Rituals.call(
        'ritual_ZN11QSvgFeBlendC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectFS4_NS_'
        '4ModeE',
        self._addressOf(parent), input, result, self._valueOf(rect), input2,
        mode.value,
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
