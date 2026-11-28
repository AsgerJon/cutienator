"""
QQuick3DXrActionMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrActionMapper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuick3DXrActionMapper(QObject):
  """
  The cute side of Qt's QQuick3DXrActionMapper: a plain Python object
  standing in front of one C++ QQuick3DXrActionMapper.

  It is built on the cute 'QObject', as Qt's QQuick3DXrActionMapper is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrActionMapper that has a ritual and that
  Python can call so far, 1 name in all: 'metaObject'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrActionMapper::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrActionMapper::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  11 of the 14 functions Qt declares: 6 leans on 'vtable for
  QQuick3DXrActionMapper', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 2 not a gap; 2 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 1 leans on 'QQuick3DXrActionMapper.

  What to expect
  --------------

  - The C++ QQuick3DXrActionMapper is created at the first use, not by
    'QQuick3DXrActionMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrActionMapper.
  - Qt tells when it has removed the C++ QQuick3DXrActionMapper. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrActionMapper that has no cute function yet,
    '__init__', 'getHapticEffects', 'handleInput', 'instance',
    'registerAction', 'registerHapticEffect', 'removeAction',
    'removeHapticEffect', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrActionMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrActionMapper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxractionmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrActionMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DXrActionMapper10metaObjectEv',
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
    Qt's 'QQuick3DXrActionMapper::QQuick3DXrActionMapper(QObject *parent)':
    leans on 'vtable for QQuick3DXrActionMapper', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrActionMapper.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrActionMapper::QQuick3DXrActionMapper(QObject *parent)': "
        "leans on 'vtable for QQuick3DXrActionMapper', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
  def getHapticEffects(*__, **_) -> Never:
    """
    Qt's 'QList<QPointer<QQuick3DXrHapticFeedback>>
    QQuick3DXrActionMapper::getHapticEffects(QtQuick3DXr::Controller
    controller)': leans on 'vtable for QQuick3DXrActionMapper', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrActionMapper.getHapticEffects' has no cute function "
        "yet. Qt's 'QList<QPointer<QQuick3DXrHapticFeedback>> "
        "QQuick3DXrActionMapper::getHapticEffects(QtQuick3DXr::Controller "
        "controller)': leans on 'vtable for QQuick3DXrActionMapper', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def handleInput(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrActionMapper::handleInput(QQuick3DXrInputAction::Action id,
    QtQuick3DXr::Controller controller, const char *shortName, float value)':
    leans on 'vtable for QQuick3DXrActionMapper', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrActionMapper.handleInput' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DXrActionMapper::handleInput(QQuick3DXrInputAction::Action "
        "id, QtQuick3DXr::Controller controller, const char *shortName, "
        "float value)': leans on 'vtable for QQuick3DXrActionMapper', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QQuick3DXrActionMapper *QQuick3DXrActionMapper::instance()': leans
    on 'vtable for QQuick3DXrActionMapper', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrActionMapper.instance' has no cute function yet. Qt's "
        "'QQuick3DXrActionMapper *QQuick3DXrActionMapper::instance()': "
        "leans on 'vtable for QQuick3DXrActionMapper', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def registerAction(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrActionMapper::registerAction(QQuick3DXrInputAction
    *action)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'actionStringKey'.
    """
    raise NotImplementedError(
        "'QQuick3DXrActionMapper.registerAction' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DXrActionMapper::registerAction(QQuick3DXrInputAction "
        "*action)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'actionStringKey'.")

  @staticmethod
  def registerHapticEffect(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrActionMapper::registerHapticEffect(
    QPointer<QQuick3DXrHapticFeedback> a0)': leans on 'vtable for
    QQuick3DXrActionMapper', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrActionMapper.registerHapticEffect' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DXrActionMapper::registerHapticEffect(QPointer<QQuick3DXrHap"
        "ticFeedback> a0)': leans on 'vtable for QQuick3DXrActionMapper', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def removeAction(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrActionMapper::removeAction(QQuick3DXrInputAction
    *action)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'actionIntKey'.
    """
    raise NotImplementedError(
        "'QQuick3DXrActionMapper.removeAction' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DXrActionMapper::removeAction(QQuick3DXrInputAction "
        "*action)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'actionIntKey'.")

  @staticmethod
  def removeHapticEffect(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrActionMapper::removeHapticEffect(QQuick3DXrHapticFeedback
    *action)': leans on 'vtable for QQuick3DXrActionMapper', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrActionMapper.removeHapticEffect' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DXrActionMapper::removeHapticEffect(QQuick3DXrHapticFeedback"
        " *action)': leans on 'vtable for QQuick3DXrActionMapper', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
