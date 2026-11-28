"""
QNetworkCookie binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qnetworkcookie.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QByteArray, QByteArrayView, QDateTime, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QDateTime = WAIT['QDateTime']
  QUrl = WAIT['QUrl']


class QNetworkCookie(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkCookie: a plain Python object standing in
  front of one C++ QNetworkCookie.

  C++ hands a QNetworkCookie around as a copy, so every C++ QNetworkCookie
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkCookie that has a ritual and that Python can
  call so far, 23 names in all: '__eq__', '__ne__', 'isSecure', 'setSecure',
  'isHttpOnly', 'setHttpOnly', 'sameSitePolicy', 'setSameSitePolicy',
  'isSessionCookie', 'expirationDate', 'setExpirationDate', 'domain',
  'setDomain', 'path', 'setPath', 'name', 'setName', 'value', 'setValue',
  'toRawForm', 'hasSameIdentifier', 'normalize', 'parseCookies'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkCookie::~QNetworkCookie()': the destructor: Python removes
    its C++ QNetworkCookie by it, and has no other use for it.
  - Qt's 'QNetworkCookie &QNetworkCookie::operator=(QNetworkCookie &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QNetworkCookie &QNetworkCookie::operator=(const QNetworkCookie
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QNetworkCookie::swap(QNetworkCookie &other)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 32 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QNetworkCookie is created at the first use, not by
    'QNetworkCookie(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkCookie back gives a copy the ritual made for
    Python, in a new cute QNetworkCookie.
  - Each name of Qt's QNetworkCookie that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QNetworkCookie, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RawForm(CuteNum):
    """
    The enum 'QNetworkCookie::RawForm' of Qt, with the 2 names Qt gives in
    it.
    """

    NameAndValueOnly = Kee[int](0)
    Full = Kee[int](1)

  class SameSite(CuteNum, scoped=True):
    """
    The enum 'QNetworkCookie::SameSite' of Qt, with the 4 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Default = Kee[int](0)
    NULL = Kee[int](1)
    Lax = Kee[int](2)
    Strict = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArrayView)
  def parseCookies(cookieString: QByteArrayView) -> QList[QNetworkCookie]:
    """
    Calls Qt's 'QList<QNetworkCookie>
    QNetworkCookie::parseCookies(QByteArrayView cookieString)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#parseCookies

    Parameters
    ----------

    cookieString : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QList[QNetworkCookie]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNetworkCookie> QNetworkCookie::parseCookies(QByteArrayView
    #      cookieString)
    address = Rituals.call(
        'ritual_ZN14QNetworkCookie12parseCookiesE14QByteArrayView',
        CuteMixin._valueOf(cookieString),
    )
    return QList[QNetworkCookie]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkCookie'

  #  Qt's '~QNetworkCookie()'. Naming it makes this a value class: Python
  #  owns every C++ QNetworkCookie behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QNetworkCookieD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSecure(self) -> bool:
    """
    Calls Qt's 'bool QNetworkCookie::isSecure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#isSecure
    """
    #  bool QNetworkCookie::isSecure() const
    return self.uglySide.call('ritual_ZNK14QNetworkCookie8isSecureEv')

  def isHttpOnly(self) -> bool:
    """
    Calls Qt's 'bool QNetworkCookie::isHttpOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#isHttpOnly
    """
    #  bool QNetworkCookie::isHttpOnly() const
    return self.uglySide.call('ritual_ZNK14QNetworkCookie10isHttpOnlyEv')

  def sameSitePolicy(self) -> SameSite:
    """
    Calls Qt's 'SameSite QNetworkCookie::sameSitePolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#sameSitePolicy

    Returns
    -------

    SameSite
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SameSite(number)' gives.
    """
    #  SameSite QNetworkCookie::sameSitePolicy() const
    return QNetworkCookie.SameSite(self.uglySide.call(
        'ritual_ZNK14QNetworkCookie14sameSitePolicyEv',
    ))

  def isSessionCookie(self) -> bool:
    """
    Calls Qt's 'bool QNetworkCookie::isSessionCookie() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookie.html#isSessionCookie
    """
    #  bool QNetworkCookie::isSessionCookie() const
    return self.uglySide.call(
        'ritual_ZNK14QNetworkCookie15isSessionCookieEv',
    )

  def expirationDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QNetworkCookie::expirationDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#expirationDate

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QNetworkCookie::expirationDate() const
    address = self.uglySide.call(
        'ritual_ZNK14QNetworkCookie14expirationDateEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def domain(self) -> str:
    """
    Calls Qt's 'QString QNetworkCookie::domain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#domain

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkCookie::domain() const
    return self.uglySide.call('ritual_ZNK14QNetworkCookie6domainEv')

  def path(self) -> str:
    """
    Calls Qt's 'QString QNetworkCookie::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNetworkCookie::path() const
    return self.uglySide.call('ritual_ZNK14QNetworkCookie4pathEv')

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkCookie::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkCookie::name() const
    address = self.uglySide.call('ritual_ZNK14QNetworkCookie4nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkCookie::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkCookie::value() const
    address = self.uglySide.call('ritual_ZNK14QNetworkCookie5valueEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload()
  @overload(RawForm)
  def toRawForm(self, form: RawForm = RawForm.Full) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkCookie::toRawForm(RawForm form) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#toRawForm

    Parameters
    ----------

    form : RawForm
      Passed on as its number. May be left out, as in Qt: it is then
      RawForm.Full.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkCookie::toRawForm(RawForm form) const
    address = self.uglySide.call(
        'ritual_ZNK14QNetworkCookie9toRawFormENS_7RawFormE', form.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(THIS)
  def hasSameIdentifier(self, other: QNetworkCookie) -> bool:
    """
    Calls Qt's 'bool QNetworkCookie::hasSameIdentifier(const QNetworkCookie
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookie.html#hasSameIdentifier

    Parameters
    ----------

    other : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  bool QNetworkCookie::hasSameIdentifier(const QNetworkCookie &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK14QNetworkCookie17hasSameIdentifierERKS_',
        self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSecure(self, enable: bool) -> None:
    """
    Calls Qt's 'void QNetworkCookie::setSecure(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#setSecure

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QNetworkCookie::setSecure(bool enable)
    self.uglySide.call('ritual_ZN14QNetworkCookie9setSecureEb', enable)

  @overload(bool)
  def setHttpOnly(self, enable: bool) -> None:
    """
    Calls Qt's 'void QNetworkCookie::setHttpOnly(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#setHttpOnly

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QNetworkCookie::setHttpOnly(bool enable)
    self.uglySide.call('ritual_ZN14QNetworkCookie11setHttpOnlyEb', enable)

  @overload(SameSite)
  def setSameSitePolicy(self, sameSite: SameSite) -> None:
    """
    Calls Qt's 'void QNetworkCookie::setSameSitePolicy(SameSite sameSite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookie.html#setSameSitePolicy

    Parameters
    ----------

    sameSite : SameSite
      Passed on as its number.
    """
    #  void QNetworkCookie::setSameSitePolicy(SameSite sameSite)
    self.uglySide.call(
        'ritual_ZN14QNetworkCookie17setSameSitePolicyENS_8SameSiteE',
        sameSite.value,
    )

  @overload(QDateTime)
  def setExpirationDate(self, date: QDateTime) -> None:
    """
    Calls Qt's 'void QNetworkCookie::setExpirationDate(const QDateTime
    &date)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcookie.html#setExpirationDate

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QNetworkCookie::setExpirationDate(const QDateTime &date)
    self.uglySide.call(
        'ritual_ZN14QNetworkCookie17setExpirationDateERK9QDateTime',
        self._valueOf(date),
    )

  @overload(str)
  def setDomain(self, domain: str) -> None:
    """
    Calls Qt's 'void QNetworkCookie::setDomain(const QString &domain)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#setDomain

    Parameters
    ----------

    domain : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkCookie::setDomain(const QString &domain)
    self.uglySide.call(
        'ritual_ZN14QNetworkCookie9setDomainERK7QString', domain,
    )

  @overload(str)
  def setPath(self, path: str) -> None:
    """
    Calls Qt's 'void QNetworkCookie::setPath(const QString &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#setPath

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNetworkCookie::setPath(const QString &path)
    self.uglySide.call('ritual_ZN14QNetworkCookie7setPathERK7QString', path)

  @overload(QByteArray)
  def setName(self, cookieName: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkCookie::setName(const QByteArray &cookieName)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#setName

    Parameters
    ----------

    cookieName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkCookie::setName(const QByteArray &cookieName)
    self.uglySide.call(
        'ritual_ZN14QNetworkCookie7setNameERK10QByteArray',
        self._valueOf(cookieName),
    )

  @overload(QByteArray)
  def setValue(self, value: QByteArray) -> None:
    """
    Calls Qt's 'void QNetworkCookie::setValue(const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#setValue

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNetworkCookie::setValue(const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN14QNetworkCookie8setValueERK10QByteArray',
        self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QNetworkCookie) -> bool:
    """
    Calls Qt's 'bool QNetworkCookie::operator==(const QNetworkCookie &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#operator==

    Parameters
    ----------

    other : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  bool QNetworkCookie::operator==(const QNetworkCookie &other) const
    return self.uglySide.call(
        'ritual_ZNK14QNetworkCookieeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QNetworkCookie) -> bool:
    """
    Calls Qt's 'bool QNetworkCookie::operator!=(const QNetworkCookie &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#operator!=

    Parameters
    ----------

    other : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  bool QNetworkCookie::operator!=(const QNetworkCookie &other) const
    return self.uglySide.call(
        'ritual_ZNK14QNetworkCookieneERKS_', self._valueOf(other),
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
  @overload(QByteArray)
  @overload(QByteArray, QByteArray)
  def __init__(
      self,
      name: Optional[QByteArray] = None,
      value: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QNetworkCookie::QNetworkCookie(const
    QByteArray &name, const QByteArray &value)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#QNetworkCookie

    Parameters
    ----------

    name : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    value : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QNetworkCookie::QNetworkCookie(const QByteArray &name, const
    #      QByteArray &value)
    if name is None:
      from ..QtCore import QByteArray
      name = QByteArray()
    if value is None:
      from ..QtCore import QByteArray
      value = QByteArray()
    self._noteCreation(QNetworkCookie, lambda: Rituals.call(
        'ritual_ZN14QNetworkCookieC1ERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(value),
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkCookie) -> None:
    """
    Notes what was given, for Qt's 'QNetworkCookie::QNetworkCookie(const
    QNetworkCookie &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#QNetworkCookie

    Parameters
    ----------

    other : QNetworkCookie
      Passed on as a value: Qt reads the C++ QNetworkCookie, which stays
      Python's own.
    """
    #  QNetworkCookie::QNetworkCookie(const QNetworkCookie &other)
    self._noteCreation(QNetworkCookie, lambda: Rituals.call(
        'ritual_ZN14QNetworkCookieC1ERKS_', self._valueOf(other),
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

  @overload(QUrl)
  def normalize(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkCookie::normalize(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcookie.html#normalize

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkCookie::normalize(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN14QNetworkCookie9normalizeERK4QUrl', self._valueOf(url),
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QNetworkCookie::swap(QNetworkCookie &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkCookie.swap' has no cute function yet. Qt's 'void "
        "QNetworkCookie::swap(QNetworkCookie &other)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QList<QNetworkCookie>': the list of QNetworkCookie, which
#  'QList[QNetworkCookie]' gives. It is made here, so that there is one as
#  soon as there can be a QNetworkCookie.
QList.createKind(
    QNetworkCookie, 'value',
    make='ritual_list_make_QNetworkCookie',
    add='ritual_list_add_QNetworkCookie',
    size='ritual_list_size_QNetworkCookie',
    at='ritual_list_at_QNetworkCookie',
    drop='ritual_list_drop_QNetworkCookie',
)
