//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qscatter3dseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qscatter3dseries.h>
#include <QtCore/qstring.h>
#include <QtGraphs/qscatterdataitem.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QScatter3DSeries that Python can take functions over in. Every QScatter3DSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatter3DSeriesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatter3DSeriesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatter3DSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScatter3DSeries : public QScatter3DSeries {
public:
  using QScatter3DSeries::QScatter3DSeries;
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
      CuteQScatter3DSeriesCall0 call = reinterpret_cast<CuteQScatter3DSeriesCall0>(taken[0]);
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
      CuteQScatter3DSeriesCall1 call = reinterpret_cast<CuteQScatter3DSeriesCall1>(taken[1]);
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
      CuteQScatter3DSeriesCall2 call = reinterpret_cast<CuteQScatter3DSeriesCall2>(taken[2]);
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
      CuteQScatter3DSeriesCall3 call = reinterpret_cast<CuteQScatter3DSeriesCall3>(taken[3]);
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
      CuteQScatter3DSeriesCall4 call = reinterpret_cast<CuteQScatter3DSeriesCall4>(taken[4]);
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
      CuteQScatter3DSeriesCall5 call = reinterpret_cast<CuteQScatter3DSeriesCall5>(taken[5]);
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
      CuteQScatter3DSeriesCall6 call = reinterpret_cast<CuteQScatter3DSeriesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScatter3DSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QScatter3DSeries10metaObjectEv(
    const QScatter3DSeries *self) {
  return self->metaObject();
}

//  QString QScatter3DSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QScatter3DSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScatter3DSeries::tr(s, c, n));
}

//  QScatter3DSeriesPrivate *QScatter3DSeries::d_func()
extern "C" Q_DECL_EXPORT
QScatter3DSeriesPrivate *ritual_ZN16QScatter3DSeries6d_funcEv(
    QScatter3DSeries *self) {
  return self->d_func();
}

//  const QScatter3DSeriesPrivate *QScatter3DSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QScatter3DSeriesPrivate *ritual_ZNK16QScatter3DSeries6d_funcEv(
    const QScatter3DSeries *self) {
  return self->d_func();
}

//  void QScatter3DSeries::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries24qt_qmlMarker_uncreatableEv(
    QScatter3DSeries *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QScatter3DSeries::QScatter3DSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZN16QScatter3DSeriesC1EP7QObject(QObject *parent) {
  return new CuteQScatter3DSeries(parent);
}

//  QScatter3DSeries::QScatter3DSeries(QScatterDataProxy *dataProxy, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZN16QScatter3DSeriesC1EP17QScatterDataProxyP7QObject(
    QScatterDataProxy *dataProxy,
    QObject *parent) {
  return new CuteQScatter3DSeries(dataProxy, parent);
}

//  QScatter3DSeries::~QScatter3DSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeriesD1Ev(QScatter3DSeries *self) {
  delete self;
}

//  void QScatter3DSeries::setDataProxy(QScatterDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries12setDataProxyEP17QScatterDataProxy(
    QScatter3DSeries *self,
    QScatterDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  QScatterDataProxy *QScatter3DSeries::dataProxy() const
extern "C" Q_DECL_EXPORT
QScatterDataProxy *ritual_ZNK16QScatter3DSeries9dataProxyEv(
    const QScatter3DSeries *self) {
  return self->dataProxy();
}

//  void QScatter3DSeries::setSelectedItem(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries15setSelectedItemEx(
    QScatter3DSeries *self,
    qsizetype index) {
  self->setSelectedItem(index);
}

//  qsizetype QScatter3DSeries::selectedItem() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QScatter3DSeries12selectedItemEv(
    const QScatter3DSeries *self) {
  return self->selectedItem();
}

//  qsizetype QScatter3DSeries::invalidSelectionIndex()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN16QScatter3DSeries21invalidSelectionIndexEv() {
  return QScatter3DSeries::invalidSelectionIndex();
}

//  void QScatter3DSeries::setItemSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries11setItemSizeEf(
    QScatter3DSeries *self,
    float size) {
  self->setItemSize(size);
}

