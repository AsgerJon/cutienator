"""
QAbstractFileIconEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qabstractfileiconengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractFileIconEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QIcon, QPixmapIconEngine, QPlatformTheme

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QFileInfo, QSize
  from . import QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QAbstractFileIconEngine(QPixmapIconEngine):
  """
  The cute side of Qt's QAbstractFileIconEngine: a plain Python object
  standing in front of one C++ QAbstractFileIconEngine.

  It is built on the cute 'QPixmapIconEngine', as Qt's
  QAbstractFileIconEngine is built on Qt's QPixmapIconEngine, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractFileIconEngine that has a ritual and that
  Python can call so far, 8 names in all: 'pixmap', 'scaledPixmap',
  'actualSize', 'isNull', 'fileInfo', 'options', 'filePixmap', 'cacheKey'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open; 1 a template.

  What to expect
  --------------

  - The C++ QAbstractFileIconEngine is created at the first use, not by
    'QAbstractFileIconEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractFileIconEngine.
  - Each name of Qt's QAbstractFileIconEngine that has no cute function yet,
    '__init__', 'toSizeList', holds a function that raises
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
  __qt_class__ = 'QAbstractFileIconEngine'

  #  The functions Qt calls itself that QAbstractFileIconEngine is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'filePixmap': (
          ('_ZN23QAbstractFileIconEngine10filePixmapERK5QSizeN5QIcon4ModeEN'
           'S3_5StateE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('address', 'value', 'QtCore:QSize'),
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('int', 'enum', 'QtGui:QIcon.State'),
           )),
      ),
      'cacheKey': (
          ('_ZNK23QAbstractFileIconEngine8cacheKeyEv',
           ('address', 'text', ''),
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

  def fileInfo(self) -> QFileInfo:
    """
    Calls Qt's 'QFileInfo QAbstractFileIconEngine::fileInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconengine.html#fileInfo

    Returns
    -------

    QFileInfo
      A new cute QFileInfo around the copy Qt gave back. Python owns it.
    """
    #  QFileInfo QAbstractFileIconEngine::fileInfo() const
    address = self.uglySide.call(
        'ritual_ZNK23QAbstractFileIconEngine8fileInfoEv',
    )
    from ..QtCore import QFileInfo
    return QFileInfo._cuteOwning(address)

  def options(self) -> QPlatformTheme.IconOptions:
    """
    Calls Qt's 'QPlatformTheme::IconOptions
    QAbstractFileIconEngine::options() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconengine.html#options

    Returns
    -------

    QPlatformTheme.IconOptions
      The value standing for the combination Qt gave back.
    """
    #  QPlatformTheme::IconOptions QAbstractFileIconEngine::options() const
    return QPlatformTheme.IconOptions(self.uglySide.call(
        'ritual_ZNK23QAbstractFileIconEngine7optionsEv',
    ))

  def cacheKey(self) -> str:
    """
    Calls Qt's 'QString QAbstractFileIconEngine::cacheKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconengine.html#cacheKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileIconEngine::cacheKey() const
    ritual = 'ritual_ZNK23QAbstractFileIconEngine8cacheKeyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QAbstractFileIconEngine8cacheKeyEv'
    return self.uglySide.call(ritual)

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
    Qt's 'QAbstractFileIconEngine::QAbstractFileIconEngine(const QFileInfo
    &info, QPlatformTheme::IconOptions opts)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractFileIconEngine.__init__' has no cute function yet. Qt's "
        "'QAbstractFileIconEngine::QAbstractFileIconEngine(const QFileInfo "
        "&info, QPlatformTheme::IconOptions opts)': the class is abstract, "
        "so C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  @overload(QSize, QIcon.Mode, QIcon.State)
  def pixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      a2: QIcon.State,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QAbstractFileIconEngine::pixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconengine.html#pixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    a2 : QIcon.State
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QAbstractFileIconEngine::pixmap(const QSize &size, QIcon::Mode
    #      mode, QIcon::State a2)
    ritual = (
        'ritual_ZN23QAbstractFileIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3'
        '_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstractFileIconEngine6pixmapERK5QSizeN5QIcon4Mo'
          'deENS3_5StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, a2.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSize, QIcon.Mode, QIcon.State, float)
  def scaledPixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      a2: QIcon.State,
      scale: float,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QAbstractFileIconEngine::scaledPixmap(const QSize
    &size, QIcon::Mode mode, QIcon::State a2, qreal scale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconengine.html#scaledPixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    a2 : QIcon.State
      Passed on as its number.

    scale : float
      Passed on as it is.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QAbstractFileIconEngine::scaledPixmap(const QSize &size,
    #      QIcon::Mode mode, QIcon::State a2, qreal scale)
    ritual = (
        'ritual_ZN23QAbstractFileIconEngine12scaledPixmapERK5QSizeN5QIcon4M'
        'odeENS3_5StateEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstractFileIconEngine12scaledPixmapERK5QSizeN5Q'
          'Icon4ModeENS3_5StateEd')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, a2.value, scale,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QSize, QIcon.Mode, QIcon.State)
  def actualSize(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QSize:
    """
    Calls Qt's 'QSize QAbstractFileIconEngine::actualSize(const QSize &size,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconengine.html#actualSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractFileIconEngine::actualSize(const QSize &size,
    #      QIcon::Mode mode, QIcon::State state)
    ritual = (
        'ritual_ZN23QAbstractFileIconEngine10actualSizeERK5QSizeN5QIcon4Mod'
        'eENS3_5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstractFileIconEngine10actualSizeERK5QSizeN5QIc'
          'on4ModeENS3_5StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileIconEngine::isNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconengine.html#isNull
    """
    #  bool QAbstractFileIconEngine::isNull()
    ritual = 'ritual_ZN23QAbstractFileIconEngine6isNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QAbstractFileIconEngine6isNullEv'
    return self.uglySide.call(ritual)

  @overload(QSize, QIcon.Mode, QIcon.State)
  def filePixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      a2: QIcon.State,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QAbstractFileIconEngine::filePixmap(const QSize
    &size, QIcon::Mode mode, QIcon::State a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconengine.html#filePixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    a2 : QIcon.State
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QAbstractFileIconEngine::filePixmap(const QSize &size,
    #      QIcon::Mode mode, QIcon::State a2)
    address = self.uglySide.call(
        'ritual_ZN23QAbstractFileIconEngine10filePixmapERK5QSizeN5QIcon4Mod'
        'eENS3_5StateE',
        self._valueOf(size), mode.value, a2.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @staticmethod
  def toSizeList(*__, **_) -> Never:
    """
    Qt's 'QAbstractFileIconEngine::toSizeList': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QAbstractFileIconEngine.toSizeList' has no cute function yet. "
        "Qt's 'QAbstractFileIconEngine::toSizeList': a template: a pattern "
        "and no single function.")
