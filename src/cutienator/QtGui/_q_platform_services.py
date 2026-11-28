"""
QPlatformServices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformservices.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QUrl
  from . import QPlatformServiceColorPicker, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformServices(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformServices: a plain Python object standing in
  front of one C++ QPlatformServices.

  What exists
  -----------

  Every function of Qt's QPlatformServices that has a ritual and that Python
  can call so far, 5 names in all: 'openUrl', 'openDocument',
  'desktopEnvironment', 'hasCapability', 'colorPicker'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformServices::~QPlatformServices()': the destructor: Python
    never removes a C++ QPlatformServices.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPlatformServices is created at the first use, not by
    'QPlatformServices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformServices.
  """

  #  The enums Qt writes inside QPlatformServices, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Capability(CuteNum):
    """
    The enum 'QPlatformServices::Capability' of Qt, with the 1 names Qt gives
    in it.
    """

    ColorPicking = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformServices'

  #  A C++ QPlatformServices Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformServices'

  #  The functions Qt calls itself that QPlatformServices is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'openUrl': (
          ('_ZN17QPlatformServices7openUrlERK4QUrl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'openDocument': (
          ('_ZN17QPlatformServices12openDocumentERK4QUrl',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'desktopEnvironment': (
          ('_ZNK17QPlatformServices18desktopEnvironmentEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
      'hasCapability': (
          ('_ZNK17QPlatformServices13hasCapabilityENS_10CapabilityE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPlatformServices.Capability'),
           )),
      ),
      'colorPicker': (
          ('_ZN17QPlatformServices11colorPickerEP7QWindow',
           ('address', 'address', 'QtGui:QPlatformServiceColorPicker'),
           (
               ('address', 'address', 'QtGui:QWindow'),
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

  def desktopEnvironment(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QPlatformServices::desktopEnvironment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformservices.html#desktopEnvironment

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QPlatformServices::desktopEnvironment() const
    ritual = 'ritual_ZNK17QPlatformServices18desktopEnvironmentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QPlatformServices18desktopEnvironmentEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(Capability)
  def hasCapability(self, capability: Capability) -> bool:
    """
    Calls Qt's 'bool QPlatformServices::hasCapability(Capability capability)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformservices.html#hasCapability

    Parameters
    ----------

    capability : Capability
      Passed on as its number.
    """
    #  bool QPlatformServices::hasCapability(Capability capability) const
    ritual = 'ritual_ZNK17QPlatformServices13hasCapabilityENS_10CapabilityE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QPlatformServices13hasCapabilityENS_10Capability'
          'E')
    return self.uglySide.call(ritual, capability.value)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPlatformServices::QPlatformServices()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformservices.html#QPlatformServices
    """
    #  QPlatformServices::QPlatformServices()
    self._noteCreation(QPlatformServices, lambda: Rituals.call(
        'ritual_ZN17QPlatformServicesC1Ev',
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

  @overload(QUrl)
  def openUrl(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QPlatformServices::openUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformservices.html#openUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QPlatformServices::openUrl(const QUrl &url)
    ritual = 'ritual_ZN17QPlatformServices7openUrlERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPlatformServices7openUrlERK4QUrl'
    return self.uglySide.call(ritual, self._valueOf(url))

  @overload(QUrl)
  def openDocument(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QPlatformServices::openDocument(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformservices.html#openDocument

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QPlatformServices::openDocument(const QUrl &url)
    ritual = 'ritual_ZN17QPlatformServices12openDocumentERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPlatformServices12openDocumentERK4QUrl'
    return self.uglySide.call(ritual, self._valueOf(url))

  @overload()
  @overload(QWindow)
  @overload(NoneType)
  def colorPicker(
      self,
      parent: Optional[QWindow] = None,
  ) -> Optional[QPlatformServiceColorPicker]:
    """
    Calls Qt's 'QPlatformServiceColorPicker
    *QPlatformServices::colorPicker(QWindow *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformservices.html#colorPicker

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QPlatformServiceColorPicker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformServiceColorPicker *QPlatformServices::colorPicker(QWindow
    #      *parent)
    ritual = 'ritual_ZN17QPlatformServices11colorPickerEP7QWindow'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPlatformServices11colorPickerEP7QWindow'
    address = self.uglySide.call(ritual, self._addressOf(parent))
    from . import QPlatformServiceColorPicker
    return QPlatformServiceColorPicker._cuteAt(address)
