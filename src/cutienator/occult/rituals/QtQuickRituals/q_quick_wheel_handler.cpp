//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwheelhandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(wheelevent)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwheelhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickWheelHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickWheelHandler : QQuickWheelHandler {
  using QQuickWheelHandler::wantsPointerEvent;
  using QQuickWheelHandler::onTargetChanged;
  using QQuickWheelHandler::onActiveChanged;
  using QQuickWheelHandler::timerEvent;
};

//  A QQuickWheelHandler that Python can take functions over in. Every QQuickWheelHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickWheelHandlerCall0)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickWheelHandlerCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickWheelHandlerCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWheelHandlerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWheelHandlerCall4)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickWheelHandlerCall5)(const void *, int *);
typedef void (*CuteQQuickWheelHandlerCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWheelHandlerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWheelHandlerCall8)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickWheelHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickWheelHandlerCall10)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWheelHandlerCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWheelHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWheelHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWheelHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWheelHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWheelHandler : public QQuickWheelHandler {
public:
  using QQuickWheelHandler::QQuickWheelHandler;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler17wantsPointerEventEP13QPointerEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onActiveChangedEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler22handlePointerEventImplEP13QPointerEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler7canGrabEP13QPointerEventRK11QEventPoint")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler21approveGrabTransitionEP13QPointerEventRK11QEventPointP7QObject")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

  //  bool QQuickWheelHandler::wantsPointerEvent(QPointerEvent *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall0 call = reinterpret_cast<CuteQQuickWheelHandlerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickWheelHandler::wantsPointerEvent(event);
  }

  //  void QQuickWheelHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall1 call = reinterpret_cast<CuteQQuickWheelHandlerCall1>(taken[1]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickWheelHandler::onTargetChanged(oldTarget);
  }

  //  void QQuickWheelHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall2 call = reinterpret_cast<CuteQQuickWheelHandlerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWheelHandler::onActiveChanged();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickWheelHandler::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall3 call = reinterpret_cast<CuteQQuickWheelHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickWheelHandler::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall4 call = reinterpret_cast<CuteQQuickWheelHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickSinglePointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall5 call = reinterpret_cast<CuteQQuickWheelHandlerCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall6 call = reinterpret_cast<CuteQQuickWheelHandlerCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickPointerHandler::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall7 call = reinterpret_cast<CuteQQuickWheelHandlerCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall8 call = reinterpret_cast<CuteQQuickWheelHandlerCall8>(taken[8]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::wantsEventPoint(event, point);
  }

  //  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
  //      QEventPoint &point)
  bool canGrab(QPointerEvent *event, const QEventPoint &point) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall9 call = reinterpret_cast<CuteQQuickWheelHandlerCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall10 call = reinterpret_cast<CuteQQuickWheelHandlerCall10>(taken[10]);
      bool given = call(this, event, &point, proposedGrabber, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::approveGrabTransition(event, point, proposedGrabber);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall11 call = reinterpret_cast<CuteQQuickWheelHandlerCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickWheelHandlerCall12 call = reinterpret_cast<CuteQQuickWheelHandlerCall12>(taken[12]);
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
      CuteQQuickWheelHandlerCall13 call = reinterpret_cast<CuteQQuickWheelHandlerCall13>(taken[13]);
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
      CuteQQuickWheelHandlerCall14 call = reinterpret_cast<CuteQQuickWheelHandlerCall14>(taken[14]);
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
      CuteQQuickWheelHandlerCall15 call = reinterpret_cast<CuteQQuickWheelHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWheelHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickWheelHandler10metaObjectEv(
    const QQuickWheelHandler *self) {
  return self->metaObject();
}

//  void *QQuickWheelHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickWheelHandler11qt_metacastEPKc(
    QQuickWheelHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWheelHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickWheelHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWheelHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWheelHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickWheelHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWheelHandler::tr(s, c, n));
}

//  QQuickWheelHandler::QQuickWheelHandler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickWheelHandler *ritual_ZN18QQuickWheelHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickWheelHandler(parent);
}

