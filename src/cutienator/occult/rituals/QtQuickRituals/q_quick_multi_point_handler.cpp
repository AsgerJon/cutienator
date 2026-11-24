//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickmultipointhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickmultipointhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickhandlerpoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickMultiPointHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMultiPointHandler : QQuickMultiPointHandler {
  using QQuickMultiPointHandler::wantsPointerEvent;
  using QQuickMultiPointHandler::handlePointerEventImpl;
  using QQuickMultiPointHandler::onActiveChanged;
};

//  A QQuickMultiPointHandler that Python can take functions over in. Every QQuickMultiPointHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickMultiPointHandlerCall0)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickMultiPointHandlerCall1)(const void *, QPointerEvent *, int *);
typedef void (*CuteQQuickMultiPointHandlerCall2)(const void *, int *);
typedef void (*CuteQQuickMultiPointHandlerCall3)(const void *, int *);
typedef void (*CuteQQuickMultiPointHandlerCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMultiPointHandlerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMultiPointHandlerCall6)(const void *, const QPointerEvent *, const QEventPoint *, int *);
typedef void (*CuteQQuickMultiPointHandlerCall7)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickMultiPointHandlerCall8)(const void *, QPointerEvent *, const QEventPoint *, int *);
typedef bool (*CuteQQuickMultiPointHandlerCall9)(const void *, QPointerEvent *, const QEventPoint *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMultiPointHandlerCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointHandlerCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointHandlerCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointHandlerCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointHandlerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMultiPointHandlerCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickMultiPointHandler : public QQuickMultiPointHandler {
public:
  using QQuickMultiPointHandler::QQuickMultiPointHandler;
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
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onActiveChangedEv")) {
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
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickPointerHandler15onTargetChangedEP10QQuickItem")) {
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

  //  bool QQuickMultiPointHandler::wantsPointerEvent(QPointerEvent *event)
  bool wantsPointerEvent(QPointerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerCall0 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickMultiPointHandler::wantsPointerEvent(event);
  }

  //  void QQuickMultiPointHandler::handlePointerEventImpl(QPointerEvent
  //      *event)
  void handlePointerEventImpl(QPointerEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerCall1 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickMultiPointHandler::handlePointerEventImpl(event);
  }

  //  void QQuickMultiPointHandler::onActiveChanged()
  void onActiveChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerCall2 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMultiPointHandler::onActiveChanged();
  }

  //  void QQuickPointerHandler::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerCall3 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::classBegin();
  }

  //  void QQuickPointerHandler::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerCall4 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall4>(taken[4]);
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
      CuteQQuickMultiPointHandlerCall5 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerCall6 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall6>(taken[6]);
      bool given = call(this, event, &point, &handled);
      if (handled) return given;
    }
    return QQuickPointerHandler::wantsEventPoint(event, point);
  }

  //  void QQuickPointerHandler::onTargetChanged(QQuickItem *oldTarget)
  void onTargetChanged(QQuickItem *oldTarget) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerCall7 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall7>(taken[7]);
      call(this, oldTarget, &handled);
      if (handled) return;
    }
    QQuickPointerHandler::onTargetChanged(oldTarget);
  }

  //  bool QQuickPointerHandler::canGrab(QPointerEvent *event, const
  //      QEventPoint &point)
  bool canGrab(QPointerEvent *event, const QEventPoint &point) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMultiPointHandlerCall8 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall8>(taken[8]);
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
      CuteQQuickMultiPointHandlerCall9 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall9>(taken[9]);
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
      CuteQQuickMultiPointHandlerCall10 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall10>(taken[10]);
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
      CuteQQuickMultiPointHandlerCall11 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall11>(taken[11]);
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
      CuteQQuickMultiPointHandlerCall12 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall12>(taken[12]);
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
      CuteQQuickMultiPointHandlerCall13 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall13>(taken[13]);
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
      CuteQQuickMultiPointHandlerCall14 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall14>(taken[14]);
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
      CuteQQuickMultiPointHandlerCall15 call = reinterpret_cast<CuteQQuickMultiPointHandlerCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickMultiPointHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickMultiPointHandler10metaObjectEv(
    const QQuickMultiPointHandler *self) {
  return self->metaObject();
}

//  QString QQuickMultiPointHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickMultiPointHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMultiPointHandler::tr(s, c, n));
}

//  QQuickMultiPointHandler::QQuickMultiPointHandler(QQuickItem *parent, int
//      minimumPointCount, int maximumPointCount)
extern "C" Q_DECL_EXPORT
QQuickMultiPointHandler *ritual_ZN23QQuickMultiPointHandlerC1EP10QQuickItemii(
    QQuickItem *parent,
    int minimumPointCount,
    int maximumPointCount) {
  return new CuteQQuickMultiPointHandler(
      parent,
      minimumPointCount,
      maximumPointCount);
}

//  int QQuickMultiPointHandler::minimumPointCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickMultiPointHandler17minimumPointCountEv(
    const QQuickMultiPointHandler *self) {
  return self->minimumPointCount();
}

//  void QQuickMultiPointHandler::setMinimumPointCount(int c)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMultiPointHandler20setMinimumPointCountEi(
    QQuickMultiPointHandler *self,
    int c) {
  self->setMinimumPointCount(c);
}

