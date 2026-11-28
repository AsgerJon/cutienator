"""
QOpcUaContentFilterElement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuacontentfilterelement.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QOpcUaContentFilterElement(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaContentFilterElement: a plain Python object
  standing in front of one C++ QOpcUaContentFilterElement.

  C++ hands a QOpcUaContentFilterElement around as a copy, so every C++
  QOpcUaContentFilterElement behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaContentFilterElement that has a ritual and
  that Python can call so far, 6 names in all: 'filterOperator',
  'setFilterOperator', 'filterOperands', 'setFilterOperands', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaContentFilterElement
    &QOpcUaContentFilterElement::operator=(const QOpcUaContentFilterElement
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaContentFilterElement::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaContentFilterElement::~QOpcUaContentFilterElement()': the
    destructor: Python removes its C++ QOpcUaContentFilterElement by it, and
    has no other use for it.
  - Qt's 'QOpcUaContentFilterElement
    &QOpcUaContentFilterElement::operator<<(FilterOperator op)': gives a type
    Python has no way to take yet.
  - Qt's 'QOpcUaContentFilterElement
    &QOpcUaContentFilterElement::operator<<(const
    QOpcUaSimpleAttributeOperand &op)': gives a type Python has no way to
    take yet.
  - Qt's 'QOpcUaContentFilterElement
    &QOpcUaContentFilterElement::operator<<(const QOpcUaAttributeOperand
    &op)': gives a type Python has no way to take yet.
  - Qt's 'QOpcUaContentFilterElement
    &QOpcUaContentFilterElement::operator<<(const QOpcUaLiteralOperand &op)':
    gives a type Python has no way to take yet.
  - Qt's 'QOpcUaContentFilterElement
    &QOpcUaContentFilterElement::operator<<(const QOpcUaElementOperand &op)':
    gives a type Python has no way to take yet.
  - Qt's 'QList<QVariant> &QOpcUaContentFilterElement::filterOperandsRef()':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaContentFilterElement is created at the first use, not by
    'QOpcUaContentFilterElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaContentFilterElement back gives a copy the
    ritual made for Python, in a new cute QOpcUaContentFilterElement.
  - Each name of Qt's QOpcUaContentFilterElement that has no cute function
    yet, 'filterOperandsRef', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaContentFilterElement, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FilterOperator(CuteNum):
    """
    The enum 'QOpcUaContentFilterElement::FilterOperator' of Qt, with the 18
    names Qt gives in it.
    """

    Equals = Kee[int](0)
    IsNull = Kee[int](1)
    GreaterThan = Kee[int](2)
    LessThan = Kee[int](3)
    GreaterThanOrEqual = Kee[int](4)
    LessThanOrEqual = Kee[int](5)
    Like = Kee[int](6)
    Not = Kee[int](7)
    Between = Kee[int](8)
    InList = Kee[int](9)
    And = Kee[int](10)
    Or = Kee[int](11)
    Cast = Kee[int](12)
    InView = Kee[int](13)
    OfType = Kee[int](14)
    RelatedTo = Kee[int](15)
    BitwiseAnd = Kee[int](16)
    BitwiseOr = Kee[int](17)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaContentFilterElement'

  #  Qt's '~QOpcUaContentFilterElement()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaContentFilterElement behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QOpcUaContentFilterElementD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def filterOperator(self) -> FilterOperator:
    """
    Calls Qt's 'QOpcUaContentFilterElement::FilterOperator
    QOpcUaContentFilterElement::filterOperator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelement.html#filterOperator

    Returns
    -------

    FilterOperator
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FilterOperator(number)'
      gives.
    """
    #  QOpcUaContentFilterElement::FilterOperator
    #      QOpcUaContentFilterElement::filterOperator() const
    return QOpcUaContentFilterElement.FilterOperator(self.uglySide.call(
        'ritual_ZNK26QOpcUaContentFilterElement14filterOperatorEv',
    ))

  def filterOperands(self) -> QList[QVariant]:
    """
    Calls Qt's 'QList<QVariant> QOpcUaContentFilterElement::filterOperands()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelement.html#filterOperands

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVariant> QOpcUaContentFilterElement::filterOperands() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaContentFilterElement14filterOperandsEv',
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FilterOperator)
  def setFilterOperator(self, filterOperator: FilterOperator) -> None:
    """
    Calls Qt's 'void QOpcUaContentFilterElement::setFilterOperator(
    QOpcUaContentFilterElement::FilterOperator filterOperator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelement.html#setFilterOperator

    Parameters
    ----------

    filterOperator : FilterOperator
      Passed on as its number.
    """
    #  void QOpcUaContentFilterElement::setFilterOperator(
    #      QOpcUaContentFilterElement::FilterOperator filterOperator)
    self.uglySide.call(
        'ritual_ZN26QOpcUaContentFilterElement17setFilterOperatorENS_14Filt'
        'erOperatorE',
        filterOperator.value,
    )

  @overload(QList[QVariant])
  def setFilterOperands(self, filterOperands: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QOpcUaContentFilterElement::setFilterOperands(const
    QList<QVariant> &filterOperands)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelement.html#setFilterOperands

    Parameters
    ----------

    filterOperands : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaContentFilterElement::setFilterOperands(const
    #      QList<QVariant> &filterOperands)
    self.uglySide.call(
        'ritual_ZN26QOpcUaContentFilterElement17setFilterOperandsERK5QListI'
        '8QVariantE',
        self._valueOf(filterOperands),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaContentFilterElement) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaContentFilterElement &lhs, const
    QOpcUaContentFilterElement &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelement.html#operator==

    Parameters
    ----------

    rhs : QOpcUaContentFilterElement
      Passed on as a value: Qt reads the C++ QOpcUaContentFilterElement,
      which stays Python's own.
    """
    #  bool operator==(const QOpcUaContentFilterElement &lhs, const
    #      QOpcUaContentFilterElement &rhs)
    return Rituals.call(
        'ritual_ZeqRK26QOpcUaContentFilterElementS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QOpcUaContentFilterElement) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaContentFilterElement &lhs, const
    QOpcUaContentFilterElement &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelement.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaContentFilterElement
      Passed on as a value: Qt reads the C++ QOpcUaContentFilterElement,
      which stays Python's own.
    """
    #  bool operator!=(const QOpcUaContentFilterElement &lhs, const
    #      QOpcUaContentFilterElement &rhs)
    return Rituals.call(
        'ritual_ZneRK26QOpcUaContentFilterElementS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaContentFilterElement::QOpcUaContentFilterElement()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelement.html
    """
    #  QOpcUaContentFilterElement::QOpcUaContentFilterElement()
    self._noteCreation(QOpcUaContentFilterElement, lambda: Rituals.call(
        'ritual_ZN26QOpcUaContentFilterElementC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaContentFilterElement) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaContentFilterElement::QOpcUaContentFilterElement(const
    QOpcUaContentFilterElement &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacontentfilterelement.html

    Parameters
    ----------

    a0 : QOpcUaContentFilterElement
      Passed on as a value: Qt reads the C++ QOpcUaContentFilterElement,
      which stays Python's own.
    """
    #  QOpcUaContentFilterElement::QOpcUaContentFilterElement(const
    #      QOpcUaContentFilterElement &a0)
    self._noteCreation(QOpcUaContentFilterElement, lambda: Rituals.call(
        'ritual_ZN26QOpcUaContentFilterElementC1ERKS_', self._valueOf(a0),
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

  @staticmethod
  def filterOperandsRef(*__, **_) -> Never:
    """
    Qt's 'QList<QVariant> &QOpcUaContentFilterElement::filterOperandsRef()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaContentFilterElement.filterOperandsRef' has no cute "
        "function yet. Qt's 'QList<QVariant> "
        "&QOpcUaContentFilterElement::filterOperandsRef()': gives a type "
        "Python has no way to take yet.")


#  Qt's 'QList<QOpcUaContentFilterElement>': the list of
#  QOpcUaContentFilterElement, which 'QList[QOpcUaContentFilterElement]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QOpcUaContentFilterElement.
QList.createKind(
    QOpcUaContentFilterElement, 'value',
    make='ritual_list_make_QOpcUaContentFilterElement',
    add='ritual_list_add_QOpcUaContentFilterElement',
    size='ritual_list_size_QOpcUaContentFilterElement',
    at='ritual_list_at_QOpcUaContentFilterElement',
    drop='ritual_list_drop_QOpcUaContentFilterElement',
)
