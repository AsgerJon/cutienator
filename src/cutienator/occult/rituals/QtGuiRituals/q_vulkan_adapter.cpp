//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: everything after the global includes
//  stands also under '__has_include(<vulkan/vulkan.h>)', the check Qt's
//  'qvulkaninstance.h' makes, because without Vulkan's headers Qt
//  declares none of the Vulkan types ('VkBuffer' and the rest) that
//  'qrhivulkan_p.h' uses. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhivulkan_p.h>
#include <QtGui/qpa/qplatformvulkaninstance.h>
#include <QtCore/qmath.h>
#include <QtGui/qwindow.h>
#include <QtGui/private/qvulkandefaultinstance_p.h>
#include <QtCore/q20memory.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhivulkan.cpp, line 1285, as _ZNK14QVulkanAdapter4infoEv
inline QRhiDriverInfo QVulkanAdapter::info() const
{
    return adapterInfo;
}
//  -----------------------------------------------------------------------

//  A QVulkanAdapter that Python can take functions over in. Every QVulkanAdapter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRhiDriverInfo * (*CuteQVulkanAdapterCall0)(const void *, int *);
class CuteQVulkanAdapter : public QVulkanAdapter {
public:
  using QVulkanAdapter::QVulkanAdapter;
  CuteQVulkanAdapter(const QVulkanAdapter &other) : QVulkanAdapter(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QRhiAdapter4infoEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QRhiDriverInfo QVulkanAdapter::info() const
  QRhiDriverInfo info() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQVulkanAdapterCall0 call = reinterpret_cast<CuteQVulkanAdapterCall0>(taken[0]);
      const QRhiDriverInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QVulkanAdapter::info();
  }
};

//  QRhiDriverInfo QVulkanAdapter::info() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK14QVulkanAdapter4infoEv(
    const QVulkanAdapter *self) {
  return new QRhiDriverInfo(self->info());
}

//  QVulkanAdapter::~QVulkanAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QVulkanAdapterD1Ev(QVulkanAdapter *self) {
  delete self;
}

//  a Python function taken by a CuteQVulkanAdapter, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVulkanAdapter(
    QVulkanAdapter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVulkanAdapter *>(self)->take(key, call);
}

//  QRhiDriverInfo QVulkanAdapter::info() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_own_ZNK14QVulkanAdapter4infoEv(
    const QVulkanAdapter *self) {
  return new QRhiDriverInfo(self->QVulkanAdapter::info());
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
