"""
QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/gattdescriptor1adaptor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from ..QtDBus import QDBusMessage, QDBusObjectPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDBusMessage = WAIT['QDBusMessage']
  QVariant = WAIT['QVariant']


class OrgBluezGattDescriptor1Adaptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor: a
  plain Python object standing in front of one C++
  QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor.

  What exists
  -----------

  Every function of Qt's QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor
  that has a ritual and that Python can call so far, 6 names in all:
  'metaObject', 'characteristic', 'uUID', 'value', 'ReadValue', 'WriteValue'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::
    ~OrgBluezGattDescriptor1Adaptor()': the destructor: Python never removes
    a C++ QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 leans on
  'QtBluetoothPrivate.

  What to expect
  --------------

  - The C++ QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor is created at
    the first use, not by
    'QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor.
  - Qt tells when it has removed the C++
    QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor that
    has no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor'

  #  A C++ QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor Python makes is
  #  of a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtBluetoothPrivate_OrgBluezGattDescriptor1Adaptor'

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
    *QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattdescriptor1adaptor.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate30OrgBluezGattDescriptor1Adaptor10me'
        'taObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def characteristic(self) -> QDBusObjectPath:
    """
    Calls Qt's 'QDBusObjectPath
    QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::characteristic()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattdescriptor1adaptor.html

    Returns
    -------

    QDBusObjectPath
      A new cute QDBusObjectPath around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusObjectPath QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::
    #      characteristic() const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate30OrgBluezGattDescriptor1Adaptor14ch'
        'aracteristicEv',
    )
    from ..QtDBus import QDBusObjectPath
    return QDBusObjectPath._cuteOwning(address)

  def uUID(self) -> str:
    """
    Calls Qt's 'QString
    QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::uUID() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattdescriptor1adaptor.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::uUID()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate30OrgBluezGattDescriptor1Adaptor4uUI'
        'DEv',
    )

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattdescriptor1adaptor.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::value()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QtBluetoothPrivate30OrgBluezGattDescriptor1Adaptor5val'
        'ueEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::
    OrgBluezGattDescriptor1Adaptor(QObject *parent)': leans on
    'QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::qt_metacall(
    QMetaObject::Call, int, void**)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtBluetoothPrivate.OrgBluezGattDescriptor1Adaptor.__init__' has "
        "no cute function yet. Qt's "
        "'QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::OrgBluezGattDe"
        "scriptor1Adaptor(QObject *parent)': leans on "
        "'QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::qt_metacall(QM"
        "etaObject::Call, int, void**)', which Qt's source does not mark "
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

  @overload(QMap[str, QVariant], QDBusMessage)
  def ReadValue(
      self,
      options: QMap[str, QVariant],
      msg: QDBusMessage,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::ReadValue(const
    QVariantMap &options, const QDBusMessage &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattdescriptor1adaptor.html

    Parameters
    ----------

    options : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    msg : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray
    #      QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::ReadValue(
    #      const QVariantMap &options, const QDBusMessage &msg)
    address = self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate30OrgBluezGattDescriptor1Adaptor9Read'
        'ValueERK4QMapI7QString8QVariantERK12QDBusMessage',
        self._valueOf(options), self._valueOf(msg),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray, QMap[str, QVariant], QDBusMessage)
  def WriteValue(
      self,
      value: QByteArray,
      options: QMap[str, QVariant],
      msg: QDBusMessage,
  ) -> None:
    """
    Calls Qt's 'void
    QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::WriteValue(const
    QByteArray &value, const QVariantMap &options, const QDBusMessage &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtbluetoothprivate-orgbluezgattdescriptor1adaptor.html

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    options : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    msg : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  void QtBluetoothPrivate::OrgBluezGattDescriptor1Adaptor::WriteValue(
    #      const QByteArray &value, const QVariantMap &options, const
    #      QDBusMessage &msg)
    self.uglySide.call(
        'ritual_ZN18QtBluetoothPrivate30OrgBluezGattDescriptor1Adaptor10Wri'
        'teValueERK10QByteArrayRK4QMapI7QString8QVariantERK12QDBusMessage',
        self._valueOf(value), self._valueOf(options), self._valueOf(msg),
    )
