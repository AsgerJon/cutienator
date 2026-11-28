"""
QWebViewLoadingInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebView/qwebviewloadinginfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QUrl = WAIT['QUrl']


class QWebViewLoadingInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebViewLoadingInfo: a plain Python object standing
  in front of one C++ QWebViewLoadingInfo.

  C++ hands a QWebViewLoadingInfo around as a copy, so every C++
  QWebViewLoadingInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebViewLoadingInfo that has a ritual and that
  Python can call so far, 4 names in all: 'url', 'status', 'errorString',
  '__rlshift__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebViewLoadingInfo &QWebViewLoadingInfo::operator=(const
    QWebViewLoadingInfo &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QWebViewLoadingInfo::QWebViewLoadingInfo(QWebViewLoadingInfo
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebViewLoadingInfo
    &QWebViewLoadingInfo::operator=(QWebViewLoadingInfo &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebViewLoadingInfo::~QWebViewLoadingInfo()': the destructor:
    Python removes its C++ QWebViewLoadingInfo by it, and has no other use
    for it.
  - Qt's 'void QWebViewLoadingInfo::swap(QWebViewLoadingInfo &other)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 18 functions Qt declares: 3 not a gap; 3 forbidden.

  What to expect
  --------------

  - The C++ QWebViewLoadingInfo is created at the first use, not by
    'QWebViewLoadingInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebViewLoadingInfo back gives a copy the ritual made
    for Python, in a new cute QWebViewLoadingInfo.
  - Each name of Qt's QWebViewLoadingInfo that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QWebViewLoadingInfo, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class LoadStatus(CuteNum, scoped=True):
    """
    The enum 'QWebViewLoadingInfo::LoadStatus' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Started = Kee[int](0)
    Stopped = Kee[int](1)
    Succeeded = Kee[int](2)
    Failed = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebViewLoadingInfo'

  #  Qt's '~QWebViewLoadingInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QWebViewLoadingInfo behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QWebViewLoadingInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebViewLoadingInfo::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewloadinginfo.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebViewLoadingInfo::url() const
    address = self.uglySide.call('ritual_ZNK19QWebViewLoadingInfo3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> LoadStatus:
    """
    Calls Qt's 'LoadStatus QWebViewLoadingInfo::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebviewloadinginfo.html#status

    Returns
    -------

    LoadStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LoadStatus(number)'
      gives.
    """
    #  LoadStatus QWebViewLoadingInfo::status() const
    return QWebViewLoadingInfo.LoadStatus(self.uglySide.call(
        'ritual_ZNK19QWebViewLoadingInfo6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QWebViewLoadingInfo::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewloadinginfo.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebViewLoadingInfo::errorString() const
    return self.uglySide.call(
        'ritual_ZNK19QWebViewLoadingInfo11errorStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, ds: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug ds, const QWebViewLoadingInfo
    &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewloadinginfo.html#operator<<

    Parameters
    ----------

    ds : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug ds, const QWebViewLoadingInfo &info)
    address = Rituals.call(
        'ritual_Zls6QDebugRK19QWebViewLoadingInfo',
        CuteMixin._valueOf(ds), CuteMixin._valueOf(self),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWebViewLoadingInfo::QWebViewLoadingInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewloadinginfo.html#QWebViewLoadingInfo
    """
    #  QWebViewLoadingInfo::QWebViewLoadingInfo()
    self._noteCreation(QWebViewLoadingInfo, lambda: Rituals.call(
        'ritual_ZN19QWebViewLoadingInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebViewLoadingInfo) -> None:
    """
    Notes what was given, for Qt's
    'QWebViewLoadingInfo::QWebViewLoadingInfo(const QWebViewLoadingInfo
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewloadinginfo.html#QWebViewLoadingInfo

    Parameters
    ----------

    other : QWebViewLoadingInfo
      Passed on as a value: Qt reads the C++ QWebViewLoadingInfo, which stays
      Python's own.
    """
    #  QWebViewLoadingInfo::QWebViewLoadingInfo(const QWebViewLoadingInfo
    #      &other)
    self._noteCreation(QWebViewLoadingInfo, lambda: Rituals.call(
        'ritual_ZN19QWebViewLoadingInfoC1ERKS_', self._valueOf(other),
    ))

  @overload(QUrl, LoadStatus, str)
  def __init__(
      self,
      url: QUrl,
      status: LoadStatus,
      errorString: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWebViewLoadingInfo::QWebViewLoadingInfo(const QUrl &url, LoadStatus
    status, const QString &errorString)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebviewloadinginfo.html#QWebViewLoadingInfo

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    status : LoadStatus
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QWebViewLoadingInfo::QWebViewLoadingInfo(const QUrl &url, LoadStatus
    #      status, const QString &errorString)
    self._noteCreation(QWebViewLoadingInfo, lambda: Rituals.call(
        'ritual_ZN19QWebViewLoadingInfoC1ERK4QUrlNS_10LoadStatusERK7QString',
        self._valueOf(url), status.value, errorString,
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
    Qt's 'void QWebViewLoadingInfo::swap(QWebViewLoadingInfo &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebViewLoadingInfo.swap' has no cute function yet. Qt's 'void "
        "QWebViewLoadingInfo::swap(QWebViewLoadingInfo &other)': takes a "
        "type Python has no way to hand over yet.")
