"""
QDomDocumentFragment binding of the Qt C++
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

  from . import QDomDocumentFragmentPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomDocumentFragmentPrivate = WAIT['QDomDocumentFragmentPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomDocumentFragment(QDomNode):
  """
  The cute side of Qt's QDomDocumentFragment: a plain Python object standing
  in front of one C++ QDomDocumentFragment.

  It is built on the cute 'QDomNode', as Qt's QDomDocumentFragment is built
  on Qt's QDomNode, and has everything that class has.

  C++ hands a QDomDocumentFragment around as a copy, so every C++
  QDomDocumentFragment behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomDocumentFragment that has a ritual and that
  Python can call so far, 1 name in all: 'nodeType'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomDocumentFragment &QDomDocumentFragment::operator=(const
    QDomDocumentFragment &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QDomDocumentFragment::~QDomDocumentFragment()': the destructor:
    Python removes its C++ QDomDocumentFragment by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QDomDocumentFragment is created at the first use, not by
    'QDomDocumentFragment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomDocumentFragment back gives a copy the ritual
    made for Python, in a new cute QDomDocumentFragment.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomDocumentFragment'

  #  Qt's '~QDomDocumentFragment()'. Naming it makes this a value class:
  #  Python owns every C++ QDomDocumentFragment behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QDomDocumentFragmentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomDocumentFragment::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumentfragment.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomDocumentFragment::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK20QDomDocumentFragment8nodeTypeEv',
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
    Notes what was given, for Qt's
    'QDomDocumentFragment::QDomDocumentFragment()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumentfragment.html#QDomDocumentFragment
    """
    #  QDomDocumentFragment::QDomDocumentFragment()
    self._noteCreation(QDomDocumentFragment, lambda: Rituals.call(
        'ritual_ZN20QDomDocumentFragmentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, documentFragment: QDomDocumentFragment) -> None:
    """
    Notes what was given, for Qt's
    'QDomDocumentFragment::QDomDocumentFragment(const QDomDocumentFragment
    &documentFragment)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumentfragment.html#QDomDocumentFragment

    Parameters
    ----------

    documentFragment : QDomDocumentFragment
      Passed on as a value: Qt reads the C++ QDomDocumentFragment, which
      stays Python's own.
    """
    #  QDomDocumentFragment::QDomDocumentFragment(const QDomDocumentFragment
    #      &documentFragment)
    self._noteCreation(QDomDocumentFragment, lambda: Rituals.call(
        'ritual_ZN20QDomDocumentFragmentC1ERKS_',
        self._valueOf(documentFragment),
    ))

  @overload(QDomDocumentFragmentPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomDocumentFragmentPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomDocumentFragment::QDomDocumentFragment(QDomDocumentFragmentPrivate
    *a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumentfragment.html#QDomDocumentFragment

    Parameters
    ----------

    a0 : Optional[QDomDocumentFragmentPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomDocumentFragment::QDomDocumentFragment(QDomDocumentFragmentPrivate
    #      *a0)
    self._noteCreation(QDomDocumentFragment, lambda: Rituals.call(
        'ritual_ZN20QDomDocumentFragmentC1EP27QDomDocumentFragmentPrivate',
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
