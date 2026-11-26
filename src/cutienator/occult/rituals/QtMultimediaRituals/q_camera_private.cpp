//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qcamera_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/qcamera.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qcameradevice.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qcamera_p.h>
#include <QtMultimedia/qcameradevice.h>
#include <QtMultimedia/private/qplatformcamera_p.h>
#include <QtMultimedia/private/qplatformimagecapture_p.h>
#include <QtMultimedia/private/qplatformmediaintegration_p.h>
#include <QtMultimedia/private/qplatformmediacapture_p.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/qmediacapturesession.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/camera/qcamera.cpp, line 90, as _ZN14QCameraPrivate4initERK13QCameraDevice
inline void QCameraPrivate::init(const QCameraDevice &device)
{
    Q_Q(QCamera);

    auto maybeControl = QPlatformMediaIntegration::instance()->createCamera(q);
    if (!maybeControl) {
        qWarning() << "Failed to initialize QCamera" << maybeControl.error();
        return;
    }
    control = maybeControl.value();
    cameraDevice = !device.isNull() ? device : QMediaDevices::defaultVideoInput();
    if (cameraDevice.isNull())
        control->updateError(QCamera::CameraError, QStringLiteral("No camera detected"));
    control->setCamera(cameraDevice);
    q->connect(control, &QPlatformVideoSource::activeChanged, q, &QCamera::activeChanged);
    q->connect(control, &QPlatformCamera::errorChanged, q, &QCamera::errorChanged);
    q->connect(control, &QPlatformCamera::errorOccurred, q, &QCamera::errorOccurred);
}
//  -----------------------------------------------------------------------

//  QCamera *QCameraPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCamera *ritual_ZN14QCameraPrivate6q_funcEv(QCameraPrivate *self) {
  return self->q_func();
}

//  const QCamera *QCameraPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCamera *ritual_ZNK14QCameraPrivate6q_funcEv(
    const QCameraPrivate *self) {
  return self->q_func();
}

//  void QCameraPrivate::init(const QCameraDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCameraPrivate4initERK13QCameraDevice(
    QCameraPrivate *self,
    const QCameraDevice *device) {
  self->init(*device);
}
