"""
QRhiShaderResourceBindings binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteFlags, WAIT
from ..occult import Rituals
from . import QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QRhiImplementation, QRhiShaderResourceBinding
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiShaderResourceBindings(QRhiResource):
  """
  The cute side of Qt's QRhiShaderResourceBindings: a plain Python object
  standing in front of one C++ QRhiShaderResourceBindings.

  It is built on the cute 'QRhiResource', as Qt's QRhiShaderResourceBindings
  is built on Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiShaderResourceBindings that has a ritual and
  that Python can call so far, 8 names in all: 'resourceType',
  'cbeginBindings', 'cendBindings', 'bindingAt', 'bindingCount',
  'isLayoutCompatible', 'create', 'updateResources'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QRhiShaderResourceBindings::setBindings(std::
    initializer_list<QRhiShaderResourceBinding> list)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVector<quint32>
    QRhiShaderResourceBindings::serializedLayoutDescription() const': gives a
    type Python has no way to take yet.
  - Qt's 'QDebug operator<<(QDebug a0, const QRhiShaderResourceBindings
    &a1)': an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QRhiShaderResourceBindings is created at the first use, not by
    'QRhiShaderResourceBindings(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiShaderResourceBindings.
  - Each name of Qt's QRhiShaderResourceBindings that has no cute function
    yet, 'serializedLayoutDescription', 'setBindings', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QRhiShaderResourceBindings, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class UpdateFlag(CuteFlags):
    """
    The flags enum 'QRhiShaderResourceBindings::UpdateFlag' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QRhiShaderResourceBindings::UpdateFlags'.
    """

    BindingsAreSorted = 0x1

  UpdateFlags = UpdateFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiShaderResourceBindings'

  #  A C++ QRhiShaderResourceBindings Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiShaderResourceBindings'

  #  The functions Qt calls itself that QRhiShaderResourceBindings is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN26QRhiShaderResourceBindings6createEv',
           ('bool', 'number', ''),
           ()),
      ),
      'updateResources': (
          ('_ZN26QRhiShaderResourceBindings15updateResourcesE6QFlagsINS_10U'
           'pdateFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtGui:QRhiShaderResourceBindings.UpdateFlag'),
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

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiShaderResourceBindings::resourceType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiShaderResourceBindings::resourceType() const
    ritual = 'ritual_ZNK26QRhiShaderResourceBindings12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QRhiShaderResourceBindings12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

  def cbeginBindings(self) -> Optional[QRhiShaderResourceBinding]:
    """
    Calls Qt's 'const QRhiShaderResourceBinding
    *QRhiShaderResourceBindings::cbeginBindings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html#cbeginBindings

    Returns
    -------

    Optional[QRhiShaderResourceBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderResourceBinding
    #      *QRhiShaderResourceBindings::cbeginBindings() const
    address = self.uglySide.call(
        'ritual_ZNK26QRhiShaderResourceBindings14cbeginBindingsEv',
    )
    from . import QRhiShaderResourceBinding
    return QRhiShaderResourceBinding._cuteAt(address)

  def cendBindings(self) -> Optional[QRhiShaderResourceBinding]:
    """
    Calls Qt's 'const QRhiShaderResourceBinding
    *QRhiShaderResourceBindings::cendBindings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html#cendBindings

    Returns
    -------

    Optional[QRhiShaderResourceBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderResourceBinding
    #      *QRhiShaderResourceBindings::cendBindings() const
    address = self.uglySide.call(
        'ritual_ZNK26QRhiShaderResourceBindings12cendBindingsEv',
    )
    from . import QRhiShaderResourceBinding
    return QRhiShaderResourceBinding._cuteAt(address)

  @overload(int)
  def bindingAt(self, index: int) -> Optional[QRhiShaderResourceBinding]:
    """
    Calls Qt's 'const QRhiShaderResourceBinding
    *QRhiShaderResourceBindings::bindingAt(qsizetype index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html#bindingAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiShaderResourceBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiShaderResourceBinding
    #      *QRhiShaderResourceBindings::bindingAt(qsizetype index) const
    address = self.uglySide.call(
        'ritual_ZNK26QRhiShaderResourceBindings9bindingAtEx', index,
    )
    from . import QRhiShaderResourceBinding
    return QRhiShaderResourceBinding._cuteAt(address)

  def bindingCount(self) -> int:
    """
    Calls Qt's 'qsizetype QRhiShaderResourceBindings::bindingCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html#bindingCount
    """
    #  qsizetype QRhiShaderResourceBindings::bindingCount() const
    return self.uglySide.call(
        'ritual_ZNK26QRhiShaderResourceBindings12bindingCountEv',
    )

  @overload(THIS)
  @overload(NoneType)
  def isLayoutCompatible(
      self,
      other: Optional[QRhiShaderResourceBindings],
  ) -> bool:
    """
    Calls Qt's 'bool QRhiShaderResourceBindings::isLayoutCompatible(const
    QRhiShaderResourceBindings *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html#isLayoutCompatible

    Parameters
    ----------

    other : Optional[QRhiShaderResourceBindings]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhiShaderResourceBindings::isLayoutCompatible(const
    #      QRhiShaderResourceBindings *other) const
    return self.uglySide.call(
        'ritual_ZNK26QRhiShaderResourceBindings18isLayoutCompatibleEPKS_',
        self._addressOf(other),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiImplementation)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiShaderResourceBindings::QRhiShaderResourceBindings(
    QRhiImplementation *rhi)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiShaderResourceBindings::QRhiShaderResourceBindings(
    #      QRhiImplementation *rhi)
    self._noteCreation(QRhiShaderResourceBindings, lambda: Rituals.call(
        'ritual_ZN26QRhiShaderResourceBindingsC1EP18QRhiImplementation',
        self._addressOf(rhi),
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QRhiShaderResourceBindings::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html#create
    """
    #  bool QRhiShaderResourceBindings::create()
    return self.uglySide.call(
        'ritual_ZN26QRhiShaderResourceBindings6createEv',
    )

  @overload()
  @overload(UpdateFlags)
  def updateResources(self, flags: UpdateFlags = UpdateFlags()) -> None:
    """
    Calls Qt's 'void QRhiShaderResourceBindings::updateResources(UpdateFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderresourcebindings.html#updateResources

    Parameters
    ----------

    flags : UpdateFlags
      Passed on as its number. May be left out, as in Qt: it is then
      UpdateFlags().
    """
    #  void QRhiShaderResourceBindings::updateResources(UpdateFlags flags)
    self.uglySide.call(
        'ritual_ZN26QRhiShaderResourceBindings15updateResourcesE6QFlagsINS_'
        '10UpdateFlagEE',
        flags.value,
    )

  @staticmethod
  def serializedLayoutDescription(*__, **_) -> Never:
    """
    Qt's 'QVector<quint32>
    QRhiShaderResourceBindings::serializedLayoutDescription() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRhiShaderResourceBindings.serializedLayoutDescription' has no "
        "cute function yet. Qt's 'QVector<quint32> "
        "QRhiShaderResourceBindings::serializedLayoutDescription() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setBindings(*__, **_) -> Never:
    """
    - Qt's 'void QRhiShaderResourceBindings::setBindings(std::
      initializer_list<QRhiShaderResourceBinding> list)': takes a type Python
      has no way to hand over yet.
    - Qt's 'QRhiShaderResourceBindings::setBindings': a template: a pattern
      and no single function.
    """
    raise NotImplementedError(
        "'QRhiShaderResourceBindings.setBindings' has no cute function yet. "
        "Qt's 'void "
        "QRhiShaderResourceBindings::setBindings(std::initializer_list<QRhiS"
        "haderResourceBinding> list)': takes a type Python has no way to "
        "hand over yet. Qt's 'QRhiShaderResourceBindings::setBindings': a "
        "template: a pattern and no single function.")
