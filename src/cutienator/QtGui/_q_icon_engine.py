"""
QIconEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qiconengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtCore import QList
from . import QIcon

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from . import QPainter, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPixmap = WAIT['QPixmap']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QIconEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QIconEngine: a plain Python object standing in front
  of one C++ QIconEngine.

  What exists
  -----------

  Every function of Qt's QIconEngine that has a ritual and that Python can
  call so far, 11 names in all: 'paint', 'actualSize', 'pixmap', 'addPixmap',
  'addFile', 'key', 'clone', 'availableSizes', 'iconName', 'isNull',
  'scaledPixmap'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIconEngine::~QIconEngine()': the destructor: Python never removes
    a C++ QIconEngine.

  What has no ritual
  ------------------

  6 of the 18 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 2 the class is abstract, so C++ cannot make one; 1 forbidden.

  What to expect
  --------------

  - The C++ QIconEngine is created at the first use, not by
    'QIconEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIconEngine.
  """

  #  The enums Qt writes inside QIconEngine, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class IconEngineHook(CuteNum):
    """
    The enum 'QIconEngine::IconEngineHook' of Qt, with the 2 names Qt gives
    in it.
    """

    IsNullHook = Kee[int](3)
    ScaledPixmapHook = Kee[int](4)

  #  The classes Qt writes inside QIconEngine, each a class in here as in
  #  C++.

  class ScaledPixmapArgument(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QIconEngine::ScaledPixmapArgument: a plain Python
    object standing in front of one C++ QIconEngine::ScaledPixmapArgument.

    C++ hands a QIconEngine::ScaledPixmapArgument around as a copy, so every
    C++ QIconEngine::ScaledPixmapArgument behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QIconEngine::ScaledPixmapArgument yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QIconEngine::ScaledPixmapArgument::~ScaledPixmapArgument()': the
      destructor: Python removes its C++ QIconEngine::ScaledPixmapArgument by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QIconEngine::ScaledPixmapArgument is created at the first use,
      not by 'QIconEngine::ScaledPixmapArgument(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QIconEngine::ScaledPixmapArgument back gives a copy
      the ritual made for Python, in a new cute
      QIconEngine::ScaledPixmapArgument.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QIconEngine::ScaledPixmapArgument'

    #  Qt's '~QIconEngine::ScaledPixmapArgument()'. Naming it makes this a
    #  value class: Python owns every C++ QIconEngine::ScaledPixmapArgument
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QIconEngine20ScaledPixmapArgumentD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIconEngine'

  #  A C++ QIconEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIconEngine'

  #  The functions Qt calls itself that QIconEngine is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'read': (
          'bool QIconEngine::read(QDataStream &)',
      ),
      'write': (
          'bool QIconEngine::write(QDataStream &) const',
      ),
      'availableSizes': (
          'QList<QSize> QIconEngine::availableSizes(QIcon::Mode, '
          'QIcon::State)',
      ),
      'virtual_hook': (
          'void QIconEngine::virtual_hook(int, void *)',
      ),
  }

  #  The functions Qt calls itself that QIconEngine is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'paint': (
          ('_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5Stat'
           'eE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('int', 'enum', 'QtGui:QIcon.State'),
           )),
      ),
      'actualSize': (
          ('_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5StateE',
           ('address', 'value', 'QtCore:QSize'),
           (
               ('address', 'value', 'QtCore:QSize'),
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('int', 'enum', 'QtGui:QIcon.State'),
           )),
      ),
      'pixmap': (
          ('_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('address', 'value', 'QtCore:QSize'),
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('int', 'enum', 'QtGui:QIcon.State'),
           )),
      ),
      'addPixmap': (
          ('_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5StateE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPixmap'),
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('int', 'enum', 'QtGui:QIcon.State'),
           )),
      ),
      'addFile': (
          ('_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_5St'
           'ateE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QSize'),
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('int', 'enum', 'QtGui:QIcon.State'),
           )),
      ),
      'key': (
          ('_ZNK11QIconEngine3keyEv',
           ('address', 'text', ''),
           ()),
      ),
      'clone': (
          ('_ZNK11QIconEngine5cloneEv',
           ('address', 'address', 'QtGui:QIconEngine'),
           ()),
      ),
      'iconName': (
          ('_ZN11QIconEngine8iconNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'isNull': (
          ('_ZN11QIconEngine6isNullEv',
           ('bool', 'number', ''),
           ()),
      ),
      'scaledPixmap': (
          ('_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5StateE'
           'd',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('address', 'value', 'QtCore:QSize'),
               ('int', 'enum', 'QtGui:QIcon.Mode'),
               ('int', 'enum', 'QtGui:QIcon.State'),
               ('double', 'number', ''),
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

  def key(self) -> str:
    """
    Calls Qt's 'QString QIconEngine::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIconEngine::key() const
    ritual = 'ritual_ZNK11QIconEngine3keyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QIconEngine3keyEv'
    return self.uglySide.call(ritual)

  def clone(self) -> Optional[QIconEngine]:
    """
    Calls Qt's 'QIconEngine *QIconEngine::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#clone

    Returns
    -------

    Optional[QIconEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIconEngine *QIconEngine::clone() const
    address = self.uglySide.call('ritual_ZNK11QIconEngine5cloneEv')
    return QIconEngine._cuteAt(address)

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

  @overload(QPainter, QRect, QIcon.Mode, QIcon.State)
  @overload(NoneType, QRect, QIcon.Mode, QIcon.State)
  def paint(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> None:
    """
    Calls Qt's 'void QIconEngine::paint(QPainter *painter, const QRect &rect,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.
    """
    #  void QIconEngine::paint(QPainter *painter, const QRect &rect,
    #      QIcon::Mode mode, QIcon::State state)
    self.uglySide.call(
        'ritual_ZN11QIconEngine5paintEP8QPainterRK5QRectN5QIcon4ModeENS5_5S'
        'tateE',
        self._addressOf(painter), self._valueOf(rect), mode.value,
        state.value,
    )

  @overload(QSize, QIcon.Mode, QIcon.State)
  def actualSize(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QSize:
    """
    Calls Qt's 'QSize QIconEngine::actualSize(const QSize &size, QIcon::Mode
    mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#actualSize

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
    #  QSize QIconEngine::actualSize(const QSize &size, QIcon::Mode mode,
    #      QIcon::State state)
    ritual = (
        'ritual_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_5State'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QIconEngine10actualSizeERK5QSizeN5QIcon4ModeENS3_'
          '5StateE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QSize, QIcon.Mode, QIcon.State)
  def pixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QIconEngine::pixmap(const QSize &size, QIcon::Mode
    mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#pixmap

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

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QIconEngine::pixmap(const QSize &size, QIcon::Mode mode,
    #      QIcon::State state)
    ritual = 'ritual_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5StateE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QIconEngine6pixmapERK5QSizeN5QIcon4ModeENS3_5Stat'
          'eE')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QPixmap, QIcon.Mode, QIcon.State)
  def addPixmap(
      self,
      pixmap: QPixmap,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> None:
    """
    Calls Qt's 'void QIconEngine::addPixmap(const QPixmap &pixmap,
    QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#addPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.
    """
    #  void QIconEngine::addPixmap(const QPixmap &pixmap, QIcon::Mode mode,
    #      QIcon::State state)
    ritual = (
        'ritual_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_5State'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QIconEngine9addPixmapERK7QPixmapN5QIcon4ModeENS3_'
          '5StateE')
    self.uglySide.call(
        ritual, self._valueOf(pixmap), mode.value, state.value,
    )

  @overload(str, QSize, QIcon.Mode, QIcon.State)
  def addFile(
      self,
      fileName: str,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> None:
    """
    Calls Qt's 'void QIconEngine::addFile(const QString &fileName, const
    QSize &size, QIcon::Mode mode, QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#addFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.
    """
    #  void QIconEngine::addFile(const QString &fileName, const QSize &size,
    #      QIcon::Mode mode, QIcon::State state)
    ritual = (
        'ritual_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4ModeENS6_'
        '5StateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QIconEngine7addFileERK7QStringRK5QSizeN5QIcon4Mod'
          'eENS6_5StateE')
    self.uglySide.call(
        ritual, fileName, self._valueOf(size), mode.value, state.value,
    )

  @overload()
  @overload(QIcon.Mode)
  @overload(QIcon.Mode, QIcon.State)
  def availableSizes(
      self,
      mode: QIcon.Mode = QIcon.Mode.Normal,
      state: QIcon.State = QIcon.State.Off,
  ) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QIconEngine::availableSizes(QIcon::Mode mode,
    QIcon::State state)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#availableSizes

    Parameters
    ----------

    mode : QIcon.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QIcon.Mode.Normal.

    state : QIcon.State
      Passed on as its number. May be left out, as in Qt: it is then
      QIcon.State.Off.

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QIconEngine::availableSizes(QIcon::Mode mode,
    #      QIcon::State state)
    address = self.uglySide.call(
        'ritual_ZN11QIconEngine14availableSizesEN5QIcon4ModeENS0_5StateE',
        mode.value, state.value,
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  def iconName(self) -> str:
    """
    Calls Qt's 'QString QIconEngine::iconName()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#iconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIconEngine::iconName()
    ritual = 'ritual_ZN11QIconEngine8iconNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QIconEngine8iconNameEv'
    return self.uglySide.call(ritual)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QIconEngine::isNull()'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#isNull
    """
    #  bool QIconEngine::isNull()
    ritual = 'ritual_ZN11QIconEngine6isNullEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QIconEngine6isNullEv'
    return self.uglySide.call(ritual)

  @overload(QSize, QIcon.Mode, QIcon.State, float)
  def scaledPixmap(
      self,
      size: QSize,
      mode: QIcon.Mode,
      state: QIcon.State,
      scale: float,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QIconEngine::scaledPixmap(const QSize &size,
    QIcon::Mode mode, QIcon::State state, qreal scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qiconengine.html#scaledPixmap

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    scale : float
      Passed on as it is.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QIconEngine::scaledPixmap(const QSize &size, QIcon::Mode mode,
    #      QIcon::State state, qreal scale)
    ritual = (
        'ritual_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS3_5Sta'
        'teEd')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QIconEngine12scaledPixmapERK5QSizeN5QIcon4ModeENS'
          '3_5StateEd')
    address = self.uglySide.call(
        ritual, self._valueOf(size), mode.value, state.value, scale,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)
