//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qbar3dseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbar3dseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBar3DSeries that Python can take functions over in. Every QBar3DSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBar3DSeriesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBar3DSeriesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBar3DSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBar3DSeries : public QBar3DSeries {
public:
  using QBar3DSeries::QBar3DSeries;
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
      CuteQBar3DSeriesCall0 call = reinterpret_cast<CuteQBar3DSeriesCall0>(taken[0]);
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
      CuteQBar3DSeriesCall1 call = reinterpret_cast<CuteQBar3DSeriesCall1>(taken[1]);
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
      CuteQBar3DSeriesCall2 call = reinterpret_cast<CuteQBar3DSeriesCall2>(taken[2]);
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
      CuteQBar3DSeriesCall3 call = reinterpret_cast<CuteQBar3DSeriesCall3>(taken[3]);
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
      CuteQBar3DSeriesCall4 call = reinterpret_cast<CuteQBar3DSeriesCall4>(taken[4]);
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
      CuteQBar3DSeriesCall5 call = reinterpret_cast<CuteQBar3DSeriesCall5>(taken[5]);
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
      CuteQBar3DSeriesCall6 call = reinterpret_cast<CuteQBar3DSeriesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBar3DSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QBar3DSeries10metaObjectEv(
    const QBar3DSeries *self) {
  return self->metaObject();
}

//  QString QBar3DSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QBar3DSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBar3DSeries::tr(s, c, n));
}

//  void QBar3DSeries::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries24qt_qmlMarker_uncreatableEv(
    QBar3DSeries *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QBar3DSeries::QBar3DSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZN12QBar3DSeriesC1EP7QObject(QObject *parent) {
  return new CuteQBar3DSeries(parent);
}

//  QBar3DSeries::QBar3DSeries(QBarDataProxy *dataProxy, QObject *parent)
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZN12QBar3DSeriesC1EP13QBarDataProxyP7QObject(
    QBarDataProxy *dataProxy,
    QObject *parent) {
  return new CuteQBar3DSeries(dataProxy, parent);
}

//  QBar3DSeries::~QBar3DSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeriesD1Ev(QBar3DSeries *self) {
  delete self;
}

//  void QBar3DSeries::setDataProxy(QBarDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries12setDataProxyEP13QBarDataProxy(
    QBar3DSeries *self,
    QBarDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  QBarDataProxy *QBar3DSeries::dataProxy() const
extern "C" Q_DECL_EXPORT
QBarDataProxy *ritual_ZNK12QBar3DSeries9dataProxyEv(
    const QBar3DSeries *self) {
  return self->dataProxy();
}

//  void QBar3DSeries::setSelectedBar(QPoint position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries14setSelectedBarE6QPoint(
    QBar3DSeries *self,
    const QPoint *position) {
  self->setSelectedBar(*position);
}

//  QPoint QBar3DSeries::selectedBar() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK12QBar3DSeries11selectedBarEv(const QBar3DSeries *self) {
  return new QPoint(self->selectedBar());
}

//  QPoint QBar3DSeries::invalidSelectionPosition()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN12QBar3DSeries24invalidSelectionPositionEv() {
  return new QPoint(QBar3DSeries::invalidSelectionPosition());
}

//  void QBar3DSeries::setMeshAngle(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries12setMeshAngleEf(
    QBar3DSeries *self,
    float angle) {
  self->setMeshAngle(angle);
}

//  float QBar3DSeries::meshAngle() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QBar3DSeries9meshAngleEv(const QBar3DSeries *self) {
  return self->meshAngle();
}

//  QList<QColor> QBar3DSeries::rowColors() const
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_ZNK12QBar3DSeries9rowColorsEv(
    const QBar3DSeries *self) {
  return new QList<QColor>(self->rowColors());
}

//  void QBar3DSeries::setRowColors(const QList<QColor> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries12setRowColorsERK5QListI6QColorE(
    QBar3DSeries *self,
    const QList<QColor> *colors) {
  self->setRowColors(*colors);
}

//  bool QBar3DSeries::isValueColoringEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QBar3DSeries22isValueColoringEnabledEv(
    const QBar3DSeries *self) {
  return self->isValueColoringEnabled();
}

//  void QBar3DSeries::setValueColoringEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries23setValueColoringEnabledEb(
    QBar3DSeries *self,
    bool enabled) {
  self->setValueColoringEnabled(enabled);
}

//  void QBar3DSeries::clearRow(qsizetype rowIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries8clearRowEx(
    QBar3DSeries *self,
    qsizetype rowIndex) {
  self->clearRow(rowIndex);
}

//  void QBar3DSeries::clearArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries10clearArrayEv(QBar3DSeries *self) {
  self->clearArray();
}

