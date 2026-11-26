"""RawAddressExpert says how an address crosses that points to no
object of a class: as an address, with nothing known of what lies
there."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from . import TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]


class RawAddressExpert(TypeExpert):
  """
  Says how an address crosses that 'AddressExpert' leaves: an address
  of an address, as 'void **' and 'const GLchar *const *'; an address
  that may not be changed itself, as
  'const QOpenGLPixelTransferOptions *const'; and a thing of the system
  that is an address by its name, as 'GLsync'. The ritual takes it as
  the header writes it and hands it on; Python hands over a number,
  and what lies there is for the Python side to know. Its word in the
  row is 'address'; its kind, 'raw address', tells it from the address
  of an object of a class, which Python knows by its cute class.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The names of things of the system that are addresses, which no
  #  header of Qt says: OpenGL's 'GLsync' is 'struct __GLsync *', and
  #  its 'GLeglImageOES' is 'void *', by the OpenGL specification of
  #  Khronos, on every system alike.
  __system_addresses__ = ('GLsync', 'GLeglImageOES', 'GLeglClientBufferEXT')
  #  An address, as the compiler writes one: it ends in '*', or in
  #  '* const' or '*const' where the address itself may not change.
  __address_ending__ = re.compile(r'\*\s*(?:const\s*)?$')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('raw address',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims every address 'AddressExpert' leaves, and the things of
    the system that are addresses by their name."""
    if plain in self.__system_addresses__:
      return True
    if '(' in plain:
      #  An address of a function is 'FunctionAddressExpert''s.
      return False
    return True if self.__address_ending__.search(plain) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the address crosses as it is."""
    return dict(kind='raw address', word='address')