//  float QScatter3DSeries::itemSize() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QScatter3DSeries8itemSizeEv(const QScatter3DSeries *self) {
  return self->itemSize();
}

//  void QScatter3DSeries::setDataArray(const QScatterDataArray
//      &newDataArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries12setDataArrayERK5QListI16QScatterDataItemE(
    QScatter3DSeries *self,
    const QList<QScatterDataItem> *newDataArray) {
  self->setDataArray(*newDataArray);
}

//  void QScatter3DSeries::clearArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries10clearArrayEv(QScatter3DSeries *self) {
  self->clearArray();
}

//  const QScatterDataArray &QScatter3DSeries::dataArray() const
extern "C" Q_DECL_EXPORT
QList<QScatterDataItem> *ritual_ZNKR16QScatter3DSeries9dataArrayEv(
    const QScatter3DSeries *self) {
  return new QList<QScatterDataItem>(self->dataArray());
}

//  void QScatter3DSeries::setScaleArray(const QList<QVector3D>
//      &newScaleArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries13setScaleArrayERK5QListI9QVector3DE(
    QScatter3DSeries *self,
    const QList<QVector3D> *newScaleArray) {
  self->setScaleArray(*newScaleArray);
}

//  void QScatter3DSeries::clearScaleArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries15clearScaleArrayEv(QScatter3DSeries *self) {
  self->clearScaleArray();
}

//  const QList<QVector3D> &QScatter3DSeries::scaleArray() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNKR16QScatter3DSeries10scaleArrayEv(
    const QScatter3DSeries *self) {
  return new QList<QVector3D>(self->scaleArray());
}

//  void QScatter3DSeries::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries8setAxisXEP12QValue3DAxis(
    QScatter3DSeries *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  void QScatter3DSeries::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries8setAxisYEP12QValue3DAxis(
    QScatter3DSeries *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  void QScatter3DSeries::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries8setAxisZEP12QValue3DAxis(
    QScatter3DSeries *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  QValue3DAxis *QScatter3DSeries::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK16QScatter3DSeries5axisXEv(
    const QScatter3DSeries *self) {
  return self->axisX();
}

//  QValue3DAxis *QScatter3DSeries::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK16QScatter3DSeries5axisYEv(
    const QScatter3DSeries *self) {
  return self->axisY();
}

//  QValue3DAxis *QScatter3DSeries::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK16QScatter3DSeries5axisZEv(
    const QScatter3DSeries *self) {
  return self->axisZ();
}

//  void QScatter3DSeries::resetAxisX()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries10resetAxisXEv(QScatter3DSeries *self) {
  self->resetAxisX();
}

//  void QScatter3DSeries::resetAxisY()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries10resetAxisYEv(QScatter3DSeries *self) {
  self->resetAxisY();
}

//  void QScatter3DSeries::resetAxisZ()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatter3DSeries10resetAxisZEv(QScatter3DSeries *self) {
  self->resetAxisZ();
}

//  a Python function taken by a CuteQScatter3DSeries, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScatter3DSeries(
    QScatter3DSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScatter3DSeries *>(self)->take(key, call);
}

//  QList<QScatter3DSeries *>::QList()
extern "C" Q_DECL_EXPORT
QList<QScatter3DSeries *> *ritual_list_make_QScatter3DSeries_ptr() {
  return new QList<QScatter3DSeries *>();
}

//  void QList<QScatter3DSeries *>::append(const QScatter3DSeries * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QScatter3DSeries_ptr(
    QList<QScatter3DSeries *> *self,
    QScatter3DSeries *element) {
  self->append(element);
}

//  qsizetype QList<QScatter3DSeries *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QScatter3DSeries_ptr(
    const QList<QScatter3DSeries *> *self) {
  return self->size();
}

//  const QScatter3DSeries * &QList<QScatter3DSeries *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_list_at_QScatter3DSeries_ptr(
    const QList<QScatter3DSeries *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QScatter3DSeries *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QScatter3DSeries_ptr(QList<QScatter3DSeries *> *self) {
  delete self;
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
