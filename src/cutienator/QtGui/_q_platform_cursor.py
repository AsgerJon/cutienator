"""
QPlatformCursor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformcursor.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QSize
  from . import QCursor, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCursor = WAIT['QCursor']
  QPoint = WAIT['QPoint']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformCursor(QObject):
  """
  The cute side of Qt's QPlatformCursor: a plain Python object standing in
  front of one C++ QPlatformCursor.

  It is built on the cute 'QObject', as Qt's QPlatformCursor is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformCursor that has a ritual and that Python
  can call so far, 9 names in all: 'changeCursor', 'setOverrideCursor',
  'clearOverrideCursor', 'pos', 'setPos', 'size', 'capabilities',
  'setCapabilities', 'setCapability'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QPlatformCursor::pointerEvent(const QMouseEvent &event)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 15 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QPlatformCursor is created at the first use, not by
    'QPlatformCursor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformCursor.
  - Qt tells when it has removed the C++ QPlatformCursor. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformCursor that has no cute function yet,
    '__init__', 'pointerEvent', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlatformCursor, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Capability(CuteFlags):
    """
    The flags enum 'QPlatformCursor::Capability' of Qt, with the 1 names Qt
    gives in it. Qt names the type of its combinations
    'QPlatformCursor::Capabilities'.
    """

    OverrideCursor = 0x1

  Capabilities = Capability

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def capabilities() -> Capabilities:
    """
    Calls Qt's 'Capabilities QPlatformCursor::capabilities()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursor.html#capabilities

    Returns
    -------

    Capabilities
      The value standing for the combination Qt gave back.
    """
    #  Capabilities QPlatformCursor::capabilities()
    return QPlatformCursor.Capabilities(Rituals.call(
        'ritual_ZN15QPlatformCursor12capabilitiesEv',
    ))

  @staticmethod
  @overload(Capabilities)
  def setCapabilities(c: Capabilities) -> None:
    """
    Calls Qt's 'void QPlatformCursor::setCapabilities(Capabilities c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcursor.html#setCapabilities

    Parameters
    ----------

    c : Capabilities
      Passed on as its number.
    """
    #  void QPlatformCursor::setCapabilities(Capabilities c)
    Rituals.call(
        'ritual_ZN15QPlatformCursor15setCapabilitiesE6QFlagsINS_10Capabilit'
        'yEE',
        c.value,
    )

  @staticmethod
  @overload(Capability)
  def setCapability(c: Capability) -> None:
    """
    Calls Qt's 'void QPlatformCursor::setCapability(Capability c)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursor.html#setCapability

    Parameters
    ----------

    c : Capability
      Passed on as its number.
    """
    #  void QPlatformCursor::setCapability(Capability c)
    Rituals.call(
        'ritual_ZN15QPlatformCursor13setCapabilityENS_10CapabilityE',
        c.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformCursor'

  #  The functions Qt calls itself that QPlatformCursor is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'pointerEvent': (
          'void QPlatformCursor::pointerEvent(const QMouseEvent &)',
      ),
  }

  #  The functions Qt calls itself that QPlatformCursor is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'changeCursor': (
          ('_ZN15QPlatformCursor12changeCursorEP7QCursorP7QWindow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QCursor'),
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'setOverrideCursor': (
          ('_ZN15QPlatformCursor17setOverrideCursorERK7QCursor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QCursor'),
           )),
      ),
      'clearOverrideCursor': (
          ('_ZN15QPlatformCursor19clearOverrideCursorEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'pos': (
          ('_ZNK15QPlatformCursor3posEv',
           ('address', 'value', 'QtCore:QPoint'),
           ()),
      ),
      'setPos': (
          ('_ZN15QPlatformCursor6setPosERK6QPoint',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'size': (
          ('_ZNK15QPlatformCursor4sizeEv',
           ('address', 'value', 'QtCore:QSize'),
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

  def pos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QPlatformCursor::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursor.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QPlatformCursor::pos() const
    ritual = 'ritual_ZNK15QPlatformCursor3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformCursor3posEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QPlatformCursor::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursor.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPlatformCursor::size() const
    ritual = 'ritual_ZNK15QPlatformCursor4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QPlatformCursor4sizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCursor)
  def setOverrideCursor(self, a0: QCursor) -> None:
    """
    Calls Qt's 'void QPlatformCursor::setOverrideCursor(const QCursor &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcursor.html#setOverrideCursor

    Parameters
    ----------

    a0 : QCursor
      Passed on as a value: Qt reads the C++ QCursor, which stays Python's
      own.
    """
    #  void QPlatformCursor::setOverrideCursor(const QCursor &a0)
    ritual = 'ritual_ZN15QPlatformCursor17setOverrideCursorERK7QCursor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformCursor17setOverrideCursorERK7QCursor'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QPoint)
  def setPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QPlatformCursor::setPos(const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursor.html#setPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QPlatformCursor::setPos(const QPoint &pos)
    ritual = 'ritual_ZN15QPlatformCursor6setPosERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformCursor6setPosERK6QPoint'
    self.uglySide.call(ritual, self._valueOf(pos))

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
    Qt's 'QPlatformCursor::QPlatformCursor()': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QPlatformCursor.__init__' has no cute function yet. Qt's "
        "'QPlatformCursor::QPlatformCursor()': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
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

  @overload(QCursor, QWindow)
  @overload(QCursor, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def changeCursor(
      self,
      windowCursor: Optional[QCursor],
      window: Optional[QWindow],
  ) -> None:
    """
    Calls Qt's 'void QPlatformCursor::changeCursor(QCursor *windowCursor,
    QWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcursor.html#changeCursor

    Parameters
    ----------

    windowCursor : Optional[QCursor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformCursor::changeCursor(QCursor *windowCursor, QWindow
    #      *window)
    self.uglySide.call(
        'ritual_ZN15QPlatformCursor12changeCursorEP7QCursorP7QWindow',
        self._addressOf(windowCursor), self._addressOf(window),
    )

  def clearOverrideCursor(self) -> None:
    """
    Calls Qt's 'void QPlatformCursor::clearOverrideCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcursor.html#clearOverrideCursor
    """
    #  void QPlatformCursor::clearOverrideCursor()
    ritual = 'ritual_ZN15QPlatformCursor19clearOverrideCursorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QPlatformCursor19clearOverrideCursorEv'
    self.uglySide.call(ritual)

  @staticmethod
  def pointerEvent(*__, **_) -> Never:
    """
    Qt's 'void QPlatformCursor::pointerEvent(const QMouseEvent &event)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformCursor.pointerEvent' has no cute function yet. Qt's "
        "'void QPlatformCursor::pointerEvent(const QMouseEvent &event)': "
        "takes a type Python has no way to hand over yet.")
