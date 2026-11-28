"""
QQuickWorkerScript binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlWorkerScript/6.12.0/QtQmlWorkerScript/private/qquickworkerscript_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWorkerScript to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QUrl
  from ..QtQml import QJSValue, QQmlV4Function
  from . import QQuickWorkerScriptEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QJSValue = WAIT['QJSValue']
  QQmlV4Function = WAIT['QQmlV4Function']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWorkerScript(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickWorkerScript: a plain Python object standing in
  front of one C++ QQuickWorkerScript.

  It is built on the cute 'QObject', as Qt's QQuickWorkerScript is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickWorkerScript is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWorkerScript that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'ready', 'sendMessage', 'sourceChanged', 'readyChanged',
  'message', 'classBegin', 'componentComplete', 'event', 'engine'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWorkerScript::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickWorkerScript::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWorkerScript::~QQuickWorkerScript()': the destructor: Python
    never removes a C++ QQuickWorkerScript.

  What has no ritual
  ------------------

  6 of the 23 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWorkerScript is created at the first use, not by
    'QQuickWorkerScript(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWorkerScript.
  - Qt tells when it has removed the C++ QQuickWorkerScript. Every call on
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
    Calls Qt's 'QString QQuickWorkerScript::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#tr

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
    #  QString QQuickWorkerScript::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickWorkerScript2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWorkerScript'

  #  Qt's QQuickWorkerScript is built on more than one class. The part of a
  #  C++ QQuickWorkerScript that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickWorkerScript_QQmlParserStatus',
  }

  #  A C++ QQuickWorkerScript Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWorkerScript'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWorkerScript::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWorkerScript::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickWorkerScript10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickWorkerScript::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickWorkerScript::source() const
    address = self.uglySide.call('ritual_ZNK18QQuickWorkerScript6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def ready(self) -> bool:
    """
    Calls Qt's 'bool QQuickWorkerScript::ready() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#ready
    """
    #  bool QQuickWorkerScript::ready() const
    return self.uglySide.call('ritual_ZNK18QQuickWorkerScript5readyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQuickWorkerScript::setSource(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#setSource

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickWorkerScript::setSource(const QUrl &a0)
    self.uglySide.call(
        'ritual_ZN18QQuickWorkerScript9setSourceERK4QUrl', self._valueOf(a0),
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
    'QQuickWorkerScript::QQuickWorkerScript(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickworkerscript.html#QQuickWorkerScript

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWorkerScript::QQuickWorkerScript(QObject *parent)
    self._noteCreation(QQuickWorkerScript, lambda: Rituals.call(
        'ritual_ZN18QQuickWorkerScriptC1EP7QObject',
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

  @overload(QQmlV4Function)
  @overload(NoneType)
  def sendMessage(self, a0: Optional[QQmlV4Function]) -> None:
    """
    Calls Qt's 'void QQuickWorkerScript::sendMessage(QQmlV4FunctionPtr a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickworkerscript.html#sendMessage

    Parameters
    ----------

    a0 : Optional[QQmlV4Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWorkerScript::sendMessage(QQmlV4FunctionPtr a0)
    self.uglySide.call(
        'ritual_ZN18QQuickWorkerScript11sendMessageEP14QQmlV4Function',
        self._addressOf(a0),
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWorkerScript::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickworkerscript.html#sourceChanged
    """
    #  void QQuickWorkerScript::sourceChanged()
    self.uglySide.call('ritual_ZN18QQuickWorkerScript13sourceChangedEv')

  def readyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWorkerScript::readyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickworkerscript.html#readyChanged
    """
    #  void QQuickWorkerScript::readyChanged()
    self.uglySide.call('ritual_ZN18QQuickWorkerScript12readyChangedEv')

  @overload(QJSValue)
  def message(self, messageObject: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickWorkerScript::message(const QJSValue
    &messageObject)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#message

    Parameters
    ----------

    messageObject : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickWorkerScript::message(const QJSValue &messageObject)
    self.uglySide.call(
        'ritual_ZN18QQuickWorkerScript7messageERK8QJSValue',
        self._valueOf(messageObject),
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickWorkerScript::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#classBegin
    """
    #  void QQuickWorkerScript::classBegin()
    ritual = 'ritual_ZN18QQuickWorkerScript10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickWorkerScript10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickWorkerScript::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickworkerscript.html#componentComplete
    """
    #  void QQuickWorkerScript::componentComplete()
    ritual = 'ritual_ZN18QQuickWorkerScript17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickWorkerScript17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickWorkerScript::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickWorkerScript::event(QEvent *a0)
    ritual = 'ritual_ZN18QQuickWorkerScript5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickWorkerScript5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def engine(self) -> Optional[QQuickWorkerScriptEngine]:
    """
    Calls Qt's 'QQuickWorkerScriptEngine *QQuickWorkerScript::engine()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickworkerscript.html#engine

    Returns
    -------

    Optional[QQuickWorkerScriptEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWorkerScriptEngine *QQuickWorkerScript::engine()
    address = self.uglySide.call('ritual_ZN18QQuickWorkerScript6engineEv')
    from . import QQuickWorkerScriptEngine
    return QQuickWorkerScriptEngine._cuteAt(address)
