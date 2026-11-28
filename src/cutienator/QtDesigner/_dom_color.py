"""
DomColor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomColor to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomColor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomColor: a plain Python object standing in front of
  one C++ DomColor.

  What exists
  -----------

  Every function of Qt's DomColor that has a ritual and that Python can call
  so far, 16 names in all: 'hasAttributeAlpha', 'attributeAlpha',
  'setAttributeAlpha', 'clearAttributeAlpha', 'elementRed', 'setElementRed',
  'hasElementRed', 'clearElementRed', 'elementGreen', 'setElementGreen',
  'hasElementGreen', 'clearElementGreen', 'elementBlue', 'setElementBlue',
  'hasElementBlue', 'clearElementBlue'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomColor::~DomColor()': the destructor: Python never removes a C++
    DomColor.
  - Qt's 'void DomColor::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomColor::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomColor is created at the first use, not by 'DomColor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomColor.
  - Each name of Qt's DomColor that has no cute function yet, 'read',
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
  __qt_class__ = 'DomColor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeAlpha(self) -> bool:
    """
    Calls Qt's 'bool DomColor::hasAttributeAlpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#hasAttributeAlpha
    """
    #  bool DomColor::hasAttributeAlpha() const
    return self.uglySide.call('ritual_ZNK8DomColor17hasAttributeAlphaEv')

  def attributeAlpha(self) -> int:
    """
    Calls Qt's 'int DomColor::attributeAlpha() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#attributeAlpha
    """
    #  int DomColor::attributeAlpha() const
    return self.uglySide.call('ritual_ZNK8DomColor14attributeAlphaEv')

  def elementRed(self) -> int:
    """
    Calls Qt's 'int DomColor::elementRed() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#elementRed
    """
    #  int DomColor::elementRed() const
    return self.uglySide.call('ritual_ZNK8DomColor10elementRedEv')

  def hasElementRed(self) -> bool:
    """
    Calls Qt's 'bool DomColor::hasElementRed() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#hasElementRed
    """
    #  bool DomColor::hasElementRed() const
    return self.uglySide.call('ritual_ZNK8DomColor13hasElementRedEv')

  def elementGreen(self) -> int:
    """
    Calls Qt's 'int DomColor::elementGreen() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#elementGreen
    """
    #  int DomColor::elementGreen() const
    return self.uglySide.call('ritual_ZNK8DomColor12elementGreenEv')

  def hasElementGreen(self) -> bool:
    """
    Calls Qt's 'bool DomColor::hasElementGreen() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#hasElementGreen
    """
    #  bool DomColor::hasElementGreen() const
    return self.uglySide.call('ritual_ZNK8DomColor15hasElementGreenEv')

  def elementBlue(self) -> int:
    """
    Calls Qt's 'int DomColor::elementBlue() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#elementBlue
    """
    #  int DomColor::elementBlue() const
    return self.uglySide.call('ritual_ZNK8DomColor11elementBlueEv')

  def hasElementBlue(self) -> bool:
    """
    Calls Qt's 'bool DomColor::hasElementBlue() const'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#hasElementBlue
    """
    #  bool DomColor::hasElementBlue() const
    return self.uglySide.call('ritual_ZNK8DomColor14hasElementBlueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAttributeAlpha(self, a: int) -> None:
    """
    Calls Qt's 'void DomColor::setAttributeAlpha(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#setAttributeAlpha

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomColor::setAttributeAlpha(int a)
    self.uglySide.call('ritual_ZN8DomColor17setAttributeAlphaEi', a)

  @overload(int)
  def setElementRed(self, a: int) -> None:
    """
    Calls Qt's 'void DomColor::setElementRed(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#setElementRed

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomColor::setElementRed(int a)
    self.uglySide.call('ritual_ZN8DomColor13setElementRedEi', a)

  @overload(int)
  def setElementGreen(self, a: int) -> None:
    """
    Calls Qt's 'void DomColor::setElementGreen(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#setElementGreen

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomColor::setElementGreen(int a)
    self.uglySide.call('ritual_ZN8DomColor15setElementGreenEi', a)

  @overload(int)
  def setElementBlue(self, a: int) -> None:
    """
    Calls Qt's 'void DomColor::setElementBlue(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#setElementBlue

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomColor::setElementBlue(int a)
    self.uglySide.call('ritual_ZN8DomColor14setElementBlueEi', a)

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
    Notes what was given, for Qt's 'DomColor::DomColor()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#DomColor
    """
    #  DomColor::DomColor()
    self._noteCreation(DomColor, lambda: Rituals.call(
        'ritual_ZN8DomColorC1Ev',
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

  def clearAttributeAlpha(self) -> None:
    """
    Calls Qt's 'void DomColor::clearAttributeAlpha()'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#clearAttributeAlpha
    """
    #  void DomColor::clearAttributeAlpha()
    self.uglySide.call('ritual_ZN8DomColor19clearAttributeAlphaEv')

  def clearElementRed(self) -> None:
    """
    Calls Qt's 'void DomColor::clearElementRed()'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#clearElementRed
    """
    #  void DomColor::clearElementRed()
    self.uglySide.call('ritual_ZN8DomColor15clearElementRedEv')

  def clearElementGreen(self) -> None:
    """
    Calls Qt's 'void DomColor::clearElementGreen()'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#clearElementGreen
    """
    #  void DomColor::clearElementGreen()
    self.uglySide.call('ritual_ZN8DomColor17clearElementGreenEv')

  def clearElementBlue(self) -> None:
    """
    Calls Qt's 'void DomColor::clearElementBlue()'.

    Qt's own words: https://doc.qt.io/qt-6/domcolor.html#clearElementBlue
    """
    #  void DomColor::clearElementBlue()
    self.uglySide.call('ritual_ZN8DomColor16clearElementBlueEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomColor::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomColor.read' has no cute function yet. Qt's 'void "
        "DomColor::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomColor::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomColor.write' has no cute function yet. Qt's 'void "
        "DomColor::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomColor *>': the list of DomColor, which 'QList[DomColor]'
#  gives. It is made here, so that there is one as soon as there can be a
#  DomColor.
QList.createKind(
    DomColor, 'address',
    make='ritual_list_make_DomColor_ptr',
    add='ritual_list_add_DomColor_ptr',
    size='ritual_list_size_DomColor_ptr',
    at='ritual_list_at_DomColor_ptr',
    drop='ritual_list_drop_DomColor_ptr',
)
