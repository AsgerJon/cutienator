"""
QDomDocumentType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDomNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDomDocumentTypePrivate, QDomNamedNodeMap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomDocumentTypePrivate = WAIT['QDomDocumentTypePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomDocumentType(QDomNode):
  """
  The cute side of Qt's QDomDocumentType: a plain Python object standing in
  front of one C++ QDomDocumentType.

  It is built on the cute 'QDomNode', as Qt's QDomDocumentType is built on
  Qt's QDomNode, and has everything that class has.

  C++ hands a QDomDocumentType around as a copy, so every C++
  QDomDocumentType behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomDocumentType that has a ritual and that Python
  can call so far, 7 names in all: 'name', 'entities', 'notations',
  'publicId', 'systemId', 'internalSubset', 'nodeType'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomDocumentType &QDomDocumentType::operator=(const
    QDomDocumentType &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDomDocumentType::~QDomDocumentType()': the destructor: Python
    removes its C++ QDomDocumentType by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomDocumentType is created at the first use, not by
    'QDomDocumentType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomDocumentType back gives a copy the ritual made
    for Python, in a new cute QDomDocumentType.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomDocumentType'

  #  Qt's '~QDomDocumentType()'. Naming it makes this a value class: Python
  #  owns every C++ QDomDocumentType behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QDomDocumentTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QDomDocumentType::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumenttype.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomDocumentType::name() const
    return self.uglySide.call('ritual_ZNK16QDomDocumentType4nameEv')

  def entities(self) -> QDomNamedNodeMap:
    """
    Calls Qt's 'QDomNamedNodeMap QDomDocumentType::entities() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumenttype.html#entities

    Returns
    -------

    QDomNamedNodeMap
      A new cute QDomNamedNodeMap around the copy Qt gave back. Python owns
      it.
    """
    #  QDomNamedNodeMap QDomDocumentType::entities() const
    address = self.uglySide.call('ritual_ZNK16QDomDocumentType8entitiesEv')
    from . import QDomNamedNodeMap
    return QDomNamedNodeMap._cuteOwning(address)

  def notations(self) -> QDomNamedNodeMap:
    """
    Calls Qt's 'QDomNamedNodeMap QDomDocumentType::notations() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumenttype.html#notations

    Returns
    -------

    QDomNamedNodeMap
      A new cute QDomNamedNodeMap around the copy Qt gave back. Python owns
      it.
    """
    #  QDomNamedNodeMap QDomDocumentType::notations() const
    address = self.uglySide.call('ritual_ZNK16QDomDocumentType9notationsEv')
    from . import QDomNamedNodeMap
    return QDomNamedNodeMap._cuteOwning(address)

  def publicId(self) -> str:
    """
    Calls Qt's 'QString QDomDocumentType::publicId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumenttype.html#publicId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomDocumentType::publicId() const
    return self.uglySide.call('ritual_ZNK16QDomDocumentType8publicIdEv')

  def systemId(self) -> str:
    """
    Calls Qt's 'QString QDomDocumentType::systemId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumenttype.html#systemId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomDocumentType::systemId() const
    return self.uglySide.call('ritual_ZNK16QDomDocumentType8systemIdEv')

  def internalSubset(self) -> str:
    """
    Calls Qt's 'QString QDomDocumentType::internalSubset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttype.html#internalSubset

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomDocumentType::internalSubset() const
    return self.uglySide.call(
        'ritual_ZNK16QDomDocumentType14internalSubsetEv',
    )

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomDocumentType::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumenttype.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomDocumentType::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK16QDomDocumentType8nodeTypeEv',
    ))

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
    Notes what was given, for Qt's 'QDomDocumentType::QDomDocumentType()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttype.html#QDomDocumentType
    """
    #  QDomDocumentType::QDomDocumentType()
    self._noteCreation(QDomDocumentType, lambda: Rituals.call(
        'ritual_ZN16QDomDocumentTypeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, documentType: QDomDocumentType) -> None:
    """
    Notes what was given, for Qt's 'QDomDocumentType::QDomDocumentType(const
    QDomDocumentType &documentType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttype.html#QDomDocumentType

    Parameters
    ----------

    documentType : QDomDocumentType
      Passed on as a value: Qt reads the C++ QDomDocumentType, which stays
      Python's own.
    """
    #  QDomDocumentType::QDomDocumentType(const QDomDocumentType
    #      &documentType)
    self._noteCreation(QDomDocumentType, lambda: Rituals.call(
        'ritual_ZN16QDomDocumentTypeC1ERKS_', self._valueOf(documentType),
    ))

  @overload(QDomDocumentTypePrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomDocumentTypePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomDocumentType::QDomDocumentType(QDomDocumentTypePrivate *a0)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumenttype.html#QDomDocumentType

    Parameters
    ----------

    a0 : Optional[QDomDocumentTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomDocumentType::QDomDocumentType(QDomDocumentTypePrivate *a0)
    self._noteCreation(QDomDocumentType, lambda: Rituals.call(
        'ritual_ZN16QDomDocumentTypeC1EP23QDomDocumentTypePrivate',
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
