"""
QNetworkInterfacePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkinterface_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkInterfacePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QNetworkAddressEntry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkAddressEntry = WAIT['QNetworkAddressEntry']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkInterfacePrivate(QSharedData):
  """
  The cute side of Qt's QNetworkInterfacePrivate: a plain Python object
  standing in front of one C++ QNetworkInterfacePrivate.

  It is built on the cute 'QSharedData', as Qt's QNetworkInterfacePrivate is
  built on Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkInterfacePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'calculateDnsEligibility'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkInterfacePrivate::~QNetworkInterfacePrivate()': the
    destructor: Python never removes a C++ QNetworkInterfacePrivate.
  - Qt's 'QString QNetworkInterfacePrivate::makeHwAddress(int len, uchar
    *data)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QNetworkInterfacePrivate is created at the first use, not by
    'QNetworkInterfacePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkInterfacePrivate.
  - Each name of Qt's QNetworkInterfacePrivate that has no cute function yet,
    'makeHwAddress', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QNetworkAddressEntry, bool, bool)
  @overload(NoneType, bool, bool)
  def calculateDnsEligibility(
      entry: Optional[QNetworkAddressEntry],
      isTemporary: bool,
      isDeprecated: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkInterfacePrivate::calculateDnsEligibility(QNetworkAddressEntry
    *entry, bool isTemporary, bool isDeprecated)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterfaceprivate.html

    Parameters
    ----------

    entry : Optional[QNetworkAddressEntry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isTemporary : bool
      Passed on as it is.

    isDeprecated : bool
      Passed on as it is.
    """
    #  void QNetworkInterfacePrivate::calculateDnsEligibility(
    #      QNetworkAddressEntry *entry, bool isTemporary, bool isDeprecated)
    Rituals.call(
        'ritual_ZN24QNetworkInterfacePrivate23calculateDnsEligibilityEP20QN'
        'etworkAddressEntrybb',
        CuteMixin._addressOf(entry), isTemporary, isDeprecated,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkInterfacePrivate'

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
    Notes what was given, for Qt's
    'QNetworkInterfacePrivate::QNetworkInterfacePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkinterfaceprivate.html
    """
    #  QNetworkInterfacePrivate::QNetworkInterfacePrivate()
    self._noteCreation(QNetworkInterfacePrivate, lambda: Rituals.call(
        'ritual_ZN24QNetworkInterfacePrivateC1Ev',
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

  @staticmethod
  def makeHwAddress(*__, **_) -> Never:
    """
    Qt's 'QString QNetworkInterfacePrivate::makeHwAddress(int len, uchar
    *data)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QNetworkInterfacePrivate.makeHwAddress' has no cute function yet. "
        "Qt's 'QString QNetworkInterfacePrivate::makeHwAddress(int len, "
        "uchar *data)': takes a number to change where it is.")


#  Qt's 'QList<QNetworkInterfacePrivate *>': the list of
#  QNetworkInterfacePrivate, which 'QList[QNetworkInterfacePrivate]' gives.
#  It is made here, so that there is one as soon as there can be a
#  QNetworkInterfacePrivate.
QList.createKind(
    QNetworkInterfacePrivate, 'address',
    make='ritual_list_make_QNetworkInterfacePrivate_ptr',
    add='ritual_list_add_QNetworkInterfacePrivate_ptr',
    size='ritual_list_size_QNetworkInterfacePrivate_ptr',
    at='ritual_list_at_QNetworkInterfacePrivate_ptr',
    drop='ritual_list_drop_QNetworkInterfacePrivate_ptr',
)
