//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qhcandlestickmodelmapper.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_candlestick_chart)
#include <QtCharts/qhcandlestickmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHCandlestickModelMapper that Python can take functions over in. Every QHCandlestickModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQHCandlestickModelMapperCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHCandlestickModelMapperCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHCandlestickModelMapperCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHCandlestickModelMapperCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHCandlestickModelMapperCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHCandlestickModelMapperCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHCandlestickModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHCandlestickModelMapperCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHCandlestickModelMapper : public QHCandlestickModelMapper {
public:
  using QHCandlestickModelMapper::QHCandlestickModelMapper;
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

  //  Qt::Orientation QHCandlestickModelMapper::orientation() const
  Qt::Orientation orientation() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHCandlestickModelMapperCall0 call = reinterpret_cast<CuteQHCandlestickModelMapperCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::Orientation>(given);
    }
    return QHCandlestickModelMapper::orientation();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHCandlestickModelMapperCall1 call = reinterpret_cast<CuteQHCandlestickModelMapperCall1>(taken[1]);
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
      CuteQHCandlestickModelMapperCall2 call = reinterpret_cast<CuteQHCandlestickModelMapperCall2>(taken[2]);
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
      CuteQHCandlestickModelMapperCall3 call = reinterpret_cast<CuteQHCandlestickModelMapperCall3>(taken[3]);
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
      CuteQHCandlestickModelMapperCall4 call = reinterpret_cast<CuteQHCandlestickModelMapperCall4>(taken[4]);
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
      CuteQHCandlestickModelMapperCall5 call = reinterpret_cast<CuteQHCandlestickModelMapperCall5>(taken[5]);
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
      CuteQHCandlestickModelMapperCall6 call = reinterpret_cast<CuteQHCandlestickModelMapperCall6>(taken[6]);
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
      CuteQHCandlestickModelMapperCall7 call = reinterpret_cast<CuteQHCandlestickModelMapperCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHCandlestickModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QHCandlestickModelMapper10metaObjectEv(
    const QHCandlestickModelMapper *self) {
  return self->metaObject();
}

//  QString QHCandlestickModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QHCandlestickModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHCandlestickModelMapper::tr(s, c, n));
}

//  QHCandlestickModelMapper::QHCandlestickModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QHCandlestickModelMapper *ritual_ZN24QHCandlestickModelMapperC1EP7QObject(
    QObject *parent) {
  return new CuteQHCandlestickModelMapper(parent);
}

//  Qt::Orientation QHCandlestickModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK24QHCandlestickModelMapper11orientationEv(
    const QHCandlestickModelMapper *self) {
  return self->orientation();
}

//  void QHCandlestickModelMapper::setTimestampColumn(int timestampColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHCandlestickModelMapper18setTimestampColumnEi(
    QHCandlestickModelMapper *self,
    int timestampColumn) {
  self->setTimestampColumn(timestampColumn);
}

//  int QHCandlestickModelMapper::timestampColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QHCandlestickModelMapper15timestampColumnEv(
    const QHCandlestickModelMapper *self) {
  return self->timestampColumn();
}

//  void QHCandlestickModelMapper::setOpenColumn(int openColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHCandlestickModelMapper13setOpenColumnEi(
    QHCandlestickModelMapper *self,
    int openColumn) {
  self->setOpenColumn(openColumn);
}

//  int QHCandlestickModelMapper::openColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QHCandlestickModelMapper10openColumnEv(
    const QHCandlestickModelMapper *self) {
  return self->openColumn();
}

//  void QHCandlestickModelMapper::setHighColumn(int highColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHCandlestickModelMapper13setHighColumnEi(
    QHCandlestickModelMapper *self,
    int highColumn) {
  self->setHighColumn(highColumn);
}

//  int QHCandlestickModelMapper::highColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QHCandlestickModelMapper10highColumnEv(
    const QHCandlestickModelMapper *self) {
  return self->highColumn();
}

//  void QHCandlestickModelMapper::setLowColumn(int lowColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHCandlestickModelMapper12setLowColumnEi(
    QHCandlestickModelMapper *self,
    int lowColumn) {
  self->setLowColumn(lowColumn);
}

//  int QHCandlestickModelMapper::lowColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QHCandlestickModelMapper9lowColumnEv(
    const QHCandlestickModelMapper *self) {
  return self->lowColumn();
}

//  void QHCandlestickModelMapper::setCloseColumn(int closeColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHCandlestickModelMapper14setCloseColumnEi(
    QHCandlestickModelMapper *self,
    int closeColumn) {
  self->setCloseColumn(closeColumn);
}

//  int QHCandlestickModelMapper::closeColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QHCandlestickModelMapper11closeColumnEv(
    const QHCandlestickModelMapper *self) {
  return self->closeColumn();
}

//  void QHCandlestickModelMapper::setFirstSetRow(int firstSetRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHCandlestickModelMapper14setFirstSetRowEi(
    QHCandlestickModelMapper *self,
    int firstSetRow) {
  self->setFirstSetRow(firstSetRow);
}

//  int QHCandlestickModelMapper::firstSetRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QHCandlestickModelMapper11firstSetRowEv(
    const QHCandlestickModelMapper *self) {
  return self->firstSetRow();
}

//  void QHCandlestickModelMapper::setLastSetRow(int lastSetRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHCandlestickModelMapper13setLastSetRowEi(
    QHCandlestickModelMapper *self,
    int lastSetRow) {
  self->setLastSetRow(lastSetRow);
}

//  int QHCandlestickModelMapper::lastSetRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QHCandlestickModelMapper10lastSetRowEv(
    const QHCandlestickModelMapper *self) {
  return self->lastSetRow();
}

//  a Python function taken by a CuteQHCandlestickModelMapper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHCandlestickModelMapper(
    QHCandlestickModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHCandlestickModelMapper *>(self)->take(key, call);
}

//  Qt::Orientation QHCandlestickModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_own_ZNK24QHCandlestickModelMapper11orientationEv(
    const QHCandlestickModelMapper *self) {
  return self->QHCandlestickModelMapper::orientation();
}

#endif  // QT_CONFIG(charts_candlestick_chart)
