"""
QQuick3DXrInputManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrinputmanager_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrInputManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuick3DXrInputManagerPrivate


class QQuick3DXrInputManager(QObject):
  """
  The cute side of Qt's QQuick3DXrInputManager: a plain Python object
  standing in front of one C++ QQuick3DXrInputManager.

  It is built on the cute 'QObject', as Qt's QQuick3DXrInputManager is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrInputManager that has a ritual and that
  Python can call so far, 2 names in all: 'metaObject', 'd_func'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrInputManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrInputManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuick3DXrInputManagerPrivate
    *QQuick3DXrInputManager::d_func() const': takes in Python what
    'QQuick3DXrInputManagerPrivate *QQuick3DXrInputManager::d_func()' takes.
  - Qt's 'QQuick3DXrInputManager::~QQuick3DXrInputManager()': the destructor:
    Python never removes a C++ QQuick3DXrInputManager.

  What has no ritual
  ------------------

  10 of the 16 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'QQuick3DXrInputManager.

  What to expect
  --------------

  - The C++ QQuick3DXrInputManager is created at the first use, not by
    'QQuick3DXrInputManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrInputManager.
  - Qt tells when it has removed the C++ QQuick3DXrInputManager. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrInputManager that has no cute function yet,
    '__init__', 'instance', 'isValid', 'leftHandInput', 'registerController',
    'rightHandInput', 'unregisterController', holds a function that raises
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
  __qt_class__ = 'QQuick3DXrInputManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrInputManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrinputmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrInputManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DXrInputManager10metaObjectEv',
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
    Qt's 'QQuick3DXrInputManager::QQuick3DXrInputManager(QObject *parent)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: allocation of incomplete type
    'QQuick3DXrInputManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManager.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrInputManager::QQuick3DXrInputManager(QObject *parent)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: allocation of incomplete type "
        "'QQuick3DXrInputManagerPrivate'.")

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

  def d_func(self) -> Optional[QQuick3DXrInputManagerPrivate]:
    """
    Calls Qt's 'QQuick3DXrInputManagerPrivate
    *QQuick3DXrInputManager::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrinputmanager.html#d_func

    Returns
    -------

    Optional[QQuick3DXrInputManagerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrInputManagerPrivate *QQuick3DXrInputManager::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuick3DXrInputManager6d_funcEv',
    )
    from . import QQuick3DXrInputManagerPrivate
    return QQuick3DXrInputManagerPrivate._cuteAt(address)

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QQuick3DXrInputManager *QQuick3DXrInputManager::instance()': leans
    on 'QQuick3DXrInputManager::QQuick3DXrInputManager(QObject*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManager.instance' has no cute function yet. Qt's "
        "'QQuick3DXrInputManager *QQuick3DXrInputManager::instance()': "
        "leans on "
        "'QQuick3DXrInputManager::QQuick3DXrInputManager(QObject*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def isValid(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrInputManager::isValid() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const
    QQuick3DXrInputManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManager.isValid' has no cute function yet. Qt's "
        "'bool QQuick3DXrInputManager::isValid() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuick3DXrInputManagerPrivate'.")

  @staticmethod
  def leftHandInput(*__, **_) -> Never:
    """
    Qt's 'QQuick3DXrHandInput *QQuick3DXrInputManager::leftHandInput()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'const QQuick3DXrInputManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManager.leftHandInput' has no cute function yet. "
        "Qt's 'QQuick3DXrHandInput *QQuick3DXrInputManager::leftHandInput() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'const QQuick3DXrInputManagerPrivate'.")

  @staticmethod
  def registerController(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrInputManager::registerController(QQuick3DXrController
    *controller)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QQuick3DXrInputManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManager.registerController' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DXrInputManager::registerController(QQuick3DXrController "
        "*controller)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QQuick3DXrInputManagerPrivate'.")

  @staticmethod
  def rightHandInput(*__, **_) -> Never:
    """
    Qt's 'QQuick3DXrHandInput *QQuick3DXrInputManager::rightHandInput()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'const QQuick3DXrInputManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManager.rightHandInput' has no cute function yet. "
        "Qt's 'QQuick3DXrHandInput "
        "*QQuick3DXrInputManager::rightHandInput() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuick3DXrInputManagerPrivate'.")

  @staticmethod
  def unregisterController(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrInputManager::unregisterController(QQuick3DXrController
    *controller)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QQuick3DXrInputManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrInputManager.unregisterController' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DXrInputManager::unregisterController(QQuick3DXrController "
        "*controller)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QQuick3DXrInputManagerPrivate'.")
