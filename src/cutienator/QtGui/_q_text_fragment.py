"""
QTextFragment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QTextCharFormat


class QTextFragment(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextFragment: a plain Python object standing in
  front of one C++ QTextFragment.

  C++ hands a QTextFragment around as a copy, so every C++ QTextFragment
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextFragment that has a ritual and that Python can
  call so far, 7 names in all: 'isValid', 'position', 'length', 'contains',
  'charFormat', 'charFormatIndex', 'text'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QTextFragment::operator==(const QTextFragment &o) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextFragment::operator!=(const QTextFragment &o) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextFragment::operator<(const QTextFragment &o) const': an
    operator, which is not reflected yet.
  - Qt's 'QTextFragment::~QTextFragment()': the destructor: Python removes
    its C++ QTextFragment by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QTextFragment is created at the first use, not by
    'QTextFragment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextFragment back gives a copy the ritual made for
    Python, in a new cute QTextFragment.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextFragment'

  #  Qt's '~QTextFragment()'. Naming it makes this a value class: Python owns
  #  every C++ QTextFragment behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QTextFragmentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextFragment::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#isValid
    """
    #  bool QTextFragment::isValid() const
    return self.uglySide.call('ritual_ZNK13QTextFragment7isValidEv')

  def position(self) -> int:
    """
    Calls Qt's 'int QTextFragment::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#position
    """
    #  int QTextFragment::position() const
    return self.uglySide.call('ritual_ZNK13QTextFragment8positionEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QTextFragment::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#length
    """
    #  int QTextFragment::length() const
    return self.uglySide.call('ritual_ZNK13QTextFragment6lengthEv')

  @overload(int)
  def contains(self, position: int) -> bool:
    """
    Calls Qt's 'bool QTextFragment::contains(int position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#contains

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  bool QTextFragment::contains(int position) const
    return self.uglySide.call(
        'ritual_ZNK13QTextFragment8containsEi', position,
    )

  def charFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextFragment::charFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#charFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextFragment::charFormat() const
    address = self.uglySide.call('ritual_ZNK13QTextFragment10charFormatEv')
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def charFormatIndex(self) -> int:
    """
    Calls Qt's 'int QTextFragment::charFormatIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#charFormatIndex
    """
    #  int QTextFragment::charFormatIndex() const
    return self.uglySide.call('ritual_ZNK13QTextFragment15charFormatIndexEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QTextFragment::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextFragment::text() const
    return self.uglySide.call('ritual_ZNK13QTextFragment4textEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTextFragment::QTextFragment()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#QTextFragment
    """
    #  QTextFragment::QTextFragment()
    self._noteCreation(QTextFragment, lambda: Rituals.call(
        'ritual_ZN13QTextFragmentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, o: QTextFragment) -> None:
    """
    Notes what was given, for Qt's 'QTextFragment::QTextFragment(const
    QTextFragment &o)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextfragment.html#QTextFragment

    Parameters
    ----------

    o : QTextFragment
      Passed on as a value: Qt reads the C++ QTextFragment, which stays
      Python's own.
    """
    #  QTextFragment::QTextFragment(const QTextFragment &o)
    self._noteCreation(QTextFragment, lambda: Rituals.call(
        'ritual_ZN13QTextFragmentC1ERKS_', self._valueOf(o),
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
