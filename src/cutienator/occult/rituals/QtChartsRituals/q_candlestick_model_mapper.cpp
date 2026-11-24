//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qcandlestickmodelmapper.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_candlestick_chart)
#include <QtCharts/qcandlestickmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCandlestickModelMapper that Python can take functions over in. Every QCandlestickModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQCandlestickModelMapperCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickModelMapperCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickModelMapperCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickModelMapperCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickModelMapperCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickModelMapperCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickModelMapperCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCandlestickModelMapper : public QCandlestickModelMapper {
public:
  using QCandlestickModelMapper::QCandlestickModelMapper;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QCandlestickModelMapper11orientationEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  Qt::Orientation QCandlestickModelMapper::orientation() const
  Qt::Orientation orientation() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCandlestickModelMapperCall0 call = reinterpret_cast<CuteQCandlestickModelMapperCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::Orientation>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCandlestickModelMapperCall1 call = reinterpret_cast<CuteQCandlestickModelMapperCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCandlestickModelMapperCall2 call = reinterpret_cast<CuteQCandlestickModelMapperCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCandlestickModelMapperCall3 call = reinterpret_cast<CuteQCandlestickModelMapperCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCandlestickModelMapperCall4 call = reinterpret_cast<CuteQCandlestickModelMapperCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCandlestickModelMapperCall5 call = reinterpret_cast<CuteQCandlestickModelMapperCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCandlestickModelMapperCall6 call = reinterpret_cast<CuteQCandlestickModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCandlestickModelMapperCall7 call = reinterpret_cast<CuteQCandlestickModelMapperCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCandlestickModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QCandlestickModelMapper10metaObjectEv(
    const QCandlestickModelMapper *self) {
  return self->metaObject();
}

//  QString QCandlestickModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QCandlestickModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCandlestickModelMapper::tr(s, c, n));
}

//  void QCandlestickModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper8setModelEP18QAbstractItemModel(
    QCandlestickModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QAbstractItemModel *QCandlestickModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK23QCandlestickModelMapper5modelEv(
    const QCandlestickModelMapper *self) {
  return self->model();
}

//  void QCandlestickModelMapper::setSeries(QCandlestickSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper9setSeriesEP18QCandlestickSeries(
    QCandlestickModelMapper *self,
    QCandlestickSeries *series) {
  self->setSeries(series);
}

//  QCandlestickSeries *QCandlestickModelMapper::series() const
extern "C" Q_DECL_EXPORT
QCandlestickSeries *ritual_ZNK23QCandlestickModelMapper6seriesEv(
    const QCandlestickModelMapper *self) {
  return self->series();
}

//  Qt::Orientation QCandlestickModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK23QCandlestickModelMapper11orientationEv(
    const QCandlestickModelMapper *self) {
  return self->orientation();
}

//  void QCandlestickModelMapper::setTimestamp(int timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper12setTimestampEi(
    QCandlestickModelMapper *self,
    int timestamp) {
  self->setTimestamp(timestamp);
}

//  int QCandlestickModelMapper::timestamp() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QCandlestickModelMapper9timestampEv(
    const QCandlestickModelMapper *self) {
  return self->timestamp();
}

//  void QCandlestickModelMapper::setOpen(int open)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper7setOpenEi(
    QCandlestickModelMapper *self,
    int open) {
  self->setOpen(open);
}

//  int QCandlestickModelMapper::open() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QCandlestickModelMapper4openEv(
    const QCandlestickModelMapper *self) {
  return self->open();
}

//  void QCandlestickModelMapper::setHigh(int high)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper7setHighEi(
    QCandlestickModelMapper *self,
    int high) {
  self->setHigh(high);
}

//  int QCandlestickModelMapper::high() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QCandlestickModelMapper4highEv(
    const QCandlestickModelMapper *self) {
  return self->high();
}

//  void QCandlestickModelMapper::setLow(int low)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper6setLowEi(
    QCandlestickModelMapper *self,
    int low) {
  self->setLow(low);
}

//  int QCandlestickModelMapper::low() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QCandlestickModelMapper3lowEv(
    const QCandlestickModelMapper *self) {
  return self->low();
}

//  void QCandlestickModelMapper::setClose(int close)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper8setCloseEi(
    QCandlestickModelMapper *self,
    int close) {
  self->setClose(close);
}

//  int QCandlestickModelMapper::close() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QCandlestickModelMapper5closeEv(
    const QCandlestickModelMapper *self) {
  return self->close();
}

//  void QCandlestickModelMapper::setFirstSetSection(int firstSetSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper18setFirstSetSectionEi(
    QCandlestickModelMapper *self,
    int firstSetSection) {
  self->setFirstSetSection(firstSetSection);
}

//  int QCandlestickModelMapper::firstSetSection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QCandlestickModelMapper15firstSetSectionEv(
    const QCandlestickModelMapper *self) {
  return self->firstSetSection();
}

//  void QCandlestickModelMapper::setLastSetSection(int lastSetSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QCandlestickModelMapper17setLastSetSectionEi(
    QCandlestickModelMapper *self,
    int lastSetSection) {
  self->setLastSetSection(lastSetSection);
}

//  int QCandlestickModelMapper::lastSetSection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QCandlestickModelMapper14lastSetSectionEv(
    const QCandlestickModelMapper *self) {
  return self->lastSetSection();
}

//  QCandlestickModelMapperPrivate *QCandlestickModelMapper::d_func()
extern "C" Q_DECL_EXPORT
QCandlestickModelMapperPrivate *ritual_ZN23QCandlestickModelMapper6d_funcEv(
    QCandlestickModelMapper *self) {
  return self->d_func();
}

//  const QCandlestickModelMapperPrivate *QCandlestickModelMapper::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QCandlestickModelMapperPrivate *ritual_ZNK23QCandlestickModelMapper6d_funcEv(
    const QCandlestickModelMapper *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCandlestickModelMapper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCandlestickModelMapper(
    QCandlestickModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCandlestickModelMapper *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_candlestick_chart)
