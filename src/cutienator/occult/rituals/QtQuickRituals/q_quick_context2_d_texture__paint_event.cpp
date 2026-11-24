//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcontext2dtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickContext2DTexture::PaintEvent that Python can take functions over in. Every QQuickContext2DTexture::PaintEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickContext2DTexture_PaintEventCall0)(const void *, bool, int *);
typedef void * (*CuteQQuickContext2DTexture_PaintEventCall1)(const void *, int *);
class CuteQQuickContext2DTexture_PaintEvent : public QQuickContext2DTexture::PaintEvent {
public:
  using QQuickContext2DTexture::PaintEvent::PaintEvent;
  CuteQQuickContext2DTexture_PaintEvent(const QQuickContext2DTexture::PaintEvent &other) : QQuickContext2DTexture::PaintEvent(other) {}
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
      CuteQQuickContext2DTexture_PaintEventCall0 call = reinterpret_cast<CuteQQuickContext2DTexture_PaintEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContext2DTexture_PaintEventCall1 call = reinterpret_cast<CuteQQuickContext2DTexture_PaintEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QQuickContext2DTexture::PaintEvent::PaintEvent(QQuickContext2DCommandBuff
//      er *b)
extern "C" Q_DECL_EXPORT
QQuickContext2DTexture::PaintEvent *ritual_ZN22QQuickContext2DTexture10PaintEventC1EP28QQuickContext2DCommandBuffer(
    QQuickContext2DCommandBuffer *b) {
  return new CuteQQuickContext2DTexture_PaintEvent(b);
}

//  QQuickContext2DTexture::PaintEvent::~PaintEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickContext2DTexture10PaintEventD1Ev(
    QQuickContext2DTexture::PaintEvent *self) {
  delete self;
}

//  a Python function taken by a CuteQQuickContext2DTexture_PaintEvent, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContext2DTexture_PaintEvent(
    QQuickContext2DTexture::PaintEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContext2DTexture_PaintEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_canvas)
