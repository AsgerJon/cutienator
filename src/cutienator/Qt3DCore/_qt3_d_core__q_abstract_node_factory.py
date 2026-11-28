"""
Qt3DCore::QAbstractNodeFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qabstractnodefactory_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::QAbstractNodeFactory to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractNodeFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QAbstractNodeFactory: a plain Python object
  standing in front of one C++ Qt3DCore::QAbstractNodeFactory.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAbstractNodeFactory that has a ritual and
  that Python can call so far, 2 names in all: 'createNode',
  'registerNodeFactory'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QAbstractNodeFactory::~QAbstractNodeFactory()': the
    destructor: Python never removes a C++ Qt3DCore::QAbstractNodeFactory.
  - Qt's 'QList<QAbstractNodeFactory *>
    Qt3DCore::QAbstractNodeFactory::nodeFactories()': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ Qt3DCore::QAbstractNodeFactory is created at the first use, not
    by 'Qt3DCore::QAbstractNodeFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAbstractNodeFactory.
  - Each name of Qt's Qt3DCore::QAbstractNodeFactory that has no cute
    function yet, 'nodeFactories', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def registerNodeFactory(factory: Optional[QAbstractNodeFactory]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAbstractNodeFactory::registerNodeFactory(QAbstractNodeFactory
    *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractnodefactory.html

    Parameters
    ----------

    factory : Optional[QAbstractNodeFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAbstractNodeFactory::registerNodeFactory(
    #      QAbstractNodeFactory *factory)
    Rituals.call(
        'ritual_ZN8Qt3DCore20QAbstractNodeFactory19registerNodeFactoryEPS0_',
        CuteMixin._addressOf(factory),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAbstractNodeFactory'

  #  The functions Qt calls itself that Qt3DCore::QAbstractNodeFactory is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createNode': (
          'QNode *Qt3DCore::QAbstractNodeFactory::createNode(const char *)',
      ),
  }

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
  @overload(NoneType)
  def createNode(self, type: Optional[str]) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QAbstractNodeFactory::createNode(const char
    *type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractnodefactory.html#createNode

    Parameters
    ----------

    type : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QAbstractNodeFactory::createNode(const char *type)
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore20QAbstractNodeFactory10createNodeEPKc',
        self._bytesOf(type),
    )
    return Qt3DCore.QNode._cuteAt(address)

  @staticmethod
  def nodeFactories(*__, **_) -> Never:
    """
    Qt's 'QList<QAbstractNodeFactory *>
    Qt3DCore::QAbstractNodeFactory::nodeFactories()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAbstractNodeFactory.nodeFactories' has no cute function "
        "yet. Qt's 'QList<QAbstractNodeFactory *> "
        "Qt3DCore::QAbstractNodeFactory::nodeFactories()': gives a type "
        "Python has no way to take yet.")
