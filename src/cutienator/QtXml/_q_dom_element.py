"""
QDomElement binding of the Qt C++
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

  from . import QDomAttr, QDomElementPrivate, QDomNamedNodeMap, QDomNodeList
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomAttr = WAIT['QDomAttr']
  QDomElementPrivate = WAIT['QDomElementPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomElement(QDomNode):
  """
  The cute side of Qt's QDomElement: a plain Python object standing in front
  of one C++ QDomElement.

  It is built on the cute 'QDomNode', as Qt's QDomElement is built on Qt's
  QDomNode, and has everything that class has.

  C++ hands a QDomElement around as a copy, so every C++ QDomElement behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomElement that has a ritual and that Python can
  call so far, 20 names in all: 'attribute', 'setAttribute',
  'removeAttribute', 'attributeNode', 'setAttributeNode',
  'removeAttributeNode', 'elementsByTagName', 'hasAttribute', 'attributeNS',
  'setAttributeNS', 'removeAttributeNS', 'attributeNodeNS',
  'setAttributeNodeNS', 'elementsByTagNameNS', 'hasAttributeNS', 'tagName',
  'setTagName', 'attributes', 'nodeType', 'text'. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomElement &QDomElement::operator=(const QDomElement &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QDomElement::setAttribute(const QString &name, qulonglong
    value)': takes in Python what 'void QDomElement::setAttribute(const
    QString &name, qlonglong value)' takes.
  - Qt's 'void QDomElement::setAttribute(const QString &name, int value)':
    takes in Python what 'void QDomElement::setAttribute(const QString &name,
    qlonglong value)' takes.
  - Qt's 'void QDomElement::setAttribute(const QString &name, uint value)':
    takes in Python what 'void QDomElement::setAttribute(const QString &name,
    qlonglong value)' takes.
  - Qt's 'void QDomElement::setAttribute(const QString &name, double value)':
    takes in Python what 'void QDomElement::setAttribute(const QString &name,
    float value)' takes.
  - Qt's 'void QDomElement::setAttributeNS(const QString &nsURI, const
    QString &qName, uint value)': takes in Python what 'void
    QDomElement::setAttributeNS(const QString &nsURI, const QString &qName,
    int value)' takes.
  - Qt's 'void QDomElement::setAttributeNS(const QString &nsURI, const
    QString &qName, qlonglong value)': takes in Python what 'void
    QDomElement::setAttributeNS(const QString &nsURI, const QString &qName,
    int value)' takes.
  - Qt's 'void QDomElement::setAttributeNS(const QString &nsURI, const
    QString &qName, qulonglong value)': takes in Python what 'void
    QDomElement::setAttributeNS(const QString &nsURI, const QString &qName,
    int value)' takes.
  - Qt's 'QDomElement::~QDomElement()': the destructor: Python removes its
    C++ QDomElement by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomElement is created at the first use, not by
    'QDomElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomElement back gives a copy the ritual made for
    Python, in a new cute QDomElement.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomElement'

  #  Qt's '~QDomElement()'. Naming it makes this a value class: Python owns
  #  every C++ QDomElement behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QDomElementD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, str)
  def attribute(self, name: str, defValue: str = '') -> str:
    """
    Calls Qt's 'QString QDomElement::attribute(const QString &name, const
    QString &defValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#attribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    defValue : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomElement::attribute(const QString &name, const QString
    #      &defValue) const
    return self.uglySide.call(
        'ritual_ZNK11QDomElement9attributeERK7QStringS2_', name, defValue,
    )

  @overload(str)
  def elementsByTagName(self, tagname: str) -> QDomNodeList:
    """
    Calls Qt's 'QDomNodeList QDomElement::elementsByTagName(const QString
    &tagname) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#elementsByTagName

    Parameters
    ----------

    tagname : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNodeList
      A new cute QDomNodeList around the copy Qt gave back. Python owns it.
    """
    #  QDomNodeList QDomElement::elementsByTagName(const QString &tagname)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QDomElement17elementsByTagNameERK7QString', tagname,
    )
    from . import QDomNodeList
    return QDomNodeList._cuteOwning(address)

  @overload(str)
  def hasAttribute(self, name: str) -> bool:
    """
    Calls Qt's 'bool QDomElement::hasAttribute(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#hasAttribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomElement::hasAttribute(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK11QDomElement12hasAttributeERK7QString', name,
    )

  @overload(str, str)
  @overload(str, str, str)
  def attributeNS(
      self,
      nsURI: str,
      localName: str,
      defValue: str = '',
  ) -> str:
    """
    Calls Qt's 'QString QDomElement::attributeNS(const QString &nsURI, const
    QString &localName, const QString &defValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#attributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    defValue : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomElement::attributeNS(const QString &nsURI, const QString
    #      &localName, const QString &defValue) const
    return self.uglySide.call(
        'ritual_ZNK11QDomElement11attributeNSERK7QStringS2_S2_',
        nsURI, localName, defValue,
    )

  @overload(str, str)
  def elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList:
    """
    Calls Qt's 'QDomNodeList QDomElement::elementsByTagNameNS(const QString
    &nsURI, const QString &localName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelement.html#elementsByTagNameNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNodeList
      A new cute QDomNodeList around the copy Qt gave back. Python owns it.
    """
    #  QDomNodeList QDomElement::elementsByTagNameNS(const QString &nsURI,
    #      const QString &localName) const
    address = self.uglySide.call(
        'ritual_ZNK11QDomElement19elementsByTagNameNSERK7QStringS2_',
        nsURI, localName,
    )
    from . import QDomNodeList
    return QDomNodeList._cuteOwning(address)

  @overload(str, str)
  def hasAttributeNS(self, nsURI: str, localName: str) -> bool:
    """
    Calls Qt's 'bool QDomElement::hasAttributeNS(const QString &nsURI, const
    QString &localName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#hasAttributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomElement::hasAttributeNS(const QString &nsURI, const QString
    #      &localName) const
    return self.uglySide.call(
        'ritual_ZNK11QDomElement14hasAttributeNSERK7QStringS2_',
        nsURI, localName,
    )

  def tagName(self) -> str:
    """
    Calls Qt's 'QString QDomElement::tagName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#tagName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomElement::tagName() const
    return self.uglySide.call('ritual_ZNK11QDomElement7tagNameEv')

  def attributes(self) -> QDomNamedNodeMap:
    """
    Calls Qt's 'QDomNamedNodeMap QDomElement::attributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#attributes

    Returns
    -------

    QDomNamedNodeMap
      A new cute QDomNamedNodeMap around the copy Qt gave back. Python owns
      it.
    """
    #  QDomNamedNodeMap QDomElement::attributes() const
    address = self.uglySide.call('ritual_ZNK11QDomElement10attributesEv')
    from . import QDomNamedNodeMap
    return QDomNamedNodeMap._cuteOwning(address)

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomElement::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomElement::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK11QDomElement8nodeTypeEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString QDomElement::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomElement::text() const
    return self.uglySide.call('ritual_ZNK11QDomElement4textEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def setAttribute(self, name: str, value: str) -> None:
    """
    Calls Qt's 'void QDomElement::setAttribute(const QString &name, const
    QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#setAttribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomElement::setAttribute(const QString &name, const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN11QDomElement12setAttributeERK7QStringS2_', name, value,
    )

  @overload(str, int)
  def setAttribute(self, name: str, value: int) -> None:
    """
    Calls Qt's 'void QDomElement::setAttribute(const QString &name, qlonglong
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#setAttribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : int
      Passed on as it is.
    """
    #  void QDomElement::setAttribute(const QString &name, qlonglong value)
    self.uglySide.call(
        'ritual_ZN11QDomElement12setAttributeERK7QStringx', name, value,
    )

  @overload(str, float)
  def setAttribute(self, name: str, value: float) -> None:
    """
    Calls Qt's 'void QDomElement::setAttribute(const QString &name, float
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#setAttribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : float
      Passed on as it is.
    """
    #  void QDomElement::setAttribute(const QString &name, float value)
    self.uglySide.call(
        'ritual_ZN11QDomElement12setAttributeERK7QStringf', name, value,
    )

  @overload(QDomAttr)
  def setAttributeNode(self, newAttr: QDomAttr) -> QDomAttr:
    """
    Calls Qt's 'QDomAttr QDomElement::setAttributeNode(const QDomAttr
    &newAttr)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#setAttributeNode

    Parameters
    ----------

    newAttr : QDomAttr
      Passed on as a value: Qt reads the C++ QDomAttr, which stays Python's
      own.

    Returns
    -------

    QDomAttr
      A new cute QDomAttr around the copy Qt gave back. Python owns it.
    """
    #  QDomAttr QDomElement::setAttributeNode(const QDomAttr &newAttr)
    address = self.uglySide.call(
        'ritual_ZN11QDomElement16setAttributeNodeERK8QDomAttr',
        self._valueOf(newAttr),
    )
    from . import QDomAttr
    return QDomAttr._cuteOwning(address)

  @overload(str, str, str)
  def setAttributeNS(self, nsURI: str, qName: str, value: str) -> None:
    """
    Calls Qt's 'void QDomElement::setAttributeNS(const QString &nsURI, const
    QString &qName, const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#setAttributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomElement::setAttributeNS(const QString &nsURI, const QString
    #      &qName, const QString &value)
    self.uglySide.call(
        'ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_S2_',
        nsURI, qName, value,
    )

  @overload(str, str, int)
  def setAttributeNS(self, nsURI: str, qName: str, value: int) -> None:
    """
    Calls Qt's 'void QDomElement::setAttributeNS(const QString &nsURI, const
    QString &qName, int value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#setAttributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.

    value : int
      Passed on as it is.
    """
    #  void QDomElement::setAttributeNS(const QString &nsURI, const QString
    #      &qName, int value)
    self.uglySide.call(
        'ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_i',
        nsURI, qName, value,
    )

  @overload(str, str, float)
  def setAttributeNS(self, nsURI: str, qName: str, value: float) -> None:
    """
    Calls Qt's 'void QDomElement::setAttributeNS(const QString &nsURI, const
    QString &qName, double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#setAttributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    qName : str
      Passed on as it is: a QString is made of it for the call.

    value : float
      Passed on as it is.
    """
    #  void QDomElement::setAttributeNS(const QString &nsURI, const QString
    #      &qName, double value)
    self.uglySide.call(
        'ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_d',
        nsURI, qName, value,
    )

  @overload(QDomAttr)
  def setAttributeNodeNS(self, newAttr: QDomAttr) -> QDomAttr:
    """
    Calls Qt's 'QDomAttr QDomElement::setAttributeNodeNS(const QDomAttr
    &newAttr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelement.html#setAttributeNodeNS

    Parameters
    ----------

    newAttr : QDomAttr
      Passed on as a value: Qt reads the C++ QDomAttr, which stays Python's
      own.

    Returns
    -------

    QDomAttr
      A new cute QDomAttr around the copy Qt gave back. Python owns it.
    """
    #  QDomAttr QDomElement::setAttributeNodeNS(const QDomAttr &newAttr)
    address = self.uglySide.call(
        'ritual_ZN11QDomElement18setAttributeNodeNSERK8QDomAttr',
        self._valueOf(newAttr),
    )
    from . import QDomAttr
    return QDomAttr._cuteOwning(address)

  @overload(str)
  def setTagName(self, name: str) -> None:
    """
    Calls Qt's 'void QDomElement::setTagName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#setTagName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomElement::setTagName(const QString &name)
    self.uglySide.call('ritual_ZN11QDomElement10setTagNameERK7QString', name)

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
    Notes what was given, for Qt's 'QDomElement::QDomElement()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#QDomElement
    """
    #  QDomElement::QDomElement()
    self._noteCreation(QDomElement, lambda: Rituals.call(
        'ritual_ZN11QDomElementC1Ev',
    ))

  @overload(THIS)
  def __init__(self, element: QDomElement) -> None:
    """
    Notes what was given, for Qt's 'QDomElement::QDomElement(const
    QDomElement &element)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#QDomElement

    Parameters
    ----------

    element : QDomElement
      Passed on as a value: Qt reads the C++ QDomElement, which stays
      Python's own.
    """
    #  QDomElement::QDomElement(const QDomElement &element)
    self._noteCreation(QDomElement, lambda: Rituals.call(
        'ritual_ZN11QDomElementC1ERKS_', self._valueOf(element),
    ))

  @overload(QDomElementPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomElementPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomElement::QDomElement(QDomElementPrivate *a0)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#QDomElement

    Parameters
    ----------

    a0 : Optional[QDomElementPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomElement::QDomElement(QDomElementPrivate *a0)
    self._noteCreation(QDomElement, lambda: Rituals.call(
        'ritual_ZN11QDomElementC1EP18QDomElementPrivate',
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
  def removeAttribute(self, name: str) -> None:
    """
    Calls Qt's 'void QDomElement::removeAttribute(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#removeAttribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomElement::removeAttribute(const QString &name)
    self.uglySide.call(
        'ritual_ZN11QDomElement15removeAttributeERK7QString', name,
    )

  @overload(str)
  def attributeNode(self, name: str) -> QDomAttr:
    """
    Calls Qt's 'QDomAttr QDomElement::attributeNode(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#attributeNode

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomAttr
      A new cute QDomAttr around the copy Qt gave back. Python owns it.
    """
    #  QDomAttr QDomElement::attributeNode(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN11QDomElement13attributeNodeERK7QString', name,
    )
    from . import QDomAttr
    return QDomAttr._cuteOwning(address)

  @overload(QDomAttr)
  def removeAttributeNode(self, oldAttr: QDomAttr) -> QDomAttr:
    """
    Calls Qt's 'QDomAttr QDomElement::removeAttributeNode(const QDomAttr
    &oldAttr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelement.html#removeAttributeNode

    Parameters
    ----------

    oldAttr : QDomAttr
      Passed on as a value: Qt reads the C++ QDomAttr, which stays Python's
      own.

    Returns
    -------

    QDomAttr
      A new cute QDomAttr around the copy Qt gave back. Python owns it.
    """
    #  QDomAttr QDomElement::removeAttributeNode(const QDomAttr &oldAttr)
    address = self.uglySide.call(
        'ritual_ZN11QDomElement19removeAttributeNodeERK8QDomAttr',
        self._valueOf(oldAttr),
    )
    from . import QDomAttr
    return QDomAttr._cuteOwning(address)

  @overload(str, str)
  def removeAttributeNS(self, nsURI: str, localName: str) -> None:
    """
    Calls Qt's 'void QDomElement::removeAttributeNS(const QString &nsURI,
    const QString &localName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#removeAttributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomElement::removeAttributeNS(const QString &nsURI, const
    #      QString &localName)
    self.uglySide.call(
        'ritual_ZN11QDomElement17removeAttributeNSERK7QStringS2_',
        nsURI, localName,
    )

  @overload(str, str)
  def attributeNodeNS(self, nsURI: str, localName: str) -> QDomAttr:
    """
    Calls Qt's 'QDomAttr QDomElement::attributeNodeNS(const QString &nsURI,
    const QString &localName)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelement.html#attributeNodeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomAttr
      A new cute QDomAttr around the copy Qt gave back. Python owns it.
    """
    #  QDomAttr QDomElement::attributeNodeNS(const QString &nsURI, const
    #      QString &localName)
    address = self.uglySide.call(
        'ritual_ZN11QDomElement15attributeNodeNSERK7QStringS2_',
        nsURI, localName,
    )
    from . import QDomAttr
    return QDomAttr._cuteOwning(address)
