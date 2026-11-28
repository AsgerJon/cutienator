"""
QOffscreenSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qoffscreensurface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSurface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize
  from . import QOffscreenSurfacePrivate, QPlatformOffscreenSurface
  from . import QPlatformSurface, QScreen, QSurfaceFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScreen = WAIT['QScreen']
  QSurfaceFormat = WAIT['QSurfaceFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOffscreenSurface(QObject, QSurface):
  """
  The cute side of Qt's QOffscreenSurface: a plain Python object standing in
  front of one C++ QOffscreenSurface.

  It is built on the cute 'QObject', as Qt's QOffscreenSurface is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QSurface' as well, as Qt's QOffscreenSurface is built on Qt's QSurface
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOffscreenSurface that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'd_func',
  'surfaceType', 'create', 'destroy', 'isValid', 'setFormat', 'format',
  'requestedFormat', 'size', 'screen', 'setScreen', 'handle',
  'screenChanged', 'screenDestroyed', 'surfaceHandle'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOffscreenSurface::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QOffscreenSurface::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QOffscreenSurfacePrivate *QOffscreenSurface::d_func() const':
    takes in Python what 'QOffscreenSurfacePrivate
    *QOffscreenSurface::d_func()' takes.
  - Qt's 'QOffscreenSurface::~QOffscreenSurface()': the destructor: Python
    never removes a C++ QOffscreenSurface.
  - Qt's 'void *QOffscreenSurface::resolveInterface(const char *name, int
    revision) const': gives 'void', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 28 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QOffscreenSurface is created at the first use, not by
    'QOffscreenSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOffscreenSurface.
  - Qt tells when it has removed the C++ QOffscreenSurface. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QOffscreenSurface that has no cute function yet,
    'nativeInterface', 'resolveInterface', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QOffscreenSurface::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#tr

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
    #  QString QOffscreenSurface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QOffscreenSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOffscreenSurface'

  #  Qt's QOffscreenSurface is built on more than one class. The part of a
  #  C++ QOffscreenSurface that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSurface': 'ritual_cast_QOffscreenSurface_QSurface',
  }

  #  A C++ QOffscreenSurface Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOffscreenSurface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOffscreenSurface::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOffscreenSurface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QOffscreenSurface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def surfaceType(self) -> QSurface.SurfaceType:
    """
    Calls Qt's 'SurfaceType QOffscreenSurface::surfaceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#surfaceType

    Returns
    -------

    QSurface.SurfaceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSurface.SurfaceType(number)' gives.
    """
    #  SurfaceType QOffscreenSurface::surfaceType() const
    ritual = 'ritual_ZNK17QOffscreenSurface11surfaceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QOffscreenSurface11surfaceTypeEv'
    return QSurface.SurfaceType(self.uglySide.call(ritual))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOffscreenSurface::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#isValid
    """
    #  bool QOffscreenSurface::isValid() const
    return self.uglySide.call('ritual_ZNK17QOffscreenSurface7isValidEv')

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QOffscreenSurface::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QOffscreenSurface::format() const
    ritual = 'ritual_ZNK17QOffscreenSurface6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QOffscreenSurface6formatEv'
    address = self.uglySide.call(ritual)
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def requestedFormat(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QOffscreenSurface::requestedFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoffscreensurface.html#requestedFormat

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QOffscreenSurface::requestedFormat() const
    address = self.uglySide.call(
        'ritual_ZNK17QOffscreenSurface15requestedFormatEv',
    )
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QOffscreenSurface::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QOffscreenSurface::size() const
    ritual = 'ritual_ZNK17QOffscreenSurface4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QOffscreenSurface4sizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def screen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QOffscreenSurface::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#screen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QOffscreenSurface::screen() const
    address = self.uglySide.call('ritual_ZNK17QOffscreenSurface6screenEv')
    from . import QScreen
    return QScreen._cuteAt(address)

  def handle(self) -> Optional[QPlatformOffscreenSurface]:
    """
    Calls Qt's 'QPlatformOffscreenSurface *QOffscreenSurface::handle()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#handle

    Returns
    -------

    Optional[QPlatformOffscreenSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformOffscreenSurface *QOffscreenSurface::handle() const
    address = self.uglySide.call('ritual_ZNK17QOffscreenSurface6handleEv')
    from . import QPlatformOffscreenSurface
    return QPlatformOffscreenSurface._cuteAt(address)

  def surfaceHandle(self) -> Optional[QPlatformSurface]:
    """
    Calls Qt's 'QPlatformSurface *QOffscreenSurface::surfaceHandle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoffscreensurface.html#surfaceHandle

    Returns
    -------

    Optional[QPlatformSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformSurface *QOffscreenSurface::surfaceHandle() const
    ritual = 'ritual_ZNK17QOffscreenSurface13surfaceHandleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QOffscreenSurface13surfaceHandleEv'
    address = self.uglySide.call(ritual)
    from . import QPlatformSurface
    return QPlatformSurface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSurfaceFormat)
  def setFormat(self, format: QSurfaceFormat) -> None:
    """
    Calls Qt's 'void QOffscreenSurface::setFormat(const QSurfaceFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#setFormat

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  void QOffscreenSurface::setFormat(const QSurfaceFormat &format)
    self.uglySide.call(
        'ritual_ZN17QOffscreenSurface9setFormatERK14QSurfaceFormat',
        self._valueOf(format),
    )

  @overload(QScreen)
  @overload(NoneType)
  def setScreen(self, screen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QOffscreenSurface::setScreen(QScreen *screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#setScreen

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOffscreenSurface::setScreen(QScreen *screen)
    self.uglySide.call(
        'ritual_ZN17QOffscreenSurface9setScreenEP7QScreen',
        self._addressOf(screen),
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

  @overload()
  @overload(QScreen)
  @overload(NoneType)
  @overload(QScreen, QObject)
  @overload(QScreen, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      screen: Optional[QScreen] = None,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOffscreenSurface::QOffscreenSurface(QScreen *screen, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoffscreensurface.html#QOffscreenSurface

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOffscreenSurface::QOffscreenSurface(QScreen *screen, QObject *parent)
    self._noteCreation(QOffscreenSurface, lambda: Rituals.call(
        'ritual_ZN17QOffscreenSurfaceC1EP7QScreenP7QObject',
        self._addressOf(screen), self._addressOf(parent, 'QObject'),
    ))

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

  def d_func(self) -> Optional[QOffscreenSurfacePrivate]:
    """
    Calls Qt's 'QOffscreenSurfacePrivate *QOffscreenSurface::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#d_func

    Returns
    -------

    Optional[QOffscreenSurfacePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOffscreenSurfacePrivate *QOffscreenSurface::d_func()
    address = self.uglySide.call('ritual_ZN17QOffscreenSurface6d_funcEv')
    from . import QOffscreenSurfacePrivate
    return QOffscreenSurfacePrivate._cuteAt(address)

  def create(self) -> None:
    """
    Calls Qt's 'void QOffscreenSurface::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#create
    """
    #  void QOffscreenSurface::create()
    self.uglySide.call('ritual_ZN17QOffscreenSurface6createEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QOffscreenSurface::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qoffscreensurface.html#destroy
    """
    #  void QOffscreenSurface::destroy()
    self.uglySide.call('ritual_ZN17QOffscreenSurface7destroyEv')

  @overload(QScreen)
  @overload(NoneType)
  def screenChanged(self, screen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QOffscreenSurface::screenChanged(QScreen *screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoffscreensurface.html#screenChanged

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOffscreenSurface::screenChanged(QScreen *screen)
    self.uglySide.call(
        'ritual_ZN17QOffscreenSurface13screenChangedEP7QScreen',
        self._addressOf(screen),
    )

  @overload(QObject)
  @overload(NoneType)
  def screenDestroyed(self, screen: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QOffscreenSurface::screenDestroyed(QObject *screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoffscreensurface.html#screenDestroyed

    Parameters
    ----------

    screen : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOffscreenSurface::screenDestroyed(QObject *screen)
    self.uglySide.call(
        'ritual_ZN17QOffscreenSurface15screenDestroyedEP7QObject',
        self._addressOf(screen, 'QObject'),
    )

  @staticmethod
  def nativeInterface(*__, **_) -> Never:
    """
    Qt's 'QOffscreenSurface::nativeInterface': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QOffscreenSurface.nativeInterface' has no cute function yet. Qt's "
        "'QOffscreenSurface::nativeInterface': a template: a pattern and no "
        "single function.")

  @staticmethod
  def resolveInterface(*__, **_) -> Never:
    """
    Qt's 'void *QOffscreenSurface::resolveInterface(const char *name, int
    revision) const': gives 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOffscreenSurface.resolveInterface' has no cute function yet. "
        "Qt's 'void *QOffscreenSurface::resolveInterface(const char *name, "
        "int revision) const': gives 'void', which has no cute class yet.")
