//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickhoverhandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickhoverhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickHoverHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickHoverHandler : QQuickHoverHandler {
  using QQuickHoverHandler::componentComplete;
  using QQuickHoverHandler::wantsPointerEvent;
};

//  A QQuickHoverHandler that Python can take functions over in. Every QQuickHoverHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickHoverHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHoverHandlerCall1)(const void *, int *);
typedef bool (*CuteQQuickHoverHandlerCall2)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickHoverHandlerCall3)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickHoverHandlerCall4)(const void *, int *);
typedef bool (*CuteQQuickHoverHandlerCall5)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef void (*CuteQQuickHoverHandlerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickHoverHandlerCall7)(const void *, int *);
typedef bool (*CuteQQuickHoverHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickHoverHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickHoverHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHoverHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHoverHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHoverHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHoverHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickHoverHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickHoverHandler : public QQuickHoverHandler {
public:
  using QQuickHoverHandler::QQuickHoverHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
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

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickHoverHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickHoverHandlerCall0 call = reinterpret_cast<CuteQQuickHoverHandlerCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickHoverHandler::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickHoverHandler::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickHoverHandlerCall1 call = reinterpret_cast<CuteQQuickHoverHandlerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickHoverHandler::componentComplete();
  }

  //  bool QQuickHoverHandler::wantsPointerEvent(QPointerEvent *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickHoverHandlerCall2 call = reinterpret_cast<CuteQQuickHoverHandlerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickHoverHandler::wantsPointerEvent(event);
  }

  //  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickHoverHandlerCall3 call = reinterpret_cast<CuteQQuickHoverHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSinglePointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickHoverHandlerCall4 call = reinterpret_cast<CuteQQuickHoverHandlerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  bool QQuickPointerHandler::wantsEventPoint(const QPointerEvent
  //      *event, const QEventPoint &point)
  bool wantsEventPoint(
      const QPointerEvent *event,
      const QEventPoint &point) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickHoverHandlerCall5 call = reinterpret_cast<CuteQQuickHoverHandlerCall5>(taken[5]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::wantsEventPoint(event, point);
  }

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickHoverHandlerCall6 call = reinterpret_cast<CuteQQuickHoverHandlerCall6>(taken[6]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickHoverHandlerCall7 call = reinterpret_cast<CuteQQuickHoverHandlerCall7>(taken[7]);
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
      CuteQQuickHoverHandlerCall8 call = reinterpret_cast<CuteQQuickHoverHandlerCall8>(taken[8]);
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
      CuteQQuickHoverHandlerCall9 call = reinterpret_cast<CuteQQuickHoverHandlerCall9>(taken[9]);
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
      CuteQQuickHoverHandlerCall10 call = reinterpret_cast<CuteQQuickHoverHandlerCall10>(taken[10]);
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
      CuteQQuickHoverHandlerCall11 call = reinterpret_cast<CuteQQuickHoverHandlerCall11>(taken[11]);
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
      CuteQQuickHoverHandlerCall12 call = reinterpret_cast<CuteQQuickHoverHandlerCall12>(taken[12]);
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
      CuteQQuickHoverHandlerCall13 call = reinterpret_cast<CuteQQuickHoverHandlerCall13>(taken[13]);
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
      CuteQQuickHoverHandlerCall14 call = reinterpret_cast<CuteQQuickHoverHandlerCall14>(taken[14]);
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
      CuteQQuickHoverHandlerCall15 call = reinterpret_cast<CuteQQuickHoverHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickHoverHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickHoverHandler10metaObjectEv(
    const QQuickHoverHandler *self) {
  return self->metaObject();
}

//  QString QQuickHoverHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickHoverHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickHoverHandler::tr(s, c, n));
}

//  QQuickHoverHandler::QQuickHoverHandler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickHoverHandler *ritual_ZN18QQuickHoverHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickHoverHandler(parent);
}

//  QQuickHoverHandler::~QQuickHoverHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHoverHandlerD1Ev(QQuickHoverHandler *self) {
  delete self;
}

//  bool QQuickHoverHandler::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickHoverHandler5eventEP6QEvent(
    QQuickHoverHandler *self,
    QEvent *a0) {
  return self->event(a0);
}

//  bool QQuickHoverHandler::isHovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickHoverHandler9isHoveredEv(
    const QQuickHoverHandler *self) {
  return self->isHovered();
}

//  bool QQuickHoverHandler::isBlocking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickHoverHandler10isBlockingEv(
    const QQuickHoverHandler *self) {
  return self->isBlocking();
}

//  void QQuickHoverHandler::setBlocking(bool blocking)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHoverHandler11setBlockingEb(
    QQuickHoverHandler *self,
    bool blocking) {
  self->setBlocking(blocking);
}

//  void QQuickHoverHandler::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHoverHandler17componentCompleteEv(
    QQuickHoverHandler *self) {
  self->componentComplete();
}

//  bool QQuickHoverHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickHoverHandler17wantsPointerEventEP13QPointerEvent(
    QQuickHoverHandler *self,
    QPointerEvent *event) {
  return self->wantsPointerEvent(event);
}

//  void QQuickHoverHandler::setHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHoverHandler10setHoveredEb(
    QQuickHoverHandler *self,
    bool hovered) {
  self->setHovered(hovered);
}

//  a Python function taken by a CuteQQuickHoverHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickHoverHandler(
    QQuickHoverHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickHoverHandler *>(self)->take(key, call);
}

//  bool QQuickHoverHandler::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickHoverHandler5eventEP6QEvent(
    QQuickHoverHandler *self,
    QEvent *a0) {
  return self->QQuickHoverHandler::event(a0);
}

//  void QQuickHoverHandler::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickHoverHandler17componentCompleteEv(
    QQuickHoverHandler *self) {
  static_cast<OwnQQuickHoverHandler *>(self)->OwnQQuickHoverHandler::componentComplete();
}

//  bool QQuickHoverHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickHoverHandler17wantsPointerEventEP13QPointerEvent(
    QQuickHoverHandler *self,
    QPointerEvent *event) {
  return static_cast<OwnQQuickHoverHandler *>(self)->OwnQQuickHoverHandler::wantsPointerEvent(
      event);
}
