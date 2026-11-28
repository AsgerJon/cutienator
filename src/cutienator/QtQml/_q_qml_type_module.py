"""
QQmlTypeModule binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypemodule_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlTypeModule to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTypeRevision
  from . import QHashedStringRef, QQmlType, QQmlTypePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHashedStringRef = WAIT['QHashedStringRef']
  QQmlTypePrivate = WAIT['QQmlTypePrivate']
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeModule(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTypeModule: a plain Python object standing in
  front of one C++ QQmlTypeModule.

  What exists
  -----------

  Every function of Qt's QQmlTypeModule that has a ritual and that Python can
  call so far, 10 names in all: 'add', 'remove', 'lockLevel', 'setLockLevel',
  'module', 'majorVersion', 'addMinorVersion', 'minimumMinorVersion',
  'maximumMinorVersion', 'type'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlTypeModule::walkCompositeSingletons(const
    std::function<void (const QQmlType &)> &callback) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlType QQmlTypeModule::findType(const QList<QQmlTypePrivate *>
    *types, QTypeRevision version)': names 'QList<QQmlTypePrivate *>', which
    has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlTypeModule is created at the first use, not by
    'QQmlTypeModule(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTypeModule.
  - Each name of Qt's QQmlTypeModule that has no cute function yet,
    'findType', 'walkCompositeSingletons', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlTypeModule, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LockLevel(CuteNum, scoped=True):
    """
    The enum 'QQmlTypeModule::LockLevel' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Open = Kee[int](0)
    Weak = Kee[int](1)
    Strong = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTypeModule'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lockLevel(self) -> LockLevel:
    """
    Calls Qt's 'LockLevel QQmlTypeModule::lockLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#lockLevel

    Returns
    -------

    LockLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LockLevel(number)' gives.
    """
    #  LockLevel QQmlTypeModule::lockLevel() const
    return QQmlTypeModule.LockLevel(self.uglySide.call(
        'ritual_ZNK14QQmlTypeModule9lockLevelEv',
    ))

  def module(self) -> str:
    """
    Calls Qt's 'QString QQmlTypeModule::module() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#module

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeModule::module() const
    return self.uglySide.call('ritual_ZNK14QQmlTypeModule6moduleEv')

  def majorVersion(self) -> int:
    """
    Calls Qt's 'quint8 QQmlTypeModule::majorVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#majorVersion
    """
    #  quint8 QQmlTypeModule::majorVersion() const
    return self.uglySide.call('ritual_ZNK14QQmlTypeModule12majorVersionEv')

  def minimumMinorVersion(self) -> int:
    """
    Calls Qt's 'quint8 QQmlTypeModule::minimumMinorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypemodule.html#minimumMinorVersion
    """
    #  quint8 QQmlTypeModule::minimumMinorVersion() const
    return self.uglySide.call(
        'ritual_ZNK14QQmlTypeModule19minimumMinorVersionEv',
    )

  def maximumMinorVersion(self) -> int:
    """
    Calls Qt's 'quint8 QQmlTypeModule::maximumMinorVersion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypemodule.html#maximumMinorVersion
    """
    #  quint8 QQmlTypeModule::maximumMinorVersion() const
    return self.uglySide.call(
        'ritual_ZNK14QQmlTypeModule19maximumMinorVersionEv',
    )

  @overload(QHashedStringRef, QTypeRevision)
  def type(self, name: QHashedStringRef, version: QTypeRevision) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlTypeModule::type(const QHashedStringRef &name,
    QTypeRevision version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#type

    Parameters
    ----------

    name : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlTypeModule::type(const QHashedStringRef &name,
    #      QTypeRevision version) const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlTypeModule4typeERK16QHashedStringRef13QTypeRevisio'
        'n',
        self._valueOf(name), self._valueOf(version),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @overload(WAIT['QV4.String'], QTypeRevision)
  @overload(NoneType, QTypeRevision)
  def type(
      self,
      name: Optional[QV4.String],
      version: QTypeRevision,
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlTypeModule::type(const QV4::String *name,
    QTypeRevision version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#type

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlTypeModule::type(const QV4::String *name, QTypeRevision
    #      version) const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlTypeModule4typeEPKN3QV46StringE13QTypeRevision',
        self._addressOf(name), self._valueOf(version),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(LockLevel)
  def setLockLevel(self, mode: LockLevel) -> bool:
    """
    Calls Qt's 'bool QQmlTypeModule::setLockLevel(LockLevel mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#setLockLevel

    Parameters
    ----------

    mode : LockLevel
      Passed on as its number.
    """
    #  bool QQmlTypeModule::setLockLevel(LockLevel mode)
    return self.uglySide.call(
        'ritual_ZN14QQmlTypeModule12setLockLevelENS_9LockLevelE', mode.value,
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
    Notes what was given, for Qt's 'QQmlTypeModule::QQmlTypeModule()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#QQmlTypeModule
    """
    #  QQmlTypeModule::QQmlTypeModule()
    self._noteCreation(QQmlTypeModule, lambda: Rituals.call(
        'ritual_ZN14QQmlTypeModuleC1Ev',
    ))

  @overload(str, int)
  def __init__(self, uri: str, majorVersion: int) -> None:
    """
    Notes what was given, for Qt's 'QQmlTypeModule::QQmlTypeModule(const
    QString &uri, quint8 majorVersion)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#QQmlTypeModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    majorVersion : int
      Passed on as it is.
    """
    #  QQmlTypeModule::QQmlTypeModule(const QString &uri, quint8
    #      majorVersion)
    self._noteCreation(QQmlTypeModule, lambda: Rituals.call(
        'ritual_ZN14QQmlTypeModuleC1ERK7QStringh', uri, majorVersion,
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

  @overload(QQmlTypePrivate)
  @overload(NoneType)
  def add(self, a0: Optional[QQmlTypePrivate]) -> None:
    """
    Calls Qt's 'void QQmlTypeModule::add(QQmlTypePrivate *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#add

    Parameters
    ----------

    a0 : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeModule::add(QQmlTypePrivate *a0)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeModule3addEP15QQmlTypePrivate',
        self._addressOf(a0),
    )

  @overload(QQmlTypePrivate)
  @overload(NoneType)
  def remove(self, type: Optional[QQmlTypePrivate]) -> None:
    """
    Calls Qt's 'void QQmlTypeModule::remove(const QQmlTypePrivate *type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypemodule.html#remove

    Parameters
    ----------

    type : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTypeModule::remove(const QQmlTypePrivate *type)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeModule6removeEPK15QQmlTypePrivate',
        self._addressOf(type),
    )

  @overload(int)
  def addMinorVersion(self, minorVersion: int) -> None:
    """
    Calls Qt's 'void QQmlTypeModule::addMinorVersion(quint8 minorVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypemodule.html#addMinorVersion

    Parameters
    ----------

    minorVersion : int
      Passed on as it is.
    """
    #  void QQmlTypeModule::addMinorVersion(quint8 minorVersion)
    self.uglySide.call(
        'ritual_ZN14QQmlTypeModule15addMinorVersionEh', minorVersion,
    )

  @staticmethod
  def findType(*__, **_) -> Never:
    """
    Qt's 'QQmlType QQmlTypeModule::findType(const QList<QQmlTypePrivate *>
    *types, QTypeRevision version)': names 'QList<QQmlTypePrivate *>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlTypeModule.findType' has no cute function yet. Qt's 'QQmlType "
        "QQmlTypeModule::findType(const QList<QQmlTypePrivate *> *types, "
        "QTypeRevision version)': names 'QList<QQmlTypePrivate *>', which "
        "has no cute class yet.")

  @staticmethod
  def walkCompositeSingletons(*__, **_) -> Never:
    """
    Qt's 'void QQmlTypeModule::walkCompositeSingletons(const
    std::function<void (const QQmlType &)> &callback) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeModule.walkCompositeSingletons' has no cute function yet. "
        "Qt's 'void QQmlTypeModule::walkCompositeSingletons(const "
        "std::function<void (const QQmlType &)> &callback) const': takes a "
        "type Python has no way to hand over yet.")
