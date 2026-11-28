"""
QSGNodePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgnode_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSGNodePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGNodePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGNodePrivate: a plain Python object standing in
  front of one C++ QSGNodePrivate.

  C++ hands a QSGNodePrivate around as a copy, so every C++ QSGNodePrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGNodePrivate that has a ritual and that Python can
  call so far, 4 names in all: 'mutabilityGroup',
  'setMutabilityGroupOfSubtree', 'setDescription', 'description'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGNodePrivate::~QSGNodePrivate()': the destructor: Python removes
    its C++ QSGNodePrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGNodePrivate is created at the first use, not by
    'QSGNodePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGNodePrivate back gives a copy the ritual made for
    Python, in a new cute QSGNodePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSGNode)
  @overload(NoneType)
  def mutabilityGroup(node: Optional[QSGNode]) -> int:
    """
    Calls Qt's 'quint8 QSGNodePrivate::mutabilityGroup(const QSGNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeprivate.html#mutabilityGroup

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  quint8 QSGNodePrivate::mutabilityGroup(const QSGNode *node)
    return Rituals.call(
        'ritual_ZN14QSGNodePrivate15mutabilityGroupEPK7QSGNode',
        CuteMixin._addressOf(node, 'QSGNode'),
    )

  @staticmethod
  @overload(QSGNode, int)
  @overload(NoneType, int)
  def setMutabilityGroupOfSubtree(
      node: Optional[QSGNode],
      mutabilityGroup: int,
  ) -> None:
    """
    Calls Qt's 'void QSGNodePrivate::setMutabilityGroupOfSubtree(QSGNode
    *node, quint8 mutabilityGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgnodeprivate.html#setMutabilityGroupOfSubtree

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mutabilityGroup : int
      Passed on as it is.
    """
    #  void QSGNodePrivate::setMutabilityGroupOfSubtree(QSGNode *node, quint8
    #      mutabilityGroup)
    Rituals.call(
        'ritual_ZN14QSGNodePrivate27setMutabilityGroupOfSubtreeEP7QSGNodeh',
        CuteMixin._addressOf(node, 'QSGNode'), mutabilityGroup,
    )

  @staticmethod
  @overload(QSGNode, str)
  @overload(NoneType, str)
  def setDescription(node: Optional[QSGNode], description: str) -> None:
    """
    Calls Qt's 'void QSGNodePrivate::setDescription(QSGNode *node, const
    QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeprivate.html#setDescription

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSGNodePrivate::setDescription(QSGNode *node, const QString
    #      &description)
    Rituals.call(
        'ritual_ZN14QSGNodePrivate14setDescriptionEP7QSGNodeRK7QString',
        CuteMixin._addressOf(node, 'QSGNode'), description,
    )

  @staticmethod
  @overload(QSGNode)
  @overload(NoneType)
  def description(node: Optional[QSGNode]) -> str:
    """
    Calls Qt's 'QString QSGNodePrivate::description(const QSGNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeprivate.html#description

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSGNodePrivate::description(const QSGNode *node)
    return Rituals.call(
        'ritual_ZN14QSGNodePrivate11descriptionEPK7QSGNode',
        CuteMixin._addressOf(node, 'QSGNode'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGNodePrivate'

  #  Qt's '~QSGNodePrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QSGNodePrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSGNodePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QSGNodePrivate::QSGNodePrivate()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsgnodeprivate.html#QSGNodePrivate
    """
    #  QSGNodePrivate::QSGNodePrivate()
    self._noteCreation(QSGNodePrivate, lambda: Rituals.call(
        'ritual_ZN14QSGNodePrivateC1Ev',
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
