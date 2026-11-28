"""
QQuickWebEngineActionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineaction_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineActionPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QQuickWebEngineAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QQuickWebEngineActionPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickWebEngineActionPrivate: a plain Python object
  standing in front of one C++ QQuickWebEngineActionPrivate.

  C++ hands a QQuickWebEngineActionPrivate around as a copy, so every C++
  QQuickWebEngineActionPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineActionPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func', 'setEnabled',
  'data', 'trigger'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickWebEngineAction *QQuickWebEngineActionPrivate::q_func()
    const': takes in Python what 'QQuickWebEngineAction
    *QQuickWebEngineActionPrivate::q_func()' takes.
  - Qt's 'QQuickWebEngineActionPrivate::~QQuickWebEngineActionPrivate()': the
    destructor: Python removes its C++ QQuickWebEngineActionPrivate by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickWebEngineActionPrivate is created at the first use, not by
    'QQuickWebEngineActionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickWebEngineActionPrivate back gives a copy the
    ritual made for Python, in a new cute QQuickWebEngineActionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineActionPrivate'

  #  Qt's '~QQuickWebEngineActionPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickWebEngineActionPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QQuickWebEngineActionPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def data(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickWebEngineActionPrivate::data() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineactionprivate.html#data

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickWebEngineActionPrivate::data() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickWebEngineActionPrivate4dataEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineActionPrivate::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineactionprivate.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineActionPrivate::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN28QQuickWebEngineActionPrivate10setEnabledEb', enabled,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, str, str, bool)
  def __init__(
      self,
      data: QVariant,
      text: str,
      iconName: str,
      enabled: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWebEngineActionPrivate::QQuickWebEngineActionPrivate(const
    QVariant &data, const QString &text, const QString &iconName, bool
    enabled)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineactionprivate.html

    Parameters
    ----------

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    iconName : str
      Passed on as it is: a QString is made of it for the call.

    enabled : bool
      Passed on as it is.
    """
    #  QQuickWebEngineActionPrivate::QQuickWebEngineActionPrivate(const
    #      QVariant &data, const QString &text, const QString &iconName, bool
    #      enabled)
    self._noteCreation(QQuickWebEngineActionPrivate, lambda: Rituals.call(
        'ritual_ZN28QQuickWebEngineActionPrivateC1ERK8QVariantRK7QStringS5_'
        'b',
        self._valueOf(data), text, iconName, enabled,
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

  def q_func(self) -> Optional[QQuickWebEngineAction]:
    """
    Calls Qt's 'QQuickWebEngineAction
    *QQuickWebEngineActionPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineactionprivate.html#q_func

    Returns
    -------

    Optional[QQuickWebEngineAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWebEngineAction *QQuickWebEngineActionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickWebEngineActionPrivate6q_funcEv',
    )
    from . import QQuickWebEngineAction
    return QQuickWebEngineAction._cuteAt(address)

  def trigger(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineActionPrivate::trigger()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebengineactionprivate.html#trigger
    """
    #  void QQuickWebEngineActionPrivate::trigger()
    self.uglySide.call('ritual_ZN28QQuickWebEngineActionPrivate7triggerEv')