//  Qt::Orientation QQuickWheelHandler::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK18QQuickWheelHandler11orientationEv(
    const QQuickWheelHandler *self) {
  return self->orientation();
}

//  void QQuickWheelHandler::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler14setOrientationEN2Qt11OrientationE(
    QQuickWheelHandler *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  bool QQuickWheelHandler::isInvertible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickWheelHandler12isInvertibleEv(
    const QQuickWheelHandler *self) {
  return self->isInvertible();
}

//  void QQuickWheelHandler::setInvertible(bool invertible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler13setInvertibleEb(
    QQuickWheelHandler *self,
    bool invertible) {
  self->setInvertible(invertible);
}

//  qreal QQuickWheelHandler::activeTimeout() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickWheelHandler13activeTimeoutEv(
    const QQuickWheelHandler *self) {
  return self->activeTimeout();
}

//  void QQuickWheelHandler::setActiveTimeout(qreal timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler16setActiveTimeoutEd(
    QQuickWheelHandler *self,
    qreal timeout) {
  self->setActiveTimeout(timeout);
}

//  qreal QQuickWheelHandler::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickWheelHandler8rotationEv(
    const QQuickWheelHandler *self) {
  return self->rotation();
}

//  void QQuickWheelHandler::setRotation(qreal rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler11setRotationEd(
    QQuickWheelHandler *self,
    qreal rotation) {
  self->setRotation(rotation);
}

//  qreal QQuickWheelHandler::rotationScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickWheelHandler13rotationScaleEv(
    const QQuickWheelHandler *self) {
  return self->rotationScale();
}

//  void QQuickWheelHandler::setRotationScale(qreal rotationScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler16setRotationScaleEd(
    QQuickWheelHandler *self,
    qreal rotationScale) {
  self->setRotationScale(rotationScale);
}

//  QString QQuickWheelHandler::property() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickWheelHandler8propertyEv(
    const QQuickWheelHandler *self) {
  return new QString(self->property());
}

//  void QQuickWheelHandler::setProperty(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler11setPropertyERK7QString(
    QQuickWheelHandler *self,
    const QString *name) {
  self->setProperty(*name);
}

//  qreal QQuickWheelHandler::targetScaleMultiplier() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickWheelHandler21targetScaleMultiplierEv(
    const QQuickWheelHandler *self) {
  return self->targetScaleMultiplier();
}

//  void QQuickWheelHandler::setTargetScaleMultiplier(qreal
//      targetScaleMultiplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler24setTargetScaleMultiplierEd(
    QQuickWheelHandler *self,
    qreal targetScaleMultiplier) {
  self->setTargetScaleMultiplier(targetScaleMultiplier);
}

//  bool QQuickWheelHandler::isTargetTransformAroundCursor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickWheelHandler29isTargetTransformAroundCursorEv(
    const QQuickWheelHandler *self) {
  return self->isTargetTransformAroundCursor();
}

//  void QQuickWheelHandler::setTargetTransformAroundCursor(bool ttac)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler30setTargetTransformAroundCursorEb(
    QQuickWheelHandler *self,
    bool ttac) {
  self->setTargetTransformAroundCursor(ttac);
}

//  bool QQuickWheelHandler::isBlocking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickWheelHandler10isBlockingEv(
    const QQuickWheelHandler *self) {
  return self->isBlocking();
}

//  void QQuickWheelHandler::setBlocking(bool blocking)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler11setBlockingEb(
    QQuickWheelHandler *self,
    bool blocking) {
  self->setBlocking(blocking);
}

//  void QQuickWheelHandler::wheel(QQuickWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler5wheelEP16QQuickWheelEvent(
    QQuickWheelHandler *self,
    QQuickWheelEvent *event) {
  self->wheel(event);
}

//  void QQuickWheelHandler::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler18orientationChangedEv(
    QQuickWheelHandler *self) {
  self->orientationChanged();
}

//  void QQuickWheelHandler::invertibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler17invertibleChangedEv(
    QQuickWheelHandler *self) {
  self->invertibleChanged();
}