//  QStringList QBar3DSeries::rowLabels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QBar3DSeries9rowLabelsEv(
    const QBar3DSeries *self) {
  return new QList<QString>(self->rowLabels());
}

//  void QBar3DSeries::setRowLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries12setRowLabelsERK5QListI7QStringE(
    QBar3DSeries *self,
    const QList<QString> *labels) {
  self->setRowLabels(*labels);
}

//  QStringList QBar3DSeries::columnLabels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QBar3DSeries12columnLabelsEv(
    const QBar3DSeries *self) {
  return new QList<QString>(self->columnLabels());
}

//  void QBar3DSeries::setColumnLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries15setColumnLabelsERK5QListI7QStringE(
    QBar3DSeries *self,
    const QList<QString> *labels) {
  self->setColumnLabels(*labels);
}

//  QStringList QBar3DSeries::customRowLabels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QBar3DSeries15customRowLabelsEv(
    const QBar3DSeries *self) {
  return new QList<QString>(self->customRowLabels());
}

//  void QBar3DSeries::setCustomRowLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries18setCustomRowLabelsERK5QListI7QStringE(
    QBar3DSeries *self,
    const QList<QString> *labels) {
  self->setCustomRowLabels(*labels);
}

//  QStringList QBar3DSeries::customColumnLabels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QBar3DSeries18customColumnLabelsEv(
    const QBar3DSeries *self) {
  return new QList<QString>(self->customColumnLabels());
}

//  void QBar3DSeries::setCustomColumnLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries21setCustomColumnLabelsERK5QListI7QStringE(
    QBar3DSeries *self,
    const QList<QString> *labels) {
  self->setCustomColumnLabels(*labels);
}

//  void QBar3DSeries::setRowAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries10setRowAxisEP15QCategory3DAxis(
    QBar3DSeries *self,
    QCategory3DAxis *axis) {
  self->setRowAxis(axis);
}

//  void QBar3DSeries::setValueAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries12setValueAxisEP12QValue3DAxis(
    QBar3DSeries *self,
    QValue3DAxis *axis) {
  self->setValueAxis(axis);
}

//  void QBar3DSeries::setColumnAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries13setColumnAxisEP15QCategory3DAxis(
    QBar3DSeries *self,
    QCategory3DAxis *axis) {
  self->setColumnAxis(axis);
}

//  QCategory3DAxis *QBar3DSeries::rowAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK12QBar3DSeries7rowAxisEv(
    const QBar3DSeries *self) {
  return self->rowAxis();
}

//  QValue3DAxis *QBar3DSeries::valueAxis() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK12QBar3DSeries9valueAxisEv(
    const QBar3DSeries *self) {
  return self->valueAxis();
}

//  QCategory3DAxis *QBar3DSeries::columnAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK12QBar3DSeries10columnAxisEv(
    const QBar3DSeries *self) {
  return self->columnAxis();
}

//  void QBar3DSeries::resetRowAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries12resetRowAxisEv(QBar3DSeries *self) {
  self->resetRowAxis();
}

//  void QBar3DSeries::resetValueAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries14resetValueAxisEv(QBar3DSeries *self) {
  self->resetValueAxis();
}

//  void QBar3DSeries::resetColumnAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries15resetColumnAxisEv(QBar3DSeries *self) {
  self->resetColumnAxis();
}

//  void QBar3DSeries::connectSignals()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries14connectSignalsEv(QBar3DSeries *self) {
  self->connectSignals();
}

//  void QBar3DSeries::handleMeshRotationChanged(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBar3DSeries25handleMeshRotationChangedERK11QQuaternion(
    QBar3DSeries *self,
    const QQuaternion *rotation) {
  self->handleMeshRotationChanged(*rotation);
}

//  a Python function taken by a CuteQBar3DSeries, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBar3DSeries(
    QBar3DSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBar3DSeries *>(self)->take(key, call);
}

//  QList<QBar3DSeries *>::QList()
extern "C" Q_DECL_EXPORT
QList<QBar3DSeries *> *ritual_list_make_QBar3DSeries_ptr() {
  return new QList<QBar3DSeries *>();
}

//  void QList<QBar3DSeries *>::append(const QBar3DSeries * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBar3DSeries_ptr(
    QList<QBar3DSeries *> *self,
    QBar3DSeries *element) {
  self->append(element);
}

//  qsizetype QList<QBar3DSeries *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBar3DSeries_ptr(
    const QList<QBar3DSeries *> *self) {
  return self->size();
}

//  const QBar3DSeries * &QList<QBar3DSeries *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_list_at_QBar3DSeries_ptr(
    const QList<QBar3DSeries *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QBar3DSeries *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBar3DSeries_ptr(QList<QBar3DSeries *> *self) {
  delete self;
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
