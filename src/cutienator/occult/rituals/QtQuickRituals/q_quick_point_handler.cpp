//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpointhandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpointhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickPointHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPointHandler : QQuickPointHandler {
  using QQuickPointHandler::wantsEventPoint;
};

//  A QQuickPointHandler that Python can take functions over in. Every QQuickPointHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickPointHandlerCall0)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickPointHandlerCall1)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickPointHandlerCall2)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickPointHandlerCall3)(const void *, int *);
typedef void (*CuteQQuickPointHandlerCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPointHandlerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointHandlerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPointHandlerCall7)(const void *, int *);
typedef bool (*CuteQQuickPointHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickPointHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPointHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPointHandler : public QQuickPointHandler {
public:
  using QQuickPointHandler::QQuickPointHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onActiveChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEventPoint")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointerEventRK11QEventPointP7QObject")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QQuickPointHandler::wantsEventPoint(const QPointerEvent *event,
  //      const QEventPoint &point)
  bool wantsEventPoint(
      const QPointerEvent *event,
      const QEventPoint &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPointHandlerCall0 call = reinterpret_cast<CuteQQuickPointHandlerCall0>(taken[0]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointHandler::wantsEventPoint(event, point);
  }

  //  bool QQuickSinglePointHandler::wantsPointerEvent(QPointerEvent
  //      *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPointHandlerCall1 call = reinterpret_cast<CuteQQuickPointHandlerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickSinglePointHandler::wantsPointerEvent(event);
  }

  //  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPointHandlerCall2 call = reinterpret_cast<CuteQQuickPointHandlerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSinglePointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPointHandlerCall3 call = reinterpret_cast<CuteQQuickPointHandlerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPointHandlerCall4 call = reinterpret_cast<CuteQQuickPointHandlerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickPointerHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPointHandlerCall5 call = reinterpret_cast<CuteQQuickPointHandlerCall5>(taken[5]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPointHandlerCall6 call = reinterpret_cast<CuteQQuickPointHandlerCall6>(taken[6]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPointHandlerCall7 call = reinterpret_cast<CuteQQuickPointHandlerCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onActiveChanged();
  }

  //  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
  //      QEventPoint &point)
  bool canGrab(QPointerEvent *event, const QEventPoint &point) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPointHandlerCall8 call = reinterpret_cast<CuteQQuickPointHandlerCall8>(taken[8]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::canGrab(event, point);
  }

  //  bool QQuickPointerHandler::approveGrabTransition(QPointerEvent
  //      *event, const QEventPoint &point, QObject *proposedGrabber)
  bool approveGrabTransition(
      QPointerEvent *event,
      const QEventPoint &point,
      QObject *proposedGrabber) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPointHandlerCall9 call = reinterpret_cast<CuteQQuickPointHandlerCall9>(taken[9]);
      bool given = call(this, event, &point, proposedGrabber, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::approveGrabTransition(event, point, proposedGrabber);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPointHandlerCall10 call = reinterpret_cast<CuteQQuickPointHandlerCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPointHandlerCall11 call = reinterpret_cast<CuteQQuickPointHandlerCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPointHandlerCall12 call = reinterpret_cast<CuteQQuickPointHandlerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPointHandlerCall13 call = reinterpret_cast<CuteQQuickPointHandlerCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPointHandlerCall14 call = reinterpret_cast<CuteQQuickPointHandlerCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPointHandlerCall15 call = reinterpret_cast<CuteQQuickPointHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPointHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickPointHandler10metaObjectEv(
    const QQuickPointHandler *self) {
  return self->metaObject();
}

//  QString QQuickPointHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickPointHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPointHandler::tr(s, c, n));
}

//  QQuickPointHandler::QQuickPointHandler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPointHandler *ritual_ZN18QQuickPointHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickPointHandler(parent);
}

//  QVector2D QQuickPointHandler::translation() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK18QQuickPointHandler11translationEv(
    const QQuickPointHandler *self) {
  return new QVector2D(self->translation());
}

//  bool QQuickPointHandler::wantsEventPoint(const QPointerEvent *event,
//      const QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPointHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickPointHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return self->wantsEventPoint(event, *point);
}

//  a Python function taken by a CuteQQuickPointHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPointHandler(
    QQuickPointHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPointHandler *>(self)->take(key, call);
}

//  bool QQuickPointHandler::wantsEventPoint(const QPointerEvent *event,
//      const QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPointHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickPointHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return static_cast<OwnQQuickPointHandler *>(self)->OwnQQuickPointHandler::wantsEventPoint(
      event,
      *point);
}
