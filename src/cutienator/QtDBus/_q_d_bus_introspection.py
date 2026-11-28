"""
QDBusIntrospection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusintrospection_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDBusIntrospection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusIntrospection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusIntrospection: a plain Python object standing in
  front of one C++ QDBusIntrospection.

  C++ hands a QDBusIntrospection around as a copy, so every C++
  QDBusIntrospection behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusIntrospection that has a ritual and that Python
  can call so far, 2 names in all: 'parseInterface', 'parseObject'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Interfaces QDBusIntrospection::parseInterfaces(const QString &xml,
    DiagnosticsReporter *reporter)': gives a type Python has no way to take
    yet.
  - Qt's 'QDBusIntrospection::~QDBusIntrospection()': the destructor: Python
    removes its C++ QDBusIntrospection by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QDBusIntrospection is created at the first use, not by
    'QDBusIntrospection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusIntrospection back gives a copy the ritual made
    for Python, in a new cute QDBusIntrospection.
  - Each name of Qt's QDBusIntrospection that has no cute function yet,
    'parseInterfaces', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QDBusIntrospection, each a class in here as
  #  in C++.

  class Annotation(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusIntrospection::Annotation: a plain Python
    object standing in front of one C++ QDBusIntrospection::Annotation.

    C++ hands a QDBusIntrospection::Annotation around as a copy, so every C++
    QDBusIntrospection::Annotation behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QDBusIntrospection::Annotation that has a ritual
    and that Python can call so far, 1 name in all: '__eq__'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::Annotation::~Annotation()': the destructor:
      Python removes its C++ QDBusIntrospection::Annotation by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QDBusIntrospection::Annotation is created at the first use, not
      by 'QDBusIntrospection::Annotation(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusIntrospection::Annotation back gives a copy
      the ritual made for Python, in a new cute
      QDBusIntrospection::Annotation.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::Annotation'

    #  Qt's '~QDBusIntrospection::Annotation()'. Naming it makes this a value
    #  class: Python owns every C++ QDBusIntrospection::Annotation behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QDBusIntrospection10AnnotationD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QDBusIntrospection.Annotation) -> bool:
      """
      Calls Qt's 'bool QDBusIntrospection::Annotation::operator==(const
      Annotation &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusintrospection-annotation.html#operator==

      Parameters
      ----------

      other : QDBusIntrospection.Annotation
        Passed on as a value: Qt reads the C++
        QDBusIntrospection::Annotation, which stays Python's own.
      """
      #  bool QDBusIntrospection::Annotation::operator==(const Annotation
      #      &other) const
      return self.uglySide.call(
          'ritual_ZNK18QDBusIntrospection10AnnotationeqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  class Argument(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusIntrospection::Argument: a plain Python object
    standing in front of one C++ QDBusIntrospection::Argument.

    C++ hands a QDBusIntrospection::Argument around as a copy, so every C++
    QDBusIntrospection::Argument behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QDBusIntrospection::Argument that has a ritual and
    that Python can call so far, 1 name in all: '__eq__'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::Argument::~Argument()': the destructor:
      Python removes its C++ QDBusIntrospection::Argument by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QDBusIntrospection::Argument is created at the first use, not
      by 'QDBusIntrospection::Argument(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusIntrospection::Argument back gives a copy the
      ritual made for Python, in a new cute QDBusIntrospection::Argument.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::Argument'

    #  Qt's '~QDBusIntrospection::Argument()'. Naming it makes this a value
    #  class: Python owns every C++ QDBusIntrospection::Argument behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QDBusIntrospection8ArgumentD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QDBusIntrospection.Argument) -> bool:
      """
      Calls Qt's 'bool QDBusIntrospection::Argument::operator==(const
      Argument &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusintrospection-argument.html#operator==

      Parameters
      ----------

      other : QDBusIntrospection.Argument
        Passed on as a value: Qt reads the C++ QDBusIntrospection::Argument,
        which stays Python's own.
      """
      #  bool QDBusIntrospection::Argument::operator==(const Argument &other)
      #      const
      return self.uglySide.call(
          'ritual_ZNK18QDBusIntrospection8ArgumenteqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  class DiagnosticsReporter(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusIntrospection::DiagnosticsReporter: a plain
    Python object standing in front of one C++
    QDBusIntrospection::DiagnosticsReporter.

    What exists
    -----------

    No function of Qt's QDBusIntrospection::DiagnosticsReporter yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::DiagnosticsReporter::~DiagnosticsReporter()':
      the destructor: Python never removes a C++
      QDBusIntrospection::DiagnosticsReporter.

    What has no ritual
    ------------------

    7 of the 8 functions Qt declares: 4 forbidden; 2 takes any number of
    arguments; 1 the class is abstract, so C++ cannot make one, and the C++
    class of ours does not fill in every function it leaves open.

    What to expect
    --------------

    - The C++ QDBusIntrospection::DiagnosticsReporter is created at the first
      use, not by 'QDBusIntrospection::DiagnosticsReporter(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QDBusIntrospection::DiagnosticsReporter.
    - Each name of Qt's QDBusIntrospection::DiagnosticsReporter that has no
      cute function yet, '__init__', 'error', 'warning', holds a function
      that raises 'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::DiagnosticsReporter'

    #  The functions Qt calls itself that
    #  QDBusIntrospection::DiagnosticsReporter is the first to declare and
    #  that cannot be handed to Python yet, each as Qt declares it. A class
    #  of a program that writes one of them anew is refused, since Qt would
    #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
    __virtual_left_out__ = {
        'warning': (
            'void QDBusIntrospection::DiagnosticsReporter::warning(const '
            'SourceLocation &, const char *, ...)',
        ),
        'error': (
            'void QDBusIntrospection::DiagnosticsReporter::error(const '
            'SourceLocation &, const char *, ...)',
        ),
    }

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QDBusIntrospection::DiagnosticsReporter::DiagnosticsReporter()':
      the class is abstract, so C++ cannot make one, and the C++ class of
      ours does not fill in every function it leaves open.
      """
      raise NotImplementedError(
          "'QDBusIntrospection.DiagnosticsReporter.__init__' has no cute "
          "function yet. Qt's "
          "'QDBusIntrospection::DiagnosticsReporter::DiagnosticsReporter()':"
          " the class is abstract, so C++ cannot make one, and the C++ "
          "class of ours does not fill in every function it leaves open.")

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

    @staticmethod
    def error(*__, **_) -> Never:
      """
      Qt's 'void QDBusIntrospection::DiagnosticsReporter::error(const
      SourceLocation &location, const char *msg)': takes any number of
      arguments.
      """
      raise NotImplementedError(
          "'QDBusIntrospection.DiagnosticsReporter.error' has no cute "
          "function yet. Qt's 'void "
          "QDBusIntrospection::DiagnosticsReporter::error(const "
          "SourceLocation &location, const char *msg)': takes any number of "
          "arguments.")

    @staticmethod
    def warning(*__, **_) -> Never:
      """
      Qt's 'void QDBusIntrospection::DiagnosticsReporter::warning(const
      SourceLocation &location, const char *msg)': takes any number of
      arguments.
      """
      raise NotImplementedError(
          "'QDBusIntrospection.DiagnosticsReporter.warning' has no cute "
          "function yet. Qt's 'void "
          "QDBusIntrospection::DiagnosticsReporter::warning(const "
          "SourceLocation &location, const char *msg)': takes any number of "
          "arguments.")

  class Interface(QSharedData):
    """
    The cute side of Qt's QDBusIntrospection::Interface: a plain Python
    object standing in front of one C++ QDBusIntrospection::Interface.

    It is built on the cute 'QSharedData', as Qt's
    QDBusIntrospection::Interface is built on Qt's QSharedData, and has
    everything that class has.

    C++ hands a QDBusIntrospection::Interface around as a copy, so every C++
    QDBusIntrospection::Interface behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QDBusIntrospection::Interface that has a ritual
    and that Python can call so far, 1 name in all: '__eq__'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::Interface::~Interface()': the destructor:
      Python removes its C++ QDBusIntrospection::Interface by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QDBusIntrospection::Interface is created at the first use, not
      by 'QDBusIntrospection::Interface(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusIntrospection::Interface back gives a copy the
      ritual made for Python, in a new cute QDBusIntrospection::Interface.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::Interface'

    #  Qt's '~QDBusIntrospection::Interface()'. Naming it makes this a value
    #  class: Python owns every C++ QDBusIntrospection::Interface behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QDBusIntrospection9InterfaceD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QDBusIntrospection.Interface) -> bool:
      """
      Calls Qt's 'bool QDBusIntrospection::Interface::operator==(const
      Interface &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusintrospection-interface.html#operator==

      Parameters
      ----------

      other : QDBusIntrospection.Interface
        Passed on as a value: Qt reads the C++ QDBusIntrospection::Interface,
        which stays Python's own.
      """
      #  bool QDBusIntrospection::Interface::operator==(const Interface
      #      &other) const
      return self.uglySide.call(
          'ritual_ZNK18QDBusIntrospection9InterfaceeqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  class Method(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusIntrospection::Method: a plain Python object
    standing in front of one C++ QDBusIntrospection::Method.

    C++ hands a QDBusIntrospection::Method around as a copy, so every C++
    QDBusIntrospection::Method behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QDBusIntrospection::Method that has a ritual and
    that Python can call so far, 1 name in all: '__eq__'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::Method::~Method()': the destructor: Python
      removes its C++ QDBusIntrospection::Method by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QDBusIntrospection::Method is created at the first use, not by
      'QDBusIntrospection::Method(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusIntrospection::Method back gives a copy the
      ritual made for Python, in a new cute QDBusIntrospection::Method.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::Method'

    #  Qt's '~QDBusIntrospection::Method()'. Naming it makes this a value
    #  class: Python owns every C++ QDBusIntrospection::Method behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QDBusIntrospection6MethodD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QDBusIntrospection.Method) -> bool:
      """
      Calls Qt's 'bool QDBusIntrospection::Method::operator==(const Method
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusintrospection-method.html#operator==

      Parameters
      ----------

      other : QDBusIntrospection.Method
        Passed on as a value: Qt reads the C++ QDBusIntrospection::Method,
        which stays Python's own.
      """
      #  bool QDBusIntrospection::Method::operator==(const Method &other)
      #      const
      return self.uglySide.call(
          'ritual_ZNK18QDBusIntrospection6MethodeqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  class Object(QSharedData):
    """
    The cute side of Qt's QDBusIntrospection::Object: a plain Python object
    standing in front of one C++ QDBusIntrospection::Object.

    It is built on the cute 'QSharedData', as Qt's QDBusIntrospection::Object
    is built on Qt's QSharedData, and has everything that class has.

    C++ hands a QDBusIntrospection::Object around as a copy, so every C++
    QDBusIntrospection::Object behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QDBusIntrospection::Object yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::Object::~Object()': the destructor: Python
      removes its C++ QDBusIntrospection::Object by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QDBusIntrospection::Object is created at the first use, not by
      'QDBusIntrospection::Object(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusIntrospection::Object back gives a copy the
      ritual made for Python, in a new cute QDBusIntrospection::Object.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::Object'

    #  Qt's '~QDBusIntrospection::Object()'. Naming it makes this a value
    #  class: Python owns every C++ QDBusIntrospection::Object behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QDBusIntrospection6ObjectD1Ev'

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

  class Property(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusIntrospection::Property: a plain Python object
    standing in front of one C++ QDBusIntrospection::Property.

    C++ hands a QDBusIntrospection::Property around as a copy, so every C++
    QDBusIntrospection::Property behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QDBusIntrospection::Property that has a ritual and
    that Python can call so far, 1 name in all: '__eq__'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::Property::~Property()': the destructor:
      Python removes its C++ QDBusIntrospection::Property by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QDBusIntrospection::Property is created at the first use, not
      by 'QDBusIntrospection::Property(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusIntrospection::Property back gives a copy the
      ritual made for Python, in a new cute QDBusIntrospection::Property.
    """

    #  The enums Qt writes inside QDBusIntrospection::Property, each a class
    #  in here as in C++, and the names Qt has for the combinations of its
    #  flags enums.

    class Access(CuteNum):
      """
      The enum 'QDBusIntrospection::Property::Access' of Qt, with the 3 names
      Qt gives in it.
      """

      Read = Kee[int](0)
      Write = Kee[int](1)
      ReadWrite = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::Property'

    #  Qt's '~QDBusIntrospection::Property()'. Naming it makes this a value
    #  class: Python owns every C++ QDBusIntrospection::Property behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QDBusIntrospection8PropertyD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QDBusIntrospection.Property) -> bool:
      """
      Calls Qt's 'bool QDBusIntrospection::Property::operator==(const
      Property &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusintrospection-property.html#operator==

      Parameters
      ----------

      other : QDBusIntrospection.Property
        Passed on as a value: Qt reads the C++ QDBusIntrospection::Property,
        which stays Python's own.
      """
      #  bool QDBusIntrospection::Property::operator==(const Property &other)
      #      const
      return self.uglySide.call(
          'ritual_ZNK18QDBusIntrospection8PropertyeqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  class Signal(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusIntrospection::Signal: a plain Python object
    standing in front of one C++ QDBusIntrospection::Signal.

    C++ hands a QDBusIntrospection::Signal around as a copy, so every C++
    QDBusIntrospection::Signal behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QDBusIntrospection::Signal that has a ritual and
    that Python can call so far, 1 name in all: '__eq__'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::Signal::~Signal()': the destructor: Python
      removes its C++ QDBusIntrospection::Signal by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QDBusIntrospection::Signal is created at the first use, not by
      'QDBusIntrospection::Signal(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusIntrospection::Signal back gives a copy the
      ritual made for Python, in a new cute QDBusIntrospection::Signal.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::Signal'

    #  Qt's '~QDBusIntrospection::Signal()'. Naming it makes this a value
    #  class: Python owns every C++ QDBusIntrospection::Signal behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QDBusIntrospection6SignalD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QDBusIntrospection.Signal) -> bool:
      """
      Calls Qt's 'bool QDBusIntrospection::Signal::operator==(const Signal
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdbusintrospection-signal.html#operator==

      Parameters
      ----------

      other : QDBusIntrospection.Signal
        Passed on as a value: Qt reads the C++ QDBusIntrospection::Signal,
        which stays Python's own.
      """
      #  bool QDBusIntrospection::Signal::operator==(const Signal &other)
      #      const
      return self.uglySide.call(
          'ritual_ZNK18QDBusIntrospection6SignaleqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

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

  class SourceLocation(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDBusIntrospection::SourceLocation: a plain Python
    object standing in front of one C++ QDBusIntrospection::SourceLocation.

    C++ hands a QDBusIntrospection::SourceLocation around as a copy, so every
    C++ QDBusIntrospection::SourceLocation behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QDBusIntrospection::SourceLocation yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDBusIntrospection::SourceLocation::~SourceLocation()': the
      destructor: Python removes its C++ QDBusIntrospection::SourceLocation
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QDBusIntrospection::SourceLocation is created at the first use,
      not by 'QDBusIntrospection::SourceLocation(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDBusIntrospection::SourceLocation back gives a
      copy the ritual made for Python, in a new cute
      QDBusIntrospection::SourceLocation.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDBusIntrospection::SourceLocation'

    #  Qt's '~QDBusIntrospection::SourceLocation()'. Naming it makes this a
    #  value class: Python owns every C++ QDBusIntrospection::SourceLocation
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QDBusIntrospection14SourceLocationD1Ev'

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

  @staticmethod
  @overload(str)
  @overload(str, DiagnosticsReporter)
  @overload(str, NoneType)
  def parseInterface(
      xml: str,
      reporter: Optional[DiagnosticsReporter] = None,
  ) -> Interface:
    """
    Calls Qt's 'Interface QDBusIntrospection::parseInterface(const QString
    &xml, DiagnosticsReporter *reporter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusintrospection.html#parseInterface

    Parameters
    ----------

    xml : str
      Passed on as it is: a QString is made of it for the call.

    reporter : Optional[DiagnosticsReporter]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Interface
      A new cute QDBusIntrospection::Interface around the copy Qt gave back.
      Python owns it.
    """
    #  Interface QDBusIntrospection::parseInterface(const QString &xml,
    #      DiagnosticsReporter *reporter)
    address = Rituals.call(
        'ritual_ZN18QDBusIntrospection14parseInterfaceERK7QStringPNS_19Diag'
        'nosticsReporterE',
        xml, CuteMixin._addressOf(reporter),
    )
    return QDBusIntrospection.Interface._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, str)
  @overload(str, str, str)
  @overload(str, str, str, DiagnosticsReporter)
  @overload(str, str, str, NoneType)
  def parseObject(
      xml: str,
      service: str = '',
      path: str = '',
      reporter: Optional[DiagnosticsReporter] = None,
  ) -> Object:
    """
    Calls Qt's 'Object QDBusIntrospection::parseObject(const QString &xml,
    const QString &service, const QString &path, DiagnosticsReporter
    *reporter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusintrospection.html#parseObject

    Parameters
    ----------

    xml : str
      Passed on as it is: a QString is made of it for the call.

    service : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    path : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    reporter : Optional[DiagnosticsReporter]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Object
      A new cute QDBusIntrospection::Object around the copy Qt gave back.
      Python owns it.
    """
    #  Object QDBusIntrospection::parseObject(const QString &xml, const
    #      QString &service, const QString &path, DiagnosticsReporter
    #      *reporter)
    address = Rituals.call(
        'ritual_ZN18QDBusIntrospection11parseObjectERK7QStringS2_S2_PNS_19D'
        'iagnosticsReporterE',
        xml, service, path, CuteMixin._addressOf(reporter),
    )
    return QDBusIntrospection.Object._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusIntrospection'

  #  Qt's '~QDBusIntrospection()'. Naming it makes this a value class: Python
  #  owns every C++ QDBusIntrospection behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QDBusIntrospectionD1Ev'

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

  @staticmethod
  def parseInterfaces(*__, **_) -> Never:
    """
    Qt's 'Interfaces QDBusIntrospection::parseInterfaces(const QString &xml,
    DiagnosticsReporter *reporter)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QDBusIntrospection.parseInterfaces' has no cute function yet. "
        "Qt's 'Interfaces QDBusIntrospection::parseInterfaces(const QString "
        "&xml, DiagnosticsReporter *reporter)': gives a type Python has no "
        "way to take yet.")
