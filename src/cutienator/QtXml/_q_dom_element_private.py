"""
QDomElementPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomElementPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QDomNode, QDomNodePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDomAttrPrivate, QDomNamedNodeMapPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomAttrPrivate = WAIT['QDomAttrPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomElementPrivate(QDomNodePrivate):
  """
  The cute side of Qt's QDomElementPrivate: a plain Python object standing in
  front of one C++ QDomElementPrivate.

  It is built on the cute 'QDomNodePrivate', as Qt's QDomElementPrivate is
  built on Qt's QDomNodePrivate, and has everything that class has.

  C++ hands a QDomElementPrivate around as a copy, so every C++
  QDomElementPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomElementPrivate that has a ritual and that Python
  can call so far, 15 names in all: 'attribute', 'attributeNS',
  'removeAttribute', 'attributeNode', 'attributeNodeNS', 'setAttributeNode',
  'setAttributeNodeNS', 'removeAttributeNode', 'hasAttribute',
  'hasAttributeNS', 'text', 'attributes', 'hasAttributes', 'nodeType',
  'cloneNode'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomElementPrivate::~QDomElementPrivate()': the destructor: Python
    removes its C++ QDomElementPrivate by it, and has no other use for it.
  - Qt's 'void QDomElementPrivate::save(QTextStream &s, int a1, int a2)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QDomElementPrivate::afterSave(QTextStream &s, int a1, int a2)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 23 functions Qt declares: 4 leans on 'QDomNodePrivate; 1 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file.

  What to expect
  --------------

  - The C++ QDomElementPrivate is created at the first use, not by
    'QDomElementPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomElementPrivate back gives a copy the ritual made
    for Python, in a new cute QDomElementPrivate.
  - Each name of Qt's QDomElementPrivate that has no cute function yet,
    '__init__', 'setAttribute', 'setAttributeNS', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomElementPrivate'

  #  A C++ QDomElementPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDomElementPrivate'

  #  Qt's '~QDomElementPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QDomElementPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QDomElementPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def attribute(self, name: str, defValue: str) -> str:
    """
    Calls Qt's 'QString QDomElementPrivate::attribute(const QString &name,
    const QString &defValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelementprivate.html#attribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    defValue : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomElementPrivate::attribute(const QString &name, const
    #      QString &defValue) const
    return self.uglySide.call(
        'ritual_ZNK18QDomElementPrivate9attributeERK7QStringS2_',
        name, defValue,
    )

  @overload(str, str, str)
  def attributeNS(self, nsURI: str, localName: str, defValue: str) -> str:
    """
    Calls Qt's 'QString QDomElementPrivate::attributeNS(const QString &nsURI,
    const QString &localName, const QString &defValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#attributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    defValue : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomElementPrivate::attributeNS(const QString &nsURI, const
    #      QString &localName, const QString &defValue) const
    return self.uglySide.call(
        'ritual_ZNK18QDomElementPrivate11attributeNSERK7QStringS2_S2_',
        nsURI, localName, defValue,
    )

  @overload(str)
  def hasAttribute(self, name: str) -> bool:
    """
    Calls Qt's 'bool QDomElementPrivate::hasAttribute(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#hasAttribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomElementPrivate::hasAttribute(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK18QDomElementPrivate12hasAttributeERK7QString', name,
    )

  @overload(str, str)
  def hasAttributeNS(self, nsURI: str, localName: str) -> bool:
    """
    Calls Qt's 'bool QDomElementPrivate::hasAttributeNS(const QString &nsURI,
    const QString &localName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#hasAttributeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomElementPrivate::hasAttributeNS(const QString &nsURI, const
    #      QString &localName) const
    return self.uglySide.call(
        'ritual_ZNK18QDomElementPrivate14hasAttributeNSERK7QStringS2_',
        nsURI, localName,
    )

  def text(self) -> str:
    """
    Calls Qt's 'QString QDomElementPrivate::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelementprivate.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomElementPrivate::text() const
    return self.uglySide.call('ritual_ZNK18QDomElementPrivate4textEv')

  def hasAttributes(self) -> bool:
    """
    Calls Qt's 'bool QDomElementPrivate::hasAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#hasAttributes
    """
    #  bool QDomElementPrivate::hasAttributes() const
    return self.uglySide.call(
        'ritual_ZNK18QDomElementPrivate13hasAttributesEv',
    )

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomElementPrivate::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelementprivate.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomElementPrivate::nodeType() const
    ritual = 'ritual_ZNK18QDomElementPrivate8nodeTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QDomElementPrivate8nodeTypeEv'
    return QDomNode.NodeType(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDomAttrPrivate)
  @overload(NoneType)
  def setAttributeNode(
      self,
      newAttr: Optional[QDomAttrPrivate],
  ) -> Optional[QDomAttrPrivate]:
    """
    Calls Qt's 'QDomAttrPrivate
    *QDomElementPrivate::setAttributeNode(QDomAttrPrivate *newAttr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#setAttributeNode

    Parameters
    ----------

    newAttr : Optional[QDomAttrPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomAttrPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomAttrPrivate *QDomElementPrivate::setAttributeNode(QDomAttrPrivate
    #      *newAttr)
    address = self.uglySide.call(
        'ritual_ZN18QDomElementPrivate16setAttributeNodeEP15QDomAttrPrivate',
        self._addressOf(newAttr),
    )
    from . import QDomAttrPrivate
    return QDomAttrPrivate._cuteAt(address)

  @overload(QDomAttrPrivate)
  @overload(NoneType)
  def setAttributeNodeNS(
      self,
      newAttr: Optional[QDomAttrPrivate],
  ) -> Optional[QDomAttrPrivate]:
    """
    Calls Qt's 'QDomAttrPrivate
    *QDomElementPrivate::setAttributeNodeNS(QDomAttrPrivate *newAttr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#setAttributeNodeNS

    Parameters
    ----------

    newAttr : Optional[QDomAttrPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomAttrPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomAttrPrivate
    #      *QDomElementPrivate::setAttributeNodeNS(QDomAttrPrivate *newAttr)
    address = self.uglySide.call(
        'ritual_ZN18QDomElementPrivate18setAttributeNodeNSEP15QDomAttrPriva'
        'te',
        self._addressOf(newAttr),
    )
    from . import QDomAttrPrivate
    return QDomAttrPrivate._cuteAt(address)

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
    - Qt's 'QDomElementPrivate::QDomElementPrivate(QDomDocumentPrivate *a0,
      QDomNodePrivate *parent, const QString &name)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomElementPrivate::QDomElementPrivate(QDomDocumentPrivate *a0,
      QDomNodePrivate *parent, const QString &nsURI, const QString &qName)':
      leans on 'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomElementPrivate::QDomElementPrivate(QDomElementPrivate *n,
      bool deep)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QDomElementPrivate.__init__' has no cute function yet. Qt's "
        "'QDomElementPrivate::QDomElementPrivate(QDomDocumentPrivate *a0, "
        "QDomNodePrivate *parent, const QString &name)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomElementPrivate::QDomElementPrivate(QDomDocumentPrivate *a0, "
        "QDomNodePrivate *parent, const QString &nsURI, const QString "
        "&qName)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomElementPrivate::QDomElementPrivate(QDomElementPrivate *n, "
        "bool deep)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    Calls Qt's 'void QDomElementPrivate::removeAttribute(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#removeAttribute

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomElementPrivate::removeAttribute(const QString &name)
    self.uglySide.call(
        'ritual_ZN18QDomElementPrivate15removeAttributeERK7QString', name,
    )

  @overload(str)
  def attributeNode(self, name: str) -> Optional[QDomAttrPrivate]:
    """
    Calls Qt's 'QDomAttrPrivate *QDomElementPrivate::attributeNode(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#attributeNode

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QDomAttrPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomAttrPrivate *QDomElementPrivate::attributeNode(const QString
    #      &name)
    address = self.uglySide.call(
        'ritual_ZN18QDomElementPrivate13attributeNodeERK7QString', name,
    )
    from . import QDomAttrPrivate
    return QDomAttrPrivate._cuteAt(address)

  @overload(str, str)
  def attributeNodeNS(
      self,
      nsURI: str,
      localName: str,
  ) -> Optional[QDomAttrPrivate]:
    """
    Calls Qt's 'QDomAttrPrivate *QDomElementPrivate::attributeNodeNS(const
    QString &nsURI, const QString &localName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#attributeNodeNS

    Parameters
    ----------

    nsURI : str
      Passed on as it is: a QString is made of it for the call.

    localName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QDomAttrPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomAttrPrivate *QDomElementPrivate::attributeNodeNS(const QString
    #      &nsURI, const QString &localName)
    address = self.uglySide.call(
        'ritual_ZN18QDomElementPrivate15attributeNodeNSERK7QStringS2_',
        nsURI, localName,
    )
    from . import QDomAttrPrivate
    return QDomAttrPrivate._cuteAt(address)

  @overload(QDomAttrPrivate)
  @overload(NoneType)
  def removeAttributeNode(
      self,
      oldAttr: Optional[QDomAttrPrivate],
  ) -> Optional[QDomAttrPrivate]:
    """
    Calls Qt's 'QDomAttrPrivate
    *QDomElementPrivate::removeAttributeNode(QDomAttrPrivate *oldAttr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomelementprivate.html#removeAttributeNode

    Parameters
    ----------

    oldAttr : Optional[QDomAttrPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomAttrPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomAttrPrivate
    #      *QDomElementPrivate::removeAttributeNode(QDomAttrPrivate *oldAttr)
    address = self.uglySide.call(
        'ritual_ZN18QDomElementPrivate19removeAttributeNodeEP15QDomAttrPriv'
        'ate',
        self._addressOf(oldAttr),
    )
    from . import QDomAttrPrivate
    return QDomAttrPrivate._cuteAt(address)

  def attributes(self) -> Optional[QDomNamedNodeMapPrivate]:
    """
    Calls Qt's 'QDomNamedNodeMapPrivate *QDomElementPrivate::attributes()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelementprivate.html#attributes

    Returns
    -------

    Optional[QDomNamedNodeMapPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNamedNodeMapPrivate *QDomElementPrivate::attributes()
    address = self.uglySide.call(
        'ritual_ZN18QDomElementPrivate10attributesEv',
    )
    from . import QDomNamedNodeMapPrivate
    return QDomNamedNodeMapPrivate._cuteAt(address)

  @overload()
  @overload(bool)
  def cloneNode(self, deep: bool = True) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomElementPrivate::cloneNode(bool deep)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomelementprivate.html#cloneNode

    Parameters
    ----------

    deep : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomElementPrivate::cloneNode(bool deep)
    address = self.uglySide.call(
        'ritual_ZN18QDomElementPrivate9cloneNodeEb', deep,
    )
    return QDomNodePrivate._cuteAt(address)

  @staticmethod
  def setAttribute(*__, **_) -> Never:
    """
    Qt's 'void QDomElementPrivate::setAttribute(const QString &name, const
    QString &value)': leans on
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomElementPrivate.setAttribute' has no cute function yet. Qt's "
        "'void QDomElementPrivate::setAttribute(const QString &name, const "
        "QString &value)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def setAttributeNS(*__, **_) -> Never:
    """
    Qt's 'void QDomElementPrivate::setAttributeNS(const QString &nsURI, const
    QString &qName, const QString &newValue)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qt_split_namespace'.
    """
    raise NotImplementedError(
        "'QDomElementPrivate.setAttributeNS' has no cute function yet. Qt's "
        "'void QDomElementPrivate::setAttributeNS(const QString &nsURI, "
        "const QString &qName, const QString &newValue)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qt_split_namespace'.")
