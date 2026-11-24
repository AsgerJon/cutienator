//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpointerhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpointerhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickPointerHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPointerHandler : QQuickPointerHandler {
  using QQuickPointerHandler::classBegin;
  using QQuickPointerHandler::componentComplete;
  using QQuickPointerHandler::event;
  using QQuickPointerHandler::wantsPointerEvent;
  using QQuickPointerHandler::wantsEventPoint;
  using QQuickPointerHandler::handlePointerEventImpl;
  using QQuickPointerHandler::onTargetChanged;
  using QQuickPointerHandler::onActiveChanged;
  using QQuickPointerHandler::canGrab;
  using QQuickPointerHandler::approveGrabTransition;
};

//  A QQuickPointerHandler that Python can take functions over in. Every QQuickPointerHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPointerHandlerCall0)(const void *, int *);
typedef void (*CuteQQuickPointerHandlerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPointerHandlerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPointerHandlerCall3)(const void *, QPointerEvent *, int *);
typedef bool (*CuteQQuickPointerHandlerCall4)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef void (*CuteQQuickPointerHandlerCall5)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickPointerHandlerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPointerHandlerCall7)(const void *, int *);
typedef bool (*CuteQQuickPointerHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickPointerHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPointerHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPointerHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPointerHandler : public QQuickPointerHandler {
public:
  using QQuickPointerHandler::QQuickPointerHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent")) {
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

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPointerHandlerCall0 call = reinterpret_cast<CuteQQuickPointerHandlerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPointerHandlerCall1 call = reinterpret_cast<CuteQQuickPointerHandlerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickPointerHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPointerHandlerCall2 call = reinterpret_cast<CuteQQuickPointerHandlerCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QQuickPointerHandler::wantsPointerEvent(QPointerEvent *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPointerHandlerCall3 call = reinterpret_cast<CuteQQuickPointerHandlerCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::wantsPointerEvent(event);
  }

  //  bool QQuickPointerHandler::wantsEventPoint(const QPointerEvent
  //      *event, const QEventPoint &point)
  bool wantsEventPoint(
      const QPointerEvent *event,
      const QEventPoint &point) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPointerHandlerCall4 call = reinterpret_cast<CuteQQuickPointerHandlerCall4>(taken[4]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::wantsEventPoint(event, point);
  }

  //  void QQuickPointerHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPointerHandlerCall5 call = reinterpret_cast<CuteQQuickPointerHandlerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPointerHandlerCall6 call = reinterpret_cast<CuteQQuickPointerHandlerCall6>(taken[6]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickPointerHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPointerHandlerCall7 call = reinterpret_cast<CuteQQuickPointerHandlerCall7>(taken[7]);
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
      CuteQQuickPointerHandlerCall8 call = reinterpret_cast<CuteQQuickPointerHandlerCall8>(taken[8]);
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
      CuteQQuickPointerHandlerCall9 call = reinterpret_cast<CuteQQuickPointerHandlerCall9>(taken[9]);
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
      CuteQQuickPointerHandlerCall10 call = reinterpret_cast<CuteQQuickPointerHandlerCall10>(taken[10]);
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
      CuteQQuickPointerHandlerCall11 call = reinterpret_cast<CuteQQuickPointerHandlerCall11>(taken[11]);
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
      CuteQQuickPointerHandlerCall12 call = reinterpret_cast<CuteQQuickPointerHandlerCall12>(taken[12]);
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
      CuteQQuickPointerHandlerCall13 call = reinterpret_cast<CuteQQuickPointerHandlerCall13>(taken[13]);
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
      CuteQQuickPointerHandlerCall14 call = reinterpret_cast<CuteQQuickPointerHandlerCall14>(taken[14]);
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
      CuteQQuickPointerHandlerCall15 call = reinterpret_cast<CuteQQuickPointerHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPointerHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickPointerHandler10metaObjectEv(
    const QQuickPointerHandler *self) {
  return self->metaObject();
}

//  QString QQuickPointerHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickPointerHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPointerHandler::tr(s, c, n));
}

//  void QQuickPointerHandler::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler24qt_qmlMarker_uncreatableEv(
    QQuickPointerHandler *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickPointerHandler::QQuickPointerHandler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPointerHandler *ritual_ZN20QQuickPointerHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickPointerHandler(parent);
}

//  QQuickPointerHandler::~QQuickPointerHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandlerD1Ev(QQuickPointerHandler *self) {
  delete self;
}

//  bool QQuickPointerHandler::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickPointerHandler7enabledEv(
    const QQuickPointerHandler *self) {
  return self->enabled();
}

//  void QQuickPointerHandler::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler10setEnabledEb(
    QQuickPointerHandler *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QQuickPointerHandler::active() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickPointerHandler6activeEv(
    const QQuickPointerHandler *self) {
  return self->active();
}

//  QQuickItem *QQuickPointerHandler::target() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickPointerHandler6targetEv(
    const QQuickPointerHandler *self) {
  return self->target();
}

//  void QQuickPointerHandler::setTarget(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler9setTargetEP10QQuickItem(
    QQuickPointerHandler *self,
    QQuickItem *target) {
  self->setTarget(target);
}

