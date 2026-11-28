"""
QtFontFoundry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QtFontFoundry to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QtFontStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QtFontFoundry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtFontFoundry: a plain Python object standing in
  front of one C++ QtFontFoundry.

  C++ hands a QtFontFoundry around as a copy, so every C++ QtFontFoundry
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtFontFoundry that has a ritual and that Python can
  call so far, 1 name in all: 'style'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtFontFoundry::~QtFontFoundry()': the destructor: Python removes
    its C++ QtFontFoundry by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtFontFoundry is created at the first use, not by
    'QtFontFoundry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtFontFoundry back gives a copy the ritual made for
    Python, in a new cute QtFontFoundry.
  """

  #  The enums Qt writes inside QtFontFoundry, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class StyleRetrievalFlags(CuteNum):
    """
    The enum 'QtFontFoundry::StyleRetrievalFlags' of Qt, with the 4 names Qt
    gives in it.
    """

    NoRetrievalFlags = Kee[int](0)
    AddWhenMissing = Kee[int](1)
    MatchAllProperties = Kee[int](2)
    AllRetrievalFlags = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtFontFoundry'

  #  Qt's '~QtFontFoundry()'. Naming it makes this a value class: Python owns
  #  every C++ QtFontFoundry behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QtFontFoundryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QtFontFoundry::QtFontFoundry(const
    QString &n)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtfontfoundry.html#QtFontFoundry

    Parameters
    ----------

    n : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QtFontFoundry::QtFontFoundry(const QString &n)
    self._noteCreation(QtFontFoundry, lambda: Rituals.call(
        'ritual_ZN13QtFontFoundryC1ERK7QString', n,
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

  @overload(QtFontStyle.Key)
  @overload(QtFontStyle.Key, str)
  @overload(QtFontStyle.Key, str, StyleRetrievalFlags)
  def style(
      self,
      a0: QtFontStyle.Key,
      a1: str = '',
      flags: StyleRetrievalFlags = StyleRetrievalFlags.NoRetrievalFlags,
  ) -> Optional[QtFontStyle]:
    """
    Calls Qt's 'QtFontStyle *QtFontFoundry::style(const QtFontStyle::Key &a0,
    const QString &a1, StyleRetrievalFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qtfontfoundry.html#style

    Parameters
    ----------

    a0 : QtFontStyle.Key
      Passed on as a value: Qt reads the C++ QtFontStyle::Key, which stays
      Python's own.

    a1 : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    flags : StyleRetrievalFlags
      Passed on as its number. May be left out, as in Qt: it is then
      StyleRetrievalFlags.NoRetrievalFlags.

    Returns
    -------

    Optional[QtFontStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtFontStyle *QtFontFoundry::style(const QtFontStyle::Key &a0, const
    #      QString &a1, StyleRetrievalFlags flags)
    address = self.uglySide.call(
        'ritual_ZN13QtFontFoundry5styleERKN11QtFontStyle3KeyERK7QStringNS_1'
        '9StyleRetrievalFlagsE',
        self._valueOf(a0), a1, flags.value,
    )
    return QtFontStyle._cuteAt(address)
