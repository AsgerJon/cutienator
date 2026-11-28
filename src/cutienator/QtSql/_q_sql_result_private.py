"""
QSqlResultPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqlresult_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSqlResultPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QSqlDriver, QSqlResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlDriver = WAIT['QSqlDriver']
  QSqlResult = WAIT['QSqlResult']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlResultPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSqlResultPrivate: a plain Python object standing in
  front of one C++ QSqlResultPrivate.

  C++ hands a QSqlResultPrivate around as a copy, so every C++
  QSqlResultPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlResultPrivate that has a ritual and that Python
  can call so far, 10 names in all: 'q_func', 'clearValues',
  'resetBindCount', 'clearIndex', 'clear', 'fieldSerial',
  'positionalToNamedBinding', 'namedToPositionalBinding', 'holderAt',
  'isVariantNull'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSqlResult *QSqlResultPrivate::q_func() const': takes in
    Python what 'QSqlResult *QSqlResultPrivate::q_func()' takes.
  - Qt's 'QSqlResultPrivate::~QSqlResultPrivate()': the destructor: Python
    removes its C++ QSqlResultPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSqlResultPrivate is created at the first use, not by
    'QSqlResultPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlResultPrivate back gives a copy the ritual made
    for Python, in a new cute QSqlResultPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVariant)
  def isVariantNull(variant: QVariant) -> bool:
    """
    Calls Qt's 'bool QSqlResultPrivate::isVariantNull(const QVariant
    &variant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresultprivate.html#isVariantNull

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QSqlResultPrivate::isVariantNull(const QVariant &variant)
    return Rituals.call(
        'ritual_ZN17QSqlResultPrivate13isVariantNullERK8QVariant',
        CuteMixin._valueOf(variant),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlResultPrivate'

  #  A C++ QSqlResultPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlResultPrivate'

  #  The functions Qt calls itself that QSqlResultPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'fieldSerial': (
          ('_ZNK17QSqlResultPrivate11fieldSerialEx',
           ('address', 'text', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QSqlResultPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QSqlResultPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QSqlResultPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def fieldSerial(self, a0: int) -> str:
    """
    Calls Qt's 'QString QSqlResultPrivate::fieldSerial(qsizetype a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresultprivate.html#fieldSerial

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlResultPrivate::fieldSerial(qsizetype a0) const
    ritual = 'ritual_ZNK17QSqlResultPrivate11fieldSerialEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QSqlResultPrivate11fieldSerialEx'
    return self.uglySide.call(ritual, a0)

  @overload(str)
  def positionalToNamedBinding(self, query: str) -> str:
    """
    Calls Qt's 'QString QSqlResultPrivate::positionalToNamedBinding(const
    QString &query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresultprivate.html#positionalToNamedBinding

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlResultPrivate::positionalToNamedBinding(const QString
    #      &query) const
    return self.uglySide.call(
        'ritual_ZNK17QSqlResultPrivate24positionalToNamedBindingERK7QString',
        query,
    )

  @overload(int)
  def holderAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QSqlResultPrivate::holderAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresultprivate.html#holderAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlResultPrivate::holderAt(int index) const
    return self.uglySide.call(
        'ritual_ZNK17QSqlResultPrivate8holderAtEi', index,
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

  @overload(QSqlResult, QSqlDriver)
  @overload(QSqlResult, NoneType)
  @overload(NoneType, QSqlDriver)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      q: Optional[QSqlResult],
      drv: Optional[QSqlDriver],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSqlResultPrivate::QSqlResultPrivate(QSqlResult *q, const QSqlDriver
    *drv)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresultprivate.html#QSqlResultPrivate

    Parameters
    ----------

    q : Optional[QSqlResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    drv : Optional[QSqlDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSqlResultPrivate::QSqlResultPrivate(QSqlResult *q, const QSqlDriver
    #      *drv)
    self._noteCreation(QSqlResultPrivate, lambda: Rituals.call(
        'ritual_ZN17QSqlResultPrivateC1EP10QSqlResultPK10QSqlDriver',
        self._addressOf(q), self._addressOf(drv),
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

  def q_func(self) -> Optional[QSqlResult]:
    """
    Calls Qt's 'QSqlResult *QSqlResultPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresultprivate.html#q_func

    Returns
    -------

    Optional[QSqlResult]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlResult *QSqlResultPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QSqlResultPrivate6q_funcEv')
    from . import QSqlResult
    return QSqlResult._cuteAt(address)

  def clearValues(self) -> None:
    """
    Calls Qt's 'void QSqlResultPrivate::clearValues()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresultprivate.html#clearValues
    """
    #  void QSqlResultPrivate::clearValues()
    self.uglySide.call('ritual_ZN17QSqlResultPrivate11clearValuesEv')

  def resetBindCount(self) -> None:
    """
    Calls Qt's 'void QSqlResultPrivate::resetBindCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresultprivate.html#resetBindCount
    """
    #  void QSqlResultPrivate::resetBindCount()
    self.uglySide.call('ritual_ZN17QSqlResultPrivate14resetBindCountEv')

  def clearIndex(self) -> None:
    """
    Calls Qt's 'void QSqlResultPrivate::clearIndex()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresultprivate.html#clearIndex
    """
    #  void QSqlResultPrivate::clearIndex()
    self.uglySide.call('ritual_ZN17QSqlResultPrivate10clearIndexEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlResultPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresultprivate.html#clear
    """
    #  void QSqlResultPrivate::clear()
    self.uglySide.call('ritual_ZN17QSqlResultPrivate5clearEv')

  @overload(str)
  def namedToPositionalBinding(self, query: str) -> str:
    """
    Calls Qt's 'QString QSqlResultPrivate::namedToPositionalBinding(const
    QString &query)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresultprivate.html#namedToPositionalBinding

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlResultPrivate::namedToPositionalBinding(const QString
    #      &query)
    return self.uglySide.call(
        'ritual_ZN17QSqlResultPrivate24namedToPositionalBindingERK7QString',
        query,
    )
