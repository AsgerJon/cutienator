"""
Qt3DRender::QShaderNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qshadernode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QShaderNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QUuid, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUuid = WAIT['QUuid']
  QVariant = WAIT['QVariant']


class QShaderNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QShaderNode: a plain Python object
  standing in front of one C++ Qt3DRender::QShaderNode.

  C++ hands a Qt3DRender::QShaderNode around as a copy, so every C++
  Qt3DRender::QShaderNode behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QShaderNode that has a ritual and that
  Python can call so far, 14 names in all: 'type', 'uuid', 'setUuid',
  'layers', 'setLayers', 'addPort', 'removePort', 'parameterNames',
  'parameter', 'setParameter', 'clearParameter', 'addRule', 'removeRule',
  'rule'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QShaderNodePort> Qt3DRender::QShaderNode::ports() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QShaderFormat> Qt3DRender::QShaderNode::availableFormats()
    const': gives a type Python has no way to take yet.
  - Qt's 'Qt3DRender::QShaderNode::~QShaderNode()': the destructor: Python
    removes its C++ Qt3DRender::QShaderNode by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ Qt3DRender::QShaderNode is created at the first use, not by
    'Qt3DRender::QShaderNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QShaderNode back gives a copy the ritual
    made for Python, in a new cute Qt3DRender::QShaderNode.
  - Each name of Qt's Qt3DRender::QShaderNode that has no cute function yet,
    'availableFormats', 'ports', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QShaderNode, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'Qt3DRender::QShaderNode::Type' of Qt, with the 4 names Qt gives
    in it.
    """

    Invalid = Kee[int](0)
    Input = Kee[int](1)
    Output = Kee[int](2)
    Function = Kee[int](3)

  #  The classes Qt writes inside Qt3DRender::QShaderNode, each a class in
  #  here as in C++.

  class Rule(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DRender::QShaderNode::Rule: a plain Python
    object standing in front of one C++ Qt3DRender::QShaderNode::Rule.

    C++ hands a Qt3DRender::QShaderNode::Rule around as a copy, so every C++
    Qt3DRender::QShaderNode::Rule behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's Qt3DRender::QShaderNode::Rule yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Qt3DRender::QShaderNode::Rule::~Rule()': the destructor: Python
      removes its C++ Qt3DRender::QShaderNode::Rule by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ Qt3DRender::QShaderNode::Rule is created at the first use, not
      by 'Qt3DRender::QShaderNode::Rule(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DRender::QShaderNode::Rule back gives a copy the
      ritual made for Python, in a new cute Qt3DRender::QShaderNode::Rule.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DRender::QShaderNode::Rule'

    #  Qt's '~Qt3DRender::QShaderNode::Rule()'. Naming it makes this a value
    #  class: Python owns every C++ Qt3DRender::QShaderNode::Rule behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10Qt3DRender11QShaderNode4RuleD1Ev'

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

    @overload(QByteArray, QList[QByteArray])
    def __init__(
        self,
        substitution: QByteArray,
        headerSnippets: QList[QByteArray],
    ) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DRender::QShaderNode::Rule::Rule(const QByteArray &substitution,
      const QByteArrayList &headerSnippets)', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3drender-qshadernode-rule.html#Rule

      Parameters
      ----------

      substitution : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.

      headerSnippets : QList[QByteArray]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  Qt3DRender::QShaderNode::Rule::Rule(const QByteArray &substitution,
      #      const QByteArrayList &headerSnippets)
      self._noteCreation(QShaderNode.Rule, lambda: Rituals.call(
          'ritual_ZN10Qt3DRender11QShaderNode4RuleC1ERK10QByteArrayRK5QList'
          'IS2_E',
          self._valueOf(substitution), self._valueOf(headerSnippets),
      ))

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
  __qt_class__ = 'Qt3DRender::QShaderNode'

  #  Qt's '~Qt3DRender::QShaderNode()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DRender::QShaderNode behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender11QShaderNodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type Qt3DRender::QShaderNode::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshadernode.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type Qt3DRender::QShaderNode::type() const
    return QShaderNode.Type(self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QShaderNode4typeEv',
    ))

  def uuid(self) -> QUuid:
    """
    Calls Qt's 'QUuid Qt3DRender::QShaderNode::uuid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshadernode.html#uuid

    Returns
    -------

    QUuid
      A new cute QUuid around the copy Qt gave back. Python owns it.
    """
    #  QUuid Qt3DRender::QShaderNode::uuid() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QShaderNode4uuidEv',
    )
    from ..QtCore import QUuid
    return QUuid._cuteOwning(address)

  def layers(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QShaderNode::layers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshadernode.html#layers

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QShaderNode::layers() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QShaderNode6layersEv',
    )
    return QStringList._cuteOwning(address)

  def parameterNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QShaderNode::parameterNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#parameterNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QShaderNode::parameterNames() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QShaderNode14parameterNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def parameter(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DRender::QShaderNode::parameter(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#parameter

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::QShaderNode::parameter(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QShaderNode9parameterERK7QString', name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(WAIT['Qt3DRender.QShaderFormat'])
  def rule(self, format: Qt3DRender.QShaderFormat) -> Rule:
    """
    Calls Qt's 'Rule Qt3DRender::QShaderNode::rule(const QShaderFormat
    &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qshadernode.html#rule

    Parameters
    ----------

    format : Qt3DRender.QShaderFormat
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderFormat, which
      stays Python's own.

    Returns
    -------

    Rule
      A new cute Qt3DRender::QShaderNode::Rule around the copy Qt gave back.
      Python owns it.
    """
    #  Rule Qt3DRender::QShaderNode::rule(const QShaderFormat &format) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QShaderNode4ruleERKNS_13QShaderFormatE',
        self._valueOf(format),
    )
    return Qt3DRender.QShaderNode.Rule._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUuid)
  def setUuid(self, uuid: QUuid) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNode::setUuid(const QUuid &uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#setUuid

    Parameters
    ----------

    uuid : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
    """
    #  void Qt3DRender::QShaderNode::setUuid(const QUuid &uuid)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QShaderNode7setUuidERK5QUuid',
        self._valueOf(uuid),
    )

  @overload(QStringList)
  def setLayers(self, layers: QStringList) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNode::setLayers(const QStringList
    &layers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#setLayers

    Parameters
    ----------

    layers : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::QShaderNode::setLayers(const QStringList &layers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QShaderNode9setLayersERK5QListI7QStringE',
        self._valueOf(layers),
    )

  @overload(str, QVariant)
  def setParameter(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNode::setParameter(const QString
    &name, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#setParameter

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QShaderNode::setParameter(const QString &name, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QShaderNode12setParameterERK7QStringRK8QVar'
        'iant',
        name, self._valueOf(value),
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

  @overload(WAIT['Qt3DRender.QShaderNodePort'])
  def addPort(self, port: Qt3DRender.QShaderNodePort) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNode::addPort(const QShaderNodePort
    &port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#addPort

    Parameters
    ----------

    port : Qt3DRender.QShaderNodePort
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderNodePort,
      which stays Python's own.
    """
    #  void Qt3DRender::QShaderNode::addPort(const QShaderNodePort &port)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QShaderNode7addPortERKNS_15QShaderNodePortE',
        self._valueOf(port),
    )

  @overload(WAIT['Qt3DRender.QShaderNodePort'])
  def removePort(self, port: Qt3DRender.QShaderNodePort) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNode::removePort(const
    QShaderNodePort &port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#removePort

    Parameters
    ----------

    port : Qt3DRender.QShaderNodePort
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderNodePort,
      which stays Python's own.
    """
    #  void Qt3DRender::QShaderNode::removePort(const QShaderNodePort &port)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QShaderNode10removePortERKNS_15QShaderNodeP'
        'ortE',
        self._valueOf(port),
    )

  @overload(str)
  def clearParameter(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNode::clearParameter(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#clearParameter

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QShaderNode::clearParameter(const QString &name)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QShaderNode14clearParameterERK7QString',
        name,
    )

  @overload(WAIT['Qt3DRender.QShaderFormat'], Rule)
  def addRule(self, format: Qt3DRender.QShaderFormat, rule: Rule) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNode::addRule(const QShaderFormat
    &format, const Rule &rule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#addRule

    Parameters
    ----------

    format : Qt3DRender.QShaderFormat
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderFormat, which
      stays Python's own.

    rule : Rule
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderNode::Rule,
      which stays Python's own.
    """
    #  void Qt3DRender::QShaderNode::addRule(const QShaderFormat &format,
    #      const Rule &rule)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QShaderNode7addRuleERKNS_13QShaderFormatERK'
        'NS0_4RuleE',
        self._valueOf(format), self._valueOf(rule),
    )

  @overload(WAIT['Qt3DRender.QShaderFormat'])
  def removeRule(self, format: Qt3DRender.QShaderFormat) -> None:
    """
    Calls Qt's 'void Qt3DRender::QShaderNode::removeRule(const QShaderFormat
    &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qshadernode.html#removeRule

    Parameters
    ----------

    format : Qt3DRender.QShaderFormat
      Passed on as a value: Qt reads the C++ Qt3DRender::QShaderFormat, which
      stays Python's own.
    """
    #  void Qt3DRender::QShaderNode::removeRule(const QShaderFormat &format)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QShaderNode10removeRuleERKNS_13QShaderForma'
        'tE',
        self._valueOf(format),
    )

  @staticmethod
  def availableFormats(*__, **_) -> Never:
    """
    Qt's 'QList<QShaderFormat> Qt3DRender::QShaderNode::availableFormats()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QShaderNode.availableFormats' has no cute function "
        "yet. Qt's 'QList<QShaderFormat> "
        "Qt3DRender::QShaderNode::availableFormats() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def ports(*__, **_) -> Never:
    """
    Qt's 'QList<QShaderNodePort> Qt3DRender::QShaderNode::ports() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QShaderNode.ports' has no cute function yet. Qt's "
        "'QList<QShaderNodePort> Qt3DRender::QShaderNode::ports() const': "
        "gives a type Python has no way to take yet.")
