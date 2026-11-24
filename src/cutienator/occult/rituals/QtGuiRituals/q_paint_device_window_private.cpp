//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintdevicewindow_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qpaintdevicewindow.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintdevicewindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtGui/qpalette.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QPaintDeviceWindowPrivate that Python can take functions over in. Every QPaintDeviceWindowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPaintDeviceWindowPrivateCall0)(const void *, int *);
typedef void (*CuteQPaintDeviceWindowPrivateCall1)(const void *, const QRegion *, int *);
typedef void (*CuteQPaintDeviceWindowPrivateCall2)(const void *, int *);
typedef void (*CuteQPaintDeviceWindowPrivateCall3)(const void *, const QRegion *, int *);
typedef void * (*CuteQPaintDeviceWindowPrivateCall4)(const void *, int *);
typedef const QPalette * (*CuteQPaintDeviceWindowPrivateCall5)(const void *, int *);
typedef void (*CuteQPaintDeviceWindowPrivateCall6)(const void *, bool, int *);
typedef void (*CuteQPaintDeviceWindowPrivateCall7)(const void *, int *);
typedef void (*CuteQPaintDeviceWindowPrivateCall8)(const void *, int, int, int *);
typedef const QRectF * (*CuteQPaintDeviceWindowPrivateCall9)(const void *, const QRectF *, int *);
typedef bool (*CuteQPaintDeviceWindowPrivateCall10)(const void *, int *);
typedef bool (*CuteQPaintDeviceWindowPrivateCall11)(const void *, int *);
typedef void (*CuteQPaintDeviceWindowPrivateCall12)(const void *, QMouseEvent *, int *);
class CuteQPaintDeviceWindowPrivate : public QPaintDeviceWindowPrivate {
public:
  using QPaintDeviceWindowPrivate::QPaintDeviceWindowPrivate;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QPaintDeviceWindowPrivate17handleResizeEventEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPaintDeviceWindowPrivate10beginPaintERK7QRegion")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPaintDeviceWindowPrivate8endPaintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QPaintDeviceWindowPrivate5flushERK7QRegion")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate13eventReceiverEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate13windowPaletteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate10setVisibleEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16clearFocusObjectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate30participatesInLastWindowClosedEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate14treatAsVisibleEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  void QPaintDeviceWindowPrivate::handleResizeEvent()
  void handleResizeEvent() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall0 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintDeviceWindowPrivate::handleResizeEvent();
  }

  //  void QPaintDeviceWindowPrivate::beginPaint(const QRegion &region)
  void beginPaint(const QRegion &region) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall1 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall1>(taken[1]);
      call(this, &region, &handled);
      if (handled) return;
    }
    QPaintDeviceWindowPrivate::beginPaint(region);
  }

  //  void QPaintDeviceWindowPrivate::endPaint()
  void endPaint() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall2 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintDeviceWindowPrivate::endPaint();
  }

  //  void QPaintDeviceWindowPrivate::flush(const QRegion &region)
  void flush(const QRegion &region) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall3 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall3>(taken[3]);
      call(this, &region, &handled);
      if (handled) return;
    }
    QPaintDeviceWindowPrivate::flush(region);
  }

  //  QWindow *QWindowPrivate::eventReceiver()
  QWindow *eventReceiver() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall4 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QWindowPrivate::eventReceiver();
  }

  //  QPalette QWindowPrivate::windowPalette() const
  QPalette windowPalette() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall5 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall5>(taken[5]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::windowPalette();
  }

  //  void QWindowPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall6 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall6>(taken[6]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWindowPrivate::setVisible(visible);
  }

  //  void QWindowPrivate::clearFocusObject()
  void clearFocusObject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall7 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowPrivate::clearFocusObject();
  }

  //  void QWindowPrivate::setFocusToTarget(FocusTarget a0, Qt::FocusReason
  //      a1)
  void setFocusToTarget(
      QWindowPrivate::FocusTarget a0,
      Qt::FocusReason a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall8 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall8>(taken[8]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QWindowPrivate::setFocusToTarget(a0, a1);
  }

  //  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
  //      const
  QRectF closestAcceptableGeometry(const QRectF &rect) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall9 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall9>(taken[9]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::closestAcceptableGeometry(rect);
  }

  //  bool QWindowPrivate::participatesInLastWindowClosed() const
  bool participatesInLastWindowClosed() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall10 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::participatesInLastWindowClosed();
  }

  //  bool QWindowPrivate::treatAsVisible() const
  bool treatAsVisible() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall11 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::treatAsVisible();
  }

  //  void QWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
  //      *event)
  void maybeSynthesizeContextMenuEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPaintDeviceWindowPrivateCall12 call = reinterpret_cast<CuteQPaintDeviceWindowPrivateCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWindowPrivate::maybeSynthesizeContextMenuEvent(event);
  }
};

