"""
QSSGStageGeneratorBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenerator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGStageGeneratorBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QSSGShaderResourceMergeContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSSGShaderResourceMergeContext = WAIT['QSSGShaderResourceMergeContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGStageGeneratorBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGStageGeneratorBase: a plain Python object
  standing in front of one C++ QSSGStageGeneratorBase.

  C++ hands a QSSGStageGeneratorBase around as a copy, so every C++
  QSSGStageGeneratorBase behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGStageGeneratorBase that has a ritual and that
  Python can call so far, 21 names in all: 'addIncoming', 'addOutgoing',
  'addFlatIncoming', 'addFlatOutgoing', 'addUniform', 'addUniformArray',
  'addConstantBuffer', 'addConstantBufferParam', 'append',
  'addShaderPass2Marker', 'addShaderIncomingMap', 'addShaderUniformMap',
  'addShaderOutgoingMap', 'appendShaderCode', 'addInclude',
  'buildShaderSourcePass1', 'buildShaderSourcePass2', 'addFunction',
  'addDefinition', 'addTypeDeclaration', 'addPrefix'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSSGStageGeneratorBase::QSSGStageGeneratorBase(QSSGShaderGeneratorStage
    inStage)': names the enum 'QSSGShaderGeneratorStage', whose class cannot
    be named here.
  - Qt's 'QSSGStageGeneratorBase::~QSSGStageGeneratorBase()': the destructor:
    Python removes its C++ QSSGStageGeneratorBase by it, and has no other use
    for it.
  - Qt's 'void QSSGStageGeneratorBase::begin(QSSGShaderGeneratorStageFlags
    inEnabledStages)': names the enum 'QSSGShaderGeneratorStage', whose class
    cannot be named here.
  - Qt's 'QSSGStageGeneratorBase &QSSGStageGeneratorBase::operator<<(const
    QByteArray &data)': gives a type Python has no way to take yet.
  - Qt's 'QSSGShaderGeneratorStage QSSGStageGeneratorBase::stage() const':
    gives the enum 'QSSGShaderGeneratorStage', whose class cannot be named
    here.
  - Qt's 'void QSSGStageGeneratorBase::addShaderItemMap(ShaderItemType
    itemType, const TStrTableStrMap &itemMap, ShaderItemMapFlags flags)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGStageGeneratorBase::addShaderConstantBufferItemMap(const
    QByteArray &itemType, const TStrTableStrMap &cbMap,
    TConstantBufferParamArray cbParamsArray)': takes a type Python has no way
    to hand over yet.

  What to expect
  --------------

  - The C++ QSSGStageGeneratorBase is created at the first use, not by
    'QSSGStageGeneratorBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGStageGeneratorBase back gives a copy the ritual
    made for Python, in a new cute QSSGStageGeneratorBase.
  - Each name of Qt's QSSGStageGeneratorBase that has no cute function yet,
    '__init__', 'addShaderConstantBufferItemMap', 'addShaderItemMap',
    'begin', 'stage', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QSSGStageGeneratorBase, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ShaderItemMapFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QSSGStageGeneratorBase::ShaderItemMapFlag' of Qt, with
    the 1 names Qt gives in it. Qt names the type of its combinations
    'QSSGStageGeneratorBase::ShaderItemMapFlags'. C++ keeps these names
    inside the enum, so the class that holds the enum does not have them.
    """

    Flat = 0x1

  ShaderItemMapFlags = ShaderItemMapFlag

  class ShaderItemType(CuteNum, scoped=True):
    """
    The enum 'QSSGStageGeneratorBase::ShaderItemType' of Qt, with the 5 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    VertexInput = Kee[int](0)
    Input = Kee[int](1)
    Output = Kee[int](2)
    Uniform = Kee[int](3)
    Image = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGStageGeneratorBase'

  #  A C++ QSSGStageGeneratorBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSSGStageGeneratorBase'

  #  The functions Qt calls itself that QSSGStageGeneratorBase is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'begin': (
          'void '
          'QSSGStageGeneratorBase::begin(QSSGShaderGeneratorStageFlags)',
      ),
      'addShaderConstantBufferItemMap': (
          'void '
          'QSSGStageGeneratorBase::addShaderConstantBufferItemMap(const '
          'QByteArray &, const TStrTableStrMap &, '
          'TConstantBufferParamArray)',
      ),
  }

  #  The functions Qt calls itself that QSSGStageGeneratorBase is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'addIncoming': (
          ('_ZN22QSSGStageGeneratorBase11addIncomingERK10QByteArrayS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'addOutgoing': (
          ('_ZN22QSSGStageGeneratorBase11addOutgoingERK10QByteArrayS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'addFlatIncoming': (
          ('_ZN22QSSGStageGeneratorBase15addFlatIncomingERK10QByteArrayS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'addFlatOutgoing': (
          ('_ZN22QSSGStageGeneratorBase15addFlatOutgoingERK10QByteArrayS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'addUniform': (
          ('_ZN22QSSGStageGeneratorBase10addUniformERK10QByteArrayS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'addUniformArray': (
          ('_ZN22QSSGStageGeneratorBase15addUniformArrayERK10QByteArrayS2_j',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'addConstantBuffer': (
          ('_ZN22QSSGStageGeneratorBase17addConstantBufferERK10QByteArrayS2'
           '_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'addConstantBufferParam': (
          ('_ZN22QSSGStageGeneratorBase22addConstantBufferParamERK10QByteAr'
           'rayS2_S2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'append': (
          ('_ZN22QSSGStageGeneratorBase6appendERK10QByteArray',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
      'addShaderIncomingMap': (
          ('_ZN22QSSGStageGeneratorBase20addShaderIncomingMapEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addShaderUniformMap': (
          ('_ZN22QSSGStageGeneratorBase19addShaderUniformMapEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addShaderOutgoingMap': (
          ('_ZN22QSSGStageGeneratorBase20addShaderOutgoingMapEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Qt's '~QSSGStageGeneratorBase()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGStageGeneratorBase behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QSSGStageGeneratorBaseD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QSSGStageGeneratorBase::QSSGStageGeneratorBase(QSSGShaderGeneratorStage
    inStage)': names the enum 'QSSGShaderGeneratorStage', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QSSGStageGeneratorBase.__init__' has no cute function yet. Qt's "
        "'QSSGStageGeneratorBase::QSSGStageGeneratorBase(QSSGShaderGenerator"
        "Stage inStage)': names the enum 'QSSGShaderGeneratorStage', whose "
        "class cannot be named here.")

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

  @overload(QByteArray, QByteArray)
  def addIncoming(self, name: QByteArray, type: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addIncoming(const QByteArray
    &name, const QByteArray &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addIncoming

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addIncoming(const QByteArray &name, const
    #      QByteArray &type)
    ritual = (
        'ritual_ZN22QSSGStageGeneratorBase11addIncomingERK10QByteArrayS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase11addIncomingERK10QByteArra'
          'yS2_')
    self.uglySide.call(ritual, self._valueOf(name), self._valueOf(type))

  @overload(QByteArray, QByteArray)
  def addOutgoing(self, name: QByteArray, type: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addOutgoing(const QByteArray
    &name, const QByteArray &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addOutgoing

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addOutgoing(const QByteArray &name, const
    #      QByteArray &type)
    ritual = (
        'ritual_ZN22QSSGStageGeneratorBase11addOutgoingERK10QByteArrayS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase11addOutgoingERK10QByteArra'
          'yS2_')
    self.uglySide.call(ritual, self._valueOf(name), self._valueOf(type))

  @overload(QByteArray, QByteArray)
  def addFlatIncoming(self, name: QByteArray, type: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addFlatIncoming(const QByteArray
    &name, const QByteArray &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addFlatIncoming

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addFlatIncoming(const QByteArray &name,
    #      const QByteArray &type)
    ritual = (
        'ritual_ZN22QSSGStageGeneratorBase15addFlatIncomingERK10QByteArrayS'
        '2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase15addFlatIncomingERK10QByte'
          'ArrayS2_')
    self.uglySide.call(ritual, self._valueOf(name), self._valueOf(type))

  @overload(QByteArray, QByteArray)
  def addFlatOutgoing(self, name: QByteArray, type: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addFlatOutgoing(const QByteArray
    &name, const QByteArray &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addFlatOutgoing

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addFlatOutgoing(const QByteArray &name,
    #      const QByteArray &type)
    ritual = (
        'ritual_ZN22QSSGStageGeneratorBase15addFlatOutgoingERK10QByteArrayS'
        '2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase15addFlatOutgoingERK10QByte'
          'ArrayS2_')
    self.uglySide.call(ritual, self._valueOf(name), self._valueOf(type))

  @overload(QByteArray, QByteArray)
  def addUniform(self, name: QByteArray, type: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addUniform(const QByteArray
    &name, const QByteArray &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addUniform

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addUniform(const QByteArray &name, const
    #      QByteArray &type)
    ritual = (
        'ritual_ZN22QSSGStageGeneratorBase10addUniformERK10QByteArrayS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase10addUniformERK10QByteArray'
          'S2_')
    self.uglySide.call(ritual, self._valueOf(name), self._valueOf(type))

  @overload(QByteArray, QByteArray, int)
  def addUniformArray(
      self,
      name: QByteArray,
      type: QByteArray,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addUniformArray(const QByteArray
    &name, const QByteArray &type, quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addUniformArray

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    size : int
      Passed on as it is.
    """
    #  void QSSGStageGeneratorBase::addUniformArray(const QByteArray &name,
    #      const QByteArray &type, quint32 size)
    ritual = (
        'ritual_ZN22QSSGStageGeneratorBase15addUniformArrayERK10QByteArrayS'
        '2_j')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase15addUniformArrayERK10QByte'
          'ArrayS2_j')
    self.uglySide.call(
        ritual, self._valueOf(name), self._valueOf(type), size,
    )

  @overload(QByteArray, QByteArray)
  def addConstantBuffer(self, name: QByteArray, layout: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addConstantBuffer(const
    QByteArray &name, const QByteArray &layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addConstantBuffer

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    layout : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addConstantBuffer(const QByteArray &name,
    #      const QByteArray &layout)
    ritual = (
        'ritual_ZN22QSSGStageGeneratorBase17addConstantBufferERK10QByteArra'
        'yS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase17addConstantBufferERK10QBy'
          'teArrayS2_')
    self.uglySide.call(ritual, self._valueOf(name), self._valueOf(layout))

  @overload(QByteArray, QByteArray, QByteArray)
  def addConstantBufferParam(
      self,
      cbName: QByteArray,
      paramName: QByteArray,
      type: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addConstantBufferParam(const
    QByteArray &cbName, const QByteArray &paramName, const QByteArray
    &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addConstantBufferParam

    Parameters
    ----------

    cbName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    paramName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addConstantBufferParam(const QByteArray
    #      &cbName, const QByteArray &paramName, const QByteArray &type)
    ritual = (
        'ritual_ZN22QSSGStageGeneratorBase22addConstantBufferParamERK10QByt'
        'eArrayS2_S2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase22addConstantBufferParamERK'
          '10QByteArrayS2_S2_')
    self.uglySide.call(
        ritual,
        self._valueOf(cbName), self._valueOf(paramName), self._valueOf(type),
    )

  @overload(QByteArray)
  def append(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::append(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#append

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::append(const QByteArray &data)
    ritual = 'ritual_ZN22QSSGStageGeneratorBase6appendERK10QByteArray'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSSGStageGeneratorBase6appendERK10QByteArray'
    self.uglySide.call(ritual, self._valueOf(data))

  @overload(ShaderItemType)
  def addShaderPass2Marker(self, itemType: ShaderItemType) -> None:
    """
    Calls Qt's 'void
    QSSGStageGeneratorBase::addShaderPass2Marker(ShaderItemType itemType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addShaderPass2Marker

    Parameters
    ----------

    itemType : ShaderItemType
      Passed on as its number.
    """
    #  void QSSGStageGeneratorBase::addShaderPass2Marker(ShaderItemType
    #      itemType)
    self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase20addShaderPass2MarkerENS_14Shade'
        'rItemTypeE',
        itemType.value,
    )

  def addShaderIncomingMap(self) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addShaderIncomingMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addShaderIncomingMap
    """
    #  void QSSGStageGeneratorBase::addShaderIncomingMap()
    ritual = 'ritual_ZN22QSSGStageGeneratorBase20addShaderIncomingMapEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase20addShaderIncomingMapEv')
    self.uglySide.call(ritual)

  def addShaderUniformMap(self) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addShaderUniformMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addShaderUniformMap
    """
    #  void QSSGStageGeneratorBase::addShaderUniformMap()
    ritual = 'ritual_ZN22QSSGStageGeneratorBase19addShaderUniformMapEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QSSGStageGeneratorBase19addShaderUniformMapEv'
    self.uglySide.call(ritual)

  def addShaderOutgoingMap(self) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addShaderOutgoingMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addShaderOutgoingMap
    """
    #  void QSSGStageGeneratorBase::addShaderOutgoingMap()
    ritual = 'ritual_ZN22QSSGStageGeneratorBase20addShaderOutgoingMapEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QSSGStageGeneratorBase20addShaderOutgoingMapEv')
    self.uglySide.call(ritual)

  def appendShaderCode(self) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::appendShaderCode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#appendShaderCode
    """
    #  void QSSGStageGeneratorBase::appendShaderCode()
    self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase16appendShaderCodeEv',
    )

  @overload(QByteArray)
  def addInclude(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addInclude(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addInclude

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addInclude(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase10addIncludeERK10QByteArray',
        self._valueOf(name),
    )

  @overload(QSSGShaderResourceMergeContext)
  @overload(NoneType)
  def buildShaderSourcePass1(
      self,
      mergeContext: Optional[QSSGShaderResourceMergeContext],
  ) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::buildShaderSourcePass1(
    QSSGShaderResourceMergeContext *mergeContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#buildShaderSourcePass1

    Parameters
    ----------

    mergeContext : Optional[QSSGShaderResourceMergeContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSSGStageGeneratorBase::buildShaderSourcePass1(
    #      QSSGShaderResourceMergeContext *mergeContext)
    self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase22buildShaderSourcePass1EP30QSSGS'
        'haderResourceMergeContext',
        self._addressOf(mergeContext),
    )

  @overload(QSSGShaderResourceMergeContext)
  @overload(NoneType)
  def buildShaderSourcePass2(
      self,
      mergeContext: Optional[QSSGShaderResourceMergeContext],
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSSGStageGeneratorBase::buildShaderSourcePass2(
    QSSGShaderResourceMergeContext *mergeContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#buildShaderSourcePass2

    Parameters
    ----------

    mergeContext : Optional[QSSGShaderResourceMergeContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSSGStageGeneratorBase::buildShaderSourcePass2(
    #      QSSGShaderResourceMergeContext *mergeContext)
    address = self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase22buildShaderSourcePass2EP30QSSGS'
        'haderResourceMergeContext',
        self._addressOf(mergeContext),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray)
  def addFunction(self, functionName: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addFunction(const QByteArray
    &functionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addFunction

    Parameters
    ----------

    functionName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addFunction(const QByteArray
    #      &functionName)
    self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase11addFunctionERK10QByteArray',
        self._valueOf(functionName),
    )

  @overload(QByteArray, QByteArray)
  def addDefinition(self, name: QByteArray, value: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addDefinition(const QByteArray
    &name, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addDefinition

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addDefinition(const QByteArray &name,
    #      const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase13addDefinitionERK10QByteArrayS2_',
        self._valueOf(name), self._valueOf(value),
    )

  @overload(QByteArray, QByteArray)
  def addTypeDeclaration(
      self,
      typeName: QByteArray,
      snippet: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addTypeDeclaration(const
    QByteArray &typeName, const QByteArray &snippet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addTypeDeclaration

    Parameters
    ----------

    typeName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    snippet : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addTypeDeclaration(const QByteArray
    #      &typeName, const QByteArray &snippet)
    self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase18addTypeDeclarationERK10QByteArr'
        'ayS2_',
        self._valueOf(typeName), self._valueOf(snippet),
    )

  @overload(QByteArray)
  def addPrefix(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGStageGeneratorBase::addPrefix(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgstagegeneratorbase.html#addPrefix

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGStageGeneratorBase::addPrefix(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN22QSSGStageGeneratorBase9addPrefixERK10QByteArray',
        self._valueOf(data),
    )

  @staticmethod
  def addShaderConstantBufferItemMap(*__, **_) -> Never:
    """
    Qt's 'void QSSGStageGeneratorBase::addShaderConstantBufferItemMap(const
    QByteArray &itemType, const TStrTableStrMap &cbMap,
    TConstantBufferParamArray cbParamsArray)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGStageGeneratorBase.addShaderConstantBufferItemMap' has no "
        "cute function yet. Qt's 'void "
        "QSSGStageGeneratorBase::addShaderConstantBufferItemMap(const "
        "QByteArray &itemType, const TStrTableStrMap &cbMap, "
        "TConstantBufferParamArray cbParamsArray)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def addShaderItemMap(*__, **_) -> Never:
    """
    Qt's 'void QSSGStageGeneratorBase::addShaderItemMap(ShaderItemType
    itemType, const TStrTableStrMap &itemMap, ShaderItemMapFlags flags)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGStageGeneratorBase.addShaderItemMap' has no cute function "
        "yet. Qt's 'void "
        "QSSGStageGeneratorBase::addShaderItemMap(ShaderItemType itemType, "
        "const TStrTableStrMap &itemMap, ShaderItemMapFlags flags)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'void QSSGStageGeneratorBase::begin(QSSGShaderGeneratorStageFlags
    inEnabledStages)': names the enum 'QSSGShaderGeneratorStage', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGStageGeneratorBase.begin' has no cute function yet. Qt's "
        "'void QSSGStageGeneratorBase::begin(QSSGShaderGeneratorStageFlags "
        "inEnabledStages)': names the enum 'QSSGShaderGeneratorStage', "
        "whose class cannot be named here.")

  @staticmethod
  def stage(*__, **_) -> Never:
    """
    Qt's 'QSSGShaderGeneratorStage QSSGStageGeneratorBase::stage() const':
    gives the enum 'QSSGShaderGeneratorStage', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QSSGStageGeneratorBase.stage' has no cute function yet. Qt's "
        "'QSSGShaderGeneratorStage QSSGStageGeneratorBase::stage() const': "
        "gives the enum 'QSSGShaderGeneratorStage', whose class cannot be "
        "named here.")
