"""
QWaylandTextInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandtextinput.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QWaylandTextInput(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandTextInput: a plain Python object standing in
  front of one C++ QWaylandTextInput.

  What exists
  -----------

  Every function of Qt's QWaylandTextInput that has a ritual and that Python
  can call so far, 1 name in all: 'metaObject'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandTextInput::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandTextInput::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandTextInputPrivate *QWaylandTextInput::d_func()': gives
    'QWaylandTextInputPrivate', which has no cute class yet.
  - Qt's 'const QWaylandTextInputPrivate *QWaylandTextInput::d_func() const':
    gives 'QWaylandTextInputPrivate', which has no cute class yet.
  - Qt's 'QWaylandTextInput::~QWaylandTextInput()': the destructor: Python
    never removes a C++ QWaylandTextInput.

  What has no ritual
  ------------------

  21 of the 27 functions Qt declares: 15 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 cannot be
  called and cannot be called through the meta-object and cannot be copied; 2
  not a gap; 1 leans on 'QWaylandTextInput.

  What to expect
  --------------

  - The C++ QWaylandTextInput is created at the first use, not by
    'QWaylandTextInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandTextInput.
  - Each name of Qt's QWaylandTextInput that has no cute function yet,
    '__init__', 'add', 'd_func', 'focus', 'focusSurfaceDestroyed',
    'inputMethodQuery', 'interface', 'interfaceName', 'isSurfaceEnabled',
    'sendInputMethodEvent', 'sendInputPanelState', 'sendKeyEvent',
    'sendLocale', 'sendModifiersMap', 'sendTextDirection', 'setFocus',
    'surfaceDisabled', 'surfaceEnabled', 'tr', 'updateInputMethod', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandTextInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandTextInput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtextinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandTextInput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QWaylandTextInput10metaObjectEv',
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
    Qt's 'QWaylandTextInput::QWaylandTextInput(QWaylandObject *container,
    QWaylandCompositor *compositor)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.__init__' has no cute function yet. Qt's "
        "'QWaylandTextInput::QWaylandTextInput(QWaylandObject *container, "
        "QWaylandCompositor *compositor)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QWaylandTextInputPrivate'.")

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
    Qt's 'void QWaylandTextInput::add(::wl_client *client, uint32_t id, int
    version)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.add' has no cute function yet. Qt's 'void "
        "QWaylandTextInput::add(::wl_client *client, uint32_t id, int "
        "version)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QWaylandTextInputPrivate'.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandTextInputPrivate *QWaylandTextInput::d_func()': gives
      'QWaylandTextInputPrivate', which has no cute class yet.
    - Qt's 'const QWaylandTextInputPrivate *QWaylandTextInput::d_func()
      const': gives 'QWaylandTextInputPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.d_func' has no cute function yet. Qt's "
        "'QWaylandTextInputPrivate *QWaylandTextInput::d_func()': gives "
        "'QWaylandTextInputPrivate', which has no cute class yet. Qt's "
        "'const QWaylandTextInputPrivate *QWaylandTextInput::d_func() "
        "const': gives 'QWaylandTextInputPrivate', which has no cute class "
        "yet.")

  @staticmethod
  def focus(*__, **_) -> Never:
    """
    Qt's 'QWaylandSurface *QWaylandTextInput::focus() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.focus' has no cute function yet. Qt's "
        "'QWaylandSurface *QWaylandTextInput::focus() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QWaylandTextInputPrivate'.")

  @staticmethod
  def focusSurfaceDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::focusSurfaceDestroyed(void *a0)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.focusSurfaceDestroyed' has no cute function "
        "yet. Qt's 'void QWaylandTextInput::focusSurfaceDestroyed(void "
        "*a0)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QWaylandTextInputPrivate'.")

  @staticmethod
  def inputMethodQuery(*__, **_) -> Never:
    """
    Qt's 'QVariant QWaylandTextInput::inputMethodQuery(Qt::InputMethodQuery
    property, QVariant argument) const': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'const QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.inputMethodQuery' has no cute function yet. "
        "Qt's 'QVariant "
        "QWaylandTextInput::inputMethodQuery(Qt::InputMethodQuery property, "
        "QVariant argument) const': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const "
        "QWaylandTextInputPrivate'.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandTextInput::interface()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: incomplete type 'QWaylandTextInputPrivate' named in
    nested name specifier.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.interface' has no cute function yet. Qt's "
        "'const struct wl_interface *QWaylandTextInput::interface()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: incomplete type "
        "'QWaylandTextInputPrivate' named in nested name specifier.")

  @staticmethod
  def interfaceName(*__, **_) -> Never:
    """
    Qt's 'QByteArray QWaylandTextInput::interfaceName()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: incomplete type 'QWaylandTextInputPrivate' named in nested name
    specifier.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.interfaceName' has no cute function yet. Qt's "
        "'QByteArray QWaylandTextInput::interfaceName()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: incomplete type 'QWaylandTextInputPrivate' named in "
        "nested name specifier.")

  @staticmethod
  def isSurfaceEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QWaylandTextInput::isSurfaceEnabled(QWaylandSurface *surface)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'const QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.isSurfaceEnabled' has no cute function yet. "
        "Qt's 'bool QWaylandTextInput::isSurfaceEnabled(QWaylandSurface "
        "*surface) const': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'const QWaylandTextInputPrivate'.")

  @staticmethod
  def sendInputMethodEvent(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::sendInputMethodEvent(QInputMethodEvent
    *event)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.sendInputMethodEvent' has no cute function yet. "
        "Qt's 'void "
        "QWaylandTextInput::sendInputMethodEvent(QInputMethodEvent "
        "*event)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QWaylandTextInputPrivate'.")

  @staticmethod
  def sendInputPanelState(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::sendInputPanelState()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.sendInputPanelState' has no cute function yet. "
        "Qt's 'void QWaylandTextInput::sendInputPanelState()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QWaylandTextInputPrivate'.")

  @staticmethod
  def sendKeyEvent(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::sendKeyEvent(QKeyEvent *event)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.sendKeyEvent' has no cute function yet. Qt's "
        "'void QWaylandTextInput::sendKeyEvent(QKeyEvent *event)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QWaylandTextInputPrivate'.")

  @staticmethod
  def sendLocale(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::sendLocale()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.sendLocale' has no cute function yet. Qt's "
        "'void QWaylandTextInput::sendLocale()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type "
        "'QWaylandTextInputPrivate'.")

  @staticmethod
  def sendModifiersMap(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::sendModifiersMap(const QByteArray
    &modifiersMap)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.sendModifiersMap' has no cute function yet. "
        "Qt's 'void QWaylandTextInput::sendModifiersMap(const QByteArray "
        "&modifiersMap)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QWaylandTextInputPrivate'.")

  @staticmethod
  def sendTextDirection(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::sendTextDirection()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.sendTextDirection' has no cute function yet. "
        "Qt's 'void QWaylandTextInput::sendTextDirection()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QWaylandTextInputPrivate'.")

  @staticmethod
  def setFocus(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::setFocus(QWaylandSurface *surface)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QWaylandTextInputPrivate'.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.setFocus' has no cute function yet. Qt's 'void "
        "QWaylandTextInput::setFocus(QWaylandSurface *surface)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QWaylandTextInputPrivate'.")

  @staticmethod
  def surfaceDisabled(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::surfaceDisabled(QWaylandSurface *surface)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.surfaceDisabled' has no cute function yet. Qt's "
        "'void QWaylandTextInput::surfaceDisabled(QWaylandSurface "
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
    Qt's 'void QWaylandTextInput::surfaceEnabled(QWaylandSurface *surface)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.surfaceEnabled' has no cute function yet. Qt's "
        "'void QWaylandTextInput::surfaceEnabled(QWaylandSurface "
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
    Qt's 'QString QWaylandTextInput::tr(const char *s, const char *c, int
    n)': leans on 'QWaylandTextInput::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.tr' has no cute function yet. Qt's 'QString "
        "QWaylandTextInput::tr(const char *s, const char *c, int n)': leans "
        "on 'QWaylandTextInput::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateInputMethod(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInput::updateInputMethod(Qt::InputMethodQueries
    queries)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandTextInput.updateInputMethod' has no cute function yet. "
        "Qt's 'void "
        "QWaylandTextInput::updateInputMethod(Qt::InputMethodQueries "
        "queries)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
