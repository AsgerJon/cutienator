"""
QOpcUaExtensionObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaextensionobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QOpcUaExtensionObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaExtensionObject: a plain Python object standing
  in front of one C++ QOpcUaExtensionObject.

  C++ hands a QOpcUaExtensionObject around as a copy, so every C++
  QOpcUaExtensionObject behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaExtensionObject that has a ritual and that
  Python can call so far, 9 names in all: '__eq__', 'encodingTypeId',
  'setEncodingTypeId', 'encodedBody', 'setEncodedBody',
  'setBinaryEncodedBody', 'setXmlEncodedBody', 'encoding', 'setEncoding'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaExtensionObject::~QOpcUaExtensionObject()': the destructor:
    Python removes its C++ QOpcUaExtensionObject by it, and has no other use
    for it.
  - Qt's 'QOpcUaExtensionObject &QOpcUaExtensionObject::operator=(const
    QOpcUaExtensionObject &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaExtensionObject::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QByteArray &QOpcUaExtensionObject::encodedBodyRef()': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaExtensionObject is created at the first use, not by
    'QOpcUaExtensionObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaExtensionObject back gives a copy the ritual
    made for Python, in a new cute QOpcUaExtensionObject.
  - Each name of Qt's QOpcUaExtensionObject that has no cute function yet,
    'encodedBodyRef', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaExtensionObject, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Encoding(CuteNum):
    """
    The enum 'QOpcUaExtensionObject::Encoding' of Qt, with the 3 names Qt
    gives in it.
    """

    NoBody = Kee[int](0)
    ByteString = Kee[int](1)
    Xml = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaExtensionObject'

  #  Qt's '~QOpcUaExtensionObject()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaExtensionObject behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QOpcUaExtensionObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def encodingTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaExtensionObject::encodingTypeId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#encodingTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaExtensionObject::encodingTypeId() const
    return self.uglySide.call(
        'ritual_ZNK21QOpcUaExtensionObject14encodingTypeIdEv',
    )

  def encodedBody(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOpcUaExtensionObject::encodedBody() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#encodedBody

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOpcUaExtensionObject::encodedBody() const
    address = self.uglySide.call(
        'ritual_ZNK21QOpcUaExtensionObject11encodedBodyEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def encoding(self) -> Encoding:
    """
    Calls Qt's 'QOpcUaExtensionObject::Encoding
    QOpcUaExtensionObject::encoding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#encoding

    Returns
    -------

    Encoding
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Encoding(number)' gives.
    """
    #  QOpcUaExtensionObject::Encoding QOpcUaExtensionObject::encoding()
    #      const
    return QOpcUaExtensionObject.Encoding(self.uglySide.call(
        'ritual_ZNK21QOpcUaExtensionObject8encodingEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setEncodingTypeId(self, encodingTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaExtensionObject::setEncodingTypeId(const QString
    &encodingTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#setEncodingTypeId

    Parameters
    ----------

    encodingTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaExtensionObject::setEncodingTypeId(const QString
    #      &encodingTypeId)
    self.uglySide.call(
        'ritual_ZN21QOpcUaExtensionObject17setEncodingTypeIdERK7QString',
        encodingTypeId,
    )

  @overload(QByteArray)
  def setEncodedBody(self, encodedBody: QByteArray) -> None:
    """
    Calls Qt's 'void QOpcUaExtensionObject::setEncodedBody(const QByteArray
    &encodedBody)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#setEncodedBody

    Parameters
    ----------

    encodedBody : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QOpcUaExtensionObject::setEncodedBody(const QByteArray
    #      &encodedBody)
    self.uglySide.call(
        'ritual_ZN21QOpcUaExtensionObject14setEncodedBodyERK10QByteArray',
        self._valueOf(encodedBody),
    )

  @overload(QByteArray, str)
  def setBinaryEncodedBody(
      self,
      encodedBody: QByteArray,
      typeId: str,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaExtensionObject::setBinaryEncodedBody(const
    QByteArray &encodedBody, const QString &typeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#setBinaryEncodedBody

    Parameters
    ----------

    encodedBody : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    typeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaExtensionObject::setBinaryEncodedBody(const QByteArray
    #      &encodedBody, const QString &typeId)
    self.uglySide.call(
        'ritual_ZN21QOpcUaExtensionObject20setBinaryEncodedBodyERK10QByteAr'
        'rayRK7QString',
        self._valueOf(encodedBody), typeId,
    )

  @overload(QByteArray, str)
  def setXmlEncodedBody(self, encodedBody: QByteArray, typeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaExtensionObject::setXmlEncodedBody(const
    QByteArray &encodedBody, const QString &typeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#setXmlEncodedBody

    Parameters
    ----------

    encodedBody : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    typeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaExtensionObject::setXmlEncodedBody(const QByteArray
    #      &encodedBody, const QString &typeId)
    self.uglySide.call(
        'ritual_ZN21QOpcUaExtensionObject17setXmlEncodedBodyERK10QByteArray'
        'RK7QString',
        self._valueOf(encodedBody), typeId,
    )

  @overload(Encoding)
  def setEncoding(self, encoding: Encoding) -> None:
    """
    Calls Qt's 'void
    QOpcUaExtensionObject::setEncoding(QOpcUaExtensionObject::Encoding
    encoding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#setEncoding

    Parameters
    ----------

    encoding : Encoding
      Passed on as its number.
    """
    #  void
    #      QOpcUaExtensionObject::setEncoding(QOpcUaExtensionObject::Encoding
    #      encoding)
    self.uglySide.call(
        'ritual_ZN21QOpcUaExtensionObject11setEncodingENS_8EncodingE',
        encoding.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaExtensionObject) -> bool:
    """
    Calls Qt's 'bool QOpcUaExtensionObject::operator==(const
    QOpcUaExtensionObject &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#operator==

    Parameters
    ----------

    rhs : QOpcUaExtensionObject
      Passed on as a value: Qt reads the C++ QOpcUaExtensionObject, which
      stays Python's own.
    """
    #  bool QOpcUaExtensionObject::operator==(const QOpcUaExtensionObject
    #      &rhs) const
    return self.uglySide.call(
        'ritual_ZNK21QOpcUaExtensionObjecteqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaExtensionObject::QOpcUaExtensionObject()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#QOpcUaExtensionObject
    """
    #  QOpcUaExtensionObject::QOpcUaExtensionObject()
    self._noteCreation(QOpcUaExtensionObject, lambda: Rituals.call(
        'ritual_ZN21QOpcUaExtensionObjectC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaExtensionObject) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaExtensionObject::QOpcUaExtensionObject(const QOpcUaExtensionObject
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#QOpcUaExtensionObject

    Parameters
    ----------

    a0 : QOpcUaExtensionObject
      Passed on as a value: Qt reads the C++ QOpcUaExtensionObject, which
      stays Python's own.
    """
    #  QOpcUaExtensionObject::QOpcUaExtensionObject(const
    #      QOpcUaExtensionObject &a0)
    self._noteCreation(QOpcUaExtensionObject, lambda: Rituals.call(
        'ritual_ZN21QOpcUaExtensionObjectC1ERKS_', self._valueOf(a0),
    ))

  @overload(str)
  @overload(str, Encoding)
  def __init__(
      self,
      typeId: str,
      encoding: Encoding = Encoding.ByteString,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaExtensionObject::QOpcUaExtensionObject(const QString &typeId,
    Encoding encoding)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaextensionobject.html#QOpcUaExtensionObject

    Parameters
    ----------

    typeId : str
      Passed on as it is: a QString is made of it for the call.

    encoding : Encoding
      Passed on as its number. May be left out, as in Qt: it is then
      Encoding.ByteString.
    """
    #  QOpcUaExtensionObject::QOpcUaExtensionObject(const QString &typeId,
    #      Encoding encoding)
    self._noteCreation(QOpcUaExtensionObject, lambda: Rituals.call(
        'ritual_ZN21QOpcUaExtensionObjectC1ERK7QStringNS_8EncodingE',
        typeId, encoding.value,
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
  def encodedBodyRef(*__, **_) -> Never:
    """
    Qt's 'QByteArray &QOpcUaExtensionObject::encodedBodyRef()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaExtensionObject.encodedBodyRef' has no cute function yet. "
        "Qt's 'QByteArray &QOpcUaExtensionObject::encodedBodyRef()': gives "
        "a type Python has no way to take yet.")
