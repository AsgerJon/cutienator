"""
QDomNamedNodeMapPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomNamedNodeMapPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomNodePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomNodePrivate = WAIT['QDomNodePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomNamedNodeMapPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomNamedNodeMapPrivate: a plain Python object
  standing in front of one C++ QDomNamedNodeMapPrivate.

  C++ hands a QDomNamedNodeMapPrivate around as a copy, so every C++
  QDomNamedNodeMapPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomNamedNodeMapPrivate that has a ritual and that
  Python can call so far, 15 names in all: 'namedItem', 'namedItemNS',
  'setNamedItem', 'setNamedItemNS', 'removeNamedItem', 'item', 'length',
  'contains', 'containsNS', 'clearMap', 'isReadOnly', 'setReadOnly',
  'isAppendToParent', 'setAppendToParent', 'clone'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomNamedNodeMapPrivate::~QDomNamedNodeMapPrivate()': the
    destructor: Python removes its C++ QDomNamedNodeMapPrivate by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QDomNamedNodeMapPrivate is created at the first use, not by
    'QDomNamedNodeMapPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomNamedNodeMapPrivate back gives a copy the ritual
    made for Python, in a new cute QDomNamedNodeMapPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomNamedNodeMapPrivate'

  #  Qt's '~QDomNamedNodeMapPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QDomNamedNodeMapPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QDomNamedNodeMapPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def namedItem(self, name: str) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNamedNodeMapPrivate::namedItem(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#namedItem

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNamedNodeMapPrivate::namedItem(const QString
    #      &name) const
    address = self.uglySide.call(
        'ritual_ZNK23QDomNamedNodeMapPrivate9namedItemERK7QString', name,
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  @overload(str, str)
  def namedItemNS(
      self,
      nsURI: str,
      localName: str,
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNamedNodeMapPrivate::namedItemNS(const
    QString &nsURI, const QString &localName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#namedItemNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNamedNodeMapPrivate::namedItemNS(const QString
    #      &nsURI, const QString &localName) const
    address = self.uglySide.call(
        'ritual_ZNK23QDomNamedNodeMapPrivate11namedItemNSERK7QStringS2_',
        nsURI, localName,
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  @overload(int)
  def item(self, index: int) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNamedNodeMapPrivate::item(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#item

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNamedNodeMapPrivate::item(int index) const
    address = self.uglySide.call(
        'ritual_ZNK23QDomNamedNodeMapPrivate4itemEi', index,
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  def length(self) -> int:
    """
    Calls Qt's 'int QDomNamedNodeMapPrivate::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#length
    """
    #  int QDomNamedNodeMapPrivate::length() const
    return self.uglySide.call('ritual_ZNK23QDomNamedNodeMapPrivate6lengthEv')

  @overload(str)
  def contains(self, name: str) -> bool:
    """
    Calls Qt's 'bool QDomNamedNodeMapPrivate::contains(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#contains

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomNamedNodeMapPrivate::contains(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK23QDomNamedNodeMapPrivate8containsERK7QString', name,
    )

  @overload(str, str)
  def containsNS(self, nsURI: str, localName: str) -> bool:
    """
    Calls Qt's 'bool QDomNamedNodeMapPrivate::containsNS(const QString
    &nsURI, const QString &localName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#containsNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomNamedNodeMapPrivate::containsNS(const QString &nsURI, const
    #      QString &localName) const
    return self.uglySide.call(
        'ritual_ZNK23QDomNamedNodeMapPrivate10containsNSERK7QStringS2_',
        nsURI, localName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def setNamedItem(
      self,
      arg: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomNamedNodeMapPrivate::setNamedItem(QDomNodePrivate *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#setNamedItem

    Parameters
    ----------

    arg : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNamedNodeMapPrivate::setNamedItem(QDomNodePrivate
    #      *arg)
    address = self.uglySide.call(
        'ritual_ZN23QDomNamedNodeMapPrivate12setNamedItemEP15QDomNodePrivat'
        'e',
        self._addressOf(arg),
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def setNamedItemNS(
      self,
      arg: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomNamedNodeMapPrivate::setNamedItemNS(QDomNodePrivate *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#setNamedItemNS

    Parameters
    ----------

    arg : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate
    #      *QDomNamedNodeMapPrivate::setNamedItemNS(QDomNodePrivate *arg)
    address = self.uglySide.call(
        'ritual_ZN23QDomNamedNodeMapPrivate14setNamedItemNSEP15QDomNodePriv'
        'ate',
        self._addressOf(arg),
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  @overload(bool)
  def setReadOnly(self, r: bool) -> None:
    """
    Calls Qt's 'void QDomNamedNodeMapPrivate::setReadOnly(bool r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#setReadOnly

    Parameters
    ----------

    r : bool
      Passed on as it is.
    """
    #  void QDomNamedNodeMapPrivate::setReadOnly(bool r)
    self.uglySide.call(
        'ritual_ZN23QDomNamedNodeMapPrivate11setReadOnlyEb', r,
    )

  @overload(bool)
  def setAppendToParent(self, b: bool) -> None:
    """
    Calls Qt's 'void QDomNamedNodeMapPrivate::setAppendToParent(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#setAppendToParent

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QDomNamedNodeMapPrivate::setAppendToParent(bool b)
    self.uglySide.call(
        'ritual_ZN23QDomNamedNodeMapPrivate17setAppendToParentEb', b,
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

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomNodePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomNamedNodeMapPrivate::QDomNamedNodeMapPrivate(QDomNodePrivate *a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html

    Parameters
    ----------

    a0 : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomNamedNodeMapPrivate::QDomNamedNodeMapPrivate(QDomNodePrivate *a0)
    self._noteCreation(QDomNamedNodeMapPrivate, lambda: Rituals.call(
        'ritual_ZN23QDomNamedNodeMapPrivateC1EP15QDomNodePrivate',
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
  def removeNamedItem(self, name: str) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomNamedNodeMapPrivate::removeNamedItem(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#removeNamedItem

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNamedNodeMapPrivate::removeNamedItem(const
    #      QString &name)
    address = self.uglySide.call(
        'ritual_ZN23QDomNamedNodeMapPrivate15removeNamedItemERK7QString',
        name,
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  def clearMap(self) -> None:
    """
    Calls Qt's 'void QDomNamedNodeMapPrivate::clearMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#clearMap
    """
    #  void QDomNamedNodeMapPrivate::clearMap()
    self.uglySide.call('ritual_ZN23QDomNamedNodeMapPrivate8clearMapEv')

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QDomNamedNodeMapPrivate::isReadOnly()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#isReadOnly
    """
    #  bool QDomNamedNodeMapPrivate::isReadOnly()
    return self.uglySide.call(
        'ritual_ZN23QDomNamedNodeMapPrivate10isReadOnlyEv',
    )

  def isAppendToParent(self) -> bool:
    """
    Calls Qt's 'bool QDomNamedNodeMapPrivate::isAppendToParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#isAppendToParent
    """
    #  bool QDomNamedNodeMapPrivate::isAppendToParent()
    return self.uglySide.call(
        'ritual_ZN23QDomNamedNodeMapPrivate16isAppendToParentEv',
    )

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def clone(
      self,
      parent: Optional[QDomNodePrivate],
  ) -> Optional[QDomNamedNodeMapPrivate]:
    """
    Calls Qt's 'QDomNamedNodeMapPrivate
    *QDomNamedNodeMapPrivate::clone(QDomNodePrivate *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnamednodemapprivate.html#clone

    Parameters
    ----------

    parent : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNamedNodeMapPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNamedNodeMapPrivate
    #      *QDomNamedNodeMapPrivate::clone(QDomNodePrivate *parent)
    address = self.uglySide.call(
        'ritual_ZN23QDomNamedNodeMapPrivate5cloneEP15QDomNodePrivate',
        self._addressOf(parent),
    )
    return QDomNamedNodeMapPrivate._cuteAt(address)
