"""
qdesigner_internal::QEditorFormBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qsimpleresource_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QEditorFormBuilder to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QObject
  from ..QtWidgets import QWidget
  from . import DomUI, QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomUI = WAIT['DomUI']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QIODevice = WAIT['QIODevice']
  QObject = WAIT['QObject']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEditorFormBuilder(qdesigner_internal.QSimpleResource):
  """
  The cute side of Qt's qdesigner_internal::QEditorFormBuilder: a plain
  Python object standing in front of one C++
  qdesigner_internal::QEditorFormBuilder.

  It is built on the cute 'qdesigner_internal::QSimpleResource', as Qt's
  qdesigner_internal::QEditorFormBuilder is built on Qt's
  qdesigner_internal::QSimpleResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QEditorFormBuilder that has a
  ritual and that Python can call so far, 2 names in all: 'copy', 'paste'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::QEditorFormBuilder is created at the first
    use, not by 'qdesigner_internal::QEditorFormBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QEditorFormBuilder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QEditorFormBuilder'

  #  A C++ qdesigner_internal::QEditorFormBuilder Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_QEditorFormBuilder'

  #  The functions Qt calls itself that
  #  qdesigner_internal::QEditorFormBuilder is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'copy': (
          ('_ZN18qdesigner_internal18QEditorFormBuilder4copyEP9QIODeviceRKN'
           'S_20FormBuilderClipboardE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
               ('address', 'value',
                'QtDesigner:qdesigner_internal.FormBuilderClipboard'),
           )),
          ('_ZN18qdesigner_internal18QEditorFormBuilder4copyERKNS_20FormBui'
           'lderClipboardE',
           ('address', 'address', 'QtDesigner:DomUI'),
           (
               ('address', 'value',
                'QtDesigner:qdesigner_internal.FormBuilderClipboard'),
           )),
      ),
      'paste': (
          ('_ZN18qdesigner_internal18QEditorFormBuilder5pasteEP5DomUIP7QWid'
           'getP7QObject',
           ('address', 'value',
            'QtDesigner:qdesigner_internal.FormBuilderClipboard'),
           (
               ('address', 'address', 'QtDesigner:DomUI'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtCore:QObject'),
           )),
          ('_ZN18qdesigner_internal18QEditorFormBuilder5pasteEP9QIODeviceP7'
           'QWidgetP7QObject',
           ('address', 'value',
            'QtDesigner:qdesigner_internal.FormBuilderClipboard'),
           (
               ('address', 'address', 'QtCore:QIODevice'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtCore:QObject'),
           )),
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def __init__(self, core: Optional[QDesignerFormEditorInterface]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QEditorFormBuilder::QEditorFormBuilder(
    QDesignerFormEditorInterface *core)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qeditorformbuilder.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::QEditorFormBuilder::QEditorFormBuilder(
    #      QDesignerFormEditorInterface *core)
    self._noteCreation(QEditorFormBuilder, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal18QEditorFormBuilderC1EP28QDesignerFo'
        'rmEditorInterface',
        self._addressOf(core),
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

  @overload(QIODevice, WAIT['qdesigner_internal.FormBuilderClipboard'])
  @overload(NoneType, WAIT['qdesigner_internal.FormBuilderClipboard'])
  def copy(
      self,
      dev: Optional[QIODevice],
      selection: qdesigner_internal.FormBuilderClipboard,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::QEditorFormBuilder::copy(QIODevice
    *dev, const FormBuilderClipboard &selection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qeditorformbuilder.html#copy

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    selection : qdesigner_internal.FormBuilderClipboard
      Passed on as a value: Qt reads the C++
      qdesigner_internal::FormBuilderClipboard, which stays Python's own.
    """
    #  bool qdesigner_internal::QEditorFormBuilder::copy(QIODevice *dev,
    #      const FormBuilderClipboard &selection)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18QEditorFormBuilder4copyEP9QIODevice'
        'RKNS_20FormBuilderClipboardE',
        self._addressOf(dev), self._valueOf(selection),
    )

  @overload(WAIT['qdesigner_internal.FormBuilderClipboard'])
  def copy(
      self,
      selection: qdesigner_internal.FormBuilderClipboard,
  ) -> Optional[DomUI]:
    """
    Calls Qt's 'DomUI *qdesigner_internal::QEditorFormBuilder::copy(const
    FormBuilderClipboard &selection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qeditorformbuilder.html#copy

    Parameters
    ----------

    selection : qdesigner_internal.FormBuilderClipboard
      Passed on as a value: Qt reads the C++
      qdesigner_internal::FormBuilderClipboard, which stays Python's own.

    Returns
    -------

    Optional[DomUI]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomUI *qdesigner_internal::QEditorFormBuilder::copy(const
    #      FormBuilderClipboard &selection)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal18QEditorFormBuilder4copyERKNS_20Form'
        'BuilderClipboardE',
        self._valueOf(selection),
    )
    from . import DomUI
    return DomUI._cuteAt(address)

  @overload(DomUI, QWidget)
  @overload(DomUI, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(DomUI, QWidget, QObject)
  @overload(DomUI, QWidget, NoneType)
  @overload(DomUI, NoneType, QObject)
  @overload(DomUI, NoneType, NoneType)
  @overload(NoneType, QWidget, QObject)
  @overload(NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def paste(
      self,
      ui: Optional[DomUI],
      widgetParent: Optional[QWidget],
      actionParent: Optional[QObject] = None,
  ) -> qdesigner_internal.FormBuilderClipboard:
    """
    Calls Qt's 'FormBuilderClipboard
    qdesigner_internal::QEditorFormBuilder::paste(DomUI *ui, QWidget
    *widgetParent, QObject *actionParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qeditorformbuilder.html#paste

    Parameters
    ----------

    ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widgetParent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    actionParent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    qdesigner_internal.FormBuilderClipboard
      A new cute qdesigner_internal::FormBuilderClipboard around the copy Qt
      gave back. Python owns it.
    """
    #  FormBuilderClipboard
    #      qdesigner_internal::QEditorFormBuilder::paste(DomUI *ui, QWidget
    #      *widgetParent, QObject *actionParent)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal18QEditorFormBuilder5pasteEP5DomUIP7Q'
        'WidgetP7QObject',
        self._addressOf(ui), self._addressOf(widgetParent),
        self._addressOf(actionParent, 'QObject'),
    )
    return qdesigner_internal.FormBuilderClipboard._cuteOwning(address)

  @overload(QIODevice, QWidget)
  @overload(QIODevice, NoneType)
  @overload(QIODevice, QWidget, QObject)
  @overload(QIODevice, QWidget, NoneType)
  @overload(QIODevice, NoneType, QObject)
  @overload(QIODevice, NoneType, NoneType)
  def paste(
      self,
      dev: Optional[QIODevice],
      widgetParent: Optional[QWidget],
      actionParent: Optional[QObject] = None,
  ) -> qdesigner_internal.FormBuilderClipboard:
    """
    Calls Qt's 'FormBuilderClipboard
    qdesigner_internal::QEditorFormBuilder::paste(QIODevice *dev, QWidget
    *widgetParent, QObject *actionParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qeditorformbuilder.html#paste

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widgetParent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    actionParent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    qdesigner_internal.FormBuilderClipboard
      A new cute qdesigner_internal::FormBuilderClipboard around the copy Qt
      gave back. Python owns it.
    """
    #  FormBuilderClipboard
    #      qdesigner_internal::QEditorFormBuilder::paste(QIODevice *dev,
    #      QWidget *widgetParent, QObject *actionParent)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal18QEditorFormBuilder5pasteEP9QIODevic'
        'eP7QWidgetP7QObject',
        self._addressOf(dev), self._addressOf(widgetParent),
        self._addressOf(actionParent, 'QObject'),
    )
    return qdesigner_internal.FormBuilderClipboard._cuteOwning(address)
