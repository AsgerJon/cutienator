"""
QRhiVertexInputLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug
  from . import QRhiVertexInputAttribute, QRhiVertexInputBinding
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QRhiVertexInputLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiVertexInputLayout: a plain Python object standing
  in front of one C++ QRhiVertexInputLayout.

  C++ hands a QRhiVertexInputLayout around as a copy, so every C++
  QRhiVertexInputLayout behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiVertexInputLayout that has a ritual and that
  Python can call so far, 11 names in all: 'cbeginBindings', 'cendBindings',
  'bindingAt', 'bindingCount', 'cbeginAttributes', 'cendAttributes',
  'attributeAt', 'attributeCount', '__eq__', '__ne__', '__rlshift__'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QRhiVertexInputLayout::setBindings(std::
    initializer_list<QRhiVertexInputBinding> list)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QRhiVertexInputLayout::setAttributes(std::
    initializer_list<QRhiVertexInputAttribute> list)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QRhiVertexInputLayout::~QRhiVertexInputLayout()': the destructor:
    Python removes its C++ QRhiVertexInputLayout by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QRhiVertexInputLayout is created at the first use, not by
    'QRhiVertexInputLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiVertexInputLayout back gives a copy the ritual
    made for Python, in a new cute QRhiVertexInputLayout.
  - Each name of Qt's QRhiVertexInputLayout that has no cute function yet,
    'setAttributes', 'setBindings', holds a function that raises
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
  __qt_class__ = 'QRhiVertexInputLayout'

  #  Qt's '~QRhiVertexInputLayout()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiVertexInputLayout behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QRhiVertexInputLayoutD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cbeginBindings(self) -> Optional[QRhiVertexInputBinding]:
    """
    Calls Qt's 'const QRhiVertexInputBinding
    *QRhiVertexInputLayout::cbeginBindings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#cbeginBindings

    Returns
    -------

    Optional[QRhiVertexInputBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiVertexInputBinding *QRhiVertexInputLayout::cbeginBindings()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QRhiVertexInputLayout14cbeginBindingsEv',
    )
    from . import QRhiVertexInputBinding
    return QRhiVertexInputBinding._cuteAt(address)

  def cendBindings(self) -> Optional[QRhiVertexInputBinding]:
    """
    Calls Qt's 'const QRhiVertexInputBinding
    *QRhiVertexInputLayout::cendBindings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#cendBindings

    Returns
    -------

    Optional[QRhiVertexInputBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiVertexInputBinding *QRhiVertexInputLayout::cendBindings()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QRhiVertexInputLayout12cendBindingsEv',
    )
    from . import QRhiVertexInputBinding
    return QRhiVertexInputBinding._cuteAt(address)

  @overload(int)
  def bindingAt(self, index: int) -> Optional[QRhiVertexInputBinding]:
    """
    Calls Qt's 'const QRhiVertexInputBinding
    *QRhiVertexInputLayout::bindingAt(qsizetype index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#bindingAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiVertexInputBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiVertexInputBinding
    #      *QRhiVertexInputLayout::bindingAt(qsizetype index) const
    address = self.uglySide.call(
        'ritual_ZNK21QRhiVertexInputLayout9bindingAtEx', index,
    )
    from . import QRhiVertexInputBinding
    return QRhiVertexInputBinding._cuteAt(address)

  def bindingCount(self) -> int:
    """
    Calls Qt's 'qsizetype QRhiVertexInputLayout::bindingCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#bindingCount
    """
    #  qsizetype QRhiVertexInputLayout::bindingCount() const
    return self.uglySide.call(
        'ritual_ZNK21QRhiVertexInputLayout12bindingCountEv',
    )

  def cbeginAttributes(self) -> Optional[QRhiVertexInputAttribute]:
    """
    Calls Qt's 'const QRhiVertexInputAttribute
    *QRhiVertexInputLayout::cbeginAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#cbeginAttributes

    Returns
    -------

    Optional[QRhiVertexInputAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiVertexInputAttribute
    #      *QRhiVertexInputLayout::cbeginAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK21QRhiVertexInputLayout16cbeginAttributesEv',
    )
    from . import QRhiVertexInputAttribute
    return QRhiVertexInputAttribute._cuteAt(address)

  def cendAttributes(self) -> Optional[QRhiVertexInputAttribute]:
    """
    Calls Qt's 'const QRhiVertexInputAttribute
    *QRhiVertexInputLayout::cendAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#cendAttributes

    Returns
    -------

    Optional[QRhiVertexInputAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiVertexInputAttribute
    #      *QRhiVertexInputLayout::cendAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK21QRhiVertexInputLayout14cendAttributesEv',
    )
    from . import QRhiVertexInputAttribute
    return QRhiVertexInputAttribute._cuteAt(address)

  @overload(int)
  def attributeAt(self, index: int) -> Optional[QRhiVertexInputAttribute]:
    """
    Calls Qt's 'const QRhiVertexInputAttribute
    *QRhiVertexInputLayout::attributeAt(qsizetype index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#attributeAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiVertexInputAttribute]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiVertexInputAttribute
    #      *QRhiVertexInputLayout::attributeAt(qsizetype index) const
    address = self.uglySide.call(
        'ritual_ZNK21QRhiVertexInputLayout11attributeAtEx', index,
    )
    from . import QRhiVertexInputAttribute
    return QRhiVertexInputAttribute._cuteAt(address)

  def attributeCount(self) -> int:
    """
    Calls Qt's 'qsizetype QRhiVertexInputLayout::attributeCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#attributeCount
    """
    #  qsizetype QRhiVertexInputLayout::attributeCount() const
    return self.uglySide.call(
        'ritual_ZNK21QRhiVertexInputLayout14attributeCountEv',
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
  def __eq__(self, b: QRhiVertexInputLayout) -> bool:
    """
    Calls Qt's 'bool operator==(const QRhiVertexInputLayout &a, const
    QRhiVertexInputLayout &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#operator==

    Parameters
    ----------

    b : QRhiVertexInputLayout
      Passed on as a value: Qt reads the C++ QRhiVertexInputLayout, which
      stays Python's own.
    """
    #  bool operator==(const QRhiVertexInputLayout &a, const
    #      QRhiVertexInputLayout &b)
    return Rituals.call(
        'ritual_ZeqRK21QRhiVertexInputLayoutS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QRhiVertexInputLayout) -> bool:
    """
    Calls Qt's 'bool operator!=(const QRhiVertexInputLayout &a, const
    QRhiVertexInputLayout &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#operator!=

    Parameters
    ----------

    b : QRhiVertexInputLayout
      Passed on as a value: Qt reads the C++ QRhiVertexInputLayout, which
      stays Python's own.
    """
    #  bool operator!=(const QRhiVertexInputLayout &a, const
    #      QRhiVertexInputLayout &b)
    return Rituals.call(
        'ritual_ZneRK21QRhiVertexInputLayoutS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QRhiVertexInputLayout
    &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QRhiVertexInputLayout &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK21QRhiVertexInputLayout',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
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
    'QRhiVertexInputLayout::QRhiVertexInputLayout()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhivertexinputlayout.html#QRhiVertexInputLayout
    """
    #  QRhiVertexInputLayout::QRhiVertexInputLayout()
    self._noteCreation(QRhiVertexInputLayout, lambda: Rituals.call(
        'ritual_ZN21QRhiVertexInputLayoutC1Ev',
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
  def setAttributes(*__, **_) -> Never:
    """
    - Qt's 'void QRhiVertexInputLayout::setAttributes(std::
      initializer_list<QRhiVertexInputAttribute> list)': takes a type Python
      has no way to hand over yet.
    - Qt's 'QRhiVertexInputLayout::setAttributes': a template: a pattern and
      no single function.
    """
    raise NotImplementedError(
        "'QRhiVertexInputLayout.setAttributes' has no cute function yet. "
        "Qt's 'void "
        "QRhiVertexInputLayout::setAttributes(std::initializer_list<QRhiVert"
        "exInputAttribute> list)': takes a type Python has no way to hand "
        "over yet. Qt's 'QRhiVertexInputLayout::setAttributes': a template: "
        "a pattern and no single function.")

  @staticmethod
  def setBindings(*__, **_) -> Never:
    """
    - Qt's 'void QRhiVertexInputLayout::setBindings(std::
      initializer_list<QRhiVertexInputBinding> list)': takes a type Python
      has no way to hand over yet.
    - Qt's 'QRhiVertexInputLayout::setBindings': a template: a pattern and no
      single function.
    """
    raise NotImplementedError(
        "'QRhiVertexInputLayout.setBindings' has no cute function yet. Qt's "
        "'void "
        "QRhiVertexInputLayout::setBindings(std::initializer_list<QRhiVertex"
        "InputBinding> list)': takes a type Python has no way to hand over "
        "yet. Qt's 'QRhiVertexInputLayout::setBindings': a template: a "
        "pattern and no single function.")
