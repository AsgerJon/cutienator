"""
Qt3DRender::QShaderNodesLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qshadernodesloader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QShaderNodesLoader to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QJsonObject = WAIT['QJsonObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShaderNodesLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QShaderNodesLoader: a plain Python object
  standing in front of one C++ Qt3DRender::QShaderNodesLoader.

  C++ hands a Qt3DRender::QShaderNodesLoader around as a copy, so every C++
  Qt3DRender::QShaderNodesLoader behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QShaderNodesLoader that has a ritual and
  that Python can call so far, 4 names in all: 'status', 'device',
  'setDevice', 'load'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHash<QString, QShaderNode> Qt3DRender::QShaderNodesLoader::nodes()
    const': gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::QShaderNodesLoader::~QShaderNodesLoader()': the
    destructor: Python removes its C++ Qt3DRender::QShaderNodesLoader by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::QShaderNodesLoader is created at the first use, not
    by 'Qt3DRender::QShaderNodesLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QShaderNodesLoader back gives a copy the
    ritual made for Python, in a new cute Qt3DRender::QShaderNodesLoader.
  - Each name of Qt's Qt3DRender::QShaderNodesLoader that has no cute
    function yet, 'nodes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QShaderNodesLoader, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Status(CuteNum):
    """
    The enum 'Qt3DRender::QShaderNodesLoader::Status' of Qt, with the 4 names
    Qt gives in it.
    """

    Null = Kee[int](0)
    Waiting = Kee[int](1)
    Ready = Kee[int](2)
    Error = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QShaderNodesLoader'

  #  Qt's '~Qt3DRender::QShaderNodesLoader()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::QShaderNodesLoader behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender18QShaderNodesLoaderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DRender::QShaderNodesLoader::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernodesloader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DRender::QShaderNodesLoader::status() const
    return QShaderNodesLoader.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QShaderNodesLoader6statusEv',
    ))

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *Qt3DRender::QShaderNodesLoader::device() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernodesloader.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *Qt3DRender::QShaderNodesLoader::device() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender18QShaderNodesLoader6deviceEv',
    )
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNodesLoader::setDevice(QIODevice
    *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernodesloader.html#setDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QShaderNodesLoader::setDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QShaderNodesLoader9setDeviceEP9QIODevice',
        self._addressOf(device),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QShaderNodesLoader::QShaderNodesLoader()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernodesloader.html
    """
    #  Qt3DRender::QShaderNodesLoader::QShaderNodesLoader()
    self._noteCreation(QShaderNodesLoader, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender18QShaderNodesLoaderC1Ev',
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
  def load(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNodesLoader::load()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernodesloader.html#load
    """
    #  void Qt3DRender::QShaderNodesLoader::load()
    self.uglySide.call('ritual_ZN10Qt3DRender18QShaderNodesLoader4loadEv')

  @overload(QJsonObject)
  def load(self, prototypesObject: QJsonObject) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNodesLoader::load(const QJsonObject
    &prototypesObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernodesloader.html#load

    Parameters
    ----------

    prototypesObject : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  void Qt3DRender::QShaderNodesLoader::load(const QJsonObject
    #      &prototypesObject)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender18QShaderNodesLoader4loadERK11QJsonObject',
        self._valueOf(prototypesObject),
    )

  @staticmethod
  def nodes(*__, **_) -> Never:
    """
    Qt's 'QHash<QString, QShaderNode> Qt3DRender::QShaderNodesLoader::nodes()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QShaderNodesLoader.nodes' has no cute function yet. "
        "Qt's 'QHash<QString, QShaderNode> "
        "Qt3DRender::QShaderNodesLoader::nodes() const': gives a type "
        "Python has no way to take yet.")
