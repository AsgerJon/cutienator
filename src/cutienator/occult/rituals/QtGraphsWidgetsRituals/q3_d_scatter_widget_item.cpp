//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphsWidgets/q3dscatterwidgetitem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphsWidgets/qgraphswidgetsglobal.h>
#if QT_CONFIG(graphs_3d_scatter3d)
#include <QtGraphsWidgets/q3dscatterwidgetitem.h>
#include <QtCore/qstring.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qscatter3dseries.h>
#include <QtGraphs/qvalue3daxis.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on Q3DScatterWidgetItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQ3DScatterWidgetItem : Q3DScatterWidgetItem {
  using Q3DScatterWidgetItem::event;
};

//  A Q3DScatterWidgetItem that Python can take functions over in. Every Q3DScatterWidgetItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DScatterWidgetItemCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DScatterWidgetItemCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterWidgetItemCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterWidgetItemCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterWidgetItemCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterWidgetItemCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DScatterWidgetItemCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DScatterWidgetItem : public Q3DScatterWidgetItem {
public:
  using Q3DScatterWidgetItem::Q3DScatterWidgetItem;
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
  //  bool Q3DScatterWidgetItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DScatterWidgetItemCall0 call = reinterpret_cast<CuteQ3DScatterWidgetItemCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return Q3DScatterWidgetItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool Q3DGraphsWidgetItem::eventFilter(QObject *obj, QEvent *event)
  bool eventFilter(QObject *obj, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DScatterWidgetItemCall1 call = reinterpret_cast<CuteQ3DScatterWidgetItemCall1>(taken[1]);
      bool given = call(this, obj, event, &handled);
      if (handled) return given;
    }
    return Q3DGraphsWidgetItem::eventFilter(obj, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQ3DScatterWidgetItemCall2 call = reinterpret_cast<CuteQ3DScatterWidgetItemCall2>(taken[2]);
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
      CuteQ3DScatterWidgetItemCall3 call = reinterpret_cast<CuteQ3DScatterWidgetItemCall3>(taken[3]);
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
      CuteQ3DScatterWidgetItemCall4 call = reinterpret_cast<CuteQ3DScatterWidgetItemCall4>(taken[4]);
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
      CuteQ3DScatterWidgetItemCall5 call = reinterpret_cast<CuteQ3DScatterWidgetItemCall5>(taken[5]);
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
      CuteQ3DScatterWidgetItemCall6 call = reinterpret_cast<CuteQ3DScatterWidgetItemCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DScatterWidgetItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20Q3DScatterWidgetItem10metaObjectEv(
    const Q3DScatterWidgetItem *self) {
  return self->metaObject();
}

//  QString Q3DScatterWidgetItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20Q3DScatterWidgetItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DScatterWidgetItem::tr(s, c, n));
}

//  Q3DScatterWidgetItem::Q3DScatterWidgetItem(QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DScatterWidgetItem *ritual_ZN20Q3DScatterWidgetItemC1EP7QObject(
    QObject *parent) {
  return new CuteQ3DScatterWidgetItem(parent);
}

//  Q3DScatterWidgetItem::~Q3DScatterWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DScatterWidgetItemD1Ev(Q3DScatterWidgetItem *self) {
  delete self;
}

//  void Q3DScatterWidgetItem::addSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DScatterWidgetItem9addSeriesEP16QScatter3DSeries(
    Q3DScatterWidgetItem *self,
    QScatter3DSeries *series) {
  self->addSeries(series);
}

//  void Q3DScatterWidgetItem::removeSeries(QScatter3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DScatterWidgetItem12removeSeriesEP16QScatter3DSeries(
    Q3DScatterWidgetItem *self,
    QScatter3DSeries *series) {
  self->removeSeries(series);
}

//  QList<QScatter3DSeries *> Q3DScatterWidgetItem::seriesList() const
extern "C" Q_DECL_EXPORT
QList<QScatter3DSeries *> *ritual_ZNK20Q3DScatterWidgetItem10seriesListEv(
    const Q3DScatterWidgetItem *self) {
  return new QList<QScatter3DSeries *>(self->seriesList());
}

