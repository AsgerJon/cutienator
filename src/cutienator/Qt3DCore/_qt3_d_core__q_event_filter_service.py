"""
Qt3DCore::QEventFilterService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qeventfilterservice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::QEventFilterService to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventFilterService(Qt3DCore.QAbstractServiceProvider):
  """
  The cute side of Qt's Qt3DCore::QEventFilterService: a plain Python object
  standing in front of one C++ Qt3DCore::QEventFilterService.

  It is built on the cute 'Qt3DCore::QAbstractServiceProvider', as Qt's
  Qt3DCore::QEventFilterService is built on Qt's
  Qt3DCore::QAbstractServiceProvider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QEventFilterService that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'initialize', 'shutdown', 'registerEventFilter', 'unregisterEventFilter'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QEventFilterService::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QEventFilterService::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QEventFilterService::~QEventFilterService()': the
    destructor: Python never removes a C++ Qt3DCore::QEventFilterService.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DCore::QEventFilterService is created at the first use, not by
    'Qt3DCore::QEventFilterService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QEventFilterService.
  - Qt tells when it has removed the C++ Qt3DCore::QEventFilterService. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QEventFilterService::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qeventfilterservice.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QEventFilterService::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore19QEventFilterService2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QEventFilterService'

  #  A C++ Qt3DCore::QEventFilterService Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QEventFilterService'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::QEventFilterService::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qeventfilterservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QEventFilterService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore19QEventFilterService10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    'Qt3DCore::QEventFilterService::QEventFilterService()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qeventfilterservice.html
    """
    #  Qt3DCore::QEventFilterService::QEventFilterService()
    self._noteCreation(QEventFilterService, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore19QEventFilterServiceC1Ev',
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

  @overload(QObject)
  @overload(NoneType)
  def initialize(self, eventSource: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QEventFilterService::initialize(QObject
    *eventSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qeventfilterservice.html#initialize

    Parameters
    ----------

    eventSource : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QEventFilterService::initialize(QObject *eventSource)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore19QEventFilterService10initializeEP7QObject',
        self._addressOf(eventSource, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def shutdown(self, eventSource: Optional[QObject]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QEventFilterService::shutdown(QObject
    *eventSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qeventfilterservice.html#shutdown

    Parameters
    ----------

    eventSource : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QEventFilterService::shutdown(QObject *eventSource)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore19QEventFilterService8shutdownEP7QObject',
        self._addressOf(eventSource, 'QObject'),
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def registerEventFilter(
      self,
      eventFilter: Optional[QObject],
      priority: int,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QEventFilterService::registerEventFilter(QObject *eventFilter,
    int priority)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qeventfilterservice.html

    Parameters
    ----------

    eventFilter : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    priority : int
      Passed on as it is.
    """
    #  void Qt3DCore::QEventFilterService::registerEventFilter(QObject
    #      *eventFilter, int priority)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore19QEventFilterService19registerEventFilterEP7QOb'
        'jecti',
        self._addressOf(eventFilter, 'QObject'), priority,
    )

  @overload(QObject)
  @overload(NoneType)
  def unregisterEventFilter(self, eventFilter: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QEventFilterService::unregisterEventFilter(QObject
    *eventFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qeventfilterservice.html

    Parameters
    ----------

    eventFilter : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QEventFilterService::unregisterEventFilter(QObject
    #      *eventFilter)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore19QEventFilterService21unregisterEventFilterEP7Q'
        'Object',
        self._addressOf(eventFilter, 'QObject'),
    )
