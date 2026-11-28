"""
QPropertyBindingError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QPropertyBindingError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPropertyBindingError: a plain Python object standing
  in front of one C++ QPropertyBindingError.

  C++ hands a QPropertyBindingError around as a copy, so every C++
  QPropertyBindingError behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPropertyBindingError that has a ritual and that
  Python can call so far, 3 names in all: 'hasError', 'type', 'description'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPropertyBindingError &QPropertyBindingError::operator=(const
    QPropertyBindingError &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QPropertyBindingError::QPropertyBindingError(QPropertyBindingError
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QPropertyBindingError
    &QPropertyBindingError::operator=(QPropertyBindingError &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QPropertyBindingError::~QPropertyBindingError()': the destructor:
    Python removes its C++ QPropertyBindingError by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPropertyBindingError is created at the first use, not by
    'QPropertyBindingError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPropertyBindingError back gives a copy the ritual
    made for Python, in a new cute QPropertyBindingError.
  """

  #  The enums Qt writes inside QPropertyBindingError, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QPropertyBindingError::Type' of Qt, with the 4 names Qt gives
    in it.
    """

    NoError = Kee[int](0)
    BindingLoop = Kee[int](1)
    EvaluationError = Kee[int](2)
    UnknownError = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyBindingError'

  #  Qt's '~QPropertyBindingError()'. Naming it makes this a value class:
  #  Python owns every C++ QPropertyBindingError behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QPropertyBindingErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QPropertyBindingError::hasError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingerror.html#hasError
    """
    #  bool QPropertyBindingError::hasError() const
    return self.uglySide.call('ritual_ZNK21QPropertyBindingError8hasErrorEv')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QPropertyBindingError::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpropertybindingerror.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QPropertyBindingError::type() const
    return QPropertyBindingError.Type(self.uglySide.call(
        'ritual_ZNK21QPropertyBindingError4typeEv',
    ))

  def description(self) -> str:
    """
    Calls Qt's 'QString QPropertyBindingError::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingerror.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPropertyBindingError::description() const
    return self.uglySide.call(
        'ritual_ZNK21QPropertyBindingError11descriptionEv',
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyBindingError::QPropertyBindingError()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingerror.html#QPropertyBindingError
    """
    #  QPropertyBindingError::QPropertyBindingError()
    self._noteCreation(QPropertyBindingError, lambda: Rituals.call(
        'ritual_ZN21QPropertyBindingErrorC1Ev',
    ))

  @overload(Type)
  @overload(Type, str)
  def __init__(self, type: Type, description: str = '') -> None:
    """
    Notes what was given, for Qt's
    'QPropertyBindingError::QPropertyBindingError(Type type, const QString
    &description)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingerror.html#QPropertyBindingError

    Parameters
    ----------

    type : Type
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QPropertyBindingError::QPropertyBindingError(Type type, const QString
    #      &description)
    self._noteCreation(QPropertyBindingError, lambda: Rituals.call(
        'ritual_ZN21QPropertyBindingErrorC1ENS_4TypeERK7QString',
        type.value, description,
    ))

  @overload(THIS)
  def __init__(self, other: QPropertyBindingError) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyBindingError::QPropertyBindingError(const QPropertyBindingError
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertybindingerror.html#QPropertyBindingError

    Parameters
    ----------

    other : QPropertyBindingError
      Passed on as a value: Qt reads the C++ QPropertyBindingError, which
      stays Python's own.
    """
    #  QPropertyBindingError::QPropertyBindingError(const
    #      QPropertyBindingError &other)
    self._noteCreation(QPropertyBindingError, lambda: Rituals.call(
        'ritual_ZN21QPropertyBindingErrorC1ERKS_', self._valueOf(other),
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
