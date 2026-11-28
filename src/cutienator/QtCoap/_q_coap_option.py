"""
QCoapOption binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoapoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QCoapOptionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QCoapOption(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCoapOption: a plain Python object standing in front
  of one C++ QCoapOption.

  C++ hands a QCoapOption around as a copy, so every C++ QCoapOption behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCoapOption that has a ritual and that Python can
  call so far, 9 names in all: 'opaqueValue', 'uintValue', 'stringValue',
  'length', 'name', 'isValid', '__eq__', '__ne__', 'd_func'. It can be made
  from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapOption::QCoapOption(QCoapOption &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QCoapOption::~QCoapOption()': the destructor: Python removes its
    C++ QCoapOption by it, and has no other use for it.
  - Qt's 'QCoapOption &QCoapOption::operator=(const QCoapOption &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCoapOption &QCoapOption::operator=(QCoapOption &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCoapOption::swap(QCoapOption &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'const QCoapOptionPrivate *QCoapOption::d_func() const': takes in
    Python what 'QCoapOptionPrivate *QCoapOption::d_func()' takes.

  What to expect
  --------------

  - The C++ QCoapOption is created at the first use, not by
    'QCoapOption(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCoapOption back gives a copy the ritual made for
    Python, in a new cute QCoapOption.
  - Each name of Qt's QCoapOption that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QCoapOption, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class OptionName(CuteNum):
    """
    The enum 'QCoapOption::OptionName' of Qt, with the 20 names Qt gives in
    it.
    """

    Invalid = Kee[int](0)
    IfMatch = Kee[int](1)
    UriHost = Kee[int](3)
    Etag = Kee[int](4)
    IfNoneMatch = Kee[int](5)
    Observe = Kee[int](6)
    UriPort = Kee[int](7)
    LocationPath = Kee[int](8)
    UriPath = Kee[int](11)
    ContentFormat = Kee[int](12)
    MaxAge = Kee[int](14)
    UriQuery = Kee[int](15)
    Accept = Kee[int](17)
    LocationQuery = Kee[int](20)
    Block2 = Kee[int](23)
    Block1 = Kee[int](27)
    Size2 = Kee[int](28)
    ProxyUri = Kee[int](35)
    ProxyScheme = Kee[int](39)
    Size1 = Kee[int](60)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapOption'

  #  Qt's '~QCoapOption()'. Naming it makes this a value class: Python owns
  #  every C++ QCoapOption behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QCoapOptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def opaqueValue(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCoapOption::opaqueValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#opaqueValue

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCoapOption::opaqueValue() const
    address = self.uglySide.call('ritual_ZNK11QCoapOption11opaqueValueEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def uintValue(self) -> int:
    """
    Calls Qt's 'quint32 QCoapOption::uintValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#uintValue
    """
    #  quint32 QCoapOption::uintValue() const
    return self.uglySide.call('ritual_ZNK11QCoapOption9uintValueEv')

  def stringValue(self) -> str:
    """
    Calls Qt's 'QString QCoapOption::stringValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#stringValue

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCoapOption::stringValue() const
    return self.uglySide.call('ritual_ZNK11QCoapOption11stringValueEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QCoapOption::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#length
    """
    #  int QCoapOption::length() const
    return self.uglySide.call('ritual_ZNK11QCoapOption6lengthEv')

  def name(self) -> OptionName:
    """
    Calls Qt's 'OptionName QCoapOption::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#name

    Returns
    -------

    OptionName
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OptionName(number)'
      gives.
    """
    #  OptionName QCoapOption::name() const
    return QCoapOption.OptionName(self.uglySide.call(
        'ritual_ZNK11QCoapOption4nameEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCoapOption::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#isValid
    """
    #  bool QCoapOption::isValid() const
    return self.uglySide.call('ritual_ZNK11QCoapOption7isValidEv')

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
  def __eq__(self, other: QCoapOption) -> bool:
    """
    Calls Qt's 'bool QCoapOption::operator==(const QCoapOption &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#operator==

    Parameters
    ----------

    other : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  bool QCoapOption::operator==(const QCoapOption &other) const
    return self.uglySide.call(
        'ritual_ZNK11QCoapOptioneqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QCoapOption) -> bool:
    """
    Calls Qt's 'bool QCoapOption::operator!=(const QCoapOption &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#operator!=

    Parameters
    ----------

    other : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  bool QCoapOption::operator!=(const QCoapOption &other) const
    return self.uglySide.call(
        'ritual_ZNK11QCoapOptionneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
  @overload(OptionName)
  @overload(OptionName, QByteArray)
  def __init__(
      self,
      name: OptionName = OptionName.Invalid,
      opaqueValue: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCoapOption::QCoapOption(OptionName name,
    const QByteArray &opaqueValue)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#QCoapOption

    Parameters
    ----------

    name : OptionName
      Passed on as its number. May be left out, as in Qt: it is then
      OptionName.Invalid.

    opaqueValue : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QCoapOption::QCoapOption(OptionName name, const QByteArray
    #      &opaqueValue)
    if opaqueValue is None:
      from ..QtCore import QByteArray
      opaqueValue = QByteArray()
    self._noteCreation(QCoapOption, lambda: Rituals.call(
        'ritual_ZN11QCoapOptionC1ENS_10OptionNameERK10QByteArray',
        name.value, self._valueOf(opaqueValue),
    ))

  @overload(OptionName, str)
  def __init__(self, name: OptionName, stringValue: str) -> None:
    """
    Notes what was given, for Qt's 'QCoapOption::QCoapOption(OptionName name,
    const QString &stringValue)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#QCoapOption

    Parameters
    ----------

    name : OptionName
      Passed on as its number.

    stringValue : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QCoapOption::QCoapOption(OptionName name, const QString &stringValue)
    self._noteCreation(QCoapOption, lambda: Rituals.call(
        'ritual_ZN11QCoapOptionC1ENS_10OptionNameERK7QString',
        name.value, stringValue,
    ))

  @overload(OptionName, int)
  def __init__(self, name: OptionName, intValue: int) -> None:
    """
    Notes what was given, for Qt's 'QCoapOption::QCoapOption(OptionName name,
    quint32 intValue)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#QCoapOption

    Parameters
    ----------

    name : OptionName
      Passed on as its number.

    intValue : int
      Passed on as it is.
    """
    #  QCoapOption::QCoapOption(OptionName name, quint32 intValue)
    self._noteCreation(QCoapOption, lambda: Rituals.call(
        'ritual_ZN11QCoapOptionC1ENS_10OptionNameEj', name.value, intValue,
    ))

  @overload(THIS)
  def __init__(self, other: QCoapOption) -> None:
    """
    Notes what was given, for Qt's 'QCoapOption::QCoapOption(const
    QCoapOption &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#QCoapOption

    Parameters
    ----------

    other : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  QCoapOption::QCoapOption(const QCoapOption &other)
    self._noteCreation(QCoapOption, lambda: Rituals.call(
        'ritual_ZN11QCoapOptionC1ERKS_', self._valueOf(other),
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

  def d_func(self) -> Optional[QCoapOptionPrivate]:
    """
    Calls Qt's 'QCoapOptionPrivate *QCoapOption::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapoption.html#d_func

    Returns
    -------

    Optional[QCoapOptionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapOptionPrivate *QCoapOption::d_func()
    address = self.uglySide.call('ritual_ZN11QCoapOption6d_funcEv')
    from . import QCoapOptionPrivate
    return QCoapOptionPrivate._cuteAt(address)

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCoapOption::swap(QCoapOption &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCoapOption.swap' has no cute function yet. Qt's 'void "
        "QCoapOption::swap(QCoapOption &other)': takes a type Python has no "
        "way to hand over yet.")


#  Qt's 'QList<QCoapOption>': the list of QCoapOption, which
#  'QList[QCoapOption]' gives. It is made here, so that there is one as soon
#  as there can be a QCoapOption.
QList.createKind(
    QCoapOption, 'value',
    make='ritual_list_make_QCoapOption',
    add='ritual_list_add_QCoapOption',
    size='ritual_list_size_QCoapOption',
    at='ritual_list_at_QCoapOption',
    drop='ritual_list_drop_QCoapOption',
)
