"""
DomSize binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomSize to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomSize(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomSize: a plain Python object standing in front of
  one C++ DomSize.

  What exists
  -----------

  Every function of Qt's DomSize that has a ritual and that Python can call
  so far, 8 names in all: 'elementWidth', 'setElementWidth',
  'hasElementWidth', 'clearElementWidth', 'elementHeight',
  'setElementHeight', 'hasElementHeight', 'clearElementHeight'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomSize::~DomSize()': the destructor: Python never removes a C++
    DomSize.
  - Qt's 'void DomSize::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomSize::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomSize is created at the first use, not by 'DomSize(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomSize.
  - Each name of Qt's DomSize that has no cute function yet, 'read', 'write',
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
  __qt_class__ = 'DomSize'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementWidth(self) -> int:
    """
    Calls Qt's 'int DomSize::elementWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#elementWidth
    """
    #  int DomSize::elementWidth() const
    return self.uglySide.call('ritual_ZNK7DomSize12elementWidthEv')

  def hasElementWidth(self) -> bool:
    """
    Calls Qt's 'bool DomSize::hasElementWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#hasElementWidth
    """
    #  bool DomSize::hasElementWidth() const
    return self.uglySide.call('ritual_ZNK7DomSize15hasElementWidthEv')

  def elementHeight(self) -> int:
    """
    Calls Qt's 'int DomSize::elementHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#elementHeight
    """
    #  int DomSize::elementHeight() const
    return self.uglySide.call('ritual_ZNK7DomSize13elementHeightEv')

  def hasElementHeight(self) -> bool:
    """
    Calls Qt's 'bool DomSize::hasElementHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#hasElementHeight
    """
    #  bool DomSize::hasElementHeight() const
    return self.uglySide.call('ritual_ZNK7DomSize16hasElementHeightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setElementWidth(self, a: int) -> None:
    """
    Calls Qt's 'void DomSize::setElementWidth(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#setElementWidth

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomSize::setElementWidth(int a)
    self.uglySide.call('ritual_ZN7DomSize15setElementWidthEi', a)

  @overload(int)
  def setElementHeight(self, a: int) -> None:
    """
    Calls Qt's 'void DomSize::setElementHeight(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#setElementHeight

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomSize::setElementHeight(int a)
    self.uglySide.call('ritual_ZN7DomSize16setElementHeightEi', a)

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
    Notes what was given, for Qt's 'DomSize::DomSize()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#DomSize
    """
    #  DomSize::DomSize()
    self._noteCreation(DomSize, lambda: Rituals.call(
        'ritual_ZN7DomSizeC1Ev',
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

  def clearElementWidth(self) -> None:
    """
    Calls Qt's 'void DomSize::clearElementWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#clearElementWidth
    """
    #  void DomSize::clearElementWidth()
    self.uglySide.call('ritual_ZN7DomSize17clearElementWidthEv')

  def clearElementHeight(self) -> None:
    """
    Calls Qt's 'void DomSize::clearElementHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/domsize.html#clearElementHeight
    """
    #  void DomSize::clearElementHeight()
    self.uglySide.call('ritual_ZN7DomSize18clearElementHeightEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomSize::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomSize.read' has no cute function yet. Qt's 'void "
        "DomSize::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomSize::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomSize.write' has no cute function yet. Qt's 'void "
        "DomSize::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
