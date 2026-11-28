"""
QDesignerMetaDataBaseItemInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractmetadatabase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']


class QDesignerMetaDataBaseItemInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerMetaDataBaseItemInterface: a plain Python
  object standing in front of one C++ QDesignerMetaDataBaseItemInterface.

  What exists
  -----------

  Every function of Qt's QDesignerMetaDataBaseItemInterface that has a ritual
  and that Python can call so far, 6 names in all: 'name', 'setName',
  'tabOrder', 'setTabOrder', 'enabled', 'setEnabled'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QDesignerMetaDataBaseItemInterface::~QDesignerMetaDataBaseItemInterface(
    )': the destructor: Python never removes a C++
    QDesignerMetaDataBaseItemInterface.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerMetaDataBaseItemInterface is created at the first use,
    not by 'QDesignerMetaDataBaseItemInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMetaDataBaseItemInterface.
  - Each name of Qt's QDesignerMetaDataBaseItemInterface that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMetaDataBaseItemInterface'

  #  A C++ QDesignerMetaDataBaseItemInterface Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMetaDataBaseItemInterface'

  #  The functions Qt calls itself that QDesignerMetaDataBaseItemInterface is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'tabOrder': (
          'QList<QWidget *> QDesignerMetaDataBaseItemInterface::tabOrder() '
          'const',
      ),
      'setTabOrder': (
          'void QDesignerMetaDataBaseItemInterface::setTabOrder(const '
          'QList<QWidget *> &)',
      ),
  }

  #  The functions Qt calls itself that QDesignerMetaDataBaseItemInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK34QDesignerMetaDataBaseItemInterface4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'setName': (
          ('_ZN34QDesignerMetaDataBaseItemInterface7setNameERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'enabled': (
          ('_ZNK34QDesignerMetaDataBaseItemInterface7enabledEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setEnabled': (
          ('_ZN34QDesignerMetaDataBaseItemInterface10setEnabledEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
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

  def name(self) -> str:
    """
    Calls Qt's 'QString QDesignerMetaDataBaseItemInterface::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseiteminterface.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerMetaDataBaseItemInterface::name() const
    return self.uglySide.call(
        'ritual_ZNK34QDesignerMetaDataBaseItemInterface4nameEv',
    )

  def tabOrder(self) -> QList[QWidget]:
    """
    Calls Qt's 'QList<QWidget *>
    QDesignerMetaDataBaseItemInterface::tabOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseiteminterface.html#tabOrder

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWidget *> QDesignerMetaDataBaseItemInterface::tabOrder() const
    address = self.uglySide.call(
        'ritual_ZNK34QDesignerMetaDataBaseItemInterface8tabOrderEv',
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QDesignerMetaDataBaseItemInterface::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseiteminterface.html#enabled
    """
    #  bool QDesignerMetaDataBaseItemInterface::enabled() const
    return self.uglySide.call(
        'ritual_ZNK34QDesignerMetaDataBaseItemInterface7enabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDesignerMetaDataBaseItemInterface::setName(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseiteminterface.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerMetaDataBaseItemInterface::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN34QDesignerMetaDataBaseItemInterface7setNameERK7QString',
        name,
    )

  @overload(QList[QWidget])
  def setTabOrder(self, tabOrder: QList[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerMetaDataBaseItemInterface::setTabOrder(const
    QList<QWidget *> &tabOrder)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseiteminterface.html

    Parameters
    ----------

    tabOrder : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerMetaDataBaseItemInterface::setTabOrder(const
    #      QList<QWidget *> &tabOrder)
    self.uglySide.call(
        'ritual_ZN34QDesignerMetaDataBaseItemInterface11setTabOrderERK5QLis'
        'tIP7QWidgetE',
        self._valueOf(tabOrder),
    )

  @overload(bool)
  def setEnabled(self, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerMetaDataBaseItemInterface::setEnabled(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermetadatabaseiteminterface.html#setEnabled

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QDesignerMetaDataBaseItemInterface::setEnabled(bool b)
    self.uglySide.call(
        'ritual_ZN34QDesignerMetaDataBaseItemInterface10setEnabledEb', b,
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
    Qt's
    'QDesignerMetaDataBaseItemInterface::QDesignerMetaDataBaseItemInterface(
    )': the class is abstract, so C++ cannot make one, and the C++ class of
    ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerMetaDataBaseItemInterface.__init__' has no cute function "
        "yet. Qt's "
        "'QDesignerMetaDataBaseItemInterface::QDesignerMetaDataBaseItemInter"
        "face()': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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
