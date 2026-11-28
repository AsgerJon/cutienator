"""
QDomAttr binding of the Qt C++
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

  from . import QDomAttrPrivate, QDomElement
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomAttrPrivate = WAIT['QDomAttrPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomAttr(QDomNode):
  """
  The cute side of Qt's QDomAttr: a plain Python object standing in front of
  one C++ QDomAttr.

  It is built on the cute 'QDomNode', as Qt's QDomAttr is built on Qt's
  QDomNode, and has everything that class has.

  C++ hands a QDomAttr around as a copy, so every C++ QDomAttr behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomAttr that has a ritual and that Python can call
  so far, 6 names in all: 'name', 'specified', 'ownerElement', 'value',
  'setValue', 'nodeType'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomAttr &QDomAttr::operator=(const QDomAttr &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QDomAttr::~QDomAttr()': the destructor: Python removes its C++
    QDomAttr by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDomAttr is created at the first use, not by 'QDomAttr(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomAttr back gives a copy the ritual made for
    Python, in a new cute QDomAttr.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomAttr'

  #  Qt's '~QDomAttr()'. Naming it makes this a value class: Python owns
  #  every C++ QDomAttr behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QDomAttrD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QDomAttr::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomAttr::name() const
    return self.uglySide.call('ritual_ZNK8QDomAttr4nameEv')

  def specified(self) -> bool:
    """
    Calls Qt's 'bool QDomAttr::specified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#specified
    """
    #  bool QDomAttr::specified() const
    return self.uglySide.call('ritual_ZNK8QDomAttr9specifiedEv')

  def ownerElement(self) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomAttr::ownerElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#ownerElement

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomAttr::ownerElement() const
    address = self.uglySide.call('ritual_ZNK8QDomAttr12ownerElementEv')
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  def value(self) -> str:
    """
    Calls Qt's 'QString QDomAttr::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#value

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomAttr::value() const
    return self.uglySide.call('ritual_ZNK8QDomAttr5valueEv')

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomAttr::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomAttr::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK8QDomAttr8nodeTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setValue(self, value: str) -> None:
    """
    Calls Qt's 'void QDomAttr::setValue(const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#setValue

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomAttr::setValue(const QString &value)
    self.uglySide.call('ritual_ZN8QDomAttr8setValueERK7QString', value)

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
    Notes what was given, for Qt's 'QDomAttr::QDomAttr()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#QDomAttr
    """
    #  QDomAttr::QDomAttr()
    self._noteCreation(QDomAttr, lambda: Rituals.call(
        'ritual_ZN8QDomAttrC1Ev',
    ))

  @overload(THIS)
  def __init__(self, attr: QDomAttr) -> None:
    """
    Notes what was given, for Qt's 'QDomAttr::QDomAttr(const QDomAttr
    &attr)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#QDomAttr

    Parameters
    ----------

    attr : QDomAttr
      Passed on as a value: Qt reads the C++ QDomAttr, which stays Python's
      own.
    """
    #  QDomAttr::QDomAttr(const QDomAttr &attr)
    self._noteCreation(QDomAttr, lambda: Rituals.call(
        'ritual_ZN8QDomAttrC1ERKS_', self._valueOf(attr),
    ))

  @overload(QDomAttrPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomAttrPrivate]) -> None:
    """
    Notes what was given, for Qt's 'QDomAttr::QDomAttr(QDomAttrPrivate *a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomattr.html#QDomAttr

    Parameters
    ----------

    a0 : Optional[QDomAttrPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomAttr::QDomAttr(QDomAttrPrivate *a0)
    self._noteCreation(QDomAttr, lambda: Rituals.call(
        'ritual_ZN8QDomAttrC1EP15QDomAttrPrivate', self._addressOf(a0),
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
