"""
QQuickStateGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstategroup_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickStateGroup to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickState = WAIT['QQuickState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStateGroup(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickStateGroup: a plain Python object standing in
  front of one C++ QQuickStateGroup.

  It is built on the cute 'QObject', as Qt's QQuickStateGroup is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickStateGroup is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStateGroup that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'state', 'setState',
  'states', 'findState', 'removeState', 'classBegin', 'componentComplete',
  'stateChanged', 'updateAutoState', 'stateAboutToComplete'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStateGroup::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickStateGroup::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickStateGroupPrivate *QQuickStateGroup::d_func()': gives
    'QQuickStateGroupPrivate', which has no cute class yet.
  - Qt's 'const QQuickStateGroupPrivate *QQuickStateGroup::d_func() const':
    gives 'QQuickStateGroupPrivate', which has no cute class yet.
  - Qt's 'QQuickStateGroup::~QQuickStateGroup()': the destructor: Python
    never removes a C++ QQuickStateGroup.
  - Qt's 'QQmlListProperty<QQuickState> QQuickStateGroup::statesProperty()':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickTransition>
    QQuickStateGroup::transitionsProperty()': gives a type Python has no way
    to take yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickStateGroup is created at the first use, not by
    'QQuickStateGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStateGroup.
  - Qt tells when it has removed the C++ QQuickStateGroup. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickStateGroup that has no cute function yet,
    'statesProperty', 'transitionsProperty', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickStateGroup::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#tr

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
    #  QString QQuickStateGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickStateGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStateGroup'

  #  Qt's QQuickStateGroup is built on more than one class. The part of a C++
  #  QQuickStateGroup that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickStateGroup_QQmlParserStatus',
  }

  #  A C++ QQuickStateGroup Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStateGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStateGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStateGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickStateGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def state(self) -> str:
    """
    Calls Qt's 'QString QQuickStateGroup::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#state

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStateGroup::state() const
    return self.uglySide.call('ritual_ZNK16QQuickStateGroup5stateEv')

  def states(self) -> QList[QQuickState]:
    """
    Calls Qt's 'QList<QQuickState *> QQuickStateGroup::states() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#states

    Returns
    -------

    QList[QQuickState]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickState *> QQuickStateGroup::states() const
    address = self.uglySide.call('ritual_ZNK16QQuickStateGroup6statesEv')
    from . import QQuickState
    return QList[QQuickState]._cuteOwning(address)

  @overload(str)
  def findState(self, name: str) -> Optional[QQuickState]:
    """
    Calls Qt's 'QQuickState *QQuickStateGroup::findState(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#findState

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQuickState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickState *QQuickStateGroup::findState(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickStateGroup9findStateERK7QString', name,
    )
    from . import QQuickState
    return QQuickState._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setState(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickStateGroup::setState(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#setState

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStateGroup::setState(const QString &a0)
    self.uglySide.call('ritual_ZN16QQuickStateGroup8setStateERK7QString', a0)

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
  def __init__(self, a0: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStateGroup::QQuickStateGroup(QObject *a0)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstategroup.html#QQuickStateGroup

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStateGroup::QQuickStateGroup(QObject *a0)
    self._noteCreation(QQuickStateGroup, lambda: Rituals.call(
        'ritual_ZN16QQuickStateGroupC1EP7QObject',
        self._addressOf(a0, 'QObject'),
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

  @overload(QQuickState)
  @overload(NoneType)
  def removeState(self, state: Optional[QQuickState]) -> None:
    """
    Calls Qt's 'void QQuickStateGroup::removeState(QQuickState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#removeState

    Parameters
    ----------

    state : Optional[QQuickState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStateGroup::removeState(QQuickState *state)
    self.uglySide.call(
        'ritual_ZN16QQuickStateGroup11removeStateEP11QQuickState',
        self._addressOf(state),
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickStateGroup::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#classBegin
    """
    #  void QQuickStateGroup::classBegin()
    ritual = 'ritual_ZN16QQuickStateGroup10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickStateGroup10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickStateGroup::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstategroup.html#componentComplete
    """
    #  void QQuickStateGroup::componentComplete()
    ritual = 'ritual_ZN16QQuickStateGroup17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickStateGroup17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(str)
  def stateChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickStateGroup::stateChanged(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstategroup.html#stateChanged

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStateGroup::stateChanged(const QString &a0)
    self.uglySide.call(
        'ritual_ZN16QQuickStateGroup12stateChangedERK7QString', a0,
    )

  def updateAutoState(self) -> bool:
    """
    Calls Qt's 'bool QQuickStateGroup::updateAutoState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstategroup.html#updateAutoState
    """
    #  bool QQuickStateGroup::updateAutoState()
    return self.uglySide.call(
        'ritual_ZN16QQuickStateGroup15updateAutoStateEv',
    )

  def stateAboutToComplete(self) -> None:
    """
    Calls Qt's 'void QQuickStateGroup::stateAboutToComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstategroup.html#stateAboutToComplete
    """
    #  void QQuickStateGroup::stateAboutToComplete()
    self.uglySide.call('ritual_ZN16QQuickStateGroup20stateAboutToCompleteEv')

  @staticmethod
  def statesProperty(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickState> QQuickStateGroup::statesProperty()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickStateGroup.statesProperty' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickState> "
        "QQuickStateGroup::statesProperty()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def transitionsProperty(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickTransition>
    QQuickStateGroup::transitionsProperty()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuickStateGroup.transitionsProperty' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuickTransition> "
        "QQuickStateGroup::transitionsProperty()': gives a type Python has "
        "no way to take yet.")
