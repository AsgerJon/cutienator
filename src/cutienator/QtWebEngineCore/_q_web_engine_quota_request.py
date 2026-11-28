"""
QWebEngineQuotaRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginequotarequest.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl


class QWebEngineQuotaRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineQuotaRequest: a plain Python object
  standing in front of one C++ QWebEngineQuotaRequest.

  C++ hands a QWebEngineQuotaRequest around as a copy, so every C++
  QWebEngineQuotaRequest behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineQuotaRequest that has a ritual and that
  Python can call so far, 6 names in all: 'accept', 'reject', 'origin',
  'requestedSize', '__eq__', '__ne__'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineQuotaRequest::~QWebEngineQuotaRequest()': the destructor:
    Python removes its C++ QWebEngineQuotaRequest by it, and has no other use
    for it.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineQuotaRequest is created at the first use, not by
    'QWebEngineQuotaRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineQuotaRequest back gives a copy the ritual
    made for Python, in a new cute QWebEngineQuotaRequest.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineQuotaRequest'

  #  Qt's '~QWebEngineQuotaRequest()'. Naming it makes this a value class:
  #  Python owns every C++ QWebEngineQuotaRequest behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QWebEngineQuotaRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def origin(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineQuotaRequest::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginequotarequest.html#origin

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineQuotaRequest::origin() const
    address = self.uglySide.call(
        'ritual_ZNK22QWebEngineQuotaRequest6originEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def requestedSize(self) -> int:
    """
    Calls Qt's 'qint64 QWebEngineQuotaRequest::requestedSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginequotarequest.html#requestedSize
    """
    #  qint64 QWebEngineQuotaRequest::requestedSize() const
    return self.uglySide.call(
        'ritual_ZNK22QWebEngineQuotaRequest13requestedSizeEv',
    )

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
  def __eq__(self, a0: QWebEngineQuotaRequest) -> bool:
    """
    Calls Qt's 'bool QWebEngineQuotaRequest::operator==(const
    QWebEngineQuotaRequest &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginequotarequest.html#operator==

    Parameters
    ----------

    a0 : QWebEngineQuotaRequest
      Passed on as a value: Qt reads the C++ QWebEngineQuotaRequest, which
      stays Python's own.
    """
    #  bool QWebEngineQuotaRequest::operator==(const QWebEngineQuotaRequest
    #      &a0) const
    return self.uglySide.call(
        'ritual_ZNK22QWebEngineQuotaRequesteqERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, a0: QWebEngineQuotaRequest) -> bool:
    """
    Calls Qt's 'bool QWebEngineQuotaRequest::operator!=(const
    QWebEngineQuotaRequest &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginequotarequest.html#operator!=

    Parameters
    ----------

    a0 : QWebEngineQuotaRequest
      Passed on as a value: Qt reads the C++ QWebEngineQuotaRequest, which
      stays Python's own.
    """
    #  bool QWebEngineQuotaRequest::operator!=(const QWebEngineQuotaRequest
    #      &a0) const
    return self.uglySide.call(
        'ritual_ZNK22QWebEngineQuotaRequestneERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineQuotaRequest::QWebEngineQuotaRequest()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginequotarequest.html#QWebEngineQuotaRequest
    """
    #  QWebEngineQuotaRequest::QWebEngineQuotaRequest()
    self._noteCreation(QWebEngineQuotaRequest, lambda: Rituals.call(
        'ritual_ZN22QWebEngineQuotaRequestC1Ev',
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

  def accept(self) -> None:
    """
    Calls Qt's 'void QWebEngineQuotaRequest::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginequotarequest.html#accept
    """
    #  void QWebEngineQuotaRequest::accept()
    self.uglySide.call('ritual_ZN22QWebEngineQuotaRequest6acceptEv')

  def reject(self) -> None:
    """
    Calls Qt's 'void QWebEngineQuotaRequest::reject()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginequotarequest.html#reject
    """
    #  void QWebEngineQuotaRequest::reject()
    self.uglySide.call('ritual_ZN22QWebEngineQuotaRequest6rejectEv')
