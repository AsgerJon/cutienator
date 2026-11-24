//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qhpiemodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/qhpiemodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHPieModelMapper that Python can take functions over in. Every QHPieModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHPieModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHPieModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHPieModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHPieModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHPieModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHPieModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHPieModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHPieModelMapper : public QHPieModelMapper {
public:
  using QHPieModelMapper::QHPieModelMapper;
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
      CuteQHPieModelMapperCall0 call = reinterpret_cast<CuteQHPieModelMapperCall0>(taken[0]);
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
      CuteQHPieModelMapperCall1 call = reinterpret_cast<CuteQHPieModelMapperCall1>(taken[1]);
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
      CuteQHPieModelMapperCall2 call = reinterpret_cast<CuteQHPieModelMapperCall2>(taken[2]);
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
      CuteQHPieModelMapperCall3 call = reinterpret_cast<CuteQHPieModelMapperCall3>(taken[3]);
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
      CuteQHPieModelMapperCall4 call = reinterpret_cast<CuteQHPieModelMapperCall4>(taken[4]);
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
      CuteQHPieModelMapperCall5 call = reinterpret_cast<CuteQHPieModelMapperCall5>(taken[5]);
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
      CuteQHPieModelMapperCall6 call = reinterpret_cast<CuteQHPieModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHPieModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QHPieModelMapper10metaObjectEv(
    const QHPieModelMapper *self) {
  return self->metaObject();
}

//  QString QHPieModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QHPieModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHPieModelMapper::tr(s, c, n));
}

//  QHPieModelMapper::QHPieModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QHPieModelMapper *ritual_ZN16QHPieModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQHPieModelMapper(parent);
}

//  QAbstractItemModel *QHPieModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK16QHPieModelMapper5modelEv(
    const QHPieModelMapper *self) {
  return self->model();
}

//  void QHPieModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHPieModelMapper8setModelEP18QAbstractItemModel(
    QHPieModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QPieSeries *QHPieModelMapper::series() const
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZNK16QHPieModelMapper6seriesEv(
    const QHPieModelMapper *self) {
  return self->series();
}

//  void QHPieModelMapper::setSeries(QPieSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHPieModelMapper9setSeriesEP10QPieSeries(
    QHPieModelMapper *self,
    QPieSeries *series) {
  self->setSeries(series);
}

//  int QHPieModelMapper::valuesRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHPieModelMapper9valuesRowEv(const QHPieModelMapper *self) {
  return self->valuesRow();
}

//  void QHPieModelMapper::setValuesRow(int valuesRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHPieModelMapper12setValuesRowEi(
    QHPieModelMapper *self,
    int valuesRow) {
  self->setValuesRow(valuesRow);
}

//  int QHPieModelMapper::labelsRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHPieModelMapper9labelsRowEv(const QHPieModelMapper *self) {
  return self->labelsRow();
}

//  void QHPieModelMapper::setLabelsRow(int labelsRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHPieModelMapper12setLabelsRowEi(
    QHPieModelMapper *self,
    int labelsRow) {
  self->setLabelsRow(labelsRow);
}

//  int QHPieModelMapper::firstColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHPieModelMapper11firstColumnEv(
    const QHPieModelMapper *self) {
  return self->firstColumn();
}

//  void QHPieModelMapper::setFirstColumn(int firstColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHPieModelMapper14setFirstColumnEi(
    QHPieModelMapper *self,
    int firstColumn) {
  self->setFirstColumn(firstColumn);
}

//  int QHPieModelMapper::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHPieModelMapper11columnCountEv(
    const QHPieModelMapper *self) {
  return self->columnCount();
}

//  void QHPieModelMapper::setColumnCount(int columnCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHPieModelMapper14setColumnCountEi(
    QHPieModelMapper *self,
    int columnCount) {
  self->setColumnCount(columnCount);
}

//  a Python function taken by a CuteQHPieModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHPieModelMapper(
    QHPieModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHPieModelMapper *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_pie_chart)
