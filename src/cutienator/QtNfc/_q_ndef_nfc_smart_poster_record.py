"""
QNdefNfcSmartPosterRecord binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qndefnfcsmartposterrecord.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QNdefNfcTextRecord, QNdefRecord

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QUrl
  from . import QNdefNfcIconRecord, QNdefNfcUriRecord
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNdefNfcIconRecord = WAIT['QNdefNfcIconRecord']
  QNdefNfcUriRecord = WAIT['QNdefNfcUriRecord']
  QUrl = WAIT['QUrl']


class QNdefNfcSmartPosterRecord(QNdefRecord):
  """
  The cute side of Qt's QNdefNfcSmartPosterRecord: a plain Python object
  standing in front of one C++ QNdefNfcSmartPosterRecord.

  It is built on the cute 'QNdefRecord', as Qt's QNdefNfcSmartPosterRecord is
  built on Qt's QNdefRecord, and has everything that class has.

  C++ hands a QNdefNfcSmartPosterRecord around as a copy, so every C++
  QNdefNfcSmartPosterRecord behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNdefNfcSmartPosterRecord that has a ritual and that
  Python can call so far, 33 names in all: 'setPayload', 'hasTitle',
  'hasAction', 'hasIcon', 'hasSize', 'hasTypeInfo', 'titleCount',
  'titleRecord', 'title', 'titleRecords', 'addTitle', 'removeTitle',
  'setTitles', 'uri', 'uriRecord', 'setUri', 'action', 'setAction',
  'iconCount', 'iconRecord', 'icon', 'iconRecords', 'addIcon', 'removeIcon',
  'setIcons', 'size', 'setSize', 'typeInfo', 'setTypeInfo', 'cleanup',
  'convertToPayload', 'addTitleInternal', 'addIconInternal'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNdefNfcSmartPosterRecord
    &QNdefNfcSmartPosterRecord::operator=(const QNdefNfcSmartPosterRecord
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QNdefNfcSmartPosterRecord::~QNdefNfcSmartPosterRecord()': the
    destructor: Python removes its C++ QNdefNfcSmartPosterRecord by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QNdefNfcSmartPosterRecord is created at the first use, not by
    'QNdefNfcSmartPosterRecord(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNdefNfcSmartPosterRecord back gives a copy the
    ritual made for Python, in a new cute QNdefNfcSmartPosterRecord.
  """

  #  The enums Qt writes inside QNdefNfcSmartPosterRecord, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Action(CuteNum):
    """
    The enum 'QNdefNfcSmartPosterRecord::Action' of Qt, with the 4 names Qt
    gives in it.
    """

    UnspecifiedAction = Kee[int](-1)
    DoAction = Kee[int](0)
    SaveAction = Kee[int](1)
    EditAction = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNdefNfcSmartPosterRecord'

  #  Qt's '~QNdefNfcSmartPosterRecord()'. Naming it makes this a value class:
  #  Python owns every C++ QNdefNfcSmartPosterRecord behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QNdefNfcSmartPosterRecordD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(str)
  def hasTitle(self, locale: str = '') -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::hasTitle(const QString
    &locale) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#hasTitle

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QNdefNfcSmartPosterRecord::hasTitle(const QString &locale) const
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord8hasTitleERK7QString', locale,
    )

  def hasAction(self) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::hasAction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#hasAction
    """
    #  bool QNdefNfcSmartPosterRecord::hasAction() const
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord9hasActionEv',
    )

  @overload()
  @overload(QByteArray)
  def hasIcon(self, mimetype: Optional[QByteArray] = None) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::hasIcon(const QByteArray
    &mimetype) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#hasIcon

    Parameters
    ----------

    mimetype : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  bool QNdefNfcSmartPosterRecord::hasIcon(const QByteArray &mimetype)
    #      const
    if mimetype is None:
      from ..QtCore import QByteArray
      mimetype = QByteArray()
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord7hasIconERK10QByteArray',
        self._valueOf(mimetype),
    )

  def hasSize(self) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::hasSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#hasSize
    """
    #  bool QNdefNfcSmartPosterRecord::hasSize() const
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord7hasSizeEv',
    )

  def hasTypeInfo(self) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::hasTypeInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#hasTypeInfo
    """
    #  bool QNdefNfcSmartPosterRecord::hasTypeInfo() const
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord11hasTypeInfoEv',
    )

  def titleCount(self) -> int:
    """
    Calls Qt's 'qsizetype QNdefNfcSmartPosterRecord::titleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#titleCount
    """
    #  qsizetype QNdefNfcSmartPosterRecord::titleCount() const
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord10titleCountEv',
    )

  @overload(int)
  def titleRecord(self, index: int) -> QNdefNfcTextRecord:
    """
    Calls Qt's 'QNdefNfcTextRecord
    QNdefNfcSmartPosterRecord::titleRecord(qsizetype index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#titleRecord

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QNdefNfcTextRecord
      A new cute QNdefNfcTextRecord around the copy Qt gave back. Python owns
      it.
    """
    #  QNdefNfcTextRecord QNdefNfcSmartPosterRecord::titleRecord(qsizetype
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord11titleRecordEx', index,
    )
    return QNdefNfcTextRecord._cuteOwning(address)

  @overload()
  @overload(str)
  def title(self, locale: str = '') -> str:
    """
    Calls Qt's 'QString QNdefNfcSmartPosterRecord::title(const QString
    &locale) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#title

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNdefNfcSmartPosterRecord::title(const QString &locale) const
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord5titleERK7QString', locale,
    )

  def titleRecords(self) -> QList[QNdefNfcTextRecord]:
    """
    Calls Qt's 'QList<QNdefNfcTextRecord>
    QNdefNfcSmartPosterRecord::titleRecords() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#titleRecords

    Returns
    -------

    QList[QNdefNfcTextRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNdefNfcTextRecord> QNdefNfcSmartPosterRecord::titleRecords()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord12titleRecordsEv',
    )
    return QList[QNdefNfcTextRecord]._cuteOwning(address)

  def uri(self) -> QUrl:
    """
    Calls Qt's 'QUrl QNdefNfcSmartPosterRecord::uri() const'.

    Qt's own words: https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#uri

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QNdefNfcSmartPosterRecord::uri() const
    address = self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord3uriEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def uriRecord(self) -> QNdefNfcUriRecord:
    """
    Calls Qt's 'QNdefNfcUriRecord QNdefNfcSmartPosterRecord::uriRecord()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#uriRecord

    Returns
    -------

    QNdefNfcUriRecord
      A new cute QNdefNfcUriRecord around the copy Qt gave back. Python owns
      it.
    """
    #  QNdefNfcUriRecord QNdefNfcSmartPosterRecord::uriRecord() const
    address = self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord9uriRecordEv',
    )
    from . import QNdefNfcUriRecord
    return QNdefNfcUriRecord._cuteOwning(address)

  def action(self) -> Action:
    """
    Calls Qt's 'Action QNdefNfcSmartPosterRecord::action() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#action

    Returns
    -------

    Action
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Action(number)' gives.
    """
    #  Action QNdefNfcSmartPosterRecord::action() const
    return QNdefNfcSmartPosterRecord.Action(self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord6actionEv',
    ))

  def iconCount(self) -> int:
    """
    Calls Qt's 'qsizetype QNdefNfcSmartPosterRecord::iconCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#iconCount
    """
    #  qsizetype QNdefNfcSmartPosterRecord::iconCount() const
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord9iconCountEv',
    )

  @overload(int)
  def iconRecord(self, index: int) -> QNdefNfcIconRecord:
    """
    Calls Qt's 'QNdefNfcIconRecord
    QNdefNfcSmartPosterRecord::iconRecord(qsizetype index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#iconRecord

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QNdefNfcIconRecord
      A new cute QNdefNfcIconRecord around the copy Qt gave back. Python owns
      it.
    """
    #  QNdefNfcIconRecord QNdefNfcSmartPosterRecord::iconRecord(qsizetype
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord10iconRecordEx', index,
    )
    from . import QNdefNfcIconRecord
    return QNdefNfcIconRecord._cuteOwning(address)

  @overload()
  @overload(QByteArray)
  def icon(self, mimetype: Optional[QByteArray] = None) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNdefNfcSmartPosterRecord::icon(const QByteArray
    &mimetype) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#icon

    Parameters
    ----------

    mimetype : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNdefNfcSmartPosterRecord::icon(const QByteArray &mimetype)
    #      const
    if mimetype is None:
      from ..QtCore import QByteArray
      mimetype = QByteArray()
    address = self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord4iconERK10QByteArray',
        self._valueOf(mimetype),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def iconRecords(self) -> QList[QNdefNfcIconRecord]:
    """
    Calls Qt's 'QList<QNdefNfcIconRecord>
    QNdefNfcSmartPosterRecord::iconRecords() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#iconRecords

    Returns
    -------

    QList[QNdefNfcIconRecord]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QNdefNfcIconRecord> QNdefNfcSmartPosterRecord::iconRecords()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord11iconRecordsEv',
    )
    from . import QNdefNfcIconRecord
    return QList[QNdefNfcIconRecord]._cuteOwning(address)

  def size(self) -> int:
    """
    Calls Qt's 'quint32 QNdefNfcSmartPosterRecord::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#size
    """
    #  quint32 QNdefNfcSmartPosterRecord::size() const
    return self.uglySide.call('ritual_ZNK25QNdefNfcSmartPosterRecord4sizeEv')

  def typeInfo(self) -> str:
    """
    Calls Qt's 'QString QNdefNfcSmartPosterRecord::typeInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#typeInfo

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QNdefNfcSmartPosterRecord::typeInfo() const
    return self.uglySide.call(
        'ritual_ZNK25QNdefNfcSmartPosterRecord8typeInfoEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setPayload(self, payload: QByteArray) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::setPayload(const QByteArray
    &payload)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#setPayload

    Parameters
    ----------

    payload : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNdefNfcSmartPosterRecord::setPayload(const QByteArray &payload)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord10setPayloadERK10QByteArray',
        self._valueOf(payload),
    )

  @overload(QList[QNdefNfcTextRecord])
  def setTitles(self, titles: QList[QNdefNfcTextRecord]) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::setTitles(const
    QList<QNdefNfcTextRecord> &titles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#setTitles

    Parameters
    ----------

    titles : QList[QNdefNfcTextRecord]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNdefNfcSmartPosterRecord::setTitles(const
    #      QList<QNdefNfcTextRecord> &titles)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord9setTitlesERK5QListI18QNdefNfc'
        'TextRecordE',
        self._valueOf(titles),
    )

  @overload(QNdefNfcUriRecord)
  def setUri(self, url: QNdefNfcUriRecord) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::setUri(const
    QNdefNfcUriRecord &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#setUri

    Parameters
    ----------

    url : QNdefNfcUriRecord
      Passed on as a value: Qt reads the C++ QNdefNfcUriRecord, which stays
      Python's own.
    """
    #  void QNdefNfcSmartPosterRecord::setUri(const QNdefNfcUriRecord &url)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord6setUriERK17QNdefNfcUriRecord',
        self._valueOf(url),
    )

  @overload(QUrl)
  def setUri(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::setUri(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#setUri

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNdefNfcSmartPosterRecord::setUri(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord6setUriERK4QUrl',
        self._valueOf(url),
    )

  @overload(Action)
  def setAction(self, act: Action) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::setAction(Action act)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#setAction

    Parameters
    ----------

    act : Action
      Passed on as its number.
    """
    #  void QNdefNfcSmartPosterRecord::setAction(Action act)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord9setActionENS_6ActionE',
        act.value,
    )

  @overload(QList[QNdefNfcIconRecord])
  def setIcons(self, icons: QList[QNdefNfcIconRecord]) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::setIcons(const
    QList<QNdefNfcIconRecord> &icons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#setIcons

    Parameters
    ----------

    icons : QList[QNdefNfcIconRecord]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNdefNfcSmartPosterRecord::setIcons(const
    #      QList<QNdefNfcIconRecord> &icons)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord8setIconsERK5QListI18QNdefNfcI'
        'conRecordE',
        self._valueOf(icons),
    )

  @overload(int)
  def setSize(self, size: int) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::setSize(quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#setSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QNdefNfcSmartPosterRecord::setSize(quint32 size)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord7setSizeEj', size,
    )

  @overload(str)
  def setTypeInfo(self, type: str) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::setTypeInfo(const QString
    &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#setTypeInfo

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNdefNfcSmartPosterRecord::setTypeInfo(const QString &type)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord11setTypeInfoERK7QString', type,
    )

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
    'QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html
    """
    #  QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord()
    self._noteCreation(QNdefNfcSmartPosterRecord, lambda: Rituals.call(
        'ritual_ZN25QNdefNfcSmartPosterRecordC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QNdefNfcSmartPosterRecord) -> None:
    """
    Notes what was given, for Qt's
    'QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord(const
    QNdefNfcSmartPosterRecord &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html

    Parameters
    ----------

    other : QNdefNfcSmartPosterRecord
      Passed on as a value: Qt reads the C++ QNdefNfcSmartPosterRecord, which
      stays Python's own.
    """
    #  QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord(const
    #      QNdefNfcSmartPosterRecord &other)
    self._noteCreation(QNdefNfcSmartPosterRecord, lambda: Rituals.call(
        'ritual_ZN25QNdefNfcSmartPosterRecordC1ERKS_', self._valueOf(other),
    ))

  @overload(QNdefRecord)
  def __init__(self, other: QNdefRecord) -> None:
    """
    Notes what was given, for Qt's
    'QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord(const QNdefRecord
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html

    Parameters
    ----------

    other : QNdefRecord
      Passed on as a value: Qt reads the C++ QNdefRecord, which stays
      Python's own.
    """
    #  QNdefNfcSmartPosterRecord::QNdefNfcSmartPosterRecord(const QNdefRecord
    #      &other)
    self._noteCreation(QNdefNfcSmartPosterRecord, lambda: Rituals.call(
        'ritual_ZN25QNdefNfcSmartPosterRecordC1ERK11QNdefRecord',
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

  @overload(QNdefNfcTextRecord)
  def addTitle(self, text: QNdefNfcTextRecord) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::addTitle(const
    QNdefNfcTextRecord &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#addTitle

    Parameters
    ----------

    text : QNdefNfcTextRecord
      Passed on as a value: Qt reads the C++ QNdefNfcTextRecord, which stays
      Python's own.
    """
    #  bool QNdefNfcSmartPosterRecord::addTitle(const QNdefNfcTextRecord
    #      &text)
    return self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord8addTitleERK18QNdefNfcTextReco'
        'rd',
        self._valueOf(text),
    )

  @overload(str, str, QNdefNfcTextRecord.Encoding)
  def addTitle(
      self,
      text: str,
      locale: str,
      encoding: QNdefNfcTextRecord.Encoding,
  ) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::addTitle(const QString &text,
    const QString &locale, QNdefNfcTextRecord::Encoding encoding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#addTitle

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    locale : str
      Passed on as it is: a QString is made of it for the call.

    encoding : QNdefNfcTextRecord.Encoding
      Passed on as its number.
    """
    #  bool QNdefNfcSmartPosterRecord::addTitle(const QString &text, const
    #      QString &locale, QNdefNfcTextRecord::Encoding encoding)
    return self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord8addTitleERK7QStringS2_N18QNde'
        'fNfcTextRecord8EncodingE',
        text, locale, encoding.value,
    )

  @overload(QNdefNfcTextRecord)
  def removeTitle(self, text: QNdefNfcTextRecord) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::removeTitle(const
    QNdefNfcTextRecord &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#removeTitle

    Parameters
    ----------

    text : QNdefNfcTextRecord
      Passed on as a value: Qt reads the C++ QNdefNfcTextRecord, which stays
      Python's own.
    """
    #  bool QNdefNfcSmartPosterRecord::removeTitle(const QNdefNfcTextRecord
    #      &text)
    return self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord11removeTitleERK18QNdefNfcText'
        'Record',
        self._valueOf(text),
    )

  @overload(str)
  def removeTitle(self, locale: str) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::removeTitle(const QString
    &locale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#removeTitle

    Parameters
    ----------

    locale : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QNdefNfcSmartPosterRecord::removeTitle(const QString &locale)
    return self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord11removeTitleERK7QString',
        locale,
    )

  @overload(QNdefNfcIconRecord)
  def addIcon(self, icon: QNdefNfcIconRecord) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::addIcon(const
    QNdefNfcIconRecord &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#addIcon

    Parameters
    ----------

    icon : QNdefNfcIconRecord
      Passed on as a value: Qt reads the C++ QNdefNfcIconRecord, which stays
      Python's own.
    """
    #  void QNdefNfcSmartPosterRecord::addIcon(const QNdefNfcIconRecord
    #      &icon)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord7addIconERK18QNdefNfcIconRecor'
        'd',
        self._valueOf(icon),
    )

  @overload(QByteArray, QByteArray)
  def addIcon(self, type: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::addIcon(const QByteArray
    &type, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#addIcon

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QNdefNfcSmartPosterRecord::addIcon(const QByteArray &type, const
    #      QByteArray &data)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord7addIconERK10QByteArrayS2_',
        self._valueOf(type), self._valueOf(data),
    )

  @overload(QNdefNfcIconRecord)
  def removeIcon(self, icon: QNdefNfcIconRecord) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::removeIcon(const
    QNdefNfcIconRecord &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#removeIcon

    Parameters
    ----------

    icon : QNdefNfcIconRecord
      Passed on as a value: Qt reads the C++ QNdefNfcIconRecord, which stays
      Python's own.
    """
    #  bool QNdefNfcSmartPosterRecord::removeIcon(const QNdefNfcIconRecord
    #      &icon)
    return self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord10removeIconERK18QNdefNfcIconR'
        'ecord',
        self._valueOf(icon),
    )

  @overload(QByteArray)
  def removeIcon(self, type: QByteArray) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::removeIcon(const QByteArray
    &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#removeIcon

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QNdefNfcSmartPosterRecord::removeIcon(const QByteArray &type)
    return self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord10removeIconERK10QByteArray',
        self._valueOf(type),
    )

  def cleanup(self) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#cleanup
    """
    #  void QNdefNfcSmartPosterRecord::cleanup()
    self.uglySide.call('ritual_ZN25QNdefNfcSmartPosterRecord7cleanupEv')

  def convertToPayload(self) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::convertToPayload()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#convertToPayload
    """
    #  void QNdefNfcSmartPosterRecord::convertToPayload()
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord16convertToPayloadEv',
    )

  @overload(QNdefNfcTextRecord)
  def addTitleInternal(self, text: QNdefNfcTextRecord) -> bool:
    """
    Calls Qt's 'bool QNdefNfcSmartPosterRecord::addTitleInternal(const
    QNdefNfcTextRecord &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#addTitleInternal

    Parameters
    ----------

    text : QNdefNfcTextRecord
      Passed on as a value: Qt reads the C++ QNdefNfcTextRecord, which stays
      Python's own.
    """
    #  bool QNdefNfcSmartPosterRecord::addTitleInternal(const
    #      QNdefNfcTextRecord &text)
    return self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord16addTitleInternalERK18QNdefNf'
        'cTextRecord',
        self._valueOf(text),
    )

  @overload(QNdefNfcIconRecord)
  def addIconInternal(self, icon: QNdefNfcIconRecord) -> None:
    """
    Calls Qt's 'void QNdefNfcSmartPosterRecord::addIconInternal(const
    QNdefNfcIconRecord &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qndefnfcsmartposterrecord.html#addIconInternal

    Parameters
    ----------

    icon : QNdefNfcIconRecord
      Passed on as a value: Qt reads the C++ QNdefNfcIconRecord, which stays
      Python's own.
    """
    #  void QNdefNfcSmartPosterRecord::addIconInternal(const
    #      QNdefNfcIconRecord &icon)
    self.uglySide.call(
        'ritual_ZN25QNdefNfcSmartPosterRecord15addIconInternalERK18QNdefNfc'
        'IconRecord',
        self._valueOf(icon),
    )
