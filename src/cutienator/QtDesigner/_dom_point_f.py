"""
DomPointF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomPointF to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomPointF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomPointF: a plain Python object standing in front of
  one C++ DomPointF.

  What exists
  -----------

  Every function of Qt's DomPointF that has a ritual and that Python can call
  so far, 8 names in all: 'elementX', 'setElementX', 'hasElementX',
  'clearElementX', 'elementY', 'setElementY', 'hasElementY', 'clearElementY'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomPointF::~DomPointF()': the destructor: Python never removes a
    C++ DomPointF.
  - Qt's 'void DomPointF::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomPointF::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomPointF is created at the first use, not by 'DomPointF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomPointF.
  - Each name of Qt's DomPointF that has no cute function yet, 'read',
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
  __qt_class__ = 'DomPointF'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementX(self) -> float:
    """
    Calls Qt's 'double DomPointF::elementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#elementX
    """
    #  double DomPointF::elementX() const
    return self.uglySide.call('ritual_ZNK9DomPointF8elementXEv')

  def hasElementX(self) -> bool:
    """
    Calls Qt's 'bool DomPointF::hasElementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#hasElementX
    """
    #  bool DomPointF::hasElementX() const
    return self.uglySide.call('ritual_ZNK9DomPointF11hasElementXEv')

  def elementY(self) -> float:
    """
    Calls Qt's 'double DomPointF::elementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#elementY
    """
    #  double DomPointF::elementY() const
    return self.uglySide.call('ritual_ZNK9DomPointF8elementYEv')

  def hasElementY(self) -> bool:
    """
    Calls Qt's 'bool DomPointF::hasElementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#hasElementY
    """
    #  bool DomPointF::hasElementY() const
    return self.uglySide.call('ritual_ZNK9DomPointF11hasElementYEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setElementX(self, a: float) -> None:
    """
    Calls Qt's 'void DomPointF::setElementX(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#setElementX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomPointF::setElementX(double a)
    self.uglySide.call('ritual_ZN9DomPointF11setElementXEd', a)

  @overload(float)
  def setElementY(self, a: float) -> None:
    """
    Calls Qt's 'void DomPointF::setElementY(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#setElementY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomPointF::setElementY(double a)
    self.uglySide.call('ritual_ZN9DomPointF11setElementYEd', a)

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
    Notes what was given, for Qt's 'DomPointF::DomPointF()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#DomPointF
    """
    #  DomPointF::DomPointF()
    self._noteCreation(DomPointF, lambda: Rituals.call(
        'ritual_ZN9DomPointFC1Ev',
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
    Calls Qt's 'void DomPointF::clearElementX()'.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#clearElementX
    """
    #  void DomPointF::clearElementX()
    self.uglySide.call('ritual_ZN9DomPointF13clearElementXEv')

  def clearElementY(self) -> None:
    """
    Calls Qt's 'void DomPointF::clearElementY()'.

    Qt's own words: https://doc.qt.io/qt-6/dompointf.html#clearElementY
    """
    #  void DomPointF::clearElementY()
    self.uglySide.call('ritual_ZN9DomPointF13clearElementYEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomPointF::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomPointF.read' has no cute function yet. Qt's 'void "
        "DomPointF::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomPointF::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomPointF.write' has no cute function yet. Qt's 'void "
        "DomPointF::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