//  QPaintDeviceWindow *QPaintDeviceWindowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPaintDeviceWindow *ritual_ZN25QPaintDeviceWindowPrivate6q_funcEv(
    QPaintDeviceWindowPrivate *self) {
  return self->q_func();
}

//  const QPaintDeviceWindow *QPaintDeviceWindowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPaintDeviceWindow *ritual_ZNK25QPaintDeviceWindowPrivate6q_funcEv(
    const QPaintDeviceWindowPrivate *self) {
  return self->q_func();
}

//  QPaintDeviceWindowPrivate::QPaintDeviceWindowPrivate()
extern "C" Q_DECL_EXPORT
QPaintDeviceWindowPrivate *ritual_ZN25QPaintDeviceWindowPrivateC1Ev() {
  return new CuteQPaintDeviceWindowPrivate();
}

//  QPaintDeviceWindowPrivate::~QPaintDeviceWindowPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPaintDeviceWindowPrivateD1Ev(
    QPaintDeviceWindowPrivate *self) {
  delete self;
}

//  void QPaintDeviceWindowPrivate::handleResizeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPaintDeviceWindowPrivate17handleResizeEventEv(
    QPaintDeviceWindowPrivate *self) {
  self->handleResizeEvent();
}

//  void QPaintDeviceWindowPrivate::beginPaint(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPaintDeviceWindowPrivate10beginPaintERK7QRegion(
    QPaintDeviceWindowPrivate *self,
    const QRegion *region) {
  self->beginPaint(*region);
}

//  void QPaintDeviceWindowPrivate::endPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPaintDeviceWindowPrivate8endPaintEv(
    QPaintDeviceWindowPrivate *self) {
  self->endPaint();
}

//  void QPaintDeviceWindowPrivate::flush(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPaintDeviceWindowPrivate5flushERK7QRegion(
    QPaintDeviceWindowPrivate *self,
    const QRegion *region) {
  self->flush(*region);
}

//  bool QPaintDeviceWindowPrivate::paint(const QRegion &region)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QPaintDeviceWindowPrivate5paintERK7QRegion(
    QPaintDeviceWindowPrivate *self,
    const QRegion *region) {
  return self->paint(*region);
}

//  void QPaintDeviceWindowPrivate::doFlush(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPaintDeviceWindowPrivate7doFlushERK7QRegion(
    QPaintDeviceWindowPrivate *self,
    const QRegion *region) {
  self->doFlush(*region);
}

//  void QPaintDeviceWindowPrivate::handleUpdateEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPaintDeviceWindowPrivate17handleUpdateEventEv(
    QPaintDeviceWindowPrivate *self) {
  self->handleUpdateEvent();
}

//  void QPaintDeviceWindowPrivate::markWindowAsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPaintDeviceWindowPrivate17markWindowAsDirtyEv(
    QPaintDeviceWindowPrivate *self) {
  self->markWindowAsDirty();
}

//  a Python function taken by a CuteQPaintDeviceWindowPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPaintDeviceWindowPrivate(
    QPaintDeviceWindowPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPaintDeviceWindowPrivate *>(self)->take(key, call);
}

//  void QPaintDeviceWindowPrivate::handleResizeEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QPaintDeviceWindowPrivate17handleResizeEventEv(
    QPaintDeviceWindowPrivate *self) {
  self->QPaintDeviceWindowPrivate::handleResizeEvent();
}

//  void QPaintDeviceWindowPrivate::beginPaint(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QPaintDeviceWindowPrivate10beginPaintERK7QRegion(
    QPaintDeviceWindowPrivate *self,
    const QRegion *region) {
  self->QPaintDeviceWindowPrivate::beginPaint(*region);
}

//  void QPaintDeviceWindowPrivate::endPaint()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QPaintDeviceWindowPrivate8endPaintEv(
    QPaintDeviceWindowPrivate *self) {
  self->QPaintDeviceWindowPrivate::endPaint();
}

//  void QPaintDeviceWindowPrivate::flush(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QPaintDeviceWindowPrivate5flushERK7QRegion(
    QPaintDeviceWindowPrivate *self,
    const QRegion *region) {
  self->QPaintDeviceWindowPrivate::flush(*region);
}
