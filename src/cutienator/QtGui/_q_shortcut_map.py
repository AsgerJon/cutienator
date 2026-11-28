"""
QShortcutMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qshortcutmap_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QShortcutMap to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QKeySequence

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShortcutMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShortcutMap: a plain Python object standing in front
  of one C++ QShortcutMap.

  What exists
  -----------

  Every function of Qt's QShortcutMap that has a ritual and that Python can
  call so far, 12 names in all: 'removeShortcut', 'setShortcutEnabled',
  'setShortcutAutoRepeat', 'state', 'tryShortcut',
  'hasShortcutForKeySequence', 'keySequences', 'resetState', 'nextState',
  'dispatchEvent', 'find', 'translateModifiers'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShortcutMapPrivate *QShortcutMap::d_func()': gives
    'QShortcutMapPrivate', which has no cute class yet.
  - Qt's 'const QShortcutMapPrivate *QShortcutMap::d_func() const': gives
    'QShortcutMapPrivate', which has no cute class yet.
  - Qt's 'QShortcutMap::~QShortcutMap()': the destructor: Python never
    removes a C++ QShortcutMap.
  - Qt's 'int QShortcutMap::addShortcut(QObject *owner, const QKeySequence
    &key, Qt::ShortcutContext context, ContextMatcher matcher)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QList<const QShortcutEntry *> QShortcutMap::matches() const': gives
    a type Python has no way to take yet.
  - Qt's 'void QShortcutMap::createNewSequences(QKeyEvent *e,
    QList<QKeySequence> &ksl, int ignoredModifiers)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QShortcutMap::clearSequence(QList<QKeySequence> &ksl)': takes
    a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QShortcutMap is created at the first use, not by
    'QShortcutMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QShortcutMap.
  - Each name of Qt's QShortcutMap that has no cute function yet,
    'addShortcut', 'clearSequence', 'createNewSequences', 'd_func',
    'matches', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QShortcutMap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QKeySequence)
  def hasShortcutForKeySequence(self, seq: QKeySequence) -> bool:
    """
    Calls Qt's 'bool QShortcutMap::hasShortcutForKeySequence(const
    QKeySequence &seq) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshortcutmap.html#hasShortcutForKeySequence

    Parameters
    ----------

    seq : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  bool QShortcutMap::hasShortcutForKeySequence(const QKeySequence &seq)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12QShortcutMap25hasShortcutForKeySequenceERK12QKeySequen'
        'ce',
        self._valueOf(seq),
    )

  @overload()
  @overload(bool)
  def keySequences(self, getAll: bool = False) -> QList[QKeySequence]:
    """
    Calls Qt's 'QList<QKeySequence> QShortcutMap::keySequences(bool getAll)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#keySequences

    Parameters
    ----------

    getAll : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QList[QKeySequence]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QKeySequence> QShortcutMap::keySequences(bool getAll) const
    address = self.uglySide.call(
        'ritual_ZNK12QShortcutMap12keySequencesEb', getAll,
    )
    return QList[QKeySequence]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool, int, QObject)
  @overload(bool, int, NoneType)
  @overload(bool, int, QObject, QKeySequence)
  @overload(bool, int, NoneType, QKeySequence)
  def setShortcutEnabled(
      self,
      enable: bool,
      id: int,
      owner: Optional[QObject],
      key: Optional[QKeySequence] = None,
  ) -> int:
    """
    Calls Qt's 'int QShortcutMap::setShortcutEnabled(bool enable, int id,
    QObject *owner, const QKeySequence &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshortcutmap.html#setShortcutEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.

    id : int
      Passed on as it is.

    owner : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    key : Optional[QKeySequence]
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own. May be left out, as in Qt: a new 'QKeySequence()' is then
      passed on.
    """
    #  int QShortcutMap::setShortcutEnabled(bool enable, int id, QObject
    #      *owner, const QKeySequence &key)
    if key is None:
      key = QKeySequence()
    return self.uglySide.call(
        'ritual_ZN12QShortcutMap18setShortcutEnabledEbiP7QObjectRK12QKeySeq'
        'uence',
        enable, id, self._addressOf(owner, 'QObject'), self._valueOf(key),
    )

  @overload(bool, int, QObject)
  @overload(bool, int, NoneType)
  @overload(bool, int, QObject, QKeySequence)
  @overload(bool, int, NoneType, QKeySequence)
  def setShortcutAutoRepeat(
      self,
      on: bool,
      id: int,
      owner: Optional[QObject],
      key: Optional[QKeySequence] = None,
  ) -> int:
    """
    Calls Qt's 'int QShortcutMap::setShortcutAutoRepeat(bool on, int id,
    QObject *owner, const QKeySequence &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshortcutmap.html#setShortcutAutoRepeat

    Parameters
    ----------

    on : bool
      Passed on as it is.

    id : int
      Passed on as it is.

    owner : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    key : Optional[QKeySequence]
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own. May be left out, as in Qt: a new 'QKeySequence()' is then
      passed on.
    """
    #  int QShortcutMap::setShortcutAutoRepeat(bool on, int id, QObject
    #      *owner, const QKeySequence &key)
    if key is None:
      key = QKeySequence()
    return self.uglySide.call(
        'ritual_ZN12QShortcutMap21setShortcutAutoRepeatEbiP7QObjectRK12QKey'
        'Sequence',
        on, id, self._addressOf(owner, 'QObject'), self._valueOf(key),
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
    Notes what was given, for Qt's 'QShortcutMap::QShortcutMap()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#QShortcutMap
    """
    #  QShortcutMap::QShortcutMap()
    self._noteCreation(QShortcutMap, lambda: Rituals.call(
        'ritual_ZN12QShortcutMapC1Ev',
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

  @overload(int, QObject)
  @overload(int, NoneType)
  @overload(int, QObject, QKeySequence)
  @overload(int, NoneType, QKeySequence)
  def removeShortcut(
      self,
      id: int,
      owner: Optional[QObject],
      key: Optional[QKeySequence] = None,
  ) -> int:
    """
    Calls Qt's 'int QShortcutMap::removeShortcut(int id, QObject *owner,
    const QKeySequence &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#removeShortcut

    Parameters
    ----------

    id : int
      Passed on as it is.

    owner : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    key : Optional[QKeySequence]
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own. May be left out, as in Qt: a new 'QKeySequence()' is then
      passed on.
    """
    #  int QShortcutMap::removeShortcut(int id, QObject *owner, const
    #      QKeySequence &key)
    if key is None:
      key = QKeySequence()
    return self.uglySide.call(
        'ritual_ZN12QShortcutMap14removeShortcutEiP7QObjectRK12QKeySequence',
        id, self._addressOf(owner, 'QObject'), self._valueOf(key),
    )

  def state(self) -> QKeySequence.SequenceMatch:
    """
    Calls Qt's 'QKeySequence::SequenceMatch QShortcutMap::state()'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#state

    Returns
    -------

    QKeySequence.SequenceMatch
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QKeySequence.SequenceMatch(number)' gives.
    """
    #  QKeySequence::SequenceMatch QShortcutMap::state()
    return QKeySequence.SequenceMatch(self.uglySide.call(
        'ritual_ZN12QShortcutMap5stateEv',
    ))

  @overload(QKeyEvent)
  @overload(NoneType)
  def tryShortcut(self, e: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool QShortcutMap::tryShortcut(QKeyEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#tryShortcut

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QShortcutMap::tryShortcut(QKeyEvent *e)
    return self.uglySide.call(
        'ritual_ZN12QShortcutMap11tryShortcutEP9QKeyEvent',
        self._addressOf(e),
    )

  def resetState(self) -> None:
    """
    Calls Qt's 'void QShortcutMap::resetState()'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#resetState
    """
    #  void QShortcutMap::resetState()
    self.uglySide.call('ritual_ZN12QShortcutMap10resetStateEv')

  @overload(QKeyEvent)
  @overload(NoneType)
  def nextState(self, e: Optional[QKeyEvent]) -> QKeySequence.SequenceMatch:
    """
    Calls Qt's 'QKeySequence::SequenceMatch QShortcutMap::nextState(QKeyEvent
    *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#nextState

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QKeySequence.SequenceMatch
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QKeySequence.SequenceMatch(number)' gives.
    """
    #  QKeySequence::SequenceMatch QShortcutMap::nextState(QKeyEvent *e)
    return QKeySequence.SequenceMatch(self.uglySide.call(
        'ritual_ZN12QShortcutMap9nextStateEP9QKeyEvent', self._addressOf(e),
    ))

  @overload(QKeyEvent)
  @overload(NoneType)
  def dispatchEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QShortcutMap::dispatchEvent(QKeyEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#dispatchEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QShortcutMap::dispatchEvent(QKeyEvent *e)
    self.uglySide.call(
        'ritual_ZN12QShortcutMap13dispatchEventEP9QKeyEvent',
        self._addressOf(e),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  @overload(QKeyEvent, int)
  @overload(NoneType, int)
  def find(
      self,
      e: Optional[QKeyEvent],
      ignoredModifiers: int = 0,
  ) -> QKeySequence.SequenceMatch:
    """
    Calls Qt's 'QKeySequence::SequenceMatch QShortcutMap::find(QKeyEvent *e,
    int ignoredModifiers)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutmap.html#find

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ignoredModifiers : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QKeySequence.SequenceMatch
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QKeySequence.SequenceMatch(number)' gives.
    """
    #  QKeySequence::SequenceMatch QShortcutMap::find(QKeyEvent *e, int
    #      ignoredModifiers)
    return QKeySequence.SequenceMatch(self.uglySide.call(
        'ritual_ZN12QShortcutMap4findEP9QKeyEventi',
        self._addressOf(e), ignoredModifiers,
    ))

  @overload(Qt.KeyboardModifiers)
  def translateModifiers(self, modifiers: Qt.KeyboardModifiers) -> int:
    """
    Calls Qt's 'int QShortcutMap::translateModifiers(Qt::KeyboardModifiers
    modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshortcutmap.html#translateModifiers

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  int QShortcutMap::translateModifiers(Qt::KeyboardModifiers modifiers)
    return self.uglySide.call(
        'ritual_ZN12QShortcutMap18translateModifiersE6QFlagsIN2Qt16Keyboard'
        'ModifierEE',
        modifiers.value,
    )

  @staticmethod
  def addShortcut(*__, **_) -> Never:
    """
    Qt's 'int QShortcutMap::addShortcut(QObject *owner, const QKeySequence
    &key, Qt::ShortcutContext context, ContextMatcher matcher)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QShortcutMap.addShortcut' has no cute function yet. Qt's 'int "
        "QShortcutMap::addShortcut(QObject *owner, const QKeySequence &key, "
        "Qt::ShortcutContext context, ContextMatcher matcher)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def clearSequence(*__, **_) -> Never:
    """
    Qt's 'void QShortcutMap::clearSequence(QList<QKeySequence> &ksl)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QShortcutMap.clearSequence' has no cute function yet. Qt's 'void "
        "QShortcutMap::clearSequence(QList<QKeySequence> &ksl)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def createNewSequences(*__, **_) -> Never:
    """
    Qt's 'void QShortcutMap::createNewSequences(QKeyEvent *e,
    QList<QKeySequence> &ksl, int ignoredModifiers)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QShortcutMap.createNewSequences' has no cute function yet. Qt's "
        "'void QShortcutMap::createNewSequences(QKeyEvent *e, "
        "QList<QKeySequence> &ksl, int ignoredModifiers)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QShortcutMapPrivate *QShortcutMap::d_func()': gives
      'QShortcutMapPrivate', which has no cute class yet.
    - Qt's 'const QShortcutMapPrivate *QShortcutMap::d_func() const': gives
      'QShortcutMapPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QShortcutMap.d_func' has no cute function yet. Qt's "
        "'QShortcutMapPrivate *QShortcutMap::d_func()': gives "
        "'QShortcutMapPrivate', which has no cute class yet. Qt's 'const "
        "QShortcutMapPrivate *QShortcutMap::d_func() const': gives "
        "'QShortcutMapPrivate', which has no cute class yet.")

  @staticmethod
  def matches(*__, **_) -> Never:
    """
    Qt's 'QList<const QShortcutEntry *> QShortcutMap::matches() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShortcutMap.matches' has no cute function yet. Qt's 'QList<const "
        "QShortcutEntry *> QShortcutMap::matches() const': gives a type "
        "Python has no way to take yet.")
