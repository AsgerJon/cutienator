"""
qdesigner_internal::QDesignerPromotion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotion_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerPromotion to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QDesignerPromotionInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QString
  from . import QDesignerFormEditorInterface
  from . import QDesignerWidgetDataBaseItemInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerWidgetDataBaseItemInterface = WAIT['QDesignerWidgetDataBaseItemInterface']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerPromotion(QDesignerPromotionInterface):
  """
  The cute side of Qt's qdesigner_internal::QDesignerPromotion: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerPromotion.

  It is built on the cute 'QDesignerPromotionInterface', as Qt's
  qdesigner_internal::QDesignerPromotion is built on Qt's
  QDesignerPromotionInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerPromotion that has a
  ritual and that Python can call so far, 7 names in all: 'addPromotedClass',
  'removePromotedClass', 'changePromotedClassName',
  'setPromotedClassIncludeFile', 'promotionBaseClasses', 'canBePromoted',
  'refreshObjectInspector'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'PromotedClasses
    qdesigner_internal::QDesignerPromotion::promotedClasses() const': gives a
    type Python has no way to take yet.
  - Qt's 'QSet<QString>
    qdesigner_internal::QDesignerPromotion::referencedPromotedClassNames()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerPromotion is created at the first
    use, not by 'qdesigner_internal::QDesignerPromotion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerPromotion.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerPromotion'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def promotionBaseClasses(
      self,
  ) -> QList[QDesignerWidgetDataBaseItemInterface]:
    """
    Calls Qt's 'QList<QDesignerWidgetDataBaseItemInterface *>
    qdesigner_internal::QDesignerPromotion::promotionBaseClasses() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotion.html

    Returns
    -------

    QList[QDesignerWidgetDataBaseItemInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDesignerWidgetDataBaseItemInterface *>
    #      qdesigner_internal::QDesignerPromotion::promotionBaseClasses()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18QDesignerPromotion20promotionBaseC'
        'lassesEv',
    )
    from . import QDesignerWidgetDataBaseItemInterface
    return QList[QDesignerWidgetDataBaseItemInterface]._cuteOwning(address)

  @overload(QDesignerWidgetDataBaseItemInterface)
  @overload(NoneType)
  def canBePromoted(
      self,
      a0: Optional[QDesignerWidgetDataBaseItemInterface],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerPromotion::canBePromoted(const
    QDesignerWidgetDataBaseItemInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotion.html

    Parameters
    ----------

    a0 : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerPromotion::canBePromoted(const
    #      QDesignerWidgetDataBaseItemInterface *a0) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18QDesignerPromotion13canBePromotedE'
        'PK36QDesignerWidgetDataBaseItemInterface',
        self._addressOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str, QString)
  @overload(str, str, NoneType)
  def setPromotedClassIncludeFile(
      self,
      className: str,
      includeFile: str,
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerPromotion::setPromotedClassIncludeFile(const
    QString &className, const QString &includeFile, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotion.html

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    includeFile : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerPromotion::
    #      setPromotedClassIncludeFile(const QString &className, const
    #      QString &includeFile, QString *errorMessage)
    ritual = (
        'ritual_ZN18qdesigner_internal18QDesignerPromotion27setPromotedClas'
        'sIncludeFileERK7QStringS3_PS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18QDesignerPromotion27setPromot'
          'edClassIncludeFileERK7QStringS3_PS1_')
    return self.uglySide.call(
        ritual, className, includeFile, self._addressOf(errorMessage),
    )

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
    'qdesigner_internal::QDesignerPromotion::QDesignerPromotion(
    QDesignerFormEditorInterface *core)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotion.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::QDesignerPromotion::QDesignerPromotion(
    #      QDesignerFormEditorInterface *core)
    self._noteCreation(QDesignerPromotion, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal18QDesignerPromotionC1EP28QDesignerFo'
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

  @overload(str, str, str, QString)
  @overload(str, str, str, NoneType)
  def addPromotedClass(
      self,
      baseClass: str,
      className: str,
      includeFile: str,
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerPromotion::addPromotedClass(const QString
    &baseClass, const QString &className, const QString &includeFile, QString
    *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotion.html

    Parameters
    ----------

    baseClass : str
      Passed on as it is: a QString is made of it for the call.

    className : str
      Passed on as it is: a QString is made of it for the call.

    includeFile : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerPromotion::addPromotedClass(const
    #      QString &baseClass, const QString &className, const QString
    #      &includeFile, QString *errorMessage)
    ritual = (
        'ritual_ZN18qdesigner_internal18QDesignerPromotion16addPromotedClas'
        'sERK7QStringS3_S3_PS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18QDesignerPromotion16addPromot'
          'edClassERK7QStringS3_S3_PS1_')
    return self.uglySide.call(
        ritual,
        baseClass, className, includeFile, self._addressOf(errorMessage),
    )

  @overload(str, QString)
  @overload(str, NoneType)
  def removePromotedClass(
      self,
      className: str,
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerPromotion::removePromotedClass(const QString
    &className, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotion.html

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerPromotion::removePromotedClass(const
    #      QString &className, QString *errorMessage)
    ritual = (
        'ritual_ZN18qdesigner_internal18QDesignerPromotion19removePromotedC'
        'lassERK7QStringPS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18QDesignerPromotion19removePro'
          'motedClassERK7QStringPS1_')
    return self.uglySide.call(
        ritual, className, self._addressOf(errorMessage),
    )

  @overload(str, str, QString)
  @overload(str, str, NoneType)
  def changePromotedClassName(
      self,
      oldclassName: str,
      newClassName: str,
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerPromotion::changePromotedClassName(const
    QString &oldclassName, const QString &newClassName, QString
    *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotion.html

    Parameters
    ----------

    oldclassName : str
      Passed on as it is: a QString is made of it for the call.

    newClassName : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerPromotion::changePromotedClassName(
    #      const QString &oldclassName, const QString &newClassName, QString
    #      *errorMessage)
    ritual = (
        'ritual_ZN18qdesigner_internal18QDesignerPromotion23changePromotedC'
        'lassNameERK7QStringS3_PS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18QDesignerPromotion23changePro'
          'motedClassNameERK7QStringS3_PS1_')
    return self.uglySide.call(
        ritual, oldclassName, newClassName, self._addressOf(errorMessage),
    )

  def refreshObjectInspector(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotion::refreshObjectInspector()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotion.html
    """
    #  void qdesigner_internal::QDesignerPromotion::refreshObjectInspector()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18QDesignerPromotion22refreshObjectIn'
        'spectorEv',
    )
