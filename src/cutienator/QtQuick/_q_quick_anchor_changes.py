"""
QQuickAnchorChanges binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAnchorChanges to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickStateActionEvent, QQuickStateOperation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickAnchorSet, QQuickItem, QQuickStateAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnchorChanges(QQuickStateOperation, QQuickStateActionEvent):
  """
  The cute side of Qt's QQuickAnchorChanges: a plain Python object standing
  in front of one C++ QQuickAnchorChanges.

  It is built on the cute 'QQuickStateOperation', as Qt's QQuickAnchorChanges
  is built on Qt's QQuickStateOperation, and has everything that class has.
  It is built on the cute 'QQuickStateActionEvent' as well, as Qt's
  QQuickAnchorChanges is built on Qt's QQuickStateActionEvent too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnchorChanges that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'actions',
  'anchors', 'object', 'setObject', 'execute', 'isReversable', 'reverse',
  'type', 'mayOverride', 'changesBindings', 'saveOriginals', 'needsCopy',
  'copyOriginals', 'clearBindings', 'rewind', 'saveCurrentValues',
  'additionalActions', 'saveTargetValues'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnchorChanges::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAnchorChanges::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickAnchorChangesPrivate *QQuickAnchorChanges::d_func()': gives
    'QQuickAnchorChangesPrivate', which has no cute class yet.
  - Qt's 'const QQuickAnchorChangesPrivate *QQuickAnchorChanges::d_func()
    const': gives 'QQuickAnchorChangesPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAnchorChanges is created at the first use, not by
    'QQuickAnchorChanges(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnchorChanges.
  - Qt tells when it has removed the C++ QQuickAnchorChanges. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickAnchorChanges::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#tr

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
    #  QString QQuickAnchorChanges::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickAnchorChanges2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnchorChanges'

  #  Qt's QQuickAnchorChanges is built on more than one class. The part of a
  #  C++ QQuickAnchorChanges that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickStateActionEvent':
          'ritual_cast_QQuickAnchorChanges_QQuickStateActionEvent',
  }

  #  A C++ QQuickAnchorChanges Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnchorChanges'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnchorChanges::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnchorChanges::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickAnchorChanges10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def anchors(self) -> Optional[QQuickAnchorSet]:
    """
    Calls Qt's 'QQuickAnchorSet *QQuickAnchorChanges::anchors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#anchors

    Returns
    -------

    Optional[QQuickAnchorSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnchorSet *QQuickAnchorChanges::anchors() const
    address = self.uglySide.call('ritual_ZNK19QQuickAnchorChanges7anchorsEv')
    from . import QQuickAnchorSet
    return QQuickAnchorSet._cuteAt(address)

  def object(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAnchorChanges::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#object

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAnchorChanges::object() const
    address = self.uglySide.call('ritual_ZNK19QQuickAnchorChanges6objectEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def type(self) -> QQuickStateActionEvent.EventType:
    """
    Calls Qt's 'EventType QQuickAnchorChanges::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#type

    Returns
    -------

    QQuickStateActionEvent.EventType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickStateActionEvent.EventType(number)' gives.
    """
    #  EventType QQuickAnchorChanges::type() const
    ritual = 'ritual_ZNK19QQuickAnchorChanges4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickAnchorChanges4typeEv'
    return QQuickStateActionEvent.EventType(self.uglySide.call(ritual))

  def additionalActions(self) -> QList[QQuickStateAction]:
    """
    Calls Qt's 'QList<QQuickStateAction>
    QQuickAnchorChanges::additionalActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#additionalActions

    Returns
    -------

    QList[QQuickStateAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickStateAction> QQuickAnchorChanges::additionalActions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickAnchorChanges17additionalActionsEv',
    )
    from . import QQuickStateAction
    return QList[QQuickStateAction]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setObject(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnchorChanges::setObject(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#setObject

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnchorChanges::setObject(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickAnchorChanges9setObjectEP10QQuickItem',
        self._addressOf(a0),
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
    Notes what was given, for Qt's
    'QQuickAnchorChanges::QQuickAnchorChanges(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#QQuickAnchorChanges

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAnchorChanges::QQuickAnchorChanges(QObject *parent)
    self._noteCreation(QQuickAnchorChanges, lambda: Rituals.call(
        'ritual_ZN19QQuickAnchorChangesC1EP7QObject',
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

  def actions(self) -> QList[QQuickStateAction]:
    """
    Calls Qt's 'ActionList QQuickAnchorChanges::actions()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#actions

    Returns
    -------

    QList[QQuickStateAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  ActionList QQuickAnchorChanges::actions()
    address = self.uglySide.call('ritual_ZN19QQuickAnchorChanges7actionsEv')
    from . import QQuickStateAction
    return QList[QQuickStateAction]._cuteOwning(address)

  def execute(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorChanges::execute()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#execute
    """
    #  void QQuickAnchorChanges::execute()
    ritual = 'ritual_ZN19QQuickAnchorChanges7executeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges7executeEv'
    self.uglySide.call(ritual)

  def isReversable(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnchorChanges::isReversable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#isReversable
    """
    #  bool QQuickAnchorChanges::isReversable()
    ritual = 'ritual_ZN19QQuickAnchorChanges12isReversableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges12isReversableEv'
    return self.uglySide.call(ritual)

  def reverse(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorChanges::reverse()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#reverse
    """
    #  void QQuickAnchorChanges::reverse()
    ritual = 'ritual_ZN19QQuickAnchorChanges7reverseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges7reverseEv'
    self.uglySide.call(ritual)

  @overload(QQuickStateActionEvent)
  @overload(NoneType)
  def mayOverride(self, other: Optional[QQuickStateActionEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickAnchorChanges::mayOverride(QQuickStateActionEvent
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#mayOverride

    Parameters
    ----------

    other : Optional[QQuickStateActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickAnchorChanges::mayOverride(QQuickStateActionEvent *other)
    ritual = (
        'ritual_ZN19QQuickAnchorChanges11mayOverrideEP22QQuickStateActionEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickAnchorChanges11mayOverrideEP22QQuickStateAc'
          'tionEvent')
    return self.uglySide.call(
        ritual, self._addressOf(other, 'QQuickStateActionEvent'),
    )

  def changesBindings(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnchorChanges::changesBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#changesBindings
    """
    #  bool QQuickAnchorChanges::changesBindings()
    ritual = 'ritual_ZN19QQuickAnchorChanges15changesBindingsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges15changesBindingsEv'
    return self.uglySide.call(ritual)

  def saveOriginals(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorChanges::saveOriginals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#saveOriginals
    """
    #  void QQuickAnchorChanges::saveOriginals()
    ritual = 'ritual_ZN19QQuickAnchorChanges13saveOriginalsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges13saveOriginalsEv'
    self.uglySide.call(ritual)

  def needsCopy(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnchorChanges::needsCopy()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#needsCopy
    """
    #  bool QQuickAnchorChanges::needsCopy()
    ritual = 'ritual_ZN19QQuickAnchorChanges9needsCopyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges9needsCopyEv'
    return self.uglySide.call(ritual)

  @overload(QQuickStateActionEvent)
  @overload(NoneType)
  def copyOriginals(self, a0: Optional[QQuickStateActionEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickAnchorChanges::copyOriginals(QQuickStateActionEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#copyOriginals

    Parameters
    ----------

    a0 : Optional[QQuickStateActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnchorChanges::copyOriginals(QQuickStateActionEvent *a0)
    ritual = (
        'ritual_ZN19QQuickAnchorChanges13copyOriginalsEP22QQuickStateAction'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickAnchorChanges13copyOriginalsEP22QQuickState'
          'ActionEvent')
    self.uglySide.call(ritual, self._addressOf(a0, 'QQuickStateActionEvent'))

  def clearBindings(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorChanges::clearBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#clearBindings
    """
    #  void QQuickAnchorChanges::clearBindings()
    ritual = 'ritual_ZN19QQuickAnchorChanges13clearBindingsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges13clearBindingsEv'
    self.uglySide.call(ritual)

  def rewind(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorChanges::rewind()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorchanges.html#rewind
    """
    #  void QQuickAnchorChanges::rewind()
    ritual = 'ritual_ZN19QQuickAnchorChanges6rewindEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges6rewindEv'
    self.uglySide.call(ritual)

  def saveCurrentValues(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorChanges::saveCurrentValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#saveCurrentValues
    """
    #  void QQuickAnchorChanges::saveCurrentValues()
    ritual = 'ritual_ZN19QQuickAnchorChanges17saveCurrentValuesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges17saveCurrentValuesEv'
    self.uglySide.call(ritual)

  def saveTargetValues(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorChanges::saveTargetValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorchanges.html#saveTargetValues
    """
    #  void QQuickAnchorChanges::saveTargetValues()
    ritual = 'ritual_ZN19QQuickAnchorChanges16saveTargetValuesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnchorChanges16saveTargetValuesEv'
    self.uglySide.call(ritual)
