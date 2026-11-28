"""
QDBusMetaType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusmetatype.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaType = WAIT['QMetaType']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusMetaType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusMetaType: a plain Python object standing in
  front of one C++ QDBusMetaType.

  C++ hands a QDBusMetaType around as a copy, so every C++ QDBusMetaType
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusMetaType that has a ritual and that Python can
  call so far, 3 names in all: 'registerCustomType', 'signatureToMetaType',
  'typeToSignature'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QDBusMetaType::registerMarshallOperators(QMetaType typeId,
    MarshallFunction a1, DemarshallFunction a2)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QDBusMetaType::marshall(QDBusArgument &a0, QMetaType id, const
    void *data)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QDBusMetaType::demarshall(const QDBusArgument &a0, QMetaType
    id, void *data)': names 'void', which has no cute class yet.
  - Qt's 'QDBusMetaType::~QDBusMetaType()': the destructor: Python removes
    its C++ QDBusMetaType by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDBusMetaType is created at the first use, not by
    'QDBusMetaType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusMetaType back gives a copy the ritual made for
    Python, in a new cute QDBusMetaType.
  - Each name of Qt's QDBusMetaType that has no cute function yet,
    'demarshall', 'marshall', 'registerMarshallOperators', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMetaType, QByteArray)
  def registerCustomType(type: QMetaType, signature: QByteArray) -> None:
    """
    Calls Qt's 'void QDBusMetaType::registerCustomType(QMetaType type, const
    QByteArray &signature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmetatype.html#registerCustomType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    signature : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QDBusMetaType::registerCustomType(QMetaType type, const
    #      QByteArray &signature)
    Rituals.call(
        'ritual_ZN13QDBusMetaType18registerCustomTypeE9QMetaTypeRK10QByteAr'
        'ray',
        CuteMixin._valueOf(type), CuteMixin._valueOf(signature),
    )

  @staticmethod
  @overload(str)
  @overload(NoneType)
  def signatureToMetaType(signature: Optional[str]) -> QMetaType:
    """
    Calls Qt's 'QMetaType QDBusMetaType::signatureToMetaType(const char
    *signature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmetatype.html#signatureToMetaType

    Parameters
    ----------

    signature : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QDBusMetaType::signatureToMetaType(const char *signature)
    address = Rituals.call(
        'ritual_ZN13QDBusMetaType19signatureToMetaTypeEPKc',
        CuteMixin._bytesOf(signature),
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def typeToSignature(type: QMetaType) -> Optional[str]:
    """
    Calls Qt's 'const char *QDBusMetaType::typeToSignature(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmetatype.html#typeToSignature

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QDBusMetaType::typeToSignature(QMetaType type)
    chars = Rituals.call(
        'ritual_ZN13QDBusMetaType15typeToSignatureE9QMetaType',
        CuteMixin._valueOf(type),
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMetaType'

  #  Qt's '~QDBusMetaType()'. Naming it makes this a value class: Python owns
  #  every C++ QDBusMetaType behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QDBusMetaTypeD1Ev'

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

  @staticmethod
  def demarshall(*__, **_) -> Never:
    """
    Qt's 'bool QDBusMetaType::demarshall(const QDBusArgument &a0, QMetaType
    id, void *data)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDBusMetaType.demarshall' has no cute function yet. Qt's 'bool "
        "QDBusMetaType::demarshall(const QDBusArgument &a0, QMetaType id, "
        "void *data)': names 'void', which has no cute class yet.")

  @staticmethod
  def marshall(*__, **_) -> Never:
    """
    Qt's 'bool QDBusMetaType::marshall(QDBusArgument &a0, QMetaType id, const
    void *data)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusMetaType.marshall' has no cute function yet. Qt's 'bool "
        "QDBusMetaType::marshall(QDBusArgument &a0, QMetaType id, const "
        "void *data)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def registerMarshallOperators(*__, **_) -> Never:
    """
    Qt's 'void QDBusMetaType::registerMarshallOperators(QMetaType typeId,
    MarshallFunction a1, DemarshallFunction a2)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusMetaType.registerMarshallOperators' has no cute function "
        "yet. Qt's 'void QDBusMetaType::registerMarshallOperators(QMetaType "
        "typeId, MarshallFunction a1, DemarshallFunction a2)': takes a type "
        "Python has no way to hand over yet.")
