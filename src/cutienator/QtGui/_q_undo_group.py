"""
QUndoGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qundogroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAction, QUndoStack
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUndoStack = WAIT['QUndoStack']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUndoGroup(QObject):
  """
  The cute side of Qt's QUndoGroup: a plain Python object standing in front
  of one C++ QUndoGroup.

  It is built on the cute 'QObject', as Qt's QUndoGroup is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QUndoGroup that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'addStack',
  'removeStack', 'stacks', 'activeStack', 'createUndoAction',
  'createRedoAction', 'canUndo', 'canRedo', 'undoText', 'redoText',
  'isClean', 'undo', 'redo', 'setActiveStack'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUndoGroup::~QUndoGroup()': the destructor: Python never removes a
    C++ QUndoGroup.

  What has no ritual
  ------------------

  15 of the 33 functions Qt declares: 7 a signal; 4 takes or gives a type
  that cannot be passed yet; 2 forbidden; 1 a template; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QUndoGroup is created at the first use, not by 'QUndoGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUndoGroup.
  - Qt tells when it has removed the C++ QUndoGroup. Every call on the cute
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
    Calls Qt's 'QString QUndoGroup::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#tr

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
    #  QString QUndoGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QUndoGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUndoGroup'

  #  A C++ QUndoGroup Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUndoGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QUndoGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QUndoGroup::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QUndoGroup10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def stacks(self) -> QList[QUndoStack]:
    """
    Calls Qt's 'QList<QUndoStack *> QUndoGroup::stacks() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#stacks

    Returns
    -------

    QList[QUndoStack]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUndoStack *> QUndoGroup::stacks() const
    address = self.uglySide.call('ritual_ZNK10QUndoGroup6stacksEv')
    from . import QUndoStack
    return QList[QUndoStack]._cuteOwning(address)

  def activeStack(self) -> Optional[QUndoStack]:
    """
    Calls Qt's 'QUndoStack *QUndoGroup::activeStack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#activeStack

    Returns
    -------

    Optional[QUndoStack]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUndoStack *QUndoGroup::activeStack() const
    address = self.uglySide.call('ritual_ZNK10QUndoGroup11activeStackEv')
    from . import QUndoStack
    return QUndoStack._cuteAt(address)

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
    Calls Qt's 'QAction *QUndoGroup::createUndoAction(QObject *parent, const
    QString &prefix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#createUndoAction

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
    #  QAction *QUndoGroup::createUndoAction(QObject *parent, const QString
    #      &prefix) const
    address = self.uglySide.call(
        'ritual_ZNK10QUndoGroup16createUndoActionEP7QObjectRK7QString',
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
    Calls Qt's 'QAction *QUndoGroup::createRedoAction(QObject *parent, const
    QString &prefix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#createRedoAction

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
    #  QAction *QUndoGroup::createRedoAction(QObject *parent, const QString
    #      &prefix) const
    address = self.uglySide.call(
        'ritual_ZNK10QUndoGroup16createRedoActionEP7QObjectRK7QString',
        self._addressOf(parent, 'QObject'), prefix,
    )
    from . import QAction
    return QAction._cuteAt(address)

  def canUndo(self) -> bool:
    """
    Calls Qt's 'bool QUndoGroup::canUndo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#canUndo
    """
    #  bool QUndoGroup::canUndo() const
    return self.uglySide.call('ritual_ZNK10QUndoGroup7canUndoEv')

  def canRedo(self) -> bool:
    """
    Calls Qt's 'bool QUndoGroup::canRedo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#canRedo
    """
    #  bool QUndoGroup::canRedo() const
    return self.uglySide.call('ritual_ZNK10QUndoGroup7canRedoEv')

  def undoText(self) -> str:
    """
    Calls Qt's 'QString QUndoGroup::undoText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#undoText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoGroup::undoText() const
    return self.uglySide.call('ritual_ZNK10QUndoGroup8undoTextEv')

  def redoText(self) -> str:
    """
    Calls Qt's 'QString QUndoGroup::redoText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#redoText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoGroup::redoText() const
    return self.uglySide.call('ritual_ZNK10QUndoGroup8redoTextEv')

  def isClean(self) -> bool:
    """
    Calls Qt's 'bool QUndoGroup::isClean() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#isClean
    """
    #  bool QUndoGroup::isClean() const
    return self.uglySide.call('ritual_ZNK10QUndoGroup7isCleanEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUndoStack)
  @overload(NoneType)
  def setActiveStack(self, stack: Optional[QUndoStack]) -> None:
    """
    Calls Qt's 'void QUndoGroup::setActiveStack(QUndoStack *stack)'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#setActiveStack

    Parameters
    ----------

    stack : Optional[QUndoStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUndoGroup::setActiveStack(QUndoStack *stack)
    self.uglySide.call(
        'ritual_ZN10QUndoGroup14setActiveStackEP10QUndoStack',
        self._addressOf(stack),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QUndoGroup::QUndoGroup(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#QUndoGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUndoGroup::QUndoGroup(QObject *parent)
    self._noteCreation(QUndoGroup, lambda: Rituals.call(
        'ritual_ZN10QUndoGroupC1EP7QObject',
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

  @overload(QUndoStack)
  @overload(NoneType)
  def addStack(self, stack: Optional[QUndoStack]) -> None:
    """
    Calls Qt's 'void QUndoGroup::addStack(QUndoStack *stack)'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#addStack

    Parameters
    ----------

    stack : Optional[QUndoStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUndoGroup::addStack(QUndoStack *stack)
    self.uglySide.call(
        'ritual_ZN10QUndoGroup8addStackEP10QUndoStack',
        self._addressOf(stack),
    )

  @overload(QUndoStack)
  @overload(NoneType)
  def removeStack(self, stack: Optional[QUndoStack]) -> None:
    """
    Calls Qt's 'void QUndoGroup::removeStack(QUndoStack *stack)'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#removeStack

    Parameters
    ----------

    stack : Optional[QUndoStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUndoGroup::removeStack(QUndoStack *stack)
    self.uglySide.call(
        'ritual_ZN10QUndoGroup11removeStackEP10QUndoStack',
        self._addressOf(stack),
    )

  def undo(self) -> None:
    """
    Calls Qt's 'void QUndoGroup::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#undo
    """
    #  void QUndoGroup::undo()
    self.uglySide.call('ritual_ZN10QUndoGroup4undoEv')

  def redo(self) -> None:
    """
    Calls Qt's 'void QUndoGroup::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qundogroup.html#redo
    """
    #  void QUndoGroup::redo()
    self.uglySide.call('ritual_ZN10QUndoGroup4redoEv')
