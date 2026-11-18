"""
CuteMixin provides shape
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.desc import Field
from worktoy.mcls import BaseObject

from ._ugly import Ugly

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional, Any


class CuteMixin(BaseObject):
  """
  CuteMixin provides shape
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _addressOf(cuteSide: Optional[Any]) -> Optional[int]:
    """
    Gives what a ritual takes in the place of a cute object: the address
    of the C++ object it stands for, or None for None, which C++ reads
    as no object. Asking makes the C++ object if it is not made yet.
    """
    if cuteSide is None:
      return None
    return cuteSide.uglySide.getAddress()

  @staticmethod
  def _bytesOf(text: Optional[str]) -> Optional[bytes]:
    """
    Gives what a ritual takes in the place of text: the text as bytes,
    or None for None, which C++ reads as no text.
    """
    if text is None:
      return None
    return text.encode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __private_name__: str = '__ugly_name__'

  #  Fallback Variables

  #  Private Variables
  __ugly_side__: Optional[object] = None

  #  Public Variables
  uglySide: Field[object] = Field()

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _createUglySide(self, ) -> None:
    raise NotImplementedError

  @uglySide.GET
  def _getUglySide(self, **kwargs) -> object:
    if self.__ugly_side__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createUglySide()
      return self._getUglySide(_recursion=True)
    return self.__ugly_side__

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

  @classmethod
  def _cuteAt(cls, address: Optional[int]) -> Optional[Any]:
    """
    Gives the cute object standing for the C++ object at an address
    that a ritual gave back. A cute function giving an object back ends
    with this:

      address = self.uglySide.call('ritual_ZNK7QObject6threadEv')
      return QThread._cuteAt(address)

    What comes back
    ---------------

    - None, when the address is None: C++ answered with no object.
    - The cute object that stands for that C++ object already, when
      there is one. It is given as it is, whatever class it has.
    - Otherwise a new object of the class this is called on, made
      around the address. No C++ object is created for it, and its
      '__init__' does not run: it stands for an object C++ made itself,
      as the thread Python runs in.

    Nothing keeps a cute object made here alive but the one who asked
    for it. Asked again after it is gone, a new one is made.

    Parameters
    ----------

    address : Optional[int]
      What the ritual gave back: an address, or None.

    Returns
    -------

    Optional[Any]
      A cute object, or None.
    """
    if address is None:
      return None
    try:
      return Ugly.at(address).getCuteSide()
    except LookupError:
      pass
    cuteSide = cls.__new__(cls)
    ugly = Ugly()
    ugly.setAddress(address)
    ugly.setCuteSide(cuteSide)
    cuteSide.__ugly_side__ = ugly
    return cuteSide

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
