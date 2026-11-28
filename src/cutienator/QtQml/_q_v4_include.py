"""
QV4Include binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4include_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4Include to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
  from . import QJSValue, QQmlNotifyingBlob, QQmlScriptBlob
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QQmlNotifyingBlob = WAIT['QQmlNotifyingBlob']
  QQmlScriptBlob = WAIT['QQmlScriptBlob']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QV4Include(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4Include: a plain Python object standing in front
  of one C++ QV4Include.

  C++ hands a QV4Include around as a copy, so every C++ QV4Include behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4Include that has a ritual and that Python can
  call so far, 6 names in all: 'method_include', 'ready', 'callback',
  'resultValue', 'populateResultValue', 'processScriptBlob'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4Include::~QV4Include()': the destructor: Python removes its C++
    QV4Include by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4Include is created at the first use, not by 'QV4Include(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4Include back gives a copy the ritual made for
    Python, in a new cute QV4Include.
  """

  #  The enums Qt writes inside QV4Include, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QV4Include::Status' of Qt, with the 4 names Qt gives in it.
    """

    Ok = Kee[int](0)
    Loading = Kee[int](1)
    NetworkError = Kee[int](2)
    Exception = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QUrl, QJSValue)
  @overload(NoneType, QUrl, QJSValue)
  def method_include(
      engine: Optional[QV4.ExecutionEngine],
      url: QUrl,
      callbackFunction: QJSValue,
  ) -> QJSValue:
    """
    Calls Qt's 'QJSValue QV4Include::method_include(QV4::ExecutionEngine
    *engine, const QUrl &url, const QJSValue &callbackFunction)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4include.html#method_include

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    callbackFunction : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QV4Include::method_include(QV4::ExecutionEngine *engine,
    #      const QUrl &url, const QJSValue &callbackFunction)
    address = Rituals.call(
        'ritual_ZN10QV4Include14method_includeEPN3QV415ExecutionEngineERK4Q'
        'UrlRK8QJSValue',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(url),
        CuteMixin._valueOf(callbackFunction),
    )
    from . import QJSValue
    return QJSValue._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Object'])
  @overload(WAIT['QV4.FunctionObject'], NoneType)
  @overload(NoneType, WAIT['QV4.Object'])
  @overload(NoneType, NoneType)
  def callback(
      callback: Optional[QV4.FunctionObject],
      result: Optional[QV4.Object],
  ) -> None:
    """
    Calls Qt's 'void QV4Include::callback(QV4::FunctionObject *callback,
    QV4::Object *result)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4include.html#callback

    Parameters
    ----------

    callback : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    result : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4Include::callback(QV4::FunctionObject *callback, QV4::Object
    #      *result)
    Rituals.call(
        'ritual_ZN10QV4Include8callbackEPN3QV414FunctionObjectEPNS0_6Object'
        'E',
        CuteMixin._addressOf(callback), CuteMixin._addressOf(result),
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def resultValue(v4: Optional[QV4.ExecutionEngine]) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue
    QV4Include::resultValue(QV4::ExecutionEngine *v4)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4include.html#resultValue

    Parameters
    ----------

    v4 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::ReturnedValue QV4Include::resultValue(QV4::ExecutionEngine *v4)
    return Rituals.call(
        'ritual_ZN10QV4Include11resultValueEPN3QV415ExecutionEngineE',
        CuteMixin._addressOf(v4),
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], Status)
  @overload(NoneType, Status)
  @overload(WAIT['QV4.Object'], Status, str)
  @overload(NoneType, Status, str)
  def populateResultValue(
      o: Optional[QV4.Object],
      status: Status,
      statusText: str = '',
  ) -> None:
    """
    Calls Qt's 'void QV4Include::populateResultValue(QV4::Object *o, Status
    status, const QString &statusText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4include.html#populateResultValue

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    status : Status
      Passed on as its number.

    statusText : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QV4Include::populateResultValue(QV4::Object *o, Status status,
    #      const QString &statusText)
    Rituals.call(
        'ritual_ZN10QV4Include19populateResultValueEPN3QV46ObjectENS_6Statu'
        'sERK7QString',
        CuteMixin._addressOf(o), status.value, statusText,
    )

  @staticmethod
  @overload(
      QQmlScriptBlob, WAIT['QV4.Object'], WAIT['QV4.FunctionObject'],
      WAIT['QV4.QmlContext'],
  )
  @overload(
      QQmlScriptBlob, WAIT['QV4.Object'], WAIT['QV4.FunctionObject'],
      NoneType,
  )
  @overload(
      QQmlScriptBlob, WAIT['QV4.Object'], NoneType, WAIT['QV4.QmlContext'],
  )
  @overload(QQmlScriptBlob, WAIT['QV4.Object'], NoneType, NoneType)
  @overload(
      QQmlScriptBlob, NoneType, WAIT['QV4.FunctionObject'],
      WAIT['QV4.QmlContext'],
  )
  @overload(QQmlScriptBlob, NoneType, WAIT['QV4.FunctionObject'], NoneType)
  @overload(QQmlScriptBlob, NoneType, NoneType, WAIT['QV4.QmlContext'])
  @overload(QQmlScriptBlob, NoneType, NoneType, NoneType)
  @overload(
      NoneType, WAIT['QV4.Object'], WAIT['QV4.FunctionObject'],
      WAIT['QV4.QmlContext'],
  )
  @overload(
      NoneType, WAIT['QV4.Object'], WAIT['QV4.FunctionObject'], NoneType,
  )
  @overload(NoneType, WAIT['QV4.Object'], NoneType, WAIT['QV4.QmlContext'])
  @overload(NoneType, WAIT['QV4.Object'], NoneType, NoneType)
  @overload(
      NoneType, NoneType, WAIT['QV4.FunctionObject'], WAIT['QV4.QmlContext'],
  )
  @overload(NoneType, NoneType, WAIT['QV4.FunctionObject'], NoneType)
  @overload(NoneType, NoneType, NoneType, WAIT['QV4.QmlContext'])
  @overload(NoneType, NoneType, NoneType, NoneType)
  def processScriptBlob(
      scriptBlob: Optional[QQmlScriptBlob],
      result: Optional[QV4.Object],
      callbackFunction: Optional[QV4.FunctionObject],
      qmlContext: Optional[QV4.QmlContext],
  ) -> None:
    """
    Calls Qt's 'void QV4Include::processScriptBlob(QQmlScriptBlob
    *scriptBlob, QV4::Object *result, QV4::FunctionObject *callbackFunction,
    QV4::QmlContext *qmlContext)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4include.html#processScriptBlob

    Parameters
    ----------

    scriptBlob : Optional[QQmlScriptBlob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    result : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    callbackFunction : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qmlContext : Optional[QV4.QmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4Include::processScriptBlob(QQmlScriptBlob *scriptBlob,
    #      QV4::Object *result, QV4::FunctionObject *callbackFunction,
    #      QV4::QmlContext *qmlContext)
    Rituals.call(
        'ritual_ZN10QV4Include17processScriptBlobEP14QQmlScriptBlobPN3QV46O'
        'bjectEPNS2_14FunctionObjectEPNS2_10QmlContextE',
        CuteMixin._addressOf(scriptBlob), CuteMixin._addressOf(result),
        CuteMixin._addressOf(callbackFunction),
        CuteMixin._addressOf(qmlContext),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4Include'

  #  Qt's '~QV4Include()'. Naming it makes this a value class: Python owns
  #  every C++ QV4Include behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QV4IncludeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(
      WAIT['QV4.Object'], WAIT['QV4.FunctionObject'], WAIT['QV4.QmlContext'],
  )
  @overload(WAIT['QV4.Object'], WAIT['QV4.FunctionObject'], NoneType)
  @overload(WAIT['QV4.Object'], NoneType, WAIT['QV4.QmlContext'])
  @overload(WAIT['QV4.Object'], NoneType, NoneType)
  @overload(NoneType, WAIT['QV4.FunctionObject'], WAIT['QV4.QmlContext'])
  @overload(NoneType, WAIT['QV4.FunctionObject'], NoneType)
  @overload(NoneType, NoneType, WAIT['QV4.QmlContext'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      result: Optional[QV4.Object],
      callbackFunction: Optional[QV4.FunctionObject],
      qmlContext: Optional[QV4.QmlContext],
  ) -> None:
    """
    Notes what was given, for Qt's 'QV4Include::QV4Include(QV4::Object
    *result, QV4::FunctionObject *callbackFunction, QV4::QmlContext
    *qmlContext)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4include.html#QV4Include

    Parameters
    ----------

    result : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    callbackFunction : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qmlContext : Optional[QV4.QmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4Include::QV4Include(QV4::Object *result, QV4::FunctionObject
    #      *callbackFunction, QV4::QmlContext *qmlContext)
    self._noteCreation(QV4Include, lambda: Rituals.call(
        'ritual_ZN10QV4IncludeC1EPN3QV46ObjectEPNS0_14FunctionObjectEPNS0_1'
        '0QmlContextE',
        self._addressOf(result), self._addressOf(callbackFunction),
        self._addressOf(qmlContext),
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

  @overload(QQmlNotifyingBlob)
  @overload(NoneType)
  def ready(self, a0: Optional[QQmlNotifyingBlob]) -> None:
    """
    Calls Qt's 'void QV4Include::ready(QQmlNotifyingBlob *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4include.html#ready

    Parameters
    ----------

    a0 : Optional[QQmlNotifyingBlob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4Include::ready(QQmlNotifyingBlob *a0)
    self.uglySide.call(
        'ritual_ZN10QV4Include5readyEP17QQmlNotifyingBlob',
        self._addressOf(a0),
    )
