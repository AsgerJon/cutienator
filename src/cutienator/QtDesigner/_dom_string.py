"""
DomString binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomString to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomString(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomString: a plain Python object standing in front of
  one C++ DomString.

  What exists
  -----------

  Every function of Qt's DomString that has a ritual and that Python can call
  so far, 18 names in all: 'text', 'setText', 'hasAttributeNotr',
  'attributeNotr', 'setAttributeNotr', 'clearAttributeNotr',
  'hasAttributeComment', 'attributeComment', 'setAttributeComment',
  'clearAttributeComment', 'hasAttributeExtraComment',
  'attributeExtraComment', 'setAttributeExtraComment',
  'clearAttributeExtraComment', 'hasAttributeId', 'attributeId',
  'setAttributeId', 'clearAttributeId'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomString::~DomString()': the destructor: Python never removes a
    C++ DomString.
  - Qt's 'void DomString::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomString::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomString is created at the first use, not by 'DomString(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomString.
  - Each name of Qt's DomString that has no cute function yet, 'read',
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
  __qt_class__ = 'DomString'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString DomString::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomString::text() const
    return self.uglySide.call('ritual_ZNK9DomString4textEv')

  def hasAttributeNotr(self) -> bool:
    """
    Calls Qt's 'bool DomString::hasAttributeNotr() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#hasAttributeNotr
    """
    #  bool DomString::hasAttributeNotr() const
    return self.uglySide.call('ritual_ZNK9DomString16hasAttributeNotrEv')

  def attributeNotr(self) -> str:
    """
    Calls Qt's 'QString DomString::attributeNotr() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#attributeNotr

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomString::attributeNotr() const
    return self.uglySide.call('ritual_ZNK9DomString13attributeNotrEv')

  def hasAttributeComment(self) -> bool:
    """
    Calls Qt's 'bool DomString::hasAttributeComment() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#hasAttributeComment
    """
    #  bool DomString::hasAttributeComment() const
    return self.uglySide.call('ritual_ZNK9DomString19hasAttributeCommentEv')

  def attributeComment(self) -> str:
    """
    Calls Qt's 'QString DomString::attributeComment() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#attributeComment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomString::attributeComment() const
    return self.uglySide.call('ritual_ZNK9DomString16attributeCommentEv')

  def hasAttributeExtraComment(self) -> bool:
    """
    Calls Qt's 'bool DomString::hasAttributeExtraComment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstring.html#hasAttributeExtraComment
    """
    #  bool DomString::hasAttributeExtraComment() const
    return self.uglySide.call(
        'ritual_ZNK9DomString24hasAttributeExtraCommentEv',
    )

  def attributeExtraComment(self) -> str:
    """
    Calls Qt's 'QString DomString::attributeExtraComment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstring.html#attributeExtraComment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomString::attributeExtraComment() const
    return self.uglySide.call(
        'ritual_ZNK9DomString21attributeExtraCommentEv',
    )

  def hasAttributeId(self) -> bool:
    """
    Calls Qt's 'bool DomString::hasAttributeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#hasAttributeId
    """
    #  bool DomString::hasAttributeId() const
    return self.uglySide.call('ritual_ZNK9DomString14hasAttributeIdEv')

  def attributeId(self) -> str:
    """
    Calls Qt's 'QString DomString::attributeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#attributeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomString::attributeId() const
    return self.uglySide.call('ritual_ZNK9DomString11attributeIdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, s: str) -> None:
    """
    Calls Qt's 'void DomString::setText(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#setText

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomString::setText(const QString &s)
    self.uglySide.call('ritual_ZN9DomString7setTextERK7QString', s)

  @overload(str)
  def setAttributeNotr(self, a: str) -> None:
    """
    Calls Qt's 'void DomString::setAttributeNotr(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#setAttributeNotr

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomString::setAttributeNotr(const QString &a)
    self.uglySide.call('ritual_ZN9DomString16setAttributeNotrERK7QString', a)

  @overload(str)
  def setAttributeComment(self, a: str) -> None:
    """
    Calls Qt's 'void DomString::setAttributeComment(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#setAttributeComment

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomString::setAttributeComment(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomString19setAttributeCommentERK7QString', a,
    )

  @overload(str)
  def setAttributeExtraComment(self, a: str) -> None:
    """
    Calls Qt's 'void DomString::setAttributeExtraComment(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstring.html#setAttributeExtraComment

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomString::setAttributeExtraComment(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomString24setAttributeExtraCommentERK7QString', a,
    )

  @overload(str)
  def setAttributeId(self, a: str) -> None:
    """
    Calls Qt's 'void DomString::setAttributeId(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#setAttributeId

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomString::setAttributeId(const QString &a)
    self.uglySide.call('ritual_ZN9DomString14setAttributeIdERK7QString', a)

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
    Notes what was given, for Qt's 'DomString::DomString()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#DomString
    """
    #  DomString::DomString()
    self._noteCreation(DomString, lambda: Rituals.call(
        'ritual_ZN9DomStringC1Ev',
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

  def clearAttributeNotr(self) -> None:
    """
    Calls Qt's 'void DomString::clearAttributeNotr()'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#clearAttributeNotr
    """
    #  void DomString::clearAttributeNotr()
    self.uglySide.call('ritual_ZN9DomString18clearAttributeNotrEv')

  def clearAttributeComment(self) -> None:
    """
    Calls Qt's 'void DomString::clearAttributeComment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstring.html#clearAttributeComment
    """
    #  void DomString::clearAttributeComment()
    self.uglySide.call('ritual_ZN9DomString21clearAttributeCommentEv')

  def clearAttributeExtraComment(self) -> None:
    """
    Calls Qt's 'void DomString::clearAttributeExtraComment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstring.html#clearAttributeExtraComment
    """
    #  void DomString::clearAttributeExtraComment()
    self.uglySide.call('ritual_ZN9DomString26clearAttributeExtraCommentEv')

  def clearAttributeId(self) -> None:
    """
    Calls Qt's 'void DomString::clearAttributeId()'.

    Qt's own words: https://doc.qt.io/qt-6/domstring.html#clearAttributeId
    """
    #  void DomString::clearAttributeId()
    self.uglySide.call('ritual_ZN9DomString16clearAttributeIdEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomString::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomString.read' has no cute function yet. Qt's 'void "
        "DomString::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomString::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomString.write' has no cute function yet. Qt's 'void "
        "DomString::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
