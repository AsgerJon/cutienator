"""
QGestureManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgesturemanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGestureManager to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QGesture, QGestureRecognizer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGesture = WAIT['QGesture']
  QGestureRecognizer = WAIT['QGestureRecognizer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGestureManager(QObject):
  """
  The cute side of Qt's QGestureManager: a plain Python object standing in
  front of one C++ QGestureManager.

  It is built on the cute 'QObject', as Qt's QGestureManager is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGestureManager that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'registerGestureRecognizer',
  'unregisterGestureRecognizer', 'cleanupCachedGestures', 'recycle',
  'cleanupGesturesForRemovedRecognizer'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGestureManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGestureManager::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGestureManager::~QGestureManager()': the destructor: Python never
    removes a C++ QGestureManager.
  - Qt's 'void QGestureManager::getGestureTargets(const QSet<QGesture *>
    &gestures, QHash<QWidget *, QList<QGesture *>> *conflicts, QHash<QWidget
    *, QList<QGesture *>> *normal)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  13 of the 23 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 5 leans on
  'QGestureManager; 2 not a gap; 1 leans on 'QWidgetWindow.

  What to expect
  --------------

  - The C++ QGestureManager is created at the first use, not by
    'QGestureManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGestureManager.
  - Qt tells when it has removed the C++ QGestureManager. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGestureManager that has no cute function yet,
    '__init__', 'cancelGesturesForChildren', 'deliverEvents', 'filterEvent',
    'filterEventThroughContexts', 'gesturePending', 'getGestureTargets',
    'getState', 'instance', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGestureManager, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class InstanceCreation(CuteNum):
    """
    The enum 'QGestureManager::InstanceCreation' of Qt, with the 2 names Qt
    gives in it.
    """

    ForceCreation = Kee[int](0)
    DontForceCreation = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGestureManager'

  #  A C++ QGestureManager Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGestureManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGestureManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgesturemanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGestureManager::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGestureManager10metaObjectEv')
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
    Qt's 'QGestureManager::QGestureManager(QObject *parent)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'panTouchPoints'.
    """
    raise NotImplementedError(
        "'QGestureManager.__init__' has no cute function yet. Qt's "
        "'QGestureManager::QGestureManager(QObject *parent)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'panTouchPoints'."
    )

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

  @overload(QGestureRecognizer)
  @overload(NoneType)
  def registerGestureRecognizer(
      self,
      recognizer: Optional[QGestureRecognizer],
  ) -> Qt.GestureType:
    """
    Calls Qt's 'Qt::GestureType
    QGestureManager::registerGestureRecognizer(QGestureRecognizer
    *recognizer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgesturemanager.html#registerGestureRecognizer

    Parameters
    ----------

    recognizer : Optional[QGestureRecognizer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.GestureType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.GestureType(number)'
      gives.
    """
    #  Qt::GestureType
    #      QGestureManager::registerGestureRecognizer(QGestureRecognizer
    #      *recognizer)
    return Qt.GestureType(self.uglySide.call(
        'ritual_ZN15QGestureManager25registerGestureRecognizerEP18QGestureR'
        'ecognizer',
        self._addressOf(recognizer, 'QGestureRecognizer'),
    ))

  @overload(Qt.GestureType)
  def unregisterGestureRecognizer(self, type: Qt.GestureType) -> None:
    """
    Calls Qt's 'void
    QGestureManager::unregisterGestureRecognizer(Qt::GestureType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgesturemanager.html#unregisterGestureRecognizer

    Parameters
    ----------

    type : Qt.GestureType
      Passed on as its number.
    """
    #  void QGestureManager::unregisterGestureRecognizer(Qt::GestureType
    #      type)
    self.uglySide.call(
        'ritual_ZN15QGestureManager27unregisterGestureRecognizerEN2Qt11Gest'
        'ureTypeE',
        type.value,
    )

  @overload(QObject, Qt.GestureType)
  @overload(NoneType, Qt.GestureType)
  def cleanupCachedGestures(
      self,
      target: Optional[QObject],
      type: Qt.GestureType,
  ) -> None:
    """
    Calls Qt's 'void QGestureManager::cleanupCachedGestures(QObject *target,
    Qt::GestureType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgesturemanager.html#cleanupCachedGestures

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Qt.GestureType
      Passed on as its number.
    """
    #  void QGestureManager::cleanupCachedGestures(QObject *target,
    #      Qt::GestureType type)
    self.uglySide.call(
        'ritual_ZN15QGestureManager21cleanupCachedGesturesEP7QObjectN2Qt11G'
        'estureTypeE',
        self._addressOf(target, 'QObject'), type.value,
    )

  @overload(QGesture)
  @overload(NoneType)
  def recycle(self, gesture: Optional[QGesture]) -> None:
    """
    Calls Qt's 'void QGestureManager::recycle(QGesture *gesture)'.

    Qt's own words: https://doc.qt.io/qt-6/qgesturemanager.html#recycle

    Parameters
    ----------

    gesture : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGestureManager::recycle(QGesture *gesture)
    self.uglySide.call(
        'ritual_ZN15QGestureManager7recycleEP8QGesture',
        self._addressOf(gesture),
    )

  @overload(QGesture)
  @overload(NoneType)
  def cleanupGesturesForRemovedRecognizer(
      self,
      gesture: Optional[QGesture],
  ) -> None:
    """
    Calls Qt's 'void
    QGestureManager::cleanupGesturesForRemovedRecognizer(QGesture *gesture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgesturemanager.html

    Parameters
    ----------

    gesture : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGestureManager::cleanupGesturesForRemovedRecognizer(QGesture
    #      *gesture)
    self.uglySide.call(
        'ritual_ZN15QGestureManager35cleanupGesturesForRemovedRecognizerEP8'
        'QGesture',
        self._addressOf(gesture),
    )

  @staticmethod
  def cancelGesturesForChildren(*__, **_) -> Never:
    """
    Qt's 'void QGestureManager::cancelGesturesForChildren(QGesture
    *originatingGesture)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: unknown type name
    'lcGestureManager'; did you mean 'QGestureManager'?.
    """
    raise NotImplementedError(
        "'QGestureManager.cancelGesturesForChildren' has no cute function "
        "yet. Qt's 'void "
        "QGestureManager::cancelGesturesForChildren(QGesture "
        "*originatingGesture)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: unknown "
        "type name 'lcGestureManager'; did you mean 'QGestureManager'?.")

  @staticmethod
  def deliverEvents(*__, **_) -> Never:
    """
    Qt's 'void QGestureManager::deliverEvents(const QSet<QGesture *>
    &gestures, QSet<QGesture *> *undeliveredGestures)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: unknown type name 'lcGestureManager'; did you mean
    'QGestureManager'?.
    """
    raise NotImplementedError(
        "'QGestureManager.deliverEvents' has no cute function yet. Qt's "
        "'void QGestureManager::deliverEvents(const QSet<QGesture *> "
        "&gestures, QSet<QGesture *> *undeliveredGestures)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'lcGestureManager'; did you "
        "mean 'QGestureManager'?.")

  @staticmethod
  def filterEvent(*__, **_) -> Never:
    """
    - Qt's 'bool QGestureManager::filterEvent(QObject *receiver, QEvent
      *event)': leans on 'QWidgetWindow::staticMetaObject', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'bool QGestureManager::filterEvent(QWidget *receiver, QEvent
      *event)': leans on
      'QGestureManager::filterEventThroughContexts(QMultiMap<QObject*,
      Qt::GestureType> const&, QEvent*)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    - Qt's 'bool QGestureManager::filterEvent(QGraphicsObject *receiver,
      QEvent *event)': leans on
      'QGestureManager::filterEventThroughContexts(QMultiMap<QObject*,
      Qt::GestureType> const&, QEvent*)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGestureManager.filterEvent' has no cute function yet. Qt's 'bool "
        "QGestureManager::filterEvent(QObject *receiver, QEvent *event)': "
        "leans on 'QWidgetWindow::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'bool QGestureManager::filterEvent(QWidget *receiver, "
        "QEvent *event)': leans on "
        "'QGestureManager::filterEventThroughContexts(QMultiMap<QObject*, "
        "Qt::GestureType> const&, QEvent*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'bool QGestureManager::filterEvent(QGraphicsObject "
        "*receiver, QEvent *event)': leans on "
        "'QGestureManager::filterEventThroughContexts(QMultiMap<QObject*, "
        "Qt::GestureType> const&, QEvent*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def filterEventThroughContexts(*__, **_) -> Never:
    """
    Qt's 'bool QGestureManager::filterEventThroughContexts(const
    QMultiMap<QObject *, Qt::GestureType> &contexts, QEvent *event)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'lcGestureManager'; did you mean
    'QGestureManager'?.
    """
    raise NotImplementedError(
        "'QGestureManager.filterEventThroughContexts' has no cute function "
        "yet. Qt's 'bool QGestureManager::filterEventThroughContexts(const "
        "QMultiMap<QObject *, Qt::GestureType> &contexts, QEvent *event)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name "
        "'lcGestureManager'; did you mean 'QGestureManager'?.")

  @staticmethod
  def gesturePending(*__, **_) -> Never:
    """
    Qt's 'bool QGestureManager::gesturePending(QObject *o)': leans on
    'QGestureManager::QGestureManager(QObject*)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGestureManager.gesturePending' has no cute function yet. Qt's "
        "'bool QGestureManager::gesturePending(QObject *o)': leans on "
        "'QGestureManager::QGestureManager(QObject*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def getGestureTargets(*__, **_) -> Never:
    """
    Qt's 'void QGestureManager::getGestureTargets(const QSet<QGesture *>
    &gestures, QHash<QWidget *, QList<QGesture *>> *conflicts, QHash<QWidget
    *, QList<QGesture *>> *normal)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QGestureManager.getGestureTargets' has no cute function yet. Qt's "
        "'void QGestureManager::getGestureTargets(const QSet<QGesture *> "
        "&gestures, QHash<QWidget *, QList<QGesture *>> *conflicts, "
        "QHash<QWidget *, QList<QGesture *>> *normal)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def getState(*__, **_) -> Never:
    """
    Qt's 'QGesture *QGestureManager::getState(QObject *widget,
    QGestureRecognizer *recognizer, Qt::GestureType gesture)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'lcGestureManager'; did you
    mean 'QGestureManager'?.
    """
    raise NotImplementedError(
        "'QGestureManager.getState' has no cute function yet. Qt's "
        "'QGesture *QGestureManager::getState(QObject *widget, "
        "QGestureRecognizer *recognizer, Qt::GestureType gesture)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'lcGestureManager'; did you mean 'QGestureManager'?.")

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QGestureManager *QGestureManager::instance(InstanceCreation ic)':
    leans on 'QGestureManager::QGestureManager(QObject*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QGestureManager.instance' has no cute function yet. Qt's "
        "'QGestureManager *QGestureManager::instance(InstanceCreation ic)': "
        "leans on 'QGestureManager::QGestureManager(QObject*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