//  QValue3DAxis *Q3DScatterWidgetItem::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK20Q3DScatterWidgetItem5axisXEv(
    const Q3DScatterWidgetItem *self) {
  return self->axisX();
}

//  QValue3DAxis *Q3DScatterWidgetItem::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK20Q3DScatterWidgetItem5axisYEv(
    const Q3DScatterWidgetItem *self) {
  return self->axisY();
}

//  QValue3DAxis *Q3DScatterWidgetItem::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK20Q3DScatterWidgetItem5axisZEv(
    const Q3DScatterWidgetItem *self) {
  return self->axisZ();
}

//  void Q3DScatterWidgetItem::addAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DScatterWidgetItem7addAxisEP12QValue3DAxis(
    Q3DScatterWidgetItem *self,
    QValue3DAxis *axis) {
  self->addAxis(axis);
}

//  void Q3DScatterWidgetItem::releaseAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DScatterWidgetItem11releaseAxisEP12QValue3DAxis(
    Q3DScatterWidgetItem *self,
    QValue3DAxis *axis) {
  self->releaseAxis(axis);
}

//  QList<QValue3DAxis *> Q3DScatterWidgetItem::axes() const
extern "C" Q_DECL_EXPORT
QList<QValue3DAxis *> *ritual_ZNK20Q3DScatterWidgetItem4axesEv(
    const Q3DScatterWidgetItem *self) {
  return new QList<QValue3DAxis *>(self->axes());
}

//  QScatter3DSeries *Q3DScatterWidgetItem::selectedSeries() const
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZNK20Q3DScatterWidgetItem14selectedSeriesEv(
    const Q3DScatterWidgetItem *self) {
  return self->selectedSeries();
}

//  void Q3DScatterWidgetItem::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DScatterWidgetItem8setAxisXEP12QValue3DAxis(
    Q3DScatterWidgetItem *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  void Q3DScatterWidgetItem::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DScatterWidgetItem8setAxisYEP12QValue3DAxis(
    Q3DScatterWidgetItem *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  void Q3DScatterWidgetItem::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DScatterWidgetItem8setAxisZEP12QValue3DAxis(
    Q3DScatterWidgetItem *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  bool Q3DScatterWidgetItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20Q3DScatterWidgetItem5eventEP6QEvent(
    Q3DScatterWidgetItem *self,
    QEvent *event) {
  return self->event(event);
}

//  Q3DScatterWidgetItemPrivate *Q3DScatterWidgetItem::d_func()
extern "C" Q_DECL_EXPORT
Q3DScatterWidgetItemPrivate *ritual_ZN20Q3DScatterWidgetItem6d_funcEv(
    Q3DScatterWidgetItem *self) {
  return self->d_func();
}

//  const Q3DScatterWidgetItemPrivate *Q3DScatterWidgetItem::d_func() const
extern "C" Q_DECL_EXPORT
const Q3DScatterWidgetItemPrivate *ritual_ZNK20Q3DScatterWidgetItem6d_funcEv(
    const Q3DScatterWidgetItem *self) {
  return self->d_func();
}

//  QQuickGraphsScatter *Q3DScatterWidgetItem::graphScatter()
extern "C" Q_DECL_EXPORT
QQuickGraphsScatter *ritual_ZN20Q3DScatterWidgetItem12graphScatterEv(
    Q3DScatterWidgetItem *self) {
  return self->graphScatter();
}

//  const QQuickGraphsScatter *Q3DScatterWidgetItem::graphScatter() const
extern "C" Q_DECL_EXPORT
const QQuickGraphsScatter *ritual_ZNK20Q3DScatterWidgetItem12graphScatterEv(
    const Q3DScatterWidgetItem *self) {
  return self->graphScatter();
}

//  a Python function taken by a CuteQ3DScatterWidgetItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DScatterWidgetItem(
    Q3DScatterWidgetItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DScatterWidgetItem *>(self)->take(key, call);
}

//  bool Q3DScatterWidgetItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20Q3DScatterWidgetItem5eventEP6QEvent(
    Q3DScatterWidgetItem *self,
    QEvent *event) {
  return static_cast<OwnQ3DScatterWidgetItem *>(self)->OwnQ3DScatterWidgetItem::event(
      event);
}

#endif  // QT_CONFIG(graphs_3d_scatter3d)
