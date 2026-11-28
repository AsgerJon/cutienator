"""
QMediaMetaData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qmediametadata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug, QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']
  QVariant = WAIT['QVariant']


class QMediaMetaData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMediaMetaData: a plain Python object standing in
  front of one C++ QMediaMetaData.

  C++ hands a QMediaMetaData around as a copy, so every C++ QMediaMetaData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMediaMetaData that has a ritual and that Python can
  call so far, 11 names in all: 'value', 'insert', 'remove', 'clear',
  'isEmpty', 'stringValue', 'metaDataKeyToString', '__rlshift__', '__eq__',
  '__ne__', 'keyType'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<Key> QMediaMetaData::keys() const': gives a type Python has
    no way to take yet.
  - Qt's 'QVariant &QMediaMetaData::operator[](Key k)': gives a type Python
    has no way to take yet.
  - Qt's 'QMediaMetaData::~QMediaMetaData()': the destructor: Python removes
    its C++ QMediaMetaData by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 3 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QMediaMetaData is created at the first use, not by
    'QMediaMetaData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMediaMetaData back gives a copy the ritual made for
    Python, in a new cute QMediaMetaData.
  - Each name of Qt's QMediaMetaData that has no cute function yet,
    'asKeyValueRange', 'keys', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMediaMetaData, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Key(CuteNum):
    """
    The enum 'QMediaMetaData::Key' of Qt, with the 29 names Qt gives in it.
    """

    Title = Kee[int](0)
    Author = Kee[int](1)
    Comment = Kee[int](2)
    Description = Kee[int](3)
    Genre = Kee[int](4)
    Date = Kee[int](5)
    Language = Kee[int](6)
    Publisher = Kee[int](7)
    Copyright = Kee[int](8)
    Url = Kee[int](9)
    Duration = Kee[int](10)
    MediaType = Kee[int](11)
    FileFormat = Kee[int](12)
    AudioBitRate = Kee[int](13)
    AudioCodec = Kee[int](14)
    VideoBitRate = Kee[int](15)
    VideoCodec = Kee[int](16)
    VideoFrameRate = Kee[int](17)
    AlbumTitle = Kee[int](18)
    AlbumArtist = Kee[int](19)
    ContributingArtist = Kee[int](20)
    TrackNumber = Kee[int](21)
    Composer = Kee[int](22)
    LeadPerformer = Kee[int](23)
    ThumbnailImage = Kee[int](24)
    CoverArtImage = Kee[int](25)
    Orientation = Kee[int](26)
    Resolution = Kee[int](27)
    HasHdrContent = Kee[int](28)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Key)
  def metaDataKeyToString(k: Key) -> str:
    """
    Calls Qt's 'QString QMediaMetaData::metaDataKeyToString(Key k)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediametadata.html#metaDataKeyToString

    Parameters
    ----------

    k : Key
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaMetaData::metaDataKeyToString(Key k)
    return Rituals.call(
        'ritual_ZN14QMediaMetaData19metaDataKeyToStringENS_3KeyE', k.value,
    )

  @staticmethod
  @overload(Key)
  def keyType(key: Key) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMediaMetaData::keyType(Key key)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#keyType

    Parameters
    ----------

    key : Key
      Passed on as its number.

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMediaMetaData::keyType(Key key)
    address = Rituals.call(
        'ritual_ZN14QMediaMetaData7keyTypeENS_3KeyE', key.value,
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaMetaData'

  #  Qt's '~QMediaMetaData()'. Naming it makes this a value class: Python
  #  owns every C++ QMediaMetaData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QMediaMetaDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Key)
  def value(self, k: Key) -> QVariant:
    """
    Calls Qt's 'QVariant QMediaMetaData::value(Key k) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#value

    Parameters
    ----------

    k : Key
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMediaMetaData::value(Key k) const
    address = self.uglySide.call(
        'ritual_ZNK14QMediaMetaData5valueENS_3KeyE', k.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QMediaMetaData::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#isEmpty
    """
    #  bool QMediaMetaData::isEmpty() const
    return self.uglySide.call('ritual_ZNK14QMediaMetaData7isEmptyEv')

  @overload(Key)
  def stringValue(self, k: Key) -> str:
    """
    Calls Qt's 'QString QMediaMetaData::stringValue(Key k) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#stringValue

    Parameters
    ----------

    k : Key
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMediaMetaData::stringValue(Key k) const
    return self.uglySide.call(
        'ritual_ZNK14QMediaMetaData11stringValueENS_3KeyE', k.value,
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
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QMediaMetaData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QMediaMetaData &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK14QMediaMetaData',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
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

  @overload(THIS)
  def __eq__(self, b: QMediaMetaData) -> bool:
    """
    Calls Qt's 'bool operator==(const QMediaMetaData &a, const QMediaMetaData
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#operator==

    Parameters
    ----------

    b : QMediaMetaData
      Passed on as a value: Qt reads the C++ QMediaMetaData, which stays
      Python's own.
    """
    #  bool operator==(const QMediaMetaData &a, const QMediaMetaData &b)
    return Rituals.call(
        'ritual_ZeqRK14QMediaMetaDataS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QMediaMetaData) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMediaMetaData &a, const QMediaMetaData
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#operator!=

    Parameters
    ----------

    b : QMediaMetaData
      Passed on as a value: Qt reads the C++ QMediaMetaData, which stays
      Python's own.
    """
    #  bool operator!=(const QMediaMetaData &a, const QMediaMetaData &b)
    return Rituals.call(
        'ritual_ZneRK14QMediaMetaDataS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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

  @overload(Key, QVariant)
  def insert(self, k: Key, value: QVariant) -> None:
    """
    Calls Qt's 'void QMediaMetaData::insert(Key k, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#insert

    Parameters
    ----------

    k : Key
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QMediaMetaData::insert(Key k, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN14QMediaMetaData6insertENS_3KeyERK8QVariant',
        k.value, self._valueOf(value),
    )

  @overload(Key)
  def remove(self, k: Key) -> None:
    """
    Calls Qt's 'void QMediaMetaData::remove(Key k)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#remove

    Parameters
    ----------

    k : Key
      Passed on as its number.
    """
    #  void QMediaMetaData::remove(Key k)
    self.uglySide.call('ritual_ZN14QMediaMetaData6removeENS_3KeyE', k.value)

  def clear(self) -> None:
    """
    Calls Qt's 'void QMediaMetaData::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediametadata.html#clear
    """
    #  void QMediaMetaData::clear()
    self.uglySide.call('ritual_ZN14QMediaMetaData5clearEv')

  @staticmethod
  def asKeyValueRange(*__, **_) -> Never:
    """
    Qt's 'QMediaMetaData::asKeyValueRange': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QMediaMetaData.asKeyValueRange' has no cute function yet. Qt's "
        "'QMediaMetaData::asKeyValueRange': a template: a pattern and no "
        "single function.")

  @staticmethod
  def keys(*__, **_) -> Never:
    """
    Qt's 'QList<Key> QMediaMetaData::keys() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QMediaMetaData.keys' has no cute function yet. Qt's 'QList<Key> "
        "QMediaMetaData::keys() const': gives a type Python has no way to "
        "take yet.")


#  Qt's 'QList<QMediaMetaData>': the list of QMediaMetaData, which
#  'QList[QMediaMetaData]' gives. It is made here, so that there is one as
#  soon as there can be a QMediaMetaData.
QList.createKind(
    QMediaMetaData, 'value',
    make='ritual_list_make_QMediaMetaData',
    add='ritual_list_add_QMediaMetaData',
    size='ritual_list_size_QMediaMetaData',
    at='ritual_list_at_QMediaMetaData',
    drop='ritual_list_drop_QMediaMetaData',
)
