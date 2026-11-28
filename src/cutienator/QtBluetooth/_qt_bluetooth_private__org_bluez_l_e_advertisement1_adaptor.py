"""
QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/leadvertisement1adaptor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor to be
#  private: it declares the class in a header it calls private. cutienator
#  does not care. Qt hands objects of the class out all the same, and a class
#  we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class OrgBluezLEAdvertisement1Adaptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor:
  a plain Python object standing in front of one C++
  QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor.

  What exists
  -----------

  Every function of Qt's QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor
  that has a ritual and that Python can call so far, 16 names in all:
  'metaObject', 'discoverable', 'setDiscoverable', 'includes', 'setIncludes',
  'localName', 'setLocalName', 'maxInterval', 'setMaxInterval',
  'minInterval', 'setMinInterval', 'serviceUUIDs', 'setServiceUUIDs', 'type',
  'setType', 'Release'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::
    ~OrgBluezLEAdvertisement1Adaptor()': the destructor: Python never removes
    a C++ QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor.

  What has no ritual
  ------------------

  6 of the 25 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate; 2 leans on
  'qRegisterNormalizedMetaType_ManufacturerDataList(QByteArray const&)',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor is created at
    the first use, not by
    'QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor
    that has no cute function yet, '__init__', 'manufacturerData',
    'setManufacturerData', holds a function that raises
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
  __qt_class__ = 'QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor'

  #  A C++ QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor Python makes
  #  is of a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgBluezLEAdvertisement1Adaptor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor10m'
        'etaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def discoverable(self) -> bool:
    """
    Calls Qt's 'bool
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::discoverable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html
    """
    #  bool
    #      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::discoverable(
    #      ) const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12d'
        'iscoverableEv',
    )

  def includes(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::includes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::includes()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor8in'
        'cludesEv',
    )
    return QStringList._cuteOwning(address)

  def localName(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::localName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::localName()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor9lo'
        'calNameEv',
    )

  def maxInterval(self) -> int:
    """
    Calls Qt's 'uint
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::maxInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html
    """
    #  uint
    #      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::maxInterval()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11m'
        'axIntervalEv',
    )

  def minInterval(self) -> int:
    """
    Calls Qt's 'uint
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::minInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html
    """
    #  uint
    #      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::minInterval()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11m'
        'inIntervalEv',
    )

  def serviceUUIDs(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::serviceUUIDs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::serviceUUIDs(
    #      ) const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12s'
        'erviceUUIDsEv',
    )
    return QStringList._cuteOwning(address)

  def type(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::type()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor4ty'
        'peEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setDiscoverable(self, value: bool) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setDiscoverable(bool
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::
    #      setDiscoverable(bool value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor15se'
        'tDiscoverableEb',
        value,
    )

  @overload(QStringList)
  def setIncludes(self, value: QStringList) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setIncludes(const
    QStringList &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Parameters
    ----------

    value : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setIncludes(
    #      const QStringList &value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor11se'
        'tIncludesERK5QListI7QStringE',
        self._valueOf(value),
    )

  @overload(str)
  def setLocalName(self, value: str) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setLocalName(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setLocalName(
    #      const QString &value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor12se'
        'tLocalNameERK7QString',
        value,
    )

  @overload(int)
  def setMaxInterval(self, value: int) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setMaxInterval(uint
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::
    #      setMaxInterval(uint value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor14se'
        'tMaxIntervalEj',
        value,
    )

  @overload(int)
  def setMinInterval(self, value: int) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setMinInterval(uint
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::
    #      setMinInterval(uint value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor14se'
        'tMinIntervalEj',
        value,
    )

  @overload(QStringList)
  def setServiceUUIDs(self, value: QStringList) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setServiceUUIDs(
    const QStringList &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Parameters
    ----------

    value : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::
    #      setServiceUUIDs(const QStringList &value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor15se'
        'tServiceUUIDsERK5QListI7QStringE',
        self._valueOf(value),
    )

  @overload(str)
  def setType(self, value: str) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setType(const
    QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setType(const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor7set'
        'TypeERK7QString',
        value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::
    OrgBluezLEAdvertisement1Adaptor(QObject *parent)': leans on
    'QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezLEAdvertisement1Adaptor.__init__' has "
        "no cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::OrgBluezLEAdv"
        "ertisement1Adaptor(QObject *parent)': leans on "
        "'QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::qt_metacall(Q"
        "MetaObject::Call, int, void**)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  def Release(self) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::Release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezleadvertisement1adaptor.html
    """
    #  void QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::Release()
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate31OrgBluezLEAdvertisement1Adaptor7Rel'
        'easeEv',
    )

  @staticmethod
  def manufacturerData(*__, **_) -> Never:
    """
    Qt's 'ManufacturerDataList
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::manufacturerData()
    const': leans on
    'qRegisterNormalizedMetaType_ManufacturerDataList(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezLEAdvertisement1Adaptor.manufacturerDat"
        "a' has no cute function yet. Qt's 'ManufacturerDataList "
        "QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::manufacturerDa"
        "ta() const': leans on "
        "'qRegisterNormalizedMetaType_ManufacturerDataList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setManufacturerData(*__, **_) -> Never:
    """
    Qt's 'void
    QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setManufacturerData(
    ManufacturerDataList value)': leans on
    'qRegisterNormalizedMetaType_ManufacturerDataList(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezLEAdvertisement1Adaptor.setManufacturer"
        "Data' has no cute function yet. Qt's 'void "
        "QtBluetoothPrivate::OrgBluezLEAdvertisement1Adaptor::setManufacture"
        "rData(ManufacturerDataList value)': leans on "
        "'qRegisterNormalizedMetaType_ManufacturerDataList(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
