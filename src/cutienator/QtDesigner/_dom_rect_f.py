"""
DomRectF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomRectF to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomRectF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomRectF: a plain Python object standing in front of
  one C++ DomRectF.

  What exists
  -----------

  Every function of Qt's DomRectF that has a ritual and that Python can call
  so far, 16 names in all: 'elementX', 'setElementX', 'hasElementX',
  'clearElementX', 'elementY', 'setElementY', 'hasElementY', 'clearElementY',
  'elementWidth', 'setElementWidth', 'hasElementWidth', 'clearElementWidth',
  'elementHeight', 'setElementHeight', 'hasElementHeight',
  'clearElementHeight'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomRectF::~DomRectF()': the destructor: Python never removes a C++
    DomRectF.
  - Qt's 'void DomRectF::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomRectF::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomRectF is created at the first use, not by 'DomRectF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomRectF.
  - Each name of Qt's DomRectF that has no cute function yet, 'read',
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
  __qt_class__ = 'DomRectF'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementX(self) -> float:
    """
    Calls Qt's 'double DomRectF::elementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#elementX
    """
    #  double DomRectF::elementX() const
    return self.uglySide.call('ritual_ZNK8DomRectF8elementXEv')

  def hasElementX(self) -> bool:
    """
    Calls Qt's 'bool DomRectF::hasElementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#hasElementX
    """
    #  bool DomRectF::hasElementX() const
    return self.uglySide.call('ritual_ZNK8DomRectF11hasElementXEv')

  def elementY(self) -> float:
    """
    Calls Qt's 'double DomRectF::elementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#elementY
    """
    #  double DomRectF::elementY() const
    return self.uglySide.call('ritual_ZNK8DomRectF8elementYEv')

  def hasElementY(self) -> bool:
    """
    Calls Qt's 'bool DomRectF::hasElementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#hasElementY
    """
    #  bool DomRectF::hasElementY() const
    return self.uglySide.call('ritual_ZNK8DomRectF11hasElementYEv')

  def elementWidth(self) -> float:
    """
    Calls Qt's 'double DomRectF::elementWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#elementWidth
    """
    #  double DomRectF::elementWidth() const
    return self.uglySide.call('ritual_ZNK8DomRectF12elementWidthEv')

  def hasElementWidth(self) -> bool:
    """
    Calls Qt's 'bool DomRectF::hasElementWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#hasElementWidth
    """
    #  bool DomRectF::hasElementWidth() const
    return self.uglySide.call('ritual_ZNK8DomRectF15hasElementWidthEv')

  def elementHeight(self) -> float:
    """
    Calls Qt's 'double DomRectF::elementHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#elementHeight
    """
    #  double DomRectF::elementHeight() const
    return self.uglySide.call('ritual_ZNK8DomRectF13elementHeightEv')

  def hasElementHeight(self) -> bool:
    """
    Calls Qt's 'bool DomRectF::hasElementHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#hasElementHeight
    """
    #  bool DomRectF::hasElementHeight() const
    return self.uglySide.call('ritual_ZNK8DomRectF16hasElementHeightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setElementX(self, a: float) -> None:
    """
    Calls Qt's 'void DomRectF::setElementX(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#setElementX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomRectF::setElementX(double a)
    self.uglySide.call('ritual_ZN8DomRectF11setElementXEd', a)

  @overload(float)
  def setElementY(self, a: float) -> None:
    """
    Calls Qt's 'void DomRectF::setElementY(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#setElementY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomRectF::setElementY(double a)
    self.uglySide.call('ritual_ZN8DomRectF11setElementYEd', a)

  @overload(float)
  def setElementWidth(self, a: float) -> None:
    """
    Calls Qt's 'void DomRectF::setElementWidth(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#setElementWidth

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomRectF::setElementWidth(double a)
    self.uglySide.call('ritual_ZN8DomRectF15setElementWidthEd', a)

  @overload(float)
  def setElementHeight(self, a: float) -> None:
    """
    Calls Qt's 'void DomRectF::setElementHeight(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#setElementHeight

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomRectF::setElementHeight(double a)
    self.uglySide.call('ritual_ZN8DomRectF16setElementHeightEd', a)

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
    Notes what was given, for Qt's 'DomRectF::DomRectF()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#DomRectF
    """
    #  DomRectF::DomRectF()
    self._noteCreation(DomRectF, lambda: Rituals.call(
        'ritual_ZN8DomRectFC1Ev',
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
    Calls Qt's 'void DomRectF::clearElementX()'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#clearElementX
    """
    #  void DomRectF::clearElementX()
    self.uglySide.call('ritual_ZN8DomRectF13clearElementXEv')

  def clearElementY(self) -> None:
    """
    Calls Qt's 'void DomRectF::clearElementY()'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#clearElementY
    """
    #  void DomRectF::clearElementY()
    self.uglySide.call('ritual_ZN8DomRectF13clearElementYEv')

  def clearElementWidth(self) -> None:
    """
    Calls Qt's 'void DomRectF::clearElementWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#clearElementWidth
    """
    #  void DomRectF::clearElementWidth()
    self.uglySide.call('ritual_ZN8DomRectF17clearElementWidthEv')

  def clearElementHeight(self) -> None:
    """
    Calls Qt's 'void DomRectF::clearElementHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/domrectf.html#clearElementHeight
    """
    #  void DomRectF::clearElementHeight()
    self.uglySide.call('ritual_ZN8DomRectF18clearElementHeightEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomRectF::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomRectF.read' has no cute function yet. Qt's 'void "
        "DomRectF::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomRectF::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomRectF.write' has no cute function yet. Qt's 'void "
        "DomRectF::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
