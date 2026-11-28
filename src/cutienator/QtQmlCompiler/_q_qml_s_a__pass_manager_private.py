"""
QQmlSA::PassManagerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlSA::PassManagerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSImportVisitor, QQmlJSTypeResolver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSImportVisitor = WAIT['QQmlJSImportVisitor']
  QQmlJSTypeResolver = WAIT['QQmlJSTypeResolver']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PassManagerPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::PassManagerPrivate: a plain Python object
  standing in front of one C++ QQmlSA::PassManagerPrivate.

  What exists
  -----------

  Every function of Qt's QQmlSA::PassManagerPrivate that has a ritual and
  that Python can call so far, 9 names in all: 'get', 'createPassManager',
  'deletePassManager', 'analyze', 'analyzeWrite', 'analyzeRead',
  'analyzeCall', 'analyzeBinding', 'addBindingSourceLocations'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const PassManagerPrivate *QQmlSA::PassManagerPrivate::get(const
    PassManager *manager)': takes in Python what 'PassManagerPrivate
    *QQmlSA::PassManagerPrivate::get(PassManager *manager)' takes.
  - Qt's 'bool QQmlSA::PassManagerPrivate::registerPropertyPass(std::
    shared_ptr<PropertyPass> pass, QAnyStringView moduleName, QAnyStringView
    typeName, QAnyStringView propertyName, bool allowInheritance)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool
    QQmlSA::PassManagerPrivate::registerPropertyPassOnBuiltinType(std::
    shared_ptr<PropertyPass> pass, QAnyStringView typeName, QAnyStringView
    propertyName, bool allowInheritance)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlJSImportVisitor *QQmlSA::PassManagerPrivate::visitor(const
    QQmlSA::PassManager &a0)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlJSTypeResolver *QQmlSA::PassManagerPrivate::resolver(const
    QQmlSA::PassManager &a0)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QSet<PropertyPass *>
    QQmlSA::PassManagerPrivate::findPropertyUsePasses(const QQmlSA::Element
    &element, const QString &propertyName)': gives a type Python has no way
    to take yet.

  What has no ritual
  ------------------

  6 of the 22 functions Qt declares: 4 forbidden; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied; 1 the
  compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ QQmlSA::PassManagerPrivate is created at the first use, not by
    'QQmlSA::PassManagerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSA::PassManagerPrivate.
  - Each name of Qt's QQmlSA::PassManagerPrivate that has no cute function
    yet, 'findPropertyUsePasses', 'hasImportedModule', 'registerElementPass',
    'registerPropertyPass', 'registerPropertyPassOnBuiltinType', 'resolver',
    'visitor', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QQmlSA.PassManager'])
  @overload(NoneType)
  def get(
      manager: Optional[QQmlSA.PassManager],
  ) -> Optional[PassManagerPrivate]:
    """
    Calls Qt's 'PassManagerPrivate
    *QQmlSA::PassManagerPrivate::get(PassManager *manager)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#get

    Parameters
    ----------

    manager : Optional[QQmlSA.PassManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[PassManagerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PassManagerPrivate *QQmlSA::PassManagerPrivate::get(PassManager
    #      *manager)
    address = Rituals.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate3getEPNS_11PassManagerE',
        CuteMixin._addressOf(manager),
    )
    return PassManagerPrivate._cuteAt(address)

  @staticmethod
  @overload(QQmlJSImportVisitor, QQmlJSTypeResolver)
  @overload(QQmlJSImportVisitor, NoneType)
  @overload(NoneType, QQmlJSTypeResolver)
  @overload(NoneType, NoneType)
  def createPassManager(
      visitor: Optional[QQmlJSImportVisitor],
      resolver: Optional[QQmlJSTypeResolver],
  ) -> Optional[QQmlSA.PassManager]:
    """
    Calls Qt's 'PassManager
    *QQmlSA::PassManagerPrivate::createPassManager(QQmlJSImportVisitor
    *visitor, QQmlJSTypeResolver *resolver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#createPassManager

    Parameters
    ----------

    visitor : Optional[QQmlJSImportVisitor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resolver : Optional[QQmlJSTypeResolver]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlSA.PassManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PassManager
    #      *QQmlSA::PassManagerPrivate::createPassManager(QQmlJSImportVisitor
    #      *visitor, QQmlJSTypeResolver *resolver)
    address = Rituals.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate17createPassManagerEP19QQmlJSI'
        'mportVisitorP18QQmlJSTypeResolver',
        CuteMixin._addressOf(visitor), CuteMixin._addressOf(resolver),
    )
    return QQmlSA.PassManager._cuteAt(address)

  @staticmethod
  @overload(WAIT['QQmlSA.PassManager'])
  @overload(NoneType)
  def deletePassManager(q: Optional[QQmlSA.PassManager]) -> None:
    """
    Calls Qt's 'void
    QQmlSA::PassManagerPrivate::deletePassManager(PassManager *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#deletePassManager

    Parameters
    ----------

    q : Optional[QQmlSA.PassManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlSA::PassManagerPrivate::deletePassManager(PassManager *q)
    Rituals.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate17deletePassManagerEPNS_11Pass'
        'ManagerE',
        CuteMixin._addressOf(q),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::PassManagerPrivate'

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

  @overload(QQmlJSImportVisitor, QQmlJSTypeResolver)
  @overload(QQmlJSImportVisitor, NoneType)
  @overload(NoneType, QQmlJSTypeResolver)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      visitor: Optional[QQmlJSImportVisitor],
      resolver: Optional[QQmlJSTypeResolver],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::PassManagerPrivate::PassManagerPrivate(QQmlJSImportVisitor
    *visitor, QQmlJSTypeResolver *resolver)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#PassManagerPrivate

    Parameters
    ----------

    visitor : Optional[QQmlJSImportVisitor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resolver : Optional[QQmlJSTypeResolver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::PassManagerPrivate::PassManagerPrivate(QQmlJSImportVisitor
    #      *visitor, QQmlJSTypeResolver *resolver)
    self._noteCreation(PassManagerPrivate, lambda: Rituals.call(
        'ritual_ZN6QQmlSA18PassManagerPrivateC1EP19QQmlJSImportVisitorP18QQ'
        'mlJSTypeResolver',
        self._addressOf(visitor), self._addressOf(resolver),
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

  @overload(WAIT['QQmlSA.Element'])
  def analyze(self, root: QQmlSA.Element) -> None:
    """
    Calls Qt's 'void QQmlSA::PassManagerPrivate::analyze(const Element
    &root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#analyze

    Parameters
    ----------

    root : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  void QQmlSA::PassManagerPrivate::analyze(const Element &root)
    self.uglySide.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate7analyzeERKNS_7ElementE',
        self._valueOf(root),
    )

  @overload(
      WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.SourceLocation'],
  )
  def analyzeWrite(
      self,
      element: QQmlSA.Element,
      propertyName: str,
      value: QQmlSA.Element,
      writeScope: QQmlSA.Element,
      location: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::PassManagerPrivate::analyzeWrite(const
    QQmlSA::Element &element, const QString &propertyName, const
    QQmlSA::Element &value, const QQmlSA::Element &writeScope, const
    QQmlSA::SourceLocation &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#analyzeWrite

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    writeScope : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::PassManagerPrivate::analyzeWrite(const QQmlSA::Element
    #      &element, const QString &propertyName, const QQmlSA::Element
    #      &value, const QQmlSA::Element &writeScope, const
    #      QQmlSA::SourceLocation &location)
    self.uglySide.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate12analyzeWriteERKNS_7ElementER'
        'K7QStringS3_S3_RKNS_14SourceLocationE',
        self._valueOf(element), propertyName, self._valueOf(value),
        self._valueOf(writeScope), self._valueOf(location),
    )

  @overload(
      WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.SourceLocation'],
  )
  def analyzeRead(
      self,
      element: QQmlSA.Element,
      propertyName: str,
      readScope: QQmlSA.Element,
      location: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::PassManagerPrivate::analyzeRead(const
    QQmlSA::Element &element, const QString &propertyName, const
    QQmlSA::Element &readScope, const QQmlSA::SourceLocation &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#analyzeRead

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    readScope : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::PassManagerPrivate::analyzeRead(const QQmlSA::Element
    #      &element, const QString &propertyName, const QQmlSA::Element
    #      &readScope, const QQmlSA::SourceLocation &location)
    self.uglySide.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate11analyzeReadERKNS_7ElementERK'
        '7QStringS3_RKNS_14SourceLocationE',
        self._valueOf(element), propertyName, self._valueOf(readScope),
        self._valueOf(location),
    )

  @overload(
      WAIT['QQmlSA.Element'], str, WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.SourceLocation'],
  )
  def analyzeCall(
      self,
      element: QQmlSA.Element,
      propertyName: str,
      readScope: QQmlSA.Element,
      location: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::PassManagerPrivate::analyzeCall(const
    QQmlSA::Element &element, const QString &propertyName, const
    QQmlSA::Element &readScope, const QQmlSA::SourceLocation &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#analyzeCall

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    readScope : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::PassManagerPrivate::analyzeCall(const QQmlSA::Element
    #      &element, const QString &propertyName, const QQmlSA::Element
    #      &readScope, const QQmlSA::SourceLocation &location)
    self.uglySide.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate11analyzeCallERKNS_7ElementERK'
        '7QStringS3_RKNS_14SourceLocationE',
        self._valueOf(element), propertyName, self._valueOf(readScope),
        self._valueOf(location),
    )

  @overload(
      WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'],
      WAIT['QQmlSA.SourceLocation'],
  )
  def analyzeBinding(
      self,
      element: QQmlSA.Element,
      value: QQmlSA.Element,
      location: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::PassManagerPrivate::analyzeBinding(const
    QQmlSA::Element &element, const QQmlSA::Element &value, const
    QQmlSA::SourceLocation &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html#analyzeBinding

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    value : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::PassManagerPrivate::analyzeBinding(const QQmlSA::Element
    #      &element, const QQmlSA::Element &value, const
    #      QQmlSA::SourceLocation &location)
    self.uglySide.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate14analyzeBindingERKNS_7Element'
        'ES3_RKNS_14SourceLocationE',
        self._valueOf(element), self._valueOf(value),
        self._valueOf(location),
    )

  @overload(WAIT['QQmlSA.Element'])
  @overload(WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'])
  @overload(WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'], str)
  @overload(WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'], str, bool)
  def addBindingSourceLocations(
      self,
      element: QQmlSA.Element,
      scope: Optional[QQmlSA.Element] = None,
      prefix: str = '',
      isAttached: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlSA::PassManagerPrivate::addBindingSourceLocations(const
    QQmlSA::Element &element, const QQmlSA::Element &scope, const QString
    prefix, bool isAttached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanagerprivate.html

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    scope : Optional[QQmlSA.Element]
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own. May be left out, as in Qt: a new 'QQmlSA.Element()' is
      then passed on.

    prefix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    isAttached : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQmlSA::PassManagerPrivate::addBindingSourceLocations(const
    #      QQmlSA::Element &element, const QQmlSA::Element &scope, const
    #      QString prefix, bool isAttached)
    if scope is None:
      scope = QQmlSA.Element()
    self.uglySide.call(
        'ritual_ZN6QQmlSA18PassManagerPrivate25addBindingSourceLocationsERK'
        'NS_7ElementES3_7QStringb',
        self._valueOf(element), self._valueOf(scope), prefix, isAttached,
    )

  @staticmethod
  def findPropertyUsePasses(*__, **_) -> Never:
    """
    Qt's 'QSet<PropertyPass *>
    QQmlSA::PassManagerPrivate::findPropertyUsePasses(const QQmlSA::Element
    &element, const QString &propertyName)': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManagerPrivate.findPropertyUsePasses' has no cute "
        "function yet. Qt's 'QSet<PropertyPass *> "
        "QQmlSA::PassManagerPrivate::findPropertyUsePasses(const "
        "QQmlSA::Element &element, const QString &propertyName)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def hasImportedModule(*__, **_) -> Never:
    """
    Qt's 'bool QQmlSA::PassManagerPrivate::hasImportedModule(QAnyStringView
    name) const': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManagerPrivate.hasImportedModule' has no cute function "
        "yet. Qt's 'bool "
        "QQmlSA::PassManagerPrivate::hasImportedModule(QAnyStringView name) "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def registerElementPass(*__, **_) -> Never:
    """
    Qt's 'void QQmlSA::PassManagerPrivate::registerElementPass(std::
    unique_ptr<ElementPass> pass)': the compiler refuses its ritual as it
    would be written here: call to deleted constructor of
    'std::unique_ptr<ElementPass>'.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManagerPrivate.registerElementPass' has no cute "
        "function yet. Qt's 'void "
        "QQmlSA::PassManagerPrivate::registerElementPass(std::unique_ptr<Ele"
        "mentPass> pass)': the compiler refuses its ritual as it would be "
        "written here: call to deleted constructor of "
        "'std::unique_ptr<ElementPass>'.")

  @staticmethod
  def registerPropertyPass(*__, **_) -> Never:
    """
    Qt's 'bool QQmlSA::PassManagerPrivate::registerPropertyPass(std::
    shared_ptr<PropertyPass> pass, QAnyStringView moduleName, QAnyStringView
    typeName, QAnyStringView propertyName, bool allowInheritance)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManagerPrivate.registerPropertyPass' has no cute "
        "function yet. Qt's 'bool "
        "QQmlSA::PassManagerPrivate::registerPropertyPass(std::shared_ptr<Pr"
        "opertyPass> pass, QAnyStringView moduleName, QAnyStringView "
        "typeName, QAnyStringView propertyName, bool allowInheritance)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def registerPropertyPassOnBuiltinType(*__, **_) -> Never:
    """
    Qt's 'bool
    QQmlSA::PassManagerPrivate::registerPropertyPassOnBuiltinType(std::
    shared_ptr<PropertyPass> pass, QAnyStringView typeName, QAnyStringView
    propertyName, bool allowInheritance)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManagerPrivate.registerPropertyPassOnBuiltinType' has "
        "no cute function yet. Qt's 'bool "
        "QQmlSA::PassManagerPrivate::registerPropertyPassOnBuiltinType(std::"
        "shared_ptr<PropertyPass> pass, QAnyStringView typeName, "
        "QAnyStringView propertyName, bool allowInheritance)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def resolver(*__, **_) -> Never:
    """
    Qt's 'QQmlJSTypeResolver *QQmlSA::PassManagerPrivate::resolver(const
    QQmlSA::PassManager &a0)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManagerPrivate.resolver' has no cute function yet. "
        "Qt's 'QQmlJSTypeResolver "
        "*QQmlSA::PassManagerPrivate::resolver(const QQmlSA::PassManager "
        "&a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def visitor(*__, **_) -> Never:
    """
    Qt's 'QQmlJSImportVisitor *QQmlSA::PassManagerPrivate::visitor(const
    QQmlSA::PassManager &a0)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManagerPrivate.visitor' has no cute function yet. Qt's "
        "'QQmlJSImportVisitor *QQmlSA::PassManagerPrivate::visitor(const "
        "QQmlSA::PassManager &a0)': takes a type Python has no way to hand "
        "over yet.")
