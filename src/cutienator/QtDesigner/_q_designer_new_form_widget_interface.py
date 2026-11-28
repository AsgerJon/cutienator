"""
QDesignerNewFormWidgetInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractnewformwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QString
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerNewFormWidgetInterface(QWidget):
  """
  The cute side of Qt's QDesignerNewFormWidgetInterface: a plain Python
  object standing in front of one C++ QDesignerNewFormWidgetInterface.

  It is built on the cute 'QWidget', as Qt's QDesignerNewFormWidgetInterface
  is built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerNewFormWidgetInterface that has a ritual
  and that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'hasCurrentTemplate', 'currentTemplate', 'createNewFormWidget',
  'templateActivated', 'currentTemplateChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerNewFormWidgetInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QDesignerNewFormWidgetInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDesignerNewFormWidgetInterface::~QDesignerNewFormWidgetInterface()':
    the destructor: Python never removes a C++
    QDesignerNewFormWidgetInterface.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerNewFormWidgetInterface is created at the first use, not
    by 'QDesignerNewFormWidgetInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerNewFormWidgetInterface.
  - Qt tells when it has removed the C++ QDesignerNewFormWidgetInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QDesignerNewFormWidgetInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignernewformwidgetinterface.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerNewFormWidgetInterface::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QDesignerNewFormWidgetInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def createNewFormWidget(
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QWidget] = None,
  ) -> Optional[QDesignerNewFormWidgetInterface]:
    """
    Calls Qt's 'QDesignerNewFormWidgetInterface
    *QDesignerNewFormWidgetInterface::createNewFormWidget(
    QDesignerFormEditorInterface *core, QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignernewformwidgetinterface.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QDesignerNewFormWidgetInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerNewFormWidgetInterface
    #      *QDesignerNewFormWidgetInterface::createNewFormWidget(
    #      QDesignerFormEditorInterface *core, QWidget *parent)
    address = Rituals.call(
        'ritual_ZN31QDesignerNewFormWidgetInterface19createNewFormWidgetEP2'
        '8QDesignerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(parent),
    )
    return QDesignerNewFormWidgetInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerNewFormWidgetInterface'

  #  A C++ QDesignerNewFormWidgetInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerNewFormWidgetInterface'

  #  The functions Qt calls itself that QDesignerNewFormWidgetInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'hasCurrentTemplate': (
          ('_ZNK31QDesignerNewFormWidgetInterface18hasCurrentTemplateEv',
           ('bool', 'number', ''),
           ()),
      ),
      'currentTemplate': (
          ('_ZN31QDesignerNewFormWidgetInterface15currentTemplateEP7QString',
           ('address', 'text', ''),
           (
               ('address', 'address', 'QtCore:QString'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QDesignerNewFormWidgetInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignernewformwidgetinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerNewFormWidgetInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QDesignerNewFormWidgetInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasCurrentTemplate(self) -> bool:
    """
    Calls Qt's 'bool QDesignerNewFormWidgetInterface::hasCurrentTemplate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignernewformwidgetinterface.html
    """
    #  bool QDesignerNewFormWidgetInterface::hasCurrentTemplate() const
    return self.uglySide.call(
        'ritual_ZNK31QDesignerNewFormWidgetInterface18hasCurrentTemplateEv',
    )

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerNewFormWidgetInterface::QDesignerNewFormWidgetInterface(QWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignernewformwidgetinterface.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerNewFormWidgetInterface::QDesignerNewFormWidgetInterface(
    #      QWidget *parent)
    self._noteCreation(QDesignerNewFormWidgetInterface, lambda: Rituals.call(
        'ritual_ZN31QDesignerNewFormWidgetInterfaceC1EP7QWidget',
        self._addressOf(parent),
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

  @overload()
  @overload(QString)
  @overload(NoneType)
  def currentTemplate(self, errorMessage: Optional[QString] = None) -> str:
    """
    Calls Qt's 'QString
    QDesignerNewFormWidgetInterface::currentTemplate(QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignernewformwidgetinterface.html

    Parameters
    ----------

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerNewFormWidgetInterface::currentTemplate(QString
    #      *errorMessage)
    return self.uglySide.call(
        'ritual_ZN31QDesignerNewFormWidgetInterface15currentTemplateEP7QStr'
        'ing',
        self._addressOf(errorMessage),
    )

  def templateActivated(self) -> None:
    """
    Calls Qt's 'void QDesignerNewFormWidgetInterface::templateActivated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignernewformwidgetinterface.html
    """
    #  void QDesignerNewFormWidgetInterface::templateActivated()
    self.uglySide.call(
        'ritual_ZN31QDesignerNewFormWidgetInterface17templateActivatedEv',
    )

  @overload(bool)
  def currentTemplateChanged(self, templateSelected: bool) -> None:
    """
    Calls Qt's 'void
    QDesignerNewFormWidgetInterface::currentTemplateChanged(bool
    templateSelected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignernewformwidgetinterface.html

    Parameters
    ----------

    templateSelected : bool
      Passed on as it is.
    """
    #  void QDesignerNewFormWidgetInterface::currentTemplateChanged(bool
    #      templateSelected)
    self.uglySide.call(
        'ritual_ZN31QDesignerNewFormWidgetInterface22currentTemplateChanged'
        'Eb',
        templateSelected,
    )
