"""
QHstsPolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhstspolicy.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QUrl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDateTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']


class QHstsPolicy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHstsPolicy: a plain Python object standing in front
  of one C++ QHstsPolicy.

  C++ hands a QHstsPolicy around as a copy, so every C++ QHstsPolicy behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHstsPolicy that has a ritual and that Python can
  call so far, 10 names in all: 'setHost', 'host', 'setExpiry', 'expiry',
  'setIncludesSubDomains', 'includesSubDomains', 'isExpired', 'isEqual',
  '__eq__', '__ne__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHstsPolicy &QHstsPolicy::operator=(const QHstsPolicy &rhs)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHstsPolicy &QHstsPolicy::operator=(QHstsPolicy &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHstsPolicy::~QHstsPolicy()': the destructor: Python removes its
    C++ QHstsPolicy by it, and has no other use for it.
  - Qt's 'void QHstsPolicy::swap(QHstsPolicy &other)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QHstsPolicy is created at the first use, not by
    'QHstsPolicy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHstsPolicy back gives a copy the ritual made for
    Python, in a new cute QHstsPolicy.
  - Each name of Qt's QHstsPolicy that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QHstsPolicy, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PolicyFlag(CuteFlags):
    """
    The flags enum 'QHstsPolicy::PolicyFlag' of Qt, with the 1 names Qt gives
    in it. Qt names the type of its combinations 'QHstsPolicy::PolicyFlags'.
    """

    IncludeSubDomains = 0x1

  PolicyFlags = PolicyFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHstsPolicy'

  #  Qt's '~QHstsPolicy()'. Naming it makes this a value class: Python owns
  #  every C++ QHstsPolicy behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QHstsPolicyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QUrl.ComponentFormattingOptions)
  def host(
      self,
      options: QUrl.ComponentFormattingOptions = (
          QUrl.ComponentFormattingOptions.FullyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QHstsPolicy::host(QUrl::ComponentFormattingOptions
    options) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#host

    Parameters
    ----------

    options : QUrl.ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QUrl.ComponentFormattingOptions.FullyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHstsPolicy::host(QUrl::ComponentFormattingOptions options)
    #      const
    return self.uglySide.call(
        'ritual_ZNK11QHstsPolicy4hostE6QFlagsIN4QUrl25ComponentFormattingOp'
        'tionEE',
        options.value,
    )

  def expiry(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QHstsPolicy::expiry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#expiry

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QHstsPolicy::expiry() const
    address = self.uglySide.call('ritual_ZNK11QHstsPolicy6expiryEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def includesSubDomains(self) -> bool:
    """
    Calls Qt's 'bool QHstsPolicy::includesSubDomains() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhstspolicy.html#includesSubDomains
    """
    #  bool QHstsPolicy::includesSubDomains() const
    return self.uglySide.call(
        'ritual_ZNK11QHstsPolicy18includesSubDomainsEv',
    )

  def isExpired(self) -> bool:
    """
    Calls Qt's 'bool QHstsPolicy::isExpired() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#isExpired
    """
    #  bool QHstsPolicy::isExpired() const
    return self.uglySide.call('ritual_ZNK11QHstsPolicy9isExpiredEv')

  @overload(THIS)
  def isEqual(self, other: QHstsPolicy) -> bool:
    """
    Calls Qt's 'bool QHstsPolicy::isEqual(const QHstsPolicy &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#isEqual

    Parameters
    ----------

    other : QHstsPolicy
      Passed on as a value: Qt reads the C++ QHstsPolicy, which stays
      Python's own.
    """
    #  bool QHstsPolicy::isEqual(const QHstsPolicy &other) const
    return self.uglySide.call(
        'ritual_ZNK11QHstsPolicy7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, QUrl.ParsingMode)
  def setHost(
      self,
      host: str,
      mode: QUrl.ParsingMode = QUrl.ParsingMode.DecodedMode,
  ) -> None:
    """
    Calls Qt's 'void QHstsPolicy::setHost(const QString &host,
    QUrl::ParsingMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#setHost

    Parameters
    ----------

    host : str
      Passed on as it is: a QString is made of it for the call.

    mode : QUrl.ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      QUrl.ParsingMode.DecodedMode.
    """
    #  void QHstsPolicy::setHost(const QString &host, QUrl::ParsingMode mode)
    self.uglySide.call(
        'ritual_ZN11QHstsPolicy7setHostERK7QStringN4QUrl11ParsingModeE',
        host, mode.value,
    )

  @overload(QDateTime)
  def setExpiry(self, expiry: QDateTime) -> None:
    """
    Calls Qt's 'void QHstsPolicy::setExpiry(const QDateTime &expiry)'.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#setExpiry

    Parameters
    ----------

    expiry : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QHstsPolicy::setExpiry(const QDateTime &expiry)
    self.uglySide.call(
        'ritual_ZN11QHstsPolicy9setExpiryERK9QDateTime',
        self._valueOf(expiry),
    )

  @overload(bool)
  def setIncludesSubDomains(self, include: bool) -> None:
    """
    Calls Qt's 'void QHstsPolicy::setIncludesSubDomains(bool include)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhstspolicy.html#setIncludesSubDomains

    Parameters
    ----------

    include : bool
      Passed on as it is.
    """
    #  void QHstsPolicy::setIncludesSubDomains(bool include)
    self.uglySide.call(
        'ritual_ZN11QHstsPolicy21setIncludesSubDomainsEb', include,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QHstsPolicy) -> bool:
    """
    Calls Qt's 'bool operator==(const QHstsPolicy &lhs, const QHstsPolicy
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#operator==

    Parameters
    ----------

    rhs : QHstsPolicy
      Passed on as a value: Qt reads the C++ QHstsPolicy, which stays
      Python's own.
    """
    #  bool operator==(const QHstsPolicy &lhs, const QHstsPolicy &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QHstsPolicyS1_',
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
  def __ne__(self, rhs: QHstsPolicy) -> bool:
    """
    Calls Qt's 'bool operator!=(const QHstsPolicy &lhs, const QHstsPolicy
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#operator!=

    Parameters
    ----------

    rhs : QHstsPolicy
      Passed on as a value: Qt reads the C++ QHstsPolicy, which stays
      Python's own.
    """
    #  bool operator!=(const QHstsPolicy &lhs, const QHstsPolicy &rhs)
    return Rituals.call(
        'ritual_ZneRK11QHstsPolicyS1_',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QHstsPolicy::QHstsPolicy()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#QHstsPolicy
    """
    #  QHstsPolicy::QHstsPolicy()
    self._noteCreation(QHstsPolicy, lambda: Rituals.call(
        'ritual_ZN11QHstsPolicyC1Ev',
    ))

  @overload(QDateTime, PolicyFlags, str)
  @overload(QDateTime, PolicyFlags, str, QUrl.ParsingMode)
  def __init__(
      self,
      expiry: QDateTime,
      flags: PolicyFlags,
      host: str,
      mode: QUrl.ParsingMode = QUrl.ParsingMode.DecodedMode,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHstsPolicy::QHstsPolicy(const QDateTime
    &expiry, PolicyFlags flags, const QString &host, QUrl::ParsingMode
    mode)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#QHstsPolicy

    Parameters
    ----------

    expiry : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    flags : PolicyFlags
      Passed on as its number.

    host : str
      Passed on as it is: a QString is made of it for the call.

    mode : QUrl.ParsingMode
      Passed on as its number. May be left out, as in Qt: it is then
      QUrl.ParsingMode.DecodedMode.
    """
    #  QHstsPolicy::QHstsPolicy(const QDateTime &expiry, PolicyFlags flags,
    #      const QString &host, QUrl::ParsingMode mode)
    self._noteCreation(QHstsPolicy, lambda: Rituals.call(
        'ritual_ZN11QHstsPolicyC1ERK9QDateTime6QFlagsINS_10PolicyFlagEERK7Q'
        'StringN4QUrl11ParsingModeE',
        self._valueOf(expiry), flags.value, host, mode.value,
    ))

  @overload(THIS)
  def __init__(self, rhs: QHstsPolicy) -> None:
    """
    Notes what was given, for Qt's 'QHstsPolicy::QHstsPolicy(const
    QHstsPolicy &rhs)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhstspolicy.html#QHstsPolicy

    Parameters
    ----------

    rhs : QHstsPolicy
      Passed on as a value: Qt reads the C++ QHstsPolicy, which stays
      Python's own.
    """
    #  QHstsPolicy::QHstsPolicy(const QHstsPolicy &rhs)
    self._noteCreation(QHstsPolicy, lambda: Rituals.call(
        'ritual_ZN11QHstsPolicyC1ERKS_', self._valueOf(rhs),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHstsPolicy::swap(QHstsPolicy &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHstsPolicy.swap' has no cute function yet. Qt's 'void "
        "QHstsPolicy::swap(QHstsPolicy &other)': takes a type Python has no "
        "way to hand over yet.")


#  Qt's 'QList<QHstsPolicy>': the list of QHstsPolicy, which
#  'QList[QHstsPolicy]' gives. It is made here, so that there is one as soon
#  as there can be a QHstsPolicy.
QList.createKind(
    QHstsPolicy, 'value',
    make='ritual_list_make_QHstsPolicy',
    add='ritual_list_add_QHstsPolicy',
    size='ritual_list_size_QHstsPolicy',
    at='ritual_list_at_QHstsPolicy',
    drop='ritual_list_drop_QHstsPolicy',
)