//  QQuickItem *QQuickPointerHandler::parentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickPointerHandler10parentItemEv(
    const QQuickPointerHandler *self) {
  return self->parentItem();
}

//  void QQuickPointerHandler::setParentItem(QQuickItem *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler13setParentItemEP10QQuickItem(
    QQuickPointerHandler *self,
    QQuickItem *p) {
  self->setParentItem(p);
}

//  void QQuickPointerHandler::handlePointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler18handlePointerEventEP13QPointerEvent(
    QQuickPointerHandler *self,
    QPointerEvent *event) {
  self->handlePointerEvent(event);
}

//  GrabPermissions QQuickPointerHandler::grabPermissions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickPointerHandler15grabPermissionsEv(
    const QQuickPointerHandler *self) {
  return static_cast<int>(self->grabPermissions().toInt());
}

//  void QQuickPointerHandler::setGrabPermissions(GrabPermissions
//      grabPermissions)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler18setGrabPermissionsE6QFlagsINS_14GrabPermissionEE(
    QQuickPointerHandler *self,
    int grabPermissions) {
  self->setGrabPermissions(
      QFlags<QQuickPointerHandler::GrabPermission>::fromInt(grabPermissions));
}

//  qreal QQuickPointerHandler::margin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickPointerHandler6marginEv(
    const QQuickPointerHandler *self) {
  return self->margin();
}

//  void QQuickPointerHandler::setMargin(qreal pointDistanceThreshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler9setMarginEd(
    QQuickPointerHandler *self,
    qreal pointDistanceThreshold) {
  self->setMargin(pointDistanceThreshold);
}

//  int QQuickPointerHandler::dragThreshold() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickPointerHandler13dragThresholdEv(
    const QQuickPointerHandler *self) {
  return self->dragThreshold();
}

//  void QQuickPointerHandler::setDragThreshold(int t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler16setDragThresholdEi(
    QQuickPointerHandler *self,
    int t) {
  self->setDragThreshold(t);
}

//  void QQuickPointerHandler::resetDragThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler18resetDragThresholdEv(
    QQuickPointerHandler *self) {
  self->resetDragThreshold();
}

#if QT_CONFIG(cursor)
//  Qt::CursorShape QQuickPointerHandler::cursorShape() const
extern "C" Q_DECL_EXPORT
Qt::CursorShape ritual_ZNK20QQuickPointerHandler11cursorShapeEv(
    const QQuickPointerHandler *self) {
  return self->cursorShape();
}
#endif  // QT_CONFIG(cursor)

#if QT_CONFIG(cursor)
//  void QQuickPointerHandler::setCursorShape(Qt::CursorShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler14setCursorShapeEN2Qt11CursorShapeE(
    QQuickPointerHandler *self,
    Qt::CursorShape shape) {
  self->setCursorShape(shape);
}
#endif  // QT_CONFIG(cursor)

#if QT_CONFIG(cursor)
//  void QQuickPointerHandler::resetCursorShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler16resetCursorShapeEv(
    QQuickPointerHandler *self) {
  self->resetCursorShape();
}
#endif  // QT_CONFIG(cursor)

#if QT_CONFIG(cursor)
//  bool QQuickPointerHandler::isCursorShapeExplicitlySet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickPointerHandler26isCursorShapeExplicitlySetEv(
    const QQuickPointerHandler *self) {
  return self->isCursorShapeExplicitlySet();
}
#endif  // QT_CONFIG(cursor)

//  void QQuickPointerHandler::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler10classBeginEv(
    QQuickPointerHandler *self) {
  self->classBegin();
}

//  void QQuickPointerHandler::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler17componentCompleteEv(
    QQuickPointerHandler *self) {
  self->componentComplete();
}

//  bool QQuickPointerHandler::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickPointerHandler5eventEP6QEvent(
    QQuickPointerHandler *self,
    QEvent *a0) {
  return self->event(a0);
}

//  QPointerEvent *QQuickPointerHandler::currentEvent()
extern "C" Q_DECL_EXPORT
QPointerEvent *ritual_ZN20QQuickPointerHandler12currentEventEv(
    QQuickPointerHandler *self) {
  return self->currentEvent();
}

//  bool QQuickPointerHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent(
    QQuickPointerHandler *self,
    QPointerEvent *event) {
  return self->wantsPointerEvent(event);
}

//  bool QQuickPointerHandler::wantsEventPoint(const QPointerEvent *event,
//      const QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickPointerHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return self->wantsEventPoint(event, *point);
}

//  void QQuickPointerHandler::handlePointerEventImpl(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickPointerHandler *self,
    QPointerEvent *event) {
  self->handlePointerEventImpl(event);
}

//  void QQuickPointerHandler::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler9setActiveEb(
    QQuickPointerHandler *self,
    bool active) {
  self->setActive(active);
}

//  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem(
    QQuickPointerHandler *self,
    QQuickItem *oldTarget) {
  self->onTargetChanged(oldTarget);
}

//  void QQuickPointerHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler15onActiveChangedEv(
    QQuickPointerHandler *self) {
  self->onActiveChanged();
}

