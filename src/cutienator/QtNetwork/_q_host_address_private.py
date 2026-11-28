"""
QHostAddressPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhostaddress_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QHostAddressPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QIPv6Address
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIPv6Address = WAIT['QIPv6Address']


class QHostAddressPrivate(QSharedData):
  """
  The cute side of Qt's QHostAddressPrivate: a plain Python object standing
  in front of one C++ QHostAddressPrivate.

  It is built on the cute 'QSharedData', as Qt's QHostAddressPrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QHostAddressPrivate around as a copy, so every C++
  QHostAddressPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHostAddressPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'setAddress', 'parse', 'clear'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QHostAddressPrivate::setAddress(const quint8 *a_)': names
    'quint8', which has no cute class yet.
  - Qt's 'AddressClassification QHostAddressPrivate::classify() const': gives
    the enum 'AddressClassification', whose class cannot be named here.
  - Qt's 'AddressClassification QHostAddressPrivate::classify(const
    QHostAddress &address)': gives the enum 'AddressClassification', whose
    class cannot be named here.
  - Qt's 'QHostAddressPrivate::~QHostAddressPrivate()': the destructor:
    Python removes its C++ QHostAddressPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QHostAddressPrivate is created at the first use, not by
    'QHostAddressPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHostAddressPrivate back gives a copy the ritual made
    for Python, in a new cute QHostAddressPrivate.
  - Each name of Qt's QHostAddressPrivate that has no cute function yet,
    'classify', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHostAddressPrivate'

  #  Qt's '~QHostAddressPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QHostAddressPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QHostAddressPrivateD1Ev'

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

  @overload()
  @overload(int)
  def setAddress(self, a_: int = 0) -> None:
    """
    Calls Qt's 'void QHostAddressPrivate::setAddress(quint32 a_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostaddressprivate.html#setAddress

    Parameters
    ----------

    a_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QHostAddressPrivate::setAddress(quint32 a_)
    self.uglySide.call('ritual_ZN19QHostAddressPrivate10setAddressEj', a_)

  @overload(QIPv6Address)
  def setAddress(self, a_: QIPv6Address) -> None:
    """
    Calls Qt's 'void QHostAddressPrivate::setAddress(const Q_IPV6ADDR &a_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhostaddressprivate.html#setAddress

    Parameters
    ----------

    a_ : QIPv6Address
      Passed on as a value: Qt reads the C++ QIPv6Address, which stays
      Python's own.
    """
    #  void QHostAddressPrivate::setAddress(const Q_IPV6ADDR &a_)
    self.uglySide.call(
        'ritual_ZN19QHostAddressPrivate10setAddressERK12QIPv6Address',
        self._valueOf(a_),
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

  @overload(str)
  def parse(self, ipString: str) -> bool:
    """
    Calls Qt's 'bool QHostAddressPrivate::parse(const QString &ipString)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddressprivate.html#parse

    Parameters
    ----------

    ipString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QHostAddressPrivate::parse(const QString &ipString)
    return self.uglySide.call(
        'ritual_ZN19QHostAddressPrivate5parseERK7QString', ipString,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QHostAddressPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostaddressprivate.html#clear
    """
    #  void QHostAddressPrivate::clear()
    self.uglySide.call('ritual_ZN19QHostAddressPrivate5clearEv')

  @staticmethod
  def classify(*__, **_) -> Never:
    """
    - Qt's 'AddressClassification QHostAddressPrivate::classify() const':
      gives the enum 'AddressClassification', whose class cannot be named
      here.
    - Qt's 'AddressClassification QHostAddressPrivate::classify(const
      QHostAddress &address)': gives the enum 'AddressClassification', whose
      class cannot be named here.
    """
    raise NotImplementedError(
        "'QHostAddressPrivate.classify' has no cute function yet. Qt's "
        "'AddressClassification QHostAddressPrivate::classify() const': "
        "gives the enum 'AddressClassification', whose class cannot be "
        "named here. Qt's 'AddressClassification "
        "QHostAddressPrivate::classify(const QHostAddress &address)': gives "
        "the enum 'AddressClassification', whose class cannot be named here."
    )
