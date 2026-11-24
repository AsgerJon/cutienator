//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksinglepointhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksinglepointhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickhandlerpoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickSinglePointHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSinglePointHandler : QQuickSinglePointHandler {
  using QQuickSinglePointHandler::wantsPointerEvent;
  using QQuickSinglePointHandler::handlePointerEventImpl;
};

//  A QQuickSinglePointHandler that Python can take functions over in. Every QQuickSinglePointHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickSinglePointHandlerCall0)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickSinglePointHandlerCall1)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickSinglePointHandlerCall2)(const void *, int *);
typedef void (*CuteQQuickSinglePointHandlerCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSinglePointHandlerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSinglePointHandlerCall5)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef void (*CuteQQuickSinglePointHandlerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSinglePointHandlerCall7)(const void *, int *);
typedef bool (*CuteQQuickSinglePointHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickSinglePointHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSinglePointHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSinglePointHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSinglePointHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSinglePointHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSinglePointHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSinglePointHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSinglePointHandler : public QQuickSinglePointHandler {
public:
  using QQuickSinglePointHandler::QQuickSinglePointHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[5] = call;
      return true;
    }
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

  //  bool QQuickSinglePointHandler::wantsPointerEvent(QPointerEvent
  //      *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerCall0 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickSinglePointHandler::wantsPointerEvent(event);
  }

  //  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerCall1 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSinglePointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerCall2 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerCall3 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickPointerHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerCall4 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QQuickPointerHandler::wantsEventPoint(const QPointerEvent
  //      *event, const QEventPoint &point)
  bool wantsEventPoint(
      const QPointerEvent *event,
      const QEventPoint &point) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerCall5 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall5>(taken[5]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::wantsEventPoint(event, point);
  }

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerCall6 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall6>(taken[6]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSinglePointHandlerCall7 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall7>(taken[7]);
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
      CuteQQuickSinglePointHandlerCall8 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall8>(taken[8]);
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
      CuteQQuickSinglePointHandlerCall9 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall9>(taken[9]);
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
      CuteQQuickSinglePointHandlerCall10 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall10>(taken[10]);
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
      CuteQQuickSinglePointHandlerCall11 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall11>(taken[11]);
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
      CuteQQuickSinglePointHandlerCall12 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall12>(taken[12]);
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
      CuteQQuickSinglePointHandlerCall13 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall13>(taken[13]);
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
      CuteQQuickSinglePointHandlerCall14 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall14>(taken[14]);
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
      CuteQQuickSinglePointHandlerCall15 call = reinterpret_cast<CuteQQuickSinglePointHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSinglePointHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickSinglePointHandler10metaObjectEv(
    const QQuickSinglePointHandler *self) {
  return self->metaObject();
}

//  QString QQuickSinglePointHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickSinglePointHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSinglePointHandler::tr(s, c, n));
}

//  QQuickSinglePointHandler::QQuickSinglePointHandler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSinglePointHandler *ritual_ZN24QQuickSinglePointHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickSinglePointHandler(parent);
}

//  QQuickHandlerPoint QQuickSinglePointHandler::point() const
extern "C" Q_DECL_EXPORT
QQuickHandlerPoint *ritual_ZNK24QQuickSinglePointHandler5pointEv(
    const QQuickSinglePointHandler *self) {
  return new QQuickHandlerPoint(self->point());
}

//  bool QQuickSinglePointHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickSinglePointHandler17wantsPointerEventEP13QPointerEvent(
    QQuickSinglePointHandler *self,
    QPointerEvent *event) {
  return self->wantsPointerEvent(event);
}

//  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSinglePointHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickSinglePointHandler *self,
    QPointerEvent *event) {
  self->handlePointerEventImpl(event);
}

//  void QQuickSinglePointHandler::setIgnoreAdditionalPoints(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSinglePointHandler25setIgnoreAdditionalPointsEb(
    QQuickSinglePointHandler *self,
    bool v) {
  self->setIgnoreAdditionalPoints(v);
}

//  void QQuickSinglePointHandler::setPointId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSinglePointHandler10setPointIdEi(
    QQuickSinglePointHandler *self,
    int id) {
  self->setPointId(id);
}

//  QQuickSinglePointHandlerPrivate *QQuickSinglePointHandler::d_func()
extern "C" Q_DECL_EXPORT
QQuickSinglePointHandlerPrivate *ritual_ZN24QQuickSinglePointHandler6d_funcEv(
    QQuickSinglePointHandler *self) {
  return self->d_func();
}

//  const QQuickSinglePointHandlerPrivate *QQuickSinglePointHandler::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickSinglePointHandlerPrivate *ritual_ZNK24QQuickSinglePointHandler6d_funcEv(
    const QQuickSinglePointHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickSinglePointHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSinglePointHandler(
    QQuickSinglePointHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSinglePointHandler *>(self)->take(key, call);
}

//  bool QQuickSinglePointHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQuickSinglePointHandler17wantsPointerEventEP13QPointerEvent(
    QQuickSinglePointHandler *self,
    QPointerEvent *event) {
  return static_cast<OwnQQuickSinglePointHandler *>(self)->OwnQQuickSinglePointHandler::wantsPointerEvent(
      event);
}

//  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickSinglePointHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickSinglePointHandler *self,
    QPointerEvent *event) {
  static_cast<OwnQQuickSinglePointHandler *>(self)->OwnQQuickSinglePointHandler::handlePointerEventImpl(
      event);
}
