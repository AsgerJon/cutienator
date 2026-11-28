"""
QtTaskTree::QTaskInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTaskInterface(QObject):
  """
  The cute side of Qt's QtTaskTree::QTaskInterface: a plain Python object
  standing in front of one C++ QtTaskTree::QTaskInterface.

  It is built on the cute 'QObject', as Qt's QtTaskTree::QTaskInterface is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QTaskInterface that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'reportDone', 'done', 'event'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtTaskTree::QTaskInterface::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QtTaskTree::QTaskInterface::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtTaskTree::QTaskInterface is created at the first use, not by
    'QtTaskTree::QTaskInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QTaskInterface.
  - Qt tells when it has removed the C++ QtTaskTree::QTaskInterface. Every
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
    Calls Qt's 'QString QtTaskTree::QTaskInterface::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qtaskinterface.html#tr

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
    #  QString QtTaskTree::QTaskInterface::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10QtTaskTree14QTaskInterface2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QTaskInterface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtTaskTree::QTaskInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtaskinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtTaskTree::QTaskInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree14QTaskInterface10metaObjectEv',
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
    'QtTaskTree::QTaskInterface::QTaskInterface()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtaskinterface.html#QTaskInterface
    """
    #  QtTaskTree::QTaskInterface::QTaskInterface()
    self._noteCreation(QTaskInterface, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree14QTaskInterfaceC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QtTaskTree::QTaskInterface::QTaskInterface(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtaskinterface.html#QTaskInterface

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtTaskTree::QTaskInterface::QTaskInterface(QObject *parent)
    self._noteCreation(QTaskInterface, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree14QTaskInterfaceC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QtTaskTree.DoneResult)
  def reportDone(self, result: QtTaskTree.DoneResult) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskInterface::reportDone(DoneResult
    result)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtaskinterface.html#reportDone

    Parameters
    ----------

    result : QtTaskTree.DoneResult
      Passed on as its number.
    """
    #  void QtTaskTree::QTaskInterface::reportDone(DoneResult result)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree14QTaskInterface10reportDoneENS_10DoneResultE',
        result.value,
    )

  @overload(QtTaskTree.DoneResult)
  def done(self, result: QtTaskTree.DoneResult) -> None:
    """
    Calls Qt's 'void QtTaskTree::QTaskInterface::done(QtTaskTree::DoneResult
    result, QPrivateSignal a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtaskinterface.html#done

    Parameters
    ----------

    result : QtTaskTree.DoneResult
      Passed on as its number.
    """
    #  void QtTaskTree::QTaskInterface::done(QtTaskTree::DoneResult result,
    #      QPrivateSignal a1)
    self.uglySide.call(
        'ritual_ZN10QtTaskTree14QTaskInterface4doneENS_10DoneResultENS0_14Q'
        'PrivateSignalE',
        result.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QTaskInterface::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qtaskinterface.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtTaskTree::QTaskInterface::event(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN10QtTaskTree14QTaskInterface5eventEP6QEvent',
        self._addressOf(event),
    )
