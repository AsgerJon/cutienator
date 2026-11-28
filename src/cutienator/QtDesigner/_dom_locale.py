"""
DomLocale binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomLocale to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomLocale(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomLocale: a plain Python object standing in front of
  one C++ DomLocale.

  What exists
  -----------

  Every function of Qt's DomLocale that has a ritual and that Python can call
  so far, 8 names in all: 'hasAttributeLanguage', 'attributeLanguage',
  'setAttributeLanguage', 'clearAttributeLanguage', 'hasAttributeCountry',
  'attributeCountry', 'setAttributeCountry', 'clearAttributeCountry'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomLocale::~DomLocale()': the destructor: Python never removes a
    C++ DomLocale.
  - Qt's 'void DomLocale::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomLocale::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomLocale is created at the first use, not by 'DomLocale(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomLocale.
  - Each name of Qt's DomLocale that has no cute function yet, 'read',
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
  __qt_class__ = 'DomLocale'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeLanguage(self) -> bool:
    """
    Calls Qt's 'bool DomLocale::hasAttributeLanguage() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlocale.html#hasAttributeLanguage
    """
    #  bool DomLocale::hasAttributeLanguage() const
    return self.uglySide.call('ritual_ZNK9DomLocale20hasAttributeLanguageEv')

  def attributeLanguage(self) -> str:
    """
    Calls Qt's 'QString DomLocale::attributeLanguage() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlocale.html#attributeLanguage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLocale::attributeLanguage() const
    return self.uglySide.call('ritual_ZNK9DomLocale17attributeLanguageEv')

  def hasAttributeCountry(self) -> bool:
    """
    Calls Qt's 'bool DomLocale::hasAttributeCountry() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlocale.html#hasAttributeCountry
    """
    #  bool DomLocale::hasAttributeCountry() const
    return self.uglySide.call('ritual_ZNK9DomLocale19hasAttributeCountryEv')

  def attributeCountry(self) -> str:
    """
    Calls Qt's 'QString DomLocale::attributeCountry() const'.

    Qt's own words: https://doc.qt.io/qt-6/domlocale.html#attributeCountry

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLocale::attributeCountry() const
    return self.uglySide.call('ritual_ZNK9DomLocale16attributeCountryEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeLanguage(self, a: str) -> None:
    """
    Calls Qt's 'void DomLocale::setAttributeLanguage(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlocale.html#setAttributeLanguage

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLocale::setAttributeLanguage(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomLocale20setAttributeLanguageERK7QString', a,
    )

  @overload(str)
  def setAttributeCountry(self, a: str) -> None:
    """
    Calls Qt's 'void DomLocale::setAttributeCountry(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domlocale.html#setAttributeCountry

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLocale::setAttributeCountry(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomLocale19setAttributeCountryERK7QString', a,
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
    Notes what was given, for Qt's 'DomLocale::DomLocale()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domlocale.html#DomLocale
    """
    #  DomLocale::DomLocale()
    self._noteCreation(DomLocale, lambda: Rituals.call(
        'ritual_ZN9DomLocaleC1Ev',
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

  def clearAttributeLanguage(self) -> None:
    """
    Calls Qt's 'void DomLocale::clearAttributeLanguage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlocale.html#clearAttributeLanguage
    """
    #  void DomLocale::clearAttributeLanguage()
    self.uglySide.call('ritual_ZN9DomLocale22clearAttributeLanguageEv')

  def clearAttributeCountry(self) -> None:
    """
    Calls Qt's 'void DomLocale::clearAttributeCountry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlocale.html#clearAttributeCountry
    """
    #  void DomLocale::clearAttributeCountry()
    self.uglySide.call('ritual_ZN9DomLocale21clearAttributeCountryEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomLocale::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomLocale.read' has no cute function yet. Qt's 'void "
        "DomLocale::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomLocale::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomLocale.write' has no cute function yet. Qt's 'void "
        "DomLocale::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
