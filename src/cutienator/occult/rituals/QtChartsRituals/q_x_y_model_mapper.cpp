//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qxymodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qxymodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QXYModelMapper that Python can take functions over in. Every QXYModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQXYModelMapper : public QXYModelMapper {
public:
  using QXYModelMapper::QXYModelMapper;
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
      CuteQXYModelMapperCall0 call = reinterpret_cast<CuteQXYModelMapperCall0>(taken[0]);
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
      CuteQXYModelMapperCall1 call = reinterpret_cast<CuteQXYModelMapperCall1>(taken[1]);
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
      CuteQXYModelMapperCall2 call = reinterpret_cast<CuteQXYModelMapperCall2>(taken[2]);
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
      CuteQXYModelMapperCall3 call = reinterpret_cast<CuteQXYModelMapperCall3>(taken[3]);
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
      CuteQXYModelMapperCall4 call = reinterpret_cast<CuteQXYModelMapperCall4>(taken[4]);
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
      CuteQXYModelMapperCall5 call = reinterpret_cast<CuteQXYModelMapperCall5>(taken[5]);
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
      CuteQXYModelMapperCall6 call = reinterpret_cast<CuteQXYModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QXYModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QXYModelMapper10metaObjectEv(
    const QXYModelMapper *self) {
  return self->metaObject();
}

//  void *QXYModelMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QXYModelMapper11qt_metacastEPKc(
    QXYModelMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QXYModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QXYModelMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QXYModelMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QXYModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QXYModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXYModelMapper::tr(s, c, n));
}

//  QXYModelMapper::QXYModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QXYModelMapper *ritual_ZN14QXYModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQXYModelMapper(parent);
}

//  QAbstractItemModel *QXYModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK14QXYModelMapper5modelEv(
    const QXYModelMapper *self) {
  return self->model();
}

//  void QXYModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXYModelMapper8setModelEP18QAbstractItemModel(
    QXYModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QXYSeries *QXYModelMapper::series() const
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZNK14QXYModelMapper6seriesEv(const QXYModelMapper *self) {
  return self->series();
}

//  void QXYModelMapper::setSeries(QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXYModelMapper9setSeriesEP9QXYSeries(
    QXYModelMapper *self,
    QXYSeries *series) {
  self->setSeries(series);
}

//  int QXYModelMapper::first() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXYModelMapper5firstEv(const QXYModelMapper *self) {
  return self->first();
}

//  void QXYModelMapper::setFirst(int first)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXYModelMapper8setFirstEi(QXYModelMapper *self, int first) {
  self->setFirst(first);
}

//  int QXYModelMapper::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXYModelMapper5countEv(const QXYModelMapper *self) {
  return self->count();
}

//  void QXYModelMapper::setCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXYModelMapper8setCountEi(QXYModelMapper *self, int count) {
  self->setCount(count);
}

//  Qt::Orientation QXYModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK14QXYModelMapper11orientationEv(
    const QXYModelMapper *self) {
  return self->orientation();
}

//  void QXYModelMapper::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXYModelMapper14setOrientationEN2Qt11OrientationE(
    QXYModelMapper *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  int QXYModelMapper::xSection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXYModelMapper8xSectionEv(const QXYModelMapper *self) {
  return self->xSection();
}

//  void QXYModelMapper::setXSection(int xSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXYModelMapper11setXSectionEi(
    QXYModelMapper *self,
    int xSection) {
  self->setXSection(xSection);
}

//  int QXYModelMapper::ySection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QXYModelMapper8ySectionEv(const QXYModelMapper *self) {
  return self->ySection();
}

//  void QXYModelMapper::setYSection(int ySection)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QXYModelMapper11setYSectionEi(
    QXYModelMapper *self,
    int ySection) {
  self->setYSection(ySection);
}

//  QXYModelMapperPrivate *QXYModelMapper::d_func()
extern "C" Q_DECL_EXPORT
QXYModelMapperPrivate *ritual_ZN14QXYModelMapper6d_funcEv(
    QXYModelMapper *self) {
  return self->d_func();
}

//  const QXYModelMapperPrivate *QXYModelMapper::d_func() const
extern "C" Q_DECL_EXPORT
const QXYModelMapperPrivate *ritual_ZNK14QXYModelMapper6d_funcEv(
    const QXYModelMapper *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQXYModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXYModelMapper(
    QXYModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXYModelMapper *>(self)->take(key, call);
}
