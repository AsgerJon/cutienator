"""
QGraphTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qgraphtransition_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphTransition to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus
from . import QGraphAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QGraphTransition(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QGraphTransition: a plain Python object standing in
  front of one C++ QGraphTransition.

  It is built on the cute 'QObject', as Qt's QGraphTransition is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QGraphTransition is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphTransition that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'initialized', 'contains',
  'classBegin', 'componentComplete'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGraphTransition::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGraphTransition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphTransition::~QGraphTransition()': the destructor: Python
    never removes a C++ QGraphTransition.
  - Qt's 'void QGraphTransition::clear(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QGraphTransition; 2 leans on 'QGraphAnimation; 2 leans on
  'QXYSeriesAnimation; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QGraphTransition is created at the first use, not by
    'QGraphTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphTransition.
  - Qt tells when it has removed the C++ QGraphTransition. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGraphTransition that has no cute function yet,
    '__init__', 'animations', 'append', 'clear', 'initialize',
    'onPointChanged', 'stop', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGraphTransition, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class TransitionType(CuteNum, scoped=True):
    """
    The enum 'QGraphTransition::TransitionType' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    PointAdded = Kee[int](1)
    PointReplaced = Kee[int](2)
    PointRemoved = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphTransition'

  #  Qt's QGraphTransition is built on more than one class. The part of a C++
  #  QGraphTransition that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QGraphTransition_QQmlParserStatus',
  }

  #  A C++ QGraphTransition Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphTransition'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphTransition::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphtransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QGraphTransition10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGraphTransition::QGraphTransition(QObject *parent)': leans on
    'QGraphTransition::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QGraphTransition.__init__' has no cute function yet. Qt's "
        "'QGraphTransition::QGraphTransition(QObject *parent)': leans on "
        "'QGraphTransition::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def initialized(self) -> bool:
    """
    Calls Qt's 'bool QGraphTransition::initialized()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphtransition.html#initialized
    """
    #  bool QGraphTransition::initialized()
    return self.uglySide.call('ritual_ZN16QGraphTransition11initializedEv')

  @overload(QGraphAnimation.GraphAnimationType)
  def contains(self, type: QGraphAnimation.GraphAnimationType) -> bool:
    """
    Calls Qt's 'bool
    QGraphTransition::contains(QGraphAnimation::GraphAnimationType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphtransition.html#contains

    Parameters
    ----------

    type : QGraphAnimation.GraphAnimationType
      Passed on as its number.
    """
    #  bool QGraphTransition::contains(QGraphAnimation::GraphAnimationType
    #      type)
    return self.uglySide.call(
        'ritual_ZN16QGraphTransition8containsEN15QGraphAnimation18GraphAnim'
        'ationTypeE',
        type.value,
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QGraphTransition::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphtransition.html#classBegin
    """
    #  void QGraphTransition::classBegin()
    ritual = 'ritual_ZN16QGraphTransition10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QGraphTransition10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QGraphTransition::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphtransition.html#componentComplete
    """
    #  void QGraphTransition::componentComplete()
    self.uglySide.call('ritual_ZN16QGraphTransition17componentCompleteEv')

  @staticmethod
  def animations(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QGraphTransition::animations()': leans on
    'QGraphAnimation::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphTransition.animations' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QGraphTransition::animations()': leans "
        "on 'QGraphAnimation::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def append(*__, **_) -> Never:
    """
    Qt's 'void QGraphTransition::append(QQmlListProperty<QObject> *a0,
    QObject *a1)': leans on 'QGraphAnimation::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QGraphTransition.append' has no cute function yet. Qt's 'void "
        "QGraphTransition::append(QQmlListProperty<QObject> *a0, QObject "
        "*a1)': leans on 'QGraphAnimation::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'void QGraphTransition::clear(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphTransition.clear' has no cute function yet. Qt's 'void "
        "QGraphTransition::clear(QQmlListProperty<QObject> *a0)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QGraphTransition::initialize()': leans on
    'QXYSeriesAnimation::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphTransition.initialize' has no cute function yet. Qt's 'void "
        "QGraphTransition::initialize()': leans on "
        "'QXYSeriesAnimation::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def onPointChanged(*__, **_) -> Never:
    """
    Qt's 'void QGraphTransition::onPointChanged(TransitionType type, int
    index, QPointF point)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QSplineSeries'.
    """
    raise NotImplementedError(
        "'QGraphTransition.onPointChanged' has no cute function yet. Qt's "
        "'void QGraphTransition::onPointChanged(TransitionType type, int "
        "index, QPointF point)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: member "
        "access into incomplete type 'QSplineSeries'.")

  @staticmethod
  def stop(*__, **_) -> Never:
    """
    Qt's 'void QGraphTransition::stop()': leans on
    'QXYSeriesAnimation::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphTransition.stop' has no cute function yet. Qt's 'void "
        "QGraphTransition::stop()': leans on "
        "'QXYSeriesAnimation::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
