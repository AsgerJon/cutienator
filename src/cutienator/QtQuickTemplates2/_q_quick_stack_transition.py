"""
QQuickStackTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstacktransition_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackTransition to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickStackView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickStackElement
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickStackElement = WAIT['QQuickStackElement']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackTransition(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStackTransition: a plain Python object standing
  in front of one C++ QQuickStackTransition.

  C++ hands a QQuickStackTransition around as a copy, so every C++
  QQuickStackTransition behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickStackTransition that has a ritual and that
  Python can call so far, 1 name in all: 'popExit'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickStackTransition::~QQuickStackTransition()': the destructor:
    Python removes its C++ QQuickStackTransition by it, and has no other use
    for it.

  What has no ritual
  ------------------

  5 of the 7 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickStackTransition is created at the first use, not by
    'QQuickStackTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickStackTransition back gives a copy the ritual
    made for Python, in a new cute QQuickStackTransition.
  - Each name of Qt's QQuickStackTransition that has no cute function yet,
    'popEnter', 'pushEnter', 'pushExit', 'replaceEnter', 'replaceExit', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickStackView.Operation, QQuickStackElement, QQuickStackView)
  @overload(QQuickStackView.Operation, QQuickStackElement, NoneType)
  @overload(QQuickStackView.Operation, NoneType, QQuickStackView)
  @overload(QQuickStackView.Operation, NoneType, NoneType)
  def popExit(
      operation: QQuickStackView.Operation,
      element: Optional[QQuickStackElement],
      view: Optional[QQuickStackView],
  ) -> QQuickStackTransition:
    """
    Calls Qt's 'QQuickStackTransition
    QQuickStackTransition::popExit(QQuickStackView::Operation operation,
    QQuickStackElement *element, QQuickStackView *view)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstacktransition.html#popExit

    Parameters
    ----------

    operation : QQuickStackView.Operation
      Passed on as its number.

    element : Optional[QQuickStackElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    view : Optional[QQuickStackView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQuickStackTransition
      A new cute QQuickStackTransition around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickStackTransition
    #      QQuickStackTransition::popExit(QQuickStackView::Operation
    #      operation, QQuickStackElement *element, QQuickStackView *view)
    address = Rituals.call(
        'ritual_ZN21QQuickStackTransition7popExitEN15QQuickStackView9Operat'
        'ionEP18QQuickStackElementPS0_',
        operation.value, CuteMixin._addressOf(element),
        CuteMixin._addressOf(view),
    )
    return QQuickStackTransition._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackTransition'

  #  Qt's '~QQuickStackTransition()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickStackTransition behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQuickStackTransitionD1Ev'

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

  @staticmethod
  def popEnter(*__, **_) -> Never:
    """
    Qt's 'QQuickStackTransition
    QQuickStackTransition::popEnter(QQuickStackView::Operation operation,
    QQuickStackElement *element, QQuickStackView *view)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'operationTransition'.
    """
    raise NotImplementedError(
        "'QQuickStackTransition.popEnter' has no cute function yet. Qt's "
        "'QQuickStackTransition "
        "QQuickStackTransition::popEnter(QQuickStackView::Operation "
        "operation, QQuickStackElement *element, QQuickStackView *view)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'operationTransition'.")

  @staticmethod
  def pushEnter(*__, **_) -> Never:
    """
    Qt's 'QQuickStackTransition
    QQuickStackTransition::pushEnter(QQuickStackView::Operation operation,
    QQuickStackElement *element, QQuickStackView *view)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'operationTransition'.
    """
    raise NotImplementedError(
        "'QQuickStackTransition.pushEnter' has no cute function yet. Qt's "
        "'QQuickStackTransition "
        "QQuickStackTransition::pushEnter(QQuickStackView::Operation "
        "operation, QQuickStackElement *element, QQuickStackView *view)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'operationTransition'.")

  @staticmethod
  def pushExit(*__, **_) -> Never:
    """
    Qt's 'QQuickStackTransition
    QQuickStackTransition::pushExit(QQuickStackView::Operation operation,
    QQuickStackElement *element, QQuickStackView *view)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'operationTransition'.
    """
    raise NotImplementedError(
        "'QQuickStackTransition.pushExit' has no cute function yet. Qt's "
        "'QQuickStackTransition "
        "QQuickStackTransition::pushExit(QQuickStackView::Operation "
        "operation, QQuickStackElement *element, QQuickStackView *view)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'operationTransition'.")

  @staticmethod
  def replaceEnter(*__, **_) -> Never:
    """
    Qt's 'QQuickStackTransition
    QQuickStackTransition::replaceEnter(QQuickStackView::Operation operation,
    QQuickStackElement *element, QQuickStackView *view)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'operationTransition'.
    """
    raise NotImplementedError(
        "'QQuickStackTransition.replaceEnter' has no cute function yet. "
        "Qt's 'QQuickStackTransition "
        "QQuickStackTransition::replaceEnter(QQuickStackView::Operation "
        "operation, QQuickStackElement *element, QQuickStackView *view)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'operationTransition'.")

  @staticmethod
  def replaceExit(*__, **_) -> Never:
    """
    Qt's 'QQuickStackTransition
    QQuickStackTransition::replaceExit(QQuickStackView::Operation operation,
    QQuickStackElement *element, QQuickStackView *view)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'operationTransition'.
    """
    raise NotImplementedError(
        "'QQuickStackTransition.replaceExit' has no cute function yet. Qt's "
        "'QQuickStackTransition "
        "QQuickStackTransition::replaceExit(QQuickStackView::Operation "
        "operation, QQuickStackElement *element, QQuickStackView *view)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'operationTransition'.")
