"""
qdesigner_internal::QDesignerPropertyEditor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_propertyeditor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerPropertyEditor to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QDesignerPropertyEditorInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerPropertyEditor(QDesignerPropertyEditorInterface):
  """
  The cute side of Qt's qdesigner_internal::QDesignerPropertyEditor: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerPropertyEditor.

  It is built on the cute 'QDesignerPropertyEditorInterface', as Qt's
  qdesigner_internal::QDesignerPropertyEditor is built on Qt's
  QDesignerPropertyEditorInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerPropertyEditor that has
  a ritual and that Python can call so far, 12 names in all: 'metaObject',
  'tr', 'propertyValueChanged', 'resetProperty', 'addDynamicProperty',
  'removeDynamicProperty', 'editorOpened', 'editorClosed',
  'updatePropertySheet', 'reloadResourceProperties', 'slotPropertyChanged',
  'emitPropertyValueChanged'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *qdesigner_internal::QDesignerPropertyEditor::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::QDesignerPropertyEditor::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'StringPropertyParameters
    qdesigner_internal::QDesignerPropertyEditor::textPropertyValidationMode(
    QDesignerFormEditorInterface *core, const QObject *object, const QString
    &propertyName, bool isMainContainer)': gives a type Python has no way to
    take yet.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerPropertyEditor is created at the
    first use, not by 'qdesigner_internal::QDesignerPropertyEditor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerPropertyEditor.
  - Qt tells when it has removed the C++
    qdesigner_internal::QDesignerPropertyEditor. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::QDesignerPropertyEditor that has no
    cute function yet, '__init__', 'textPropertyValidationMode', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString qdesigner_internal::QDesignerPropertyEditor::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html#tr

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
    #  QString qdesigner_internal::QDesignerPropertyEditor::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerPropertyEditor'

  #  The functions Qt calls itself that
  #  qdesigner_internal::QDesignerPropertyEditor is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'updatePropertySheet': (
          ('_ZN18qdesigner_internal23QDesignerPropertyEditor19updatePropert'
           'ySheetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reloadResourceProperties': (
          ('_ZN18qdesigner_internal23QDesignerPropertyEditor24reloadResourc'
           'ePropertiesEv',
           ('nothing', 'nothing', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::QDesignerPropertyEditor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::QDesignerPropertyEditor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal23QDesignerPropertyEditor10metaObjec'
        'tEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'qdesigner_internal::QDesignerPropertyEditor::QDesignerPropertyEditor(
    QWidget *parent, Qt::WindowFlags flags)': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerPropertyEditor.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::QDesignerPropertyEditor::QDesignerPropertyEdit"
        "or(QWidget *parent, Qt::WindowFlags flags)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload(str, QVariant, bool)
  def propertyValueChanged(
      self,
      name: str,
      value: QVariant,
      enableSubPropertyHandling: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::propertyValueChanged(const
    QString &name, const QVariant &value, bool enableSubPropertyHandling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    enableSubPropertyHandling : bool
      Passed on as it is.
    """
    #  void
    #      qdesigner_internal::QDesignerPropertyEditor::propertyValueChanged(
    #      const QString &name, const QVariant &value, bool
    #      enableSubPropertyHandling)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor20propertyVa'
        'lueChangedERK7QStringRK8QVariantb',
        name, self._valueOf(value), enableSubPropertyHandling,
    )

  @overload(str)
  def resetProperty(self, name: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::resetProperty(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::QDesignerPropertyEditor::resetProperty(const
    #      QString &name)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor13resetPrope'
        'rtyERK7QString',
        name,
    )

  @overload(str, QVariant)
  def addDynamicProperty(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::addDynamicProperty(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void qdesigner_internal::QDesignerPropertyEditor::addDynamicProperty(
    #      const QString &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor18addDynamic'
        'PropertyERK7QStringRK8QVariant',
        name, self._valueOf(value),
    )

  @overload(str)
  def removeDynamicProperty(self, name: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::removeDynamicProperty(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::QDesignerPropertyEditor::
    #      removeDynamicProperty(const QString &name)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor21removeDyna'
        'micPropertyERK7QString',
        name,
    )

  def editorOpened(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::editorOpened()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html
    """
    #  void qdesigner_internal::QDesignerPropertyEditor::editorOpened()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor12editorOpen'
        'edEv',
    )

  def editorClosed(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::editorClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html
    """
    #  void qdesigner_internal::QDesignerPropertyEditor::editorClosed()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor12editorClos'
        'edEv',
    )

  def updatePropertySheet(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::updatePropertySheet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html
    """
    #  void
    #      qdesigner_internal::QDesignerPropertyEditor::updatePropertySheet()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor19updateProp'
        'ertySheetEv',
    )

  def reloadResourceProperties(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::reloadResourceProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html
    """
    #  void qdesigner_internal::QDesignerPropertyEditor::
    #      reloadResourceProperties()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor24reloadReso'
        'urcePropertiesEv',
    )

  @overload(str, QVariant)
  def slotPropertyChanged(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::slotPropertyChanged(const
    QString &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void qdesigner_internal::QDesignerPropertyEditor::slotPropertyChanged(
    #      const QString &name, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor19slotProper'
        'tyChangedERK7QStringRK8QVariant',
        name, self._valueOf(value),
    )

  @overload(str, QVariant, bool)
  def emitPropertyValueChanged(
      self,
      name: str,
      value: QVariant,
      enableSubPropertyHandling: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPropertyEditor::emitPropertyValueChanged(
    const QString &name, const QVariant &value, bool
    enableSubPropertyHandling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpropertyeditor.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    enableSubPropertyHandling : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::QDesignerPropertyEditor::
    #      emitPropertyValueChanged(const QString &name, const QVariant
    #      &value, bool enableSubPropertyHandling)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal23QDesignerPropertyEditor24emitProper'
        'tyValueChangedERK7QStringRK8QVariantb',
        name, self._valueOf(value), enableSubPropertyHandling,
    )

  @staticmethod
  def textPropertyValidationMode(*__, **_) -> Never:
    """
    Qt's 'StringPropertyParameters
    qdesigner_internal::QDesignerPropertyEditor::textPropertyValidationMode(
    QDesignerFormEditorInterface *core, const QObject *object, const QString
    &propertyName, bool isMainContainer)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerPropertyEditor.textPropertyValidationM"
        "ode' has no cute function yet. Qt's 'StringPropertyParameters "
        "qdesigner_internal::QDesignerPropertyEditor::textPropertyValidation"
        "Mode(QDesignerFormEditorInterface *core, const QObject *object, "
        "const QString &propertyName, bool isMainContainer)': gives a type "
        "Python has no way to take yet.")
