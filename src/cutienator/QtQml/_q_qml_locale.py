"""
QQmlLocale binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmllocale_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlLocale to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QLocale
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlLocale(QLocale):
  """
  The cute side of Qt's QQmlLocale: a plain Python object standing in front
  of one C++ QQmlLocale.

  It is built on the cute 'QLocale', as Qt's QQmlLocale is built on Qt's
  QLocale, and has everything that class has.

  C++ hands a QQmlLocale around as a copy, so every C++ QQmlLocale behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlLocale that has a ritual and that Python can
  call so far, 3 names in all: 'locale', 'registerStringLocaleCompare',
  'method_localeCompare'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlLocale::qt_qmlMarker_anonymous()': one of Qt's own inner
    workings.
  - Qt's 'QQmlLocale::~QQmlLocale()': the destructor: Python removes its C++
    QQmlLocale by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlLocale is created at the first use, not by 'QQmlLocale(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlLocale back gives a copy the ritual made for
    Python, in a new cute QQmlLocale.
  """

  #  The enums Qt writes inside QQmlLocale, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class DayOfWeek(CuteNum):
    """
    The enum 'QQmlLocale::DayOfWeek' of Qt, with the 7 names Qt gives in it.
    """

    Sunday = Kee[int](0)
    Monday = Kee[int](1)
    Tuesday = Kee[int](2)
    Wednesday = Kee[int](3)
    Thursday = Kee[int](4)
    Friday = Kee[int](5)
    Saturday = Kee[int](6)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], str)
  @overload(NoneType, str)
  def locale(engine: Optional[QV4.ExecutionEngine], localeName: str) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlLocale::locale(QV4::ExecutionEngine
    *engine, const QString &localeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmllocale.html#locale

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QV4::ReturnedValue QQmlLocale::locale(QV4::ExecutionEngine *engine,
    #      const QString &localeName)
    return Rituals.call(
        'ritual_ZN10QQmlLocale6localeEPN3QV415ExecutionEngineERK7QString',
        CuteMixin._addressOf(engine), localeName,
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def registerStringLocaleCompare(
      engine: Optional[QV4.ExecutionEngine],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlLocale::registerStringLocaleCompare(QV4::ExecutionEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocale.html#registerStringLocaleCompare

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlLocale::registerStringLocaleCompare(QV4::ExecutionEngine
    #      *engine)
    Rituals.call(
        'ritual_ZN10QQmlLocale27registerStringLocaleCompareEPN3QV415Executi'
        'onEngineE',
        CuteMixin._addressOf(engine),
    )

  @staticmethod
  @overload(
      WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], WAIT['QV4.Value'], int,
  )
  @overload(WAIT['QV4.FunctionObject'], WAIT['QV4.Value'], NoneType, int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.FunctionObject'], NoneType, NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], WAIT['QV4.Value'], int)
  @overload(NoneType, WAIT['QV4.Value'], NoneType, int)
  @overload(NoneType, NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, NoneType, int)
  def method_localeCompare(
      a0: Optional[QV4.FunctionObject],
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
  ) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlLocale::method_localeCompare(const
    QV4::FunctionObject *a0, const QV4::Value *thisObject, const QV4::Value
    *argv, int argc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmllocale.html#method_localeCompare

    Parameters
    ----------

    a0 : Optional[QV4.FunctionObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlLocale::method_localeCompare(const
    #      QV4::FunctionObject *a0, const QV4::Value *thisObject, const
    #      QV4::Value *argv, int argc)
    return Rituals.call(
        'ritual_ZN10QQmlLocale20method_localeCompareEPKN3QV414FunctionObjec'
        'tEPKNS0_5ValueES6_i',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(thisObject),
        CuteMixin._addressOf(argv), argc,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlLocale'

  #  Qt's '~QQmlLocale()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlLocale behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QQmlLocaleD1Ev'

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
