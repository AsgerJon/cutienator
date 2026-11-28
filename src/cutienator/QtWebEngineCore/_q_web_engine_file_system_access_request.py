"""
QWebEngineFileSystemAccessRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginefilesystemaccessrequest.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl


class QWebEngineFileSystemAccessRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineFileSystemAccessRequest: a plain Python
  object standing in front of one C++ QWebEngineFileSystemAccessRequest.

  C++ hands a QWebEngineFileSystemAccessRequest around as a copy, so every
  C++ QWebEngineFileSystemAccessRequest behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineFileSystemAccessRequest that has a ritual
  and that Python can call so far, 8 names in all: 'accept', 'reject',
  'origin', 'filePath', 'handleType', 'accessFlags', '__eq__', '__ne__'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineFileSystemAccessRequest
    &QWebEngineFileSystemAccessRequest::operator=(const
    QWebEngineFileSystemAccessRequest &other)': assignment: Python binds a
    name and has no operator for it.
  - Qt's
    'QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest(
    QWebEngineFileSystemAccessRequest &&other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QWebEngineFileSystemAccessRequest
    &QWebEngineFileSystemAccessRequest::operator=(
    QWebEngineFileSystemAccessRequest &&other)': assignment: Python binds a
    name and has no operator for it.
  - Qt's
    'QWebEngineFileSystemAccessRequest::~QWebEngineFileSystemAccessRequest(
    )': the destructor: Python removes its C++
    QWebEngineFileSystemAccessRequest by it, and has no other use for it.
  - Qt's 'void
    QWebEngineFileSystemAccessRequest::swap(QWebEngineFileSystemAccessRequest
    &other)': takes a type Python has no way to hand over yet.
  - Qt's
    'QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest(
    std::shared_ptr<QtWebEngineCore::
    FileSystemAccessPermissionRequestController> a0)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineFileSystemAccessRequest is created at the first use,
    not by 'QWebEngineFileSystemAccessRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineFileSystemAccessRequest back gives a copy
    the ritual made for Python, in a new cute
    QWebEngineFileSystemAccessRequest.
  - Each name of Qt's QWebEngineFileSystemAccessRequest that has no cute
    function yet, 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QWebEngineFileSystemAccessRequest, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class AccessFlag(CuteFlags):
    """
    The flags enum 'QWebEngineFileSystemAccessRequest::AccessFlag' of Qt,
    with the 2 names Qt gives in it. Qt names the type of its combinations
    'QWebEngineFileSystemAccessRequest::AccessFlags'.
    """

    Read = 0x1
    Write = 0x2

  AccessFlags = AccessFlag

  class HandleType(CuteNum):
    """
    The enum 'QWebEngineFileSystemAccessRequest::HandleType' of Qt, with the
    2 names Qt gives in it.
    """

    File = Kee[int](0)
    Directory = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineFileSystemAccessRequest'

  #  Qt's '~QWebEngineFileSystemAccessRequest()'. Naming it makes this a
  #  value class: Python owns every C++ QWebEngineFileSystemAccessRequest
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN33QWebEngineFileSystemAccessRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def origin(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineFileSystemAccessRequest::origin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html#origin

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineFileSystemAccessRequest::origin() const
    address = self.uglySide.call(
        'ritual_ZNK33QWebEngineFileSystemAccessRequest6originEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def filePath(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineFileSystemAccessRequest::filePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html#filePath

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineFileSystemAccessRequest::filePath() const
    address = self.uglySide.call(
        'ritual_ZNK33QWebEngineFileSystemAccessRequest8filePathEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def handleType(self) -> HandleType:
    """
    Calls Qt's 'HandleType QWebEngineFileSystemAccessRequest::handleType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html#handleType

    Returns
    -------

    HandleType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HandleType(number)'
      gives.
    """
    #  HandleType QWebEngineFileSystemAccessRequest::handleType() const
    return QWebEngineFileSystemAccessRequest.HandleType(self.uglySide.call(
        'ritual_ZNK33QWebEngineFileSystemAccessRequest10handleTypeEv',
    ))

  def accessFlags(self) -> AccessFlags:
    """
    Calls Qt's 'AccessFlags QWebEngineFileSystemAccessRequest::accessFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html#accessFlags

    Returns
    -------

    AccessFlags
      The value standing for the combination Qt gave back.
    """
    #  AccessFlags QWebEngineFileSystemAccessRequest::accessFlags() const
    return QWebEngineFileSystemAccessRequest.AccessFlags(self.uglySide.call(
        'ritual_ZNK33QWebEngineFileSystemAccessRequest11accessFlagsEv',
    ))

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
  def __eq__(self, rhs: QWebEngineFileSystemAccessRequest) -> bool:
    """
    Calls Qt's 'bool operator==(const QWebEngineFileSystemAccessRequest &lhs,
    const QWebEngineFileSystemAccessRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html#operator==

    Parameters
    ----------

    rhs : QWebEngineFileSystemAccessRequest
      Passed on as a value: Qt reads the C++
      QWebEngineFileSystemAccessRequest, which stays Python's own.
    """
    #  bool operator==(const QWebEngineFileSystemAccessRequest &lhs, const
    #      QWebEngineFileSystemAccessRequest &rhs)
    return Rituals.call(
        'ritual_ZeqRK33QWebEngineFileSystemAccessRequestS1_',
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
  def __ne__(self, rhs: QWebEngineFileSystemAccessRequest) -> bool:
    """
    Calls Qt's 'bool operator!=(const QWebEngineFileSystemAccessRequest &lhs,
    const QWebEngineFileSystemAccessRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html#operator!=

    Parameters
    ----------

    rhs : QWebEngineFileSystemAccessRequest
      Passed on as a value: Qt reads the C++
      QWebEngineFileSystemAccessRequest, which stays Python's own.
    """
    #  bool operator!=(const QWebEngineFileSystemAccessRequest &lhs, const
    #      QWebEngineFileSystemAccessRequest &rhs)
    return Rituals.call(
        'ritual_ZneRK33QWebEngineFileSystemAccessRequestS1_',
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
    Notes what was given, for Qt's
    'QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html
    """
    #  QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest()
    self._noteCreation(
        QWebEngineFileSystemAccessRequest, lambda: Rituals.call(
            'ritual_ZN33QWebEngineFileSystemAccessRequestC1Ev',
        ))

  @overload(THIS)
  def __init__(self, other: QWebEngineFileSystemAccessRequest) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineFileSystemAccessRequest::QWebEngineFileSystemAccessRequest(
    const QWebEngineFileSystemAccessRequest &other)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html

    Parameters
    ----------

    other : QWebEngineFileSystemAccessRequest
      Passed on as a value: Qt reads the C++
      QWebEngineFileSystemAccessRequest, which stays Python's own.
    """
    #  QWebEngineFileSystemAccessRequest::
    #      QWebEngineFileSystemAccessRequest(const
    #      QWebEngineFileSystemAccessRequest &other)
    self._noteCreation(
        QWebEngineFileSystemAccessRequest, lambda: Rituals.call(
            'ritual_ZN33QWebEngineFileSystemAccessRequestC1ERKS_',
            self._valueOf(other),
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

  def accept(self) -> None:
    """
    Calls Qt's 'void QWebEngineFileSystemAccessRequest::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html#accept
    """
    #  void QWebEngineFileSystemAccessRequest::accept()
    self.uglySide.call(
        'ritual_ZN33QWebEngineFileSystemAccessRequest6acceptEv',
    )

  def reject(self) -> None:
    """
    Calls Qt's 'void QWebEngineFileSystemAccessRequest::reject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefilesystemaccessrequest.html#reject
    """
    #  void QWebEngineFileSystemAccessRequest::reject()
    self.uglySide.call(
        'ritual_ZN33QWebEngineFileSystemAccessRequest6rejectEv',
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void
    QWebEngineFileSystemAccessRequest::swap(QWebEngineFileSystemAccessRequest
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEngineFileSystemAccessRequest.swap' has no cute function yet. "
        "Qt's 'void "
        "QWebEngineFileSystemAccessRequest::swap(QWebEngineFileSystemAccessR"
        "equest &other)': takes a type Python has no way to hand over yet.")
