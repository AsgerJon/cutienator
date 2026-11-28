"""
QGrpcSerializationFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcserializationformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArrayView, QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QGrpcSerializationFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGrpcSerializationFormat: a plain Python object
  standing in front of one C++ QGrpcSerializationFormat.

  C++ hands a QGrpcSerializationFormat around as a copy, so every C++
  QGrpcSerializationFormat behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGrpcSerializationFormat that has a ritual and that
  Python can call so far, 4 names in all: 'suffix', '__eq__', '__ne__',
  '__rlshift__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcSerializationFormat::QGrpcSerializationFormat(QByteArrayView
    suffix, std::shared_ptr<QAbstractProtobufSerializer> serializer)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QGrpcSerializationFormat::~QGrpcSerializationFormat()': the
    destructor: Python removes its C++ QGrpcSerializationFormat by it, and
    has no other use for it.
  - Qt's 'QGrpcSerializationFormat &QGrpcSerializationFormat::operator=(const
    QGrpcSerializationFormat &a0)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QGrpcSerializationFormat::QGrpcSerializationFormat(
    QGrpcSerializationFormat &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QGrpcSerializationFormat
    &QGrpcSerializationFormat::operator=(QGrpcSerializationFormat &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QGrpcSerializationFormat::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'void QGrpcSerializationFormat::swap(QGrpcSerializationFormat
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'std::shared_ptr<QAbstractProtobufSerializer>
    QGrpcSerializationFormat::serializer() const': gives a type Python has no
    way to take yet.
  - Qt's 'QGrpcSerializationFormatPrivate
    *QGrpcSerializationFormat::d_func()': gives
    'QGrpcSerializationFormatPrivate', which has no cute class yet.
  - Qt's 'const QGrpcSerializationFormatPrivate
    *QGrpcSerializationFormat::d_func() const': gives
    'QGrpcSerializationFormatPrivate', which has no cute class yet.

  What to expect
  --------------

  - The C++ QGrpcSerializationFormat is created at the first use, not by
    'QGrpcSerializationFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGrpcSerializationFormat back gives a copy the ritual
    made for Python, in a new cute QGrpcSerializationFormat.
  - Each name of Qt's QGrpcSerializationFormat that has no cute function yet,
    'd_func', 'serializer', 'swap', holds a function that raises
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
  __qt_class__ = 'QGrpcSerializationFormat'

  #  Qt's '~QGrpcSerializationFormat()'. Naming it makes this a value class:
  #  Python owns every C++ QGrpcSerializationFormat behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QGrpcSerializationFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def suffix(self) -> QByteArrayView:
    """
    Calls Qt's 'QByteArrayView QGrpcSerializationFormat::suffix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcserializationformat.html#suffix

    Returns
    -------

    QByteArrayView
      A new cute QByteArrayView around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayView QGrpcSerializationFormat::suffix() const
    address = self.uglySide.call(
        'ritual_ZNK24QGrpcSerializationFormat6suffixEv',
    )
    from ..QtCore import QByteArrayView
    return QByteArrayView._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGrpcSerializationFormat) -> bool:
    """
    Calls Qt's 'bool operator==(const QGrpcSerializationFormat &lhs, const
    QGrpcSerializationFormat &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcserializationformat.html#operator==

    Parameters
    ----------

    rhs : QGrpcSerializationFormat
      Passed on as a value: Qt reads the C++ QGrpcSerializationFormat, which
      stays Python's own.
    """
    #  bool operator==(const QGrpcSerializationFormat &lhs, const
    #      QGrpcSerializationFormat &rhs)
    return Rituals.call(
        'ritual_ZeqRK24QGrpcSerializationFormatS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QGrpcSerializationFormat) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGrpcSerializationFormat &lhs, const
    QGrpcSerializationFormat &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcserializationformat.html#operator!=

    Parameters
    ----------

    rhs : QGrpcSerializationFormat
      Passed on as a value: Qt reads the C++ QGrpcSerializationFormat, which
      stays Python's own.
    """
    #  bool operator!=(const QGrpcSerializationFormat &lhs, const
    #      QGrpcSerializationFormat &rhs)
    return Rituals.call(
        'ritual_ZneRK24QGrpcSerializationFormatS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const
    QGrpcSerializationFormat &sfmt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcserializationformat.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QGrpcSerializationFormat &sfmt)
    address = Rituals.call(
        'ritual_Zls6QDebugRK24QGrpcSerializationFormat',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtGrpc.SerializationFormat)
  def __init__(self, format: QtGrpc.SerializationFormat) -> None:
    """
    Notes what was given, for Qt's
    'QGrpcSerializationFormat::QGrpcSerializationFormat(QtGrpc::
    SerializationFormat format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcserializationformat.html

    Parameters
    ----------

    format : QtGrpc.SerializationFormat
      Passed on as its number.
    """
    #  QGrpcSerializationFormat::QGrpcSerializationFormat(QtGrpc::
    #      SerializationFormat format)
    self._noteCreation(QGrpcSerializationFormat, lambda: Rituals.call(
        'ritual_ZN24QGrpcSerializationFormatC1EN6QtGrpc19SerializationForma'
        'tE',
        format.value,
    ))

  @overload(THIS)
  def __init__(self, a0: QGrpcSerializationFormat) -> None:
    """
    Notes what was given, for Qt's
    'QGrpcSerializationFormat::QGrpcSerializationFormat(const
    QGrpcSerializationFormat &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcserializationformat.html

    Parameters
    ----------

    a0 : QGrpcSerializationFormat
      Passed on as a value: Qt reads the C++ QGrpcSerializationFormat, which
      stays Python's own.
    """
    #  QGrpcSerializationFormat::QGrpcSerializationFormat(const
    #      QGrpcSerializationFormat &a0)
    self._noteCreation(QGrpcSerializationFormat, lambda: Rituals.call(
        'ritual_ZN24QGrpcSerializationFormatC1ERKS_', self._valueOf(a0),
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

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QGrpcSerializationFormatPrivate
      *QGrpcSerializationFormat::d_func()': gives
      'QGrpcSerializationFormatPrivate', which has no cute class yet.
    - Qt's 'const QGrpcSerializationFormatPrivate
      *QGrpcSerializationFormat::d_func() const': gives
      'QGrpcSerializationFormatPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGrpcSerializationFormat.d_func' has no cute function yet. Qt's "
        "'QGrpcSerializationFormatPrivate "
        "*QGrpcSerializationFormat::d_func()': gives "
        "'QGrpcSerializationFormatPrivate', which has no cute class yet. "
        "Qt's 'const QGrpcSerializationFormatPrivate "
        "*QGrpcSerializationFormat::d_func() const': gives "
        "'QGrpcSerializationFormatPrivate', which has no cute class yet.")

  @staticmethod
  def serializer(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QAbstractProtobufSerializer>
    QGrpcSerializationFormat::serializer() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcSerializationFormat.serializer' has no cute function yet. "
        "Qt's 'std::shared_ptr<QAbstractProtobufSerializer> "
        "QGrpcSerializationFormat::serializer() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGrpcSerializationFormat::swap(QGrpcSerializationFormat
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcSerializationFormat.swap' has no cute function yet. Qt's "
        "'void QGrpcSerializationFormat::swap(QGrpcSerializationFormat "
        "&other)': takes a type Python has no way to hand over yet.")
