"""
QQuickStateChangeScript binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstatechangescript_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickStateChangeScript to be private: it declares the class in a
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
  from ..QtQml import QQmlScriptString
  from . import QQuickStateAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlScriptString = WAIT['QQmlScriptString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStateChangeScript(QQuickStateOperation, QQuickStateActionEvent):
  """
  The cute side of Qt's QQuickStateChangeScript: a plain Python object
  standing in front of one C++ QQuickStateChangeScript.

  It is built on the cute 'QQuickStateOperation', as Qt's
  QQuickStateChangeScript is built on Qt's QQuickStateOperation, and has
  everything that class has. It is built on the cute 'QQuickStateActionEvent'
  as well, as Qt's QQuickStateChangeScript is built on Qt's
  QQuickStateActionEvent too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickStateChangeScript that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'actions',
  'type', 'script', 'setScript', 'name', 'setName', 'execute'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStateChangeScript::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickStateChangeScript::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickStateChangeScriptPrivate *QQuickStateChangeScript::d_func()':
    gives 'QQuickStateChangeScriptPrivate', which has no cute class yet.
  - Qt's 'const QQuickStateChangeScriptPrivate
    *QQuickStateChangeScript::d_func() const': gives
    'QQuickStateChangeScriptPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickStateChangeScript is created at the first use, not by
    'QQuickStateChangeScript(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStateChangeScript.
  - Qt tells when it has removed the C++ QQuickStateChangeScript. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickStateChangeScript::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstatechangescript.html#tr

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
    #  QString QQuickStateChangeScript::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickStateChangeScript2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStateChangeScript'

  #  Qt's QQuickStateChangeScript is built on more than one class. The part
  #  of a C++ QQuickStateChangeScript that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickStateActionEvent':
          'ritual_cast_QQuickStateChangeScript_QQuickStateActionEvent',
  }

  #  A C++ QQuickStateChangeScript Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStateChangeScript'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStateChangeScript::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstatechangescript.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStateChangeScript::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickStateChangeScript10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> QQuickStateActionEvent.EventType:
    """
    Calls Qt's 'EventType QQuickStateChangeScript::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstatechangescript.html#type

    Returns
    -------

    QQuickStateActionEvent.EventType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickStateActionEvent.EventType(number)' gives.
    """
    #  EventType QQuickStateChangeScript::type() const
    ritual = 'ritual_ZNK23QQuickStateChangeScript4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QQuickStateChangeScript4typeEv'
    return QQuickStateActionEvent.EventType(self.uglySide.call(ritual))

  def script(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickStateChangeScript::script() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstatechangescript.html#script

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickStateChangeScript::script() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickStateChangeScript6scriptEv',
    )
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickStateChangeScript::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstatechangescript.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickStateChangeScript::name() const
    return self.uglySide.call('ritual_ZNK23QQuickStateChangeScript4nameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlScriptString)
  def setScript(self, a0: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickStateChangeScript::setScript(const
    QQmlScriptString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstatechangescript.html#setScript

    Parameters
    ----------

    a0 : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickStateChangeScript::setScript(const QQmlScriptString &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickStateChangeScript9setScriptERK16QQmlScriptString',
        self._valueOf(a0),
    )

  @overload(str)
  def setName(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickStateChangeScript::setName(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstatechangescript.html#setName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStateChangeScript::setName(const QString &a0)
    self.uglySide.call(
        'ritual_ZN23QQuickStateChangeScript7setNameERK7QString', a0,
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
    'QQuickStateChangeScript::QQuickStateChangeScript(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstatechangescript.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStateChangeScript::QQuickStateChangeScript(QObject *parent)
    self._noteCreation(QQuickStateChangeScript, lambda: Rituals.call(
        'ritual_ZN23QQuickStateChangeScriptC1EP7QObject',
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
    Calls Qt's 'ActionList QQuickStateChangeScript::actions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstatechangescript.html#actions

    Returns
    -------

    QList[QQuickStateAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  ActionList QQuickStateChangeScript::actions()
    address = self.uglySide.call(
        'ritual_ZN23QQuickStateChangeScript7actionsEv',
    )
    from . import QQuickStateAction
    return QList[QQuickStateAction]._cuteOwning(address)

  def execute(self) -> None:
    """
    Calls Qt's 'void QQuickStateChangeScript::execute()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstatechangescript.html#execute
    """
    #  void QQuickStateChangeScript::execute()
    ritual = 'ritual_ZN23QQuickStateChangeScript7executeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickStateChangeScript7executeEv'
    self.uglySide.call(ritual)
