"""
QNetworkAccessFileBackendFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessfilebackend_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QNetworkAccessFileBackendFactory to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QStringList
from . import QNetworkAccessBackendFactory, QNetworkAccessManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QNetworkAccessBackend, QNetworkRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QNetworkRequest = WAIT['QNetworkRequest']


class QNetworkAccessFileBackendFactory(QNetworkAccessBackendFactory):
  """
  The cute side of Qt's QNetworkAccessFileBackendFactory: a plain Python
  object standing in front of one C++ QNetworkAccessFileBackendFactory.

  It is built on the cute 'QNetworkAccessBackendFactory', as Qt's
  QNetworkAccessFileBackendFactory is built on Qt's
  QNetworkAccessBackendFactory, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkAccessFileBackendFactory that has a ritual
  and that Python can call so far, 2 names in all: 'supportedSchemes',
  'create'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What to expect
  --------------

  - The C++ QNetworkAccessFileBackendFactory is created at the first use, not
    by 'QNetworkAccessFileBackendFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkAccessFileBackendFactory.
  - Qt tells when it has removed the C++ QNetworkAccessFileBackendFactory.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkAccessFileBackendFactory'

  #  A C++ QNetworkAccessFileBackendFactory Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkAccessFileBackendFactory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def supportedSchemes(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QNetworkAccessFileBackendFactory::supportedSchemes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessfilebackendfactory.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QNetworkAccessFileBackendFactory::supportedSchemes() const
    address = self.uglySide.call(
        'ritual_ZNK32QNetworkAccessFileBackendFactory16supportedSchemesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QNetworkAccessManager.Operation, QNetworkRequest)
  def create(
      self,
      op: QNetworkAccessManager.Operation,
      request: QNetworkRequest,
  ) -> Optional[QNetworkAccessBackend]:
    """
    Calls Qt's 'QNetworkAccessBackend
    *QNetworkAccessFileBackendFactory::create(QNetworkAccessManager::
    Operation op, const QNetworkRequest &request) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkaccessfilebackendfactory.html#create

    Parameters
    ----------

    op : QNetworkAccessManager.Operation
      Passed on as its number.

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QNetworkAccessBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkAccessBackend
    #      *QNetworkAccessFileBackendFactory::create(QNetworkAccessManager::
    #      Operation op, const QNetworkRequest &request) const
    address = self.uglySide.call(
        'ritual_ZNK32QNetworkAccessFileBackendFactory6createEN21QNetworkAcc'
        'essManager9OperationERK15QNetworkRequest',
        op.value, self._valueOf(request),
    )
    from . import QNetworkAccessBackend
    return QNetworkAccessBackend._cuteAt(address)

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
