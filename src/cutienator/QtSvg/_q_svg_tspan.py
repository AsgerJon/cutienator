"""
QSvgTspan binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgTspan to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QList
from . import QSvgNode, QSvgText

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSvgTspan(QSvgNode):
  """
  The cute side of Qt's QSvgTspan: a plain Python object standing in front of
  one C++ QSvgTspan.

  It is built on the cute 'QSvgNode', as Qt's QSvgTspan is built on Qt's
  QSvgNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgTspan that has a ritual and that Python can call
  so far, 6 names in all: 'type', 'addText', 'text', 'isTspan',
  'setWhitespaceMode', 'whitespaceMode'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgTspan::~QSvgTspan()': the destructor: Python never removes a
    C++ QSvgTspan.
  - Qt's 'void QSvgTspan::drawCommand(QPainter *a0, QSvgExtraStates &a1)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSvgTspan is created at the first use, not by 'QSvgTspan(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgTspan.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgTspan'

  #  A C++ QSvgTspan Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgTspan'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QSvgNode.Type:
    """
    Calls Qt's 'Type QSvgTspan::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtspan.html#type

    Returns
    -------

    QSvgNode.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QSvgNode.Type(number)'
      gives.
    """
    #  Type QSvgTspan::type() const
    ritual = 'ritual_ZNK9QSvgTspan4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QSvgTspan4typeEv'
    return QSvgNode.Type(self.uglySide.call(ritual))

  def text(self) -> str:
    """
    Calls Qt's 'const QString &QSvgTspan::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtspan.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QSvgTspan::text() const
    return self.uglySide.call('ritual_ZNK9QSvgTspan4textEv')

  def isTspan(self) -> bool:
    """
    Calls Qt's 'bool QSvgTspan::isTspan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtspan.html#isTspan
    """
    #  bool QSvgTspan::isTspan() const
    return self.uglySide.call('ritual_ZNK9QSvgTspan7isTspanEv')

  def whitespaceMode(self) -> QSvgText.WhitespaceMode:
    """
    Calls Qt's 'QSvgText::WhitespaceMode QSvgTspan::whitespaceMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtspan.html#whitespaceMode

    Returns
    -------

    QSvgText.WhitespaceMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgText.WhitespaceMode(number)' gives.
    """
    #  QSvgText::WhitespaceMode QSvgTspan::whitespaceMode() const
    return QSvgText.WhitespaceMode(self.uglySide.call(
        'ritual_ZNK9QSvgTspan14whitespaceModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSvgText.WhitespaceMode)
  def setWhitespaceMode(self, mode: QSvgText.WhitespaceMode) -> None:
    """
    Calls Qt's 'void QSvgTspan::setWhitespaceMode(QSvgText::WhitespaceMode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtspan.html#setWhitespaceMode

    Parameters
    ----------

    mode : QSvgText.WhitespaceMode
      Passed on as its number.
    """
    #  void QSvgTspan::setWhitespaceMode(QSvgText::WhitespaceMode mode)
    self.uglySide.call(
        'ritual_ZN9QSvgTspan17setWhitespaceModeEN8QSvgText14WhitespaceModeE',
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

  @overload(QSvgNode)
  @overload(NoneType)
  @overload(QSvgNode, bool)
  @overload(NoneType, bool)
  def __init__(
      self,
      parent: Optional[QSvgNode],
      isProperTspan: bool = True,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSvgTspan::QSvgTspan(QSvgNode *parent,
    bool isProperTspan)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtspan.html#QSvgTspan

    Parameters
    ----------

    parent : Optional[QSvgNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isProperTspan : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  QSvgTspan::QSvgTspan(QSvgNode *parent, bool isProperTspan)
    self._noteCreation(QSvgTspan, lambda: Rituals.call(
        'ritual_ZN9QSvgTspanC1EP8QSvgNodeb',
        self._addressOf(parent), isProperTspan,
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

  @overload(str)
  def addText(self, text: str) -> None:
    """
    Calls Qt's 'void QSvgTspan::addText(QStringView text)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgtspan.html#addText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSvgTspan::addText(QStringView text)
    self.uglySide.call('ritual_ZN9QSvgTspan7addTextE11QStringView', text)


#  Qt's 'QList<QSvgTspan *>': the list of QSvgTspan, which 'QList[QSvgTspan]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QSvgTspan.
QList.createKind(
    QSvgTspan, 'address',
    make='ritual_list_make_QSvgTspan_ptr',
    add='ritual_list_add_QSvgTspan_ptr',
    size='ritual_list_size_QSvgTspan_ptr',
    at='ritual_list_at_QSvgTspan_ptr',
    drop='ritual_list_drop_QSvgTspan_ptr',
)
