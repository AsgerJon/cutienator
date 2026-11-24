//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qvpiemodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/qvpiemodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVPieModelMapper that Python can take functions over in. Every QVPieModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVPieModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVPieModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVPieModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVPieModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVPieModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVPieModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVPieModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVPieModelMapper : public QVPieModelMapper {
public:
  using QVPieModelMapper::QVPieModelMapper;
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
      CuteQVPieModelMapperCall0 call = reinterpret_cast<CuteQVPieModelMapperCall0>(taken[0]);
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
      CuteQVPieModelMapperCall1 call = reinterpret_cast<CuteQVPieModelMapperCall1>(taken[1]);
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
      CuteQVPieModelMapperCall2 call = reinterpret_cast<CuteQVPieModelMapperCall2>(taken[2]);
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
      CuteQVPieModelMapperCall3 call = reinterpret_cast<CuteQVPieModelMapperCall3>(taken[3]);
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
      CuteQVPieModelMapperCall4 call = reinterpret_cast<CuteQVPieModelMapperCall4>(taken[4]);
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
      CuteQVPieModelMapperCall5 call = reinterpret_cast<CuteQVPieModelMapperCall5>(taken[5]);
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
      CuteQVPieModelMapperCall6 call = reinterpret_cast<CuteQVPieModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVPieModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QVPieModelMapper10metaObjectEv(
    const QVPieModelMapper *self) {
  return self->metaObject();
}

//  QString QVPieModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QVPieModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVPieModelMapper::tr(s, c, n));
}

//  QVPieModelMapper::QVPieModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QVPieModelMapper *ritual_ZN16QVPieModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQVPieModelMapper(parent);
}

//  QAbstractItemModel *QVPieModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK16QVPieModelMapper5modelEv(
    const QVPieModelMapper *self) {
  return self->model();
}

//  void QVPieModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVPieModelMapper8setModelEP18QAbstractItemModel(
    QVPieModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QPieSeries *QVPieModelMapper::series() const
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZNK16QVPieModelMapper6seriesEv(
    const QVPieModelMapper *self) {
  return self->series();
}

//  void QVPieModelMapper::setSeries(QPieSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVPieModelMapper9setSeriesEP10QPieSeries(
    QVPieModelMapper *self,
    QPieSeries *series) {
  self->setSeries(series);
}

//  int QVPieModelMapper::valuesColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QVPieModelMapper12valuesColumnEv(
    const QVPieModelMapper *self) {
  return self->valuesColumn();
}

//  void QVPieModelMapper::setValuesColumn(int valuesColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVPieModelMapper15setValuesColumnEi(
    QVPieModelMapper *self,
    int valuesColumn) {
  self->setValuesColumn(valuesColumn);
}

//  int QVPieModelMapper::labelsColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QVPieModelMapper12labelsColumnEv(
    const QVPieModelMapper *self) {
  return self->labelsColumn();
}

//  void QVPieModelMapper::setLabelsColumn(int labelsColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVPieModelMapper15setLabelsColumnEi(
    QVPieModelMapper *self,
    int labelsColumn) {
  self->setLabelsColumn(labelsColumn);
}

//  int QVPieModelMapper::firstRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QVPieModelMapper8firstRowEv(const QVPieModelMapper *self) {
  return self->firstRow();
}

//  void QVPieModelMapper::setFirstRow(int firstRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVPieModelMapper11setFirstRowEi(
    QVPieModelMapper *self,
    int firstRow) {
  self->setFirstRow(firstRow);
}

//  int QVPieModelMapper::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QVPieModelMapper8rowCountEv(const QVPieModelMapper *self) {
  return self->rowCount();
}

//  void QVPieModelMapper::setRowCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVPieModelMapper11setRowCountEi(
    QVPieModelMapper *self,
    int rowCount) {
  self->setRowCount(rowCount);
}

//  a Python function taken by a CuteQVPieModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVPieModelMapper(
    QVPieModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVPieModelMapper *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_pie_chart)
