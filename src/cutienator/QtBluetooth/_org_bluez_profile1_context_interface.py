"""
OrgBluezProfile1ContextInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/profile1context_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means OrgBluezProfile1ContextInterface to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtDBus import QDBusObjectPath, QDBusUnixFileDescriptor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusObjectPath = WAIT['QDBusObjectPath']
  QDBusUnixFileDescriptor = WAIT['QDBusUnixFileDescriptor']
  QVariant = WAIT['QVariant']


class OrgBluezProfile1ContextInterface(QObject):
  """
  The cute side of Qt's OrgBluezProfile1ContextInterface: a plain Python
  object standing in front of one C++ OrgBluezProfile1ContextInterface.

  It is built on the cute 'QObject', as Qt's OrgBluezProfile1ContextInterface
  is built on Qt's QObject, and has everything that class has. Qt's
  OrgBluezProfile1ContextInterface is built on Qt's QDBusContext as well,
  which is not reflected.

  What exists
  -----------

  Every function of Qt's OrgBluezProfile1ContextInterface that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject',
  'newConnection', 'NewConnection', 'RequestDisconnection', 'Release'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *OrgBluezProfile1ContextInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int OrgBluezProfile1ContextInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 2 leans on
  'OrgBluezProfile1ContextInterface.

  What to expect
  --------------

  - The C++ OrgBluezProfile1ContextInterface is created at the first use, not
    by 'OrgBluezProfile1ContextInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ OrgBluezProfile1ContextInterface.
  - Qt tells when it has removed the C++ OrgBluezProfile1ContextInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's OrgBluezProfile1ContextInterface that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'OrgBluezProfile1ContextInterface'

  #  A C++ OrgBluezProfile1ContextInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_OrgBluezProfile1ContextInterface'

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
    *OrgBluezProfile1ContextInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/orgbluezprofile1contextinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *OrgBluezProfile1ContextInterface::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32OrgBluezProfile1ContextInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'OrgBluezProfile1ContextInterface::OrgBluezProfile1ContextInterface(
    QObject *parent)': leans on
    'OrgBluezProfile1ContextInterface::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'OrgBluezProfile1ContextInterface.__init__' has no cute function "
        "yet. Qt's "
        "'OrgBluezProfile1ContextInterface::OrgBluezProfile1ContextInterface"
        "(QObject *parent)': leans on "
        "'OrgBluezProfile1ContextInterface::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QDBusUnixFileDescriptor)
  def newConnection(self, fd: QDBusUnixFileDescriptor) -> None:
    """
    Calls Qt's 'void OrgBluezProfile1ContextInterface::newConnection(const
    QDBusUnixFileDescriptor &fd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/orgbluezprofile1contextinterface.html

    Parameters
    ----------

    fd : QDBusUnixFileDescriptor
      Passed on as a value: Qt reads the C++ QDBusUnixFileDescriptor, which
      stays Python's own.
    """
    #  void OrgBluezProfile1ContextInterface::newConnection(const
    #      QDBusUnixFileDescriptor &fd)
    self.uglySide.call(
        'ritual_ZN32OrgBluezProfile1ContextInterface13newConnectionERK23QDB'
        'usUnixFileDescriptor',
        self._valueOf(fd),
    )

  @overload(QDBusObjectPath, QDBusUnixFileDescriptor, QMap[str, QVariant])
  def NewConnection(
      self,
      a0: QDBusObjectPath,
      a1: QDBusUnixFileDescriptor,
      a2: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void OrgBluezProfile1ContextInterface::NewConnection(const
    QDBusObjectPath &a0, const QDBusUnixFileDescriptor &a1, const QVariantMap
    &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/orgbluezprofile1contextinterface.html

    Parameters
    ----------

    a0 : QDBusObjectPath
      Passed on as a value: Qt reads the C++ QDBusObjectPath, which stays
      Python's own.

    a1 : QDBusUnixFileDescriptor
      Passed on as a value: Qt reads the C++ QDBusUnixFileDescriptor, which
      stays Python's own.

    a2 : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void OrgBluezProfile1ContextInterface::NewConnection(const
    #      QDBusObjectPath &a0, const QDBusUnixFileDescriptor &a1, const
    #      QVariantMap &a2)
    self.uglySide.call(
        'ritual_ZN32OrgBluezProfile1ContextInterface13NewConnectionERK15QDB'
        'usObjectPathRK23QDBusUnixFileDescriptorRK4QMapI7QString8QVariantE',
        self._valueOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  @overload(QDBusObjectPath)
  def RequestDisconnection(self, a0: QDBusObjectPath) -> None:
    """
    Calls Qt's 'void
    OrgBluezProfile1ContextInterface::RequestDisconnection(const
    QDBusObjectPath &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/orgbluezprofile1contextinterface.html

    Parameters
    ----------

    a0 : QDBusObjectPath
      Passed on as a value: Qt reads the C++ QDBusObjectPath, which stays
      Python's own.
    """
    #  void OrgBluezProfile1ContextInterface::RequestDisconnection(const
    #      QDBusObjectPath &a0)
    self.uglySide.call(
        'ritual_ZN32OrgBluezProfile1ContextInterface20RequestDisconnectionE'
        'RK15QDBusObjectPath',
        self._valueOf(a0),
    )

  def Release(self) -> None:
    """
    Calls Qt's 'void OrgBluezProfile1ContextInterface::Release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/orgbluezprofile1contextinterface.html#Release
    """
    #  void OrgBluezProfile1ContextInterface::Release()
    self.uglySide.call(
        'ritual_ZN32OrgBluezProfile1ContextInterface7ReleaseEv',
    )
