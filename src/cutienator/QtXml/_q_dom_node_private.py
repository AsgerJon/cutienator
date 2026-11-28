"""
QDomNodePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomNodePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QDomNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDomDocumentPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomDocumentPrivate = WAIT['QDomDocumentPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomNodePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomNodePrivate: a plain Python object standing in
  front of one C++ QDomNodePrivate.

  C++ hands a QDomNodePrivate around as a copy, so every C++ QDomNodePrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomNodePrivate that has a ritual and that Python
  can call so far, 32 names in all: 'nodeName', 'nodeValue', 'setNodeValue',
  'ownerDocument', 'setOwnerDocument', 'insertBefore', 'insertAfter',
  'replaceChild', 'removeChild', 'appendChild', 'namedItem', 'cloneNode',
  'normalize', 'clear', 'parent', 'setParent', 'setNoParent', 'isAttr',
  'isCDATASection', 'isDocumentFragment', 'isDocument', 'isDocumentType',
  'isElement', 'isEntityReference', 'isText', 'isEntity', 'isNotation',
  'isProcessingInstruction', 'isCharacterData', 'isComment', 'nodeType',
  'setLocation'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomNodePrivate::~QDomNodePrivate()': the destructor: Python
    removes its C++ QDomNodePrivate by it, and has no other use for it.
  - Qt's 'void QDomNodePrivate::saveSubTree(const QDomNodePrivate *n,
    QTextStream &s, int depth, int indent) const': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QDomNodePrivate::save(QTextStream &a0, int a1, int a2) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QDomNodePrivate::afterSave(QTextStream &a0, int a1, int a2)
    const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDomNodePrivate is created at the first use, not by
    'QDomNodePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomNodePrivate back gives a copy the ritual made for
    Python, in a new cute QDomNodePrivate.
  - Each name of Qt's QDomNodePrivate that has no cute function yet,
    'afterSave', 'save', 'saveSubTree', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomNodePrivate'

  #  A C++ QDomNodePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDomNodePrivate'

  #  The functions Qt calls itself that QDomNodePrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'save': (
          'void QDomNodePrivate::save(QTextStream &, int, int) const',
      ),
      'afterSave': (
          'void QDomNodePrivate::afterSave(QTextStream &, int, int) const',
      ),
  }

  #  The functions Qt calls itself that QDomNodePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setNodeValue': (
          ('_ZN15QDomNodePrivate12setNodeValueERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'insertBefore': (
          ('_ZN15QDomNodePrivate12insertBeforeEPS_S0_',
           ('address', 'address', 'QtXml:QDomNodePrivate'),
           (
               ('address', 'address', 'QtXml:QDomNodePrivate'),
               ('address', 'address', 'QtXml:QDomNodePrivate'),
           )),
      ),
      'insertAfter': (
          ('_ZN15QDomNodePrivate11insertAfterEPS_S0_',
           ('address', 'address', 'QtXml:QDomNodePrivate'),
           (
               ('address', 'address', 'QtXml:QDomNodePrivate'),
               ('address', 'address', 'QtXml:QDomNodePrivate'),
           )),
      ),
      'replaceChild': (
          ('_ZN15QDomNodePrivate12replaceChildEPS_S0_',
           ('address', 'address', 'QtXml:QDomNodePrivate'),
           (
               ('address', 'address', 'QtXml:QDomNodePrivate'),
               ('address', 'address', 'QtXml:QDomNodePrivate'),
           )),
      ),
      'removeChild': (
          ('_ZN15QDomNodePrivate11removeChildEPS_',
           ('address', 'address', 'QtXml:QDomNodePrivate'),
           (
               ('address', 'address', 'QtXml:QDomNodePrivate'),
           )),
      ),
      'appendChild': (
          ('_ZN15QDomNodePrivate11appendChildEPS_',
           ('address', 'address', 'QtXml:QDomNodePrivate'),
           (
               ('address', 'address', 'QtXml:QDomNodePrivate'),
           )),
      ),
      'cloneNode': (
          ('_ZN15QDomNodePrivate9cloneNodeEb',
           ('address', 'address', 'QtXml:QDomNodePrivate'),
           (
               ('bool', 'number', ''),
           )),
      ),
      'normalize': (
          ('_ZN15QDomNodePrivate9normalizeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'clear': (
          ('_ZN15QDomNodePrivate5clearEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'nodeType': (
          ('_ZNK15QDomNodePrivate8nodeTypeEv',
           ('int', 'enum', 'QtXml:QDomNode.NodeType'),
           ()),
      ),
  }

  #  Qt's '~QDomNodePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QDomNodePrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDomNodePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeName(self) -> str:
    """
    Calls Qt's 'QString QDomNodePrivate::nodeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#nodeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNodePrivate::nodeName() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate8nodeNameEv')

  def nodeValue(self) -> str:
    """
    Calls Qt's 'QString QDomNodePrivate::nodeValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#nodeValue

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNodePrivate::nodeValue() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate9nodeValueEv')

  def parent(self) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNodePrivate::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#parent

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodePrivate::parent() const
    address = self.uglySide.call('ritual_ZNK15QDomNodePrivate6parentEv')
    return QDomNodePrivate._cuteAt(address)

  def isAttr(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isAttr() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#isAttr
    """
    #  bool QDomNodePrivate::isAttr() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate6isAttrEv')

  def isCDATASection(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isCDATASection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#isCDATASection
    """
    #  bool QDomNodePrivate::isCDATASection() const
    return self.uglySide.call(
        'ritual_ZNK15QDomNodePrivate14isCDATASectionEv',
    )

  def isDocumentFragment(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isDocumentFragment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#isDocumentFragment
    """
    #  bool QDomNodePrivate::isDocumentFragment() const
    return self.uglySide.call(
        'ritual_ZNK15QDomNodePrivate18isDocumentFragmentEv',
    )

  def isDocument(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isDocument() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#isDocument
    """
    #  bool QDomNodePrivate::isDocument() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate10isDocumentEv')

  def isDocumentType(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isDocumentType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#isDocumentType
    """
    #  bool QDomNodePrivate::isDocumentType() const
    return self.uglySide.call(
        'ritual_ZNK15QDomNodePrivate14isDocumentTypeEv',
    )

  def isElement(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#isElement
    """
    #  bool QDomNodePrivate::isElement() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate9isElementEv')

  def isEntityReference(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isEntityReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#isEntityReference
    """
    #  bool QDomNodePrivate::isEntityReference() const
    return self.uglySide.call(
        'ritual_ZNK15QDomNodePrivate17isEntityReferenceEv',
    )

  def isText(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#isText
    """
    #  bool QDomNodePrivate::isText() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate6isTextEv')

  def isEntity(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isEntity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#isEntity
    """
    #  bool QDomNodePrivate::isEntity() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate8isEntityEv')

  def isNotation(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isNotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#isNotation
    """
    #  bool QDomNodePrivate::isNotation() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate10isNotationEv')

  def isProcessingInstruction(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isProcessingInstruction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#isProcessingInstruction
    """
    #  bool QDomNodePrivate::isProcessingInstruction() const
    return self.uglySide.call(
        'ritual_ZNK15QDomNodePrivate23isProcessingInstructionEv',
    )

  def isCharacterData(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isCharacterData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#isCharacterData
    """
    #  bool QDomNodePrivate::isCharacterData() const
    return self.uglySide.call(
        'ritual_ZNK15QDomNodePrivate15isCharacterDataEv',
    )

  def isComment(self) -> bool:
    """
    Calls Qt's 'bool QDomNodePrivate::isComment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#isComment
    """
    #  bool QDomNodePrivate::isComment() const
    return self.uglySide.call('ritual_ZNK15QDomNodePrivate9isCommentEv')

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomNodePrivate::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomNodePrivate::nodeType() const
    ritual = 'ritual_ZNK15QDomNodePrivate8nodeTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QDomNodePrivate8nodeTypeEv'
    return QDomNode.NodeType(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNodeValue(self, v: str) -> None:
    """
    Calls Qt's 'void QDomNodePrivate::setNodeValue(const QString &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#setNodeValue

    Parameters
    ----------

    v : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomNodePrivate::setNodeValue(const QString &v)
    ritual = 'ritual_ZN15QDomNodePrivate12setNodeValueERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate12setNodeValueERK7QString'
    self.uglySide.call(ritual, v)

  @overload(QDomDocumentPrivate)
  @overload(NoneType)
  def setOwnerDocument(self, doc: Optional[QDomDocumentPrivate]) -> None:
    """
    Calls Qt's 'void QDomNodePrivate::setOwnerDocument(QDomDocumentPrivate
    *doc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#setOwnerDocument

    Parameters
    ----------

    doc : Optional[QDomDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDomNodePrivate::setOwnerDocument(QDomDocumentPrivate *doc)
    self.uglySide.call(
        'ritual_ZN15QDomNodePrivate16setOwnerDocumentEP19QDomDocumentPrivat'
        'e',
        self._addressOf(doc),
    )

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, p: Optional[QDomNodePrivate]) -> None:
    """
    Calls Qt's 'void QDomNodePrivate::setParent(QDomNodePrivate *p)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#setParent

    Parameters
    ----------

    p : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDomNodePrivate::setParent(QDomNodePrivate *p)
    self.uglySide.call(
        'ritual_ZN15QDomNodePrivate9setParentEPS_', self._addressOf(p),
    )

  def setNoParent(self) -> None:
    """
    Calls Qt's 'void QDomNodePrivate::setNoParent()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#setNoParent
    """
    #  void QDomNodePrivate::setNoParent()
    self.uglySide.call('ritual_ZN15QDomNodePrivate11setNoParentEv')

  @overload(int, int)
  def setLocation(self, lineNumber: int, columnNumber: int) -> None:
    """
    Calls Qt's 'void QDomNodePrivate::setLocation(int lineNumber, int
    columnNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#setLocation

    Parameters
    ----------

    lineNumber : int
      Passed on as it is.

    columnNumber : int
      Passed on as it is.
    """
    #  void QDomNodePrivate::setLocation(int lineNumber, int columnNumber)
    self.uglySide.call(
        'ritual_ZN15QDomNodePrivate11setLocationEii',
        lineNumber, columnNumber,
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

  @overload(QDomDocumentPrivate)
  @overload(NoneType)
  @overload(QDomDocumentPrivate, THIS)
  @overload(QDomDocumentPrivate, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      a0: Optional[QDomDocumentPrivate],
      parent: Optional[QDomNodePrivate] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate *a0,
    QDomNodePrivate *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#QDomNodePrivate

    Parameters
    ----------

    a0 : Optional[QDomDocumentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate *a0,
    #      QDomNodePrivate *parent)
    self._noteCreation(QDomNodePrivate, lambda: Rituals.call(
        'ritual_ZN15QDomNodePrivateC1EP19QDomDocumentPrivatePS_',
        self._addressOf(a0), self._addressOf(parent),
    ))

  @overload(THIS, bool)
  @overload(NoneType, bool)
  def __init__(self, n: Optional[QDomNodePrivate], deep: bool) -> None:
    """
    Notes what was given, for Qt's
    'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate *n, bool deep)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodeprivate.html#QDomNodePrivate

    Parameters
    ----------

    n : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deep : bool
      Passed on as it is.
    """
    #  QDomNodePrivate::QDomNodePrivate(QDomNodePrivate *n, bool deep)
    self._noteCreation(QDomNodePrivate, lambda: Rituals.call(
        'ritual_ZN15QDomNodePrivateC1EPS_b', self._addressOf(n), deep,
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

  def ownerDocument(self) -> Optional[QDomDocumentPrivate]:
    """
    Calls Qt's 'QDomDocumentPrivate *QDomNodePrivate::ownerDocument()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#ownerDocument

    Returns
    -------

    Optional[QDomDocumentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomDocumentPrivate *QDomNodePrivate::ownerDocument()
    address = self.uglySide.call(
        'ritual_ZN15QDomNodePrivate13ownerDocumentEv',
    )
    from . import QDomDocumentPrivate
    return QDomDocumentPrivate._cuteAt(address)

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def insertBefore(
      self,
      newChild: Optional[QDomNodePrivate],
      refChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomNodePrivate::insertBefore(QDomNodePrivate *newChild, QDomNodePrivate
    *refChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#insertBefore

    Parameters
    ----------

    newChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodePrivate::insertBefore(QDomNodePrivate
    #      *newChild, QDomNodePrivate *refChild)
    ritual = 'ritual_ZN15QDomNodePrivate12insertBeforeEPS_S0_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate12insertBeforeEPS_S0_'
    address = self.uglySide.call(
        ritual, self._addressOf(newChild), self._addressOf(refChild),
    )
    return QDomNodePrivate._cuteAt(address)

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def insertAfter(
      self,
      newChild: Optional[QDomNodePrivate],
      refChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNodePrivate::insertAfter(QDomNodePrivate
    *newChild, QDomNodePrivate *refChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#insertAfter

    Parameters
    ----------

    newChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    refChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodePrivate::insertAfter(QDomNodePrivate
    #      *newChild, QDomNodePrivate *refChild)
    ritual = 'ritual_ZN15QDomNodePrivate11insertAfterEPS_S0_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate11insertAfterEPS_S0_'
    address = self.uglySide.call(
        ritual, self._addressOf(newChild), self._addressOf(refChild),
    )
    return QDomNodePrivate._cuteAt(address)

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def replaceChild(
      self,
      newChild: Optional[QDomNodePrivate],
      oldChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomNodePrivate::replaceChild(QDomNodePrivate *newChild, QDomNodePrivate
    *oldChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#replaceChild

    Parameters
    ----------

    newChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodePrivate::replaceChild(QDomNodePrivate
    #      *newChild, QDomNodePrivate *oldChild)
    ritual = 'ritual_ZN15QDomNodePrivate12replaceChildEPS_S0_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate12replaceChildEPS_S0_'
    address = self.uglySide.call(
        ritual, self._addressOf(newChild), self._addressOf(oldChild),
    )
    return QDomNodePrivate._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def removeChild(
      self,
      oldChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNodePrivate::removeChild(QDomNodePrivate
    *oldChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#removeChild

    Parameters
    ----------

    oldChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodePrivate::removeChild(QDomNodePrivate
    #      *oldChild)
    ritual = 'ritual_ZN15QDomNodePrivate11removeChildEPS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate11removeChildEPS_'
    address = self.uglySide.call(ritual, self._addressOf(oldChild))
    return QDomNodePrivate._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def appendChild(
      self,
      newChild: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNodePrivate::appendChild(QDomNodePrivate
    *newChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#appendChild

    Parameters
    ----------

    newChild : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodePrivate::appendChild(QDomNodePrivate
    #      *newChild)
    ritual = 'ritual_ZN15QDomNodePrivate11appendChildEPS_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate11appendChildEPS_'
    address = self.uglySide.call(ritual, self._addressOf(newChild))
    return QDomNodePrivate._cuteAt(address)

  @overload(str)
  def namedItem(self, name: str) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNodePrivate::namedItem(const QString
    &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#namedItem

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
    #  QDomNodePrivate *QDomNodePrivate::namedItem(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN15QDomNodePrivate9namedItemERK7QString', name,
    )
    return QDomNodePrivate._cuteAt(address)

  @overload()
  @overload(bool)
  def cloneNode(self, deep: bool = True) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNodePrivate::cloneNode(bool deep)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#cloneNode

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
    #  QDomNodePrivate *QDomNodePrivate::cloneNode(bool deep)
    ritual = 'ritual_ZN15QDomNodePrivate9cloneNodeEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate9cloneNodeEb'
    address = self.uglySide.call(ritual, deep)
    return QDomNodePrivate._cuteAt(address)

  def normalize(self) -> None:
    """
    Calls Qt's 'void QDomNodePrivate::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#normalize
    """
    #  void QDomNodePrivate::normalize()
    ritual = 'ritual_ZN15QDomNodePrivate9normalizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate9normalizeEv'
    self.uglySide.call(ritual)

  def clear(self) -> None:
    """
    Calls Qt's 'void QDomNodePrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodeprivate.html#clear
    """
    #  void QDomNodePrivate::clear()
    ritual = 'ritual_ZN15QDomNodePrivate5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QDomNodePrivate5clearEv'
    self.uglySide.call(ritual)

  @staticmethod
  def afterSave(*__, **_) -> Never:
    """
    Qt's 'void QDomNodePrivate::afterSave(QTextStream &a0, int a1, int a2)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDomNodePrivate.afterSave' has no cute function yet. Qt's 'void "
        "QDomNodePrivate::afterSave(QTextStream &a0, int a1, int a2) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def save(*__, **_) -> Never:
    """
    Qt's 'void QDomNodePrivate::save(QTextStream &a0, int a1, int a2) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDomNodePrivate.save' has no cute function yet. Qt's 'void "
        "QDomNodePrivate::save(QTextStream &a0, int a1, int a2) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def saveSubTree(*__, **_) -> Never:
    """
    Qt's 'void QDomNodePrivate::saveSubTree(const QDomNodePrivate *n,
    QTextStream &s, int depth, int indent) const': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QDomNodePrivate.saveSubTree' has no cute function yet. Qt's 'void "
        "QDomNodePrivate::saveSubTree(const QDomNodePrivate *n, QTextStream "
        "&s, int depth, int indent) const': takes a type Python has no way "
        "to hand over yet.")
