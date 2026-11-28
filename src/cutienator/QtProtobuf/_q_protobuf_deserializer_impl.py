"""
QProtobufDeserializerImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QProtobufDeserializerImpl to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractProtobufSerializer, QProtobufDeserializerBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArrayView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']


class QProtobufDeserializerImpl(QProtobufDeserializerBase):
  """
  The cute side of Qt's QProtobufDeserializerImpl: a plain Python object
  standing in front of one C++ QProtobufDeserializerImpl.

  It is built on the cute 'QProtobufDeserializerBase', as Qt's
  QProtobufDeserializerImpl is built on Qt's QProtobufDeserializerBase, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QProtobufDeserializerImpl that has a ritual and that
  Python can call so far, 4 names in all: 'reset', 'setError', 'skipVarint',
  'setUnexpectedEndOfStreamError'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has no ritual
  ------------------

  12 of the 16 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 forbidden;
  2 leans on 'QProtobufDeserializerImpl; 1 leans on
  'QtProtobufSerializerHelpers.

  What to expect
  --------------

  - The C++ QProtobufDeserializerImpl is created at the first use, not by
    'QProtobufDeserializerImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufDeserializerImpl.
  - Each name of Qt's QProtobufDeserializerImpl that has no cute function
    yet, '__init__', 'decodeHeader', 'skipField', 'skipLengthDelimited',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufDeserializerImpl'

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

  @overload(QAbstractProtobufSerializer.Error, str)
  def setError(
      self,
      error: QAbstractProtobufSerializer.Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QProtobufDeserializerImpl::setError(QAbstractProtobufSerializer::Error
    error, QAnyStringView errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufdeserializerimpl.html#setError

    Parameters
    ----------

    error : QAbstractProtobufSerializer.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProtobufDeserializerImpl::setError(QAbstractProtobufSerializer::
    #      Error error, QAnyStringView errorString)
    self.uglySide.call(
        'ritual_ZN25QProtobufDeserializerImpl8setErrorEN27QAbstractProtobuf'
        'Serializer5ErrorE14QAnyStringView',
        error.value, errorString,
    )

  def setUnexpectedEndOfStreamError(self) -> None:
    """
    Calls Qt's 'void
    QProtobufDeserializerImpl::setUnexpectedEndOfStreamError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufdeserializerimpl.html
    """
    #  void QProtobufDeserializerImpl::setUnexpectedEndOfStreamError()
    self.uglySide.call(
        'ritual_ZN25QProtobufDeserializerImpl29setUnexpectedEndOfStreamErro'
        'rEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QProtobufDeserializerImpl::QProtobufDeserializerImpl(
    QProtobufSerializerPrivate *parent)': leans on
    'QProtobufDeserializerImpl::nextFieldIndex(QProtobufMessage*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerImpl.__init__' has no cute function yet. "
        "Qt's "
        "'QProtobufDeserializerImpl::QProtobufDeserializerImpl(QProtobufSeri"
        "alizerPrivate *parent)': leans on "
        "'QProtobufDeserializerImpl::nextFieldIndex(QProtobufMessage*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QByteArrayView)
  def reset(self, data: QByteArrayView) -> None:
    """
    Calls Qt's 'void QProtobufDeserializerImpl::reset(QByteArrayView data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufdeserializerimpl.html#reset

    Parameters
    ----------

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void QProtobufDeserializerImpl::reset(QByteArrayView data)
    self.uglySide.call(
        'ritual_ZN25QProtobufDeserializerImpl5resetE14QByteArrayView',
        self._valueOf(data),
    )

  def skipVarint(self) -> None:
    """
    Calls Qt's 'void QProtobufDeserializerImpl::skipVarint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufdeserializerimpl.html#skipVarint
    """
    #  void QProtobufDeserializerImpl::skipVarint()
    self.uglySide.call('ritual_ZN25QProtobufDeserializerImpl10skipVarintEv')

  @staticmethod
  def decodeHeader(*__, **_) -> Never:
    """
    Qt's 'bool
    QProtobufDeserializerImpl::decodeHeader(QProtobufSelfcheckIterator &it,
    int &fieldIndex, QtProtobuf::WireTypes &wireType)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'deserializeVarintCommon'.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerImpl.decodeHeader' has no cute function yet. "
        "Qt's 'bool "
        "QProtobufDeserializerImpl::decodeHeader(QProtobufSelfcheckIterator "
        "&it, int &fieldIndex, QtProtobuf::WireTypes &wireType)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'deserializeVarintCommon'.")

  @staticmethod
  def skipField(*__, **_) -> Never:
    """
    Qt's 'qsizetype QProtobufDeserializerImpl::skipField(const
    QProtobufSelfcheckIterator &fieldBegin)': leans on
    'QProtobufDeserializerImpl::skipLengthDelimited()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerImpl.skipField' has no cute function yet. "
        "Qt's 'qsizetype QProtobufDeserializerImpl::skipField(const "
        "QProtobufSelfcheckIterator &fieldBegin)': leans on "
        "'QProtobufDeserializerImpl::skipLengthDelimited()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def skipLengthDelimited(*__, **_) -> Never:
    """
    Qt's 'void QProtobufDeserializerImpl::skipLengthDelimited()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'deserializeVarintCommon'.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerImpl.skipLengthDelimited' has no cute "
        "function yet. Qt's 'void "
        "QProtobufDeserializerImpl::skipLengthDelimited()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'deserializeVarintCommon'.")
