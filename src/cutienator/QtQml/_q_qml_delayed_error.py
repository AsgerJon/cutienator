"""
QQmlDelayedError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelayedError to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQmlEnginePrivate, QQmlError, QQmlSourceLocation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlEnginePrivate = WAIT['QQmlEnginePrivate']
  QQmlSourceLocation = WAIT['QQmlSourceLocation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDelayedError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDelayedError: a plain Python object standing in
  front of one C++ QQmlDelayedError.

  C++ hands a QQmlDelayedError around as a copy, so every C++
  QQmlDelayedError behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlDelayedError that has a ritual and that Python
  can call so far, 9 names in all: 'addError', 'removeError', 'isValid',
  'error', 'clearError', 'setErrorLocation', 'setErrorDescription',
  'setErrorObject', 'catchJavaScriptException'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDelayedError::~QQmlDelayedError()': the destructor: Python
    removes its C++ QQmlDelayedError by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlDelayedError is created at the first use, not by
    'QQmlDelayedError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDelayedError back gives a copy the ritual made
    for Python, in a new cute QQmlDelayedError.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDelayedError'

  #  Qt's '~QQmlDelayedError()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlDelayedError behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlDelayedErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlDelayedError::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelayederror.html#isValid
    """
    #  bool QQmlDelayedError::isValid() const
    return self.uglySide.call('ritual_ZNK16QQmlDelayedError7isValidEv')

  def error(self) -> QQmlError:
    """
    Calls Qt's 'const QQmlError &QQmlDelayedError::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelayederror.html#error

    Returns
    -------

    QQmlError
      A new cute QQmlError around the copy Qt gave back. Python owns it.
    """
    #  const QQmlError &QQmlDelayedError::error() const
    address = self.uglySide.call('ritual_ZNK16QQmlDelayedError5errorEv')
    from . import QQmlError
    return QQmlError._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlSourceLocation)
  def setErrorLocation(self, sourceLocation: QQmlSourceLocation) -> None:
    """
    Calls Qt's 'void QQmlDelayedError::setErrorLocation(const
    QQmlSourceLocation &sourceLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelayederror.html#setErrorLocation

    Parameters
    ----------

    sourceLocation : QQmlSourceLocation
      Passed on as a value: Qt reads the C++ QQmlSourceLocation, which stays
      Python's own.
    """
    #  void QQmlDelayedError::setErrorLocation(const QQmlSourceLocation
    #      &sourceLocation)
    self.uglySide.call(
        'ritual_ZN16QQmlDelayedError16setErrorLocationERK18QQmlSourceLocati'
        'on',
        self._valueOf(sourceLocation),
    )

  @overload(str)
  def setErrorDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QQmlDelayedError::setErrorDescription(const QString
    &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelayederror.html#setErrorDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDelayedError::setErrorDescription(const QString &description)
    self.uglySide.call(
        'ritual_ZN16QQmlDelayedError19setErrorDescriptionERK7QString',
        description,
    )

  @overload(QObject)
  @overload(NoneType)
  def setErrorObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlDelayedError::setErrorObject(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelayederror.html#setErrorObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelayedError::setErrorObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN16QQmlDelayedError14setErrorObjectEP7QObject',
        self._addressOf(object, 'QObject'),
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
    Notes what was given, for Qt's 'QQmlDelayedError::QQmlDelayedError()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelayederror.html#QQmlDelayedError
    """
    #  QQmlDelayedError::QQmlDelayedError()
    self._noteCreation(QQmlDelayedError, lambda: Rituals.call(
        'ritual_ZN16QQmlDelayedErrorC1Ev',
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

  @overload(QQmlEnginePrivate)
  @overload(NoneType)
  def addError(self, a0: Optional[QQmlEnginePrivate]) -> bool:
    """
    Calls Qt's 'bool QQmlDelayedError::addError(QQmlEnginePrivate *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelayederror.html#addError

    Parameters
    ----------

    a0 : Optional[QQmlEnginePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlDelayedError::addError(QQmlEnginePrivate *a0)
    return self.uglySide.call(
        'ritual_ZN16QQmlDelayedError8addErrorEP17QQmlEnginePrivate',
        self._addressOf(a0),
    )

  def removeError(self) -> QQmlError:
    """
    Calls Qt's 'QQmlError QQmlDelayedError::removeError()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelayederror.html#removeError

    Returns
    -------

    QQmlError
      A new cute QQmlError around the copy Qt gave back. Python owns it.
    """
    #  QQmlError QQmlDelayedError::removeError()
    address = self.uglySide.call(
        'ritual_ZN16QQmlDelayedError11removeErrorEv',
    )
    from . import QQmlError
    return QQmlError._cuteOwning(address)

  def clearError(self) -> None:
    """
    Calls Qt's 'void QQmlDelayedError::clearError()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldelayederror.html#clearError
    """
    #  void QQmlDelayedError::clearError()
    self.uglySide.call('ritual_ZN16QQmlDelayedError10clearErrorEv')

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def catchJavaScriptException(
      self,
      engine: Optional[QV4.ExecutionEngine],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDelayedError::catchJavaScriptException(QV4::ExecutionEngine
    *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelayederror.html#catchJavaScriptException

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDelayedError::catchJavaScriptException(QV4::ExecutionEngine
    #      *engine)
    self.uglySide.call(
        'ritual_ZN16QQmlDelayedError24catchJavaScriptExceptionEPN3QV415Exec'
        'utionEngineE',
        self._addressOf(engine),
    )
