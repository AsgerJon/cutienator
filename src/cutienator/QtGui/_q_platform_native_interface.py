"""
QPlatformNativeInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformnativeinterface.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QPlatformWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformWindow = WAIT['QPlatformWindow']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformNativeInterface(QObject):
  """
  The cute side of Qt's QPlatformNativeInterface: a plain Python object
  standing in front of one C++ QPlatformNativeInterface.

  It is built on the cute 'QObject', as Qt's QPlatformNativeInterface is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformNativeInterface that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'windowProperties', 'windowProperty', 'setWindowProperty',
  'windowPropertyChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformNativeInterface::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformNativeInterface::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void *QPlatformNativeInterface::nativeResourceForIntegration(const
    QByteArray &resource)': gives 'void', which has no cute class yet.
  - Qt's 'void *QPlatformNativeInterface::nativeResourceForContext(const
    QByteArray &resource, QOpenGLContext *context)': gives 'void', which has
    no cute class yet.
  - Qt's 'void *QPlatformNativeInterface::nativeResourceForScreen(const
    QByteArray &resource, QScreen *screen)': gives 'void', which has no cute
    class yet.
  - Qt's 'void *QPlatformNativeInterface::nativeResourceForWindow(const
    QByteArray &resource, QWindow *window)': gives 'void', which has no cute
    class yet.
  - Qt's 'void *QPlatformNativeInterface::nativeResourceForBackingStore(const
    QByteArray &resource, QBackingStore *backingStore)': gives 'void', which
    has no cute class yet.
  - Qt's 'void *QPlatformNativeInterface::nativeResourceForCursor(const
    QByteArray &resource, const QCursor &cursor)': gives 'void', which has no
    cute class yet.
  - Qt's 'NativeResourceForIntegrationFunction
    QPlatformNativeInterface::nativeResourceFunctionForIntegration(const
    QByteArray &resource)': gives a type Python has no way to take yet.
  - Qt's 'NativeResourceForContextFunction
    QPlatformNativeInterface::nativeResourceFunctionForContext(const
    QByteArray &resource)': gives a type Python has no way to take yet.
  - Qt's 'NativeResourceForScreenFunction
    QPlatformNativeInterface::nativeResourceFunctionForScreen(const
    QByteArray &resource)': gives a type Python has no way to take yet.
  - Qt's 'NativeResourceForWindowFunction
    QPlatformNativeInterface::nativeResourceFunctionForWindow(const
    QByteArray &resource)': gives a type Python has no way to take yet.
  - Qt's 'NativeResourceForBackingStoreFunction
    QPlatformNativeInterface::nativeResourceFunctionForBackingStore(const
    QByteArray &resource)': gives a type Python has no way to take yet.
  - Qt's 'QFunctionPointer QPlatformNativeInterface::platformFunction(const
    QByteArray &function) const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformNativeInterface is created at the first use, not by
    'QPlatformNativeInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformNativeInterface.
  - Qt tells when it has removed the C++ QPlatformNativeInterface. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformNativeInterface that has no cute function yet,
    'nativeResourceForBackingStore', 'nativeResourceForContext',
    'nativeResourceForCursor', 'nativeResourceForIntegration',
    'nativeResourceForScreen', 'nativeResourceForWindow',
    'nativeResourceFunctionForBackingStore',
    'nativeResourceFunctionForContext',
    'nativeResourceFunctionForIntegration',
    'nativeResourceFunctionForScreen', 'nativeResourceFunctionForWindow',
    'platformFunction', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QPlatformNativeInterface::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformnativeinterface.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformNativeInterface::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QPlatformNativeInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformNativeInterface'

  #  A C++ QPlatformNativeInterface Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformNativeInterface'

  #  The functions Qt calls itself that QPlatformNativeInterface is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'nativeResourceForIntegration': (
          'void '
          '*QPlatformNativeInterface::nativeResourceForIntegration(const '
          'QByteArray &)',
      ),
      'nativeResourceForContext': (
          'void *QPlatformNativeInterface::nativeResourceForContext(const '
          'QByteArray &, QOpenGLContext *)',
      ),
      'nativeResourceForScreen': (
          'void *QPlatformNativeInterface::nativeResourceForScreen(const '
          'QByteArray &, QScreen *)',
      ),
      'nativeResourceForWindow': (
          'void *QPlatformNativeInterface::nativeResourceForWindow(const '
          'QByteArray &, QWindow *)',
      ),
      'nativeResourceForBackingStore': (
          'void '
          '*QPlatformNativeInterface::nativeResourceForBackingStore(const '
          'QByteArray &, QBackingStore *)',
      ),
      'nativeResourceForCursor': (
          'void *QPlatformNativeInterface::nativeResourceForCursor(const '
          'QByteArray &, const QCursor &)',
      ),
      'nativeResourceFunctionForIntegration': (
          'NativeResourceForIntegrationFunction '
          'QPlatformNativeInterface::nativeResourceFunctionForIntegration(c'
          'onst QByteArray &)',
      ),
      'nativeResourceFunctionForContext': (
          'NativeResourceForContextFunction '
          'QPlatformNativeInterface::nativeResourceFunctionForContext(const'
          ' QByteArray &)',
      ),
      'nativeResourceFunctionForScreen': (
          'NativeResourceForScreenFunction '
          'QPlatformNativeInterface::nativeResourceFunctionForScreen(const '
          'QByteArray &)',
      ),
      'nativeResourceFunctionForWindow': (
          'NativeResourceForWindowFunction '
          'QPlatformNativeInterface::nativeResourceFunctionForWindow(const '
          'QByteArray &)',
      ),
      'nativeResourceFunctionForBackingStore': (
          'NativeResourceForBackingStoreFunction '
          'QPlatformNativeInterface::nativeResourceFunctionForBackingStore('
          'const QByteArray &)',
      ),
      'platformFunction': (
          'QFunctionPointer '
          'QPlatformNativeInterface::platformFunction(const QByteArray &) '
          'const',
      ),
      'windowProperties': (
          'QVariantMap '
          'QPlatformNativeInterface::windowProperties(QPlatformWindow *) '
          'const',
      ),
  }

  #  The functions Qt calls itself that QPlatformNativeInterface is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'windowProperty': (
          ('_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWind'
           'owRK7QString',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'address', 'QtGui:QPlatformWindow'),
               ('address', 'text', ''),
           )),
          ('_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformWind'
           'owRK7QStringRK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'address', 'QtGui:QPlatformWindow'),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'setWindowProperty': (
          ('_ZN24QPlatformNativeInterface17setWindowPropertyEP15QPlatformWi'
           'ndowRK7QStringRK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformWindow'),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlatformNativeInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformnativeinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformNativeInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QPlatformNativeInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QPlatformWindow)
  @overload(NoneType)
  def windowProperties(
      self,
      window: Optional[QPlatformWindow],
  ) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap
    QPlatformNativeInterface::windowProperties(QPlatformWindow *window)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformnativeinterface.html#windowProperties

    Parameters
    ----------

    window : Optional[QPlatformWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QPlatformNativeInterface::windowProperties(QPlatformWindow
    #      *window) const
    address = self.uglySide.call(
        'ritual_ZNK24QPlatformNativeInterface16windowPropertiesEP15QPlatfor'
        'mWindow',
        self._addressOf(window),
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(QPlatformWindow, str)
  @overload(NoneType, str)
  def windowProperty(
      self,
      window: Optional[QPlatformWindow],
      name: str,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QPlatformNativeInterface::windowProperty(QPlatformWindow *window, const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformnativeinterface.html#windowProperty

    Parameters
    ----------

    window : Optional[QPlatformWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
    #      *window, const QString &name) const
    ritual = (
        'ritual_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformW'
        'indowRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QPlatformNativeInterface14windowPropertyEP15QPla'
          'tformWindowRK7QString')
    address = self.uglySide.call(ritual, self._addressOf(window), name)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QPlatformWindow, str, QVariant)
  @overload(NoneType, str, QVariant)
  def windowProperty(
      self,
      window: Optional[QPlatformWindow],
      name: str,
      defaultValue: QVariant,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QPlatformNativeInterface::windowProperty(QPlatformWindow *window, const
    QString &name, const QVariant &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformnativeinterface.html#windowProperty

    Parameters
    ----------

    window : Optional[QPlatformWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlatformNativeInterface::windowProperty(QPlatformWindow
    #      *window, const QString &name, const QVariant &defaultValue) const
    ritual = (
        'ritual_ZNK24QPlatformNativeInterface14windowPropertyEP15QPlatformW'
        'indowRK7QStringRK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QPlatformNativeInterface14windowPropertyEP15QPla'
          'tformWindowRK7QStringRK8QVariant')
    address = self.uglySide.call(
        ritual, self._addressOf(window), name, self._valueOf(defaultValue),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlatformWindow, str, QVariant)
  @overload(NoneType, str, QVariant)
  def setWindowProperty(
      self,
      window: Optional[QPlatformWindow],
      name: str,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformNativeInterface::setWindowProperty(QPlatformWindow *window,
    const QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformnativeinterface.html#setWindowProperty

    Parameters
    ----------

    window : Optional[QPlatformWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPlatformNativeInterface::setWindowProperty(QPlatformWindow
    #      *window, const QString &name, const QVariant &value)
    ritual = (
        'ritual_ZN24QPlatformNativeInterface17setWindowPropertyEP15QPlatfor'
        'mWindowRK7QStringRK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QPlatformNativeInterface17setWindowPropertyEP15QP'
          'latformWindowRK7QStringRK8QVariant')
    self.uglySide.call(
        ritual, self._addressOf(window), name, self._valueOf(value),
    )

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

  @overload(QPlatformWindow, str)
  @overload(NoneType, str)
  def windowPropertyChanged(
      self,
      window: Optional[QPlatformWindow],
      propertyName: str,
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformNativeInterface::windowPropertyChanged(QPlatformWindow *window,
    const QString &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformnativeinterface.html

    Parameters
    ----------

    window : Optional[QPlatformWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformNativeInterface::windowPropertyChanged(QPlatformWindow
    #      *window, const QString &propertyName)
    self.uglySide.call(
        'ritual_ZN24QPlatformNativeInterface21windowPropertyChangedEP15QPla'
        'tformWindowRK7QString',
        self._addressOf(window), propertyName,
    )

  @staticmethod
  def nativeResourceForBackingStore(*__, **_) -> Never:
    """
    Qt's 'void *QPlatformNativeInterface::nativeResourceForBackingStore(const
    QByteArray &resource, QBackingStore *backingStore)': gives 'void', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceForBackingStore' has no "
        "cute function yet. Qt's 'void "
        "*QPlatformNativeInterface::nativeResourceForBackingStore(const "
        "QByteArray &resource, QBackingStore *backingStore)': gives 'void', "
        "which has no cute class yet.")

  @staticmethod
  def nativeResourceForContext(*__, **_) -> Never:
    """
    Qt's 'void *QPlatformNativeInterface::nativeResourceForContext(const
    QByteArray &resource, QOpenGLContext *context)': gives 'void', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceForContext' has no cute "
        "function yet. Qt's 'void "
        "*QPlatformNativeInterface::nativeResourceForContext(const "
        "QByteArray &resource, QOpenGLContext *context)': gives 'void', "
        "which has no cute class yet.")

  @staticmethod
  def nativeResourceForCursor(*__, **_) -> Never:
    """
    Qt's 'void *QPlatformNativeInterface::nativeResourceForCursor(const
    QByteArray &resource, const QCursor &cursor)': gives 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceForCursor' has no cute "
        "function yet. Qt's 'void "
        "*QPlatformNativeInterface::nativeResourceForCursor(const "
        "QByteArray &resource, const QCursor &cursor)': gives 'void', which "
        "has no cute class yet.")

  @staticmethod
  def nativeResourceForIntegration(*__, **_) -> Never:
    """
    Qt's 'void *QPlatformNativeInterface::nativeResourceForIntegration(const
    QByteArray &resource)': gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceForIntegration' has no "
        "cute function yet. Qt's 'void "
        "*QPlatformNativeInterface::nativeResourceForIntegration(const "
        "QByteArray &resource)': gives 'void', which has no cute class yet.")

  @staticmethod
  def nativeResourceForScreen(*__, **_) -> Never:
    """
    Qt's 'void *QPlatformNativeInterface::nativeResourceForScreen(const
    QByteArray &resource, QScreen *screen)': gives 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceForScreen' has no cute "
        "function yet. Qt's 'void "
        "*QPlatformNativeInterface::nativeResourceForScreen(const "
        "QByteArray &resource, QScreen *screen)': gives 'void', which has "
        "no cute class yet.")

  @staticmethod
  def nativeResourceForWindow(*__, **_) -> Never:
    """
    Qt's 'void *QPlatformNativeInterface::nativeResourceForWindow(const
    QByteArray &resource, QWindow *window)': gives 'void', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceForWindow' has no cute "
        "function yet. Qt's 'void "
        "*QPlatformNativeInterface::nativeResourceForWindow(const "
        "QByteArray &resource, QWindow *window)': gives 'void', which has "
        "no cute class yet.")

  @staticmethod
  def nativeResourceFunctionForBackingStore(*__, **_) -> Never:
    """
    Qt's 'NativeResourceForBackingStoreFunction
    QPlatformNativeInterface::nativeResourceFunctionForBackingStore(const
    QByteArray &resource)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceFunctionForBackingStore' "
        "has no cute function yet. Qt's "
        "'NativeResourceForBackingStoreFunction "
        "QPlatformNativeInterface::nativeResourceFunctionForBackingStore(con"
        "st QByteArray &resource)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def nativeResourceFunctionForContext(*__, **_) -> Never:
    """
    Qt's 'NativeResourceForContextFunction
    QPlatformNativeInterface::nativeResourceFunctionForContext(const
    QByteArray &resource)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceFunctionForContext' has no "
        "cute function yet. Qt's 'NativeResourceForContextFunction "
        "QPlatformNativeInterface::nativeResourceFunctionForContext(const "
        "QByteArray &resource)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def nativeResourceFunctionForIntegration(*__, **_) -> Never:
    """
    Qt's 'NativeResourceForIntegrationFunction
    QPlatformNativeInterface::nativeResourceFunctionForIntegration(const
    QByteArray &resource)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceFunctionForIntegration' "
        "has no cute function yet. Qt's "
        "'NativeResourceForIntegrationFunction "
        "QPlatformNativeInterface::nativeResourceFunctionForIntegration(cons"
        "t QByteArray &resource)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def nativeResourceFunctionForScreen(*__, **_) -> Never:
    """
    Qt's 'NativeResourceForScreenFunction
    QPlatformNativeInterface::nativeResourceFunctionForScreen(const
    QByteArray &resource)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceFunctionForScreen' has no "
        "cute function yet. Qt's 'NativeResourceForScreenFunction "
        "QPlatformNativeInterface::nativeResourceFunctionForScreen(const "
        "QByteArray &resource)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def nativeResourceFunctionForWindow(*__, **_) -> Never:
    """
    Qt's 'NativeResourceForWindowFunction
    QPlatformNativeInterface::nativeResourceFunctionForWindow(const
    QByteArray &resource)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.nativeResourceFunctionForWindow' has no "
        "cute function yet. Qt's 'NativeResourceForWindowFunction "
        "QPlatformNativeInterface::nativeResourceFunctionForWindow(const "
        "QByteArray &resource)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def platformFunction(*__, **_) -> Never:
    """
    Qt's 'QFunctionPointer QPlatformNativeInterface::platformFunction(const
    QByteArray &function) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformNativeInterface.platformFunction' has no cute function "
        "yet. Qt's 'QFunctionPointer "
        "QPlatformNativeInterface::platformFunction(const QByteArray "
        "&function) const': gives a type Python has no way to take yet.")
