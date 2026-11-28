"""
QQuickStackViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQml import QV4
from ..QtQuick import QQuickItemViewTransitionChangeListener
from . import QQuickControlPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQml import QQmlEngine
  from ..QtQuick import QQuickItem, QQuickItemViewTransitionableItem
  from . import QQuickStackElement, QQuickStackView, QQuickStackViewArg
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlEngine = WAIT['QQmlEngine']
  QQuickItem = WAIT['QQuickItem']
  QQuickItemViewTransitionableItem = WAIT['QQuickItemViewTransitionableItem']
  QQuickStackElement = WAIT['QQuickStackElement']
  QQuickStackView = WAIT['QQuickStackView']
  QQuickStackViewArg = WAIT['QQuickStackViewArg']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackViewPrivate(QQuickControlPrivate, QQuickItemViewTransitionChangeListener):
  """
  The cute side of Qt's QQuickStackViewPrivate: a plain Python object
  standing in front of one C++ QQuickStackViewPrivate.

  It is built on the cute 'QQuickControlPrivate', as Qt's
  QQuickStackViewPrivate is built on Qt's QQuickControlPrivate, and has
  everything that class has. It is built on the cute
  'QQuickItemViewTransitionChangeListener' as well, as Qt's
  QQuickStackViewPrivate is built on Qt's
  QQuickItemViewTransitionChangeListener too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQuickStackViewPrivate that has a ritual and that
  Python can call so far, 12 names in all: 'q_func', 'get', 'warn',
  'warnOfInterruption', 'setCurrentItem', 'parseElements', 'findElement',
  'popElements', 'ensureTransitioner', 'viewItemTransitionFinished',
  'setBusy', 'depthChange'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickStackView *QQuickStackViewPrivate::q_func() const':
    takes in Python what 'QQuickStackView *QQuickStackViewPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  8 of the 22 functions Qt declares: 6 leans on 'QQuickStackElement; 2 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file.

  What to expect
  --------------

  - The C++ QQuickStackViewPrivate is created at the first use, not by
    'QQuickStackViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStackViewPrivate.
  - Each name of Qt's QQuickStackViewPrivate that has no cute function yet,
    'completeTransition', 'createElement', 'popToItem', 'pushElement',
    'pushElements', 'replaceElements', 'startTransition', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickStackViewPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class CurrentItemPolicy(CuteNum, scoped=True):
    """
    The enum 'QQuickStackViewPrivate::CurrentItemPolicy' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    DoNotPop = Kee[int](0)
    Pop = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickStackView)
  @overload(NoneType)
  def get(
      view: Optional[QQuickStackView],
  ) -> Optional[QQuickStackViewPrivate]:
    """
    Calls Qt's 'QQuickStackViewPrivate
    *QQuickStackViewPrivate::get(QQuickStackView *view)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackviewprivate.html#get

    Parameters
    ----------

    view : Optional[QQuickStackView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickStackViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackViewPrivate *QQuickStackViewPrivate::get(QQuickStackView
    #      *view)
    address = Rituals.call(
        'ritual_ZN22QQuickStackViewPrivate3getEP15QQuickStackView',
        CuteMixin._addressOf(view),
    )
    return QQuickStackViewPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackViewPrivate'

  #  Qt's QQuickStackViewPrivate is built on more than one class. The part of
  #  a C++ QQuickStackViewPrivate that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemViewTransitionChangeListener':
          'ritual_cast_QQuickStackViewPrivate_QQuickItemViewTransitionChangeListener',
  }

  #  A C++ QQuickStackViewPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStackViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def findElement(
      self,
      item: Optional[QQuickItem],
  ) -> Optional[QQuickStackElement]:
    """
    Calls Qt's 'QQuickStackElement
    *QQuickStackViewPrivate::findElement(QQuickItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#findElement

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickStackElement]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackElement *QQuickStackViewPrivate::findElement(QQuickItem
    #      *item) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickStackViewPrivate11findElementEP10QQuickItem',
        self._addressOf(item),
    )
    from . import QQuickStackElement
    return QQuickStackElement._cuteAt(address)

  @overload(WAIT['QV4.Value'])
  def findElement(self, value: QV4.Value) -> Optional[QQuickStackElement]:
    """
    Calls Qt's 'QQuickStackElement *QQuickStackViewPrivate::findElement(const
    QV4::Value &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#findElement

    Parameters
    ----------

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    Optional[QQuickStackElement]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackElement *QQuickStackViewPrivate::findElement(const
    #      QV4::Value &value) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickStackViewPrivate11findElementERKN3QV45ValueE',
        self._valueOf(value),
    )
    from . import QQuickStackElement
    return QQuickStackElement._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickStackElement)
  @overload(NoneType)
  def setCurrentItem(self, element: Optional[QQuickStackElement]) -> None:
    """
    Calls Qt's 'void
    QQuickStackViewPrivate::setCurrentItem(QQuickStackElement *element)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#setCurrentItem

    Parameters
    ----------

    element : Optional[QQuickStackElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackViewPrivate::setCurrentItem(QQuickStackElement
    #      *element)
    self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate14setCurrentItemEP18QQuickStackEl'
        'ement',
        self._addressOf(element),
    )

  @overload(bool)
  def setBusy(self, busy: bool) -> None:
    """
    Calls Qt's 'void QQuickStackViewPrivate::setBusy(bool busy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#setBusy

    Parameters
    ----------

    busy : bool
      Passed on as it is.
    """
    #  void QQuickStackViewPrivate::setBusy(bool busy)
    self.uglySide.call('ritual_ZN22QQuickStackViewPrivate7setBusyEb', busy)

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

  def q_func(self) -> Optional[QQuickStackView]:
    """
    Calls Qt's 'QQuickStackView *QQuickStackViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackviewprivate.html#q_func

    Returns
    -------

    Optional[QQuickStackView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStackView *QQuickStackViewPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate6q_funcEv',
    )
    from . import QQuickStackView
    return QQuickStackView._cuteAt(address)

  @overload(str)
  def warn(self, error: str) -> None:
    """
    Calls Qt's 'void QQuickStackViewPrivate::warn(const QString &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackviewprivate.html#warn

    Parameters
    ----------

    error : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStackViewPrivate::warn(const QString &error)
    self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate4warnERK7QString', error,
    )

  @overload(str)
  def warnOfInterruption(self, attemptedOperation: str) -> None:
    """
    Calls Qt's 'void QQuickStackViewPrivate::warnOfInterruption(const QString
    &attemptedOperation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#warnOfInterruption

    Parameters
    ----------

    attemptedOperation : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickStackViewPrivate::warnOfInterruption(const QString
    #      &attemptedOperation)
    self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate18warnOfInterruptionERK7QString',
        attemptedOperation,
    )

  @overload(QQmlEngine, QList[QQuickStackViewArg])
  @overload(NoneType, QList[QQuickStackViewArg])
  def parseElements(
      self,
      engine: Optional[QQmlEngine],
      args: QList[QQuickStackViewArg],
  ) -> QList[QQuickStackElement]:
    """
    Calls Qt's 'QList<QQuickStackElement *>
    QQuickStackViewPrivate::parseElements(QQmlEngine *engine, const
    QList<QQuickStackViewArg> &args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#parseElements

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    args : QList[QQuickStackViewArg]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QQuickStackElement]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuickStackElement *>
    #      QQuickStackViewPrivate::parseElements(QQmlEngine *engine, const
    #      QList<QQuickStackViewArg> &args)
    address = self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate13parseElementsEP10QQmlEngineRK5Q'
        'ListI18QQuickStackViewArgE',
        self._addressOf(engine), self._valueOf(args),
    )
    from . import QQuickStackElement
    return QList[QQuickStackElement]._cuteOwning(address)

  @overload(WAIT['QV4.ExecutionEngine'], QQuickStackElement)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QQuickStackElement)
  @overload(NoneType, NoneType)
  def popElements(
      self,
      v4: Optional[QV4.ExecutionEngine],
      element: Optional[QQuickStackElement],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickStackViewPrivate::popElements(QV4::ExecutionEngine
    *v4, QQuickStackElement *element)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#popElements

    Parameters
    ----------

    v4 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    element : Optional[QQuickStackElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickStackViewPrivate::popElements(QV4::ExecutionEngine *v4,
    #      QQuickStackElement *element)
    return self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate11popElementsEPN3QV415ExecutionEn'
        'gineEP18QQuickStackElement',
        self._addressOf(v4), self._addressOf(element),
    )

  def ensureTransitioner(self) -> None:
    """
    Calls Qt's 'void QQuickStackViewPrivate::ensureTransitioner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#ensureTransitioner
    """
    #  void QQuickStackViewPrivate::ensureTransitioner()
    self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate18ensureTransitionerEv',
    )

  @overload(QQuickItemViewTransitionableItem)
  @overload(NoneType)
  def viewItemTransitionFinished(
      self,
      item: Optional[QQuickItemViewTransitionableItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickStackViewPrivate::viewItemTransitionFinished(
    QQuickItemViewTransitionableItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html

    Parameters
    ----------

    item : Optional[QQuickItemViewTransitionableItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackViewPrivate::viewItemTransitionFinished(
    #      QQuickItemViewTransitionableItem *item)
    self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate26viewItemTransitionFinishedEP32Q'
        'QuickItemViewTransitionableItem',
        self._addressOf(item),
    )

  @overload(int, int)
  def depthChange(self, newDepth: int, oldDepth: int) -> None:
    """
    Calls Qt's 'void QQuickStackViewPrivate::depthChange(int newDepth, int
    oldDepth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewprivate.html#depthChange

    Parameters
    ----------

    newDepth : int
      Passed on as it is.

    oldDepth : int
      Passed on as it is.
    """
    #  void QQuickStackViewPrivate::depthChange(int newDepth, int oldDepth)
    self.uglySide.call(
        'ritual_ZN22QQuickStackViewPrivate11depthChangeEii',
        newDepth, oldDepth,
    )

  @staticmethod
  def completeTransition(*__, **_) -> Never:
    """
    Qt's 'void QQuickStackViewPrivate::completeTransition(QQuickStackElement
    *element, QQuickTransition *transition, QQuickStackView::Status status)':
    leans on 'QQuickStackElement::setStatus(QQuickStackView::Status)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackViewPrivate.completeTransition' has no cute function "
        "yet. Qt's 'void "
        "QQuickStackViewPrivate::completeTransition(QQuickStackElement "
        "*element, QQuickTransition *transition, QQuickStackView::Status "
        "status)': leans on "
        "'QQuickStackElement::setStatus(QQuickStackView::Status)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def createElement(*__, **_) -> Never:
    """
    Qt's 'QQuickStackElement *QQuickStackViewPrivate::createElement(const
    QV4::Value &value, const QQmlRefPointer<QQmlContextData> &context,
    QString *error)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'resolvedUrl'.
    """
    raise NotImplementedError(
        "'QQuickStackViewPrivate.createElement' has no cute function yet. "
        "Qt's 'QQuickStackElement "
        "*QQuickStackViewPrivate::createElement(const QV4::Value &value, "
        "const QQmlRefPointer<QQmlContextData> &context, QString *error)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'resolvedUrl'.")

  @staticmethod
  def popToItem(*__, **_) -> Never:
    """
    Qt's 'QQuickItem *QQuickStackViewPrivate::popToItem(QV4::ExecutionEngine
    *v4, QQuickItem *item, QQuickStackView::Operation operation,
    CurrentItemPolicy currentItemPolicy)': leans on
    'QQuickStackElement::setStatus(QQuickStackView::Status)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackViewPrivate.popToItem' has no cute function yet. Qt's "
        "'QQuickItem "
        "*QQuickStackViewPrivate::popToItem(QV4::ExecutionEngine *v4, "
        "QQuickItem *item, QQuickStackView::Operation operation, "
        "CurrentItemPolicy currentItemPolicy)': leans on "
        "'QQuickStackElement::setStatus(QQuickStackView::Status)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def pushElement(*__, **_) -> Never:
    """
    Qt's 'bool QQuickStackViewPrivate::pushElement(QV4::ExecutionEngine *v4,
    QQuickStackElement *element)': leans on
    'QQuickStackElement::setIndex(int)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackViewPrivate.pushElement' has no cute function yet. "
        "Qt's 'bool "
        "QQuickStackViewPrivate::pushElement(QV4::ExecutionEngine *v4, "
        "QQuickStackElement *element)': leans on "
        "'QQuickStackElement::setIndex(int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def pushElements(*__, **_) -> Never:
    """
    Qt's 'bool QQuickStackViewPrivate::pushElements(QV4::ExecutionEngine *v4,
    const QList<QQuickStackElement *> &elements)': leans on
    'QQuickStackElement::setIndex(int)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackViewPrivate.pushElements' has no cute function yet. "
        "Qt's 'bool "
        "QQuickStackViewPrivate::pushElements(QV4::ExecutionEngine *v4, "
        "const QList<QQuickStackElement *> &elements)': leans on "
        "'QQuickStackElement::setIndex(int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def replaceElements(*__, **_) -> Never:
    """
    Qt's 'bool QQuickStackViewPrivate::replaceElements(QV4::ExecutionEngine
    *v4, QQuickStackElement *element, const QList<QQuickStackElement *>
    &elements)': leans on 'QQuickStackElement::setIndex(int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackViewPrivate.replaceElements' has no cute function yet. "
        "Qt's 'bool "
        "QQuickStackViewPrivate::replaceElements(QV4::ExecutionEngine *v4, "
        "QQuickStackElement *element, const QList<QQuickStackElement *> "
        "&elements)': leans on 'QQuickStackElement::setIndex(int)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def startTransition(*__, **_) -> Never:
    """
    Qt's 'void QQuickStackViewPrivate::startTransition(const
    QQuickStackTransition &first, const QQuickStackTransition &second, bool
    immediate)': leans on
    'QQuickStackElement::setStatus(QQuickStackView::Status)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackViewPrivate.startTransition' has no cute function yet. "
        "Qt's 'void QQuickStackViewPrivate::startTransition(const "
        "QQuickStackTransition &first, const QQuickStackTransition &second, "
        "bool immediate)': leans on "
        "'QQuickStackElement::setStatus(QQuickStackView::Status)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
