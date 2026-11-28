"""
QDnsLookupReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDnsLookupReply to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QDnsLookup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDnsLookupReply(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDnsLookupReply: a plain Python object standing in
  front of one C++ QDnsLookupReply.

  C++ hands a QDnsLookupReply around as a copy, so every C++ QDnsLookupReply
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDnsLookupReply that has a ritual and that Python
  can call so far, 4 names in all: 'makeResolverSystemError',
  'makeTimeoutError', 'makeDnsRcodeError', 'allAreEmpty'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QDnsLookupReply::setError(QDnsLookup::Error err, QString
    &&msg)': takes a type Python has no way to hand over yet.
  - Qt's 'void QDnsLookupReply::makeInvalidReplyError(QString &&msg)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QDnsLookupReply::~QDnsLookupReply()': the destructor: Python
    removes its C++ QDnsLookupReply by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDnsLookupReply is created at the first use, not by
    'QDnsLookupReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDnsLookupReply back gives a copy the ritual made for
    Python, in a new cute QDnsLookupReply.
  - Each name of Qt's QDnsLookupReply that has no cute function yet,
    'makeInvalidReplyError', 'setError', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDnsLookupReply'

  #  Qt's '~QDnsLookupReply()'. Naming it makes this a value class: Python
  #  owns every C++ QDnsLookupReply behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDnsLookupReplyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def allAreEmpty(self) -> bool:
    """
    Calls Qt's 'bool QDnsLookupReply::allAreEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookupreply.html#allAreEmpty
    """
    #  bool QDnsLookupReply::allAreEmpty() const
    return self.uglySide.call('ritual_ZNK15QDnsLookupReply11allAreEmptyEv')

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

  @overload()
  @overload(int)
  def makeResolverSystemError(self, code: int = -1) -> None:
    """
    Calls Qt's 'void QDnsLookupReply::makeResolverSystemError(int code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupreply.html#makeResolverSystemError

    Parameters
    ----------

    code : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QDnsLookupReply::makeResolverSystemError(int code)
    self.uglySide.call(
        'ritual_ZN15QDnsLookupReply23makeResolverSystemErrorEi', code,
    )

  def makeTimeoutError(self) -> None:
    """
    Calls Qt's 'void QDnsLookupReply::makeTimeoutError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupreply.html#makeTimeoutError
    """
    #  void QDnsLookupReply::makeTimeoutError()
    self.uglySide.call('ritual_ZN15QDnsLookupReply16makeTimeoutErrorEv')

  @overload(int)
  def makeDnsRcodeError(self, rcode: int) -> None:
    """
    Calls Qt's 'void QDnsLookupReply::makeDnsRcodeError(quint8 rcode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupreply.html#makeDnsRcodeError

    Parameters
    ----------

    rcode : int
      Passed on as it is.
    """
    #  void QDnsLookupReply::makeDnsRcodeError(quint8 rcode)
    self.uglySide.call(
        'ritual_ZN15QDnsLookupReply17makeDnsRcodeErrorEh', rcode,
    )

  @staticmethod
  def makeInvalidReplyError(*__, **_) -> Never:
    """
    Qt's 'void QDnsLookupReply::makeInvalidReplyError(QString &&msg)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDnsLookupReply.makeInvalidReplyError' has no cute function yet. "
        "Qt's 'void QDnsLookupReply::makeInvalidReplyError(QString &&msg)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setError(*__, **_) -> Never:
    """
    Qt's 'void QDnsLookupReply::setError(QDnsLookup::Error err, QString
    &&msg)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDnsLookupReply.setError' has no cute function yet. Qt's 'void "
        "QDnsLookupReply::setError(QDnsLookup::Error err, QString &&msg)': "
        "takes a type Python has no way to hand over yet.")
