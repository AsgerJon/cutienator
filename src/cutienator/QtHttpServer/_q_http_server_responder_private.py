"""
QHttpServerResponderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverresponder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QHttpServerResponderPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QHttpServerResponderPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpServerResponderPrivate: a plain Python object
  standing in front of one C++ QHttpServerResponderPrivate.

  What exists
  -----------

  Every function of Qt's QHttpServerResponderPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'cancel'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  8 of the 9 functions Qt declares: 8 leans on 'QHttpServerStream.

  What to expect
  --------------

  - The C++ QHttpServerResponderPrivate is created at the first use, not by
    'QHttpServerResponderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpServerResponderPrivate.
  - Each name of Qt's QHttpServerResponderPrivate that has no cute function
    yet, '__init__', 'write', 'writeBeginChunked', 'writeChunk',
    'writeEndChunked', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerResponderPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QHttpServerResponderPrivate::QHttpServerResponderPrivate(
    QHttpServerStream *stream)': leans on
    'QHttpServerStream::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpServerResponderPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QHttpServerResponderPrivate::QHttpServerResponderPrivate(QHttpServ"
        "erStream *stream)': leans on "
        "'QHttpServerStream::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def cancel(self) -> None:
    """
    Calls Qt's 'void QHttpServerResponderPrivate::cancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverresponderprivate.html#cancel
    """
    #  void QHttpServerResponderPrivate::cancel()
    self.uglySide.call('ritual_ZN27QHttpServerResponderPrivate6cancelEv')

  @staticmethod
  def write(*__, **_) -> Never:
    """
    - Qt's 'void QHttpServerResponderPrivate::write(const QByteArray &body,
      const QHttpHeaders &headers, QHttpServerResponder::StatusCode status)':
      leans on 'QHttpServerStream::staticMetaObject', which Qt's source does
      not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'void
      QHttpServerResponderPrivate::write(QHttpServerResponder::StatusCode
      status)': leans on 'QHttpServerStream::staticMetaObject', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'void QHttpServerResponderPrivate::write(QIODevice *data, const
      QHttpHeaders &headers, QHttpServerResponder::StatusCode status)': leans
      on 'QHttpServerStream::staticMetaObject', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpServerResponderPrivate.write' has no cute function yet. Qt's "
        "'void QHttpServerResponderPrivate::write(const QByteArray &body, "
        "const QHttpHeaders &headers, QHttpServerResponder::StatusCode "
        "status)': leans on 'QHttpServerStream::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'void "
        "QHttpServerResponderPrivate::write(QHttpServerResponder::StatusCode"
        " status)': leans on 'QHttpServerStream::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'void "
        "QHttpServerResponderPrivate::write(QIODevice *data, const "
        "QHttpHeaders &headers, QHttpServerResponder::StatusCode status)': "
        "leans on 'QHttpServerStream::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def writeBeginChunked(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerResponderPrivate::writeBeginChunked(const
    QHttpHeaders &headers, QHttpServerResponder::StatusCode status)': leans
    on 'QHttpServerStream::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpServerResponderPrivate.writeBeginChunked' has no cute "
        "function yet. Qt's 'void "
        "QHttpServerResponderPrivate::writeBeginChunked(const QHttpHeaders "
        "&headers, QHttpServerResponder::StatusCode status)': leans on "
        "'QHttpServerStream::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def writeChunk(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerResponderPrivate::writeChunk(const QByteArray
    &body)': leans on 'QHttpServerStream::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QHttpServerResponderPrivate.writeChunk' has no cute function yet. "
        "Qt's 'void QHttpServerResponderPrivate::writeChunk(const "
        "QByteArray &body)': leans on "
        "'QHttpServerStream::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def writeEndChunked(*__, **_) -> Never:
    """
    Qt's 'void QHttpServerResponderPrivate::writeEndChunked(const QByteArray
    &data, const QHttpHeaders &trailers)': leans on
    'QHttpServerStream::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHttpServerResponderPrivate.writeEndChunked' has no cute function "
        "yet. Qt's 'void QHttpServerResponderPrivate::writeEndChunked(const "
        "QByteArray &data, const QHttpHeaders &trailers)': leans on "
        "'QHttpServerStream::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
