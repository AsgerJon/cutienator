"""
QDomNodeListPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomNodeListPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDomNodePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomNodePrivate = WAIT['QDomNodePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomNodeListPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomNodeListPrivate: a plain Python object standing
  in front of one C++ QDomNodeListPrivate.

  C++ hands a QDomNodeListPrivate around as a copy, so every C++
  QDomNodeListPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomNodeListPrivate that has a ritual and that
  Python can call so far, 9 names in all: '__eq__', 'createList',
  'checkNode', 'findNextInOrder', 'findPrevInOrder', 'maybeCreateList',
  'item', 'length', 'noexceptLength'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomNodeListPrivate::~QDomNodeListPrivate()': the destructor:
    Python removes its C++ QDomNodeListPrivate by it, and has no other use
    for it.
  - Qt's 'void QDomNodeListPrivate::forEachNode(qxp::function_ref<void
    (QDomNodePrivate *)> yield) const': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QDomNodeListPrivate is created at the first use, not by
    'QDomNodeListPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomNodeListPrivate back gives a copy the ritual made
    for Python, in a new cute QDomNodeListPrivate.
  - Each name of Qt's QDomNodeListPrivate that has no cute function yet,
    'forEachNode', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomNodeListPrivate'

  #  Qt's '~QDomNodeListPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QDomNodeListPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QDomNodeListPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def checkNode(self, p: Optional[QDomNodePrivate]) -> bool:
    """
    Calls Qt's 'bool QDomNodeListPrivate::checkNode(QDomNodePrivate *p)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelistprivate.html#checkNode

    Parameters
    ----------

    p : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDomNodeListPrivate::checkNode(QDomNodePrivate *p) const
    return self.uglySide.call(
        'ritual_ZNK19QDomNodeListPrivate9checkNodeEP15QDomNodePrivate',
        self._addressOf(p),
    )

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def findNextInOrder(
      self,
      p: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomNodeListPrivate::findNextInOrder(QDomNodePrivate *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#findNextInOrder

    Parameters
    ----------

    p : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodeListPrivate::findNextInOrder(QDomNodePrivate
    #      *p) const
    address = self.uglySide.call(
        'ritual_ZNK19QDomNodeListPrivate15findNextInOrderEP15QDomNodePrivat'
        'e',
        self._addressOf(p),
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def findPrevInOrder(
      self,
      p: Optional[QDomNodePrivate],
  ) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate
    *QDomNodeListPrivate::findPrevInOrder(QDomNodePrivate *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#findPrevInOrder

    Parameters
    ----------

    p : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodeListPrivate::findPrevInOrder(QDomNodePrivate
    #      *p) const
    address = self.uglySide.call(
        'ritual_ZNK19QDomNodeListPrivate15findPrevInOrderEP15QDomNodePrivat'
        'e',
        self._addressOf(p),
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  def maybeCreateList(self) -> bool:
    """
    Calls Qt's 'bool QDomNodeListPrivate::maybeCreateList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#maybeCreateList
    """
    #  bool QDomNodeListPrivate::maybeCreateList() const
    return self.uglySide.call(
        'ritual_ZNK19QDomNodeListPrivate15maybeCreateListEv',
    )

  def length(self) -> int:
    """
    Calls Qt's 'int QDomNodeListPrivate::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelistprivate.html#length
    """
    #  int QDomNodeListPrivate::length() const
    return self.uglySide.call('ritual_ZNK19QDomNodeListPrivate6lengthEv')

  def noexceptLength(self) -> int:
    """
    Calls Qt's 'int QDomNodeListPrivate::noexceptLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#noexceptLength
    """
    #  int QDomNodeListPrivate::noexceptLength() const
    return self.uglySide.call(
        'ritual_ZNK19QDomNodeListPrivate14noexceptLengthEv',
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

  @overload(THIS)
  def __eq__(self, a0: QDomNodeListPrivate) -> bool:
    """
    Calls Qt's 'bool QDomNodeListPrivate::operator==(const
    QDomNodeListPrivate &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#operator==

    Parameters
    ----------

    a0 : QDomNodeListPrivate
      Passed on as a value: Qt reads the C++ QDomNodeListPrivate, which stays
      Python's own.
    """
    #  bool QDomNodeListPrivate::operator==(const QDomNodeListPrivate &a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QDomNodeListPrivateeqERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomNodePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#QDomNodeListPrivate

    Parameters
    ----------

    a0 : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0)
    self._noteCreation(QDomNodeListPrivate, lambda: Rituals.call(
        'ritual_ZN19QDomNodeListPrivateC1EP15QDomNodePrivate',
        self._addressOf(a0),
    ))

  @overload(QDomNodePrivate, str)
  @overload(NoneType, str)
  def __init__(self, a0: Optional[QDomNodePrivate], a1: str) -> None:
    """
    Notes what was given, for Qt's
    'QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0, const
    QString &a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#QDomNodeListPrivate

    Parameters
    ----------

    a0 : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0, const
    #      QString &a1)
    self._noteCreation(QDomNodeListPrivate, lambda: Rituals.call(
        'ritual_ZN19QDomNodeListPrivateC1EP15QDomNodePrivateRK7QString',
        self._addressOf(a0), a1,
    ))

  @overload(QDomNodePrivate, str, str)
  @overload(NoneType, str, str)
  def __init__(
      self,
      a0: Optional[QDomNodePrivate],
      a1: str,
      a2: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0, const
    QString &a1, const QString &a2)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#QDomNodeListPrivate

    Parameters
    ----------

    a0 : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QDomNodeListPrivate::QDomNodeListPrivate(QDomNodePrivate *a0, const
    #      QString &a1, const QString &a2)
    self._noteCreation(QDomNodeListPrivate, lambda: Rituals.call(
        'ritual_ZN19QDomNodeListPrivateC1EP15QDomNodePrivateRK7QStringS4_',
        self._addressOf(a0), a1, a2,
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

  def createList(self) -> None:
    """
    Calls Qt's 'void QDomNodeListPrivate::createList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnodelistprivate.html#createList
    """
    #  void QDomNodeListPrivate::createList() const
    self.uglySide.call('ritual_ZNK19QDomNodeListPrivate10createListEv')

  @overload(int)
  def item(self, index: int) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomNodeListPrivate::item(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnodelistprivate.html#item

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomNodeListPrivate::item(int index)
    address = self.uglySide.call(
        'ritual_ZN19QDomNodeListPrivate4itemEi', index,
    )
    from . import QDomNodePrivate
    return QDomNodePrivate._cuteAt(address)

  @staticmethod
  def forEachNode(*__, **_) -> Never:
    """
    Qt's 'void QDomNodeListPrivate::forEachNode(qxp::function_ref<void
    (QDomNodePrivate *)> yield) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QDomNodeListPrivate.forEachNode' has no cute function yet. Qt's "
        "'void QDomNodeListPrivate::forEachNode(qxp::function_ref<void "
        "(QDomNodePrivate *)> yield) const': takes a type Python has no way "
        "to hand over yet.")
