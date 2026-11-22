"""
QUndoCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qundostack.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUndoCommand(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUndoCommand: a plain Python object standing in front
  of one C++ QUndoCommand.

  What exists
  -----------

  Every function of Qt's QUndoCommand that has a ritual and that Python can
  call so far, 11 names in all: 'undo', 'redo', 'text', 'actionText',
  'setText', 'isObsolete', 'setObsolete', 'id', 'mergeWith', 'childCount',
  'child'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUndoCommand::~QUndoCommand()': the destructor: Python never
    removes a C++ QUndoCommand.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QUndoCommand is created at the first use, not by
    'QUndoCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUndoCommand.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUndoCommand'

  #  A C++ QUndoCommand Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUndoCommand'

  #  The functions Qt calls itself that QUndoCommand is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'undo': (
          ('_ZN12QUndoCommand4undoEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'redo': (
          ('_ZN12QUndoCommand4redoEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'id': (
          ('_ZNK12QUndoCommand2idEv',
           ('int', 'number', ''),
           ()),
      ),
      'mergeWith': (
          ('_ZN12QUndoCommand9mergeWithEPKS_',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QUndoCommand'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString QUndoCommand::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoCommand::text() const
    return self.uglySide.call('ritual_ZNK12QUndoCommand4textEv')

  def actionText(self) -> str:
    """
    Calls Qt's 'QString QUndoCommand::actionText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#actionText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoCommand::actionText() const
    return self.uglySide.call('ritual_ZNK12QUndoCommand10actionTextEv')

  def isObsolete(self) -> bool:
    """
    Calls Qt's 'bool QUndoCommand::isObsolete() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#isObsolete
    """
    #  bool QUndoCommand::isObsolete() const
    return self.uglySide.call('ritual_ZNK12QUndoCommand10isObsoleteEv')

  def id(self) -> int:
    """
    Calls Qt's 'int QUndoCommand::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#id
    """
    #  int QUndoCommand::id() const
    ritual = 'ritual_ZNK12QUndoCommand2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QUndoCommand2idEv'
    return self.uglySide.call(ritual)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QUndoCommand::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#childCount
    """
    #  int QUndoCommand::childCount() const
    return self.uglySide.call('ritual_ZNK12QUndoCommand10childCountEv')

  @overload(int)
  def child(self, index: int) -> Optional[QUndoCommand]:
    """
    Calls Qt's 'const QUndoCommand *QUndoCommand::child(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#child

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QUndoCommand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QUndoCommand *QUndoCommand::child(int index) const
    address = self.uglySide.call('ritual_ZNK12QUndoCommand5childEi', index)
    return QUndoCommand._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QUndoCommand::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUndoCommand::setText(const QString &text)
    self.uglySide.call('ritual_ZN12QUndoCommand7setTextERK7QString', text)

  @overload(bool)
  def setObsolete(self, obsolete: bool) -> None:
    """
    Calls Qt's 'void QUndoCommand::setObsolete(bool obsolete)'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#setObsolete

    Parameters
    ----------

    obsolete : bool
      Passed on as it is.
    """
    #  void QUndoCommand::setObsolete(bool obsolete)
    self.uglySide.call('ritual_ZN12QUndoCommand11setObsoleteEb', obsolete)

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
  @overload(THIS)
  @overload(NoneType)
  def __init__(self, parent: Optional[QUndoCommand] = None) -> None:
    """
    Notes what was given, for Qt's 'QUndoCommand::QUndoCommand(QUndoCommand
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#QUndoCommand

    Parameters
    ----------

    parent : Optional[QUndoCommand]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUndoCommand::QUndoCommand(QUndoCommand *parent)
    self._noteCreation(QUndoCommand, lambda: Rituals.call(
        'ritual_ZN12QUndoCommandC1EPS_', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, THIS)
  @overload(str, NoneType)
  def __init__(
      self,
      text: str,
      parent: Optional[QUndoCommand] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QUndoCommand::QUndoCommand(const QString
    &text, QUndoCommand *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#QUndoCommand

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QUndoCommand]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUndoCommand::QUndoCommand(const QString &text, QUndoCommand *parent)
    self._noteCreation(QUndoCommand, lambda: Rituals.call(
        'ritual_ZN12QUndoCommandC1ERK7QStringPS_',
        text, self._addressOf(parent),
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

  def undo(self) -> None:
    """
    Calls Qt's 'void QUndoCommand::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#undo
    """
    #  void QUndoCommand::undo()
    ritual = 'ritual_ZN12QUndoCommand4undoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QUndoCommand4undoEv'
    self.uglySide.call(ritual)

  def redo(self) -> None:
    """
    Calls Qt's 'void QUndoCommand::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#redo
    """
    #  void QUndoCommand::redo()
    ritual = 'ritual_ZN12QUndoCommand4redoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QUndoCommand4redoEv'
    self.uglySide.call(ritual)

  @overload(THIS)
  @overload(NoneType)
  def mergeWith(self, other: Optional[QUndoCommand]) -> bool:
    """
    Calls Qt's 'bool QUndoCommand::mergeWith(const QUndoCommand *other)'.

    Qt's own words: https://doc.qt.io/qt-6/qundocommand.html#mergeWith

    Parameters
    ----------

    other : Optional[QUndoCommand]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QUndoCommand::mergeWith(const QUndoCommand *other)
    ritual = 'ritual_ZN12QUndoCommand9mergeWithEPKS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QUndoCommand9mergeWithEPKS_'
    return self.uglySide.call(ritual, self._addressOf(other))
