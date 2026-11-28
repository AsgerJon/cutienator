"""
QDomNamedNodeMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomNamedNodeMapPrivate, QDomNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomNamedNodeMapPrivate = WAIT['QDomNamedNodeMapPrivate']
  QDomNode = WAIT['QDomNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomNamedNodeMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomNamedNodeMap: a plain Python object standing in
  front of one C++ QDomNamedNodeMap.

  C++ hands a QDomNamedNodeMap around as a copy, so every C++
  QDomNamedNodeMap behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomNamedNodeMap that has a ritual and that Python
  can call so far, 14 names in all: '__eq__', '__ne__', 'namedItem',
  'setNamedItem', 'removeNamedItem', 'item', 'namedItemNS', 'setNamedItemNS',
  'removeNamedItemNS', 'length', 'count', 'size', 'isEmpty', 'contains'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomNamedNodeMap &QDomNamedNodeMap::operator=(const
    QDomNamedNodeMap &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDomNamedNodeMap::~QDomNamedNodeMap()': the destructor: Python
    removes its C++ QDomNamedNodeMap by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomNamedNodeMap is created at the first use, not by
    'QDomNamedNodeMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomNamedNodeMap back gives a copy the ritual made
    for Python, in a new cute QDomNamedNodeMap.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomNamedNodeMap'

  #  Qt's '~QDomNamedNodeMap()'. Naming it makes this a value class: Python
  #  owns every C++ QDomNamedNodeMap behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QDomNamedNodeMapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def namedItem(self, name: str) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNamedNodeMap::namedItem(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#namedItem

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNamedNodeMap::namedItem(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK16QDomNamedNodeMap9namedItemERK7QString', name,
    )
    from . import QDomNode
    return QDomNode._cuteOwning(address)

  @overload(int)
  def item(self, index: int) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNamedNodeMap::item(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#item

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNamedNodeMap::item(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QDomNamedNodeMap4itemEi', index,
    )
    from . import QDomNode
    return QDomNode._cuteOwning(address)

  @overload(str, str)
  def namedItemNS(self, nsURI: str, localName: str) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNamedNodeMap::namedItemNS(const QString &nsURI,
    const QString &localName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#namedItemNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNamedNodeMap::namedItemNS(const QString &nsURI, const
    #      QString &localName) const
    address = self.uglySide.call(
        'ritual_ZNK16QDomNamedNodeMap11namedItemNSERK7QStringS2_',
        nsURI, localName,
    )
    from . import QDomNode
    return QDomNode._cuteOwning(address)

  def length(self) -> int:
    """
    Calls Qt's 'int QDomNamedNodeMap::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#length
    """
    #  int QDomNamedNodeMap::length() const
    return self.uglySide.call('ritual_ZNK16QDomNamedNodeMap6lengthEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QDomNamedNodeMap::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#count
    """
    #  int QDomNamedNodeMap::count() const
    return self.uglySide.call('ritual_ZNK16QDomNamedNodeMap5countEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QDomNamedNodeMap::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#size
    """
    #  int QDomNamedNodeMap::size() const
    return self.uglySide.call('ritual_ZNK16QDomNamedNodeMap4sizeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QDomNamedNodeMap::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#isEmpty
    """
    #  bool QDomNamedNodeMap::isEmpty() const
    return self.uglySide.call('ritual_ZNK16QDomNamedNodeMap7isEmptyEv')

  @overload(str)
  def contains(self, name: str) -> bool:
    """
    Calls Qt's 'bool QDomNamedNodeMap::contains(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#contains

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomNamedNodeMap::contains(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK16QDomNamedNodeMap8containsERK7QString', name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDomNode)
  def setNamedItem(self, newNode: QDomNode) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNamedNodeMap::setNamedItem(const QDomNode
    &newNode)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#setNamedItem

    Parameters
    ----------

    newNode : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNamedNodeMap::setNamedItem(const QDomNode &newNode)
    address = self.uglySide.call(
        'ritual_ZN16QDomNamedNodeMap12setNamedItemERK8QDomNode',
        self._valueOf(newNode),
    )
    from . import QDomNode
    return QDomNode._cuteOwning(address)

  @overload(QDomNode)
  def setNamedItemNS(self, newNode: QDomNode) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNamedNodeMap::setNamedItemNS(const QDomNode
    &newNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemap.html#setNamedItemNS

    Parameters
    ----------

    newNode : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNamedNodeMap::setNamedItemNS(const QDomNode &newNode)
    address = self.uglySide.call(
        'ritual_ZN16QDomNamedNodeMap14setNamedItemNSERK8QDomNode',
        self._valueOf(newNode),
    )
    from . import QDomNode
    return QDomNode._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QDomNamedNodeMap) -> bool:
    """
    Calls Qt's 'bool QDomNamedNodeMap::operator==(const QDomNamedNodeMap
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#operator==

    Parameters
    ----------

    other : QDomNamedNodeMap
      Passed on as a value: Qt reads the C++ QDomNamedNodeMap, which stays
      Python's own.
    """
    #  bool QDomNamedNodeMap::operator==(const QDomNamedNodeMap &other) const
    return self.uglySide.call(
        'ritual_ZNK16QDomNamedNodeMapeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QDomNamedNodeMap) -> bool:
    """
    Calls Qt's 'bool QDomNamedNodeMap::operator!=(const QDomNamedNodeMap
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemap.html#operator!=

    Parameters
    ----------

    other : QDomNamedNodeMap
      Passed on as a value: Qt reads the C++ QDomNamedNodeMap, which stays
      Python's own.
    """
    #  bool QDomNamedNodeMap::operator!=(const QDomNamedNodeMap &other) const
    return self.uglySide.call(
        'ritual_ZNK16QDomNamedNodeMapneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDomNamedNodeMap::QDomNamedNodeMap()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemap.html#QDomNamedNodeMap
    """
    #  QDomNamedNodeMap::QDomNamedNodeMap()
    self._noteCreation(QDomNamedNodeMap, lambda: Rituals.call(
        'ritual_ZN16QDomNamedNodeMapC1Ev',
    ))

  @overload(THIS)
  def __init__(self, namedNodeMap: QDomNamedNodeMap) -> None:
    """
    Notes what was given, for Qt's 'QDomNamedNodeMap::QDomNamedNodeMap(const
    QDomNamedNodeMap &namedNodeMap)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemap.html#QDomNamedNodeMap

    Parameters
    ----------

    namedNodeMap : QDomNamedNodeMap
      Passed on as a value: Qt reads the C++ QDomNamedNodeMap, which stays
      Python's own.
    """
    #  QDomNamedNodeMap::QDomNamedNodeMap(const QDomNamedNodeMap
    #      &namedNodeMap)
    self._noteCreation(QDomNamedNodeMap, lambda: Rituals.call(
        'ritual_ZN16QDomNamedNodeMapC1ERKS_', self._valueOf(namedNodeMap),
    ))

  @overload(QDomNamedNodeMapPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomNamedNodeMapPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomNamedNodeMap::QDomNamedNodeMap(QDomNamedNodeMapPrivate *a0)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemap.html#QDomNamedNodeMap

    Parameters
    ----------

    a0 : Optional[QDomNamedNodeMapPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomNamedNodeMap::QDomNamedNodeMap(QDomNamedNodeMapPrivate *a0)
    self._noteCreation(QDomNamedNodeMap, lambda: Rituals.call(
        'ritual_ZN16QDomNamedNodeMapC1EP23QDomNamedNodeMapPrivate',
        self._addressOf(a0),
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

  @overload(str)
  def removeNamedItem(self, name: str) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNamedNodeMap::removeNamedItem(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemap.html#removeNamedItem

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNamedNodeMap::removeNamedItem(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN16QDomNamedNodeMap15removeNamedItemERK7QString', name,
    )
    from . import QDomNode
    return QDomNode._cuteOwning(address)

  @overload(str, str)
  def removeNamedItemNS(self, nsURI: str, localName: str) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNamedNodeMap::removeNamedItemNS(const QString
    &nsURI, const QString &localName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemap.html#removeNamedItemNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNamedNodeMap::removeNamedItemNS(const QString &nsURI,
    #      const QString &localName)
    address = self.uglySide.call(
        'ritual_ZN16QDomNamedNodeMap17removeNamedItemNSERK7QStringS2_',
        nsURI, localName,
    )
    from . import QDomNode
    return QDomNode._cuteOwning(address)
