"""
QRemoteObjectRegistryHostPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectRegistryHostPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QHash
from . import QRemoteObjectHostBasePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRemoteObjectRegistryHost, QRemoteObjectSourceLocationInfo


class QRemoteObjectRegistryHostPrivate(QRemoteObjectHostBasePrivate):
  """
  The cute side of Qt's QRemoteObjectRegistryHostPrivate: a plain Python
  object standing in front of one C++ QRemoteObjectRegistryHostPrivate.

  It is built on the cute 'QRemoteObjectHostBasePrivate', as Qt's
  QRemoteObjectRegistryHostPrivate is built on Qt's
  QRemoteObjectHostBasePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectRegistryHostPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'remoteObjectAddresses',
  'q_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QRemoteObjectRegistryHostPrivate::~QRemoteObjectRegistryHostPrivate()':
    the destructor: Python never removes a C++
    QRemoteObjectRegistryHostPrivate.
  - Qt's 'const QRemoteObjectRegistryHost
    *QRemoteObjectRegistryHostPrivate::q_func() const': takes in Python what
    'QRemoteObjectRegistryHost *QRemoteObjectRegistryHostPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 1 leans on 'QRegistrySource; 1 leans on
  'QRemoteObjectSourceBase.

  What to expect
  --------------

  - The C++ QRemoteObjectRegistryHostPrivate is created at the first use, not
    by 'QRemoteObjectRegistryHostPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectRegistryHostPrivate.
  - Each name of Qt's QRemoteObjectRegistryHostPrivate that has no cute
    function yet, '__init__', 'setRegistryUrlRegistryHostImpl', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectRegistryHostPrivate'

  #  A C++ QRemoteObjectRegistryHostPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectRegistryHostPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def remoteObjectAddresses(
      self,
  ) -> QHash[str, QRemoteObjectSourceLocationInfo]:
    """
    Calls Qt's 'QRemoteObjectSourceLocations
    QRemoteObjectRegistryHostPrivate::remoteObjectAddresses() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistryhostprivate.html

    Returns
    -------

    QHash[str, QRemoteObjectSourceLocationInfo]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QRemoteObjectSourceLocations
    #      QRemoteObjectRegistryHostPrivate::remoteObjectAddresses() const
    address = self.uglySide.call(
        'ritual_ZNK32QRemoteObjectRegistryHostPrivate21remoteObjectAddresse'
        'sEv',
    )
    from . import QRemoteObjectSourceLocationInfo
    return QHash[str, QRemoteObjectSourceLocationInfo]._cuteOwning(address)

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
    Qt's
    'QRemoteObjectRegistryHostPrivate::QRemoteObjectRegistryHostPrivate()':
    leans on 'QRemoteObjectSourceBase::qobjectPropertyOffset', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectRegistryHostPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QRemoteObjectRegistryHostPrivate::QRemoteObjectRegistryHostPrivate"
        "()': leans on 'QRemoteObjectSourceBase::qobjectPropertyOffset', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def q_func(self) -> Optional[QRemoteObjectRegistryHost]:
    """
    Calls Qt's 'QRemoteObjectRegistryHost
    *QRemoteObjectRegistryHostPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectregistryhostprivate.html#q_func

    Returns
    -------

    Optional[QRemoteObjectRegistryHost]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRemoteObjectRegistryHost *QRemoteObjectRegistryHostPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN32QRemoteObjectRegistryHostPrivate6q_funcEv',
    )
    from . import QRemoteObjectRegistryHost
    return QRemoteObjectRegistryHost._cuteAt(address)

  @staticmethod
  def setRegistryUrlRegistryHostImpl(*__, **_) -> Never:
    """
    Qt's 'bool
    QRemoteObjectRegistryHostPrivate::setRegistryUrlRegistryHostImpl(const
    QUrl &registryUrl)': leans on 'QRegistrySource::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectRegistryHostPrivate.setRegistryUrlRegistryHostImpl' "
        "has no cute function yet. Qt's 'bool "
        "QRemoteObjectRegistryHostPrivate::setRegistryUrlRegistryHostImpl(co"
        "nst QUrl &registryUrl)': leans on "
        "'QRegistrySource::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
