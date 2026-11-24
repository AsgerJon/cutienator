//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickDrag that Python can take functions over in. Every QQuickDrag
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDragCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickDragCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickDragCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickDrag : public QQuickDrag {
public:
  using QQuickDrag::QQuickDrag;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDragCall0 call = reinterpret_cast<CuteQQuickDragCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDragCall1 call = reinterpret_cast<CuteQQuickDragCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickDragCall2 call = reinterpret_cast<CuteQQuickDragCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickDragCall3 call = reinterpret_cast<CuteQQuickDragCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickDragCall4 call = reinterpret_cast<CuteQQuickDragCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickDragCall5 call = reinterpret_cast<CuteQQuickDragCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickDragCall6 call = reinterpret_cast<CuteQQuickDragCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickDrag::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickDrag10metaObjectEv(
    const QQuickDrag *self) {
  return self->metaObject();
}

//  QString QQuickDrag::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickDrag2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDrag::tr(s, c, n));
}

//  void QQuickDrag::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag24qt_qmlMarker_uncreatableEv(QQuickDrag *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QQuickDrag::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag21qt_qmlMarker_attachedEv(QQuickDrag *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickDrag::QQuickDrag(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickDrag *ritual_ZN10QQuickDragC1EP7QObject(QObject *parent) {
  return new CuteQQuickDrag(parent);
}

//  QQuickDrag::~QQuickDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDragD1Ev(QQuickDrag *self) {
  delete self;
}

//  QQuickItem *QQuickDrag::target() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK10QQuickDrag6targetEv(const QQuickDrag *self) {
  return self->target();
}

//  void QQuickDrag::setTarget(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag9setTargetEP10QQuickItem(
    QQuickDrag *self,
    QQuickItem *target) {
  self->setTarget(target);
}

//  void QQuickDrag::resetTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag11resetTargetEv(QQuickDrag *self) {
  self->resetTarget();
}

//  Axis QQuickDrag::axis() const
extern "C" Q_DECL_EXPORT
QQuickDrag::Axis ritual_ZNK10QQuickDrag4axisEv(const QQuickDrag *self) {
  return self->axis();
}

//  void QQuickDrag::setAxis(Axis a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag7setAxisENS_4AxisE(
    QQuickDrag *self,
    QQuickDrag::Axis a0) {
  self->setAxis(a0);
}

//  qreal QQuickDrag::xmin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDrag4xminEv(const QQuickDrag *self) {
  return self->xmin();
}

//  void QQuickDrag::setXmin(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag7setXminEd(QQuickDrag *self, qreal a0) {
  self->setXmin(a0);
}

//  qreal QQuickDrag::xmax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDrag4xmaxEv(const QQuickDrag *self) {
  return self->xmax();
}

//  void QQuickDrag::setXmax(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag7setXmaxEd(QQuickDrag *self, qreal a0) {
  self->setXmax(a0);
}

//  qreal QQuickDrag::ymin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDrag4yminEv(const QQuickDrag *self) {
  return self->ymin();
}

//  void QQuickDrag::setYmin(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag7setYminEd(QQuickDrag *self, qreal a0) {
  self->setYmin(a0);
}

//  qreal QQuickDrag::ymax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDrag4ymaxEv(const QQuickDrag *self) {
  return self->ymax();
}

//  void QQuickDrag::setYmax(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag7setYmaxEd(QQuickDrag *self, qreal a0) {
  self->setYmax(a0);
}

//  bool QQuickDrag::smoothed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickDrag8smoothedEv(const QQuickDrag *self) {
  return self->smoothed();
}

//  void QQuickDrag::setSmoothed(bool smooth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag11setSmoothedEb(QQuickDrag *self, bool smooth) {
  self->setSmoothed(smooth);
}

//  qreal QQuickDrag::threshold() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickDrag9thresholdEv(const QQuickDrag *self) {
  return self->threshold();
}

//  void QQuickDrag::setThreshold(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag12setThresholdEd(QQuickDrag *self, qreal a0) {
  self->setThreshold(a0);
}

//  void QQuickDrag::resetThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag14resetThresholdEv(QQuickDrag *self) {
  self->resetThreshold();
}

//  bool QQuickDrag::active() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickDrag6activeEv(const QQuickDrag *self) {
  return self->active();
}

//  void QQuickDrag::setActive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag9setActiveEb(QQuickDrag *self, bool a0) {
  self->setActive(a0);
}

//  bool QQuickDrag::filterChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickDrag14filterChildrenEv(const QQuickDrag *self) {
  return self->filterChildren();
}

//  void QQuickDrag::setFilterChildren(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickDrag17setFilterChildrenEb(QQuickDrag *self, bool a0) {
  self->setFilterChildren(a0);
}

//  QQuickDragAttached *QQuickDrag::qmlAttachedProperties(QObject *obj)
extern "C" Q_DECL_EXPORT
QQuickDragAttached *ritual_ZN10QQuickDrag21qmlAttachedPropertiesEP7QObject(
    QObject *obj) {
  return QQuickDrag::qmlAttachedProperties(obj);
}

//  a Python function taken by a CuteQQuickDrag, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDrag(QQuickDrag *self, const char *key, void *call) {
  return static_cast<CuteQQuickDrag *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_draganddrop)
