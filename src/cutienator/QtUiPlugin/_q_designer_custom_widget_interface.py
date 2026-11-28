"""
QDesignerCustomWidgetInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtUiPlugin/customwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QIcon
  from ..QtWidgets import QWidget
  from ..QtDesigner import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerCustomWidgetInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerCustomWidgetInterface: a plain Python object
  standing in front of one C++ QDesignerCustomWidgetInterface.

  What exists
  -----------

  Every function of Qt's QDesignerCustomWidgetInterface that has a ritual and
  that Python can call so far, 12 names in all: 'name', 'group', 'toolTip',
  'whatsThis', 'includeFile', 'icon', 'isContainer', 'createWidget',
  'isInitialized', 'initialize', 'domXml', 'codeTemplate'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerCustomWidgetInterface::~QDesignerCustomWidgetInterface()':
    the destructor: Python never removes a C++
    QDesignerCustomWidgetInterface.

  What to expect
  --------------

  - The C++ QDesignerCustomWidgetInterface is created at the first use, not
    by 'QDesignerCustomWidgetInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerCustomWidgetInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerCustomWidgetInterface'

  #  A C++ QDesignerCustomWidgetInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerCustomWidgetInterface'

  #  The functions Qt calls itself that QDesignerCustomWidgetInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK30QDesignerCustomWidgetInterface4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'group': (
          ('_ZNK30QDesignerCustomWidgetInterface5groupEv',
           ('address', 'text', ''),
           ()),
      ),
      'toolTip': (
          ('_ZNK30QDesignerCustomWidgetInterface7toolTipEv',
           ('address', 'text', ''),
           ()),
      ),
      'whatsThis': (
          ('_ZNK30QDesignerCustomWidgetInterface9whatsThisEv',
           ('address', 'text', ''),
           ()),
      ),
      'includeFile': (
          ('_ZNK30QDesignerCustomWidgetInterface11includeFileEv',
           ('address', 'text', ''),
           ()),
      ),
      'icon': (
          ('_ZNK30QDesignerCustomWidgetInterface4iconEv',
           ('address', 'value', 'QtGui:QIcon'),
           ()),
      ),
      'isContainer': (
          ('_ZNK30QDesignerCustomWidgetInterface11isContainerEv',
           ('bool', 'number', ''),
           ()),
      ),
      'createWidget': (
          ('_ZN30QDesignerCustomWidgetInterface12createWidgetEP7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'isInitialized': (
          ('_ZNK30QDesignerCustomWidgetInterface13isInitializedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'initialize': (
          ('_ZN30QDesignerCustomWidgetInterface10initializeEP28QDesignerFor'
           'mEditorInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormEditorInterface'),
           )),
      ),
      'domXml': (
          ('_ZNK30QDesignerCustomWidgetInterface6domXmlEv',
           ('address', 'text', ''),
           ()),
      ),
      'codeTemplate': (
          ('_ZNK30QDesignerCustomWidgetInterface12codeTemplateEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetInterface::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetInterface::name() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerCustomWidgetInterface4nameEv',
    )

  def group(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetInterface::group() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#group

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetInterface::group() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerCustomWidgetInterface5groupEv',
    )

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetInterface::toolTip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetInterface::toolTip() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerCustomWidgetInterface7toolTipEv',
    )

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetInterface::whatsThis() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#whatsThis

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetInterface::whatsThis() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerCustomWidgetInterface9whatsThisEv',
    )

  def includeFile(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetInterface::includeFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#includeFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetInterface::includeFile() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerCustomWidgetInterface11includeFileEv',
    )

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QDesignerCustomWidgetInterface::icon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QDesignerCustomWidgetInterface::icon() const
    address = self.uglySide.call(
        'ritual_ZNK30QDesignerCustomWidgetInterface4iconEv',
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def isContainer(self) -> bool:
    """
    Calls Qt's 'bool QDesignerCustomWidgetInterface::isContainer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#isContainer
    """
    #  bool QDesignerCustomWidgetInterface::isContainer() const
    return self.uglySide.call(
        'ritual_ZNK30QDesignerCustomWidgetInterface11isContainerEv',
    )

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QDesignerCustomWidgetInterface::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#isInitialized
    """
    #  bool QDesignerCustomWidgetInterface::isInitialized() const
    ritual = 'ritual_ZNK30QDesignerCustomWidgetInterface13isInitializedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QDesignerCustomWidgetInterface13isInitializedEv')
    return self.uglySide.call(ritual)

  def domXml(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetInterface::domXml() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#domXml

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetInterface::domXml() const
    ritual = 'ritual_ZNK30QDesignerCustomWidgetInterface6domXmlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK30QDesignerCustomWidgetInterface6domXmlEv'
    return self.uglySide.call(ritual)

  def codeTemplate(self) -> str:
    """
    Calls Qt's 'QString QDesignerCustomWidgetInterface::codeTemplate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#codeTemplate

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerCustomWidgetInterface::codeTemplate() const
    ritual = 'ritual_ZNK30QDesignerCustomWidgetInterface12codeTemplateEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK30QDesignerCustomWidgetInterface12codeTemplateEv')
    return self.uglySide.call(ritual)

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

  @overload(QWidget)
  @overload(NoneType)
  def createWidget(self, parent: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerCustomWidgetInterface::createWidget(QWidget
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#createWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerCustomWidgetInterface::createWidget(QWidget *parent)
    address = self.uglySide.call(
        'ritual_ZN30QDesignerCustomWidgetInterface12createWidgetEP7QWidget',
        self._addressOf(parent),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def initialize(self, core: Optional[QDesignerFormEditorInterface]) -> None:
    """
    Calls Qt's 'void
    QDesignerCustomWidgetInterface::initialize(QDesignerFormEditorInterface
    *core)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignercustomwidgetinterface.html#initialize

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerCustomWidgetInterface::initialize(
    #      QDesignerFormEditorInterface *core)
    ritual = (
        'ritual_ZN30QDesignerCustomWidgetInterface10initializeEP28QDesigner'
        'FormEditorInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QDesignerCustomWidgetInterface10initializeEP28QDe'
          'signerFormEditorInterface')
    self.uglySide.call(ritual, self._addressOf(core))


#  Qt's 'QList<QDesignerCustomWidgetInterface *>': the list of
#  QDesignerCustomWidgetInterface, which
#  'QList[QDesignerCustomWidgetInterface]' gives. It is made here, so that
#  there is one as soon as there can be a QDesignerCustomWidgetInterface.
QList.createKind(
    QDesignerCustomWidgetInterface, 'address',
    make='ritual_list_make_QDesignerCustomWidgetInterface_ptr',
    add='ritual_list_add_QDesignerCustomWidgetInterface_ptr',
    size='ritual_list_size_QDesignerCustomWidgetInterface_ptr',
    at='ritual_list_at_QDesignerCustomWidgetInterface_ptr',
    drop='ritual_list_drop_QDesignerCustomWidgetInterface_ptr',
)
