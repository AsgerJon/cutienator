"""
QSslKeyingMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qsslkeyingmaterial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']


class QSslKeyingMaterial(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSslKeyingMaterial: a plain Python object standing in
  front of one C++ QSslKeyingMaterial.

  C++ hands a QSslKeyingMaterial around as a copy, so every C++
  QSslKeyingMaterial behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSslKeyingMaterial that has a ritual and that Python
  can call so far, 9 names in all: 'isValid', 'label', 'context', 'value',
  'requestedSize', 'clone', '__eq__', '__ne__', '__rlshift__'. It can be made
  from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSslKeyingMaterial &QSslKeyingMaterial::operator=(const
    QSslKeyingMaterial &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QSslKeyingMaterial::QSslKeyingMaterial(QSslKeyingMaterial
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QSslKeyingMaterial
    &QSslKeyingMaterial::operator=(QSslKeyingMaterial &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QSslKeyingMaterial::~QSslKeyingMaterial()': the destructor: Python
    removes its C++ QSslKeyingMaterial by it, and has no other use for it.
  - Qt's 'void QSslKeyingMaterial::swap(QSslKeyingMaterial &other)': takes a
    type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSslKeyingMaterial is created at the first use, not by
    'QSslKeyingMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSslKeyingMaterial back gives a copy the ritual made
    for Python, in a new cute QSslKeyingMaterial.
  - Each name of Qt's QSslKeyingMaterial that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSslKeyingMaterial'

  #  Qt's '~QSslKeyingMaterial()'. Naming it makes this a value class: Python
  #  owns every C++ QSslKeyingMaterial behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSslKeyingMaterialD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSslKeyingMaterial::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyingmaterial.html#isValid
    """
    #  bool QSslKeyingMaterial::isValid() const
    return self.uglySide.call('ritual_ZNK18QSslKeyingMaterial7isValidEv')

  def label(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslKeyingMaterial::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyingmaterial.html#label

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslKeyingMaterial::label() const
    address = self.uglySide.call('ritual_ZNK18QSslKeyingMaterial5labelEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def context(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslKeyingMaterial::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyingmaterial.html#context

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslKeyingMaterial::context() const
    address = self.uglySide.call('ritual_ZNK18QSslKeyingMaterial7contextEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSslKeyingMaterial::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyingmaterial.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSslKeyingMaterial::value() const
    address = self.uglySide.call('ritual_ZNK18QSslKeyingMaterial5valueEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def requestedSize(self) -> int:
    """
    Calls Qt's 'qsizetype QSslKeyingMaterial::requestedSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslkeyingmaterial.html#requestedSize
    """
    #  qsizetype QSslKeyingMaterial::requestedSize() const
    return self.uglySide.call(
        'ritual_ZNK18QSslKeyingMaterial13requestedSizeEv',
    )

  def clone(self) -> QSslKeyingMaterial:
    """
    Calls Qt's 'QSslKeyingMaterial QSslKeyingMaterial::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyingmaterial.html#clone

    Returns
    -------

    QSslKeyingMaterial
      A new cute QSslKeyingMaterial around the copy Qt gave back. Python owns
      it.
    """
    #  QSslKeyingMaterial QSslKeyingMaterial::clone() const
    address = self.uglySide.call('ritual_ZNK18QSslKeyingMaterial5cloneEv')
    return QSslKeyingMaterial._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QSslKeyingMaterial) -> bool:
    """
    Calls Qt's 'bool operator==(const QSslKeyingMaterial &lhs, const
    QSslKeyingMaterial &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyingmaterial.html#operator==

    Parameters
    ----------

    rhs : QSslKeyingMaterial
      Passed on as a value: Qt reads the C++ QSslKeyingMaterial, which stays
      Python's own.
    """
    #  bool operator==(const QSslKeyingMaterial &lhs, const
    #      QSslKeyingMaterial &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QSslKeyingMaterialS1_',
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
  def __ne__(self, rhs: QSslKeyingMaterial) -> bool:
    """
    Calls Qt's 'bool operator!=(const QSslKeyingMaterial &lhs, const
    QSslKeyingMaterial &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyingmaterial.html#operator!=

    Parameters
    ----------

    rhs : QSslKeyingMaterial
      Passed on as a value: Qt reads the C++ QSslKeyingMaterial, which stays
      Python's own.
    """
    #  bool operator!=(const QSslKeyingMaterial &lhs, const
    #      QSslKeyingMaterial &rhs)
    return Rituals.call(
        'ritual_ZneRK18QSslKeyingMaterialS1_',
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

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QSslKeyingMaterial
    &keying)'.

    Qt's own words: https://doc.qt.io/qt-6/qsslkeyingmaterial.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QSslKeyingMaterial &keying)
    address = Rituals.call(
        'ritual_Zls6QDebugRK18QSslKeyingMaterial',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    'QSslKeyingMaterial::QSslKeyingMaterial()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslkeyingmaterial.html#QSslKeyingMaterial
    """
    #  QSslKeyingMaterial::QSslKeyingMaterial()
    self._noteCreation(QSslKeyingMaterial, lambda: Rituals.call(
        'ritual_ZN18QSslKeyingMaterialC1Ev',
    ))

  @overload(QByteArray, int)
  def __init__(self, label: QByteArray, size: int) -> None:
    """
    Notes what was given, for Qt's
    'QSslKeyingMaterial::QSslKeyingMaterial(const QByteArray &label,
    qsizetype size)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslkeyingmaterial.html#QSslKeyingMaterial

    Parameters
    ----------

    label : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    size : int
      Passed on as it is.
    """
    #  QSslKeyingMaterial::QSslKeyingMaterial(const QByteArray &label,
    #      qsizetype size)
    self._noteCreation(QSslKeyingMaterial, lambda: Rituals.call(
        'ritual_ZN18QSslKeyingMaterialC1ERK10QByteArrayx',
        self._valueOf(label), size,
    ))

  @overload(QByteArray, int, QByteArray)
  def __init__(
      self,
      label: QByteArray,
      size: int,
      context: QByteArray,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSslKeyingMaterial::QSslKeyingMaterial(const QByteArray &label,
    qsizetype size, const QByteArray &context)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslkeyingmaterial.html#QSslKeyingMaterial

    Parameters
    ----------

    label : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    size : int
      Passed on as it is.

    context : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QSslKeyingMaterial::QSslKeyingMaterial(const QByteArray &label,
    #      qsizetype size, const QByteArray &context)
    self._noteCreation(QSslKeyingMaterial, lambda: Rituals.call(
        'ritual_ZN18QSslKeyingMaterialC1ERK10QByteArrayxS2_',
        self._valueOf(label), size, self._valueOf(context),
    ))

  @overload(THIS)
  def __init__(self, other: QSslKeyingMaterial) -> None:
    """
    Notes what was given, for Qt's
    'QSslKeyingMaterial::QSslKeyingMaterial(const QSslKeyingMaterial
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsslkeyingmaterial.html#QSslKeyingMaterial

    Parameters
    ----------

    other : QSslKeyingMaterial
      Passed on as a value: Qt reads the C++ QSslKeyingMaterial, which stays
      Python's own.
    """
    #  QSslKeyingMaterial::QSslKeyingMaterial(const QSslKeyingMaterial
    #      &other)
    self._noteCreation(QSslKeyingMaterial, lambda: Rituals.call(
        'ritual_ZN18QSslKeyingMaterialC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSslKeyingMaterial::swap(QSslKeyingMaterial &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSslKeyingMaterial.swap' has no cute function yet. Qt's 'void "
        "QSslKeyingMaterial::swap(QSslKeyingMaterial &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QSslKeyingMaterial>': the list of QSslKeyingMaterial, which
#  'QList[QSslKeyingMaterial]' gives. It is made here, so that there is one
#  as soon as there can be a QSslKeyingMaterial.
QList.createKind(
    QSslKeyingMaterial, 'value',
    make='ritual_list_make_QSslKeyingMaterial',
    add='ritual_list_add_QSslKeyingMaterial',
    size='ritual_list_size_QSslKeyingMaterial',
    at='ritual_list_at_QSslKeyingMaterial',
    drop='ritual_list_drop_QSslKeyingMaterial',
)
