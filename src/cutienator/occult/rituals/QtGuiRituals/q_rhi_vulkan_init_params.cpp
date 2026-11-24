//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi_platform.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi_platform.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QByteArrayList QRhiVulkanInitParams::preferredInstanceExtensions()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN20QRhiVulkanInitParams27preferredInstanceExtensionsEv() {
  return new QList<QByteArray>(
      QRhiVulkanInitParams::preferredInstanceExtensions());
}

//  QByteArrayList
//      QRhiVulkanInitParams::preferredExtensionsForImportedDevice()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN20QRhiVulkanInitParams36preferredExtensionsForImportedDeviceEv() {
  return new QList<QByteArray>(
      QRhiVulkanInitParams::preferredExtensionsForImportedDevice());
}

//  QRhiVulkanInitParams::~QRhiVulkanInitParams()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiVulkanInitParamsD1Ev(QRhiVulkanInitParams *self) {
  delete self;
}

#endif  // (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || defined(Q_QDOC)
