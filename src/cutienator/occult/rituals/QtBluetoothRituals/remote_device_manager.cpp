//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/remotedevicemanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/remotedevicemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QLoggingCategory>
#include <QtBluetooth/private/remotedevicemanager_p.h>
#include <QtBluetooth/private/bluez5_helper_p.h>
#include <QtBluetooth/private/device1_bluez5_p.h>
#include <QtBluetooth/private/objectmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/remotedevicemanager.cpp, line 50, as _ZN19RemoteDeviceManager8runQueueEv
inline void RemoteDeviceManager::runQueue()
{
    if (jobInProgress || adapterPath.isEmpty())
        return;

    if (jobQueue.empty())
        return;

    jobInProgress = true;
    switch (jobQueue.front().first) {
    case JobType::JobDisconnectDevice:
        disconnectDevice(jobQueue.front().second);
        break;
    default:
        break;
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *RemoteDeviceManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19RemoteDeviceManager10metaObjectEv(
    const RemoteDeviceManager *self) {
  return self->metaObject();
}

//  void *RemoteDeviceManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19RemoteDeviceManager11qt_metacastEPKc(
    RemoteDeviceManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int RemoteDeviceManager::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19RemoteDeviceManager11qt_metacallEN11QMetaObject4CallEiPPv(
    RemoteDeviceManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  bool RemoteDeviceManager::isJobInProgress() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19RemoteDeviceManager15isJobInProgressEv(
    const RemoteDeviceManager *self) {
  return self->isJobInProgress();
}

//  void RemoteDeviceManager::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19RemoteDeviceManager8finishedEv(RemoteDeviceManager *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "RemoteDeviceManager")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void RemoteDeviceManager::runQueue()
extern "C" Q_DECL_EXPORT
void ritual_ZN19RemoteDeviceManager8runQueueEv(RemoteDeviceManager *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "RemoteDeviceManager")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "runQueue()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "runQueue()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void RemoteDeviceManager::prepareNextJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN19RemoteDeviceManager14prepareNextJobEv(
    RemoteDeviceManager *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "RemoteDeviceManager")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "prepareNextJob()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "prepareNextJob()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(bluez)
