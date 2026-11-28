"""
QQuickItemViewTransitionChangeListener binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickItemViewTransitionChangeListener to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickItemViewTransitionableItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItemViewTransitionableItem = WAIT['QQuickItemViewTransitionableItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemViewTransitionChangeListener(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickItemViewTransitionChangeListener: a plain
  Python object standing in front of one C++
  QQuickItemViewTransitionChangeListener.

  What exists
  -----------

  Every function of Qt's QQuickItemViewTransitionChangeListener that has a
  ritual and that Python can call so far, 1 name in all:
  'viewItemTransitionFinished'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickItemViewTransitionChangeListener::
    ~QQuickItemViewTransitionChangeListener()': the destructor: Python never
    removes a C++ QQuickItemViewTransitionChangeListener.

  What to expect
  --------------

  - The C++ QQuickItemViewTransitionChangeListener is created at the first
    use, not by 'QQuickItemViewTransitionChangeListener(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemViewTransitionChangeListener.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemViewTransitionChangeListener'

  #  A C++ QQuickItemViewTransitionChangeListener Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemViewTransitionChangeListener'

  #  The functions Qt calls itself that
  #  QQuickItemViewTransitionChangeListener is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'viewItemTransitionFinished': (
          ('_ZN38QQuickItemViewTransitionChangeListener26viewItemTransition'
           'FinishedEP32QQuickItemViewTransitionableItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQuick:QQuickItemViewTransitionableItem'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QQuickItemViewTransitionChangeListener::
    QQuickItemViewTransitionChangeListener()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionchangelistener.html
    """
    #  QQuickItemViewTransitionChangeListener::
    #      QQuickItemViewTransitionChangeListener()
    self._noteCreation(
        QQuickItemViewTransitionChangeListener, lambda: Rituals.call(
            'ritual_ZN38QQuickItemViewTransitionChangeListenerC1Ev',
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

  @overload(QQuickItemViewTransitionableItem)
  @overload(NoneType)
  def viewItemTransitionFinished(
      self,
      item: Optional[QQuickItemViewTransitionableItem],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewTransitionChangeListener::viewItemTransitionFinished(
    QQuickItemViewTransitionableItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewtransitionchangelistener.html

    Parameters
    ----------

    item : Optional[QQuickItemViewTransitionableItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewTransitionChangeListener::
    #      viewItemTransitionFinished(QQuickItemViewTransitionableItem *item)
    self._callAs(
        'QQuickItemViewTransitionChangeListener',
        'ritual_ZN38QQuickItemViewTransitionChangeListener26viewItemTransit'
        'ionFinishedEP32QQuickItemViewTransitionableItem',
        self._addressOf(item),
    )
