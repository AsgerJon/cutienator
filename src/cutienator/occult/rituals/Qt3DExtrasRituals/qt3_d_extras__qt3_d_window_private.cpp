//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qt3dwindow_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qt3dwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A Qt3DExtras::Qt3DWindowPrivate that Python can take functions over in. Every Qt3DExtras::Qt3DWindowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DExtras_Qt3DWindowPrivateCall0)(const void *, int *);
typedef const QPalette * (*CuteQt3DExtras_Qt3DWindowPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DExtras_Qt3DWindowPrivateCall2)(const void *, bool, int *);
typedef void (*CuteQt3DExtras_Qt3DWindowPrivateCall3)(const void *, int *);
typedef void (*CuteQt3DExtras_Qt3DWindowPrivateCall4)(const void *, int, int, int *);
typedef const QRectF * (*CuteQt3DExtras_Qt3DWindowPrivateCall5)(const void *, const QRectF *, int *);
typedef bool (*CuteQt3DExtras_Qt3DWindowPrivateCall6)(const void *, int *);
typedef bool (*CuteQt3DExtras_Qt3DWindowPrivateCall7)(const void *, int *);
typedef void (*CuteQt3DExtras_Qt3DWindowPrivateCall8)(const void *, QMouseEvent *, int *);
class CuteQt3DExtras_Qt3DWindowPrivate : public Qt3DExtras::Qt3DWindowPrivate {
public:
  using Qt3DExtras::Qt3DWindowPrivate::Qt3DWindowPrivate;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWindowPrivate13eventReceiverEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate13windowPaletteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16clearFocusObjectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate30participatesInLastWindowClosedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate14treatAsVisibleEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  QWindow *QWindowPrivate::eventReceiver()
  QWindow *eventReceiver() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QWindowPrivate::eventReceiver();
  }

  //  QPalette QWindowPrivate::windowPalette() const
  QPalette windowPalette() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall1>(taken[1]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::windowPalette();
  }

  //  void QWindowPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall2 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWindowPrivate::setVisible(visible);
  }

  //  void QWindowPrivate::clearFocusObject()
  void clearFocusObject() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall3 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall4 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall4>(taken[4]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QWindowPrivate::setFocusToTarget(a0, a1);
  }

  //  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
  //      const
  QRectF closestAcceptableGeometry(const QRectF &rect) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall5 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall5>(taken[5]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::closestAcceptableGeometry(rect);
  }

  //  bool QWindowPrivate::participatesInLastWindowClosed() const
  bool participatesInLastWindowClosed() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall6 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::participatesInLastWindowClosed();
  }

  //  bool QWindowPrivate::treatAsVisible() const
  bool treatAsVisible() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall7 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::treatAsVisible();
  }

  //  void QWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
  //      *event)
  void maybeSynthesizeContextMenuEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQt3DExtras_Qt3DWindowPrivateCall8 call = reinterpret_cast<CuteQt3DExtras_Qt3DWindowPrivateCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWindowPrivate::maybeSynthesizeContextMenuEvent(event);
  }
};

//  Qt3DWindow *Qt3DExtras::Qt3DWindowPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::Qt3DWindow *ritual_ZN10Qt3DExtras17Qt3DWindowPrivate6q_funcEv(
    Qt3DExtras::Qt3DWindowPrivate *self) {
  return self->q_func();
}

//  const Qt3DWindow *Qt3DExtras::Qt3DWindowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::Qt3DWindow *ritual_ZNK10Qt3DExtras17Qt3DWindowPrivate6q_funcEv(
    const Qt3DExtras::Qt3DWindowPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_Qt3DWindowPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_Qt3DWindowPrivate(
    Qt3DExtras::Qt3DWindowPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_Qt3DWindowPrivate *>(self)->take(key, call);
}
