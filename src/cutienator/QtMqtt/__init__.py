"""
The 'cutienator.QtMqtt' package provides the cute classes of the part of
Qt named QtMqtt, under the name PySide6 has for it.

  from cutienator.QtMqtt import QMqttMessageStatusProperties, QMqttUserProperties

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
    'QMqttMessageStatusProperties',
    'QMqttUserProperties',
    'QMqttConnectionPropertiesData',
    'QMqttLastWillPropertiesData',
    'QMqttMessagePrivate',
    'QMqttMessageStatusPropertiesData',
    'QMqttPublishPropertiesData',
    'QMqttServerConnectionPropertiesData',
    'QMqttSubscriptionProperties',
    'QMqttUnsubscriptionProperties',
    'QMqttControlPacket',
    'QMqttAuthenticationProperties',
    'QMqttConnectionProperties',
    'QMqttLastWillProperties',
    'QMqttPublishProperties',
    'QMqttStringPair',
    'QMqttServerConnectionProperties',
    'QMqttTopicName',
    'QMqttMessage',
    'QMqttSubscriptionPrivate',
    'QMqttTopicFilter',
    'QMqttClient',
    'QMqttClientPrivate',
    'QMqttSubscription',
    'QMqttConnection',
    'QMqtt',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_mqtt_message_status_properties import QMqttMessageStatusProperties
  from ._q_mqtt_user_properties import QMqttUserProperties
  from ._q_mqtt_connection_properties_data import QMqttConnectionPropertiesData
  from ._q_mqtt_last_will_properties_data import QMqttLastWillPropertiesData
  from ._q_mqtt_message_private import QMqttMessagePrivate
  from ._q_mqtt_message_status_properties_data import QMqttMessageStatusPropertiesData
  from ._q_mqtt_publish_properties_data import QMqttPublishPropertiesData
  from ._q_mqtt_server_connection_properties_data import QMqttServerConnectionPropertiesData
  from ._q_mqtt_subscription_properties import QMqttSubscriptionProperties
  from ._q_mqtt_unsubscription_properties import QMqttUnsubscriptionProperties
  from ._q_mqtt_control_packet import QMqttControlPacket
  from ._q_mqtt_authentication_properties import QMqttAuthenticationProperties
  from ._q_mqtt_connection_properties import QMqttConnectionProperties
  from ._q_mqtt_last_will_properties import QMqttLastWillProperties
  from ._q_mqtt_publish_properties import QMqttPublishProperties
  from ._q_mqtt_string_pair import QMqttStringPair
  from ._q_mqtt_server_connection_properties import QMqttServerConnectionProperties
  from ._q_mqtt_topic_name import QMqttTopicName
  from ._q_mqtt_message import QMqttMessage
  from ._q_mqtt_subscription_private import QMqttSubscriptionPrivate
  from ._q_mqtt_topic_filter import QMqttTopicFilter
  from ._q_mqtt_client import QMqttClient
  from ._q_mqtt_client_private import QMqttClientPrivate
  from ._q_mqtt_subscription import QMqttSubscription
  from ._q_mqtt_connection import QMqttConnection
  from . import QMqtt
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QMqttMessageStatusProperties': '_q_mqtt_message_status_properties',
      'QMqttUserProperties': '_q_mqtt_user_properties',
      'QMqttConnectionPropertiesData': '_q_mqtt_connection_properties_data',
      'QMqttLastWillPropertiesData': '_q_mqtt_last_will_properties_data',
      'QMqttMessagePrivate': '_q_mqtt_message_private',
      'QMqttMessageStatusPropertiesData': '_q_mqtt_message_status_properties_data',
      'QMqttPublishPropertiesData': '_q_mqtt_publish_properties_data',
      'QMqttServerConnectionPropertiesData': '_q_mqtt_server_connection_properties_data',
      'QMqttSubscriptionProperties': '_q_mqtt_subscription_properties',
      'QMqttUnsubscriptionProperties': '_q_mqtt_unsubscription_properties',
      'QMqttControlPacket': '_q_mqtt_control_packet',
      'QMqttAuthenticationProperties': '_q_mqtt_authentication_properties',
      'QMqttConnectionProperties': '_q_mqtt_connection_properties',
      'QMqttLastWillProperties': '_q_mqtt_last_will_properties',
      'QMqttPublishProperties': '_q_mqtt_publish_properties',
      'QMqttStringPair': '_q_mqtt_string_pair',
      'QMqttServerConnectionProperties': '_q_mqtt_server_connection_properties',
      'QMqttTopicName': '_q_mqtt_topic_name',
      'QMqttMessage': '_q_mqtt_message',
      'QMqttSubscriptionPrivate': '_q_mqtt_subscription_private',
      'QMqttTopicFilter': '_q_mqtt_topic_filter',
      'QMqttClient': '_q_mqtt_client',
      'QMqttClientPrivate': '_q_mqtt_client_private',
      'QMqttSubscription': '_q_mqtt_subscription',
      'QMqttConnection': '_q_mqtt_connection',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QMqtt',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtMqtt import QMqttConnection'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
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
