"""
qdesigner_internal::ManageWidgetCommandHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ManageWidgetCommandHelper to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ManageWidgetCommandHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::ManageWidgetCommandHelper: a
  plain Python object standing in front of one C++
  qdesigner_internal::ManageWidgetCommandHelper.

  C++ hands a qdesigner_internal::ManageWidgetCommandHelper around as a copy,
  so every C++ qdesigner_internal::ManageWidgetCommandHelper behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ManageWidgetCommandHelper that
  has a ritual and that Python can call so far, 4 names in all: 'init',
  'manage', 'unmanage', 'managedChildren'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::ManageWidgetCommandHelper::
    ~ManageWidgetCommandHelper()': the destructor: Python removes its C++
    qdesigner_internal::ManageWidgetCommandHelper by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::ManageWidgetCommandHelper is created at the
    first use, not by 'qdesigner_internal::ManageWidgetCommandHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::ManageWidgetCommandHelper back
    gives a copy the ritual made for Python, in a new cute
    qdesigner_internal::ManageWidgetCommandHelper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ManageWidgetCommandHelper'

  #  Qt's '~qdesigner_internal::ManageWidgetCommandHelper()'. Naming it makes
  #  this a value class: Python owns every C++
  #  qdesigner_internal::ManageWidgetCommandHelper behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal25ManageWidgetCommandHelperD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def managedChildren(self) -> QList[QWidget]:
    """
    Calls Qt's 'const QWidgetList
    &qdesigner_internal::ManageWidgetCommandHelper::managedChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-managewidgetcommandhelper.html

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QWidgetList
    #      &qdesigner_internal::ManageWidgetCommandHelper::managedChildren()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal25ManageWidgetCommandHelper15managed'
        'ChildrenEv',
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

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
    'qdesigner_internal::ManageWidgetCommandHelper::
    ManageWidgetCommandHelper()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-managewidgetcommandhelper.html
    """
    #  qdesigner_internal::ManageWidgetCommandHelper::
    #      ManageWidgetCommandHelper()
    self._noteCreation(ManageWidgetCommandHelper, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal25ManageWidgetCommandHelperC1Ev',
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

  @overload(QDesignerFormWindowInterface, QWidget)
  @overload(QDesignerFormWindowInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def init(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ManageWidgetCommandHelper::init(const
    QDesignerFormWindowInterface *fw, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-managewidgetcommandhelper.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ManageWidgetCommandHelper::init(const
    #      QDesignerFormWindowInterface *fw, QWidget *widget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal25ManageWidgetCommandHelper4initEPK28'
        'QDesignerFormWindowInterfaceP7QWidget',
        self._addressOf(fw), self._addressOf(widget),
    )

  @overload(QWidget, QList[QWidget])
  @overload(NoneType, QList[QWidget])
  def init(
      self,
      widget: Optional[QWidget],
      managedChildren: QList[QWidget],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ManageWidgetCommandHelper::init(QWidget *widget,
    const QWidgetList &managedChildren)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-managewidgetcommandhelper.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    managedChildren : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::ManageWidgetCommandHelper::init(QWidget
    #      *widget, const QWidgetList &managedChildren)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal25ManageWidgetCommandHelper4initEP7QW'
        'idgetRK5QListIS2_E',
        self._addressOf(widget), self._valueOf(managedChildren),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def manage(self, fw: Optional[QDesignerFormWindowInterface]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ManageWidgetCommandHelper::manage(
    QDesignerFormWindowInterface *fw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-managewidgetcommandhelper.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ManageWidgetCommandHelper::manage(
    #      QDesignerFormWindowInterface *fw)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal25ManageWidgetCommandHelper6manageEP2'
        '8QDesignerFormWindowInterface',
        self._addressOf(fw),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def unmanage(self, fw: Optional[QDesignerFormWindowInterface]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ManageWidgetCommandHelper::unmanage(
    QDesignerFormWindowInterface *fw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-managewidgetcommandhelper.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ManageWidgetCommandHelper::unmanage(
    #      QDesignerFormWindowInterface *fw)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal25ManageWidgetCommandHelper8unmanageE'
        'P28QDesignerFormWindowInterface',
        self._addressOf(fw),
    )
