"""
QPlatformSurfaceCapture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformsurfacecapture_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformSurfaceCapture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QPlatformVideoSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QCapturableWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCapturableWindow = WAIT['QCapturableWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformSurfaceCapture(QPlatformVideoSource):
  """
  The cute side of Qt's QPlatformSurfaceCapture: a plain Python object
  standing in front of one C++ QPlatformSurfaceCapture.

  It is built on the cute 'QPlatformVideoSource', as Qt's
  QPlatformSurfaceCapture is built on Qt's QPlatformVideoSource, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformSurfaceCapture that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'setActive',
  'isActive', 'error', 'errorString', 'setIgnoreCursor', 'ignoreCursor',
  'setIgnoreDropShadow', 'ignoreDropShadow', 'setActiveInternal',
  'updateError', 'sourceChanged', 'errorOccurred'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformSurfaceCapture::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformSurfaceCapture::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QPlatformSurfaceCapture::setSource(Source source)': takes a
    type Python has no way to hand over yet.
  - Qt's 'Source QPlatformSurfaceCapture::source() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QPlatformSurfaceCapture::setFrameRate(std::optional<qreal>
    a0)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<qreal> QPlatformSurfaceCapture::frameRate() const':
    gives a type Python has no way to take yet.
  - Qt's 'bool QPlatformSurfaceCapture::checkScreenWithError(ScreenSource
    &screen)': takes a type Python has no way to hand over yet.
  - Qt's 'void QPlatformSurfaceCapture::sourceChanged(ScreenSource a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QPlatformSurfaceCapture::frameRateChanged(std::optional<qreal>
    a0)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 a template.

  What to expect
  --------------

  - The C++ QPlatformSurfaceCapture is created at the first use, not by
    'QPlatformSurfaceCapture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformSurfaceCapture.
  - Qt tells when it has removed the C++ QPlatformSurfaceCapture. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformSurfaceCapture that has no cute function yet,
    '__init__', 'checkScreenWithError', 'frameRate', 'frameRateChanged',
    'setFrameRate', 'setSource', 'source', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlatformSurfaceCapture, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'QPlatformSurfaceCapture::Error' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NoError = Kee[int](0)
    InternalError = Kee[int](1)
    CapturingNotSupported = Kee[int](2)
    CaptureFailed = Kee[int](4)
    NotFound = Kee[int](5)

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
    Calls Qt's 'QString QPlatformSurfaceCapture::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformsurfacecapture.html#tr

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
    #  QString QPlatformSurfaceCapture::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QPlatformSurfaceCapture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformSurfaceCapture'

  #  The functions Qt calls itself that QPlatformSurfaceCapture is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setActiveInternal': (
          ('_ZN23QPlatformSurfaceCapture17setActiveInternalEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QPlatformSurfaceCapture::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformSurfaceCapture::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QPlatformSurfaceCapture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSurfaceCapture::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#isActive
    """
    #  bool QPlatformSurfaceCapture::isActive() const
    ritual = 'ritual_ZNK23QPlatformSurfaceCapture8isActiveEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QPlatformSurfaceCapture8isActiveEv'
    return self.uglySide.call(ritual)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QPlatformSurfaceCapture::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformsurfacecapture.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QPlatformSurfaceCapture::error() const
    return QPlatformSurfaceCapture.Error(self.uglySide.call(
        'ritual_ZNK23QPlatformSurfaceCapture5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QPlatformSurfaceCapture::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformSurfaceCapture::errorString() const
    return self.uglySide.call(
        'ritual_ZNK23QPlatformSurfaceCapture11errorStringEv',
    )

  def ignoreCursor(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSurfaceCapture::ignoreCursor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#ignoreCursor
    """
    #  bool QPlatformSurfaceCapture::ignoreCursor() const
    return self.uglySide.call(
        'ritual_ZNK23QPlatformSurfaceCapture12ignoreCursorEv',
    )

  def ignoreDropShadow(self) -> bool:
    """
    Calls Qt's 'bool QPlatformSurfaceCapture::ignoreDropShadow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#ignoreDropShadow
    """
    #  bool QPlatformSurfaceCapture::ignoreDropShadow() const
    return self.uglySide.call(
        'ritual_ZNK23QPlatformSurfaceCapture16ignoreDropShadowEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QPlatformSurfaceCapture::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QPlatformSurfaceCapture::setActive(bool active)
    ritual = 'ritual_ZN23QPlatformSurfaceCapture9setActiveEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QPlatformSurfaceCapture9setActiveEb'
    self.uglySide.call(ritual, active)

  @overload(bool)
  def setIgnoreCursor(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPlatformSurfaceCapture::setIgnoreCursor(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#setIgnoreCursor

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPlatformSurfaceCapture::setIgnoreCursor(bool a0)
    self.uglySide.call(
        'ritual_ZN23QPlatformSurfaceCapture15setIgnoreCursorEb', a0,
    )

  @overload(bool)
  def setIgnoreDropShadow(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPlatformSurfaceCapture::setIgnoreDropShadow(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#setIgnoreDropShadow

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPlatformSurfaceCapture::setIgnoreDropShadow(bool a0)
    self.uglySide.call(
        'ritual_ZN23QPlatformSurfaceCapture19setIgnoreDropShadowEb', a0,
    )

  @overload(bool)
  def setActiveInternal(self, a0: bool) -> bool:
    """
    Calls Qt's 'bool QPlatformSurfaceCapture::setActiveInternal(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#setActiveInternal

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  bool QPlatformSurfaceCapture::setActiveInternal(bool a0)
    return self.uglySide.call(
        'ritual_ZN23QPlatformSurfaceCapture17setActiveInternalEb', a0,
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
    Qt's 'QPlatformSurfaceCapture::QPlatformSurfaceCapture(Source
    initialSource)': the class is abstract, so C++ cannot make one, and the
    C++ class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformSurfaceCapture.__init__' has no cute function yet. Qt's "
        "'QPlatformSurfaceCapture::QPlatformSurfaceCapture(Source "
        "initialSource)': the class is abstract, so C++ cannot make one, "
        "and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  @overload(Error, str)
  def updateError(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QPlatformSurfaceCapture::updateError(Error error, const
    QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#updateError

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformSurfaceCapture::updateError(Error error, const QString
    #      &errorString)
    self.uglySide.call(
        'ritual_ZN23QPlatformSurfaceCapture11updateErrorENS_5ErrorERK7QStri'
        'ng',
        error.value, errorString,
    )

  @overload(QCapturableWindow)
  def sourceChanged(self, a0: QCapturableWindow) -> None:
    """
    Calls Qt's 'void QPlatformSurfaceCapture::sourceChanged(WindowSource
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#sourceChanged

    Parameters
    ----------

    a0 : QCapturableWindow
      Passed on as a value: Qt reads the C++ QCapturableWindow, which stays
      Python's own.
    """
    #  void QPlatformSurfaceCapture::sourceChanged(WindowSource a0)
    self.uglySide.call(
        'ritual_ZN23QPlatformSurfaceCapture13sourceChangedE17QCapturableWin'
        'dow',
        self._valueOf(a0),
    )

  @overload(Error, str)
  def errorOccurred(self, error: Error, errorString: str) -> None:
    """
    Calls Qt's 'void QPlatformSurfaceCapture::errorOccurred(Error error,
    QString errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformsurfacecapture.html#errorOccurred

    Parameters
    ----------

    error : Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformSurfaceCapture::errorOccurred(Error error, QString
    #      errorString)
    self.uglySide.call(
        'ritual_ZN23QPlatformSurfaceCapture13errorOccurredENS_5ErrorE7QStri'
        'ng',
        error.value, errorString,
    )

  @staticmethod
  def checkScreenWithError(*__, **_) -> Never:
    """
    Qt's 'bool QPlatformSurfaceCapture::checkScreenWithError(ScreenSource
    &screen)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSurfaceCapture.checkScreenWithError' has no cute "
        "function yet. Qt's 'bool "
        "QPlatformSurfaceCapture::checkScreenWithError(ScreenSource "
        "&screen)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def frameRate(*__, **_) -> Never:
    """
    Qt's 'std::optional<qreal> QPlatformSurfaceCapture::frameRate() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformSurfaceCapture.frameRate' has no cute function yet. Qt's "
        "'std::optional<qreal> QPlatformSurfaceCapture::frameRate() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def frameRateChanged(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSurfaceCapture::frameRateChanged(std::optional<qreal>
    a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSurfaceCapture.frameRateChanged' has no cute function "
        "yet. Qt's 'void "
        "QPlatformSurfaceCapture::frameRateChanged(std::optional<qreal> "
        "a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setFrameRate(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSurfaceCapture::setFrameRate(std::optional<qreal>
    a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSurfaceCapture.setFrameRate' has no cute function yet. "
        "Qt's 'void "
        "QPlatformSurfaceCapture::setFrameRate(std::optional<qreal> a0)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setSource(*__, **_) -> Never:
    """
    Qt's 'void QPlatformSurfaceCapture::setSource(Source source)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformSurfaceCapture.setSource' has no cute function yet. Qt's "
        "'void QPlatformSurfaceCapture::setSource(Source source)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def source(*__, **_) -> Never:
    """
    - Qt's 'Source QPlatformSurfaceCapture::source() const': gives a type
      Python has no way to take yet.
    - Qt's 'QPlatformSurfaceCapture::source': a template: a pattern and no
      single function.
    """
    raise NotImplementedError(
        "'QPlatformSurfaceCapture.source' has no cute function yet. Qt's "
        "'Source QPlatformSurfaceCapture::source() const': gives a type "
        "Python has no way to take yet. Qt's "
        "'QPlatformSurfaceCapture::source': a template: a pattern and no "
        "single function.")
