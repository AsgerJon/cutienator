//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qvcandlestickmodelmapper.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_candlestick_chart)
#include <QtCharts/qvcandlestickmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVCandlestickModelMapper that Python can take functions over in. Every QVCandlestickModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQVCandlestickModelMapperCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVCandlestickModelMapperCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVCandlestickModelMapperCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVCandlestickModelMapperCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVCandlestickModelMapperCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVCandlestickModelMapperCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVCandlestickModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVCandlestickModelMapperCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVCandlestickModelMapper : public QVCandlestickModelMapper {
public:
  using QVCandlestickModelMapper::QVCandlestickModelMapper;
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

  //  Qt::Orientation QVCandlestickModelMapper::orientation() const
  Qt::Orientation orientation() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQVCandlestickModelMapperCall0 call = reinterpret_cast<CuteQVCandlestickModelMapperCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::Orientation>(given);
    }
    return QVCandlestickModelMapper::orientation();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQVCandlestickModelMapperCall1 call = reinterpret_cast<CuteQVCandlestickModelMapperCall1>(taken[1]);
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
      CuteQVCandlestickModelMapperCall2 call = reinterpret_cast<CuteQVCandlestickModelMapperCall2>(taken[2]);
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
      CuteQVCandlestickModelMapperCall3 call = reinterpret_cast<CuteQVCandlestickModelMapperCall3>(taken[3]);
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
      CuteQVCandlestickModelMapperCall4 call = reinterpret_cast<CuteQVCandlestickModelMapperCall4>(taken[4]);
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
      CuteQVCandlestickModelMapperCall5 call = reinterpret_cast<CuteQVCandlestickModelMapperCall5>(taken[5]);
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
      CuteQVCandlestickModelMapperCall6 call = reinterpret_cast<CuteQVCandlestickModelMapperCall6>(taken[6]);
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
      CuteQVCandlestickModelMapperCall7 call = reinterpret_cast<CuteQVCandlestickModelMapperCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVCandlestickModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QVCandlestickModelMapper10metaObjectEv(
    const QVCandlestickModelMapper *self) {
  return self->metaObject();
}

//  QString QVCandlestickModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QVCandlestickModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVCandlestickModelMapper::tr(s, c, n));
}

//  QVCandlestickModelMapper::QVCandlestickModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QVCandlestickModelMapper *ritual_ZN24QVCandlestickModelMapperC1EP7QObject(
    QObject *parent) {
  return new CuteQVCandlestickModelMapper(parent);
}

//  Qt::Orientation QVCandlestickModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK24QVCandlestickModelMapper11orientationEv(
    const QVCandlestickModelMapper *self) {
  return self->orientation();
}

//  void QVCandlestickModelMapper::setTimestampRow(int timestampRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVCandlestickModelMapper15setTimestampRowEi(
    QVCandlestickModelMapper *self,
    int timestampRow) {
  self->setTimestampRow(timestampRow);
}

//  int QVCandlestickModelMapper::timestampRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QVCandlestickModelMapper12timestampRowEv(
    const QVCandlestickModelMapper *self) {
  return self->timestampRow();
}

//  void QVCandlestickModelMapper::setOpenRow(int openRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVCandlestickModelMapper10setOpenRowEi(
    QVCandlestickModelMapper *self,
    int openRow) {
  self->setOpenRow(openRow);
}

//  int QVCandlestickModelMapper::openRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QVCandlestickModelMapper7openRowEv(
    const QVCandlestickModelMapper *self) {
  return self->openRow();
}

//  void QVCandlestickModelMapper::setHighRow(int highRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVCandlestickModelMapper10setHighRowEi(
    QVCandlestickModelMapper *self,
    int highRow) {
  self->setHighRow(highRow);
}

//  int QVCandlestickModelMapper::highRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QVCandlestickModelMapper7highRowEv(
    const QVCandlestickModelMapper *self) {
  return self->highRow();
}

//  void QVCandlestickModelMapper::setLowRow(int lowRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVCandlestickModelMapper9setLowRowEi(
    QVCandlestickModelMapper *self,
    int lowRow) {
  self->setLowRow(lowRow);
}

//  int QVCandlestickModelMapper::lowRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QVCandlestickModelMapper6lowRowEv(
    const QVCandlestickModelMapper *self) {
  return self->lowRow();
}

//  void QVCandlestickModelMapper::setCloseRow(int closeRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVCandlestickModelMapper11setCloseRowEi(
    QVCandlestickModelMapper *self,
    int closeRow) {
  self->setCloseRow(closeRow);
}

//  int QVCandlestickModelMapper::closeRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QVCandlestickModelMapper8closeRowEv(
    const QVCandlestickModelMapper *self) {
  return self->closeRow();
}

//  void QVCandlestickModelMapper::setFirstSetColumn(int firstSetColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVCandlestickModelMapper17setFirstSetColumnEi(
    QVCandlestickModelMapper *self,
    int firstSetColumn) {
  self->setFirstSetColumn(firstSetColumn);
}

//  int QVCandlestickModelMapper::firstSetColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QVCandlestickModelMapper14firstSetColumnEv(
    const QVCandlestickModelMapper *self) {
  return self->firstSetColumn();
}

//  void QVCandlestickModelMapper::setLastSetColumn(int lastSetColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVCandlestickModelMapper16setLastSetColumnEi(
    QVCandlestickModelMapper *self,
    int lastSetColumn) {
  self->setLastSetColumn(lastSetColumn);
}

//  int QVCandlestickModelMapper::lastSetColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QVCandlestickModelMapper13lastSetColumnEv(
    const QVCandlestickModelMapper *self) {
  return self->lastSetColumn();
}

//  a Python function taken by a CuteQVCandlestickModelMapper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVCandlestickModelMapper(
    QVCandlestickModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVCandlestickModelMapper *>(self)->take(key, call);
}

//  Qt::Orientation QVCandlestickModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_own_ZNK24QVCandlestickModelMapper11orientationEv(
    const QVCandlestickModelMapper *self) {
  return self->QVCandlestickModelMapper::orientation();
}

#endif  // QT_CONFIG(charts_candlestick_chart)
