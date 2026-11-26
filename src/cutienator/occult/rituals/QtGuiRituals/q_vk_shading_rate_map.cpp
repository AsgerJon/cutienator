//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file now also asks
//  '__has_include(<vulkan/vulkan.h>)', as Qt's 'qvulkaninstance.h'
//  does: 'qrhivulkan_p.h' needs 'vulkan/vulkan.h' of Vulkan, outside
//  Qt, which a machine may lack although its Qt has Vulkan. Kept as it
//  is when the generator runs again.
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

//  from src/gui/rhi/qrhivulkan.cpp, line 8141, as _ZN17QVkShadingRateMapC1EP18QRhiImplementation
inline QVkShadingRateMap::QVkShadingRateMap(QRhiImplementation *rhi)
    : QRhiShadingRateMap(rhi)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8146, as _ZN17QVkShadingRateMapD1Ev
inline QVkShadingRateMap::~QVkShadingRateMap()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8151, as _ZN17QVkShadingRateMap7destroyEv
inline void QVkShadingRateMap::destroy()
{
    if (!texture)
        return;

    texture = nullptr;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8159, as _ZN17QVkShadingRateMap10createFromEP11QRhiTexture
inline bool QVkShadingRateMap::createFrom(QRhiTexture *src)
{
    if (texture)
        destroy();

    texture = QRHI_RES(QVkTexture, src);

    return true;
}
//  -----------------------------------------------------------------------

//  A QVkShadingRateMap that Python can take functions over in. Every QVkShadingRateMap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkShadingRateMapCall0)(const void *, int *);
typedef bool (*CuteQVkShadingRateMapCall1)(const void *, QRhiTexture *, int *);
typedef int (*CuteQVkShadingRateMapCall2)(const void *, int *);
typedef bool (*CuteQVkShadingRateMapCall3)(const void *, const QRhiShadingRateMap::NativeShadingRateMap *, int *);
class CuteQVkShadingRateMap : public QVkShadingRateMap {
public:
  using QVkShadingRateMap::QVkShadingRateMap;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiShadingRateMap10createFromEP11QRhiTexture")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiShadingRateMap10createFromENS_20NativeShadingRateMapE")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QVkShadingRateMap::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkShadingRateMapCall0 call = reinterpret_cast<CuteQVkShadingRateMapCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkShadingRateMap::destroy();
  }

  //  bool QVkShadingRateMap::createFrom(QRhiTexture *src)
  bool createFrom(QRhiTexture *src) override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkShadingRateMapCall1 call = reinterpret_cast<CuteQVkShadingRateMapCall1>(taken[1]);
      bool given = call(this, src, &handled);
      if (handled) return given;
    }
    return QVkShadingRateMap::createFrom(src);
  }

  //  QRhiResource::Type QRhiShadingRateMap::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkShadingRateMapCall2 call = reinterpret_cast<CuteQVkShadingRateMapCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiShadingRateMap::resourceType();
  }

  //  bool QRhiShadingRateMap::createFrom(NativeShadingRateMap src)
  bool createFrom(QRhiShadingRateMap::NativeShadingRateMap src) override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkShadingRateMapCall3 call = reinterpret_cast<CuteQVkShadingRateMapCall3>(taken[3]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QRhiShadingRateMap::createFrom(src);
  }
};

//  QVkShadingRateMap::QVkShadingRateMap(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QVkShadingRateMap *ritual_ZN17QVkShadingRateMapC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQVkShadingRateMap(rhi);
}

//  QVkShadingRateMap::~QVkShadingRateMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVkShadingRateMapD1Ev(QVkShadingRateMap *self) {
  delete self;
}

//  void QVkShadingRateMap::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QVkShadingRateMap7destroyEv(QVkShadingRateMap *self) {
  self->destroy();
}

//  bool QVkShadingRateMap::createFrom(QRhiTexture *src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QVkShadingRateMap10createFromEP11QRhiTexture(
    QVkShadingRateMap *self,
    QRhiTexture *src) {
  return self->createFrom(src);
}

//  a Python function taken by a CuteQVkShadingRateMap, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkShadingRateMap(
    QVkShadingRateMap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkShadingRateMap *>(self)->take(key, call);
}

//  void QVkShadingRateMap::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QVkShadingRateMap7destroyEv(QVkShadingRateMap *self) {
  self->QVkShadingRateMap::destroy();
}

//  bool QVkShadingRateMap::createFrom(QRhiTexture *src)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QVkShadingRateMap10createFromEP11QRhiTexture(
    QVkShadingRateMap *self,
    QRhiTexture *src) {
  return self->QVkShadingRateMap::createFrom(src);
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
