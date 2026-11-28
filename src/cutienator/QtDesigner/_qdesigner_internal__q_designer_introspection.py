"""
qdesigner_internal::QDesignerIntrospection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_introspection_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerIntrospection to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QDesignerIntrospectionInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QObject
  from . import QDesignerMetaObjectInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerIntrospection(QDesignerIntrospectionInterface):
  """
  The cute side of Qt's qdesigner_internal::QDesignerIntrospection: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerIntrospection.

  It is built on the cute 'QDesignerIntrospectionInterface', as Qt's
  qdesigner_internal::QDesignerIntrospection is built on Qt's
  QDesignerIntrospectionInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerIntrospection that has
  a ritual and that Python can call so far, 2 names in all: 'metaObject',
  'metaObjectForQMetaObject'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::QDesignerIntrospection::~QDesignerIntrospection()':
    the destructor: Python never removes a C++
    qdesigner_internal::QDesignerIntrospection.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerIntrospection is created at the
    first use, not by 'qdesigner_internal::QDesignerIntrospection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerIntrospection.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerIntrospection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def metaObject(
      self,
      object: Optional[QObject],
  ) -> Optional[QDesignerMetaObjectInterface]:
    """
    Calls Qt's 'const QDesignerMetaObjectInterface
    *qdesigner_internal::QDesignerIntrospection::metaObject(const QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerintrospection.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerMetaObjectInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDesignerMetaObjectInterface
    #      *qdesigner_internal::QDesignerIntrospection::metaObject(const
    #      QObject *object) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22QDesignerIntrospection10metaObject'
        'EPK7QObject',
        self._addressOf(object, 'QObject'),
    )
    from . import QDesignerMetaObjectInterface
    return QDesignerMetaObjectInterface._cuteAt(address)

  @overload(QMetaObject)
  @overload(NoneType)
  def metaObjectForQMetaObject(
      self,
      metaObject: Optional[QMetaObject],
  ) -> Optional[QDesignerMetaObjectInterface]:
    """
    Calls Qt's 'const QDesignerMetaObjectInterface
    *qdesigner_internal::QDesignerIntrospection::metaObjectForQMetaObject(
    const QMetaObject *metaObject) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerintrospection.html

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerMetaObjectInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QDesignerMetaObjectInterface
    #      *qdesigner_internal::QDesignerIntrospection::
    #      metaObjectForQMetaObject(const QMetaObject *metaObject) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22QDesignerIntrospection24metaObject'
        'ForQMetaObjectEPK11QMetaObject',
        self._addressOf(metaObject, 'QMetaObject'),
    )
    from . import QDesignerMetaObjectInterface
    return QDesignerMetaObjectInterface._cuteAt(address)

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
    'qdesigner_internal::QDesignerIntrospection::QDesignerIntrospection()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerintrospection.html
    """
    #  qdesigner_internal::QDesignerIntrospection::QDesignerIntrospection()
    self._noteCreation(QDesignerIntrospection, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22QDesignerIntrospectionC1Ev',
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
