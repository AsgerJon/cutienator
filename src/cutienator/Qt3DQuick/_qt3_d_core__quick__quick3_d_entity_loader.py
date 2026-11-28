"""
Qt3DCore::Quick::Quick3DEntityLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentityloader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::Quick3DEntityLoader to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQml import QQmlComponent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Quick3DEntityLoader(Qt3DCore.QEntity):
  """
  The cute side of Qt's Qt3DCore::Quick::Quick3DEntityLoader: a plain Python
  object standing in front of one C++ Qt3DCore::Quick::Quick3DEntityLoader.

  It is built on the cute 'Qt3DCore::QEntity', as Qt's
  Qt3DCore::Quick::Quick3DEntityLoader is built on Qt's Qt3DCore::QEntity,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::Quick3DEntityLoader that has a
  ritual and that Python can call so far, 13 names in all: 'metaObject',
  'tr', 'entity', 'source', 'setSource', 'sourceComponent',
  'setSourceComponent', 'status', 'entityChanged', 'sourceChanged',
  'sourceComponentChanged', 'statusChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::Quick::Quick3DEntityLoader::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::Quick::Quick3DEntityLoader::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::Quick::Quick3DEntityLoader::~Quick3DEntityLoader()': the
    destructor: Python never removes a C++
    Qt3DCore::Quick::Quick3DEntityLoader.
  - Qt's 'const Quick3DEntityLoaderPrivate
    *Qt3DCore::Quick::Quick3DEntityLoader::d_func() const': takes in Python
    what 'Quick3DEntityLoaderPrivate
    *Qt3DCore::Quick::Quick3DEntityLoader::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::Quick3DEntityLoader is created at the first use,
    not by 'Qt3DCore::Quick::Quick3DEntityLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Quick::Quick3DEntityLoader.
  - Qt tells when it has removed the C++
    Qt3DCore::Quick::Quick3DEntityLoader. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  #  The enums Qt writes inside Qt3DCore::Quick::Quick3DEntityLoader, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Status(CuteNum):
    """
    The enum 'Qt3DCore::Quick::Quick3DEntityLoader::Status' of Qt, with the 4
    names Qt gives in it.
    """

    Null = Kee[int](0)
    Loading = Kee[int](1)
    Ready = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString Qt3DCore::Quick::Quick3DEntityLoader::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html#tr

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
    #  QString Qt3DCore::Quick::Quick3DEntityLoader::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::Quick3DEntityLoader'

  #  A C++ Qt3DCore::Quick::Quick3DEntityLoader Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_Quick_Quick3DEntityLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::Quick::Quick3DEntityLoader::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::Quick::Quick3DEntityLoader::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def entity(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *Qt3DCore::Quick::Quick3DEntityLoader::entity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html#entity

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *Qt3DCore::Quick::Quick3DEntityLoader::entity() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader6entityEv',
    )
    return QObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DCore::Quick::Quick3DEntityLoader::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DCore::Quick::Quick3DEntityLoader::source() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sourceComponent(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent
    *Qt3DCore::Quick::Quick3DEntityLoader::sourceComponent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *Qt3DCore::Quick::Quick3DEntityLoader::sourceComponent()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader15sourceComponentEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DCore::Quick::Quick3DEntityLoader::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DCore::Quick::Quick3DEntityLoader::status() const
    return Quick3DEntityLoader.Status(self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick19Quick3DEntityLoader6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DEntityLoader::setSource(const
    QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DCore::Quick::Quick3DEntityLoader::setSource(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader9setSourceERK4QUrl',
        self._valueOf(url),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setSourceComponent(self, components: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DEntityLoader::setSourceComponent(QQmlComponent
    *components)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html

    Parameters
    ----------

    components : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::Quick::Quick3DEntityLoader::setSourceComponent(
    #      QQmlComponent *components)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader18setSourceComponentE'
        'P13QQmlComponent',
        self._addressOf(components),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::Quick::Quick3DEntityLoader::Quick3DEntityLoader(QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::Quick::Quick3DEntityLoader::Quick3DEntityLoader(QNode
    #      *parent)
    self._noteCreation(Quick3DEntityLoader, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoaderC1EPNS_5QNodeE',
        self._addressOf(parent),
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

  def entityChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DEntityLoader::entityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html
    """
    #  void Qt3DCore::Quick::Quick3DEntityLoader::entityChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader13entityChangedEv',
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DEntityLoader::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html
    """
    #  void Qt3DCore::Quick::Quick3DEntityLoader::sourceChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader13sourceChangedEv',
    )

  def sourceComponentChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DEntityLoader::sourceComponentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html
    """
    #  void Qt3DCore::Quick::Quick3DEntityLoader::sourceComponentChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader22sourceComponentChan'
        'gedEv',
    )

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::Quick::Quick3DEntityLoader::statusChanged(Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DCore::Quick::Quick3DEntityLoader::statusChanged(Status
    #      status)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader13statusChangedENS1_6'
        'StatusE',
        status.value,
    )

  def d_func(self) -> Optional[Qt3DCore.Quick.Quick3DEntityLoaderPrivate]:
    """
    Calls Qt's 'Quick3DEntityLoaderPrivate
    *Qt3DCore::Quick::Quick3DEntityLoader::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloader.html#d_func

    Returns
    -------

    Optional[Qt3DCore.Quick.Quick3DEntityLoaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Quick3DEntityLoaderPrivate
    #      *Qt3DCore::Quick::Quick3DEntityLoader::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick19Quick3DEntityLoader6d_funcEv',
    )
    return Qt3DCore.Quick.Quick3DEntityLoaderPrivate._cuteAt(address)
