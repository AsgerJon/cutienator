//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickViewPrivate that Python can take functions over in. Every QQuickViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickViewPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickViewPrivateCall1)(const void *, QQuickPalette *, int *);
typedef void (*CuteQQuickViewPrivateCall2)(const void *, const QPalette *, int *);
typedef void (*CuteQQuickViewPrivateCall3)(const void *, int *);
typedef void (*CuteQQuickViewPrivateCall4)(const void *, int, int, int *);
typedef void (*CuteQQuickViewPrivateCall5)(const void *, QMouseEvent *, int *);
typedef void * (*CuteQQuickViewPrivateCall6)(const void *, int *);
typedef const QPalette * (*CuteQQuickViewPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickViewPrivateCall8)(const void *, bool, int *);
typedef const QRectF * (*CuteQQuickViewPrivateCall9)(const void *, const QRectF *, int *);
typedef bool (*CuteQQuickViewPrivateCall10)(const void *, int *);
typedef bool (*CuteQQuickViewPrivateCall11)(const void *, int *);
class CuteQQuickViewPrivate : public QQuickViewPrivate {
public:
  using QQuickViewPrivate::QQuickViewPrivate;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickViewPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QPalette")) {
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
    if (!std::strcmp(key, "_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate13eventReceiverEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate13windowPaletteEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate10setVisibleEb")) {
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
    return false;
  }

  //  void QQuickViewPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickViewPrivateCall0 call = reinterpret_cast<CuteQQuickViewPrivateCall0>(taken[0]);
      call(this, item, &change, &a2, &handled);
      if (handled) return;
    }
    QQuickViewPrivate::itemGeometryChanged(item, change, a2);
  }

  //  void QQuickWindowPrivate::setPalette(QQuickPalette *p)
  void setPalette(QQuickPalette *p) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickViewPrivateCall1 call = reinterpret_cast<CuteQQuickViewPrivateCall1>(taken[1]);
      call(this, p, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::setPalette(p);
  }

  //  void QQuickWindowPrivate::updateChildrenPalettes(const QPalette
  //      &parentPalette)
  void updateChildrenPalettes(const QPalette &parentPalette) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickViewPrivateCall2 call = reinterpret_cast<CuteQQuickViewPrivateCall2>(taken[2]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::updateChildrenPalettes(parentPalette);
  }

  //  void QQuickWindowPrivate::clearFocusObject()
  void clearFocusObject() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickViewPrivateCall3 call = reinterpret_cast<CuteQQuickViewPrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQQuickViewPrivateCall4 call = reinterpret_cast<CuteQQuickViewPrivateCall4>(taken[4]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::setFocusToTarget(a0, a1);
  }

  //  void QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
  //      *event)
  void maybeSynthesizeContextMenuEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickViewPrivateCall5 call = reinterpret_cast<CuteQQuickViewPrivateCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(event);
  }

  //  QWindow *QWindowPrivate::eventReceiver()
  QWindow *eventReceiver() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickViewPrivateCall6 call = reinterpret_cast<CuteQQuickViewPrivateCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QWindowPrivate::eventReceiver();
  }

  //  QPalette QWindowPrivate::windowPalette() const
  QPalette windowPalette() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickViewPrivateCall7 call = reinterpret_cast<CuteQQuickViewPrivateCall7>(taken[7]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::windowPalette();
  }

  //  void QWindowPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickViewPrivateCall8 call = reinterpret_cast<CuteQQuickViewPrivateCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWindowPrivate::setVisible(visible);
  }

  //  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
  //      const
  QRectF closestAcceptableGeometry(const QRectF &rect) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickViewPrivateCall9 call = reinterpret_cast<CuteQQuickViewPrivateCall9>(taken[9]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::closestAcceptableGeometry(rect);
  }

  //  bool QWindowPrivate::participatesInLastWindowClosed() const
  bool participatesInLastWindowClosed() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickViewPrivateCall10 call = reinterpret_cast<CuteQQuickViewPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::participatesInLastWindowClosed();
  }

  //  bool QWindowPrivate::treatAsVisible() const
  bool treatAsVisible() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickViewPrivateCall11 call = reinterpret_cast<CuteQQuickViewPrivateCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::treatAsVisible();
  }
};

//  QQuickView *QQuickViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickView *ritual_ZN17QQuickViewPrivate6q_funcEv(QQuickViewPrivate *self) {
  return self->q_func();
}

//  const QQuickView *QQuickViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickView *ritual_ZNK17QQuickViewPrivate6q_funcEv(
    const QQuickViewPrivate *self) {
  return self->q_func();
}

//  QQuickViewPrivate *QQuickViewPrivate::get(QQuickView *view)
extern "C" Q_DECL_EXPORT
QQuickViewPrivate *ritual_ZN17QQuickViewPrivate3getEP10QQuickView(
    QQuickView *view) {
  return QQuickViewPrivate::get(view);
}

//  const QQuickViewPrivate *QQuickViewPrivate::get(const QQuickView *view)
extern "C" Q_DECL_EXPORT
const QQuickViewPrivate *ritual_ZN17QQuickViewPrivate3getEPK10QQuickView(
    const QQuickView *view) {
  return QQuickViewPrivate::get(view);
}

//  QQuickViewPrivate::QQuickViewPrivate()
extern "C" Q_DECL_EXPORT
QQuickViewPrivate *ritual_ZN17QQuickViewPrivateC1Ev() {
  return new CuteQQuickViewPrivate();
}

//  QQuickViewPrivate::~QQuickViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewPrivateD1Ev(QQuickViewPrivate *self) {
  delete self;
}

//  ExecuteState QQuickViewPrivate::executeHelper()
extern "C" Q_DECL_EXPORT
QQuickViewPrivate::ExecuteState ritual_ZN17QQuickViewPrivate13executeHelperEv(
    QQuickViewPrivate *self) {
  return self->executeHelper();
}

//  void QQuickViewPrivate::execute()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewPrivate7executeEv(QQuickViewPrivate *self) {
  self->execute();
}

//  void QQuickViewPrivate::execute(QAnyStringView uri, QAnyStringView
//      typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewPrivate7executeE14QAnyStringViewS0_(
    QQuickViewPrivate *self,
    const QString *uri,
    const QString *typeName) {
  self->execute(QAnyStringView(*uri), QAnyStringView(*typeName));
}

//  void QQuickViewPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickViewPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->itemGeometryChanged(item, *change, *a2);
}

//  void QQuickViewPrivate::initResize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewPrivate10initResizeEv(QQuickViewPrivate *self) {
  self->initResize();
}

//  void QQuickViewPrivate::updateSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewPrivate10updateSizeEv(QQuickViewPrivate *self) {
  self->updateSize();
}

//  bool QQuickViewPrivate::setRootObject(QObject *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickViewPrivate13setRootObjectEP7QObject(
    QQuickViewPrivate *self,
    QObject *a0) {
  return self->setRootObject(a0);
}

//  void QQuickViewPrivate::init(QQmlEngine *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickViewPrivate4initEP10QQmlEngine(
    QQuickViewPrivate *self,
    QQmlEngine *e) {
  self->init(e);
}

//  QSize QQuickViewPrivate::rootObjectSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QQuickViewPrivate14rootObjectSizeEv(
    const QQuickViewPrivate *self) {
  return new QSize(self->rootObjectSize());
}

//  a Python function taken by a CuteQQuickViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickViewPrivate(
    QQuickViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickViewPrivate *>(self)->take(key, call);
}

//  void QQuickViewPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickViewPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickViewPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->QQuickViewPrivate::itemGeometryChanged(item, *change, *a2);
}
