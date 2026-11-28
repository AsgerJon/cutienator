"""
QSqlQueryModelSql binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqlquerymodel_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSqlQueryModelSql to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QLatin1String


class QSqlQueryModelSql(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSqlQueryModelSql: a plain Python object standing in
  front of one C++ QSqlQueryModelSql.

  C++ hands a QSqlQueryModelSql around as a copy, so every C++
  QSqlQueryModelSql behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlQueryModelSql that has a ritual and that Python
  can call so far, 17 names in all: 'as_', 'asc', 'comma', 'desc', 'eq',
  'et', 'from_', 'leftJoin', 'on', 'orderBy', 'parenClose', 'parenOpen',
  'select', 'sp', 'where', 'concat', 'paren'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSqlQueryModelSql::~QSqlQueryModelSql()': the destructor: Python
    removes its C++ QSqlQueryModelSql by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSqlQueryModelSql is created at the first use, not by
    'QSqlQueryModelSql(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlQueryModelSql back gives a copy the ritual made
    for Python, in a new cute QSqlQueryModelSql.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload()
  def as_() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::as()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#as

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::as()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql2asEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def as_(a: str, b: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::as(const QString &a, const
    QString &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#as

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.

    b : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::as(const QString &a, const QString
    #      &b)
    return Rituals.call(
        'ritual_ZN17QSqlQueryModelSql2asERK7QStringS2_', a, b,
    )

  @staticmethod
  @overload()
  def asc() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::asc()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#asc

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::asc()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql3ascEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str)
  def asc(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::asc(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#asc

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::asc(const QString &s)
    return Rituals.call('ritual_ZN17QSqlQueryModelSql3ascERK7QString', s)

  @staticmethod
  @overload()
  def comma() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::comma()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#comma

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::comma()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql5commaEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def comma(a: str, b: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::comma(const QString &a,
    const QString &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#comma

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.

    b : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::comma(const QString &a, const QString
    #      &b)
    return Rituals.call(
        'ritual_ZN17QSqlQueryModelSql5commaERK7QStringS2_', a, b,
    )

  @staticmethod
  @overload()
  def desc() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::desc()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#desc

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::desc()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql4descEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str)
  def desc(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::desc(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#desc

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::desc(const QString &s)
    return Rituals.call('ritual_ZN17QSqlQueryModelSql4descERK7QString', s)

  @staticmethod
  @overload()
  def eq() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::eq()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#eq

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::eq()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql2eqEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def eq(a: str, b: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::eq(const QString &a, const
    QString &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#eq

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.

    b : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::eq(const QString &a, const QString
    #      &b)
    return Rituals.call(
        'ritual_ZN17QSqlQueryModelSql2eqERK7QStringS2_', a, b,
    )

  @staticmethod
  @overload()
  def et() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::et()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#et

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::et()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql2etEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def et(a: str, b: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::et(const QString &a, const
    QString &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#et

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.

    b : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::et(const QString &a, const QString
    #      &b)
    return Rituals.call(
        'ritual_ZN17QSqlQueryModelSql2etERK7QStringS2_', a, b,
    )

  @staticmethod
  @overload()
  def from_() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::from()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#from

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::from()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql4fromEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str)
  def from_(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::from(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#from

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::from(const QString &s)
    return Rituals.call('ritual_ZN17QSqlQueryModelSql4fromERK7QString', s)

  @staticmethod
  @overload()
  def leftJoin() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::leftJoin()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#leftJoin

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::leftJoin()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql8leftJoinEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str)
  def leftJoin(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::leftJoin(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#leftJoin

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::leftJoin(const QString &s)
    return Rituals.call(
        'ritual_ZN17QSqlQueryModelSql8leftJoinERK7QString', s,
    )

  @staticmethod
  @overload()
  def on() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::on()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#on

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::on()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql2onEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str)
  def on(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::on(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#on

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::on(const QString &s)
    return Rituals.call('ritual_ZN17QSqlQueryModelSql2onERK7QString', s)

  @staticmethod
  @overload()
  def orderBy() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::orderBy()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#orderBy

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::orderBy()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql7orderByEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str)
  def orderBy(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::orderBy(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#orderBy

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::orderBy(const QString &s)
    return Rituals.call('ritual_ZN17QSqlQueryModelSql7orderByERK7QString', s)

  @staticmethod
  def parenClose() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::parenClose()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#parenClose

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::parenClose()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql10parenCloseEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  def parenOpen() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::parenOpen()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#parenOpen

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::parenOpen()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql9parenOpenEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload()
  def select() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::select()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#select

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::select()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql6selectEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str)
  def select(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::select(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#select

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::select(const QString &s)
    return Rituals.call('ritual_ZN17QSqlQueryModelSql6selectERK7QString', s)

  @staticmethod
  def sp() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::sp()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#sp

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::sp()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql2spEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload()
  def where() -> QLatin1String:
    """
    Calls Qt's 'const QLatin1StringView QSqlQueryModelSql::where()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#where

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  const QLatin1StringView QSqlQueryModelSql::where()
    address = Rituals.call('ritual_ZN17QSqlQueryModelSql5whereEv')
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  @staticmethod
  @overload(str)
  def where(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::where(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#where

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::where(const QString &s)
    return Rituals.call('ritual_ZN17QSqlQueryModelSql5whereERK7QString', s)

  @staticmethod
  @overload(str, str)
  def concat(a: str, b: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::concat(const QString &a,
    const QString &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#concat

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.

    b : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::concat(const QString &a, const
    #      QString &b)
    return Rituals.call(
        'ritual_ZN17QSqlQueryModelSql6concatERK7QStringS2_', a, b,
    )

  @staticmethod
  @overload(str)
  def paren(s: str) -> str:
    """
    Calls Qt's 'const QString QSqlQueryModelSql::paren(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodelsql.html#paren

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString QSqlQueryModelSql::paren(const QString &s)
    return Rituals.call('ritual_ZN17QSqlQueryModelSql5parenERK7QString', s)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlQueryModelSql'

  #  Qt's '~QSqlQueryModelSql()'. Naming it makes this a value class: Python
  #  owns every C++ QSqlQueryModelSql behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QSqlQueryModelSqlD1Ev'

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
