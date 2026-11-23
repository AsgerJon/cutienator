"""
QUndoStack binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qundostack.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAction, QUndoCommand
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUndoCommand = WAIT['QUndoCommand']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUndoStack(QObject):
  """
  The cute side of Qt's QUndoStack: a plain Python object standing in front
  of one C++ QUndoStack.

  It is built on the cute 'QObject', as Qt's QUndoStack is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QUndoStack that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'clear', 'push',
  'canUndo', 'canRedo', 'undoText', 'redoText', 'count', 'index', 'text',
  'createUndoAction', 'createRedoAction', 'isActive', 'isClean',
  'cleanIndex', 'beginMacro', 'endMacro', 'setUndoLimit', 'undoLimit',
  'command', 'setClean', 'resetClean', 'setIndex', 'undo', 'redo',
  'setActive'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUndoStack::~QUndoStack()': the destructor: Python never removes a
    C++ QUndoStack.

  What has no ritual
  ------------------

  14 of the 43 functions Qt declares: 6 a signal; 4 takes or gives a type
  that cannot be passed yet; 2 forbidden; 1 a template; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QUndoStack is created at the first use, not by 'QUndoStack(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUndoStack.
  - Qt tells when it has removed the C++ QUndoStack. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QUndoStack::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoStack::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QUndoStack2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUndoStack'

  #  A C++ QUndoStack Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUndoStack'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QUndoStack::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QUndoStack::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QUndoStack10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def canUndo(self) -> bool:
    """
    Calls Qt's 'bool QUndoStack::canUndo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#canUndo
    """
    #  bool QUndoStack::canUndo() const
    return self.uglySide.call('ritual_ZNK10QUndoStack7canUndoEv')

  def canRedo(self) -> bool:
    """
    Calls Qt's 'bool QUndoStack::canRedo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#canRedo
    """
    #  bool QUndoStack::canRedo() const
    return self.uglySide.call('ritual_ZNK10QUndoStack7canRedoEv')

  def undoText(self) -> str:
    """
    Calls Qt's 'QString QUndoStack::undoText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#undoText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoStack::undoText() const
    return self.uglySide.call('ritual_ZNK10QUndoStack8undoTextEv')

  def redoText(self) -> str:
    """
    Calls Qt's 'QString QUndoStack::redoText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#redoText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoStack::redoText() const
    return self.uglySide.call('ritual_ZNK10QUndoStack8redoTextEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QUndoStack::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#count
    """
    #  int QUndoStack::count() const
    return self.uglySide.call('ritual_ZNK10QUndoStack5countEv')

  def index(self) -> int:
    """
    Calls Qt's 'int QUndoStack::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#index
    """
    #  int QUndoStack::index() const
    return self.uglySide.call('ritual_ZNK10QUndoStack5indexEv')

  @overload(int)
  def text(self, idx: int) -> str:
    """
    Calls Qt's 'QString QUndoStack::text(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#text

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoStack::text(int idx) const
    return self.uglySide.call('ritual_ZNK10QUndoStack4textEi', idx)

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, str)
  @overload(NoneType, str)
  def createUndoAction(
      self,
      parent: Optional[QObject],
      prefix: str = '',
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QUndoStack::createUndoAction(QObject *parent, const
    QString &prefix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#createUndoAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    prefix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QUndoStack::createUndoAction(QObject *parent, const QString
    #      &prefix) const
    address = self.uglySide.call(
        'ritual_ZNK10QUndoStack16createUndoActionEP7QObjectRK7QString',
        self._addressOf(parent, 'QObject'), prefix,
    )
    from . import QAction
    return QAction._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, str)
  @overload(NoneType, str)
  def createRedoAction(
      self,
      parent: Optional[QObject],
      prefix: str = '',
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QUndoStack::createRedoAction(QObject *parent, const
    QString &prefix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#createRedoAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    prefix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QUndoStack::createRedoAction(QObject *parent, const QString
    #      &prefix) const
    address = self.uglySide.call(
        'ritual_ZNK10QUndoStack16createRedoActionEP7QObjectRK7QString',
        self._addressOf(parent, 'QObject'), prefix,
    )
    from . import QAction
    return QAction._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QUndoStack::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#isActive
    """
    #  bool QUndoStack::isActive() const
    return self.uglySide.call('ritual_ZNK10QUndoStack8isActiveEv')

  def isClean(self) -> bool:
    """
    Calls Qt's 'bool QUndoStack::isClean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#isClean
    """
    #  bool QUndoStack::isClean() const
    return self.uglySide.call('ritual_ZNK10QUndoStack7isCleanEv')

  def cleanIndex(self) -> int:
    """
    Calls Qt's 'int QUndoStack::cleanIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#cleanIndex
    """
    #  int QUndoStack::cleanIndex() const
    return self.uglySide.call('ritual_ZNK10QUndoStack10cleanIndexEv')

  def undoLimit(self) -> int:
    """
    Calls Qt's 'int QUndoStack::undoLimit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#undoLimit
    """
    #  int QUndoStack::undoLimit() const
    return self.uglySide.call('ritual_ZNK10QUndoStack9undoLimitEv')

  @overload(int)
  def command(self, index: int) -> Optional[QUndoCommand]:
    """
    Calls Qt's 'const QUndoCommand *QUndoStack::command(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#command

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
    #  const QUndoCommand *QUndoStack::command(int index) const
    address = self.uglySide.call('ritual_ZNK10QUndoStack7commandEi', index)
    from . import QUndoCommand
    return QUndoCommand._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setUndoLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QUndoStack::setUndoLimit(int limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#setUndoLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QUndoStack::setUndoLimit(int limit)
    self.uglySide.call('ritual_ZN10QUndoStack12setUndoLimitEi', limit)

  def setClean(self) -> None:
    """
    Calls Qt's 'void QUndoStack::setClean()'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#setClean
    """
    #  void QUndoStack::setClean()
    self.uglySide.call('ritual_ZN10QUndoStack8setCleanEv')

  @overload(int)
  def setIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QUndoStack::setIndex(int idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#setIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QUndoStack::setIndex(int idx)
    self.uglySide.call('ritual_ZN10QUndoStack8setIndexEi', idx)

  @overload()
  @overload(bool)
  def setActive(self, active: bool = True) -> None:
    """
    Calls Qt's 'void QUndoStack::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QUndoStack::setActive(bool active)
    self.uglySide.call('ritual_ZN10QUndoStack9setActiveEb', active)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QUndoStack::QUndoStack(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#QUndoStack

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUndoStack::QUndoStack(QObject *parent)
    self._noteCreation(QUndoStack, lambda: Rituals.call(
        'ritual_ZN10QUndoStackC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QUndoStack::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#clear
    """
    #  void QUndoStack::clear()
    self.uglySide.call('ritual_ZN10QUndoStack5clearEv')

  @overload(QUndoCommand)
  @overload(NoneType)
  def push(self, cmd: Optional[QUndoCommand]) -> None:
    """
    Calls Qt's 'void QUndoStack::push(QUndoCommand *cmd)'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#push

    Parameters
    ----------

    cmd : Optional[QUndoCommand]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUndoStack::push(QUndoCommand *cmd)
    self.uglySide.call(
        'ritual_ZN10QUndoStack4pushEP12QUndoCommand', self._addressOf(cmd),
    )

  @overload(str)
  def beginMacro(self, text: str) -> None:
    """
    Calls Qt's 'void QUndoStack::beginMacro(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#beginMacro

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUndoStack::beginMacro(const QString &text)
    self.uglySide.call('ritual_ZN10QUndoStack10beginMacroERK7QString', text)

  def endMacro(self) -> None:
    """
    Calls Qt's 'void QUndoStack::endMacro()'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#endMacro
    """
    #  void QUndoStack::endMacro()
    self.uglySide.call('ritual_ZN10QUndoStack8endMacroEv')

  def resetClean(self) -> None:
    """
    Calls Qt's 'void QUndoStack::resetClean()'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#resetClean
    """
    #  void QUndoStack::resetClean()
    self.uglySide.call('ritual_ZN10QUndoStack10resetCleanEv')

  def undo(self) -> None:
    """
    Calls Qt's 'void QUndoStack::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#undo
    """
    #  void QUndoStack::undo()
    self.uglySide.call('ritual_ZN10QUndoStack4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QUndoStack::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qundostack.html#redo
    """
    #  void QUndoStack::redo()
    self.uglySide.call('ritual_ZN10QUndoStack4redoEv')


#  Qt's 'QList<QUndoStack *>': the list of QUndoStack, which
#  'QList[QUndoStack]' gives. It is made here, so that there is one as soon
#  as there can be a QUndoStack.
QList.createKind(
    QUndoStack, 'address',
    make='ritual_list_make_QUndoStack_ptr',
    add='ritual_list_add_QUndoStack_ptr',
    size='ritual_list_size_QUndoStack_ptr',
    at='ritual_list_at_QUndoStack_ptr',
    drop='ritual_list_drop_QUndoStack_ptr',
)
