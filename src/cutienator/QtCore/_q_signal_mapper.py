"""
QSignalMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsignalmapper.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSignalMapper(QObject):
  """
  The cute side of Qt's QSignalMapper: a plain Python object standing in
  front of one C++ QSignalMapper.

  It is built on the cute 'QObject', as Qt's QSignalMapper is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSignalMapper that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'setMapping',
  'removeMappings', 'mapping', 'map'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSignalMapper::~QSignalMapper()': the destructor: Python never
    removes a C++ QSignalMapper.

  What has no ritual
  ------------------

  11 of the 24 functions Qt declares: 3 private; 3 a signal; 2 takes or gives
  a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QSignalMapper is created at the first use, not by
    'QSignalMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSignalMapper.
  - Qt tells when it has removed the C++ QSignalMapper. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QSignalMapper::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#tr

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
    #  QString QSignalMapper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QSignalMapper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSignalMapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSignalMapper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSignalMapper::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QSignalMapper10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def mapping(self, id: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QSignalMapper::mapping(int id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#mapping

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QSignalMapper::mapping(int id) const
    address = self.uglySide.call('ritual_ZNK13QSignalMapper7mappingEi', id)
    return QObject._cuteAt(address)

  @overload(str)
  def mapping(self, text: str) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QSignalMapper::mapping(const QString &text) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#mapping

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QSignalMapper::mapping(const QString &text) const
    address = self.uglySide.call(
        'ritual_ZNK13QSignalMapper7mappingERK7QString', text,
    )
    return QObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def mapping(self, object: Optional[QObject]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QSignalMapper::mapping(QObject *object) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#mapping

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QSignalMapper::mapping(QObject *object) const
    address = self.uglySide.call(
        'ritual_ZNK13QSignalMapper7mappingEP7QObject',
        self._addressOf(object),
    )
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject, int)
  @overload(NoneType, int)
  def setMapping(self, sender: Optional[QObject], id: int) -> None:
    """
    Calls Qt's 'void QSignalMapper::setMapping(QObject *sender, int id)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#setMapping

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.
    """
    #  void QSignalMapper::setMapping(QObject *sender, int id)
    self.uglySide.call(
        'ritual_ZN13QSignalMapper10setMappingEP7QObjecti',
        self._addressOf(sender), id,
    )

  @overload(QObject, str)
  @overload(NoneType, str)
  def setMapping(self, sender: Optional[QObject], text: str) -> None:
    """
    Calls Qt's 'void QSignalMapper::setMapping(QObject *sender, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#setMapping

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSignalMapper::setMapping(QObject *sender, const QString &text)
    self.uglySide.call(
        'ritual_ZN13QSignalMapper10setMappingEP7QObjectRK7QString',
        self._addressOf(sender), text,
    )

  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def setMapping(
      self,
      sender: Optional[QObject],
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QSignalMapper::setMapping(QObject *sender, QObject
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#setMapping

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSignalMapper::setMapping(QObject *sender, QObject *object)
    self.uglySide.call(
        'ritual_ZN13QSignalMapper10setMappingEP7QObjectS1_',
        self._addressOf(sender), self._addressOf(object),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSignalMapper::QSignalMapper(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#QSignalMapper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSignalMapper::QSignalMapper(QObject *parent)
    self._noteCreation(QSignalMapper, lambda: Rituals.call(
        'ritual_ZN13QSignalMapperC1EP7QObject', self._addressOf(parent),
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

  @overload(QObject)
  @overload(NoneType)
  def removeMappings(self, sender: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QSignalMapper::removeMappings(QObject *sender)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#removeMappings

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSignalMapper::removeMappings(QObject *sender)
    self.uglySide.call(
        'ritual_ZN13QSignalMapper14removeMappingsEP7QObject',
        self._addressOf(sender),
    )

  @overload()
  def map(self) -> None:
    """
    Calls Qt's 'void QSignalMapper::map()'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#map
    """
    #  void QSignalMapper::map()
    self.uglySide.call('ritual_ZN13QSignalMapper3mapEv')

  @overload(QObject)
  @overload(NoneType)
  def map(self, sender: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QSignalMapper::map(QObject *sender)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignalmapper.html#map

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSignalMapper::map(QObject *sender)
    self.uglySide.call(
        'ritual_ZN13QSignalMapper3mapEP7QObject', self._addressOf(sender),
    )
