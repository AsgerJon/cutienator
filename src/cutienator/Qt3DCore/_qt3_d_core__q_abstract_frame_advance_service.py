"""
Qt3DCore::QAbstractFrameAdvanceService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qabstractframeadvanceservice_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DCore::QAbstractFrameAdvanceService to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractFrameAdvanceService(Qt3DCore.QAbstractServiceProvider):
  """
  The cute side of Qt's Qt3DCore::QAbstractFrameAdvanceService: a plain
  Python object standing in front of one C++
  Qt3DCore::QAbstractFrameAdvanceService.

  It is built on the cute 'Qt3DCore::QAbstractServiceProvider', as Qt's
  Qt3DCore::QAbstractFrameAdvanceService is built on Qt's
  Qt3DCore::QAbstractServiceProvider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAbstractFrameAdvanceService that has a
  ritual and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'waitForNextFrame', 'start', 'stop'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QAbstractFrameAdvanceService::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::QAbstractFrameAdvanceService::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DCore::QAbstractFrameAdvanceService::QAbstractFrameAdvanceService(
    QAbstractFrameAdvanceServicePrivate &dd)': takes a type Python has no way
    to hand over yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QAbstractFrameAdvanceService is created at the first
    use, not by 'Qt3DCore::QAbstractFrameAdvanceService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAbstractFrameAdvanceService.
  - Qt tells when it has removed the C++
    Qt3DCore::QAbstractFrameAdvanceService. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString Qt3DCore::QAbstractFrameAdvanceService::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractframeadvanceservice.html#tr

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
    #  QString Qt3DCore::QAbstractFrameAdvanceService::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAbstractFrameAdvanceService'

  #  A C++ Qt3DCore::QAbstractFrameAdvanceService Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAbstractFrameAdvanceService'

  #  The functions Qt calls itself that
  #  Qt3DCore::QAbstractFrameAdvanceService is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'waitForNextFrame': (
          ('_ZN8Qt3DCore28QAbstractFrameAdvanceService16waitForNextFrameEv',
           ('long long', 'number', ''),
           ()),
      ),
      'start': (
          ('_ZN8Qt3DCore28QAbstractFrameAdvanceService5startEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stop': (
          ('_ZN8Qt3DCore28QAbstractFrameAdvanceService4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

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
    *Qt3DCore::QAbstractFrameAdvanceService::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractframeadvanceservice.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DCore::QAbstractFrameAdvanceService::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore28QAbstractFrameAdvanceService10metaObjectEv',
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
  @overload(str)
  def __init__(self, description: str = '') -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QAbstractFrameAdvanceService::QAbstractFrameAdvanceService(
    const QString &description)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractframeadvanceservice.html

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  Qt3DCore::QAbstractFrameAdvanceService::
    #      QAbstractFrameAdvanceService(const QString &description)
    self._noteCreation(QAbstractFrameAdvanceService, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore28QAbstractFrameAdvanceServiceC1ERK7QString',
        description,
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

  def waitForNextFrame(self) -> int:
    """
    Calls Qt's 'qint64
    Qt3DCore::QAbstractFrameAdvanceService::waitForNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractframeadvanceservice.html
    """
    #  qint64 Qt3DCore::QAbstractFrameAdvanceService::waitForNextFrame()
    return self.uglySide.call(
        'ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService16waitForNextFrame'
        'Ev',
    )

  def start(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractFrameAdvanceService::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractframeadvanceservice.html#start
    """
    #  void Qt3DCore::QAbstractFrameAdvanceService::start()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService5startEv',
    )

  def stop(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractFrameAdvanceService::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractframeadvanceservice.html#stop
    """
    #  void Qt3DCore::QAbstractFrameAdvanceService::stop()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService4stopEv',
    )
