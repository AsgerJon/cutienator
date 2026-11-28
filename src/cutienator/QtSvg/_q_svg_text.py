"""
QSvgText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgText to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QSvgNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QSizeF
  from ..QtGui import QPainter
  from . import QSvgExtraStates, QSvgTspan
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QSizeF = WAIT['QSizeF']
  QSvgExtraStates = WAIT['QSvgExtraStates']
  QSvgTspan = WAIT['QSvgTspan']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgText(QSvgNode):
  """
  The cute side of Qt's QSvgText: a plain Python object standing in front of
  one C++ QSvgText.

  It is built on the cute 'QSvgNode', as Qt's QSvgText is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgText that has a ritual and that Python can call
  so far, 11 names in all: 'setTextArea', 'type', 'separateFillStroke',
  'addTspan', 'tspans', 'addText', 'addLineBreak', 'setWhitespaceMode',
  'position', 'size', 'whitespaceMode'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgText::~QSvgText()': the destructor: Python never removes a C++
    QSvgText.
  - Qt's 'void QSvgText::drawCommand(QPainter *p, QSvgExtraStates &states)':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QSvgText::shouldDrawNode(QPainter *p, QSvgExtraStates &states)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgText::internalFastBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'QRectF QSvgText::internalBounds(QPainter *p, QSvgExtraStates
    &states) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSvgText::draw_helper(QPainter *p, QSvgExtraStates &states,
    QRectF *boundingRect) const': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QSvgText is created at the first use, not by 'QSvgText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgText.
  - Each name of Qt's QSvgText that has no cute function yet, 'draw_helper',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QSvgText, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class WhitespaceMode(CuteNum):
    """
    The enum 'QSvgText::WhitespaceMode' of Qt, with the 2 names Qt gives in
    it.
    """

    Default = Kee[int](0)
    Preserve = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgText'

  #  A C++ QSvgText Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgText'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgText::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgText::type() const
    ritual = 'ritual_ZNK8QSvgText4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSvgText4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  @overload(QPainter, QSvgExtraStates)
  @overload(NoneType, QSvgExtraStates)
  def separateFillStroke(
      self,
      a0: Optional[QPainter],
      a1: QSvgExtraStates,
  ) -> bool:
    """
    Calls Qt's 'bool QSvgText::separateFillStroke(const QPainter *a0, const
    QSvgExtraStates &a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#separateFillStroke

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QSvgExtraStates
      Passed on as a value: Qt reads the C++ QSvgExtraStates, which stays
      Python's own.
    """
    #  bool QSvgText::separateFillStroke(const QPainter *a0, const
    #      QSvgExtraStates &a1) const
    ritual = (
        'ritual_ZNK8QSvgText18separateFillStrokeEPK8QPainterRK15QSvgExtraSt'
        'ates')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QSvgText18separateFillStrokeEPK8QPainterRK15QSvgE'
          'xtraStates')
    return self.uglySide.call(ritual, self._addressOf(a0), self._valueOf(a1))

  def tspans(self) -> QList[QSvgTspan]:
    """
    Calls Qt's 'const QList<QSvgTspan *> QSvgText::tspans() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#tspans

    Returns
    -------

    QList[QSvgTspan]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QSvgTspan *> QSvgText::tspans() const
    address = self.uglySide.call('ritual_ZNK8QSvgText6tspansEv')
    from . import QSvgTspan
    return QList[QSvgTspan]._cuteOwning(address)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSvgText::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSvgText::position() const
    address = self.uglySide.call('ritual_ZNK8QSvgText8positionEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QSvgText::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QSvgText::size() const
    address = self.uglySide.call('ritual_ZNK8QSvgText4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def whitespaceMode(self) -> WhitespaceMode:
    """
    Calls Qt's 'WhitespaceMode QSvgText::whitespaceMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#whitespaceMode

    Returns
    -------

    WhitespaceMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'WhitespaceMode(number)'
      gives.
    """
    #  WhitespaceMode QSvgText::whitespaceMode() const
    return QSvgText.WhitespaceMode(self.uglySide.call(
        'ritual_ZNK8QSvgText14whitespaceModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSizeF)
  def setTextArea(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QSvgText::setTextArea(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#setTextArea

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QSvgText::setTextArea(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN8QSvgText11setTextAreaERK6QSizeF', self._valueOf(size),
    )

  @overload(WhitespaceMode)
  def setWhitespaceMode(self, mode: WhitespaceMode) -> None:
    """
    Calls Qt's 'void QSvgText::setWhitespaceMode(WhitespaceMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#setWhitespaceMode

    Parameters
    ----------

    mode : WhitespaceMode
      Passed on as its number.
    """
    #  void QSvgText::setWhitespaceMode(WhitespaceMode mode)
    self.uglySide.call(
        'ritual_ZN8QSvgText17setWhitespaceModeENS_14WhitespaceModeE',
        mode.value,
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

  @overload(QSvgNode, QPointF)
  @overload(NoneType, QPointF)
  def __init__(self, parent: Optional[QSvgNode], coord: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QSvgText::QSvgText(QSvgNode *parent,
    const QPointF &coord)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#QSvgText

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coord : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QSvgText::QSvgText(QSvgNode *parent, const QPointF &coord)
    self._noteCreation(QSvgText, lambda: Rituals.call(
        'ritual_ZN8QSvgTextC1EP8QSvgNodeRK7QPointF',
        self._addressOf(parent), self._valueOf(coord, 'QPointF'),
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

  @overload(QSvgTspan)
  @overload(NoneType)
  def addTspan(self, tspan: Optional[QSvgTspan]) -> None:
    """
    Calls Qt's 'void QSvgText::addTspan(QSvgTspan *tspan)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#addTspan

    Parameters
    ----------

    tspan : Optional[QSvgTspan]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSvgText::addTspan(QSvgTspan *tspan)
    self.uglySide.call(
        'ritual_ZN8QSvgText8addTspanEP9QSvgTspan', self._addressOf(tspan),
    )

  @overload(str)
  def addText(self, text: str) -> None:
    """
    Calls Qt's 'void QSvgText::addText(QStringView text)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#addText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgText::addText(QStringView text)
    self.uglySide.call('ritual_ZN8QSvgText7addTextE11QStringView', text)

  def addLineBreak(self) -> None:
    """
    Calls Qt's 'void QSvgText::addLineBreak()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtext.html#addLineBreak
    """
    #  void QSvgText::addLineBreak()
    self.uglySide.call('ritual_ZN8QSvgText12addLineBreakEv')

  @staticmethod
  def draw_helper(*__, **_) -> Never:
    """
    Qt's 'void QSvgText::draw_helper(QPainter *p, QSvgExtraStates &states,
    QRectF *boundingRect) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QSvgText.draw_helper' has no cute function yet. Qt's 'void "
        "QSvgText::draw_helper(QPainter *p, QSvgExtraStates &states, QRectF "
        "*boundingRect) const': takes a type Python has no way to hand over "
        "yet.")
