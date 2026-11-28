"""
QtFontFamily binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QtFontFamily to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QtFontFoundry


class QtFontFamily(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtFontFamily: a plain Python object standing in front
  of one C++ QtFontFamily.

  C++ hands a QtFontFamily around as a copy, so every C++ QtFontFamily behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtFontFamily that has a ritual and that Python can
  call so far, 3 names in all: 'matchesFamilyName', 'foundry',
  'ensurePopulated'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtFontFamily::~QtFontFamily()': the destructor: Python removes its
    C++ QtFontFamily by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtFontFamily is created at the first use, not by
    'QtFontFamily(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtFontFamily back gives a copy the ritual made for
    Python, in a new cute QtFontFamily.
  """

  #  The enums Qt writes inside QtFontFamily, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class WritingSystemStatus(CuteNum):
    """
    The enum 'QtFontFamily::WritingSystemStatus' of Qt, with the 4 names Qt
    gives in it.
    """

    Unknown = Kee[int](0)
    Supported = Kee[int](1)
    UnsupportedFT = Kee[int](2)
    Unsupported = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtFontFamily'

  #  Qt's '~QtFontFamily()'. Naming it makes this a value class: Python owns
  #  every C++ QtFontFamily behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QtFontFamilyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def matchesFamilyName(self, familyName: str) -> bool:
    """
    Calls Qt's 'bool QtFontFamily::matchesFamilyName(const QString
    &familyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtfontfamily.html#matchesFamilyName

    Parameters
    ----------

    familyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QtFontFamily::matchesFamilyName(const QString &familyName) const
    return self.uglySide.call(
        'ritual_ZNK12QtFontFamily17matchesFamilyNameERK7QString', familyName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __init__(self, n: str) -> None:
    """
    Notes what was given, for Qt's 'QtFontFamily::QtFontFamily(const QString
    &n)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtfontfamily.html#QtFontFamily

    Parameters
    ----------

    n : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QtFontFamily::QtFontFamily(const QString &n)
    self._noteCreation(QtFontFamily, lambda: Rituals.call(
        'ritual_ZN12QtFontFamilyC1ERK7QString', n,
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

  @overload(str)
  @overload(str, bool)
  def foundry(self, f: str, a1: bool = False) -> Optional[QtFontFoundry]:
    """
    Calls Qt's 'QtFontFoundry *QtFontFamily::foundry(const QString &f, bool
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qtfontfamily.html#foundry

    Parameters
    ----------

    f : str
      Passed on as it is: a QString is made of it for the call.

    a1 : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QtFontFoundry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtFontFoundry *QtFontFamily::foundry(const QString &f, bool a1)
    address = self.uglySide.call(
        'ritual_ZN12QtFontFamily7foundryERK7QStringb', f, a1,
    )
    from . import QtFontFoundry
    return QtFontFoundry._cuteAt(address)

  def ensurePopulated(self) -> bool:
    """
    Calls Qt's 'bool QtFontFamily::ensurePopulated()'.

    Qt's own words: https://doc.qt.io/qt-6/qtfontfamily.html#ensurePopulated
    """
    #  bool QtFontFamily::ensurePopulated()
    return self.uglySide.call('ritual_ZN12QtFontFamily15ensurePopulatedEv')
