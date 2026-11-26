//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qboxplotmodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/qboxplotmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBoxPlotModelMapper that Python can take functions over in. Every QBoxPlotModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBoxPlotModelMapper : public QBoxPlotModelMapper {
public:
  using QBoxPlotModelMapper::QBoxPlotModelMapper;
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
      CuteQBoxPlotModelMapperCall0 call = reinterpret_cast<CuteQBoxPlotModelMapperCall0>(taken[0]);
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
      CuteQBoxPlotModelMapperCall1 call = reinterpret_cast<CuteQBoxPlotModelMapperCall1>(taken[1]);
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
      CuteQBoxPlotModelMapperCall2 call = reinterpret_cast<CuteQBoxPlotModelMapperCall2>(taken[2]);
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
      CuteQBoxPlotModelMapperCall3 call = reinterpret_cast<CuteQBoxPlotModelMapperCall3>(taken[3]);
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
      CuteQBoxPlotModelMapperCall4 call = reinterpret_cast<CuteQBoxPlotModelMapperCall4>(taken[4]);
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
      CuteQBoxPlotModelMapperCall5 call = reinterpret_cast<CuteQBoxPlotModelMapperCall5>(taken[5]);
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
      CuteQBoxPlotModelMapperCall6 call = reinterpret_cast<CuteQBoxPlotModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBoxPlotModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QBoxPlotModelMapper10metaObjectEv(
    const QBoxPlotModelMapper *self) {
  return self->metaObject();
}

//  void *QBoxPlotModelMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QBoxPlotModelMapper11qt_metacastEPKc(
    QBoxPlotModelMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBoxPlotModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QBoxPlotModelMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QBoxPlotModelMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBoxPlotModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QBoxPlotModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxPlotModelMapper::tr(s, c, n));
}

//  QBoxPlotModelMapper::QBoxPlotModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QBoxPlotModelMapper *ritual_ZN19QBoxPlotModelMapperC1EP7QObject(
    QObject *parent) {
  return new CuteQBoxPlotModelMapper(parent);
}

//  QAbstractItemModel *QBoxPlotModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK19QBoxPlotModelMapper5modelEv(
    const QBoxPlotModelMapper *self) {
  return self->model();
}

//  void QBoxPlotModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBoxPlotModelMapper8setModelEP18QAbstractItemModel(
    QBoxPlotModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QBoxPlotSeries *QBoxPlotModelMapper::series() const
extern "C" Q_DECL_EXPORT
QBoxPlotSeries *ritual_ZNK19QBoxPlotModelMapper6seriesEv(
    const QBoxPlotModelMapper *self) {
  return self->series();
}

//  void QBoxPlotModelMapper::setSeries(QBoxPlotSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBoxPlotModelMapper9setSeriesEP14QBoxPlotSeries(
    QBoxPlotModelMapper *self,
    QBoxPlotSeries *series) {
  self->setSeries(series);
}

//  int QBoxPlotModelMapper::first() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QBoxPlotModelMapper5firstEv(
    const QBoxPlotModelMapper *self) {
  return self->first();
}

//  void QBoxPlotModelMapper::setFirst(int first)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBoxPlotModelMapper8setFirstEi(
    QBoxPlotModelMapper *self,
    int first) {
  self->setFirst(first);
}

//  int QBoxPlotModelMapper::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QBoxPlotModelMapper5countEv(
    const QBoxPlotModelMapper *self) {
  return self->count();
}

//  void QBoxPlotModelMapper::setCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBoxPlotModelMapper8setCountEi(
    QBoxPlotModelMapper *self,
    int count) {
  self->setCount(count);
}

//  int QBoxPlotModelMapper::firstBoxSetSection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QBoxPlotModelMapper18firstBoxSetSectionEv(
    const QBoxPlotModelMapper *self) {
  return self->firstBoxSetSection();
}

//  void QBoxPlotModelMapper::setFirstBoxSetSection(int firstBoxSetSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBoxPlotModelMapper21setFirstBoxSetSectionEi(
    QBoxPlotModelMapper *self,
    int firstBoxSetSection) {
  self->setFirstBoxSetSection(firstBoxSetSection);
}

//  int QBoxPlotModelMapper::lastBoxSetSection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QBoxPlotModelMapper17lastBoxSetSectionEv(
    const QBoxPlotModelMapper *self) {
  return self->lastBoxSetSection();
}

//  void QBoxPlotModelMapper::setLastBoxSetSection(int lastBoxSetSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBoxPlotModelMapper20setLastBoxSetSectionEi(
    QBoxPlotModelMapper *self,
    int lastBoxSetSection) {
  self->setLastBoxSetSection(lastBoxSetSection);
}

//  Qt::Orientation QBoxPlotModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK19QBoxPlotModelMapper11orientationEv(
    const QBoxPlotModelMapper *self) {
  return self->orientation();
}

//  void QBoxPlotModelMapper::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBoxPlotModelMapper14setOrientationEN2Qt11OrientationE(
    QBoxPlotModelMapper *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  QBoxPlotModelMapperPrivate *QBoxPlotModelMapper::d_func()
extern "C" Q_DECL_EXPORT
QBoxPlotModelMapperPrivate *ritual_ZN19QBoxPlotModelMapper6d_funcEv(
    QBoxPlotModelMapper *self) {
  return self->d_func();
}

//  const QBoxPlotModelMapperPrivate *QBoxPlotModelMapper::d_func() const
extern "C" Q_DECL_EXPORT
const QBoxPlotModelMapperPrivate *ritual_ZNK19QBoxPlotModelMapper6d_funcEv(
    const QBoxPlotModelMapper *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQBoxPlotModelMapper, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBoxPlotModelMapper(
    QBoxPlotModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBoxPlotModelMapper *>(self)->take(key, call);
}

#endif  // QT_CONFIG(charts_boxplot_chart)
