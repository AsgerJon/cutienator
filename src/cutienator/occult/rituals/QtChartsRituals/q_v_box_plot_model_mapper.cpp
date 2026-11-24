//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qvboxplotmodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/qvboxplotmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVBoxPlotModelMapper that Python can take functions over in. Every QVBoxPlotModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVBoxPlotModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVBoxPlotModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxPlotModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxPlotModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxPlotModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxPlotModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBoxPlotModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVBoxPlotModelMapper : public QVBoxPlotModelMapper {
public:
  using QVBoxPlotModelMapper::QVBoxPlotModelMapper;
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
      CuteQVBoxPlotModelMapperCall0 call = reinterpret_cast<CuteQVBoxPlotModelMapperCall0>(taken[0]);
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
      CuteQVBoxPlotModelMapperCall1 call = reinterpret_cast<CuteQVBoxPlotModelMapperCall1>(taken[1]);
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
      CuteQVBoxPlotModelMapperCall2 call = reinterpret_cast<CuteQVBoxPlotModelMapperCall2>(taken[2]);
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
      CuteQVBoxPlotModelMapperCall3 call = reinterpret_cast<CuteQVBoxPlotModelMapperCall3>(taken[3]);
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
      CuteQVBoxPlotModelMapperCall4 call = reinterpret_cast<CuteQVBoxPlotModelMapperCall4>(taken[4]);
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
      CuteQVBoxPlotModelMapperCall5 call = reinterpret_cast<CuteQVBoxPlotModelMapperCall5>(taken[5]);
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
      CuteQVBoxPlotModelMapperCall6 call = reinterpret_cast<CuteQVBoxPlotModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVBoxPlotModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QVBoxPlotModelMapper10metaObjectEv(
    const QVBoxPlotModelMapper *self) {
  return self->metaObject();
}

//  QString QVBoxPlotModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QVBoxPlotModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVBoxPlotModelMapper::tr(s, c, n));
}

//  QVBoxPlotModelMapper::QVBoxPlotModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QVBoxPlotModelMapper *ritual_ZN20QVBoxPlotModelMapperC1EP7QObject(
    QObject *parent) {
  return new CuteQVBoxPlotModelMapper(parent);
}

//  QAbstractItemModel *QVBoxPlotModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK20QVBoxPlotModelMapper5modelEv(
    const QVBoxPlotModelMapper *self) {
  return self->model();
}

//  void QVBoxPlotModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVBoxPlotModelMapper8setModelEP18QAbstractItemModel(
    QVBoxPlotModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QBoxPlotSeries *QVBoxPlotModelMapper::series() const
extern "C" Q_DECL_EXPORT
QBoxPlotSeries *ritual_ZNK20QVBoxPlotModelMapper6seriesEv(
    const QVBoxPlotModelMapper *self) {
  return self->series();
}

//  void QVBoxPlotModelMapper::setSeries(QBoxPlotSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVBoxPlotModelMapper9setSeriesEP14QBoxPlotSeries(
    QVBoxPlotModelMapper *self,
    QBoxPlotSeries *series) {
  self->setSeries(series);
}

//  int QVBoxPlotModelMapper::firstBoxSetColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QVBoxPlotModelMapper17firstBoxSetColumnEv(
    const QVBoxPlotModelMapper *self) {
  return self->firstBoxSetColumn();
}

//  void QVBoxPlotModelMapper::setFirstBoxSetColumn(int firstBoxSetColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVBoxPlotModelMapper20setFirstBoxSetColumnEi(
    QVBoxPlotModelMapper *self,
    int firstBoxSetColumn) {
  self->setFirstBoxSetColumn(firstBoxSetColumn);
}

//  int QVBoxPlotModelMapper::lastBoxSetColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QVBoxPlotModelMapper16lastBoxSetColumnEv(
    const QVBoxPlotModelMapper *self) {
  return self->lastBoxSetColumn();
}

//  void QVBoxPlotModelMapper::setLastBoxSetColumn(int lastBoxSetColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVBoxPlotModelMapper19setLastBoxSetColumnEi(
    QVBoxPlotModelMapper *self,
    int lastBoxSetColumn) {
  self->setLastBoxSetColumn(lastBoxSetColumn);
}

//  int QVBoxPlotModelMapper::firstRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QVBoxPlotModelMapper8firstRowEv(
    const QVBoxPlotModelMapper *self) {
  return self->firstRow();
}

//  void QVBoxPlotModelMapper::setFirstRow(int firstRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVBoxPlotModelMapper11setFirstRowEi(
    QVBoxPlotModelMapper *self,
    int firstRow) {
  self->setFirstRow(firstRow);
}

//  int QVBoxPlotModelMapper::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QVBoxPlotModelMapper8rowCountEv(
    const QVBoxPlotModelMapper *self) {
  return self->rowCount();
}

//  void QVBoxPlotModelMapper::setRowCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVBoxPlotModelMapper11setRowCountEi(
    QVBoxPlotModelMapper *self,
    int rowCount) {
  self->setRowCount(rowCount);
}

//  a Python function taken by a CuteQVBoxPlotModelMapper, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVBoxPlotModelMapper(
    QVBoxPlotModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVBoxPlotModelMapper *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_boxplot_chart)
