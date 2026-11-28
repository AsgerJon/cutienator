"""
QIOOperation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qiooperation_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QIOOperation to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QIOOperationPrivate, QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIOOperation(QObject):
  """
  The cute side of Qt's QIOOperation: a plain Python object standing in front
  of one C++ QIOOperation.

  It is built on the cute 'QObject', as Qt's QIOOperation is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIOOperation that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'type', 'error',
  'isFinished', 'finished', 'errorOccurred', 'ensureCompleteOrCanceled',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QIOOperation::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QIOOperation::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QIOOperation::~QIOOperation()': the destructor: Python never
    removes a C++ QIOOperation.
  - Qt's 'QIOOperation::QIOOperation(QIOOperationPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QIOOperationPrivate *QIOOperation::d_func() const': takes in
    Python what 'QIOOperationPrivate *QIOOperation::d_func()' takes.

  What has no ritual
  ------------------

  7 of the 21 functions Qt declares: 5 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QIOOperation is created at the first use, not by
    'QIOOperation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIOOperation.
  - Qt tells when it has removed the C++ QIOOperation. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QIOOperation that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QIOOperation, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'QIOOperation::Error' of Qt, with the 8 names Qt gives in it.
    C++ keeps these names inside the enum, so the class that holds the enum
    does not have them.
    """

    NULL = Kee[int](0)
    FileNotOpen = Kee[int](1)
    IncorrectOffset = Kee[int](2)
    Read = Kee[int](3)
    Write = Kee[int](4)
    Flush = Kee[int](5)
    Open = Kee[int](6)
    Aborted = Kee[int](7)

  class Type(CuteNum, scoped=True):
    """
    The enum 'QIOOperation::Type' of Qt, with the 5 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Unknown = Kee[int](0)
    Read = Kee[int](1)
    Write = Kee[int](2)
    Flush = Kee[int](3)
    Open = Kee[int](4)

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
    Calls Qt's 'QString QIOOperation::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperation.html#tr

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
    #  QString QIOOperation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QIOOperation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIOOperation'

  #  A C++ QIOOperation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIOOperation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QIOOperation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QIOOperation::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QIOOperation10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QIOOperation::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperation.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QIOOperation::type() const
    return QIOOperation.Type(self.uglySide.call(
        'ritual_ZNK12QIOOperation4typeEv',
    ))

  def error(self) -> Error:
    """
    Calls Qt's 'Error QIOOperation::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperation.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QIOOperation::error() const
    return QIOOperation.Error(self.uglySide.call(
        'ritual_ZNK12QIOOperation5errorEv',
    ))

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QIOOperation::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperation.html#isFinished
    """
    #  bool QIOOperation::isFinished() const
    return self.uglySide.call('ritual_ZNK12QIOOperation10isFinishedEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QIOOperation::QIOOperation(QIOOperationPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QIOOperation.__init__' has no cute function yet. Qt's "
        "'QIOOperation::QIOOperation(QIOOperationPrivate &dd, QObject "
        "*parent)': takes a type Python has no way to hand over yet.")

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

  def finished(self) -> None:
    """
    Calls Qt's 'void QIOOperation::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperation.html#finished
    """
    #  void QIOOperation::finished()
    self.uglySide.call('ritual_ZN12QIOOperation8finishedEv')

  @overload(Error)
  def errorOccurred(self, err: Error) -> None:
    """
    Calls Qt's 'void QIOOperation::errorOccurred(Error err)'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperation.html#errorOccurred

    Parameters
    ----------

    err : Error
      Passed on as its number.
    """
    #  void QIOOperation::errorOccurred(Error err)
    self.uglySide.call(
        'ritual_ZN12QIOOperation13errorOccurredENS_5ErrorE', err.value,
    )

  def ensureCompleteOrCanceled(self) -> None:
    """
    Calls Qt's 'void QIOOperation::ensureCompleteOrCanceled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qiooperation.html#ensureCompleteOrCanceled
    """
    #  void QIOOperation::ensureCompleteOrCanceled()
    self.uglySide.call('ritual_ZN12QIOOperation24ensureCompleteOrCanceledEv')

  def d_func(self) -> Optional[QIOOperationPrivate]:
    """
    Calls Qt's 'QIOOperationPrivate *QIOOperation::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qiooperation.html#d_func

    Returns
    -------

    Optional[QIOOperationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIOOperationPrivate *QIOOperation::d_func()
    address = self.uglySide.call('ritual_ZN12QIOOperation6d_funcEv')
    from . import QIOOperationPrivate
    return QIOOperationPrivate._cuteAt(address)
