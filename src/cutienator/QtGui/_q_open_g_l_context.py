"""
QOpenGLContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qopenglcontext.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QOpenGLContextGroup, QOpenGLExtraFunctions, QOpenGLFunctions
  from . import QScreen, QSurface, QSurfaceFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QScreen = WAIT['QScreen']
  QSurface = WAIT['QSurface']
  QSurfaceFormat = WAIT['QSurfaceFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLContext(QObject):
  """
  The cute side of Qt's QOpenGLContext: a plain Python object standing in
  front of one C++ QOpenGLContext.

  It is built on the cute 'QObject', as Qt's QOpenGLContext is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLContext that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'setFormat',
  'setShareContext', 'setScreen', 'create', 'isValid', 'format',
  'shareContext', 'shareGroup', 'screen', 'makeCurrent', 'doneCurrent',
  'swapBuffers', 'surface', 'currentContext', 'areSharing', 'functions',
  'extraFunctions', 'hasExtension', 'openGLModuleType', 'isOpenGLES',
  'supportsThreadedOpenGL', 'globalShareContext'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLContext::~QOpenGLContext()': the destructor: Python never
    removes a C++ QOpenGLContext.

  What has no ritual
  ------------------

  18 of the 44 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 6 private; 2 a template; 1 protected; 1 a signal.

  What to expect
  --------------

  - The C++ QOpenGLContext is created at the first use, not by
    'QOpenGLContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLContext.
  - Qt tells when it has removed the C++ QOpenGLContext. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QOpenGLContext, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class OpenGLModuleType(CuteNum):
    """
    The enum 'QOpenGLContext::OpenGLModuleType' of Qt, with the 2 names Qt
    gives in it.
    """

    LibGL = Kee[int](0)
    LibGLES = Kee[int](1)

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
    Calls Qt's 'QString QOpenGLContext::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#tr

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
    #  QString QOpenGLContext::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QOpenGLContext2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def currentContext() -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLContext::currentContext()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#currentContext

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLContext::currentContext()
    address = Rituals.call('ritual_ZN14QOpenGLContext14currentContextEv')
    return QOpenGLContext._cuteAt(address)

  @staticmethod
  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def areSharing(
      first: Optional[QOpenGLContext],
      second: Optional[QOpenGLContext],
  ) -> bool:
    """
    Calls Qt's 'bool QOpenGLContext::areSharing(QOpenGLContext *first,
    QOpenGLContext *second)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#areSharing

    Parameters
    ----------

    first : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    second : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLContext::areSharing(QOpenGLContext *first, QOpenGLContext
    #      *second)
    return Rituals.call(
        'ritual_ZN14QOpenGLContext10areSharingEPS_S0_',
        CuteMixin._addressOf(first), CuteMixin._addressOf(second),
    )

  @staticmethod
  def openGLModuleType() -> OpenGLModuleType:
    """
    Calls Qt's 'OpenGLModuleType QOpenGLContext::openGLModuleType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontext.html#openGLModuleType

    Returns
    -------

    OpenGLModuleType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'OpenGLModuleType(number)'
      gives.
    """
    #  OpenGLModuleType QOpenGLContext::openGLModuleType()
    return QOpenGLContext.OpenGLModuleType(Rituals.call(
        'ritual_ZN14QOpenGLContext16openGLModuleTypeEv',
    ))

  @staticmethod
  def supportsThreadedOpenGL() -> bool:
    """
    Calls Qt's 'bool QOpenGLContext::supportsThreadedOpenGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontext.html#supportsThreadedOpenGL
    """
    #  bool QOpenGLContext::supportsThreadedOpenGL()
    return Rituals.call(
        'ritual_ZN14QOpenGLContext22supportsThreadedOpenGLEv',
    )

  @staticmethod
  def globalShareContext() -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLContext::globalShareContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontext.html#globalShareContext

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLContext::globalShareContext()
    address = Rituals.call('ritual_ZN14QOpenGLContext18globalShareContextEv')
    return QOpenGLContext._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLContext::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLContext::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QOpenGLContext10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLContext::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#isValid
    """
    #  bool QOpenGLContext::isValid() const
    return self.uglySide.call('ritual_ZNK14QOpenGLContext7isValidEv')

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QOpenGLContext::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QOpenGLContext::format() const
    address = self.uglySide.call('ritual_ZNK14QOpenGLContext6formatEv')
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  def shareContext(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QOpenGLContext::shareContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#shareContext

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QOpenGLContext::shareContext() const
    address = self.uglySide.call(
        'ritual_ZNK14QOpenGLContext12shareContextEv',
    )
    return QOpenGLContext._cuteAt(address)

  def shareGroup(self) -> Optional[QOpenGLContextGroup]:
    """
    Calls Qt's 'QOpenGLContextGroup *QOpenGLContext::shareGroup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#shareGroup

    Returns
    -------

    Optional[QOpenGLContextGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContextGroup *QOpenGLContext::shareGroup() const
    address = self.uglySide.call('ritual_ZNK14QOpenGLContext10shareGroupEv')
    from . import QOpenGLContextGroup
    return QOpenGLContextGroup._cuteAt(address)

  def screen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QOpenGLContext::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#screen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QOpenGLContext::screen() const
    address = self.uglySide.call('ritual_ZNK14QOpenGLContext6screenEv')
    from . import QScreen
    return QScreen._cuteAt(address)

  def surface(self) -> Optional[QSurface]:
    """
    Calls Qt's 'QSurface *QOpenGLContext::surface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#surface

    Returns
    -------

    Optional[QSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface *QOpenGLContext::surface() const
    address = self.uglySide.call('ritual_ZNK14QOpenGLContext7surfaceEv')
    from . import QSurface
    return QSurface._cuteAt(address)

  def functions(self) -> Optional[QOpenGLFunctions]:
    """
    Calls Qt's 'QOpenGLFunctions *QOpenGLContext::functions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#functions

    Returns
    -------

    Optional[QOpenGLFunctions]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLFunctions *QOpenGLContext::functions() const
    address = self.uglySide.call('ritual_ZNK14QOpenGLContext9functionsEv')
    from . import QOpenGLFunctions
    return QOpenGLFunctions._cuteAt(address)

  def extraFunctions(self) -> Optional[QOpenGLExtraFunctions]:
    """
    Calls Qt's 'QOpenGLExtraFunctions *QOpenGLContext::extraFunctions()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#extraFunctions

    Returns
    -------

    Optional[QOpenGLExtraFunctions]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLExtraFunctions *QOpenGLContext::extraFunctions() const
    address = self.uglySide.call(
        'ritual_ZNK14QOpenGLContext14extraFunctionsEv',
    )
    from . import QOpenGLExtraFunctions
    return QOpenGLExtraFunctions._cuteAt(address)

  @overload(QByteArray)
  def hasExtension(self, extension: QByteArray) -> bool:
    """
    Calls Qt's 'bool QOpenGLContext::hasExtension(const QByteArray
    &extension) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#hasExtension

    Parameters
    ----------

    extension : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QOpenGLContext::hasExtension(const QByteArray &extension) const
    return self.uglySide.call(
        'ritual_ZNK14QOpenGLContext12hasExtensionERK10QByteArray',
        self._valueOf(extension),
    )

  def isOpenGLES(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLContext::isOpenGLES() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#isOpenGLES
    """
    #  bool QOpenGLContext::isOpenGLES() const
    return self.uglySide.call('ritual_ZNK14QOpenGLContext10isOpenGLESEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSurfaceFormat)
  def setFormat(self, format: QSurfaceFormat) -> None:
    """
    Calls Qt's 'void QOpenGLContext::setFormat(const QSurfaceFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#setFormat

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  void QOpenGLContext::setFormat(const QSurfaceFormat &format)
    self.uglySide.call(
        'ritual_ZN14QOpenGLContext9setFormatERK14QSurfaceFormat',
        self._valueOf(format),
    )

  @overload(THIS)
  @overload(NoneType)
  def setShareContext(self, shareContext: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLContext::setShareContext(QOpenGLContext
    *shareContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcontext.html#setShareContext

    Parameters
    ----------

    shareContext : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContext::setShareContext(QOpenGLContext *shareContext)
    self.uglySide.call(
        'ritual_ZN14QOpenGLContext15setShareContextEPS_',
        self._addressOf(shareContext),
    )

  @overload(QScreen)
  @overload(NoneType)
  def setScreen(self, screen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QOpenGLContext::setScreen(QScreen *screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#setScreen

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContext::setScreen(QScreen *screen)
    self.uglySide.call(
        'ritual_ZN14QOpenGLContext9setScreenEP7QScreen',
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QOpenGLContext::QOpenGLContext(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#QOpenGLContext

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLContext::QOpenGLContext(QObject *parent)
    self._noteCreation(QOpenGLContext, lambda: Rituals.call(
        'ritual_ZN14QOpenGLContextC1EP7QObject', self._addressOf(parent),
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLContext::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#create
    """
    #  bool QOpenGLContext::create()
    return self.uglySide.call('ritual_ZN14QOpenGLContext6createEv')

  @overload(QSurface)
  @overload(NoneType)
  def makeCurrent(self, surface: Optional[QSurface]) -> bool:
    """
    Calls Qt's 'bool QOpenGLContext::makeCurrent(QSurface *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#makeCurrent

    Parameters
    ----------

    surface : Optional[QSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLContext::makeCurrent(QSurface *surface)
    return self.uglySide.call(
        'ritual_ZN14QOpenGLContext11makeCurrentEP8QSurface',
        self._addressOf(surface, 'QSurface'),
    )

  def doneCurrent(self) -> None:
    """
    Calls Qt's 'void QOpenGLContext::doneCurrent()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#doneCurrent
    """
    #  void QOpenGLContext::doneCurrent()
    self.uglySide.call('ritual_ZN14QOpenGLContext11doneCurrentEv')

  @overload(QSurface)
  @overload(NoneType)
  def swapBuffers(self, surface: Optional[QSurface]) -> None:
    """
    Calls Qt's 'void QOpenGLContext::swapBuffers(QSurface *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglcontext.html#swapBuffers

    Parameters
    ----------

    surface : Optional[QSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLContext::swapBuffers(QSurface *surface)
    self.uglySide.call(
        'ritual_ZN14QOpenGLContext11swapBuffersEP8QSurface',
        self._addressOf(surface, 'QSurface'),
    )
