"""
DomStringList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomStringList to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomStringList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomStringList: a plain Python object standing in
  front of one C++ DomStringList.

  What exists
  -----------

  Every function of Qt's DomStringList that has a ritual and that Python can
  call so far, 18 names in all: 'hasAttributeNotr', 'attributeNotr',
  'setAttributeNotr', 'clearAttributeNotr', 'hasAttributeComment',
  'attributeComment', 'setAttributeComment', 'clearAttributeComment',
  'hasAttributeExtraComment', 'attributeExtraComment',
  'setAttributeExtraComment', 'clearAttributeExtraComment', 'hasAttributeId',
  'attributeId', 'setAttributeId', 'clearAttributeId', 'elementString',
  'setElementString'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomStringList::~DomStringList()': the destructor: Python never
    removes a C++ DomStringList.
  - Qt's 'void DomStringList::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomStringList::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomStringList is created at the first use, not by
    'DomStringList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomStringList.
  - Each name of Qt's DomStringList that has no cute function yet, 'read',
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
  __qt_class__ = 'DomStringList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeNotr(self) -> bool:
    """
    Calls Qt's 'bool DomStringList::hasAttributeNotr() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#hasAttributeNotr
    """
    #  bool DomStringList::hasAttributeNotr() const
    return self.uglySide.call(
        'ritual_ZNK13DomStringList16hasAttributeNotrEv',
    )

  def attributeNotr(self) -> str:
    """
    Calls Qt's 'QString DomStringList::attributeNotr() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstringlist.html#attributeNotr

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomStringList::attributeNotr() const
    return self.uglySide.call('ritual_ZNK13DomStringList13attributeNotrEv')

  def hasAttributeComment(self) -> bool:
    """
    Calls Qt's 'bool DomStringList::hasAttributeComment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#hasAttributeComment
    """
    #  bool DomStringList::hasAttributeComment() const
    return self.uglySide.call(
        'ritual_ZNK13DomStringList19hasAttributeCommentEv',
    )

  def attributeComment(self) -> str:
    """
    Calls Qt's 'QString DomStringList::attributeComment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#attributeComment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomStringList::attributeComment() const
    return self.uglySide.call(
        'ritual_ZNK13DomStringList16attributeCommentEv',
    )

  def hasAttributeExtraComment(self) -> bool:
    """
    Calls Qt's 'bool DomStringList::hasAttributeExtraComment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#hasAttributeExtraComment
    """
    #  bool DomStringList::hasAttributeExtraComment() const
    return self.uglySide.call(
        'ritual_ZNK13DomStringList24hasAttributeExtraCommentEv',
    )

  def attributeExtraComment(self) -> str:
    """
    Calls Qt's 'QString DomStringList::attributeExtraComment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#attributeExtraComment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomStringList::attributeExtraComment() const
    return self.uglySide.call(
        'ritual_ZNK13DomStringList21attributeExtraCommentEv',
    )

  def hasAttributeId(self) -> bool:
    """
    Calls Qt's 'bool DomStringList::hasAttributeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstringlist.html#hasAttributeId
    """
    #  bool DomStringList::hasAttributeId() const
    return self.uglySide.call('ritual_ZNK13DomStringList14hasAttributeIdEv')

  def attributeId(self) -> str:
    """
    Calls Qt's 'QString DomStringList::attributeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstringlist.html#attributeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomStringList::attributeId() const
    return self.uglySide.call('ritual_ZNK13DomStringList11attributeIdEv')

  def elementString(self) -> QStringList:
    """
    Calls Qt's 'QStringList DomStringList::elementString() const'.

    Qt's own words: https://doc.qt.io/qt-6/domstringlist.html#elementString

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList DomStringList::elementString() const
    address = self.uglySide.call(
        'ritual_ZNK13DomStringList13elementStringEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeNotr(self, a: str) -> None:
    """
    Calls Qt's 'void DomStringList::setAttributeNotr(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#setAttributeNotr

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomStringList::setAttributeNotr(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomStringList16setAttributeNotrERK7QString', a,
    )

  @overload(str)
  def setAttributeComment(self, a: str) -> None:
    """
    Calls Qt's 'void DomStringList::setAttributeComment(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#setAttributeComment

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomStringList::setAttributeComment(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomStringList19setAttributeCommentERK7QString', a,
    )

  @overload(str)
  def setAttributeExtraComment(self, a: str) -> None:
    """
    Calls Qt's 'void DomStringList::setAttributeExtraComment(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#setAttributeExtraComment

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomStringList::setAttributeExtraComment(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomStringList24setAttributeExtraCommentERK7QString', a,
    )

  @overload(str)
  def setAttributeId(self, a: str) -> None:
    """
    Calls Qt's 'void DomStringList::setAttributeId(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domstringlist.html#setAttributeId

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomStringList::setAttributeId(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomStringList14setAttributeIdERK7QString', a,
    )

  @overload(QStringList)
  def setElementString(self, a: QStringList) -> None:
    """
    Calls Qt's 'void DomStringList::setElementString(const QStringList &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#setElementString

    Parameters
    ----------

    a : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomStringList::setElementString(const QStringList &a)
    self.uglySide.call(
        'ritual_ZN13DomStringList16setElementStringERK5QListI7QStringE',
        self._valueOf(a),
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
    Notes what was given, for Qt's 'DomStringList::DomStringList()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domstringlist.html#DomStringList
    """
    #  DomStringList::DomStringList()
    self._noteCreation(DomStringList, lambda: Rituals.call(
        'ritual_ZN13DomStringListC1Ev',
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
    Calls Qt's 'void DomStringList::clearAttributeNotr()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#clearAttributeNotr
    """
    #  void DomStringList::clearAttributeNotr()
    self.uglySide.call('ritual_ZN13DomStringList18clearAttributeNotrEv')

  def clearAttributeComment(self) -> None:
    """
    Calls Qt's 'void DomStringList::clearAttributeComment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#clearAttributeComment
    """
    #  void DomStringList::clearAttributeComment()
    self.uglySide.call('ritual_ZN13DomStringList21clearAttributeCommentEv')

  def clearAttributeExtraComment(self) -> None:
    """
    Calls Qt's 'void DomStringList::clearAttributeExtraComment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#clearAttributeExtraComment
    """
    #  void DomStringList::clearAttributeExtraComment()
    self.uglySide.call(
        'ritual_ZN13DomStringList26clearAttributeExtraCommentEv',
    )

  def clearAttributeId(self) -> None:
    """
    Calls Qt's 'void DomStringList::clearAttributeId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domstringlist.html#clearAttributeId
    """
    #  void DomStringList::clearAttributeId()
    self.uglySide.call('ritual_ZN13DomStringList16clearAttributeIdEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomStringList::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomStringList.read' has no cute function yet. Qt's 'void "
        "DomStringList::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomStringList::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomStringList.write' has no cute function yet. Qt's 'void "
        "DomStringList::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
