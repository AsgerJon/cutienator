"""
QHttpNetworkRequestPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkrequest_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpNetworkRequestPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QHttpNetworkHeaderPrivate, QHttpNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QHttpNetworkRequestPrivate(QHttpNetworkHeaderPrivate):
  """
  The cute side of Qt's QHttpNetworkRequestPrivate: a plain Python object
  standing in front of one C++ QHttpNetworkRequestPrivate.

  It is built on the cute 'QHttpNetworkHeaderPrivate', as Qt's
  QHttpNetworkRequestPrivate is built on Qt's QHttpNetworkHeaderPrivate, and
  has everything that class has.

  C++ hands a QHttpNetworkRequestPrivate around as a copy, so every C++
  QHttpNetworkRequestPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QHttpNetworkRequestPrivate that has a ritual and
  that Python can call so far, 2 names in all: '__eq__', 'header'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpNetworkRequestPrivate::~QHttpNetworkRequestPrivate()': the
    destructor: Python removes its C++ QHttpNetworkRequestPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QHttpNetworkRequestPrivate is created at the first use, not by
    'QHttpNetworkRequestPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpNetworkRequestPrivate back gives a copy the
    ritual made for Python, in a new cute QHttpNetworkRequestPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QHttpNetworkRequest, bool)
  def header(request: QHttpNetworkRequest, throughProxy: bool) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpNetworkRequestPrivate::header(const
    QHttpNetworkRequest &request, bool throughProxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequestprivate.html#header

    Parameters
    ----------

    request : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.

    throughProxy : bool
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkRequestPrivate::header(const
    #      QHttpNetworkRequest &request, bool throughProxy)
    address = Rituals.call(
        'ritual_ZN26QHttpNetworkRequestPrivate6headerERK19QHttpNetworkReque'
        'stb',
        CuteMixin._valueOf(request), throughProxy,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkRequestPrivate'

  #  Qt's '~QHttpNetworkRequestPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QHttpNetworkRequestPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QHttpNetworkRequestPrivateD1Ev'

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

  @overload(THIS)
  def __eq__(self, other: QHttpNetworkRequestPrivate) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkRequestPrivate::operator==(const
    QHttpNetworkRequestPrivate &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequestprivate.html#operator==

    Parameters
    ----------

    other : QHttpNetworkRequestPrivate
      Passed on as a value: Qt reads the C++ QHttpNetworkRequestPrivate,
      which stays Python's own.
    """
    #  bool QHttpNetworkRequestPrivate::operator==(const
    #      QHttpNetworkRequestPrivate &other) const
    return self.uglySide.call(
        'ritual_ZNK26QHttpNetworkRequestPrivateeqERKS_',
        self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHttpNetworkRequest.Operation, QHttpNetworkRequest.Priority)
  @overload(
      QHttpNetworkRequest.Operation, QHttpNetworkRequest.Priority, QUrl,
  )
  def __init__(
      self,
      op: QHttpNetworkRequest.Operation,
      pri: QHttpNetworkRequest.Priority,
      newUrl: Optional[QUrl] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(
    QHttpNetworkRequest::Operation op, QHttpNetworkRequest::Priority pri,
    const QUrl &newUrl)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequestprivate.html

    Parameters
    ----------

    op : QHttpNetworkRequest.Operation
      Passed on as its number.

    pri : QHttpNetworkRequest.Priority
      Passed on as its number.

    newUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(
    #      QHttpNetworkRequest::Operation op, QHttpNetworkRequest::Priority
    #      pri, const QUrl &newUrl)
    if newUrl is None:
      from ..QtCore import QUrl
      newUrl = QUrl()
    self._noteCreation(QHttpNetworkRequestPrivate, lambda: Rituals.call(
        'ritual_ZN26QHttpNetworkRequestPrivateC1EN19QHttpNetworkRequest9Ope'
        'rationENS0_8PriorityERK4QUrl',
        op.value, pri.value, self._valueOf(newUrl),
    ))

  @overload(THIS)
  def __init__(self, other: QHttpNetworkRequestPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(const
    QHttpNetworkRequestPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkrequestprivate.html

    Parameters
    ----------

    other : QHttpNetworkRequestPrivate
      Passed on as a value: Qt reads the C++ QHttpNetworkRequestPrivate,
      which stays Python's own.
    """
    #  QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(const
    #      QHttpNetworkRequestPrivate &other)
    self._noteCreation(QHttpNetworkRequestPrivate, lambda: Rituals.call(
        'ritual_ZN26QHttpNetworkRequestPrivateC1ERKS_', self._valueOf(other),
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
