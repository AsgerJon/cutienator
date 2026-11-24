//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolumnviewgrip_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcolumnviewgrip_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qcolumnviewgrip_p.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qpainter.h>
#include <QtGui/qbrush.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qcolumnviewgrip.cpp, line 146, as _ZN22QColumnViewGripPrivateC1Ev
inline QColumnViewGripPrivate::QColumnViewGripPrivate()
:  QWidgetPrivate(),
originalXLocation(-1)
{
}
//  -----------------------------------------------------------------------

//  A QColumnViewGripPrivate that Python can take functions over in. Every QColumnViewGripPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQColumnViewGripPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQColumnViewGripPrivateCall1)(const void *, int, int *);
typedef void (*CuteQColumnViewGripPrivateCall2)(const void *, int *);
typedef void (*CuteQColumnViewGripPrivateCall3)(const void *, int *);
typedef void * (*CuteQColumnViewGripPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQColumnViewGripPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQColumnViewGripPrivateCall6)(const void *, int *);
typedef int (*CuteQColumnViewGripPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQColumnViewGripPrivateCall8)(const void *, int *);
typedef void (*CuteQColumnViewGripPrivateCall9)(const void *, int *);
typedef void (*CuteQColumnViewGripPrivateCall10)(const void *, int *);
typedef void (*CuteQColumnViewGripPrivateCall11)(const void *, int *);
typedef void (*CuteQColumnViewGripPrivateCall12)(const void *, int *);
typedef void (*CuteQColumnViewGripPrivateCall13)(const void *, int *);
typedef void (*CuteQColumnViewGripPrivateCall14)(const void *, int *);
typedef void (*CuteQColumnViewGripPrivateCall15)(const void *, int *);
typedef bool (*CuteQColumnViewGripPrivateCall16)(const void *, int *);
typedef bool (*CuteQColumnViewGripPrivateCall17)(const void *, int *);
class CuteQColumnViewGripPrivate : public QColumnViewGripPrivate {
public:
  using QColumnViewGripPrivate::QColumnViewGripPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall0 call = reinterpret_cast<CuteQColumnViewGripPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall1 call = reinterpret_cast<CuteQColumnViewGripPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall2 call = reinterpret_cast<CuteQColumnViewGripPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall3 call = reinterpret_cast<CuteQColumnViewGripPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall4 call = reinterpret_cast<CuteQColumnViewGripPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall5 call = reinterpret_cast<CuteQColumnViewGripPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall6 call = reinterpret_cast<CuteQColumnViewGripPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall7 call = reinterpret_cast<CuteQColumnViewGripPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall8 call = reinterpret_cast<CuteQColumnViewGripPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall9 call = reinterpret_cast<CuteQColumnViewGripPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall10 call = reinterpret_cast<CuteQColumnViewGripPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall11 call = reinterpret_cast<CuteQColumnViewGripPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall12 call = reinterpret_cast<CuteQColumnViewGripPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall13 call = reinterpret_cast<CuteQColumnViewGripPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall14 call = reinterpret_cast<CuteQColumnViewGripPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall15 call = reinterpret_cast<CuteQColumnViewGripPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall16 call = reinterpret_cast<CuteQColumnViewGripPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQColumnViewGripPrivateCall17 call = reinterpret_cast<CuteQColumnViewGripPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QColumnViewGrip *QColumnViewGripPrivate::q_func()
extern "C" Q_DECL_EXPORT
QColumnViewGrip *ritual_ZN22QColumnViewGripPrivate6q_funcEv(
    QColumnViewGripPrivate *self) {
  return self->q_func();
}

//  const QColumnViewGrip *QColumnViewGripPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QColumnViewGrip *ritual_ZNK22QColumnViewGripPrivate6q_funcEv(
    const QColumnViewGripPrivate *self) {
  return self->q_func();
}

//  QColumnViewGripPrivate::QColumnViewGripPrivate()
extern "C" Q_DECL_EXPORT
QColumnViewGripPrivate *ritual_ZN22QColumnViewGripPrivateC1Ev() {
  return new CuteQColumnViewGripPrivate();
}

//  QColumnViewGripPrivate::~QColumnViewGripPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QColumnViewGripPrivateD1Ev(QColumnViewGripPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQColumnViewGripPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QColumnViewGripPrivate(
    QColumnViewGripPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQColumnViewGripPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(columnview)
