"""
QWaylandTextInputV3 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandtextinputv3.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QWaylandTextInputV3(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandTextInputV3: a plain Python object standing
  in front of one C++ QWaylandTextInputV3.

  What exists
  -----------

  Every function of Qt's QWaylandTextInputV3 that has a ritual and that
  Python can call so far, 1 name in all: 'metaObject'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandTextInputV3::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandTextInputV3::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandTextInputV3Private *QWaylandTextInputV3::d_func()': gives
    'QWaylandTextInputV3Private', which has no cute class yet.
  - Qt's 'const QWaylandTextInputV3Private *QWaylandTextInputV3::d_func()
    const': gives 'QWaylandTextInputV3Private', which has no cute class yet.
  - Qt's 'QWaylandTextInputV3::~QWaylandTextInputV3()': the destructor:
    Python never removes a C++ QWaylandTextInputV3.

  What has no ritual
  ------------------

  17 of the 23 functions Qt declares: 11 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 cannot be
  called and cannot be called through the meta-object and cannot be copied; 2
  not a gap; 1 leans on 'QWaylandTextInputV3.

  What to expect
  --------------

  - The C++ QWaylandTextInputV3 is created at the first use, not by
    'QWaylandTextInputV3(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandTextInputV3.
  - Each name of Qt's QWaylandTextInputV3 that has no cute function yet,
    '__init__', 'add', 'd_func', 'focus', 'focusSurfaceDestroyed',
    'inputMethodQuery', 'interface', 'interfaceName', 'isSurfaceEnabled',
    'sendInputMethodEvent', 'sendKeyEvent', 'setFocus', 'surfaceDisabled',
    'surfaceEnabled', 'tr', 'updateInputMethod', holds a function that raises
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
  __qt_class__ = 'QWaylandTextInputV3'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandTextInputV3::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandtextinputv3.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandTextInputV3::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandTextInputV310metaObjectEv',
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
    Qt's 'QWaylandTextInputV3::QWaylandTextInputV3(QWaylandObject *container,
    QWaylandCompositor *compositor)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.__init__' has no cute function yet. Qt's "
        "'QWaylandTextInputV3::QWaylandTextInputV3(QWaylandObject "
        "*container, QWaylandCompositor *compositor)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QWaylandTextInputV3Private'.")

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
    Qt's 'void QWaylandTextInputV3::add(::wl_client *client, uint32_t id, int
    version)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.add' has no cute function yet. Qt's 'void "
        "QWaylandTextInputV3::add(::wl_client *client, uint32_t id, int "
        "version)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QWaylandTextInputV3Private'.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandTextInputV3Private *QWaylandTextInputV3::d_func()': gives
      'QWaylandTextInputV3Private', which has no cute class yet.
    - Qt's 'const QWaylandTextInputV3Private *QWaylandTextInputV3::d_func()
      const': gives 'QWaylandTextInputV3Private', which has no cute class
      yet.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.d_func' has no cute function yet. Qt's "
        "'QWaylandTextInputV3Private *QWaylandTextInputV3::d_func()': gives "
        "'QWaylandTextInputV3Private', which has no cute class yet. Qt's "
        "'const QWaylandTextInputV3Private *QWaylandTextInputV3::d_func() "
        "const': gives 'QWaylandTextInputV3Private', which has no cute "
        "class yet.")

  @staticmethod
  def focus(*__, **_) -> Never:
    """
    Qt's 'QWaylandSurface *QWaylandTextInputV3::focus() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.focus' has no cute function yet. Qt's "
        "'QWaylandSurface *QWaylandTextInputV3::focus() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QWaylandTextInputV3Private'.")

  @staticmethod
  def focusSurfaceDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInputV3::focusSurfaceDestroyed(void *a0)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.focusSurfaceDestroyed' has no cute function "
        "yet. Qt's 'void QWaylandTextInputV3::focusSurfaceDestroyed(void "
        "*a0)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QWaylandTextInputV3Private'.")

  @staticmethod
  def inputMethodQuery(*__, **_) -> Never:
    """
    Qt's 'QVariant QWaylandTextInputV3::inputMethodQuery(Qt::InputMethodQuery
    property, QVariant argument) const': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: member
    access into incomplete type 'const QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.inputMethodQuery' has no cute function yet. "
        "Qt's 'QVariant "
        "QWaylandTextInputV3::inputMethodQuery(Qt::InputMethodQuery "
        "property, QVariant argument) const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QWaylandTextInputV3Private'.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandTextInputV3::interface()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: incomplete type 'QWaylandTextInputV3Private' named
    in nested name specifier.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.interface' has no cute function yet. Qt's "
        "'const struct wl_interface *QWaylandTextInputV3::interface()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: incomplete type "
        "'QWaylandTextInputV3Private' named in nested name specifier.")

  @staticmethod
  def interfaceName(*__, **_) -> Never:
    """
    Qt's 'QByteArray QWaylandTextInputV3::interfaceName()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: incomplete type 'QWaylandTextInputV3Private' named in nested
    name specifier.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.interfaceName' has no cute function yet. Qt's "
        "'QByteArray QWaylandTextInputV3::interfaceName()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: incomplete type 'QWaylandTextInputV3Private' "
        "named in nested name specifier.")

  @staticmethod
  def isSurfaceEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QWaylandTextInputV3::isSurfaceEnabled(QWaylandSurface
    *surface) const': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'const QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.isSurfaceEnabled' has no cute function yet. "
        "Qt's 'bool QWaylandTextInputV3::isSurfaceEnabled(QWaylandSurface "
        "*surface) const': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'const QWaylandTextInputV3Private'.")

  @staticmethod
  def sendInputMethodEvent(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInputV3::sendInputMethodEvent(QInputMethodEvent
    *event)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.sendInputMethodEvent' has no cute function "
        "yet. Qt's 'void "
        "QWaylandTextInputV3::sendInputMethodEvent(QInputMethodEvent "
        "*event)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QWaylandTextInputV3Private'.")

  @staticmethod
  def sendKeyEvent(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInputV3::sendKeyEvent(QKeyEvent *event)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.sendKeyEvent' has no cute function yet. Qt's "
        "'void QWaylandTextInputV3::sendKeyEvent(QKeyEvent *event)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QWaylandTextInputV3Private'.")

  @staticmethod
  def setFocus(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInputV3::setFocus(QWaylandSurface *surface)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QWaylandTextInputV3Private'.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.setFocus' has no cute function yet. Qt's "
        "'void QWaylandTextInputV3::setFocus(QWaylandSurface *surface)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QWaylandTextInputV3Private'.")

  @staticmethod
  def surfaceDisabled(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInputV3::surfaceDisabled(QWaylandSurface
    *surface)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.surfaceDisabled' has no cute function yet. "
        "Qt's 'void QWaylandTextInputV3::surfaceDisabled(QWaylandSurface "
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
    Qt's 'void QWaylandTextInputV3::surfaceEnabled(QWaylandSurface
    *surface)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.surfaceEnabled' has no cute function yet. "
        "Qt's 'void QWaylandTextInputV3::surfaceEnabled(QWaylandSurface "
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
    Qt's 'QString QWaylandTextInputV3::tr(const char *s, const char *c, int
    n)': leans on 'QWaylandTextInputV3::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.tr' has no cute function yet. Qt's 'QString "
        "QWaylandTextInputV3::tr(const char *s, const char *c, int n)': "
        "leans on 'QWaylandTextInputV3::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateInputMethod(*__, **_) -> Never:
    """
    Qt's 'void QWaylandTextInputV3::updateInputMethod(Qt::InputMethodQueries
    queries)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWaylandTextInputV3.updateInputMethod' has no cute function yet. "
        "Qt's 'void "
        "QWaylandTextInputV3::updateInputMethod(Qt::InputMethodQueries "
        "queries)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
