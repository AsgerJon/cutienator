"""
QQuickStackElement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackelement_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackElement to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from ..QtQml import QV4
from ..QtQuick import QQuickItemChangeListener
from ..QtQuick import QQuickItemViewTransitionableItem
from ..QtQuick import QQuickItemViewTransitioner
from . import QQuickStackView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QRectF
  from ..QtQml import RequiredProperties
  from ..QtQuick import QQuickItem, QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickItem = WAIT['QQuickItem']
  QQuickTransition = WAIT['QQuickTransition']
  QRectF = WAIT['QRectF']
  RequiredProperties = WAIT['RequiredProperties']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackElement(QQuickItemViewTransitionableItem, QQuickItemChangeListener):
  """
  The cute side of Qt's QQuickStackElement: a plain Python object standing in
  front of one C++ QQuickStackElement.

  It is built on the cute 'QQuickItemViewTransitionableItem', as Qt's
  QQuickStackElement is built on Qt's QQuickItemViewTransitionableItem, and
  has everything that class has. It is built on the cute
  'QQuickItemChangeListener' as well, as Qt's QQuickStackElement is built on
  Qt's QQuickItemChangeListener too, and has everything that class has.

  C++ hands a QQuickStackElement around as a copy, so every C++
  QQuickStackElement behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickStackElement that has a ritual and that Python
  can call so far, 8 names in all: 'load', 'incubate', 'initialize',
  'transitionNextReposition', 'prepareTransition', 'startTransition',
  'completeTransition', 'itemDestroyed'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickStackElement::~QQuickStackElement()': the destructor: Python
    removes its C++ QQuickStackElement by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 17 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 leans on
  'non-virtual thunk to QQuickStackElement.

  What to expect
  --------------

  - The C++ QQuickStackElement is created at the first use, not by
    'QQuickStackElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickStackElement back gives a copy the ritual made
    for Python, in a new cute QQuickStackElement.
  - Each name of Qt's QQuickStackElement that has no cute function yet,
    '__init__', 'fromObject', 'fromStackViewArg', 'fromString', 'setIndex',
    'setStatus', 'setView', 'setVisible', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackElement'

  #  Qt's QQuickStackElement is built on more than one class. The part of a
  #  C++ QQuickStackElement that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemChangeListener':
          'ritual_cast_QQuickStackElement_QQuickItemChangeListener',
  }

  #  A C++ QQuickStackElement Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStackElement'

  #  Qt's '~QQuickStackElement()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickStackElement behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickStackElementD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickStackElement::QQuickStackElement()': leans on 'non-virtual
    thunk to QQuickStackElement::itemDestroyed(QQuickItem*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackElement.__init__' has no cute function yet. Qt's "
        "'QQuickStackElement::QQuickStackElement()': leans on 'non-virtual "
        "thunk to QQuickStackElement::itemDestroyed(QQuickItem*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(WAIT['QV4.ExecutionEngine'], QQuickStackView)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, QQuickStackView)
  @overload(NoneType, NoneType)
  def load(
      self,
      v4: Optional[QV4.ExecutionEngine],
      parent: Optional[QQuickStackView],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickStackElement::load(QV4::ExecutionEngine *v4,
    QQuickStackView *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackelement.html#load

    Parameters
    ----------

    v4 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickStackView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickStackElement::load(QV4::ExecutionEngine *v4,
    #      QQuickStackView *parent)
    return self.uglySide.call(
        'ritual_ZN18QQuickStackElement4loadEPN3QV415ExecutionEngineEP15QQui'
        'ckStackView',
        self._addressOf(v4), self._addressOf(parent),
    )

  @overload(WAIT['QV4.ExecutionEngine'], QObject, RequiredProperties)
  @overload(WAIT['QV4.ExecutionEngine'], QObject, NoneType)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, RequiredProperties)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType)
  @overload(NoneType, QObject, RequiredProperties)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, RequiredProperties)
  @overload(NoneType, NoneType, NoneType)
  def incubate(
      self,
      v4: Optional[QV4.ExecutionEngine],
      object: Optional[QObject],
      requiredProperties: Optional[RequiredProperties],
  ) -> None:
    """
    Calls Qt's 'void QQuickStackElement::incubate(QV4::ExecutionEngine *v4,
    QObject *object, RequiredProperties *requiredProperties)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackelement.html#incubate

    Parameters
    ----------

    v4 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requiredProperties : Optional[RequiredProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackElement::incubate(QV4::ExecutionEngine *v4, QObject
    #      *object, RequiredProperties *requiredProperties)
    self.uglySide.call(
        'ritual_ZN18QQuickStackElement8incubateEPN3QV415ExecutionEngineEP7Q'
        'ObjectP18RequiredProperties',
        self._addressOf(v4), self._addressOf(object, 'QObject'),
        self._addressOf(requiredProperties),
    )

  @overload(WAIT['QV4.ExecutionEngine'], RequiredProperties)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, RequiredProperties)
  @overload(NoneType, NoneType)
  def initialize(
      self,
      v4: Optional[QV4.ExecutionEngine],
      requiredProperties: Optional[RequiredProperties],
  ) -> None:
    """
    Calls Qt's 'void QQuickStackElement::initialize(QV4::ExecutionEngine *v4,
    RequiredProperties *requiredProperties)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstackelement.html#initialize

    Parameters
    ----------

    v4 : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    requiredProperties : Optional[RequiredProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackElement::initialize(QV4::ExecutionEngine *v4,
    #      RequiredProperties *requiredProperties)
    self.uglySide.call(
        'ritual_ZN18QQuickStackElement10initializeEPN3QV415ExecutionEngineE'
        'P18RequiredProperties',
        self._addressOf(v4), self._addressOf(requiredProperties),
    )

  @overload(
      QQuickItemViewTransitioner, QQuickItemViewTransitioner.TransitionType,
      bool,
  )
  @overload(NoneType, QQuickItemViewTransitioner.TransitionType, bool)
  def transitionNextReposition(
      self,
      transitioner: Optional[QQuickItemViewTransitioner],
      type: QQuickItemViewTransitioner.TransitionType,
      asTarget: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickStackElement::transitionNextReposition(QQuickItemViewTransitioner
    *transitioner, QQuickItemViewTransitioner::TransitionType type, bool
    asTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackelement.html#transitionNextReposition

    Parameters
    ----------

    transitioner : Optional[QQuickItemViewTransitioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QQuickItemViewTransitioner.TransitionType
      Passed on as its number.

    asTarget : bool
      Passed on as it is.
    """
    #  void QQuickStackElement::transitionNextReposition(
    #      QQuickItemViewTransitioner *transitioner,
    #      QQuickItemViewTransitioner::TransitionType type, bool asTarget)
    self.uglySide.call(
        'ritual_ZN18QQuickStackElement24transitionNextRepositionEP26QQuickI'
        'temViewTransitionerNS0_14TransitionTypeEb',
        self._addressOf(transitioner), type.value, asTarget,
    )

  @overload(QQuickItemViewTransitioner, QRectF)
  @overload(NoneType, QRectF)
  def prepareTransition(
      self,
      transitioner: Optional[QQuickItemViewTransitioner],
      viewBounds: QRectF,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickStackElement::prepareTransition(QQuickItemViewTransitioner
    *transitioner, const QRectF &viewBounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackelement.html#prepareTransition

    Parameters
    ----------

    transitioner : Optional[QQuickItemViewTransitioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QQuickStackElement::prepareTransition(QQuickItemViewTransitioner
    #      *transitioner, const QRectF &viewBounds)
    return self.uglySide.call(
        'ritual_ZN18QQuickStackElement17prepareTransitionEP26QQuickItemView'
        'TransitionerRK6QRectF',
        self._addressOf(transitioner), self._valueOf(viewBounds),
    )

  @overload(QQuickItemViewTransitioner, QQuickStackView.Status)
  @overload(NoneType, QQuickStackView.Status)
  def startTransition(
      self,
      transitioner: Optional[QQuickItemViewTransitioner],
      status: QQuickStackView.Status,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickStackElement::startTransition(QQuickItemViewTransitioner
    *transitioner, QQuickStackView::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackelement.html#startTransition

    Parameters
    ----------

    transitioner : Optional[QQuickItemViewTransitioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    status : QQuickStackView.Status
      Passed on as its number.
    """
    #  void QQuickStackElement::startTransition(QQuickItemViewTransitioner
    #      *transitioner, QQuickStackView::Status status)
    self.uglySide.call(
        'ritual_ZN18QQuickStackElement15startTransitionEP26QQuickItemViewTr'
        'ansitionerN15QQuickStackView6StatusE',
        self._addressOf(transitioner), status.value,
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def completeTransition(
      self,
      quickTransition: Optional[QQuickTransition],
  ) -> None:
    """
    Calls Qt's 'void QQuickStackElement::completeTransition(QQuickTransition
    *quickTransition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackelement.html#completeTransition

    Parameters
    ----------

    quickTransition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackElement::completeTransition(QQuickTransition
    #      *quickTransition)
    self.uglySide.call(
        'ritual_ZN18QQuickStackElement18completeTransitionEP16QQuickTransit'
        'ion',
        self._addressOf(quickTransition),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickStackElement::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackelement.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStackElement::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN18QQuickStackElement13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickStackElement13itemDestroyedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @staticmethod
  def fromObject(*__, **_) -> Never:
    """
    Qt's 'QQuickStackElement *QQuickStackElement::fromObject(QObject *object,
    QQuickStackView *view, QString *error)': leans on 'non-virtual thunk to
    QQuickStackElement::itemDestroyed(QQuickItem*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackElement.fromObject' has no cute function yet. Qt's "
        "'QQuickStackElement *QQuickStackElement::fromObject(QObject "
        "*object, QQuickStackView *view, QString *error)': leans on "
        "'non-virtual thunk to "
        "QQuickStackElement::itemDestroyed(QQuickItem*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def fromStackViewArg(*__, **_) -> Never:
    """
    Qt's 'QQuickStackElement *QQuickStackElement::fromStackViewArg(QQmlEngine
    *engine, QQuickStackView *view, QQuickStackViewArg arg)': leans on
    'non-virtual thunk to QQuickStackElement::itemDestroyed(QQuickItem*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackElement.fromStackViewArg' has no cute function yet. "
        "Qt's 'QQuickStackElement "
        "*QQuickStackElement::fromStackViewArg(QQmlEngine *engine, "
        "QQuickStackView *view, QQuickStackViewArg arg)': leans on "
        "'non-virtual thunk to "
        "QQuickStackElement::itemDestroyed(QQuickItem*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def fromString(*__, **_) -> Never:
    """
    Qt's 'QQuickStackElement *QQuickStackElement::fromString(QQmlEngine
    *engine, const QString &str, QQuickStackView *view, QString *error)':
    leans on 'non-virtual thunk to
    QQuickStackElement::itemDestroyed(QQuickItem*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickStackElement.fromString' has no cute function yet. Qt's "
        "'QQuickStackElement *QQuickStackElement::fromString(QQmlEngine "
        "*engine, const QString &str, QQuickStackView *view, QString "
        "*error)': leans on 'non-virtual thunk to "
        "QQuickStackElement::itemDestroyed(QQuickItem*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setIndex(*__, **_) -> Never:
    """
    Qt's 'void QQuickStackElement::setIndex(int index)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'attachedStackObject'.
    """
    raise NotImplementedError(
        "'QQuickStackElement.setIndex' has no cute function yet. Qt's 'void "
        "QQuickStackElement::setIndex(int index)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'attachedStackObject'.")

  @staticmethod
  def setStatus(*__, **_) -> Never:
    """
    Qt's 'void QQuickStackElement::setStatus(QQuickStackView::Status
    status)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'attachedStackObject'.
    """
    raise NotImplementedError(
        "'QQuickStackElement.setStatus' has no cute function yet. Qt's "
        "'void QQuickStackElement::setStatus(QQuickStackView::Status "
        "status)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'attachedStackObject'.")

  @staticmethod
  def setView(*__, **_) -> Never:
    """
    Qt's 'void QQuickStackElement::setView(QQuickStackView *view)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'attachedStackObject'.
    """
    raise NotImplementedError(
        "'QQuickStackElement.setView' has no cute function yet. Qt's 'void "
        "QQuickStackElement::setView(QQuickStackView *view)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'attachedStackObject'.")

  @staticmethod
  def setVisible(*__, **_) -> Never:
    """
    Qt's 'void QQuickStackElement::setVisible(bool visible)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'attachedStackObject'.
    """
    raise NotImplementedError(
        "'QQuickStackElement.setVisible' has no cute function yet. Qt's "
        "'void QQuickStackElement::setVisible(bool visible)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'attachedStackObject'.")


#  Qt's 'QList<QQuickStackElement *>': the list of QQuickStackElement, which
#  'QList[QQuickStackElement]' gives. It is made here, so that there is one
#  as soon as there can be a QQuickStackElement.
QList.createKind(
    QQuickStackElement, 'address',
    make='ritual_list_make_QQuickStackElement_ptr',
    add='ritual_list_add_QQuickStackElement_ptr',
    size='ritual_list_size_QQuickStackElement_ptr',
    at='ritual_list_at_QQuickStackElement_ptr',
    drop='ritual_list_drop_QQuickStackElement_ptr',
)