//  void QQuickWheelHandler::activeTimeoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler20activeTimeoutChangedEv(
    QQuickWheelHandler *self) {
  self->activeTimeoutChanged();
}

//  void QQuickWheelHandler::rotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler15rotationChangedEv(
    QQuickWheelHandler *self) {
  self->rotationChanged();
}

//  void QQuickWheelHandler::rotationScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler20rotationScaleChangedEv(
    QQuickWheelHandler *self) {
  self->rotationScaleChanged();
}

//  void QQuickWheelHandler::propertyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler15propertyChangedEv(
    QQuickWheelHandler *self) {
  self->propertyChanged();
}

//  void QQuickWheelHandler::targetScaleMultiplierChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler28targetScaleMultiplierChangedEv(
    QQuickWheelHandler *self) {
  self->targetScaleMultiplierChanged();
}

//  void QQuickWheelHandler::targetTransformAroundCursorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler34targetTransformAroundCursorChangedEv(
    QQuickWheelHandler *self) {
  self->targetTransformAroundCursorChanged();
}

//  void QQuickWheelHandler::blockingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler15blockingChangedEv(
    QQuickWheelHandler *self) {
  self->blockingChanged();
}

//  bool QQuickWheelHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickWheelHandler17wantsPointerEventEP13QPointerEvent(
    QQuickWheelHandler *self,
    QPointerEvent *event) {
  return self->wantsPointerEvent(event);
}

//  void QQuickWheelHandler::handleEventPoint(QPointerEvent *event,
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler16handleEventPointEP13QPointerEventR11QEventPoint(
    QQuickWheelHandler *self,
    QPointerEvent *event,
    QEventPoint *point) {
  self->handleEventPoint(event, *point);
}

//  void QQuickWheelHandler::onTargetChanged(QQuickItem *oldTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler15onTargetChangedEP10QQuickItem(
    QQuickWheelHandler *self,
    QQuickItem *oldTarget) {
  self->onTargetChanged(oldTarget);
}

//  void QQuickWheelHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler15onActiveChangedEv(
    QQuickWheelHandler *self) {
  self->onActiveChanged();
}

//  void QQuickWheelHandler::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickWheelHandler10timerEventEP11QTimerEvent(
    QQuickWheelHandler *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QQuickWheelHandlerPrivate *QQuickWheelHandler::d_func()
extern "C" Q_DECL_EXPORT
QQuickWheelHandlerPrivate *ritual_ZN18QQuickWheelHandler6d_funcEv(
    QQuickWheelHandler *self) {
  return self->d_func();
}

//  const QQuickWheelHandlerPrivate *QQuickWheelHandler::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickWheelHandlerPrivate *ritual_ZNK18QQuickWheelHandler6d_funcEv(
    const QQuickWheelHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickWheelHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWheelHandler(
    QQuickWheelHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWheelHandler *>(self)->take(key, call);
}

//  bool QQuickWheelHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickWheelHandler17wantsPointerEventEP13QPointerEvent(
    QQuickWheelHandler *self,
    QPointerEvent *event) {
  return static_cast<OwnQQuickWheelHandler *>(self)->OwnQQuickWheelHandler::wantsPointerEvent(
      event);
}

//  void QQuickWheelHandler::onTargetChanged(QQuickItem *oldTarget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickWheelHandler15onTargetChangedEP10QQuickItem(
    QQuickWheelHandler *self,
    QQuickItem *oldTarget) {
  static_cast<OwnQQuickWheelHandler *>(self)->OwnQQuickWheelHandler::onTargetChanged(
      oldTarget);
}

//  void QQuickWheelHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickWheelHandler15onActiveChangedEv(
    QQuickWheelHandler *self) {
  static_cast<OwnQQuickWheelHandler *>(self)->OwnQQuickWheelHandler::onActiveChanged();
}

//  void QQuickWheelHandler::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickWheelHandler10timerEventEP11QTimerEvent(
    QQuickWheelHandler *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickWheelHandler *>(self)->OwnQQuickWheelHandler::timerEvent(
      event);
}

#endif  // QT_CONFIG(wheelevent)
