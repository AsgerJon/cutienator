"""
QFileOpenEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QFileOpenEvent(QEvent):
  """
  The cute side of Qt's QFileOpenEvent: a plain Python object standing in
  front of one C++ QFileOpenEvent.

  It is built on the cute 'QEvent', as Qt's QFileOpenEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileOpenEvent that has a ritual and that Python can
  call so far, 3 names in all: 'clone', 'file', 'url'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileOpenEvent::~QFileOpenEvent()': the destructor: Python never
    removes a C++ QFileOpenEvent.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 protected; 2 forbidden; 1 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QFileOpenEvent is created at the first use, not by
    'QFileOpenEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileOpenEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileOpenEvent'

  #  A C++ QFileOpenEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileOpenEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QFileOpenEvent]:
    """
    Calls Qt's 'QFileOpenEvent *QFileOpenEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileopenevent.html#clone

    Returns
    -------

    Optional[QFileOpenEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileOpenEvent *QFileOpenEvent::clone() const
    ritual = 'ritual_ZNK14QFileOpenEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QFileOpenEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QFileOpenEvent._cuteAt(address)

  def file(self) -> str:
    """
    Calls Qt's 'QString QFileOpenEvent::file() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileopenevent.html#file

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileOpenEvent::file() const
    return self.uglySide.call('ritual_ZNK14QFileOpenEvent4fileEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QFileOpenEvent::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileopenevent.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QFileOpenEvent::url() const
    address = self.uglySide.call('ritual_ZNK14QFileOpenEvent3urlEv')
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

  @overload(str)
  def __init__(self, file: str) -> None:
    """
    Notes what was given, for Qt's 'QFileOpenEvent::QFileOpenEvent(const
    QString &file)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfileopenevent.html#QFileOpenEvent

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QFileOpenEvent::QFileOpenEvent(const QString &file)
    self._noteCreation(QFileOpenEvent, lambda: Rituals.call(
        'ritual_ZN14QFileOpenEventC1ERK7QString', file,
    ))

  @overload(QUrl)
  def __init__(self, url: QUrl) -> None:
    """
    Notes what was given, for Qt's 'QFileOpenEvent::QFileOpenEvent(const QUrl
    &url)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfileopenevent.html#QFileOpenEvent

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QFileOpenEvent::QFileOpenEvent(const QUrl &url)
    self._noteCreation(QFileOpenEvent, lambda: Rituals.call(
        'ritual_ZN14QFileOpenEventC1ERK4QUrl', self._valueOf(url),
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
