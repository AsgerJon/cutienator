"""
DomPoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomPoint to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomPoint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomPoint: a plain Python object standing in front of
  one C++ DomPoint.

  What exists
  -----------

  Every function of Qt's DomPoint that has a ritual and that Python can call
  so far, 8 names in all: 'elementX', 'setElementX', 'hasElementX',
  'clearElementX', 'elementY', 'setElementY', 'hasElementY', 'clearElementY'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomPoint::~DomPoint()': the destructor: Python never removes a C++
    DomPoint.
  - Qt's 'void DomPoint::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomPoint::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomPoint is created at the first use, not by 'DomPoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomPoint.
  - Each name of Qt's DomPoint that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomPoint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementX(self) -> int:
    """
    Calls Qt's 'int DomPoint::elementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#elementX
    """
    #  int DomPoint::elementX() const
    return self.uglySide.call('ritual_ZNK8DomPoint8elementXEv')

  def hasElementX(self) -> bool:
    """
    Calls Qt's 'bool DomPoint::hasElementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#hasElementX
    """
    #  bool DomPoint::hasElementX() const
    return self.uglySide.call('ritual_ZNK8DomPoint11hasElementXEv')

  def elementY(self) -> int:
    """
    Calls Qt's 'int DomPoint::elementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#elementY
    """
    #  int DomPoint::elementY() const
    return self.uglySide.call('ritual_ZNK8DomPoint8elementYEv')

  def hasElementY(self) -> bool:
    """
    Calls Qt's 'bool DomPoint::hasElementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#hasElementY
    """
    #  bool DomPoint::hasElementY() const
    return self.uglySide.call('ritual_ZNK8DomPoint11hasElementYEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setElementX(self, a: int) -> None:
    """
    Calls Qt's 'void DomPoint::setElementX(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#setElementX

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomPoint::setElementX(int a)
    self.uglySide.call('ritual_ZN8DomPoint11setElementXEi', a)

  @overload(int)
  def setElementY(self, a: int) -> None:
    """
    Calls Qt's 'void DomPoint::setElementY(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#setElementY

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomPoint::setElementY(int a)
    self.uglySide.call('ritual_ZN8DomPoint11setElementYEi', a)

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
    Notes what was given, for Qt's 'DomPoint::DomPoint()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#DomPoint
    """
    #  DomPoint::DomPoint()
    self._noteCreation(DomPoint, lambda: Rituals.call(
        'ritual_ZN8DomPointC1Ev',
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
    Calls Qt's 'void DomPoint::clearElementX()'.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#clearElementX
    """
    #  void DomPoint::clearElementX()
    self.uglySide.call('ritual_ZN8DomPoint13clearElementXEv')

  def clearElementY(self) -> None:
    """
    Calls Qt's 'void DomPoint::clearElementY()'.

    Qt's own words: https://doc.qt.io/qt-6/dompoint.html#clearElementY
    """
    #  void DomPoint::clearElementY()
    self.uglySide.call('ritual_ZN8DomPoint13clearElementYEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomPoint::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomPoint.read' has no cute function yet. Qt's 'void "
        "DomPoint::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomPoint::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomPoint.write' has no cute function yet. Qt's 'void "
        "DomPoint::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
