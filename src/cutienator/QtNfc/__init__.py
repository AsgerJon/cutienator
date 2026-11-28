"""
The 'cutienator.QtNfc' package provides the cute classes of the part of
Qt named QtNfc, under the name PySide6 has for it.

  from cutienator.QtNfc import QNdefNfcSmartPosterRecordPrivate, QNdefRecordPrivate

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QNdefNfcSmartPosterRecordPrivate',
    'QNdefRecordPrivate',
    'QNdefRecord',
    'QResponseApdu',
    'QNdefMessage',
    'QNdefNfcIconRecord',
    'QNdefNfcSizeRecord',
    'QNdefNfcTextRecord',
    'QNdefNfcTypeRecord',
    'QNdefAccessFsm',
    'QNdefFilter',
    'QNdefNfcUriRecord',
    'NeardHelper',
    'QNdefNfcSmartPosterRecord',
    'QNearFieldTarget',
    'QNearFieldTargetPrivate',
    'QNdefNfcActRecord',
    'QNearFieldManager',
    'QNearFieldManagerPrivate',
    'QNearFieldTargetPrivateImpl',
    'QNfcNdefNotifier',
    'QNfcTagType4NdefFsm',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_ndef_nfc_smart_poster_record_private import QNdefNfcSmartPosterRecordPrivate
  from ._q_ndef_record_private import QNdefRecordPrivate
  from ._q_ndef_record import QNdefRecord
  from ._q_response_apdu import QResponseApdu
  from ._q_ndef_message import QNdefMessage
  from ._q_ndef_nfc_icon_record import QNdefNfcIconRecord
  from ._q_ndef_nfc_size_record import QNdefNfcSizeRecord
  from ._q_ndef_nfc_text_record import QNdefNfcTextRecord
  from ._q_ndef_nfc_type_record import QNdefNfcTypeRecord
  from ._q_ndef_access_fsm import QNdefAccessFsm
  from ._q_ndef_filter import QNdefFilter
  from ._q_ndef_nfc_uri_record import QNdefNfcUriRecord
  from ._neard_helper import NeardHelper
  from ._q_ndef_nfc_smart_poster_record import QNdefNfcSmartPosterRecord
  from ._q_near_field_target import QNearFieldTarget
  from ._q_near_field_target_private import QNearFieldTargetPrivate
  from ._q_ndef_nfc_act_record import QNdefNfcActRecord
  from ._q_near_field_manager import QNearFieldManager
  from ._q_near_field_manager_private import QNearFieldManagerPrivate
  from ._q_near_field_target_private_impl import QNearFieldTargetPrivateImpl
  from ._q_nfc_ndef_notifier import QNfcNdefNotifier
  from ._q_nfc_tag_type4_ndef_fsm import QNfcTagType4NdefFsm
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QNdefNfcSmartPosterRecordPrivate': '_q_ndef_nfc_smart_poster_record_private',
      'QNdefRecordPrivate': '_q_ndef_record_private',
      'QNdefRecord': '_q_ndef_record',
      'QResponseApdu': '_q_response_apdu',
      'QNdefMessage': '_q_ndef_message',
      'QNdefNfcIconRecord': '_q_ndef_nfc_icon_record',
      'QNdefNfcSizeRecord': '_q_ndef_nfc_size_record',
      'QNdefNfcTextRecord': '_q_ndef_nfc_text_record',
      'QNdefNfcTypeRecord': '_q_ndef_nfc_type_record',
      'QNdefAccessFsm': '_q_ndef_access_fsm',
      'QNdefFilter': '_q_ndef_filter',
      'QNdefNfcUriRecord': '_q_ndef_nfc_uri_record',
      'NeardHelper': '_neard_helper',
      'QNdefNfcSmartPosterRecord': '_q_ndef_nfc_smart_poster_record',
      'QNearFieldTarget': '_q_near_field_target',
      'QNearFieldTargetPrivate': '_q_near_field_target_private',
      'QNdefNfcActRecord': '_q_ndef_nfc_act_record',
      'QNearFieldManager': '_q_near_field_manager',
      'QNearFieldManagerPrivate': '_q_near_field_manager_private',
      'QNearFieldTargetPrivateImpl': '_q_near_field_target_private_impl',
      'QNfcNdefNotifier': '_q_nfc_ndef_notifier',
      'QNfcTagType4NdefFsm': '_q_nfc_tag_type4_ndef_fsm',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtNfc import QNfcTagType4NdefFsm'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
