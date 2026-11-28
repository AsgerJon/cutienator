"""
qdesigner_internal::WidgetDataBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/widgetdatabase_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::WidgetDataBase to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from . import QDesignerWidgetDataBaseInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize, QVariant
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class WidgetDataBase(QDesignerWidgetDataBaseInterface):
  """
  The cute side of Qt's qdesigner_internal::WidgetDataBase: a plain Python
  object standing in front of one C++ qdesigner_internal::WidgetDataBase.

  It is built on the cute 'QDesignerWidgetDataBaseInterface', as Qt's
  qdesigner_internal::WidgetDataBase is built on Qt's
  QDesignerWidgetDataBaseInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::WidgetDataBase that has a ritual
  and that Python can call so far, 13 names in all: 'metaObject', 'tr',
  'core', 'indexOfObject', 'remove', 'grabDefaultPropertyValues',
  'grabStandardWidgetBoxIcons', 'formWidgetClasses',
  'customFormWidgetClasses', 'formTemplate', 'scaleFormTemplate',
  'loadPlugins', 'defaultPropertyValues'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::WidgetDataBase::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::WidgetDataBase::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::WidgetDataBase::~WidgetDataBase()': the
    destructor: Python never removes a C++
    qdesigner_internal::WidgetDataBase.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::WidgetDataBase is created at the first use,
    not by 'qdesigner_internal::WidgetDataBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::WidgetDataBase.
  - Qt tells when it has removed the C++ qdesigner_internal::WidgetDataBase.
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
    Calls Qt's 'QString qdesigner_internal::WidgetDataBase::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html#tr

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
    #  QString qdesigner_internal::WidgetDataBase::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def formWidgetClasses(
      core: Optional[QDesignerFormEditorInterface],
  ) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::WidgetDataBase::formWidgetClasses(const
    QDesignerFormEditorInterface *core)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      qdesigner_internal::WidgetDataBase::formWidgetClasses(const
    #      QDesignerFormEditorInterface *core)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase17formWidgetClassesEP'
        'K28QDesignerFormEditorInterface',
        CuteMixin._addressOf(core),
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def customFormWidgetClasses(
      core: Optional[QDesignerFormEditorInterface],
  ) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::WidgetDataBase::customFormWidgetClasses(const
    QDesignerFormEditorInterface *core)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      qdesigner_internal::WidgetDataBase::customFormWidgetClasses(const
    #      QDesignerFormEditorInterface *core)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase23customFormWidgetCla'
        'ssesEPK28QDesignerFormEditorInterface',
        CuteMixin._addressOf(core),
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QDesignerFormEditorInterface, str, str)
  @overload(NoneType, str, str)
  def formTemplate(
      core: Optional[QDesignerFormEditorInterface],
      className: str,
      objectName: str,
  ) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::WidgetDataBase::formTemplate(const
    QDesignerFormEditorInterface *core, const QString &className, const
    QString &objectName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    className : str
      Passed on as it is: a QString is made of it for the call.

    objectName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBase::formTemplate(const
    #      QDesignerFormEditorInterface *core, const QString &className,
    #      const QString &objectName)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase12formTemplateEPK28QD'
        'esignerFormEditorInterfaceRK7QStringS6_',
        CuteMixin._addressOf(core), className, objectName,
    )

  @staticmethod
  @overload(str, QSize, bool)
  def scaleFormTemplate(xml: str, size: QSize, fixed: bool) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::WidgetDataBase::scaleFormTemplate(const QString &xml,
    const QSize &size, bool fixed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html

    Parameters
    ----------

    xml : str
      Passed on as it is: a QString is made of it for the call.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    fixed : bool
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::WidgetDataBase::scaleFormTemplate(const
    #      QString &xml, const QSize &size, bool fixed)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase17scaleFormTemplateER'
        'K7QStringRK5QSizeb',
        xml, CuteMixin._valueOf(size), fixed,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::WidgetDataBase'

  #  A C++ qdesigner_internal::WidgetDataBase Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_WidgetDataBase'

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
    *qdesigner_internal::WidgetDataBase::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::WidgetDataBase::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14WidgetDataBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *qdesigner_internal::WidgetDataBase::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *qdesigner_internal::WidgetDataBase::core() const
    ritual = 'ritual_ZNK18qdesigner_internal14WidgetDataBase4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal14WidgetDataBase4coreEv'
    address = self.uglySide.call(ritual)
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, bool)
  @overload(NoneType, bool)
  def indexOfObject(
      self,
      o: Optional[QObject],
      resolveName: bool = True,
  ) -> int:
    """
    Calls Qt's 'int qdesigner_internal::WidgetDataBase::indexOfObject(QObject
    *o, bool resolveName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resolveName : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  int qdesigner_internal::WidgetDataBase::indexOfObject(QObject *o, bool
    #      resolveName) const
    ritual = (
        'ritual_ZNK18qdesigner_internal14WidgetDataBase13indexOfObjectEP7QO'
        'bjectb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14WidgetDataBase13indexOfObjec'
          'tEP7QObjectb')
    return self.uglySide.call(
        ritual, self._addressOf(o, 'QObject'), resolveName,
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(QDesignerFormEditorInterface, QObject)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::WidgetDataBase::WidgetDataBase(
    QDesignerFormEditorInterface *core, QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::WidgetDataBase::WidgetDataBase(
    #      QDesignerFormEditorInterface *core, QObject *parent)
    self._noteCreation(WidgetDataBase, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBaseC1EP28QDesignerFormEd'
        'itorInterfaceP7QObject',
        self._addressOf(core), self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def remove(self, index: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBase::remove(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html#remove

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void qdesigner_internal::WidgetDataBase::remove(int index)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase6removeEi', index,
    )

  def grabDefaultPropertyValues(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBase::grabDefaultPropertyValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html
    """
    #  void qdesigner_internal::WidgetDataBase::grabDefaultPropertyValues()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase25grabDefaultProperty'
        'ValuesEv',
    )

  def grabStandardWidgetBoxIcons(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::WidgetDataBase::grabStandardWidgetBoxIcons()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html
    """
    #  void qdesigner_internal::WidgetDataBase::grabStandardWidgetBoxIcons()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase26grabStandardWidgetB'
        'oxIconsEv',
    )

  def loadPlugins(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::WidgetDataBase::loadPlugins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html#loadPlugins
    """
    #  void qdesigner_internal::WidgetDataBase::loadPlugins()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase11loadPluginsEv',
    )

  @overload(str)
  def defaultPropertyValues(self, name: str) -> QList[QVariant]:
    """
    Calls Qt's 'QList<QVariant>
    qdesigner_internal::WidgetDataBase::defaultPropertyValues(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-widgetdatabase.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVariant>
    #      qdesigner_internal::WidgetDataBase::defaultPropertyValues(const
    #      QString &name)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14WidgetDataBase21defaultPropertyValu'
        'esERK7QString',
        name,
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)
