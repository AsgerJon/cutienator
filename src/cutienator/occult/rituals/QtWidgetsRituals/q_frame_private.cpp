//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qframe_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qframe.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qframe.h>
#include <QtGui/qbitmap.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qframe.cpp, line 19, as _ZN13QFramePrivateC1Ev
inline QFramePrivate::QFramePrivate()
    : frect(0, 0, 0, 0),
      frameStyle(QFrame::NoFrame | QFrame::Plain),
      lineWidth(1),
      midLineWidth(0),
      frameWidth(0),
      leftFrameWidth(0), rightFrameWidth(0),
      topFrameWidth(0), bottomFrameWidth(0)
{
}

//  from src/widgets/widgets/qframe.cpp, line 30, as _ZN13QFramePrivateD1Ev
inline QFramePrivate::~QFramePrivate()
{
}

//  from src/widgets/widgets/qframe.cpp, line 406, as _ZN13QFramePrivate16updateFrameWidthEv
inline void QFramePrivate::updateFrameWidth()
{
    Q_Q(QFrame);
    QRect fr = q->frameRect();
    updateStyledFrameWidths();
    q->setFrameRect(fr);
    setLayoutItemMargins(QStyle::SE_FrameLayoutItem);
}

//  from src/widgets/widgets/qframe.cpp, line 386, as _ZN13QFramePrivate23updateStyledFrameWidthsEv
inline void QFramePrivate::updateStyledFrameWidths()
{
    Q_Q(const QFrame);
    QStyleOptionFrame opt;
    q->initStyleOption(&opt);

    QRect cr = q->style()->subElementRect(QStyle::SE_ShapedFrameContents, &opt, q);
    leftFrameWidth = cr.left() - opt.rect.left();
    topFrameWidth = cr.top() - opt.rect.top();
    rightFrameWidth = opt.rect.right() - cr.right(),
    bottomFrameWidth = opt.rect.bottom() - cr.bottom();
    frameWidth = qMax(qMax(leftFrameWidth, rightFrameWidth),
                      qMax(topFrameWidth, bottomFrameWidth));
}

//  from src/widgets/widgets/qframe.cpp, line 34, as _ZN13QFramePrivate4initEv
inline void QFramePrivate::init()
{
    Q_Q(QFrame);
    setLayoutItemMargins(QStyle::SE_FrameLayoutItem);

    // The frameRect property is implemented in terms of the widget's
    // contentsRect, which conflicts with the implicit inclusion of
    // the safe area margins in the contentsRect.
    q->setAttribute(Qt::WA_ContentsMarginsRespectsSafeArea, false);
}
//  -----------------------------------------------------------------------

//  A QFramePrivate that Python can take functions over in. Every QFramePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQFramePrivateCall0)(const void *, bool, int *);
typedef void (*CuteQFramePrivateCall1)(const void *, int, int *);
typedef void (*CuteQFramePrivateCall2)(const void *, int *);
typedef void (*CuteQFramePrivateCall3)(const void *, int *);
typedef void * (*CuteQFramePrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQFramePrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQFramePrivateCall6)(const void *, int *);
typedef int (*CuteQFramePrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQFramePrivateCall8)(const void *, int *);
typedef void (*CuteQFramePrivateCall9)(const void *, int *);
typedef void (*CuteQFramePrivateCall10)(const void *, int *);
typedef void (*CuteQFramePrivateCall11)(const void *, int *);
typedef void (*CuteQFramePrivateCall12)(const void *, int *);
typedef void (*CuteQFramePrivateCall13)(const void *, int *);
typedef void (*CuteQFramePrivateCall14)(const void *, int *);
typedef void (*CuteQFramePrivateCall15)(const void *, int *);
typedef bool (*CuteQFramePrivateCall16)(const void *, int *);
typedef bool (*CuteQFramePrivateCall17)(const void *, int *);
class CuteQFramePrivate : public QFramePrivate {
public:
  using QFramePrivate::QFramePrivate;
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
      CuteQFramePrivateCall0 call = reinterpret_cast<CuteQFramePrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFramePrivateCall1 call = reinterpret_cast<CuteQFramePrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQFramePrivateCall2 call = reinterpret_cast<CuteQFramePrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQFramePrivateCall3 call = reinterpret_cast<CuteQFramePrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQFramePrivateCall4 call = reinterpret_cast<CuteQFramePrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFramePrivateCall5 call = reinterpret_cast<CuteQFramePrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFramePrivateCall6 call = reinterpret_cast<CuteQFramePrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQFramePrivateCall7 call = reinterpret_cast<CuteQFramePrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQFramePrivateCall8 call = reinterpret_cast<CuteQFramePrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQFramePrivateCall9 call = reinterpret_cast<CuteQFramePrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQFramePrivateCall10 call = reinterpret_cast<CuteQFramePrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQFramePrivateCall11 call = reinterpret_cast<CuteQFramePrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQFramePrivateCall12 call = reinterpret_cast<CuteQFramePrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQFramePrivateCall13 call = reinterpret_cast<CuteQFramePrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQFramePrivateCall14 call = reinterpret_cast<CuteQFramePrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQFramePrivateCall15 call = reinterpret_cast<CuteQFramePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQFramePrivateCall16 call = reinterpret_cast<CuteQFramePrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQFramePrivateCall17 call = reinterpret_cast<CuteQFramePrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QFrame *QFramePrivate::q_func()
extern "C" Q_DECL_EXPORT
QFrame *ritual_ZN13QFramePrivate6q_funcEv(QFramePrivate *self) {
  return self->q_func();
}

//  const QFrame *QFramePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFrame *ritual_ZNK13QFramePrivate6q_funcEv(const QFramePrivate *self) {
  return self->q_func();
}

//  QFramePrivate::QFramePrivate()
extern "C" Q_DECL_EXPORT
QFramePrivate *ritual_ZN13QFramePrivateC1Ev() {
  return new CuteQFramePrivate();
}

//  QFramePrivate::~QFramePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFramePrivateD1Ev(QFramePrivate *self) {
  delete self;
}

//  void QFramePrivate::updateFrameWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFramePrivate16updateFrameWidthEv(QFramePrivate *self) {
  self->updateFrameWidth();
}

//  void QFramePrivate::updateStyledFrameWidths()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFramePrivate23updateStyledFrameWidthsEv(
    QFramePrivate *self) {
  self->updateStyledFrameWidths();
}

//  void QFramePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFramePrivate4initEv(QFramePrivate *self) {
  self->init();
}

//  a Python function taken by a CuteQFramePrivate, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFramePrivate(
    QFramePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFramePrivate *>(self)->take(key, call);
}
