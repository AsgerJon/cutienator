"""
DomSizeF binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomSizeF to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomSizeF(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomSizeF: a plain Python object standing in front of
  one C++ DomSizeF.

  What exists
  -----------

  Every function of Qt's DomSizeF that has a ritual and that Python can call
  so far, 8 names in all: 'elementWidth', 'setElementWidth',
  'hasElementWidth', 'clearElementWidth', 'elementHeight',
  'setElementHeight', 'hasElementHeight', 'clearElementHeight'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomSizeF::~DomSizeF()': the destructor: Python never removes a C++
    DomSizeF.
  - Qt's 'void DomSizeF::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomSizeF::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomSizeF is created at the first use, not by 'DomSizeF(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomSizeF.
  - Each name of Qt's DomSizeF that has no cute function yet, 'read',
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
  __qt_class__ = 'DomSizeF'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementWidth(self) -> float:
    """
    Calls Qt's 'double DomSizeF::elementWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#elementWidth
    """
    #  double DomSizeF::elementWidth() const
    return self.uglySide.call('ritual_ZNK8DomSizeF12elementWidthEv')

  def hasElementWidth(self) -> bool:
    """
    Calls Qt's 'bool DomSizeF::hasElementWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#hasElementWidth
    """
    #  bool DomSizeF::hasElementWidth() const
    return self.uglySide.call('ritual_ZNK8DomSizeF15hasElementWidthEv')

  def elementHeight(self) -> float:
    """
    Calls Qt's 'double DomSizeF::elementHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#elementHeight
    """
    #  double DomSizeF::elementHeight() const
    return self.uglySide.call('ritual_ZNK8DomSizeF13elementHeightEv')

  def hasElementHeight(self) -> bool:
    """
    Calls Qt's 'bool DomSizeF::hasElementHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#hasElementHeight
    """
    #  bool DomSizeF::hasElementHeight() const
    return self.uglySide.call('ritual_ZNK8DomSizeF16hasElementHeightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setElementWidth(self, a: float) -> None:
    """
    Calls Qt's 'void DomSizeF::setElementWidth(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#setElementWidth

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomSizeF::setElementWidth(double a)
    self.uglySide.call('ritual_ZN8DomSizeF15setElementWidthEd', a)

  @overload(float)
  def setElementHeight(self, a: float) -> None:
    """
    Calls Qt's 'void DomSizeF::setElementHeight(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#setElementHeight

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomSizeF::setElementHeight(double a)
    self.uglySide.call('ritual_ZN8DomSizeF16setElementHeightEd', a)

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
    Notes what was given, for Qt's 'DomSizeF::DomSizeF()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#DomSizeF
    """
    #  DomSizeF::DomSizeF()
    self._noteCreation(DomSizeF, lambda: Rituals.call(
        'ritual_ZN8DomSizeFC1Ev',
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
    Calls Qt's 'void DomSizeF::clearElementWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#clearElementWidth
    """
    #  void DomSizeF::clearElementWidth()
    self.uglySide.call('ritual_ZN8DomSizeF17clearElementWidthEv')

  def clearElementHeight(self) -> None:
    """
    Calls Qt's 'void DomSizeF::clearElementHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/domsizef.html#clearElementHeight
    """
    #  void DomSizeF::clearElementHeight()
    self.uglySide.call('ritual_ZN8DomSizeF18clearElementHeightEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomSizeF::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomSizeF.read' has no cute function yet. Qt's 'void "
        "DomSizeF::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomSizeF::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomSizeF.write' has no cute function yet. Qt's 'void "
        "DomSizeF::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
