"""
QProtobufSerializerImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QProtobufSerializerImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QProtobufSerializerBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QProtobufMessage, QProtobufSerializerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QProtobufMessage = WAIT['QProtobufMessage']
  QProtobufSerializerPrivate = WAIT['QProtobufSerializerPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProtobufSerializerImpl(QProtobufSerializerBase):
  """
  The cute side of Qt's QProtobufSerializerImpl: a plain Python object
  standing in front of one C++ QProtobufSerializerImpl.

  It is built on the cute 'QProtobufSerializerBase', as Qt's
  QProtobufSerializerImpl is built on Qt's QProtobufSerializerBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QProtobufSerializerImpl that has a ritual and that
  Python can call so far, 4 names in all: 'result', 'reset',
  'serializeUnknownFields', 'serializeMessageFieldBegin'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProtobufSerializerImpl::~QProtobufSerializerImpl()': the
    destructor: Python never removes a C++ QProtobufSerializerImpl.

  What has no ritual
  ------------------

  8 of the 14 functions Qt declares: 4 forbidden; 4 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QProtobufSerializerImpl is created at the first use, not by
    'QProtobufSerializerImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufSerializerImpl.
  - Each name of Qt's QProtobufSerializerImpl that has no cute function yet,
    'encodeHeader', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufSerializerImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def result(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QProtobufSerializerImpl::result() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerimpl.html#result

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QProtobufSerializerImpl::result() const
    address = self.uglySide.call(
        'ritual_ZNK23QProtobufSerializerImpl6resultEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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

  @overload(QProtobufSerializerPrivate)
  @overload(NoneType)
  def __init__(self, parent: Optional[QProtobufSerializerPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QProtobufSerializerImpl::QProtobufSerializerImpl(
    QProtobufSerializerPrivate *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerimpl.html

    Parameters
    ----------

    parent : Optional[QProtobufSerializerPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QProtobufSerializerImpl::QProtobufSerializerImpl(
    #      QProtobufSerializerPrivate *parent)
    self._noteCreation(QProtobufSerializerImpl, lambda: Rituals.call(
        'ritual_ZN23QProtobufSerializerImplC1EP26QProtobufSerializerPrivate',
        self._addressOf(parent),
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QProtobufSerializerImpl::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufserializerimpl.html#reset
    """
    #  void QProtobufSerializerImpl::reset()
    self.uglySide.call('ritual_ZN23QProtobufSerializerImpl5resetEv')

  @overload(QProtobufMessage)
  @overload(NoneType)
  def serializeUnknownFields(
      self,
      message: Optional[QProtobufMessage],
  ) -> None:
    """
    Calls Qt's 'void QProtobufSerializerImpl::serializeUnknownFields(const
    QProtobufMessage *message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerimpl.html

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProtobufSerializerImpl::serializeUnknownFields(const
    #      QProtobufMessage *message)
    self.uglySide.call(
        'ritual_ZN23QProtobufSerializerImpl22serializeUnknownFieldsEPK16QPr'
        'otobufMessage',
        self._addressOf(message),
    )

  def serializeMessageFieldBegin(self) -> None:
    """
    Calls Qt's 'void QProtobufSerializerImpl::serializeMessageFieldBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerimpl.html
    """
    #  void QProtobufSerializerImpl::serializeMessageFieldBegin()
    self.uglySide.call(
        'ritual_ZN23QProtobufSerializerImpl26serializeMessageFieldBeginEv',
    )

  @staticmethod
  def encodeHeader(*__, **_) -> Never:
    """
    Qt's 'QByteArray QProtobufSerializerImpl::encodeHeader(int fieldNumber,
    QtProtobuf::WireTypes wireType)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'serializeVarintCommon'.
    """
    raise NotImplementedError(
        "'QProtobufSerializerImpl.encodeHeader' has no cute function yet. "
        "Qt's 'QByteArray QProtobufSerializerImpl::encodeHeader(int "
        "fieldNumber, QtProtobuf::WireTypes wireType)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'serializeVarintCommon'.")
