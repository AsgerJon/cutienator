"""
QTypeRevision binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtyperevision.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QTypeRevision(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTypeRevision: a plain Python object standing in
  front of one C++ QTypeRevision.

  C++ hands a QTypeRevision around as a copy, so every C++ QTypeRevision
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTypeRevision that has a ritual and that Python can
  call so far, 6 names in all: 'zero', 'hasMajorVersion', 'majorVersion',
  'hasMinorVersion', 'minorVersion', 'isValid'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTypeRevision::~QTypeRevision()': the destructor: Python removes
    its C++ QTypeRevision by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 15 functions Qt declares: 6 a template; 1 private.

  What to expect
  --------------

  - The C++ QTypeRevision is created at the first use, not by
    'QTypeRevision(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTypeRevision back gives a copy the ritual made for
    Python, in a new cute QTypeRevision.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def zero() -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QTypeRevision::zero()'.

    Qt's own words: https://doc.qt.io/qt-6/qtyperevision.html#zero

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QTypeRevision::zero()
    address = Rituals.call('ritual_ZN13QTypeRevision4zeroEv')
    return QTypeRevision._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTypeRevision'

  #  Qt's '~QTypeRevision()'. Naming it makes this a value class: Python owns
  #  every C++ QTypeRevision behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QTypeRevisionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasMajorVersion(self) -> bool:
    """
    Calls Qt's 'bool QTypeRevision::hasMajorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtyperevision.html#hasMajorVersion
    """
    #  bool QTypeRevision::hasMajorVersion() const
    return self.uglySide.call('ritual_ZNK13QTypeRevision15hasMajorVersionEv')

  def majorVersion(self) -> int:
    """
    Calls Qt's 'quint8 QTypeRevision::majorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtyperevision.html#majorVersion
    """
    #  quint8 QTypeRevision::majorVersion() const
    return self.uglySide.call('ritual_ZNK13QTypeRevision12majorVersionEv')

  def hasMinorVersion(self) -> bool:
    """
    Calls Qt's 'bool QTypeRevision::hasMinorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtyperevision.html#hasMinorVersion
    """
    #  bool QTypeRevision::hasMinorVersion() const
    return self.uglySide.call('ritual_ZNK13QTypeRevision15hasMinorVersionEv')

  def minorVersion(self) -> int:
    """
    Calls Qt's 'quint8 QTypeRevision::minorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtyperevision.html#minorVersion
    """
    #  quint8 QTypeRevision::minorVersion() const
    return self.uglySide.call('ritual_ZNK13QTypeRevision12minorVersionEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTypeRevision::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtyperevision.html#isValid
    """
    #  bool QTypeRevision::isValid() const
    return self.uglySide.call('ritual_ZNK13QTypeRevision7isValidEv')

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
    Notes what was given, for Qt's 'QTypeRevision::QTypeRevision()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtyperevision.html#QTypeRevision
    """
    #  QTypeRevision::QTypeRevision()
    self._noteCreation(QTypeRevision, lambda: Rituals.call(
        'ritual_ZN13QTypeRevisionC1Ev',
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
