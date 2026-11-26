//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(splitter)
#if QT_CONFIG(splitter)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(splitter)
#include <QtWidgets/qsplitter.h>
#endif
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>

//  A QSplitterHandlePrivate that Python can take functions over in. Every QSplitterHandlePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSplitterHandlePrivateCall0)(const void *, bool, int *);
typedef void (*CuteQSplitterHandlePrivateCall1)(const void *, int, int *);
typedef void (*CuteQSplitterHandlePrivateCall2)(const void *, int *);
typedef void (*CuteQSplitterHandlePrivateCall3)(const void *, int *);
typedef void * (*CuteQSplitterHandlePrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQSplitterHandlePrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQSplitterHandlePrivateCall6)(const void *, int *);
typedef int (*CuteQSplitterHandlePrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQSplitterHandlePrivateCall8)(const void *, int *);
typedef void (*CuteQSplitterHandlePrivateCall9)(const void *, int *);
typedef void (*CuteQSplitterHandlePrivateCall10)(const void *, int *);
typedef void (*CuteQSplitterHandlePrivateCall11)(const void *, int *);
typedef void (*CuteQSplitterHandlePrivateCall12)(const void *, int *);
typedef void (*CuteQSplitterHandlePrivateCall13)(const void *, int *);
typedef void (*CuteQSplitterHandlePrivateCall14)(const void *, int *);
typedef void (*CuteQSplitterHandlePrivateCall15)(const void *, int *);
typedef bool (*CuteQSplitterHandlePrivateCall16)(const void *, int *);
typedef bool (*CuteQSplitterHandlePrivateCall17)(const void *, int *);
class CuteQSplitterHandlePrivate : public QSplitterHandlePrivate {
public:
  using QSplitterHandlePrivate::QSplitterHandlePrivate;
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
      CuteQSplitterHandlePrivateCall0 call = reinterpret_cast<CuteQSplitterHandlePrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall1 call = reinterpret_cast<CuteQSplitterHandlePrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall2 call = reinterpret_cast<CuteQSplitterHandlePrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall3 call = reinterpret_cast<CuteQSplitterHandlePrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall4 call = reinterpret_cast<CuteQSplitterHandlePrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall5 call = reinterpret_cast<CuteQSplitterHandlePrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall6 call = reinterpret_cast<CuteQSplitterHandlePrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall7 call = reinterpret_cast<CuteQSplitterHandlePrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall8 call = reinterpret_cast<CuteQSplitterHandlePrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall9 call = reinterpret_cast<CuteQSplitterHandlePrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall10 call = reinterpret_cast<CuteQSplitterHandlePrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall11 call = reinterpret_cast<CuteQSplitterHandlePrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall12 call = reinterpret_cast<CuteQSplitterHandlePrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall13 call = reinterpret_cast<CuteQSplitterHandlePrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall14 call = reinterpret_cast<CuteQSplitterHandlePrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall15 call = reinterpret_cast<CuteQSplitterHandlePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall16 call = reinterpret_cast<CuteQSplitterHandlePrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQSplitterHandlePrivateCall17 call = reinterpret_cast<CuteQSplitterHandlePrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QSplitterHandle *QSplitterHandlePrivate::q_func()
extern "C" Q_DECL_EXPORT
QSplitterHandle *ritual_ZN22QSplitterHandlePrivate6q_funcEv(
    QSplitterHandlePrivate *self) {
  return self->q_func();
}

//  const QSplitterHandle *QSplitterHandlePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSplitterHandle *ritual_ZNK22QSplitterHandlePrivate6q_funcEv(
    const QSplitterHandlePrivate *self) {
  return self->q_func();
}

//  QSplitterHandlePrivate::QSplitterHandlePrivate()
extern "C" Q_DECL_EXPORT
QSplitterHandlePrivate *ritual_ZN22QSplitterHandlePrivateC1Ev() {
  return new CuteQSplitterHandlePrivate();
}

//  int QSplitterHandlePrivate::pick(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QSplitterHandlePrivate4pickERK6QPoint(
    const QSplitterHandlePrivate *self,
    const QPoint *pos) {
  return self->pick(*pos);
}

//  a Python function taken by a CuteQSplitterHandlePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSplitterHandlePrivate(
    QSplitterHandlePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSplitterHandlePrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(splitter)
#endif  // QT_CONFIG(splitter)
