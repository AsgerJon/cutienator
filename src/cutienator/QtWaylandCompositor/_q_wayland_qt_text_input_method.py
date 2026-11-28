"""
QWaylandQtTextInputMethod binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandqttextinputmethod.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QWaylandQtTextInputMethod(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandQtTextInputMethod: a plain Python object
  standing in front of one C++ QWaylandQtTextInputMethod.

  What exists
  -----------

  Every function of Qt's QWaylandQtTextInputMethod that has a ritual and that
  Python can call so far, 1 name in all: 'metaObject'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQtTextInputMethod::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWaylandQtTextInputMethod::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandQtTextInputMethodPrivate
    *QWaylandQtTextInputMethod::d_func()': gives
    'QWaylandQtTextInputMethodPrivate', which has no cute class yet.
  - Qt's 'const QWaylandQtTextInputMethodPrivate
    *QWaylandQtTextInputMethod::d_func() const': gives
    'QWaylandQtTextInputMethodPrivate', which has no cute class yet.
  - Qt's 'QWaylandQtTextInputMethod::~QWaylandQtTextInputMethod()': the
    destructor: Python never removes a C++ QWaylandQtTextInputMethod.

  What has no ritual
  ------------------

  21 of the 27 functions Qt declares: 15 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 cannot be
  called and cannot be called through the meta-object and cannot be copied; 2
  not a gap; 1 leans on 'QWaylandQtTextInputMethod.

  What to expect
  --------------

  - The C++ QWaylandQtTextInputMethod is created at the first use, not by
    'QWaylandQtTextInputMethod(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQtTextInputMethod.
  - Each name of Qt's QWaylandQtTextInputMethod that has no cute function
    yet, '__init__', 'add', 'd_func', 'focusSurfaceDestroyed',
    'focusedSurface', 'inputMethodQuery', 'interface', 'interfaceName',
    'isSurfaceEnabled', 'sendInputDirectionChanged', 'sendInputMethodEvent',
    'sendKeyEvent', 'sendKeyboardRectangleChanged', 'sendLocaleChanged',
    'sendVisibleChanged', 'setFocus', 'surfaceDisabled', 'surfaceEnabled',
    'tr', 'updateInputMethod', holds a function that raises
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
  __qt_class__ = 'QWaylandQtTextInputMethod'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandQtTextInputMethod::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandqttextinputmethod.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQtTextInputMethod::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QWaylandQtTextInputMethod10metaObjectEv',
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
    Qt's 'QWaylandQtTextInputMethod::QWaylandQtTextInputMethod(QWaylandObject
    *container, QWaylandCompositor *compositor)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.__init__' has no cute function yet. "
        "Qt's "
        "'QWaylandQtTextInputMethod::QWaylandQtTextInputMethod(QWaylandObjec"
        "t *container, QWaylandCompositor *compositor)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QWaylandQtTextInputMethodPrivate'.")

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
  def add(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::add(::wl_client *client, uint32_t
    id, int version)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.add' has no cute function yet. Qt's "
        "'void QWaylandQtTextInputMethod::add(::wl_client *client, uint32_t "
        "id, int version)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandQtTextInputMethodPrivate
      *QWaylandQtTextInputMethod::d_func()': gives
      'QWaylandQtTextInputMethodPrivate', which has no cute class yet.
    - Qt's 'const QWaylandQtTextInputMethodPrivate
      *QWaylandQtTextInputMethod::d_func() const': gives
      'QWaylandQtTextInputMethodPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.d_func' has no cute function yet. Qt's "
        "'QWaylandQtTextInputMethodPrivate "
        "*QWaylandQtTextInputMethod::d_func()': gives "
        "'QWaylandQtTextInputMethodPrivate', which has no cute class yet. "
        "Qt's 'const QWaylandQtTextInputMethodPrivate "
        "*QWaylandQtTextInputMethod::d_func() const': gives "
        "'QWaylandQtTextInputMethodPrivate', which has no cute class yet.")

  @staticmethod
  def focusSurfaceDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::focusSurfaceDestroyed()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.focusSurfaceDestroyed' has no cute "
        "function yet. Qt's 'void "
        "QWaylandQtTextInputMethod::focusSurfaceDestroyed()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def focusedSurface(*__, **_) -> Never:
    """
    Qt's 'QWaylandSurface *QWaylandQtTextInputMethod::focusedSurface()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'const QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.focusedSurface' has no cute function "
        "yet. Qt's 'QWaylandSurface "
        "*QWaylandQtTextInputMethod::focusedSurface() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def inputMethodQuery(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QWaylandQtTextInputMethod::inputMethodQuery(Qt::InputMethodQuery
    property, QVariant argument) const': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'const QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.inputMethodQuery' has no cute function "
        "yet. Qt's 'QVariant "
        "QWaylandQtTextInputMethod::inputMethodQuery(Qt::InputMethodQuery "
        "property, QVariant argument) const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandQtTextInputMethod::interface()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: incomplete type
    'QWaylandQtTextInputMethodPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.interface' has no cute function yet. "
        "Qt's 'const struct wl_interface "
        "*QWaylandQtTextInputMethod::interface()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: incomplete type 'QWaylandQtTextInputMethodPrivate' named "
        "in nested name specifier.")

  @staticmethod
  def interfaceName(*__, **_) -> Never:
    """
    Qt's 'QByteArray QWaylandQtTextInputMethod::interfaceName()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: incomplete type 'QWaylandQtTextInputMethodPrivate'
    named in nested name specifier.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.interfaceName' has no cute function "
        "yet. Qt's 'QByteArray QWaylandQtTextInputMethod::interfaceName()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: incomplete type "
        "'QWaylandQtTextInputMethodPrivate' named in nested name specifier.")

  @staticmethod
  def isSurfaceEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QWaylandQtTextInputMethod::isSurfaceEnabled(QWaylandSurface
    *surface) const': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'const QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.isSurfaceEnabled' has no cute function "
        "yet. Qt's 'bool "
        "QWaylandQtTextInputMethod::isSurfaceEnabled(QWaylandSurface "
        "*surface) const': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'const QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def sendInputDirectionChanged(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::sendInputDirectionChanged()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.sendInputDirectionChanged' has no cute "
        "function yet. Qt's 'void "
        "QWaylandQtTextInputMethod::sendInputDirectionChanged()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def sendInputMethodEvent(*__, **_) -> Never:
    """
    Qt's 'void
    QWaylandQtTextInputMethod::sendInputMethodEvent(QInputMethodEvent
    *event)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.sendInputMethodEvent' has no cute "
        "function yet. Qt's 'void "
        "QWaylandQtTextInputMethod::sendInputMethodEvent(QInputMethodEvent "
        "*event)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def sendKeyEvent(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::sendKeyEvent(QKeyEvent *event)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.sendKeyEvent' has no cute function yet. "
        "Qt's 'void QWaylandQtTextInputMethod::sendKeyEvent(QKeyEvent "
        "*event)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def sendKeyboardRectangleChanged(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::sendKeyboardRectangleChanged()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.sendKeyboardRectangleChanged' has no "
        "cute function yet. Qt's 'void "
        "QWaylandQtTextInputMethod::sendKeyboardRectangleChanged()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def sendLocaleChanged(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::sendLocaleChanged()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.sendLocaleChanged' has no cute function "
        "yet. Qt's 'void QWaylandQtTextInputMethod::sendLocaleChanged()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def sendVisibleChanged(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::sendVisibleChanged()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QWaylandQtTextInputMethodPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.sendVisibleChanged' has no cute "
        "function yet. Qt's 'void "
        "QWaylandQtTextInputMethod::sendVisibleChanged()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QWaylandQtTextInputMethodPrivate'.")

  @staticmethod
  def setFocus(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::setFocus(QWaylandSurface
    *surface)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: incomplete type
    'QWaylandQtTextInputMethodPrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.setFocus' has no cute function yet. "
        "Qt's 'void QWaylandQtTextInputMethod::setFocus(QWaylandSurface "
        "*surface)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: incomplete type "
        "'QWaylandQtTextInputMethodPrivate' named in nested name specifier.")

  @staticmethod
  def surfaceDisabled(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::surfaceDisabled(QWaylandSurface
    *surface)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.surfaceDisabled' has no cute function "
        "yet. Qt's 'void "
        "QWaylandQtTextInputMethod::surfaceDisabled(QWaylandSurface "
        "*surface)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def surfaceEnabled(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQtTextInputMethod::surfaceEnabled(QWaylandSurface
    *surface)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.surfaceEnabled' has no cute function "
        "yet. Qt's 'void "
        "QWaylandQtTextInputMethod::surfaceEnabled(QWaylandSurface "
        "*surface)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def tr(*__, **_) -> Never:
    """
    Qt's 'QString QWaylandQtTextInputMethod::tr(const char *s, const char *c,
    int n)': leans on 'QWaylandQtTextInputMethod::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.tr' has no cute function yet. Qt's "
        "'QString QWaylandQtTextInputMethod::tr(const char *s, const char "
        "*c, int n)': leans on "
        "'QWaylandQtTextInputMethod::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def updateInputMethod(*__, **_) -> Never:
    """
    Qt's 'void
    QWaylandQtTextInputMethod::updateInputMethod(Qt::InputMethodQueries
    queries)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandQtTextInputMethod.updateInputMethod' has no cute function "
        "yet. Qt's 'void "
        "QWaylandQtTextInputMethod::updateInputMethod(Qt::InputMethodQueries"
        " queries)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
