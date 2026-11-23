"""
QObjectCleanupHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qobjectcleanuphandler.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectCleanupHandler(QObject):
  """
  The cute side of Qt's QObjectCleanupHandler: a plain Python object standing
  in front of one C++ QObjectCleanupHandler.

  It is built on the cute 'QObject', as Qt's QObjectCleanupHandler is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QObjectCleanupHandler that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'add',
  'remove', 'isEmpty', 'clear', 'objectDestroyed'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QObjectCleanupHandler::~QObjectCleanupHandler()': the destructor:
    Python never removes a C++ QObjectCleanupHandler.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QObjectCleanupHandler is created at the first use, not by
    'QObjectCleanupHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QObjectCleanupHandler.
  - Qt tells when it has removed the C++ QObjectCleanupHandler. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QObjectCleanupHandler::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectcleanuphandler.html#tr

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
    #  QString QObjectCleanupHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QObjectCleanupHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QObjectCleanupHandler'

  #  A C++ QObjectCleanupHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QObjectCleanupHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QObjectCleanupHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectcleanuphandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QObjectCleanupHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QObjectCleanupHandler10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QObjectCleanupHandler::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectcleanuphandler.html#isEmpty
    """
    #  bool QObjectCleanupHandler::isEmpty() const
    return self.uglySide.call('ritual_ZNK21QObjectCleanupHandler7isEmptyEv')

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
    'QObjectCleanupHandler::QObjectCleanupHandler()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectcleanuphandler.html#QObjectCleanupHandler
    """
    #  QObjectCleanupHandler::QObjectCleanupHandler()
    self._noteCreation(QObjectCleanupHandler, lambda: Rituals.call(
        'ritual_ZN21QObjectCleanupHandlerC1Ev',
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
  def add(self, object: Optional[QObject]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QObjectCleanupHandler::add(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectcleanuphandler.html#add

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QObjectCleanupHandler::add(QObject *object)
    address = self.uglySide.call(
        'ritual_ZN21QObjectCleanupHandler3addEP7QObject',
        self._addressOf(object, 'QObject'),
    )
    return QObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def remove(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectCleanupHandler::remove(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectcleanuphandler.html#remove

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectCleanupHandler::remove(QObject *object)
    self.uglySide.call(
        'ritual_ZN21QObjectCleanupHandler6removeEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QObjectCleanupHandler::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectcleanuphandler.html#clear
    """
    #  void QObjectCleanupHandler::clear()
    self.uglySide.call('ritual_ZN21QObjectCleanupHandler5clearEv')

  @overload(QObject)
  @overload(NoneType)
  def objectDestroyed(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectCleanupHandler::objectDestroyed(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectcleanuphandler.html#objectDestroyed

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectCleanupHandler::objectDestroyed(QObject *a0)
    self.uglySide.call(
        'ritual_ZN21QObjectCleanupHandler15objectDestroyedEP7QObject',
        self._addressOf(a0, 'QObject'),
    )
