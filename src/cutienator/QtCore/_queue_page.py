"""
QueuePage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qthreadpool_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QueuePage to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRunnable
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRunnable = WAIT['QRunnable']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QueuePage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QueuePage: a plain Python object standing in front of
  one C++ QueuePage.

  C++ hands a QueuePage around as a copy, so every C++ QueuePage behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QueuePage that has a ritual and that Python can call
  so far, 8 names in all: 'isFull', 'isFinished', 'push', 'skipToNextOrEnd',
  'first', 'pop', 'tryTake', 'priority'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QueuePage::~QueuePage()': the destructor: Python removes its C++
    QueuePage by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QueuePage is created at the first use, not by 'QueuePage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QueuePage back gives a copy the ritual made for
    Python, in a new cute QueuePage.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QueuePage'

  #  Qt's '~QueuePage()'. Naming it makes this a value class: Python owns
  #  every C++ QueuePage behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QueuePageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def priority(self) -> int:
    """
    Calls Qt's 'int QueuePage::priority() const'.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#priority
    """
    #  int QueuePage::priority() const
    return self.uglySide.call('ritual_ZNK9QueuePage8priorityEv')

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

  @overload(QRunnable, int)
  @overload(NoneType, int)
  def __init__(self, runnable: Optional[QRunnable], pri: int) -> None:
    """
    Notes what was given, for Qt's 'QueuePage::QueuePage(QRunnable *runnable,
    int pri)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#QueuePage

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pri : int
      Passed on as it is.
    """
    #  QueuePage::QueuePage(QRunnable *runnable, int pri)
    self._noteCreation(QueuePage, lambda: Rituals.call(
        'ritual_ZN9QueuePageC1EP9QRunnablei',
        self._addressOf(runnable, 'QRunnable'), pri,
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

  def isFull(self) -> bool:
    """
    Calls Qt's 'bool QueuePage::isFull()'.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#isFull
    """
    #  bool QueuePage::isFull()
    return self.uglySide.call('ritual_ZN9QueuePage6isFullEv')

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QueuePage::isFinished()'.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#isFinished
    """
    #  bool QueuePage::isFinished()
    return self.uglySide.call('ritual_ZN9QueuePage10isFinishedEv')

  @overload(QRunnable)
  @overload(NoneType)
  def push(self, runnable: Optional[QRunnable]) -> None:
    """
    Calls Qt's 'void QueuePage::push(QRunnable *runnable)'.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#push

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QueuePage::push(QRunnable *runnable)
    self.uglySide.call(
        'ritual_ZN9QueuePage4pushEP9QRunnable',
        self._addressOf(runnable, 'QRunnable'),
    )

  def skipToNextOrEnd(self) -> None:
    """
    Calls Qt's 'void QueuePage::skipToNextOrEnd()'.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#skipToNextOrEnd
    """
    #  void QueuePage::skipToNextOrEnd()
    self.uglySide.call('ritual_ZN9QueuePage15skipToNextOrEndEv')

  def first(self) -> Optional[QRunnable]:
    """
    Calls Qt's 'QRunnable *QueuePage::first()'.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#first

    Returns
    -------

    Optional[QRunnable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRunnable *QueuePage::first()
    address = self.uglySide.call('ritual_ZN9QueuePage5firstEv')
    from . import QRunnable
    return QRunnable._cuteAt(address)

  def pop(self) -> Optional[QRunnable]:
    """
    Calls Qt's 'QRunnable *QueuePage::pop()'.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#pop

    Returns
    -------

    Optional[QRunnable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRunnable *QueuePage::pop()
    address = self.uglySide.call('ritual_ZN9QueuePage3popEv')
    from . import QRunnable
    return QRunnable._cuteAt(address)

  @overload(QRunnable)
  @overload(NoneType)
  def tryTake(self, runnable: Optional[QRunnable]) -> bool:
    """
    Calls Qt's 'bool QueuePage::tryTake(QRunnable *runnable)'.

    Qt's own words: https://doc.qt.io/qt-6/queuepage.html#tryTake

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QueuePage::tryTake(QRunnable *runnable)
    return self.uglySide.call(
        'ritual_ZN9QueuePage7tryTakeEP9QRunnable',
        self._addressOf(runnable, 'QRunnable'),
    )
