"""
QPlatformClipboard binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformclipboard.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QClipboard

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMimeData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformClipboard(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformClipboard: a plain Python object standing in
  front of one C++ QPlatformClipboard.

  What exists
  -----------

  Every function of Qt's QPlatformClipboard that has a ritual and that Python
  can call so far, 5 names in all: 'mimeData', 'setMimeData', 'supportsMode',
  'ownsMode', 'emitChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformClipboard::~QPlatformClipboard()': the destructor: Python
    never removes a C++ QPlatformClipboard.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPlatformClipboard is created at the first use, not by
    'QPlatformClipboard(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformClipboard.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformClipboard'

  #  A C++ QPlatformClipboard Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformClipboard'

  #  The functions Qt calls itself that QPlatformClipboard is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'mimeData': (
          ('_ZN18QPlatformClipboard8mimeDataEN10QClipboard4ModeE',
           ('address', 'address', 'QtCore:QMimeData'),
           (
               ('int', 'enum', 'QtGui:QClipboard.Mode'),
           )),
      ),
      'setMimeData': (
          ('_ZN18QPlatformClipboard11setMimeDataEP9QMimeDataN10QClipboard4M'
           'odeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
               ('int', 'enum', 'QtGui:QClipboard.Mode'),
           )),
      ),
      'supportsMode': (
          ('_ZNK18QPlatformClipboard12supportsModeEN10QClipboard4ModeE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QClipboard.Mode'),
           )),
      ),
      'ownsMode': (
          ('_ZNK18QPlatformClipboard8ownsModeEN10QClipboard4ModeE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QClipboard.Mode'),
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

  @overload(QClipboard.Mode)
  def supportsMode(self, mode: QClipboard.Mode) -> bool:
    """
    Calls Qt's 'bool QPlatformClipboard::supportsMode(QClipboard::Mode mode)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformclipboard.html#supportsMode

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number.
    """
    #  bool QPlatformClipboard::supportsMode(QClipboard::Mode mode) const
    ritual = (
        'ritual_ZNK18QPlatformClipboard12supportsModeEN10QClipboard4ModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QPlatformClipboard12supportsModeEN10QClipboard4M'
          'odeE')
    return self.uglySide.call(ritual, mode.value)

  @overload(QClipboard.Mode)
  def ownsMode(self, mode: QClipboard.Mode) -> bool:
    """
    Calls Qt's 'bool QPlatformClipboard::ownsMode(QClipboard::Mode mode)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformclipboard.html#ownsMode

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number.
    """
    #  bool QPlatformClipboard::ownsMode(QClipboard::Mode mode) const
    ritual = 'ritual_ZNK18QPlatformClipboard8ownsModeEN10QClipboard4ModeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QPlatformClipboard8ownsModeEN10QClipboard4ModeE')
    return self.uglySide.call(ritual, mode.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMimeData)
  @overload(NoneType)
  @overload(QMimeData, QClipboard.Mode)
  @overload(NoneType, QClipboard.Mode)
  def setMimeData(
      self,
      data: Optional[QMimeData],
      mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
  ) -> None:
    """
    Calls Qt's 'void QPlatformClipboard::setMimeData(QMimeData *data,
    QClipboard::Mode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformclipboard.html#setMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.
    """
    #  void QPlatformClipboard::setMimeData(QMimeData *data, QClipboard::Mode
    #      mode)
    ritual = (
        'ritual_ZN18QPlatformClipboard11setMimeDataEP9QMimeDataN10QClipboar'
        'd4ModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QPlatformClipboard11setMimeDataEP9QMimeDataN10QCl'
          'ipboard4ModeE')
    self.uglySide.call(ritual, self._addressOf(data), mode.value)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformClipboard::QPlatformClipboard()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformclipboard.html#QPlatformClipboard
    """
    #  QPlatformClipboard::QPlatformClipboard()
    self._noteCreation(QPlatformClipboard, lambda: Rituals.call(
        'ritual_ZN18QPlatformClipboardC1Ev',
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

  @overload()
  @overload(QClipboard.Mode)
  def mimeData(
      self,
      mode: QClipboard.Mode = QClipboard.Mode.Clipboard,
  ) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QPlatformClipboard::mimeData(QClipboard::Mode
    mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformclipboard.html#mimeData

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number. May be left out, as in Qt: it is then
      QClipboard.Mode.Clipboard.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QPlatformClipboard::mimeData(QClipboard::Mode mode)
    ritual = 'ritual_ZN18QPlatformClipboard8mimeDataEN10QClipboard4ModeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QPlatformClipboard8mimeDataEN10QClipboard4ModeE')
    address = self.uglySide.call(ritual, mode.value)
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  @overload(QClipboard.Mode)
  def emitChanged(self, mode: QClipboard.Mode) -> None:
    """
    Calls Qt's 'void QPlatformClipboard::emitChanged(QClipboard::Mode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformclipboard.html#emitChanged

    Parameters
    ----------

    mode : QClipboard.Mode
      Passed on as its number.
    """
    #  void QPlatformClipboard::emitChanged(QClipboard::Mode mode)
    self.uglySide.call(
        'ritual_ZN18QPlatformClipboard11emitChangedEN10QClipboard4ModeE',
        mode.value,
    )
