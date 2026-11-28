"""
DomUrl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomUrl to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomString = WAIT['DomString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomUrl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomUrl: a plain Python object standing in front of
  one C++ DomUrl.

  What exists
  -----------

  Every function of Qt's DomUrl that has a ritual and that Python can call so
  far, 5 names in all: 'elementString', 'takeElementString',
  'setElementString', 'hasElementString', 'clearElementString'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomUrl::~DomUrl()': the destructor: Python never removes a C++
    DomUrl.
  - Qt's 'void DomUrl::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomUrl::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomUrl is created at the first use, not by 'DomUrl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomUrl.
  - Each name of Qt's DomUrl that has no cute function yet, 'read', 'write',
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
  __qt_class__ = 'DomUrl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementString(self) -> Optional[DomString]:
    """
    Calls Qt's 'DomString *DomUrl::elementString() const'.

    Qt's own words: https://doc.qt.io/qt-6/domurl.html#elementString

    Returns
    -------

    Optional[DomString]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomString *DomUrl::elementString() const
    address = self.uglySide.call('ritual_ZNK6DomUrl13elementStringEv')
    from . import DomString
    return DomString._cuteAt(address)

  def hasElementString(self) -> bool:
    """
    Calls Qt's 'bool DomUrl::hasElementString() const'.

    Qt's own words: https://doc.qt.io/qt-6/domurl.html#hasElementString
    """
    #  bool DomUrl::hasElementString() const
    return self.uglySide.call('ritual_ZNK6DomUrl16hasElementStringEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DomString)
  @overload(NoneType)
  def setElementString(self, a: Optional[DomString]) -> None:
    """
    Calls Qt's 'void DomUrl::setElementString(DomString *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domurl.html#setElementString

    Parameters
    ----------

    a : Optional[DomString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomUrl::setElementString(DomString *a)
    self.uglySide.call(
        'ritual_ZN6DomUrl16setElementStringEP9DomString', self._addressOf(a),
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
    Notes what was given, for Qt's 'DomUrl::DomUrl()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/domurl.html#DomUrl
    """
    #  DomUrl::DomUrl()
    self._noteCreation(DomUrl, lambda: Rituals.call('ritual_ZN6DomUrlC1Ev'))

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

  def takeElementString(self) -> Optional[DomString]:
    """
    Calls Qt's 'DomString *DomUrl::takeElementString()'.

    Qt's own words: https://doc.qt.io/qt-6/domurl.html#takeElementString

    Returns
    -------

    Optional[DomString]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomString *DomUrl::takeElementString()
    address = self.uglySide.call('ritual_ZN6DomUrl17takeElementStringEv')
    from . import DomString
    return DomString._cuteAt(address)

  def clearElementString(self) -> None:
    """
    Calls Qt's 'void DomUrl::clearElementString()'.

    Qt's own words: https://doc.qt.io/qt-6/domurl.html#clearElementString
    """
    #  void DomUrl::clearElementString()
    self.uglySide.call('ritual_ZN6DomUrl18clearElementStringEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomUrl::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomUrl.read' has no cute function yet. Qt's 'void "
        "DomUrl::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomUrl::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomUrl.write' has no cute function yet. Qt's 'void "
        "DomUrl::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
