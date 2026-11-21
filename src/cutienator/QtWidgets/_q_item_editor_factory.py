"""
QItemEditorFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qitemeditorfactory.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QItemEditorFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QItemEditorFactory: a plain Python object standing in
  front of one C++ QItemEditorFactory.

  C++ hands a QItemEditorFactory around as a copy, so every C++
  QItemEditorFactory behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QItemEditorFactory that has a ritual and that Python
  can call so far, 4 names in all: 'createEditor', 'valuePropertyName',
  'defaultFactory', 'setDefaultFactory'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QItemEditorFactory::~QItemEditorFactory()': the destructor: Python
    removes its C++ QItemEditorFactory by it, and has no other use for it.
  - Qt's 'void QItemEditorFactory::registerEditor(int userType,
    QItemEditorCreatorBase *creator)': names 'QItemEditorCreatorBase', which
    has no cute class yet.

  What to expect
  --------------

  - The C++ QItemEditorFactory is created at the first use, not by
    'QItemEditorFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QItemEditorFactory back gives a copy the ritual made
    for Python, in a new cute QItemEditorFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultFactory() -> Optional[QItemEditorFactory]:
    """
    Calls Qt's 'const QItemEditorFactory
    *QItemEditorFactory::defaultFactory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemeditorfactory.html#defaultFactory

    Returns
    -------

    Optional[QItemEditorFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QItemEditorFactory *QItemEditorFactory::defaultFactory()
    address = Rituals.call('ritual_ZN18QItemEditorFactory14defaultFactoryEv')
    return QItemEditorFactory._cuteAt(address)

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def setDefaultFactory(factory: Optional[QItemEditorFactory]) -> None:
    """
    Calls Qt's 'void QItemEditorFactory::setDefaultFactory(QItemEditorFactory
    *factory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemeditorfactory.html#setDefaultFactory

    Parameters
    ----------

    factory : Optional[QItemEditorFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QItemEditorFactory::setDefaultFactory(QItemEditorFactory
    #      *factory)
    Rituals.call(
        'ritual_ZN18QItemEditorFactory17setDefaultFactoryEPS_',
        CuteMixin._addressOf(factory),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemEditorFactory'

  #  Qt's '~QItemEditorFactory()'. Naming it makes this a value class: Python
  #  owns every C++ QItemEditorFactory behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QItemEditorFactoryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QWidget)
  @overload(int, NoneType)
  def createEditor(
      self,
      userType: int,
      parent: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QItemEditorFactory::createEditor(int userType,
    QWidget *parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemeditorfactory.html#createEditor

    Parameters
    ----------

    userType : int
      Passed on as it is.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QItemEditorFactory::createEditor(int userType, QWidget
    #      *parent) const
    address = self.uglySide.call(
        'ritual_ZNK18QItemEditorFactory12createEditorEiP7QWidget',
        userType, self._addressOf(parent),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(int)
  def valuePropertyName(self, userType: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QItemEditorFactory::valuePropertyName(int
    userType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemeditorfactory.html#valuePropertyName

    Parameters
    ----------

    userType : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QItemEditorFactory::valuePropertyName(int userType) const
    address = self.uglySide.call(
        'ritual_ZNK18QItemEditorFactory17valuePropertyNameEi', userType,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
    'QItemEditorFactory::QItemEditorFactory()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemeditorfactory.html#QItemEditorFactory
    """
    #  QItemEditorFactory::QItemEditorFactory()
    self._noteCreation(QItemEditorFactory, lambda: Rituals.call(
        'ritual_ZN18QItemEditorFactoryC1Ev',
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
