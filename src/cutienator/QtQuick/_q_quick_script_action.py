"""
QQuickScriptAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickScriptAction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickAbstractAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlScriptString
  from . import QQuickScriptActionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlScriptString = WAIT['QQmlScriptString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScriptAction(QQuickAbstractAnimation):
  """
  The cute side of Qt's QQuickScriptAction: a plain Python object standing in
  front of one C++ QQuickScriptAction.

  It is built on the cute 'QQuickAbstractAnimation', as Qt's
  QQuickScriptAction is built on Qt's QQuickAbstractAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScriptAction that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'd_func', 'script',
  'setScript', 'stateChangeScriptName', 'setStateChangeScriptName'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScriptAction::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickScriptAction::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickScriptActionPrivate *QQuickScriptAction::d_func()
    const': takes in Python what 'QQuickScriptActionPrivate
    *QQuickScriptAction::d_func()' takes.
  - Qt's 'QQuickScriptAction::~QQuickScriptAction()': the destructor: Python
    never removes a C++ QQuickScriptAction.
  - Qt's 'QAbstractAnimationJob
    *QQuickScriptAction::transition(QQuickStateActions &actions,
    QQmlProperties &modified, TransitionDirection direction, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickScriptAction is created at the first use, not by
    'QQuickScriptAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScriptAction.
  - Qt tells when it has removed the C++ QQuickScriptAction. Every call on
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
    Calls Qt's 'QString QQuickScriptAction::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscriptaction.html#tr

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
    #  QString QQuickScriptAction::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickScriptAction2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScriptAction'

  #  A C++ QQuickScriptAction Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickScriptAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickScriptAction::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscriptaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScriptAction::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickScriptAction10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def script(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickScriptAction::script() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscriptaction.html#script

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickScriptAction::script() const
    address = self.uglySide.call('ritual_ZNK18QQuickScriptAction6scriptEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def stateChangeScriptName(self) -> str:
    """
    Calls Qt's 'QString QQuickScriptAction::stateChangeScriptName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscriptaction.html#stateChangeScriptName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickScriptAction::stateChangeScriptName() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickScriptAction21stateChangeScriptNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlScriptString)
  def setScript(self, a0: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickScriptAction::setScript(const QQmlScriptString
    &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscriptaction.html#setScript

    Parameters
    ----------

    a0 : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickScriptAction::setScript(const QQmlScriptString &a0)
    self.uglySide.call(
        'ritual_ZN18QQuickScriptAction9setScriptERK16QQmlScriptString',
        self._valueOf(a0),
    )

  @overload(str)
  def setStateChangeScriptName(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickScriptAction::setStateChangeScriptName(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscriptaction.html#setStateChangeScriptName

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickScriptAction::setStateChangeScriptName(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18QQuickScriptAction24setStateChangeScriptNameERK7QString',
        a0,
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
    'QQuickScriptAction::QQuickScriptAction(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscriptaction.html#QQuickScriptAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickScriptAction::QQuickScriptAction(QObject *parent)
    self._noteCreation(QQuickScriptAction, lambda: Rituals.call(
        'ritual_ZN18QQuickScriptActionC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickScriptActionPrivate]:
    """
    Calls Qt's 'QQuickScriptActionPrivate *QQuickScriptAction::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscriptaction.html#d_func

    Returns
    -------

    Optional[QQuickScriptActionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScriptActionPrivate *QQuickScriptAction::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickScriptAction6d_funcEv')
    from . import QQuickScriptActionPrivate
    return QQuickScriptActionPrivate._cuteAt(address)
