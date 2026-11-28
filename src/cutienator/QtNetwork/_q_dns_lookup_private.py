"""
QDnsLookupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qdnslookup_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDnsLookupPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDnsLookup


class QDnsLookupPrivate(QObjectPrivate):
  """
  The cute side of Qt's QDnsLookupPrivate: a plain Python object standing in
  front of one C++ QDnsLookupPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QDnsLookupPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDnsLookupPrivate that has a ritual and that Python
  can call so far, 11 names in all: 'nameChanged',
  '_qt_property_name_offset', 'nameserverChanged',
  '_qt_property_nameserver_offset', 'typeChanged',
  '_qt_property_type_offset', 'nameserverPortChanged',
  '_qt_property_port_offset', 'nameserverProtocolChanged',
  '_qt_property_protocol_offset', 'q_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QDnsLookup *QDnsLookupPrivate::q_func() const': takes in
    Python what 'QDnsLookup *QDnsLookupPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QDnsLookupPrivate is created at the first use, not by
    'QDnsLookupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDnsLookupPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_name_offset() -> int:
    """
    Calls Qt's 'size_t QDnsLookupPrivate::_qt_property_name_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html#_qt_property_name_offset
    """
    #  size_t QDnsLookupPrivate::_qt_property_name_offset()
    return Rituals.call(
        'ritual_ZN17QDnsLookupPrivate24_qt_property_name_offsetEv',
    )

  @staticmethod
  def _qt_property_nameserver_offset() -> int:
    """
    Calls Qt's 'size_t QDnsLookupPrivate::_qt_property_nameserver_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html
    """
    #  size_t QDnsLookupPrivate::_qt_property_nameserver_offset()
    return Rituals.call(
        'ritual_ZN17QDnsLookupPrivate30_qt_property_nameserver_offsetEv',
    )

  @staticmethod
  def _qt_property_type_offset() -> int:
    """
    Calls Qt's 'size_t QDnsLookupPrivate::_qt_property_type_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html#_qt_property_type_offset
    """
    #  size_t QDnsLookupPrivate::_qt_property_type_offset()
    return Rituals.call(
        'ritual_ZN17QDnsLookupPrivate24_qt_property_type_offsetEv',
    )

  @staticmethod
  def _qt_property_port_offset() -> int:
    """
    Calls Qt's 'size_t QDnsLookupPrivate::_qt_property_port_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html#_qt_property_port_offset
    """
    #  size_t QDnsLookupPrivate::_qt_property_port_offset()
    return Rituals.call(
        'ritual_ZN17QDnsLookupPrivate24_qt_property_port_offsetEv',
    )

  @staticmethod
  def _qt_property_protocol_offset() -> int:
    """
    Calls Qt's 'size_t QDnsLookupPrivate::_qt_property_protocol_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html
    """
    #  size_t QDnsLookupPrivate::_qt_property_protocol_offset()
    return Rituals.call(
        'ritual_ZN17QDnsLookupPrivate28_qt_property_protocol_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDnsLookupPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDnsLookupPrivate::QDnsLookupPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html#QDnsLookupPrivate
    """
    #  QDnsLookupPrivate::QDnsLookupPrivate()
    self._noteCreation(QDnsLookupPrivate, lambda: Rituals.call(
        'ritual_ZN17QDnsLookupPrivateC1Ev',
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

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QDnsLookupPrivate::nameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookupprivate.html#nameChanged
    """
    #  void QDnsLookupPrivate::nameChanged()
    self.uglySide.call('ritual_ZN17QDnsLookupPrivate11nameChangedEv')

  def nameserverChanged(self) -> None:
    """
    Calls Qt's 'void QDnsLookupPrivate::nameserverChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html#nameserverChanged
    """
    #  void QDnsLookupPrivate::nameserverChanged()
    self.uglySide.call('ritual_ZN17QDnsLookupPrivate17nameserverChangedEv')

  def typeChanged(self) -> None:
    """
    Calls Qt's 'void QDnsLookupPrivate::typeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookupprivate.html#typeChanged
    """
    #  void QDnsLookupPrivate::typeChanged()
    self.uglySide.call('ritual_ZN17QDnsLookupPrivate11typeChangedEv')

  def nameserverPortChanged(self) -> None:
    """
    Calls Qt's 'void QDnsLookupPrivate::nameserverPortChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html#nameserverPortChanged
    """
    #  void QDnsLookupPrivate::nameserverPortChanged()
    self.uglySide.call(
        'ritual_ZN17QDnsLookupPrivate21nameserverPortChangedEv',
    )

  def nameserverProtocolChanged(self) -> None:
    """
    Calls Qt's 'void QDnsLookupPrivate::nameserverProtocolChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdnslookupprivate.html#nameserverProtocolChanged
    """
    #  void QDnsLookupPrivate::nameserverProtocolChanged()
    self.uglySide.call(
        'ritual_ZN17QDnsLookupPrivate25nameserverProtocolChangedEv',
    )

  def q_func(self) -> Optional[QDnsLookup]:
    """
    Calls Qt's 'QDnsLookup *QDnsLookupPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdnslookupprivate.html#q_func

    Returns
    -------

    Optional[QDnsLookup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDnsLookup *QDnsLookupPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QDnsLookupPrivate6q_funcEv')
    from . import QDnsLookup
    return QDnsLookup._cuteAt(address)
