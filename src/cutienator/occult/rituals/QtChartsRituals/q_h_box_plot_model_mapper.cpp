//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qhboxplotmodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qhboxplotmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHBoxPlotModelMapper that Python can take functions over in. Every QHBoxPlotModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHBoxPlotModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHBoxPlotModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxPlotModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxPlotModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxPlotModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxPlotModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBoxPlotModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHBoxPlotModelMapper : public QHBoxPlotModelMapper {
public:
  using QHBoxPlotModelMapper::QHBoxPlotModelMapper;
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
      CuteQHBoxPlotModelMapperCall0 call = reinterpret_cast<CuteQHBoxPlotModelMapperCall0>(taken[0]);
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
      CuteQHBoxPlotModelMapperCall1 call = reinterpret_cast<CuteQHBoxPlotModelMapperCall1>(taken[1]);
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
      CuteQHBoxPlotModelMapperCall2 call = reinterpret_cast<CuteQHBoxPlotModelMapperCall2>(taken[2]);
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
      CuteQHBoxPlotModelMapperCall3 call = reinterpret_cast<CuteQHBoxPlotModelMapperCall3>(taken[3]);
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
      CuteQHBoxPlotModelMapperCall4 call = reinterpret_cast<CuteQHBoxPlotModelMapperCall4>(taken[4]);
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
      CuteQHBoxPlotModelMapperCall5 call = reinterpret_cast<CuteQHBoxPlotModelMapperCall5>(taken[5]);
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
      CuteQHBoxPlotModelMapperCall6 call = reinterpret_cast<CuteQHBoxPlotModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHBoxPlotModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QHBoxPlotModelMapper10metaObjectEv(
    const QHBoxPlotModelMapper *self) {
  return self->metaObject();
}

//  QString QHBoxPlotModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QHBoxPlotModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHBoxPlotModelMapper::tr(s, c, n));
}

//  QHBoxPlotModelMapper::QHBoxPlotModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QHBoxPlotModelMapper *ritual_ZN20QHBoxPlotModelMapperC1EP7QObject(
    QObject *parent) {
  return new CuteQHBoxPlotModelMapper(parent);
}

//  QAbstractItemModel *QHBoxPlotModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK20QHBoxPlotModelMapper5modelEv(
    const QHBoxPlotModelMapper *self) {
  return self->model();
}

//  void QHBoxPlotModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHBoxPlotModelMapper8setModelEP18QAbstractItemModel(
    QHBoxPlotModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QBoxPlotSeries *QHBoxPlotModelMapper::series() const
extern "C" Q_DECL_EXPORT
QBoxPlotSeries *ritual_ZNK20QHBoxPlotModelMapper6seriesEv(
    const QHBoxPlotModelMapper *self) {
  return self->series();
}

//  void QHBoxPlotModelMapper::setSeries(QBoxPlotSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHBoxPlotModelMapper9setSeriesEP14QBoxPlotSeries(
    QHBoxPlotModelMapper *self,
    QBoxPlotSeries *series) {
  self->setSeries(series);
}

//  int QHBoxPlotModelMapper::firstBoxSetRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QHBoxPlotModelMapper14firstBoxSetRowEv(
    const QHBoxPlotModelMapper *self) {
  return self->firstBoxSetRow();
}

//  void QHBoxPlotModelMapper::setFirstBoxSetRow(int firstBoxSetRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHBoxPlotModelMapper17setFirstBoxSetRowEi(
    QHBoxPlotModelMapper *self,
    int firstBoxSetRow) {
  self->setFirstBoxSetRow(firstBoxSetRow);
}

//  int QHBoxPlotModelMapper::lastBoxSetRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QHBoxPlotModelMapper13lastBoxSetRowEv(
    const QHBoxPlotModelMapper *self) {
  return self->lastBoxSetRow();
}

//  void QHBoxPlotModelMapper::setLastBoxSetRow(int lastBoxSetRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHBoxPlotModelMapper16setLastBoxSetRowEi(
    QHBoxPlotModelMapper *self,
    int lastBoxSetRow) {
  self->setLastBoxSetRow(lastBoxSetRow);
}

//  int QHBoxPlotModelMapper::firstColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QHBoxPlotModelMapper11firstColumnEv(
    const QHBoxPlotModelMapper *self) {
  return self->firstColumn();
}

//  void QHBoxPlotModelMapper::setFirstColumn(int firstColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHBoxPlotModelMapper14setFirstColumnEi(
    QHBoxPlotModelMapper *self,
    int firstColumn) {
  self->setFirstColumn(firstColumn);
}

//  int QHBoxPlotModelMapper::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QHBoxPlotModelMapper11columnCountEv(
    const QHBoxPlotModelMapper *self) {
  return self->columnCount();
}

//  void QHBoxPlotModelMapper::setColumnCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHBoxPlotModelMapper14setColumnCountEi(
    QHBoxPlotModelMapper *self,
    int rowCount) {
  self->setColumnCount(rowCount);
}

//  a Python function taken by a CuteQHBoxPlotModelMapper, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHBoxPlotModelMapper(
    QHBoxPlotModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHBoxPlotModelMapper *>(self)->take(key, call);
}
