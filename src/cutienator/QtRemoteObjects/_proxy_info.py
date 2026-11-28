"""
ProxyInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means ProxyInfo to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import ProxyReplicaInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  ProxyReplicaInfo = WAIT['ProxyReplicaInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ProxyInfo(QObject):
  """
  The cute side of Qt's ProxyInfo: a plain Python object standing in front of
  one C++ ProxyInfo.

  It is built on the cute 'QObject', as Qt's ProxyInfo is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ProxyInfo that has a ritual and that Python can call
  so far, 2 names in all: 'metaObject', 'disableAndDeleteObject'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ProxyInfo::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int ProxyInfo::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'ProxyInfo::~ProxyInfo()': the destructor: Python never removes a
    C++ ProxyInfo.
  - Qt's 'void ProxyInfo::proxyObject(const QRemoteObjectSourceLocation
    &entry, ProxyDirection direction)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void ProxyInfo::unproxyObject(const QRemoteObjectSourceLocation
    &entry)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 3 leans on 'ProxyInfo; 2 not a gap.

  What to expect
  --------------

  - The C++ ProxyInfo is created at the first use, not by 'ProxyInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ProxyInfo.
  - Qt tells when it has removed the C++ ProxyInfo. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's ProxyInfo that has no cute function yet, '__init__',
    'proxyObject', 'setReverseProxy', 'unproxyObject', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside ProxyInfo, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ProxyDirection(CuteNum, scoped=True):
    """
    The enum 'ProxyInfo::ProxyDirection' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Forward = Kee[int](0)
    Reverse = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ProxyInfo'

  #  A C++ ProxyInfo Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ProxyInfo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ProxyInfo::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/proxyinfo.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ProxyInfo::metaObject() const
    address = self.uglySide.call('ritual_ZNK9ProxyInfo10metaObjectEv')
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
    Qt's 'ProxyInfo::ProxyInfo(QRemoteObjectNode *node, QRemoteObjectHostBase
    *parent, QRemoteObjectHostBase::RemoteObjectNameFilter filter)': leans on
    'ProxyInfo::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'ProxyInfo.__init__' has no cute function yet. Qt's "
        "'ProxyInfo::ProxyInfo(QRemoteObjectNode *node, "
        "QRemoteObjectHostBase *parent, "
        "QRemoteObjectHostBase::RemoteObjectNameFilter filter)': leans on "
        "'ProxyInfo::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(ProxyReplicaInfo)
  @overload(NoneType)
  def disableAndDeleteObject(self, info: Optional[ProxyReplicaInfo]) -> None:
    """
    Calls Qt's 'void ProxyInfo::disableAndDeleteObject(ProxyReplicaInfo
    *info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proxyinfo.html#disableAndDeleteObject

    Parameters
    ----------

    info : Optional[ProxyReplicaInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ProxyInfo::disableAndDeleteObject(ProxyReplicaInfo *info)
    self.uglySide.call(
        'ritual_ZN9ProxyInfo22disableAndDeleteObjectEP16ProxyReplicaInfo',
        self._addressOf(info),
    )

  @staticmethod
  def proxyObject(*__, **_) -> Never:
    """
    Qt's 'void ProxyInfo::proxyObject(const QRemoteObjectSourceLocation
    &entry, ProxyDirection direction)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'ProxyInfo.proxyObject' has no cute function yet. Qt's 'void "
        "ProxyInfo::proxyObject(const QRemoteObjectSourceLocation &entry, "
        "ProxyDirection direction)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setReverseProxy(*__, **_) -> Never:
    """
    Qt's 'bool
    ProxyInfo::setReverseProxy(QRemoteObjectHostBase::RemoteObjectNameFilter
    filter)': leans on 'ProxyInfo::staticMetaObject', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'ProxyInfo.setReverseProxy' has no cute function yet. Qt's 'bool "
        "ProxyInfo::setReverseProxy(QRemoteObjectHostBase::RemoteObjectNameF"
        "ilter filter)': leans on 'ProxyInfo::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def unproxyObject(*__, **_) -> Never:
    """
    Qt's 'void ProxyInfo::unproxyObject(const QRemoteObjectSourceLocation
    &entry)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ProxyInfo.unproxyObject' has no cute function yet. Qt's 'void "
        "ProxyInfo::unproxyObject(const QRemoteObjectSourceLocation "
        "&entry)': takes a type Python has no way to hand over yet.")
