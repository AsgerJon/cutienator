"""
DomRect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomRect to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomRect(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomRect: a plain Python object standing in front of
  one C++ DomRect.

  What exists
  -----------

  Every function of Qt's DomRect that has a ritual and that Python can call
  so far, 16 names in all: 'elementX', 'setElementX', 'hasElementX',
  'clearElementX', 'elementY', 'setElementY', 'hasElementY', 'clearElementY',
  'elementWidth', 'setElementWidth', 'hasElementWidth', 'clearElementWidth',
  'elementHeight', 'setElementHeight', 'hasElementHeight',
  'clearElementHeight'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomRect::~DomRect()': the destructor: Python never removes a C++
    DomRect.
  - Qt's 'void DomRect::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomRect::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomRect is created at the first use, not by 'DomRect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomRect.
  - Each name of Qt's DomRect that has no cute function yet, 'read', 'write',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomRect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementX(self) -> int:
    """
    Calls Qt's 'int DomRect::elementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#elementX
    """
    #  int DomRect::elementX() const
    return self.uglySide.call('ritual_ZNK7DomRect8elementXEv')

  def hasElementX(self) -> bool:
    """
    Calls Qt's 'bool DomRect::hasElementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#hasElementX
    """
    #  bool DomRect::hasElementX() const
    return self.uglySide.call('ritual_ZNK7DomRect11hasElementXEv')

  def elementY(self) -> int:
    """
    Calls Qt's 'int DomRect::elementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#elementY
    """
    #  int DomRect::elementY() const
    return self.uglySide.call('ritual_ZNK7DomRect8elementYEv')

  def hasElementY(self) -> bool:
    """
    Calls Qt's 'bool DomRect::hasElementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#hasElementY
    """
    #  bool DomRect::hasElementY() const
    return self.uglySide.call('ritual_ZNK7DomRect11hasElementYEv')

  def elementWidth(self) -> int:
    """
    Calls Qt's 'int DomRect::elementWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#elementWidth
    """
    #  int DomRect::elementWidth() const
    return self.uglySide.call('ritual_ZNK7DomRect12elementWidthEv')

  def hasElementWidth(self) -> bool:
    """
    Calls Qt's 'bool DomRect::hasElementWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#hasElementWidth
    """
    #  bool DomRect::hasElementWidth() const
    return self.uglySide.call('ritual_ZNK7DomRect15hasElementWidthEv')

  def elementHeight(self) -> int:
    """
    Calls Qt's 'int DomRect::elementHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#elementHeight
    """
    #  int DomRect::elementHeight() const
    return self.uglySide.call('ritual_ZNK7DomRect13elementHeightEv')

  def hasElementHeight(self) -> bool:
    """
    Calls Qt's 'bool DomRect::hasElementHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#hasElementHeight
    """
    #  bool DomRect::hasElementHeight() const
    return self.uglySide.call('ritual_ZNK7DomRect16hasElementHeightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setElementX(self, a: int) -> None:
    """
    Calls Qt's 'void DomRect::setElementX(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#setElementX

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomRect::setElementX(int a)
    self.uglySide.call('ritual_ZN7DomRect11setElementXEi', a)

  @overload(int)
  def setElementY(self, a: int) -> None:
    """
    Calls Qt's 'void DomRect::setElementY(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#setElementY

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomRect::setElementY(int a)
    self.uglySide.call('ritual_ZN7DomRect11setElementYEi', a)

  @overload(int)
  def setElementWidth(self, a: int) -> None:
    """
    Calls Qt's 'void DomRect::setElementWidth(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#setElementWidth

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomRect::setElementWidth(int a)
    self.uglySide.call('ritual_ZN7DomRect15setElementWidthEi', a)

  @overload(int)
  def setElementHeight(self, a: int) -> None:
    """
    Calls Qt's 'void DomRect::setElementHeight(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#setElementHeight

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomRect::setElementHeight(int a)
    self.uglySide.call('ritual_ZN7DomRect16setElementHeightEi', a)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'DomRect::DomRect()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#DomRect
    """
    #  DomRect::DomRect()
    self._noteCreation(DomRect, lambda: Rituals.call(
        'ritual_ZN7DomRectC1Ev',
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

  def clearElementX(self) -> None:
    """
    Calls Qt's 'void DomRect::clearElementX()'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#clearElementX
    """
    #  void DomRect::clearElementX()
    self.uglySide.call('ritual_ZN7DomRect13clearElementXEv')

  def clearElementY(self) -> None:
    """
    Calls Qt's 'void DomRect::clearElementY()'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#clearElementY
    """
    #  void DomRect::clearElementY()
    self.uglySide.call('ritual_ZN7DomRect13clearElementYEv')

  def clearElementWidth(self) -> None:
    """
    Calls Qt's 'void DomRect::clearElementWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#clearElementWidth
    """
    #  void DomRect::clearElementWidth()
    self.uglySide.call('ritual_ZN7DomRect17clearElementWidthEv')

  def clearElementHeight(self) -> None:
    """
    Calls Qt's 'void DomRect::clearElementHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/domrect.html#clearElementHeight
    """
    #  void DomRect::clearElementHeight()
    self.uglySide.call('ritual_ZN7DomRect18clearElementHeightEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomRect::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomRect.read' has no cute function yet. Qt's 'void "
        "DomRect::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomRect::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomRect.write' has no cute function yet. Qt's 'void "
        "DomRect::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
