"""
QPlaceSearchRequestPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qplacesearchrequest_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPlaceSearchRequestPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPlaceSearchRequest
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceSearchRequest = WAIT['QPlaceSearchRequest']


class QPlaceSearchRequestPrivate(QSharedData):
  """
  The cute side of Qt's QPlaceSearchRequestPrivate: a plain Python object
  standing in front of one C++ QPlaceSearchRequestPrivate.

  It is built on the cute 'QSharedData', as Qt's QPlaceSearchRequestPrivate
  is built on Qt's QSharedData, and has everything that class has.

  C++ hands a QPlaceSearchRequestPrivate around as a copy, so every C++
  QPlaceSearchRequestPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QPlaceSearchRequestPrivate that has a ritual and
  that Python can call so far, 3 names in all: '__eq__', 'clear', 'get'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceSearchRequestPrivate
    *QPlaceSearchRequestPrivate::get(QPlaceSearchRequest &request)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QPlaceSearchRequestPrivate::~QPlaceSearchRequestPrivate()': the
    destructor: Python removes its C++ QPlaceSearchRequestPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QPlaceSearchRequestPrivate is created at the first use, not by
    'QPlaceSearchRequestPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceSearchRequestPrivate back gives a copy the
    ritual made for Python, in a new cute QPlaceSearchRequestPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPlaceSearchRequest)
  def get(
      request: QPlaceSearchRequest,
  ) -> Optional[QPlaceSearchRequestPrivate]:
    """
    Calls Qt's 'const QPlaceSearchRequestPrivate
    *QPlaceSearchRequestPrivate::get(const QPlaceSearchRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequestprivate.html#get

    Parameters
    ----------

    request : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QPlaceSearchRequestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlaceSearchRequestPrivate
    #      *QPlaceSearchRequestPrivate::get(const QPlaceSearchRequest
    #      &request)
    address = Rituals.call(
        'ritual_ZN26QPlaceSearchRequestPrivate3getERK19QPlaceSearchRequest',
        CuteMixin._valueOf(request),
    )
    return QPlaceSearchRequestPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceSearchRequestPrivate'

  #  Qt's '~QPlaceSearchRequestPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QPlaceSearchRequestPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QPlaceSearchRequestPrivateD1Ev'

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
  def __eq__(self, other: QPlaceSearchRequestPrivate) -> bool:
    """
    Calls Qt's 'bool QPlaceSearchRequestPrivate::operator==(const
    QPlaceSearchRequestPrivate &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequestprivate.html#operator==

    Parameters
    ----------

    other : QPlaceSearchRequestPrivate
      Passed on as a value: Qt reads the C++ QPlaceSearchRequestPrivate,
      which stays Python's own.
    """
    #  bool QPlaceSearchRequestPrivate::operator==(const
    #      QPlaceSearchRequestPrivate &other) const
    return self.uglySide.call(
        'ritual_ZNK26QPlaceSearchRequestPrivateeqERKS_',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequestPrivate::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequestprivate.html#clear
    """
    #  void QPlaceSearchRequestPrivate::clear()
    self.uglySide.call('ritual_ZN26QPlaceSearchRequestPrivate5clearEv')
