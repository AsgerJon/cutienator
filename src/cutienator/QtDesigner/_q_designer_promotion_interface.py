"""
QDesignerPromotionInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractpromotioninterface.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
  from . import QDesignerWidgetDataBaseItemInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerPromotionInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerPromotionInterface: a plain Python object
  standing in front of one C++ QDesignerPromotionInterface.

  What exists
  -----------

  Every function of Qt's QDesignerPromotionInterface that has a ritual and
  that Python can call so far, 5 names in all: 'addPromotedClass',
  'removePromotedClass', 'changePromotedClassName',
  'setPromotedClassIncludeFile', 'promotionBaseClasses'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerPromotionInterface::~QDesignerPromotionInterface()': the
    destructor: Python never removes a C++ QDesignerPromotionInterface.
  - Qt's 'PromotedClasses QDesignerPromotionInterface::promotedClasses()
    const': gives a type Python has no way to take yet.
  - Qt's 'QSet<QString>
    QDesignerPromotionInterface::referencedPromotedClassNames() const': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerPromotionInterface is created at the first use, not by
    'QDesignerPromotionInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerPromotionInterface.
  - Each name of Qt's QDesignerPromotionInterface that has no cute function
    yet, '__init__', 'promotedClasses', 'referencedPromotedClassNames', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QDesignerPromotionInterface, each a class
  #  in here as in C++.

  class PromotedClass(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDesignerPromotionInterface::PromotedClass: a plain
    Python object standing in front of one C++
    QDesignerPromotionInterface::PromotedClass.

    C++ hands a QDesignerPromotionInterface::PromotedClass around as a copy,
    so every C++ QDesignerPromotionInterface::PromotedClass behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QDesignerPromotionInterface::PromotedClass yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDesignerPromotionInterface::PromotedClass::~PromotedClass()':
      the destructor: Python removes its C++
      QDesignerPromotionInterface::PromotedClass by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QDesignerPromotionInterface::PromotedClass is created at the
      first use, not by 'QDesignerPromotionInterface::PromotedClass(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDesignerPromotionInterface::PromotedClass back
      gives a copy the ritual made for Python, in a new cute
      QDesignerPromotionInterface::PromotedClass.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDesignerPromotionInterface::PromotedClass'

    #  Qt's '~QDesignerPromotionInterface::PromotedClass()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QDesignerPromotionInterface::PromotedClass behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN27QDesignerPromotionInterface13PromotedClassD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerPromotionInterface'

  #  A C++ QDesignerPromotionInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerPromotionInterface'

  #  The functions Qt calls itself that QDesignerPromotionInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'promotedClasses': (
          'PromotedClasses QDesignerPromotionInterface::promotedClasses() '
          'const',
      ),
      'referencedPromotedClassNames': (
          'QSet<QString> '
          'QDesignerPromotionInterface::referencedPromotedClassNames() '
          'const',
      ),
      'promotionBaseClasses': (
          'QList<QDesignerWidgetDataBaseItemInterface *> '
          'QDesignerPromotionInterface::promotionBaseClasses() const',
      ),
  }

  #  The functions Qt calls itself that QDesignerPromotionInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'addPromotedClass': (
          ('_ZN27QDesignerPromotionInterface16addPromotedClassERK7QStringS2'
           '_S2_PS0_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
           )),
      ),
      'removePromotedClass': (
          ('_ZN27QDesignerPromotionInterface19removePromotedClassERK7QStrin'
           'gPS0_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
           )),
      ),
      'changePromotedClassName': (
          ('_ZN27QDesignerPromotionInterface23changePromotedClassNameERK7QS'
           'tringS2_PS0_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QString'),
           )),
      ),
      'setPromotedClassIncludeFile': (
          ('_ZN27QDesignerPromotionInterface27setPromotedClassIncludeFileER'
           'K7QStringS2_PS0_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
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

  def promotionBaseClasses(
      self,
  ) -> QList[QDesignerWidgetDataBaseItemInterface]:
    """
    Calls Qt's 'QList<QDesignerWidgetDataBaseItemInterface *>
    QDesignerPromotionInterface::promotionBaseClasses() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpromotioninterface.html

    Returns
    -------

    QList[QDesignerWidgetDataBaseItemInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDesignerWidgetDataBaseItemInterface *>
    #      QDesignerPromotionInterface::promotionBaseClasses() const
    address = self.uglySide.call(
        'ritual_ZNK27QDesignerPromotionInterface20promotionBaseClassesEv',
    )
    from . import QDesignerWidgetDataBaseItemInterface
    return QList[QDesignerWidgetDataBaseItemInterface]._cuteOwning(address)

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
    QDesignerPromotionInterface::setPromotedClassIncludeFile(const QString
    &className, const QString &includeFile, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpromotioninterface.html

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
    #  bool QDesignerPromotionInterface::setPromotedClassIncludeFile(const
    #      QString &className, const QString &includeFile, QString
    #      *errorMessage)
    return self.uglySide.call(
        'ritual_ZN27QDesignerPromotionInterface27setPromotedClassIncludeFil'
        'eERK7QStringS2_PS0_',
        className, includeFile, self._addressOf(errorMessage),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDesignerPromotionInterface::QDesignerPromotionInterface()': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerPromotionInterface.__init__' has no cute function yet. "
        "Qt's 'QDesignerPromotionInterface::QDesignerPromotionInterface()': "
        "the class is abstract, so C++ cannot make one, and the C++ class "
        "of ours does not fill in every function it leaves open.")

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
    Calls Qt's 'bool QDesignerPromotionInterface::addPromotedClass(const
    QString &baseClass, const QString &className, const QString &includeFile,
    QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpromotioninterface.html#addPromotedClass

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
    #  bool QDesignerPromotionInterface::addPromotedClass(const QString
    #      &baseClass, const QString &className, const QString &includeFile,
    #      QString *errorMessage)
    return self.uglySide.call(
        'ritual_ZN27QDesignerPromotionInterface16addPromotedClassERK7QStrin'
        'gS2_S2_PS0_',
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
    Calls Qt's 'bool QDesignerPromotionInterface::removePromotedClass(const
    QString &className, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpromotioninterface.html

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerPromotionInterface::removePromotedClass(const QString
    #      &className, QString *errorMessage)
    return self.uglySide.call(
        'ritual_ZN27QDesignerPromotionInterface19removePromotedClassERK7QSt'
        'ringPS0_',
        className, self._addressOf(errorMessage),
    )

  @overload(str, str, QString)
  @overload(str, str, NoneType)
  def changePromotedClassName(
      self,
      oldClassName: str,
      newClassName: str,
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDesignerPromotionInterface::changePromotedClassName(const QString
    &oldClassName, const QString &newClassName, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerpromotioninterface.html

    Parameters
    ----------

    oldClassName : str
      Passed on as it is: a QString is made of it for the call.

    newClassName : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerPromotionInterface::changePromotedClassName(const
    #      QString &oldClassName, const QString &newClassName, QString
    #      *errorMessage)
    return self.uglySide.call(
        'ritual_ZN27QDesignerPromotionInterface23changePromotedClassNameERK'
        '7QStringS2_PS0_',
        oldClassName, newClassName, self._addressOf(errorMessage),
    )

  @staticmethod
  def promotedClasses(*__, **_) -> Never:
    """
    Qt's 'PromotedClasses QDesignerPromotionInterface::promotedClasses()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDesignerPromotionInterface.promotedClasses' has no cute function "
        "yet. Qt's 'PromotedClasses "
        "QDesignerPromotionInterface::promotedClasses() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def referencedPromotedClassNames(*__, **_) -> Never:
    """
    Qt's 'QSet<QString>
    QDesignerPromotionInterface::referencedPromotedClassNames() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDesignerPromotionInterface.referencedPromotedClassNames' has no "
        "cute function yet. Qt's 'QSet<QString> "
        "QDesignerPromotionInterface::referencedPromotedClassNames() "
        "const': gives a type Python has no way to take yet.")
