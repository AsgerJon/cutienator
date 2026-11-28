"""
QCborContainerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qcborvalue_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QCborContainerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QCborValue, QSharedData, QtCbor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QByteArray, QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLatin1String = WAIT['QLatin1String']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCborContainerPrivate(QSharedData):
  """
  The cute side of Qt's QCborContainerPrivate: a plain Python object standing
  in front of one C++ QCborContainerPrivate.

  It is built on the cute 'QSharedData', as Qt's QCborContainerPrivate is
  built on Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCborContainerPrivate that has a ritual and that
  Python can call so far, 14 names in all: 'addByteData', 'byteData',
  'containerAt', 'append', 'appendByteData', 'appendAsciiString',
  'appendUtf8String', 'appendNonAsciiString', 'byteArrayAt', 'stringAt',
  'anyStringViewAt', 'makeValue', 'valueAt', 'elementFromValue'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborContainerPrivate::QCborContainerPrivate(const
    QCborContainerPrivate &a0)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QCborContainerPrivate::QCborContainerPrivate(QCborContainerPrivate
    &&a0)': takes a type Python has no way to hand over yet.
  - Qt's 'qptrdiff QCborContainerPrivate::addByteDataImpl(QByteArray &target,
    QByteArray::size_type &targetUsed, const char *block, qsizetype len)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QCborContainerPrivate::append(QCborTag tag)': names the enum
    'QCborTag', whose class cannot be named here.
  - Qt's 'void QCborContainerPrivate::resetValue(QCborValue &v)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  36 of the 59 functions Qt declares: 12 leans on 'QCborContainerPrivate; 11
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 9 a template; 2 forbidden; 2 leans on 'QUtf8.

  What to expect
  --------------

  - The C++ QCborContainerPrivate is created at the first use, not by
    'QCborContainerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCborContainerPrivate.
  - Each name of Qt's QCborContainerPrivate that has no cute function yet,
    'addByteDataImpl', 'clone', 'compact', 'compareElement',
    'compareElement_helper', 'compareUtf8', 'decodeStringFromCbor',
    'decodeValueFromCbor', 'deref', 'detach', 'extractAt',
    'extractAt_complex', 'findCborMapKey', 'findOrAddMapKey', 'grow',
    'insertAt', 'removeAt', 'replaceAt', 'replaceAt_complex',
    'replaceAt_internal', 'resetValue', 'setErrorInReader',
    'stringCompareElement', 'stringEqualsElement', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QCborContainerPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ContainerDisposition(CuteNum):
    """
    The enum 'QCborContainerPrivate::ContainerDisposition' of Qt, with the 2
    names Qt gives in it.
    """

    CopyContainer = Kee[int](0)
    MoveContainer = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QCborValue.Type, int)
  @overload(QCborValue.Type, int, THIS)
  @overload(QCborValue.Type, int, NoneType)
  @overload(QCborValue.Type, int, THIS, ContainerDisposition)
  @overload(QCborValue.Type, int, NoneType, ContainerDisposition)
  def makeValue(
      type: QCborValue.Type,
      n: int,
      d: Optional[QCborContainerPrivate] = None,
      disp: ContainerDisposition = ContainerDisposition.CopyContainer,
  ) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborContainerPrivate::makeValue(QCborValue::Type
    type, qint64 n, QCborContainerPrivate *d, ContainerDisposition disp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#makeValue

    Parameters
    ----------

    type : QCborValue.Type
      Passed on as its number.

    n : int
      Passed on as it is.

    d : Optional[QCborContainerPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    disp : ContainerDisposition
      Passed on as its number. May be left out, as in Qt: it is then
      ContainerDisposition.CopyContainer.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborContainerPrivate::makeValue(QCborValue::Type type,
    #      qint64 n, QCborContainerPrivate *d, ContainerDisposition disp)
    address = Rituals.call(
        'ritual_ZN21QCborContainerPrivate9makeValueEN10QCborValue4TypeExPS_'
        'NS_20ContainerDispositionE',
        type.value, n, CuteMixin._addressOf(d), disp.value,
    )
    return QCborValue._cuteOwning(address)

  @staticmethod
  @overload(QCborValue)
  def elementFromValue(value: QCborValue) -> QtCbor.Element:
    """
    Calls Qt's 'QtCbor::Element QCborContainerPrivate::elementFromValue(const
    QCborValue &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#elementFromValue

    Parameters
    ----------

    value : QCborValue
      Passed on as a value: Qt reads the C++ QCborValue, which stays Python's
      own.

    Returns
    -------

    QtCbor.Element
      A new cute QtCbor::Element around the copy Qt gave back. Python owns
      it.
    """
    #  QtCbor::Element QCborContainerPrivate::elementFromValue(const
    #      QCborValue &value)
    address = Rituals.call(
        'ritual_ZN21QCborContainerPrivate16elementFromValueERK10QCborValue',
        CuteMixin._valueOf(value),
    )
    return QtCbor.Element._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCborContainerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QtCbor.Element'])
  def byteData(self, e: QtCbor.Element) -> Optional[QtCbor.ByteData]:
    """
    Calls Qt's 'const QtCbor::ByteData
    *QCborContainerPrivate::byteData(QtCbor::Element e) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#byteData

    Parameters
    ----------

    e : QtCbor.Element
      Passed on as a value: Qt reads the C++ QtCbor::Element, which stays
      Python's own.

    Returns
    -------

    Optional[QtCbor.ByteData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QtCbor::ByteData
    #      *QCborContainerPrivate::byteData(QtCbor::Element e) const
    address = self.uglySide.call(
        'ritual_ZNK21QCborContainerPrivate8byteDataEN6QtCbor7ElementE',
        self._valueOf(e),
    )
    return QtCbor.ByteData._cuteAt(address)

  @overload(int)
  def byteData(self, idx: int) -> Optional[QtCbor.ByteData]:
    """
    Calls Qt's 'const QtCbor::ByteData
    *QCborContainerPrivate::byteData(qsizetype idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#byteData

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QtCbor.ByteData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QtCbor::ByteData *QCborContainerPrivate::byteData(qsizetype idx)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QCborContainerPrivate8byteDataEx', idx,
    )
    return QtCbor.ByteData._cuteAt(address)

  @overload(int, QCborValue.Type)
  def containerAt(
      self,
      idx: int,
      type: QCborValue.Type,
  ) -> Optional[QCborContainerPrivate]:
    """
    Calls Qt's 'QCborContainerPrivate
    *QCborContainerPrivate::containerAt(qsizetype idx, QCborValue::Type type)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#containerAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    type : QCborValue.Type
      Passed on as its number.

    Returns
    -------

    Optional[QCborContainerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCborContainerPrivate *QCborContainerPrivate::containerAt(qsizetype
    #      idx, QCborValue::Type type) const
    address = self.uglySide.call(
        'ritual_ZNK21QCborContainerPrivate11containerAtExN10QCborValue4Type'
        'E',
        idx, type.value,
    )
    return QCborContainerPrivate._cuteAt(address)

  @overload(int)
  def byteArrayAt(self, idx: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCborContainerPrivate::byteArrayAt(qsizetype idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#byteArrayAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCborContainerPrivate::byteArrayAt(qsizetype idx) const
    address = self.uglySide.call(
        'ritual_ZNK21QCborContainerPrivate11byteArrayAtEx', idx,
    )
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def stringAt(self, idx: int) -> str:
    """
    Calls Qt's 'QString QCborContainerPrivate::stringAt(qsizetype idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#stringAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCborContainerPrivate::stringAt(qsizetype idx) const
    return self.uglySide.call(
        'ritual_ZNK21QCborContainerPrivate8stringAtEx', idx,
    )

  @overload(int)
  def anyStringViewAt(self, idx: int) -> str:
    """
    Calls Qt's 'QAnyStringView
    QCborContainerPrivate::anyStringViewAt(qsizetype idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#anyStringViewAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QCborContainerPrivate::anyStringViewAt(qsizetype idx)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QCborContainerPrivate15anyStringViewAtEx', idx,
    )

  @overload(int)
  def valueAt(self, idx: int) -> QCborValue:
    """
    Calls Qt's 'QCborValue QCborContainerPrivate::valueAt(qsizetype idx)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcborcontainerprivate.html#valueAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QCborContainerPrivate::valueAt(qsizetype idx) const
    address = self.uglySide.call(
        'ritual_ZNK21QCborContainerPrivate7valueAtEx', idx,
    )
    return QCborValue._cuteOwning(address)

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
    'QCborContainerPrivate::QCborContainerPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#QCborContainerPrivate
    """
    #  QCborContainerPrivate::QCborContainerPrivate()
    self._noteCreation(QCborContainerPrivate, lambda: Rituals.call(
        'ritual_ZN21QCborContainerPrivateC1Ev',
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

  @overload(str, int)
  @overload(NoneType, int)
  def addByteData(self, block: Optional[str], len: int) -> int:
    """
    Calls Qt's 'qptrdiff QCborContainerPrivate::addByteData(const char
    *block, qsizetype len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#addByteData

    Parameters
    ----------

    block : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  qptrdiff QCborContainerPrivate::addByteData(const char *block,
    #      qsizetype len)
    return self.uglySide.call(
        'ritual_ZN21QCborContainerPrivate11addByteDataEPKcx',
        self._bytesOf(block), len,
    )

  @overload(WAIT['QtCbor.Undefined'])
  def append(self, a0: QtCbor.Undefined) -> None:
    """
    Calls Qt's 'void QCborContainerPrivate::append(QtCbor::Undefined a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborcontainerprivate.html#append

    Parameters
    ----------

    a0 : QtCbor.Undefined
      Passed on as a value: Qt reads the C++ QtCbor::Undefined, which stays
      Python's own.
    """
    #  void QCborContainerPrivate::append(QtCbor::Undefined a0)
    self.uglySide.call(
        'ritual_ZN21QCborContainerPrivate6appendEN6QtCbor9UndefinedE',
        self._valueOf(a0),
    )

  @overload(int)
  def append(self, value: int) -> None:
    """
    Calls Qt's 'void QCborContainerPrivate::append(qint64 value)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborcontainerprivate.html#append

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCborContainerPrivate::append(qint64 value)
    self.uglySide.call('ritual_ZN21QCborContainerPrivate6appendEx', value)

  @overload(QLatin1String)
  def append(self, s: QLatin1String) -> None:
    """
    Calls Qt's 'void QCborContainerPrivate::append(QLatin1StringView s)'.

    Qt's own words: https://doc.qt.io/qt-6/qcborcontainerprivate.html#append

    Parameters
    ----------

    s : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.
    """
    #  void QCborContainerPrivate::append(QLatin1StringView s)
    self.uglySide.call(
        'ritual_ZN21QCborContainerPrivate6appendE13QLatin1String',
        self._valueOf(s),
    )

  @overload(str, int, QCborValue.Type)
  @overload(NoneType, int, QCborValue.Type)
  @overload(str, int, QCborValue.Type, QtCbor.Element.ValueFlags)
  @overload(NoneType, int, QCborValue.Type, QtCbor.Element.ValueFlags)
  def appendByteData(
      self,
      data: Optional[str],
      len: int,
      type: QCborValue.Type,
      extraFlags: QtCbor.Element.ValueFlags = QtCbor.Element.ValueFlags(),
  ) -> None:
    """
    Calls Qt's 'void QCborContainerPrivate::appendByteData(const char *data,
    qsizetype len, QCborValue::Type type, QtCbor::Element::ValueFlags
    extraFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#appendByteData

    Parameters
    ----------

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.

    type : QCborValue.Type
      Passed on as its number.

    extraFlags : QtCbor.Element.ValueFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QtCbor.Element.ValueFlags().
    """
    #  void QCborContainerPrivate::appendByteData(const char *data, qsizetype
    #      len, QCborValue::Type type, QtCbor::Element::ValueFlags
    #      extraFlags)
    self.uglySide.call(
        'ritual_ZN21QCborContainerPrivate14appendByteDataEPKcxN10QCborValue'
        '4TypeE6QFlagsIN6QtCbor7Element9ValueFlagEE',
        self._bytesOf(data), len, type.value, extraFlags.value,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def appendAsciiString(self, str: Optional[str], len: int) -> None:
    """
    Calls Qt's 'void QCborContainerPrivate::appendAsciiString(const char
    *str, qsizetype len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#appendAsciiString

    Parameters
    ----------

    str : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  void QCborContainerPrivate::appendAsciiString(const char *str,
    #      qsizetype len)
    self.uglySide.call(
        'ritual_ZN21QCborContainerPrivate17appendAsciiStringEPKcx',
        self._bytesOf(str), len,
    )

  @overload(str, int)
  @overload(NoneType, int)
  def appendUtf8String(self, str: Optional[str], len: int) -> None:
    """
    Calls Qt's 'void QCborContainerPrivate::appendUtf8String(const char *str,
    qsizetype len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#appendUtf8String

    Parameters
    ----------

    str : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    len : int
      Passed on as it is.
    """
    #  void QCborContainerPrivate::appendUtf8String(const char *str,
    #      qsizetype len)
    self.uglySide.call(
        'ritual_ZN21QCborContainerPrivate16appendUtf8StringEPKcx',
        self._bytesOf(str), len,
    )

  @overload(str)
  def appendNonAsciiString(self, s: str) -> None:
    """
    Calls Qt's 'void QCborContainerPrivate::appendNonAsciiString(QStringView
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcborcontainerprivate.html#appendNonAsciiString

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCborContainerPrivate::appendNonAsciiString(QStringView s)
    self.uglySide.call(
        'ritual_ZN21QCborContainerPrivate20appendNonAsciiStringE11QStringVi'
        'ew',
        s,
    )

  @staticmethod
  def addByteDataImpl(*__, **_) -> Never:
    """
    Qt's 'qptrdiff QCborContainerPrivate::addByteDataImpl(QByteArray &target,
    QByteArray::size_type &targetUsed, const char *block, qsizetype len)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.addByteDataImpl' has no cute function yet. "
        "Qt's 'qptrdiff QCborContainerPrivate::addByteDataImpl(QByteArray "
        "&target, QByteArray::size_type &targetUsed, const char *block, "
        "qsizetype len)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def clone(*__, **_) -> Never:
    """
    Qt's 'QCborContainerPrivate
    *QCborContainerPrivate::clone(QCborContainerPrivate *d, qsizetype
    reserved)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'Element'.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.clone' has no cute function yet. Qt's "
        "'QCborContainerPrivate "
        "*QCborContainerPrivate::clone(QCborContainerPrivate *d, qsizetype "
        "reserved)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'Element'.")

  @staticmethod
  def compact(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::compact()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'Element'.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.compact' has no cute function yet. Qt's "
        "'void QCborContainerPrivate::compact()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'Element'.")

  @staticmethod
  def compareElement(*__, **_) -> Never:
    """
    Qt's 'int QCborContainerPrivate::compareElement(qsizetype idx, const
    QCborValue &value, QtCbor::Comparison mode) const': leans on
    'QCborContainerPrivate::compareElement_helper(QCborContainerPrivate
    const*, QtCbor::Element, QCborContainerPrivate const*, QtCbor::Element,
    QtCbor::Comparison)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.compareElement' has no cute function yet. "
        "Qt's 'int QCborContainerPrivate::compareElement(qsizetype idx, "
        "const QCborValue &value, QtCbor::Comparison mode) const': leans on "
        "'QCborContainerPrivate::compareElement_helper(QCborContainerPrivate"
        " const*, QtCbor::Element, QCborContainerPrivate const*, "
        "QtCbor::Element, QtCbor::Comparison)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def compareElement_helper(*__, **_) -> Never:
    """
    Qt's 'int QCborContainerPrivate::compareElement_helper(const
    QCborContainerPrivate *c1, QtCbor::Element e1, const
    QCborContainerPrivate *c2, QtCbor::Element e2, QtCbor::Comparison mode)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'Element'.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.compareElement_helper' has no cute function "
        "yet. Qt's 'int QCborContainerPrivate::compareElement_helper(const "
        "QCborContainerPrivate *c1, QtCbor::Element e1, const "
        "QCborContainerPrivate *c2, QtCbor::Element e2, QtCbor::Comparison "
        "mode)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'Element'.")

  @staticmethod
  def compareUtf8(*__, **_) -> Never:
    """
    - Qt's 'int QCborContainerPrivate::compareUtf8(const QtCbor::ByteData *b,
      QLatin1StringView s)': leans on 'QUtf8::compareUtf8(QByteArrayView,
      QLatin1String, Qt::CaseSensitivity)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    - Qt's 'int QCborContainerPrivate::compareUtf8(const QtCbor::ByteData *b,
      QStringView s)': leans on 'QUtf8::compareUtf8(QByteArrayView,
      QStringView, Qt::CaseSensitivity)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.compareUtf8' has no cute function yet. Qt's "
        "'int QCborContainerPrivate::compareUtf8(const QtCbor::ByteData *b, "
        "QLatin1StringView s)': leans on "
        "'QUtf8::compareUtf8(QByteArrayView, QLatin1String, "
        "Qt::CaseSensitivity)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken. Qt's 'int "
        "QCborContainerPrivate::compareUtf8(const QtCbor::ByteData *b, "
        "QStringView s)': leans on 'QUtf8::compareUtf8(QByteArrayView, "
        "QStringView, Qt::CaseSensitivity)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def decodeStringFromCbor(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::decodeStringFromCbor(QCborStreamReader
    &reader)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'Element'.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.decodeStringFromCbor' has no cute function "
        "yet. Qt's 'void "
        "QCborContainerPrivate::decodeStringFromCbor(QCborStreamReader "
        "&reader)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'Element'.")

  @staticmethod
  def decodeValueFromCbor(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::decodeValueFromCbor(QCborStreamReader
    &reader, int remainingStackDepth)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'decodeBasicValueFromCbor'.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.decodeValueFromCbor' has no cute function "
        "yet. Qt's 'void "
        "QCborContainerPrivate::decodeValueFromCbor(QCborStreamReader "
        "&reader, int remainingStackDepth)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'decodeBasicValueFromCbor'.")

  @staticmethod
  def deref(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::deref()': leans on
    'QCborContainerPrivate::~QCborContainerPrivate()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.deref' has no cute function yet. Qt's 'void "
        "QCborContainerPrivate::deref()': leans on "
        "'QCborContainerPrivate::~QCborContainerPrivate()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def detach(*__, **_) -> Never:
    """
    Qt's 'QCborContainerPrivate
    *QCborContainerPrivate::detach(QCborContainerPrivate *d, qsizetype
    reserved)': leans on
    'QCborContainerPrivate::clone(QCborContainerPrivate*, long long)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.detach' has no cute function yet. Qt's "
        "'QCborContainerPrivate "
        "*QCborContainerPrivate::detach(QCborContainerPrivate *d, qsizetype "
        "reserved)': leans on "
        "'QCborContainerPrivate::clone(QCborContainerPrivate*, long long)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def extractAt(*__, **_) -> Never:
    """
    Qt's 'QCborValue QCborContainerPrivate::extractAt(qsizetype idx)': leans
    on 'QCborContainerPrivate::extractAt_complex(QtCbor::Element)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.extractAt' has no cute function yet. Qt's "
        "'QCborValue QCborContainerPrivate::extractAt(qsizetype idx)': "
        "leans on "
        "'QCborContainerPrivate::extractAt_complex(QtCbor::Element)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def extractAt_complex(*__, **_) -> Never:
    """
    Qt's 'QCborValue QCborContainerPrivate::extractAt_complex(QtCbor::Element
    e)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: unknown type name 'Element'.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.extractAt_complex' has no cute function "
        "yet. Qt's 'QCborValue "
        "QCborContainerPrivate::extractAt_complex(QtCbor::Element e)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'Element'.")

  @staticmethod
  def findCborMapKey(*__, **_) -> Never:
    """
    Qt's 'QCborContainerPrivate::findCborMapKey': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.findCborMapKey' has no cute function yet. "
        "Qt's 'QCborContainerPrivate::findCborMapKey': a template: a "
        "pattern and no single function.")

  @staticmethod
  def findOrAddMapKey(*__, **_) -> Never:
    """
    Qt's 'QCborContainerPrivate::findOrAddMapKey': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.findOrAddMapKey' has no cute function yet. "
        "Qt's 'QCborContainerPrivate::findOrAddMapKey': a template: a "
        "pattern and no single function.")

  @staticmethod
  def grow(*__, **_) -> Never:
    """
    Qt's 'QCborContainerPrivate
    *QCborContainerPrivate::grow(QCborContainerPrivate *d, qsizetype index)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'Undefined';
    did you mean 'QtCbor::Undefined'?.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.grow' has no cute function yet. Qt's "
        "'QCborContainerPrivate "
        "*QCborContainerPrivate::grow(QCborContainerPrivate *d, qsizetype "
        "index)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'Undefined'; did you mean 'QtCbor::Undefined'?.")

  @staticmethod
  def insertAt(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::insertAt(qsizetype idx, const
    QCborValue &value, ContainerDisposition disp)': leans on
    'QCborContainerPrivate::replaceAt_complex(QtCbor::Element&, QCborValue
    const&, QCborContainerPrivate::ContainerDisposition)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.insertAt' has no cute function yet. Qt's "
        "'void QCborContainerPrivate::insertAt(qsizetype idx, const "
        "QCborValue &value, ContainerDisposition disp)': leans on "
        "'QCborContainerPrivate::replaceAt_complex(QtCbor::Element&, "
        "QCborValue const&, QCborContainerPrivate::ContainerDisposition)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def removeAt(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::removeAt(qsizetype idx)': leans on
    'QCborContainerPrivate::replaceAt_complex(QtCbor::Element&, QCborValue
    const&, QCborContainerPrivate::ContainerDisposition)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.removeAt' has no cute function yet. Qt's "
        "'void QCborContainerPrivate::removeAt(qsizetype idx)': leans on "
        "'QCborContainerPrivate::replaceAt_complex(QtCbor::Element&, "
        "QCborValue const&, QCborContainerPrivate::ContainerDisposition)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def replaceAt(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::replaceAt(qsizetype idx, const
    QCborValue &value, ContainerDisposition disp)': leans on
    'QCborContainerPrivate::replaceAt_complex(QtCbor::Element&, QCborValue
    const&, QCborContainerPrivate::ContainerDisposition)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.replaceAt' has no cute function yet. Qt's "
        "'void QCborContainerPrivate::replaceAt(qsizetype idx, const "
        "QCborValue &value, ContainerDisposition disp)': leans on "
        "'QCborContainerPrivate::replaceAt_complex(QtCbor::Element&, "
        "QCborValue const&, QCborContainerPrivate::ContainerDisposition)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def replaceAt_complex(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::replaceAt_complex(QtCbor::Element &e,
    const QCborValue &value, ContainerDisposition disp)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'Element'.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.replaceAt_complex' has no cute function "
        "yet. Qt's 'void "
        "QCborContainerPrivate::replaceAt_complex(QtCbor::Element &e, const "
        "QCborValue &value, ContainerDisposition disp)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: unknown type name 'Element'.")

  @staticmethod
  def replaceAt_internal(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::replaceAt_internal(QtCbor::Element &e,
    const QCborValue &value, ContainerDisposition disp)': leans on
    'QCborContainerPrivate::replaceAt_complex(QtCbor::Element&, QCborValue
    const&, QCborContainerPrivate::ContainerDisposition)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.replaceAt_internal' has no cute function "
        "yet. Qt's 'void "
        "QCborContainerPrivate::replaceAt_internal(QtCbor::Element &e, "
        "const QCborValue &value, ContainerDisposition disp)': leans on "
        "'QCborContainerPrivate::replaceAt_complex(QtCbor::Element&, "
        "QCborValue const&, QCborContainerPrivate::ContainerDisposition)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def resetValue(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::resetValue(QCborValue &v)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.resetValue' has no cute function yet. Qt's "
        "'void QCborContainerPrivate::resetValue(QCborValue &v)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setErrorInReader(*__, **_) -> Never:
    """
    Qt's 'void QCborContainerPrivate::setErrorInReader(QCborStreamReader
    &reader, QCborError error)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qt_cbor_stream_set_error'.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.setErrorInReader' has no cute function yet. "
        "Qt's 'void "
        "QCborContainerPrivate::setErrorInReader(QCborStreamReader &reader, "
        "QCborError error)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qt_cbor_stream_set_error'.")

  @staticmethod
  def stringCompareElement(*__, **_) -> Never:
    """
    Qt's 'QCborContainerPrivate::stringCompareElement': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.stringCompareElement' has no cute function "
        "yet. Qt's 'QCborContainerPrivate::stringCompareElement': a "
        "template: a pattern and no single function.")

  @staticmethod
  def stringEqualsElement(*__, **_) -> Never:
    """
    Qt's 'QCborContainerPrivate::stringEqualsElement': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QCborContainerPrivate.stringEqualsElement' has no cute function "
        "yet. Qt's 'QCborContainerPrivate::stringEqualsElement': a "
        "template: a pattern and no single function.")
