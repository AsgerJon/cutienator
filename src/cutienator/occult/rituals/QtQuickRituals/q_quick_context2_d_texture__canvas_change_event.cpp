//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QQuickContext2DTexture::CanvasChangeEvent that Python can take functions over in. Every QQuickContext2DTexture::CanvasChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickContext2DTexture_CanvasChangeEventCall0)(const void *, bool, int *);
typedef void * (*CuteQQuickContext2DTexture_CanvasChangeEventCall1)(const void *, int *);
class CuteQQuickContext2DTexture_CanvasChangeEvent : public QQuickContext2DTexture::CanvasChangeEvent {
public:
  using QQuickContext2DTexture::CanvasChangeEvent::CanvasChangeEvent;
  CuteQQuickContext2DTexture_CanvasChangeEvent(const QQuickContext2DTexture::CanvasChangeEvent &other) : QQuickContext2DTexture::CanvasChangeEvent(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContext2DTexture_CanvasChangeEventCall0 call = reinterpret_cast<CuteQQuickContext2DTexture_CanvasChangeEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContext2DTexture_CanvasChangeEventCall1 call = reinterpret_cast<CuteQQuickContext2DTexture_CanvasChangeEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QQuickContext2DTexture::CanvasChangeEvent::CanvasChangeEvent(const QSize
//      &cSize, const QSize &tSize, const QRect &cWindow, const QRect &dRect,
//      bool sm, bool aa)
extern "C" Q_DECL_EXPORT
QQuickContext2DTexture::CanvasChangeEvent *ritual_ZN22QQuickContext2DTexture17CanvasChangeEventC1ERK5QSizeS3_RK5QRectS6_bb(
    const QSize *cSize,
    const QSize *tSize,
    const QRect *cWindow,
    const QRect *dRect,
    bool sm,
    bool aa) {
  return new CuteQQuickContext2DTexture_CanvasChangeEvent(
      *cSize,
      *tSize,
      *cWindow,
      *dRect,
      sm,
      aa);
}

//  QQuickContext2DTexture::CanvasChangeEvent::~CanvasChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture17CanvasChangeEventD1Ev(
    QQuickContext2DTexture::CanvasChangeEvent *self) {
  delete self;
}

//  a Python function taken by a
//      CuteQQuickContext2DTexture_CanvasChangeEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContext2DTexture_CanvasChangeEvent(
    QQuickContext2DTexture::CanvasChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContext2DTexture_CanvasChangeEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_canvas)
#endif  // QT_CONFIG(quick_canvas)
