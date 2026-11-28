"""
QSSGCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGCommand to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QSSGCommand(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGCommand: a plain Python object standing in front
  of one C++ QSSGCommand.

  C++ hands a QSSGCommand around as a copy, so every C++ QSSGCommand behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGCommand that has a ritual and that Python can
  call so far, 2 names in all: 'typeAsString', 'debugString'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGCommand::QSSGCommand(CommandType inType)': names the enum
    'CommandType', whose class cannot be named here.
  - Qt's 'QSSGCommand::~QSSGCommand()': the destructor: Python removes its
    C++ QSSGCommand by it, and has no other use for it.
  - Qt's 'void QSSGCommand::addDebug(QDebug &stream) const': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSSGCommand is created at the first use, not by
    'QSSGCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGCommand back gives a copy the ritual made for
    Python, in a new cute QSSGCommand.
  - Each name of Qt's QSSGCommand that has no cute function yet, '__init__',
    'addDebug', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QSSGCommand'

  #  Qt's '~QSSGCommand()'. Naming it makes this a value class: Python owns
  #  every C++ QSSGCommand behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QSSGCommandD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def typeAsString(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QSSGCommand::typeAsString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgcommand.html#typeAsString

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QSSGCommand::typeAsString() const
    chars = self.uglySide.call('ritual_ZNK11QSSGCommand12typeAsStringEv')
    return None if chars is None else chars.decode()

  def debugString(self) -> str:
    """
    Calls Qt's 'QString QSSGCommand::debugString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgcommand.html#debugString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSSGCommand::debugString() const
    return self.uglySide.call('ritual_ZNK11QSSGCommand11debugStringEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSSGCommand::QSSGCommand(CommandType inType)': names the enum
    'CommandType', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGCommand.__init__' has no cute function yet. Qt's "
        "'QSSGCommand::QSSGCommand(CommandType inType)': names the enum "
        "'CommandType', whose class cannot be named here.")

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

  @staticmethod
  def addDebug(*__, **_) -> Never:
    """
    Qt's 'void QSSGCommand::addDebug(QDebug &stream) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGCommand.addDebug' has no cute function yet. Qt's 'void "
        "QSSGCommand::addDebug(QDebug &stream) const': takes a type Python "
        "has no way to hand over yet.")
