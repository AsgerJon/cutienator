"""
QWebEngineFullScreenRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginefullscreenrequest.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl


class QWebEngineFullScreenRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEngineFullScreenRequest: a plain Python object
  standing in front of one C++ QWebEngineFullScreenRequest.

  C++ hands a QWebEngineFullScreenRequest around as a copy, so every C++
  QWebEngineFullScreenRequest behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QWebEngineFullScreenRequest that has a ritual and
  that Python can call so far, 4 names in all: 'reject', 'accept',
  'toggleOn', 'origin'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEngineFullScreenRequest
    &QWebEngineFullScreenRequest::operator=(const QWebEngineFullScreenRequest
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineFullScreenRequest::QWebEngineFullScreenRequest(
    QWebEngineFullScreenRequest &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QWebEngineFullScreenRequest
    &QWebEngineFullScreenRequest::operator=(QWebEngineFullScreenRequest
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QWebEngineFullScreenRequest::~QWebEngineFullScreenRequest()': the
    destructor: Python removes its C++ QWebEngineFullScreenRequest by it, and
    has no other use for it.
  - Qt's 'QWebEngineFullScreenRequest::QWebEngineFullScreenRequest(const QUrl
    &origin, bool toggleOn, const std::function<void (bool)>
    &setFullScreenCallback)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineFullScreenRequest is created at the first use, not by
    'QWebEngineFullScreenRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEngineFullScreenRequest back gives a copy the
    ritual made for Python, in a new cute QWebEngineFullScreenRequest.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineFullScreenRequest'

  #  Qt's '~QWebEngineFullScreenRequest()'. Naming it makes this a value
  #  class: Python owns every C++ QWebEngineFullScreenRequest behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QWebEngineFullScreenRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toggleOn(self) -> bool:
    """
    Calls Qt's 'bool QWebEngineFullScreenRequest::toggleOn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefullscreenrequest.html#toggleOn
    """
    #  bool QWebEngineFullScreenRequest::toggleOn() const
    return self.uglySide.call(
        'ritual_ZNK27QWebEngineFullScreenRequest8toggleOnEv',
    )

  def origin(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEngineFullScreenRequest::origin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefullscreenrequest.html#origin

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEngineFullScreenRequest::origin() const
    address = self.uglySide.call(
        'ritual_ZNK27QWebEngineFullScreenRequest6originEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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
    'QWebEngineFullScreenRequest::QWebEngineFullScreenRequest()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefullscreenrequest.html
    """
    #  QWebEngineFullScreenRequest::QWebEngineFullScreenRequest()
    self._noteCreation(QWebEngineFullScreenRequest, lambda: Rituals.call(
        'ritual_ZN27QWebEngineFullScreenRequestC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEngineFullScreenRequest) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineFullScreenRequest::QWebEngineFullScreenRequest(const
    QWebEngineFullScreenRequest &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefullscreenrequest.html

    Parameters
    ----------

    other : QWebEngineFullScreenRequest
      Passed on as a value: Qt reads the C++ QWebEngineFullScreenRequest,
      which stays Python's own.
    """
    #  QWebEngineFullScreenRequest::QWebEngineFullScreenRequest(const
    #      QWebEngineFullScreenRequest &other)
    self._noteCreation(QWebEngineFullScreenRequest, lambda: Rituals.call(
        'ritual_ZN27QWebEngineFullScreenRequestC1ERKS_',
        self._valueOf(other),
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

  def reject(self) -> None:
    """
    Calls Qt's 'void QWebEngineFullScreenRequest::reject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefullscreenrequest.html#reject
    """
    #  void QWebEngineFullScreenRequest::reject()
    self.uglySide.call('ritual_ZN27QWebEngineFullScreenRequest6rejectEv')

  def accept(self) -> None:
    """
    Calls Qt's 'void QWebEngineFullScreenRequest::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginefullscreenrequest.html#accept
    """
    #  void QWebEngineFullScreenRequest::accept()
    self.uglySide.call('ritual_ZN27QWebEngineFullScreenRequest6acceptEv')
