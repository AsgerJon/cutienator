"""
QPlatformOpenGLContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QOpenGLContext, QPlatformSurface, QSurfaceFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QPlatformSurface = WAIT['QPlatformSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformOpenGLContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformOpenGLContext: a plain Python object
  standing in front of one C++ QPlatformOpenGLContext.

  What exists
  -----------

  Every function of Qt's QPlatformOpenGLContext that has a ritual and that
  Python can call so far, 12 names in all: 'initialize', 'format',
  'swapBuffers', 'defaultFramebufferObject', 'makeCurrent', 'doneCurrent',
  'beginFrame', 'endFrame', 'isSharing', 'isValid', 'context', 'setContext'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformOpenGLContextPrivate *QPlatformOpenGLContext::d_func()':
    gives 'QPlatformOpenGLContextPrivate', which has no cute class yet.
  - Qt's 'const QPlatformOpenGLContextPrivate
    *QPlatformOpenGLContext::d_func() const': gives
    'QPlatformOpenGLContextPrivate', which has no cute class yet.
  - Qt's 'QPlatformOpenGLContext::~QPlatformOpenGLContext()': the destructor:
    Python never removes a C++ QPlatformOpenGLContext.
  - Qt's 'QFunctionPointer QPlatformOpenGLContext::getProcAddress(const char
    *procName)': gives a type Python has no way to take yet.
  - Qt's 'bool QPlatformOpenGLContext::parseOpenGLVersion(const QByteArray
    &versionString, int &major, int &minor)': takes a number to change where
    it is.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 2 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QPlatformOpenGLContext is created at the first use, not by
    'QPlatformOpenGLContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformOpenGLContext.
  - Each name of Qt's QPlatformOpenGLContext that has no cute function yet,
    '__init__', 'd_func', 'getProcAddress', 'parseOpenGLVersion', holds a
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
  __qt_class__ = 'QPlatformOpenGLContext'

  #  A C++ QPlatformOpenGLContext Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformOpenGLContext'

  #  The functions Qt calls itself that QPlatformOpenGLContext is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'getProcAddress': (
          'QFunctionPointer QPlatformOpenGLContext::getProcAddress(const '
          'char *)',
      ),
  }

  #  The functions Qt calls itself that QPlatformOpenGLContext is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN22QPlatformOpenGLContext10initializeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'format': (
          ('_ZNK22QPlatformOpenGLContext6formatEv',
           ('address', 'value', 'QtGui:QSurfaceFormat'),
           ()),
      ),
      'swapBuffers': (
          ('_ZN22QPlatformOpenGLContext11swapBuffersEP16QPlatformSurface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPlatformSurface'),
           )),
      ),
      'defaultFramebufferObject': (
          ('_ZNK22QPlatformOpenGLContext24defaultFramebufferObjectEP16QPlat'
           'formSurface',
           ('unsigned int', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPlatformSurface'),
           )),
      ),
      'makeCurrent': (
          ('_ZN22QPlatformOpenGLContext11makeCurrentEP16QPlatformSurface',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QPlatformSurface'),
           )),
      ),
      'doneCurrent': (
          ('_ZN22QPlatformOpenGLContext11doneCurrentEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'beginFrame': (
          ('_ZN22QPlatformOpenGLContext10beginFrameEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endFrame': (
          ('_ZN22QPlatformOpenGLContext8endFrameEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isSharing': (
          ('_ZNK22QPlatformOpenGLContext9isSharingEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isValid': (
          ('_ZNK22QPlatformOpenGLContext7isValidEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QSurfaceFormat:
    """
    Calls Qt's 'QSurfaceFormat QPlatformOpenGLContext::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformopenglcontext.html#format

    Returns
    -------

    QSurfaceFormat
      A new cute QSurfaceFormat around the copy Qt gave back. Python owns it.
    """
    #  QSurfaceFormat QPlatformOpenGLContext::format() const
    address = self.uglySide.call(
        'ritual_ZNK22QPlatformOpenGLContext6formatEv',
    )
    from . import QSurfaceFormat
    return QSurfaceFormat._cuteOwning(address)

  @overload(QPlatformSurface)
  @overload(NoneType)
  def defaultFramebufferObject(
      self,
      surface: Optional[QPlatformSurface],
  ) -> int:
    """
    Calls Qt's 'GLuint
    QPlatformOpenGLContext::defaultFramebufferObject(QPlatformSurface
    *surface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html

    Parameters
    ----------

    surface : Optional[QPlatformSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  GLuint
    #      QPlatformOpenGLContext::defaultFramebufferObject(QPlatformSurface
    #      *surface) const
    ritual = (
        'ritual_ZNK22QPlatformOpenGLContext24defaultFramebufferObjectEP16QP'
        'latformSurface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QPlatformOpenGLContext24defaultFramebufferObject'
          'EP16QPlatformSurface')
    return self.uglySide.call(ritual, self._addressOf(surface))

  def isSharing(self) -> bool:
    """
    Calls Qt's 'bool QPlatformOpenGLContext::isSharing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#isSharing
    """
    #  bool QPlatformOpenGLContext::isSharing() const
    ritual = 'ritual_ZNK22QPlatformOpenGLContext9isSharingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QPlatformOpenGLContext9isSharingEv'
    return self.uglySide.call(ritual)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPlatformOpenGLContext::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#isValid
    """
    #  bool QPlatformOpenGLContext::isValid() const
    ritual = 'ritual_ZNK22QPlatformOpenGLContext7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QPlatformOpenGLContext7isValidEv'
    return self.uglySide.call(ritual)

  def context(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QPlatformOpenGLContext::context() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#context

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QPlatformOpenGLContext::context() const
    address = self.uglySide.call(
        'ritual_ZNK22QPlatformOpenGLContext7contextEv',
    )
    from . import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpenGLContext)
  @overload(NoneType)
  def setContext(self, context: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QPlatformOpenGLContext::setContext(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#setContext

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformOpenGLContext::setContext(QOpenGLContext *context)
    self.uglySide.call(
        'ritual_ZN22QPlatformOpenGLContext10setContextEP14QOpenGLContext',
        self._addressOf(context),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QPlatformOpenGLContext::QPlatformOpenGLContext()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformOpenGLContext.__init__' has no cute function yet. Qt's "
        "'QPlatformOpenGLContext::QPlatformOpenGLContext()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QPlatformOpenGLContext::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#initialize
    """
    #  void QPlatformOpenGLContext::initialize()
    ritual = 'ritual_ZN22QPlatformOpenGLContext10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QPlatformOpenGLContext10initializeEv'
    self.uglySide.call(ritual)

  @overload(QPlatformSurface)
  @overload(NoneType)
  def swapBuffers(self, surface: Optional[QPlatformSurface]) -> None:
    """
    Calls Qt's 'void QPlatformOpenGLContext::swapBuffers(QPlatformSurface
    *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#swapBuffers

    Parameters
    ----------

    surface : Optional[QPlatformSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformOpenGLContext::swapBuffers(QPlatformSurface *surface)
    self.uglySide.call(
        'ritual_ZN22QPlatformOpenGLContext11swapBuffersEP16QPlatformSurface',
        self._addressOf(surface),
    )

  @overload(QPlatformSurface)
  @overload(NoneType)
  def makeCurrent(self, surface: Optional[QPlatformSurface]) -> bool:
    """
    Calls Qt's 'bool QPlatformOpenGLContext::makeCurrent(QPlatformSurface
    *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#makeCurrent

    Parameters
    ----------

    surface : Optional[QPlatformSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlatformOpenGLContext::makeCurrent(QPlatformSurface *surface)
    return self.uglySide.call(
        'ritual_ZN22QPlatformOpenGLContext11makeCurrentEP16QPlatformSurface',
        self._addressOf(surface),
    )

  def doneCurrent(self) -> None:
    """
    Calls Qt's 'void QPlatformOpenGLContext::doneCurrent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#doneCurrent
    """
    #  void QPlatformOpenGLContext::doneCurrent()
    self.uglySide.call('ritual_ZN22QPlatformOpenGLContext11doneCurrentEv')

  def beginFrame(self) -> None:
    """
    Calls Qt's 'void QPlatformOpenGLContext::beginFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#beginFrame
    """
    #  void QPlatformOpenGLContext::beginFrame()
    ritual = 'ritual_ZN22QPlatformOpenGLContext10beginFrameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QPlatformOpenGLContext10beginFrameEv'
    self.uglySide.call(ritual)

  def endFrame(self) -> None:
    """
    Calls Qt's 'void QPlatformOpenGLContext::endFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformopenglcontext.html#endFrame
    """
    #  void QPlatformOpenGLContext::endFrame()
    ritual = 'ritual_ZN22QPlatformOpenGLContext8endFrameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QPlatformOpenGLContext8endFrameEv'
    self.uglySide.call(ritual)

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QPlatformOpenGLContextPrivate *QPlatformOpenGLContext::d_func()':
      gives 'QPlatformOpenGLContextPrivate', which has no cute class yet.
    - Qt's 'const QPlatformOpenGLContextPrivate
      *QPlatformOpenGLContext::d_func() const': gives
      'QPlatformOpenGLContextPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlatformOpenGLContext.d_func' has no cute function yet. Qt's "
        "'QPlatformOpenGLContextPrivate *QPlatformOpenGLContext::d_func()': "
        "gives 'QPlatformOpenGLContextPrivate', which has no cute class "
        "yet. Qt's 'const QPlatformOpenGLContextPrivate "
        "*QPlatformOpenGLContext::d_func() const': gives "
        "'QPlatformOpenGLContextPrivate', which has no cute class yet.")

  @staticmethod
  def getProcAddress(*__, **_) -> Never:
    """
    Qt's 'QFunctionPointer QPlatformOpenGLContext::getProcAddress(const char
    *procName)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformOpenGLContext.getProcAddress' has no cute function yet. "
        "Qt's 'QFunctionPointer "
        "QPlatformOpenGLContext::getProcAddress(const char *procName)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def parseOpenGLVersion(*__, **_) -> Never:
    """
    Qt's 'bool QPlatformOpenGLContext::parseOpenGLVersion(const QByteArray
    &versionString, int &major, int &minor)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QPlatformOpenGLContext.parseOpenGLVersion' has no cute function "
        "yet. Qt's 'bool QPlatformOpenGLContext::parseOpenGLVersion(const "
        "QByteArray &versionString, int &major, int &minor)': takes a "
        "number to change where it is.")