//  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEventPoint(
    QQuickPointerHandler *self,
    QPointerEvent *event,
    const QEventPoint *point) {
  return self->canGrab(event, *point);
}

//  bool QQuickPointerHandler::approveGrabTransition(QPointerEvent *event,
//      const QEventPoint &point, QObject *proposedGrabber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointerEventRK11QEventPointP7QObject(
    QQuickPointerHandler *self,
    QPointerEvent *event,
    const QEventPoint *point,
    QObject *proposedGrabber) {
  return self->approveGrabTransition(event, *point, proposedGrabber);
}

//  void QQuickPointerHandler::setPassiveGrab(QPointerEvent *event, const
//      QEventPoint &point, bool grab)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickPointerHandler14setPassiveGrabEP13QPointerEventRK11QEventPointb(
    QQuickPointerHandler *self,
    QPointerEvent *event,
    const QEventPoint *point,
    bool grab) {
  self->setPassiveGrab(event, *point, grab);
}

//  bool QQuickPointerHandler::setExclusiveGrab(QPointerEvent *ev, const
//      QEventPoint &point, bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickPointerHandler16setExclusiveGrabEP13QPointerEventRK11QEventPointb(
    QQuickPointerHandler *self,
    QPointerEvent *ev,
    const QEventPoint *point,
    bool grab) {
  return self->setExclusiveGrab(ev, *point, grab);
}

//  QPointF QQuickPointerHandler::eventPos(const QEventPoint &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK20QQuickPointerHandler8eventPosERK11QEventPoint(
    const QQuickPointerHandler *self,
    const QEventPoint *point) {
  return new QPointF(self->eventPos(*point));
}

//  bool QQuickPointerHandler::parentContains(const QEventPoint &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickPointerHandler14parentContainsERK11QEventPoint(
    const QQuickPointerHandler *self,
    const QEventPoint *point) {
  return self->parentContains(*point);
}

//  bool QQuickPointerHandler::parentContains(const QPointF &localPosition,
//      const QPointF &scenePosition) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickPointerHandler14parentContainsERK7QPointFS2_(
    const QQuickPointerHandler *self,
    const QPointF *localPosition,
    const QPointF *scenePosition) {
  return self->parentContains(*localPosition, *scenePosition);
}

//  QQuickPointerHandlerPrivate *QQuickPointerHandler::d_func()
extern "C" Q_DECL_EXPORT
QQuickPointerHandlerPrivate *ritual_ZN20QQuickPointerHandler6d_funcEv(
    QQuickPointerHandler *self) {
  return self->d_func();
}

//  const QQuickPointerHandlerPrivate *QQuickPointerHandler::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPointerHandlerPrivate *ritual_ZNK20QQuickPointerHandler6d_funcEv(
    const QQuickPointerHandler *self) {
  return self->d_func();
}

//  QQuickPointerHandler as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickPointerHandler_QQmlParserStatus(
    QQuickPointerHandler *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickPointerHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPointerHandler(
    QQuickPointerHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPointerHandler *>(self)->take(key, call);
}

//  void QQuickPointerHandler::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickPointerHandler10classBeginEv(
    QQuickPointerHandler *self) {
  static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::classBegin();
}

//  void QQuickPointerHandler::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickPointerHandler17componentCompleteEv(
    QQuickPointerHandler *self) {
  static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::componentComplete();
}

//  bool QQuickPointerHandler::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickPointerHandler5eventEP6QEvent(
    QQuickPointerHandler *self,
    QEvent *a0) {
  return static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::event(
      a0);
}

//  bool QQuickPointerHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent(
    QQuickPointerHandler *self,
    QPointerEvent *event) {
  return static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::wantsPointerEvent(
      event);
}

//  bool QQuickPointerHandler::wantsEventPoint(const QPointerEvent *event,
//      const QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickPointerHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::wantsEventPoint(
      event,
      *point);
}

//  void QQuickPointerHandler::handlePointerEventImpl(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickPointerHandler *self,
    QPointerEvent *event) {
  static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::handlePointerEventImpl(
      event);
}

//  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem(
    QQuickPointerHandler *self,
    QQuickItem *oldTarget) {
  static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::onTargetChanged(
      oldTarget);
}

//  void QQuickPointerHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickPointerHandler15onActiveChangedEv(
    QQuickPointerHandler *self) {
  static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::onActiveChanged();
}

//  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEventPoint(
    QQuickPointerHandler *self,
    QPointerEvent *event,
    const QEventPoint *point) {
  return static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::canGrab(
      event,
      *point);
}

//  bool QQuickPointerHandler::approveGrabTransition(QPointerEvent *event,
//      const QEventPoint &point, QObject *proposedGrabber)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointerEventRK11QEventPointP7QObject(
    QQuickPointerHandler *self,
    QPointerEvent *event,
    const QEventPoint *point,
    QObject *proposedGrabber) {
  return static_cast<OwnQQuickPointerHandler *>(self)->OwnQQuickPointerHandler::approveGrabTransition(
      event,
      *point,
      proposedGrabber);
}
