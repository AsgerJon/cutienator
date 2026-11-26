//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qabstractseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qabstractseries.h>
#include <QtCore/qstring.h>
#include <QtCharts/qabstractaxis.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAbstractSeries that Python can take functions over in. Every QAbstractSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAbstractSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractSeries : public QAbstractSeries {
public:
  using QAbstractSeries::QAbstractSeries;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
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

  //  SeriesType QAbstractSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSeriesCall0 call = reinterpret_cast<CuteQAbstractSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSeriesCall1 call = reinterpret_cast<CuteQAbstractSeriesCall1>(taken[1]);
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
      CuteQAbstractSeriesCall2 call = reinterpret_cast<CuteQAbstractSeriesCall2>(taken[2]);
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
      CuteQAbstractSeriesCall3 call = reinterpret_cast<CuteQAbstractSeriesCall3>(taken[3]);
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
      CuteQAbstractSeriesCall4 call = reinterpret_cast<CuteQAbstractSeriesCall4>(taken[4]);
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
      CuteQAbstractSeriesCall5 call = reinterpret_cast<CuteQAbstractSeriesCall5>(taken[5]);
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
      CuteQAbstractSeriesCall6 call = reinterpret_cast<CuteQAbstractSeriesCall6>(taken[6]);
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
      CuteQAbstractSeriesCall7 call = reinterpret_cast<CuteQAbstractSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstractSeries10metaObjectEv(
    const QAbstractSeries *self) {
  return self->metaObject();
}

//  void *QAbstractSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QAbstractSeries11qt_metacastEPKc(
    QAbstractSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QAbstractSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstractSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSeries::tr(s, c, n));
}

//  QAbstractSeries::QAbstractSeries(QAbstractSeriesPrivate &d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN15QAbstractSeriesC1ER22QAbstractSeriesPrivateP7QObject(
    QAbstractSeriesPrivate *d,
    QObject *parent) {
  return new CuteQAbstractSeries(*d, parent);
}

//  QAbstractSeries::~QAbstractSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeriesD1Ev(QAbstractSeries *self) {
  delete self;
}

//  SeriesType QAbstractSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK15QAbstractSeries4typeEv(
    const QAbstractSeries *self) {
  return self->type();
}

//  void QAbstractSeries::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries7setNameERK7QString(
    QAbstractSeries *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QAbstractSeries::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractSeries4nameEv(const QAbstractSeries *self) {
  return new QString(self->name());
}

//  void QAbstractSeries::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries10setVisibleEb(
    QAbstractSeries *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool QAbstractSeries::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSeries9isVisibleEv(const QAbstractSeries *self) {
  return self->isVisible();
}

//  qreal QAbstractSeries::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QAbstractSeries7opacityEv(const QAbstractSeries *self) {
  return self->opacity();
}

//  void QAbstractSeries::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries10setOpacityEd(
    QAbstractSeries *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  void QAbstractSeries::setUseOpenGL(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries12setUseOpenGLEb(
    QAbstractSeries *self,
    bool enable) {
  self->setUseOpenGL(enable);
}

//  bool QAbstractSeries::useOpenGL() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSeries9useOpenGLEv(const QAbstractSeries *self) {
  return self->useOpenGL();
}

//  QChart *QAbstractSeries::chart() const
extern "C" Q_DECL_EXPORT
QChart *ritual_ZNK15QAbstractSeries5chartEv(const QAbstractSeries *self) {
  return self->chart();
}

//  bool QAbstractSeries::attachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSeries10attachAxisEP13QAbstractAxis(
    QAbstractSeries *self,
    QAbstractAxis *axis) {
  return self->attachAxis(axis);
}

//  bool QAbstractSeries::detachAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSeries10detachAxisEP13QAbstractAxis(
    QAbstractSeries *self,
    QAbstractAxis *axis) {
  return self->detachAxis(axis);
}

//  QList<QAbstractAxis *> QAbstractSeries::attachedAxes()
extern "C" Q_DECL_EXPORT
QList<QAbstractAxis *> *ritual_ZN15QAbstractSeries12attachedAxesEv(
    QAbstractSeries *self) {
  return new QList<QAbstractAxis *>(self->attachedAxes());
}

//  void QAbstractSeries::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries4showEv(QAbstractSeries *self) {
  self->show();
}

//  void QAbstractSeries::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries4hideEv(QAbstractSeries *self) {
  self->hide();
}

//  void QAbstractSeries::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries11nameChangedEv(QAbstractSeries *self) {
  self->nameChanged();
}

//  void QAbstractSeries::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries14visibleChangedEv(QAbstractSeries *self) {
  self->visibleChanged();
}

//  void QAbstractSeries::opacityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries14opacityChangedEv(QAbstractSeries *self) {
  self->opacityChanged();
}

//  void QAbstractSeries::useOpenGLChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries16useOpenGLChangedEv(QAbstractSeries *self) {
  self->useOpenGLChanged();
}

//  a Python function taken by a CuteQAbstractSeries, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSeries(
    QAbstractSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSeries *>(self)->take(key, call);
}

//  QList<QAbstractSeries *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstractSeries *> *ritual_list_make_QAbstractSeries_ptr() {
  return new QList<QAbstractSeries *>();
}

//  void QList<QAbstractSeries *>::append(const QAbstractSeries * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstractSeries_ptr(
    QList<QAbstractSeries *> *self,
    QAbstractSeries *element) {
  self->append(element);
}

//  qsizetype QList<QAbstractSeries *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstractSeries_ptr(
    const QList<QAbstractSeries *> *self) {
  return self->size();
}

//  const QAbstractSeries * &QList<QAbstractSeries *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_list_at_QAbstractSeries_ptr(
    const QList<QAbstractSeries *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstractSeries *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstractSeries_ptr(QList<QAbstractSeries *> *self) {
  delete self;
}
