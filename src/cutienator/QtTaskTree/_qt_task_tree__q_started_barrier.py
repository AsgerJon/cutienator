"""
QtTaskTree::QStartedBarrier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qbarriertask.h, Qt 6.12.0. Changes made here are lost.
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


class QStartedBarrier(QtTaskTree.QBarrier):
  """
  The cute side of Qt's QtTaskTree::QStartedBarrier: a plain Python object
  standing in front of one C++ QtTaskTree::QStartedBarrier.

  It is built on the cute 'QtTaskTree::QBarrier', as Qt's
  QtTaskTree::QStartedBarrier is built on Qt's QtTaskTree::QBarrier, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QtTaskTree::QStartedBarrier that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject', 'tr', 'event'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtTaskTree::QStartedBarrier::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QtTaskTree::QStartedBarrier::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtTaskTree::QStartedBarrier::~QStartedBarrier()': the destructor:
    Python never removes a C++ QtTaskTree::QStartedBarrier.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QtTaskTree::QStartedBarrier is created at the first use, not by
    'QtTaskTree::QStartedBarrier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::QStartedBarrier.
  - Qt tells when it has removed the C++ QtTaskTree::QStartedBarrier. Every
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
    Calls Qt's 'QString QtTaskTree::QStartedBarrier::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-qstartedbarrier.html#tr

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
    #  QString QtTaskTree::QStartedBarrier::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10QtTaskTree15QStartedBarrier2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::QStartedBarrier'

  #  A C++ QtTaskTree::QStartedBarrier Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtTaskTree_QStartedBarrier'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtTaskTree::QStartedBarrier::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qstartedbarrier.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtTaskTree::QStartedBarrier::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10QtTaskTree15QStartedBarrier10metaObjectEv',
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
    'QtTaskTree::QStartedBarrier::QStartedBarrier()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qstartedbarrier.html#QStartedBarrier
    """
    #  QtTaskTree::QStartedBarrier::QStartedBarrier()
    self._noteCreation(QStartedBarrier, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree15QStartedBarrierC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QtTaskTree::QStartedBarrier::QStartedBarrier(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qstartedbarrier.html#QStartedBarrier

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtTaskTree::QStartedBarrier::QStartedBarrier(QObject *parent)
    self._noteCreation(QStartedBarrier, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree15QStartedBarrierC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  def __init__(self, limit: int, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QtTaskTree::QStartedBarrier::QStartedBarrier(qsizetype limit, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qstartedbarrier.html#QStartedBarrier

    Parameters
    ----------

    limit : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtTaskTree::QStartedBarrier::QStartedBarrier(qsizetype limit, QObject
    #      *parent)
    self._noteCreation(QStartedBarrier, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree15QStartedBarrierC1ExP7QObject',
        limit, self._addressOf(parent, 'QObject'),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QtTaskTree::QStartedBarrier::event(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttasktree-qstartedbarrier.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtTaskTree::QStartedBarrier::event(QEvent *event)
    ritual = 'ritual_ZN10QtTaskTree15QStartedBarrier5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QtTaskTree15QStartedBarrier5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))
