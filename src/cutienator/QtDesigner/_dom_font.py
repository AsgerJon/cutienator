"""
DomFont binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomFont to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomFont(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomFont: a plain Python object standing in front of
  one C++ DomFont.

  What exists
  -----------

  Every function of Qt's DomFont that has a ritual and that Python can call
  so far, 48 names in all: 'elementFamily', 'setElementFamily',
  'hasElementFamily', 'clearElementFamily', 'elementPointSize',
  'setElementPointSize', 'hasElementPointSize', 'clearElementPointSize',
  'elementWeight', 'setElementWeight', 'hasElementWeight',
  'clearElementWeight', 'elementItalic', 'setElementItalic',
  'hasElementItalic', 'clearElementItalic', 'elementBold', 'setElementBold',
  'hasElementBold', 'clearElementBold', 'elementUnderline',
  'setElementUnderline', 'hasElementUnderline', 'clearElementUnderline',
  'elementStrikeOut', 'setElementStrikeOut', 'hasElementStrikeOut',
  'clearElementStrikeOut', 'elementAntialiasing', 'setElementAntialiasing',
  'hasElementAntialiasing', 'clearElementAntialiasing',
  'elementStyleStrategy', 'setElementStyleStrategy',
  'hasElementStyleStrategy', 'clearElementStyleStrategy', 'elementKerning',
  'setElementKerning', 'hasElementKerning', 'clearElementKerning',
  'elementHintingPreference', 'setElementHintingPreference',
  'hasElementHintingPreference', 'clearElementHintingPreference',
  'elementFontWeight', 'setElementFontWeight', 'hasElementFontWeight',
  'clearElementFontWeight'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomFont::~DomFont()': the destructor: Python never removes a C++
    DomFont.
  - Qt's 'void DomFont::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomFont::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 56 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomFont is created at the first use, not by 'DomFont(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomFont.
  - Each name of Qt's DomFont that has no cute function yet, 'read', 'write',
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
  __qt_class__ = 'DomFont'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementFamily(self) -> str:
    """
    Calls Qt's 'QString DomFont::elementFamily() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementFamily

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomFont::elementFamily() const
    return self.uglySide.call('ritual_ZNK7DomFont13elementFamilyEv')

  def hasElementFamily(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementFamily() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementFamily
    """
    #  bool DomFont::hasElementFamily() const
    return self.uglySide.call('ritual_ZNK7DomFont16hasElementFamilyEv')

  def elementPointSize(self) -> int:
    """
    Calls Qt's 'int DomFont::elementPointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementPointSize
    """
    #  int DomFont::elementPointSize() const
    return self.uglySide.call('ritual_ZNK7DomFont16elementPointSizeEv')

  def hasElementPointSize(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementPointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementPointSize
    """
    #  bool DomFont::hasElementPointSize() const
    return self.uglySide.call('ritual_ZNK7DomFont19hasElementPointSizeEv')

  def elementWeight(self) -> int:
    """
    Calls Qt's 'int DomFont::elementWeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementWeight
    """
    #  int DomFont::elementWeight() const
    return self.uglySide.call('ritual_ZNK7DomFont13elementWeightEv')

  def hasElementWeight(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementWeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementWeight
    """
    #  bool DomFont::hasElementWeight() const
    return self.uglySide.call('ritual_ZNK7DomFont16hasElementWeightEv')

  def elementItalic(self) -> bool:
    """
    Calls Qt's 'bool DomFont::elementItalic() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementItalic
    """
    #  bool DomFont::elementItalic() const
    return self.uglySide.call('ritual_ZNK7DomFont13elementItalicEv')

  def hasElementItalic(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementItalic() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementItalic
    """
    #  bool DomFont::hasElementItalic() const
    return self.uglySide.call('ritual_ZNK7DomFont16hasElementItalicEv')

  def elementBold(self) -> bool:
    """
    Calls Qt's 'bool DomFont::elementBold() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementBold
    """
    #  bool DomFont::elementBold() const
    return self.uglySide.call('ritual_ZNK7DomFont11elementBoldEv')

  def hasElementBold(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementBold() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementBold
    """
    #  bool DomFont::hasElementBold() const
    return self.uglySide.call('ritual_ZNK7DomFont14hasElementBoldEv')

  def elementUnderline(self) -> bool:
    """
    Calls Qt's 'bool DomFont::elementUnderline() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementUnderline
    """
    #  bool DomFont::elementUnderline() const
    return self.uglySide.call('ritual_ZNK7DomFont16elementUnderlineEv')

  def hasElementUnderline(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementUnderline() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementUnderline
    """
    #  bool DomFont::hasElementUnderline() const
    return self.uglySide.call('ritual_ZNK7DomFont19hasElementUnderlineEv')

  def elementStrikeOut(self) -> bool:
    """
    Calls Qt's 'bool DomFont::elementStrikeOut() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementStrikeOut
    """
    #  bool DomFont::elementStrikeOut() const
    return self.uglySide.call('ritual_ZNK7DomFont16elementStrikeOutEv')

  def hasElementStrikeOut(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementStrikeOut() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementStrikeOut
    """
    #  bool DomFont::hasElementStrikeOut() const
    return self.uglySide.call('ritual_ZNK7DomFont19hasElementStrikeOutEv')

  def elementAntialiasing(self) -> bool:
    """
    Calls Qt's 'bool DomFont::elementAntialiasing() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementAntialiasing
    """
    #  bool DomFont::elementAntialiasing() const
    return self.uglySide.call('ritual_ZNK7DomFont19elementAntialiasingEv')

  def hasElementAntialiasing(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementAntialiasing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#hasElementAntialiasing
    """
    #  bool DomFont::hasElementAntialiasing() const
    return self.uglySide.call('ritual_ZNK7DomFont22hasElementAntialiasingEv')

  def elementStyleStrategy(self) -> str:
    """
    Calls Qt's 'QString DomFont::elementStyleStrategy() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementStyleStrategy

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomFont::elementStyleStrategy() const
    return self.uglySide.call('ritual_ZNK7DomFont20elementStyleStrategyEv')

  def hasElementStyleStrategy(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementStyleStrategy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#hasElementStyleStrategy
    """
    #  bool DomFont::hasElementStyleStrategy() const
    return self.uglySide.call(
        'ritual_ZNK7DomFont23hasElementStyleStrategyEv',
    )

  def elementKerning(self) -> bool:
    """
    Calls Qt's 'bool DomFont::elementKerning() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementKerning
    """
    #  bool DomFont::elementKerning() const
    return self.uglySide.call('ritual_ZNK7DomFont14elementKerningEv')

  def hasElementKerning(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementKerning() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementKerning
    """
    #  bool DomFont::hasElementKerning() const
    return self.uglySide.call('ritual_ZNK7DomFont17hasElementKerningEv')

  def elementHintingPreference(self) -> str:
    """
    Calls Qt's 'QString DomFont::elementHintingPreference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#elementHintingPreference

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomFont::elementHintingPreference() const
    return self.uglySide.call(
        'ritual_ZNK7DomFont24elementHintingPreferenceEv',
    )

  def hasElementHintingPreference(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementHintingPreference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#hasElementHintingPreference
    """
    #  bool DomFont::hasElementHintingPreference() const
    return self.uglySide.call(
        'ritual_ZNK7DomFont27hasElementHintingPreferenceEv',
    )

  def elementFontWeight(self) -> str:
    """
    Calls Qt's 'QString DomFont::elementFontWeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#elementFontWeight

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomFont::elementFontWeight() const
    return self.uglySide.call('ritual_ZNK7DomFont17elementFontWeightEv')

  def hasElementFontWeight(self) -> bool:
    """
    Calls Qt's 'bool DomFont::hasElementFontWeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#hasElementFontWeight
    """
    #  bool DomFont::hasElementFontWeight() const
    return self.uglySide.call('ritual_ZNK7DomFont20hasElementFontWeightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setElementFamily(self, a: str) -> None:
    """
    Calls Qt's 'void DomFont::setElementFamily(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementFamily

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomFont::setElementFamily(const QString &a)
    self.uglySide.call('ritual_ZN7DomFont16setElementFamilyERK7QString', a)

  @overload(int)
  def setElementPointSize(self, a: int) -> None:
    """
    Calls Qt's 'void DomFont::setElementPointSize(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementPointSize

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomFont::setElementPointSize(int a)
    self.uglySide.call('ritual_ZN7DomFont19setElementPointSizeEi', a)

  @overload(int)
  def setElementWeight(self, a: int) -> None:
    """
    Calls Qt's 'void DomFont::setElementWeight(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementWeight

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomFont::setElementWeight(int a)
    self.uglySide.call('ritual_ZN7DomFont16setElementWeightEi', a)

  @overload(bool)
  def setElementItalic(self, a: bool) -> None:
    """
    Calls Qt's 'void DomFont::setElementItalic(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementItalic

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomFont::setElementItalic(bool a)
    self.uglySide.call('ritual_ZN7DomFont16setElementItalicEb', a)

  @overload(bool)
  def setElementBold(self, a: bool) -> None:
    """
    Calls Qt's 'void DomFont::setElementBold(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementBold

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomFont::setElementBold(bool a)
    self.uglySide.call('ritual_ZN7DomFont14setElementBoldEb', a)

  @overload(bool)
  def setElementUnderline(self, a: bool) -> None:
    """
    Calls Qt's 'void DomFont::setElementUnderline(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementUnderline

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomFont::setElementUnderline(bool a)
    self.uglySide.call('ritual_ZN7DomFont19setElementUnderlineEb', a)

  @overload(bool)
  def setElementStrikeOut(self, a: bool) -> None:
    """
    Calls Qt's 'void DomFont::setElementStrikeOut(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementStrikeOut

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomFont::setElementStrikeOut(bool a)
    self.uglySide.call('ritual_ZN7DomFont19setElementStrikeOutEb', a)

  @overload(bool)
  def setElementAntialiasing(self, a: bool) -> None:
    """
    Calls Qt's 'void DomFont::setElementAntialiasing(bool a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#setElementAntialiasing

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomFont::setElementAntialiasing(bool a)
    self.uglySide.call('ritual_ZN7DomFont22setElementAntialiasingEb', a)

  @overload(str)
  def setElementStyleStrategy(self, a: str) -> None:
    """
    Calls Qt's 'void DomFont::setElementStyleStrategy(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#setElementStyleStrategy

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomFont::setElementStyleStrategy(const QString &a)
    self.uglySide.call(
        'ritual_ZN7DomFont23setElementStyleStrategyERK7QString', a,
    )

  @overload(bool)
  def setElementKerning(self, a: bool) -> None:
    """
    Calls Qt's 'void DomFont::setElementKerning(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementKerning

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void DomFont::setElementKerning(bool a)
    self.uglySide.call('ritual_ZN7DomFont17setElementKerningEb', a)

  @overload(str)
  def setElementHintingPreference(self, a: str) -> None:
    """
    Calls Qt's 'void DomFont::setElementHintingPreference(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#setElementHintingPreference

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomFont::setElementHintingPreference(const QString &a)
    self.uglySide.call(
        'ritual_ZN7DomFont27setElementHintingPreferenceERK7QString', a,
    )

  @overload(str)
  def setElementFontWeight(self, a: str) -> None:
    """
    Calls Qt's 'void DomFont::setElementFontWeight(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#setElementFontWeight

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomFont::setElementFontWeight(const QString &a)
    self.uglySide.call(
        'ritual_ZN7DomFont20setElementFontWeightERK7QString', a,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'DomFont::DomFont()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#DomFont
    """
    #  DomFont::DomFont()
    self._noteCreation(DomFont, lambda: Rituals.call(
        'ritual_ZN7DomFontC1Ev',
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

  def clearElementFamily(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementFamily()'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#clearElementFamily
    """
    #  void DomFont::clearElementFamily()
    self.uglySide.call('ritual_ZN7DomFont18clearElementFamilyEv')

  def clearElementPointSize(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementPointSize()'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#clearElementPointSize
    """
    #  void DomFont::clearElementPointSize()
    self.uglySide.call('ritual_ZN7DomFont21clearElementPointSizeEv')

  def clearElementWeight(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementWeight()'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#clearElementWeight
    """
    #  void DomFont::clearElementWeight()
    self.uglySide.call('ritual_ZN7DomFont18clearElementWeightEv')

  def clearElementItalic(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementItalic()'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#clearElementItalic
    """
    #  void DomFont::clearElementItalic()
    self.uglySide.call('ritual_ZN7DomFont18clearElementItalicEv')

  def clearElementBold(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementBold()'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#clearElementBold
    """
    #  void DomFont::clearElementBold()
    self.uglySide.call('ritual_ZN7DomFont16clearElementBoldEv')

  def clearElementUnderline(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementUnderline()'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#clearElementUnderline
    """
    #  void DomFont::clearElementUnderline()
    self.uglySide.call('ritual_ZN7DomFont21clearElementUnderlineEv')

  def clearElementStrikeOut(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementStrikeOut()'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#clearElementStrikeOut
    """
    #  void DomFont::clearElementStrikeOut()
    self.uglySide.call('ritual_ZN7DomFont21clearElementStrikeOutEv')

  def clearElementAntialiasing(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementAntialiasing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#clearElementAntialiasing
    """
    #  void DomFont::clearElementAntialiasing()
    self.uglySide.call('ritual_ZN7DomFont24clearElementAntialiasingEv')

  def clearElementStyleStrategy(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementStyleStrategy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#clearElementStyleStrategy
    """
    #  void DomFont::clearElementStyleStrategy()
    self.uglySide.call('ritual_ZN7DomFont25clearElementStyleStrategyEv')

  def clearElementKerning(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementKerning()'.

    Qt's own words: https://doc.qt.io/qt-6/domfont.html#clearElementKerning
    """
    #  void DomFont::clearElementKerning()
    self.uglySide.call('ritual_ZN7DomFont19clearElementKerningEv')

  def clearElementHintingPreference(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementHintingPreference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#clearElementHintingPreference
    """
    #  void DomFont::clearElementHintingPreference()
    self.uglySide.call('ritual_ZN7DomFont29clearElementHintingPreferenceEv')

  def clearElementFontWeight(self) -> None:
    """
    Calls Qt's 'void DomFont::clearElementFontWeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domfont.html#clearElementFontWeight
    """
    #  void DomFont::clearElementFontWeight()
    self.uglySide.call('ritual_ZN7DomFont22clearElementFontWeightEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomFont::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomFont.read' has no cute function yet. Qt's 'void "
        "DomFont::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomFont::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomFont.write' has no cute function yet. Qt's 'void "
        "DomFont::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
