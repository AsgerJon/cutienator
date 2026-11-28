"""
QWebEngineRegisterProtocolHandlerRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebengineregisterprotocolhandlerrequest.h, Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl


class QWebEngineRegisterProtocolHandlerRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineRegisterProtocolHandlerRequest: a plain
  Python object standing in front of one C++
  QWebEngineRegisterProtocolHandlerRequest.

  C++ hands a QWebEngineRegisterProtocolHandlerRequest around as a copy, so
  every C++ QWebEngineRegisterProtocolHandlerRequest behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEngineRegisterProtocolHandlerRequest that has a
  ritual and that Python can call so far, 6 names in all: 'accept', 'reject',
  'origin', 'scheme', '__eq__', '__ne__'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineRegisterProtocolHandlerRequest::
    QWebEngineRegisterProtocolHandlerRequest(
    QSharedPointer<QtWebEngineCore::RegisterProtocolHandlerRequestController>
    a0)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEngineRegisterProtocolHandlerRequest::
    ~QWebEngineRegisterProtocolHandlerRequest()': the destructor: Python
    removes its C++ QWebEngineRegisterProtocolHandlerRequest by it, and has
    no other use for it.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineRegisterProtocolHandlerRequest is created at the first
    use, not by 'QWebEngineRegisterProtocolHandlerRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineRegisterProtocolHandlerRequest back gives a
    copy the ritual made for Python, in a new cute
    QWebEngineRegisterProtocolHandlerRequest.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineRegisterProtocolHandlerRequest'

  #  Qt's '~QWebEngineRegisterProtocolHandlerRequest()'. Naming it makes this
  #  a value class: Python owns every C++
  #  QWebEngineRegisterProtocolHandlerRequest behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN40QWebEngineRegisterProtocolHandlerRequestD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def origin(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineRegisterProtocolHandlerRequest::origin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineRegisterProtocolHandlerRequest::origin() const
    address = self.uglySide.call(
        'ritual_ZNK40QWebEngineRegisterProtocolHandlerRequest6originEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def scheme(self) -> str:
    """
    Calls Qt's 'QString QWebEngineRegisterProtocolHandlerRequest::scheme()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebEngineRegisterProtocolHandlerRequest::scheme() const
    return self.uglySide.call(
        'ritual_ZNK40QWebEngineRegisterProtocolHandlerRequest6schemeEv',
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
  def __eq__(self, that: QWebEngineRegisterProtocolHandlerRequest) -> bool:
    """
    Calls Qt's 'bool
    QWebEngineRegisterProtocolHandlerRequest::operator==(const
    QWebEngineRegisterProtocolHandlerRequest &that) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html

    Parameters
    ----------

    that : QWebEngineRegisterProtocolHandlerRequest
      Passed on as a value: Qt reads the C++
      QWebEngineRegisterProtocolHandlerRequest, which stays Python's own.
    """
    #  bool QWebEngineRegisterProtocolHandlerRequest::operator==(const
    #      QWebEngineRegisterProtocolHandlerRequest &that) const
    return self.uglySide.call(
        'ritual_ZNK40QWebEngineRegisterProtocolHandlerRequesteqERKS_',
        self._valueOf(that),
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
  def __ne__(self, that: QWebEngineRegisterProtocolHandlerRequest) -> bool:
    """
    Calls Qt's 'bool
    QWebEngineRegisterProtocolHandlerRequest::operator!=(const
    QWebEngineRegisterProtocolHandlerRequest &that) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html

    Parameters
    ----------

    that : QWebEngineRegisterProtocolHandlerRequest
      Passed on as a value: Qt reads the C++
      QWebEngineRegisterProtocolHandlerRequest, which stays Python's own.
    """
    #  bool QWebEngineRegisterProtocolHandlerRequest::operator!=(const
    #      QWebEngineRegisterProtocolHandlerRequest &that) const
    return self.uglySide.call(
        'ritual_ZNK40QWebEngineRegisterProtocolHandlerRequestneERKS_',
        self._valueOf(that),
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
    'QWebEngineRegisterProtocolHandlerRequest::
    QWebEngineRegisterProtocolHandlerRequest()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html
    """
    #  QWebEngineRegisterProtocolHandlerRequest::
    #      QWebEngineRegisterProtocolHandlerRequest()
    self._noteCreation(
        QWebEngineRegisterProtocolHandlerRequest, lambda: Rituals.call(
            'ritual_ZN40QWebEngineRegisterProtocolHandlerRequestC1Ev',
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
    Calls Qt's 'void QWebEngineRegisterProtocolHandlerRequest::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html
    """
    #  void QWebEngineRegisterProtocolHandlerRequest::accept()
    self.uglySide.call(
        'ritual_ZN40QWebEngineRegisterProtocolHandlerRequest6acceptEv',
    )

  def reject(self) -> None:
    """
    Calls Qt's 'void QWebEngineRegisterProtocolHandlerRequest::reject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebengineregisterprotocolhandlerrequest.html
    """
    #  void QWebEngineRegisterProtocolHandlerRequest::reject()
    self.uglySide.call(
        'ritual_ZN40QWebEngineRegisterProtocolHandlerRequest6rejectEv',
    )
