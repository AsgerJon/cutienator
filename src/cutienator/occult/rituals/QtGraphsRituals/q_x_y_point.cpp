//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qxypoint_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qxypoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QXYPoint that Python can take functions over in. Every QXYPoint
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYPointCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYPointCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYPointCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYPointCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYPointCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYPointCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYPointCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQXYPoint : public QXYPoint {
public:
  using QXYPoint::QXYPoint;
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
      CuteQXYPointCall0 call = reinterpret_cast<CuteQXYPointCall0>(taken[0]);
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
      CuteQXYPointCall1 call = reinterpret_cast<CuteQXYPointCall1>(taken[1]);
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
      CuteQXYPointCall2 call = reinterpret_cast<CuteQXYPointCall2>(taken[2]);
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
      CuteQXYPointCall3 call = reinterpret_cast<CuteQXYPointCall3>(taken[3]);
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
      CuteQXYPointCall4 call = reinterpret_cast<CuteQXYPointCall4>(taken[4]);
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
      CuteQXYPointCall5 call = reinterpret_cast<CuteQXYPointCall5>(taken[5]);
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
      CuteQXYPointCall6 call = reinterpret_cast<CuteQXYPointCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QXYPoint::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QXYPoint10metaObjectEv(const QXYPoint *self) {
  return self->metaObject();
}

//  void *QXYPoint::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8QXYPoint11qt_metacastEPKc(QXYPoint *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QXYPoint::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QXYPoint11qt_metacallEN11QMetaObject4CallEiPPv(
    QXYPoint *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QXYPoint as the QPointF it is built on
extern "C" Q_DECL_EXPORT
QPointF *ritual_cast_QXYPoint_QPointF(QXYPoint *self) {
  return static_cast<QPointF *>(self);
}

//  a Python function taken by a CuteQXYPoint, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXYPoint(QXYPoint *self, const char *key, void *call) {
  return static_cast<CuteQXYPoint *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
