"""
QQuickRepeaterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickrepeater_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickRepeaterPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickRepeater
  from ..QtQmlModels import QQmlDelegateModelPointer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlDelegateModelPointer = WAIT['QQmlDelegateModelPointer']
  QQuickRepeater = WAIT['QQuickRepeater']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRepeaterPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickRepeaterPrivate: a plain Python object standing
  in front of one C++ QQuickRepeaterPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's QQuickRepeaterPrivate
  is built on Qt's QQuickItemPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRepeaterPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'requestItems',
  'applyDelegateChange', 'applyDelegateModelAccessChange', 'connectModel',
  'disconnectModel'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickRepeater *QQuickRepeaterPrivate::q_func() const': takes
    in Python what 'QQuickRepeater *QQuickRepeaterPrivate::q_func()' takes.
  - Qt's 'QQuickRepeaterPrivate::~QQuickRepeaterPrivate()': the destructor:
    Python never removes a C++ QQuickRepeaterPrivate.

  What to expect
  --------------

  - The C++ QQuickRepeaterPrivate is created at the first use, not by
    'QQuickRepeaterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRepeaterPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRepeaterPrivate'

  #  A C++ QQuickRepeaterPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRepeaterPrivate'

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
    Notes what was given, for Qt's
    'QQuickRepeaterPrivate::QQuickRepeaterPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeaterprivate.html#QQuickRepeaterPrivate
    """
    #  QQuickRepeaterPrivate::QQuickRepeaterPrivate()
    self._noteCreation(QQuickRepeaterPrivate, lambda: Rituals.call(
        'ritual_ZN21QQuickRepeaterPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickRepeater]:
    """
    Calls Qt's 'QQuickRepeater *QQuickRepeaterPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrepeaterprivate.html#q_func

    Returns
    -------

    Optional[QQuickRepeater]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRepeater *QQuickRepeaterPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuickRepeaterPrivate6q_funcEv')
    from . import QQuickRepeater
    return QQuickRepeater._cuteAt(address)

  def requestItems(self) -> None:
    """
    Calls Qt's 'void QQuickRepeaterPrivate::requestItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeaterprivate.html#requestItems
    """
    #  void QQuickRepeaterPrivate::requestItems()
    self.uglySide.call('ritual_ZN21QQuickRepeaterPrivate12requestItemsEv')

  def applyDelegateChange(self) -> None:
    """
    Calls Qt's 'void QQuickRepeaterPrivate::applyDelegateChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeaterprivate.html#applyDelegateChange
    """
    #  void QQuickRepeaterPrivate::applyDelegateChange()
    self.uglySide.call(
        'ritual_ZN21QQuickRepeaterPrivate19applyDelegateChangeEv',
    )

  def applyDelegateModelAccessChange(self) -> None:
    """
    Calls Qt's 'void
    QQuickRepeaterPrivate::applyDelegateModelAccessChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeaterprivate.html
    """
    #  void QQuickRepeaterPrivate::applyDelegateModelAccessChange()
    self.uglySide.call(
        'ritual_ZN21QQuickRepeaterPrivate30applyDelegateModelAccessChangeEv',
    )

  @overload(QQuickRepeater, QQmlDelegateModelPointer)
  @overload(QQuickRepeater, NoneType)
  @overload(NoneType, QQmlDelegateModelPointer)
  @overload(NoneType, NoneType)
  def connectModel(
      self,
      q: Optional[QQuickRepeater],
      model: Optional[QQmlDelegateModelPointer],
  ) -> None:
    """
    Calls Qt's 'void QQuickRepeaterPrivate::connectModel(QQuickRepeater *q,
    QQmlDelegateModelPointer *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeaterprivate.html#connectModel

    Parameters
    ----------

    q : Optional[QQuickRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QQmlDelegateModelPointer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRepeaterPrivate::connectModel(QQuickRepeater *q,
    #      QQmlDelegateModelPointer *model)
    self.uglySide.call(
        'ritual_ZN21QQuickRepeaterPrivate12connectModelEP14QQuickRepeaterP2'
        '4QQmlDelegateModelPointer',
        self._addressOf(q), self._addressOf(model),
    )

  @overload(QQuickRepeater, QQmlDelegateModelPointer)
  @overload(QQuickRepeater, NoneType)
  @overload(NoneType, QQmlDelegateModelPointer)
  @overload(NoneType, NoneType)
  def disconnectModel(
      self,
      q: Optional[QQuickRepeater],
      model: Optional[QQmlDelegateModelPointer],
  ) -> None:
    """
    Calls Qt's 'void QQuickRepeaterPrivate::disconnectModel(QQuickRepeater
    *q, QQmlDelegateModelPointer *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrepeaterprivate.html#disconnectModel

    Parameters
    ----------

    q : Optional[QQuickRepeater]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    model : Optional[QQmlDelegateModelPointer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRepeaterPrivate::disconnectModel(QQuickRepeater *q,
    #      QQmlDelegateModelPointer *model)
    self.uglySide.call(
        'ritual_ZN21QQuickRepeaterPrivate15disconnectModelEP14QQuickRepeate'
        'rP24QQmlDelegateModelPointer',
        self._addressOf(q), self._addressOf(model),
    )