//  int QQuickMultiPointHandler::maximumPointCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQuickMultiPointHandler17maximumPointCountEv(
    const QQuickMultiPointHandler *self) {
  return self->maximumPointCount();
}

//  void QQuickMultiPointHandler::setMaximumPointCount(int maximumPointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMultiPointHandler20setMaximumPointCountEi(
    QQuickMultiPointHandler *self,
    int maximumPointCount) {
  self->setMaximumPointCount(maximumPointCount);
}

//  const QQuickHandlerPoint &QQuickMultiPointHandler::centroid() const
extern "C" Q_DECL_EXPORT
QQuickHandlerPoint *ritual_ZNK23QQuickMultiPointHandler8centroidEv(
    const QQuickMultiPointHandler *self) {
  return new QQuickHandlerPoint(self->centroid());
}

//  bool QQuickMultiPointHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickMultiPointHandler17wantsPointerEventEP13QPointerEvent(
    QQuickMultiPointHandler *self,
    QPointerEvent *event) {
  return self->wantsPointerEvent(event);
}

//  void QQuickMultiPointHandler::handlePointerEventImpl(QPointerEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMultiPointHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickMultiPointHandler *self,
    QPointerEvent *event) {
  self->handlePointerEventImpl(event);
}

//  void QQuickMultiPointHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMultiPointHandler15onActiveChangedEv(
    QQuickMultiPointHandler *self) {
  self->onActiveChanged();
}

//  bool QQuickMultiPointHandler::hasCurrentPoints(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickMultiPointHandler16hasCurrentPointsEP13QPointerEvent(
    QQuickMultiPointHandler *self,
    QPointerEvent *event) {
  return self->hasCurrentPoints(event);
}

//  QList<QEventPoint> QQuickMultiPointHandler::eligiblePoints(QPointerEvent
//      *event)
extern "C" Q_DECL_EXPORT
QList<QEventPoint> *ritual_ZN23QQuickMultiPointHandler14eligiblePointsEP13QPointerEvent(
    QQuickMultiPointHandler *self,
    QPointerEvent *event) {
  return new QList<QEventPoint>(self->eligiblePoints(event));
}

//  qreal QQuickMultiPointHandler::averageTouchPointDistance(const QPointF
//      &ref)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN23QQuickMultiPointHandler25averageTouchPointDistanceERK7QPointF(
    QQuickMultiPointHandler *self,
    const QPointF *ref) {
  return self->averageTouchPointDistance(*ref);
}

//  qreal QQuickMultiPointHandler::averageStartingDistance(const QPointF
//      &ref)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN23QQuickMultiPointHandler23averageStartingDistanceERK7QPointF(
    QQuickMultiPointHandler *self,
    const QPointF *ref) {
  return self->averageStartingDistance(*ref);
}

//  void QQuickMultiPointHandler::acceptPoints(const QList<QEventPoint>
//      &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMultiPointHandler12acceptPointsERK5QListI11QEventPointE(
    QQuickMultiPointHandler *self,
    const QList<QEventPoint> *points) {
  self->acceptPoints(*points);
}

//  bool QQuickMultiPointHandler::grabPoints(QPointerEvent *event, const
//      QList<QEventPoint> &points)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickMultiPointHandler10grabPointsEP13QPointerEventRK5QListI11QEventPointE(
    QQuickMultiPointHandler *self,
    QPointerEvent *event,
    const QList<QEventPoint> *points) {
  return self->grabPoints(event, *points);
}

//  void QQuickMultiPointHandler::moveTarget(QPointF pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMultiPointHandler10moveTargetE7QPointF(
    QQuickMultiPointHandler *self,
    const QPointF *pos) {
  self->moveTarget(*pos);
}

//  QQuickMultiPointHandlerPrivate *QQuickMultiPointHandler::d_func()
extern "C" Q_DECL_EXPORT
QQuickMultiPointHandlerPrivate *ritual_ZN23QQuickMultiPointHandler6d_funcEv(
    QQuickMultiPointHandler *self) {
  return self->d_func();
}

//  const QQuickMultiPointHandlerPrivate *QQuickMultiPointHandler::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickMultiPointHandlerPrivate *ritual_ZNK23QQuickMultiPointHandler6d_funcEv(
    const QQuickMultiPointHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickMultiPointHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMultiPointHandler(
    QQuickMultiPointHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMultiPointHandler *>(self)->take(key, call);
}

//  bool QQuickMultiPointHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQuickMultiPointHandler17wantsPointerEventEP13QPointerEvent(
    QQuickMultiPointHandler *self,
    QPointerEvent *event) {
  return static_cast<OwnQQuickMultiPointHandler *>(self)->OwnQQuickMultiPointHandler::wantsPointerEvent(
      event);
}

//  void QQuickMultiPointHandler::handlePointerEventImpl(QPointerEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickMultiPointHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickMultiPointHandler *self,
    QPointerEvent *event) {
  static_cast<OwnQQuickMultiPointHandler *>(self)->OwnQQuickMultiPointHandler::handlePointerEventImpl(
      event);
}

//  void QQuickMultiPointHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickMultiPointHandler15onActiveChangedEv(
    QQuickMultiPointHandler *self) {
  static_cast<OwnQQuickMultiPointHandler *>(self)->OwnQQuickMultiPointHandler::onActiveChanged();
}
