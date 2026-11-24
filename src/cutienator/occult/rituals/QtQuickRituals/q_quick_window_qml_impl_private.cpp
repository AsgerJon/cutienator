//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwindowmodule_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwindowmodule_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QQuickWindowQmlImplPrivate that Python can take functions over in. Every QQuickWindowQmlImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWindowQmlImplPrivateCall0)(const void *, QQuickPalette *, int *);
typedef void (*CuteQQuickWindowQmlImplPrivateCall1)(const void *, const QPalette *, int *);
typedef void (*CuteQQuickWindowQmlImplPrivateCall2)(const void *, int *);
typedef void (*CuteQQuickWindowQmlImplPrivateCall3)(const void *, int, int, int *);
typedef void (*CuteQQuickWindowQmlImplPrivateCall4)(const void *, QMouseEvent *, int *);
typedef void * (*CuteQQuickWindowQmlImplPrivateCall5)(const void *, int *);
typedef const QPalette * (*CuteQQuickWindowQmlImplPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickWindowQmlImplPrivateCall7)(const void *, bool, int *);
typedef const QRectF * (*CuteQQuickWindowQmlImplPrivateCall8)(const void *, const QRectF *, int *);
typedef bool (*CuteQQuickWindowQmlImplPrivateCall9)(const void *, int *);
typedef bool (*CuteQQuickWindowQmlImplPrivateCall10)(const void *, int *);
class CuteQQuickWindowQmlImplPrivate : public QQuickWindowQmlImplPrivate {
public:
  using QQuickWindowQmlImplPrivate::QQuickWindowQmlImplPrivate;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QPalette")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16clearFocusObjectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate13eventReceiverEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate13windowPaletteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate10setVisibleEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate30participatesInLastWindowClosedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate14treatAsVisibleEv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void QQuickWindowPrivate::setPalette(QQuickPalette *p)
  void setPalette(QQuickPalette *p) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall0 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall0>(taken[0]);
      call(this, p, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::setPalette(p);
  }

  //  void QQuickWindowPrivate::updateChildrenPalettes(const QPalette
  //      &parentPalette)
  void updateChildrenPalettes(const QPalette &parentPalette) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall1 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall1>(taken[1]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::updateChildrenPalettes(parentPalette);
  }

  //  void QQuickWindowPrivate::clearFocusObject()
  void clearFocusObject() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall2 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::clearFocusObject();
  }

  //  void QQuickWindowPrivate::setFocusToTarget(FocusTarget a0,
  //      Qt::FocusReason a1)
  void setFocusToTarget(
      QWindowPrivate::FocusTarget a0,
      Qt::FocusReason a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall3 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall3>(taken[3]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::setFocusToTarget(a0, a1);
  }

  //  void QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
  //      *event)
  void maybeSynthesizeContextMenuEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall4 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(event);
  }

  //  QWindow *QWindowPrivate::eventReceiver()
  QWindow *eventReceiver() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall5 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QWindowPrivate::eventReceiver();
  }

  //  QPalette QWindowPrivate::windowPalette() const
  QPalette windowPalette() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall6 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall6>(taken[6]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::windowPalette();
  }

  //  void QWindowPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall7 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall7>(taken[7]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWindowPrivate::setVisible(visible);
  }

  //  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
  //      const
  QRectF closestAcceptableGeometry(const QRectF &rect) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall8 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall8>(taken[8]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::closestAcceptableGeometry(rect);
  }

  //  bool QWindowPrivate::participatesInLastWindowClosed() const
  bool participatesInLastWindowClosed() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall9 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::participatesInLastWindowClosed();
  }

  //  bool QWindowPrivate::treatAsVisible() const
  bool treatAsVisible() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWindowQmlImplPrivateCall10 call = reinterpret_cast<CuteQQuickWindowQmlImplPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::treatAsVisible();
  }
};

//  QQuickWindowQmlImplPrivate::QQuickWindowQmlImplPrivate()
extern "C" Q_DECL_EXPORT
QQuickWindowQmlImplPrivate *ritual_ZN26QQuickWindowQmlImplPrivateC1Ev() {
  return new CuteQQuickWindowQmlImplPrivate();
}

//  a Python function taken by a CuteQQuickWindowQmlImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWindowQmlImplPrivate(
    QQuickWindowQmlImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWindowQmlImplPrivate *>(self)->take(key, call);
}
