//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qcategory3daxis.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qcategory3daxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCategory3DAxis that Python can take functions over in. Every QCategory3DAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCategory3DAxisCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCategory3DAxisCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCategory3DAxis : public QCategory3DAxis {
public:
  using QCategory3DAxis::QCategory3DAxis;
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
      CuteQCategory3DAxisCall0 call = reinterpret_cast<CuteQCategory3DAxisCall0>(taken[0]);
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
      CuteQCategory3DAxisCall1 call = reinterpret_cast<CuteQCategory3DAxisCall1>(taken[1]);
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
      CuteQCategory3DAxisCall2 call = reinterpret_cast<CuteQCategory3DAxisCall2>(taken[2]);
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
      CuteQCategory3DAxisCall3 call = reinterpret_cast<CuteQCategory3DAxisCall3>(taken[3]);
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
      CuteQCategory3DAxisCall4 call = reinterpret_cast<CuteQCategory3DAxisCall4>(taken[4]);
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
      CuteQCategory3DAxisCall5 call = reinterpret_cast<CuteQCategory3DAxisCall5>(taken[5]);
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
      CuteQCategory3DAxisCall6 call = reinterpret_cast<CuteQCategory3DAxisCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCategory3DAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QCategory3DAxis10metaObjectEv(
    const QCategory3DAxis *self) {
  return self->metaObject();
}

//  void *QCategory3DAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QCategory3DAxis11qt_metacastEPKc(
    QCategory3DAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCategory3DAxis::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QCategory3DAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    QCategory3DAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCategory3DAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QCategory3DAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCategory3DAxis::tr(s, c, n));
}

//  QCategory3DAxis::QCategory3DAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZN15QCategory3DAxisC1EP7QObject(QObject *parent) {
  return new CuteQCategory3DAxis(parent);
}

//  QCategory3DAxis::~QCategory3DAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCategory3DAxisD1Ev(QCategory3DAxis *self) {
  delete self;
}

//  void QCategory3DAxis::setLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCategory3DAxis9setLabelsERK5QListI7QStringE(
    QCategory3DAxis *self,
    const QList<QString> *labels) {
  self->setLabels(*labels);
}

//  QStringList QCategory3DAxis::labels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QCategory3DAxis6labelsEv(
    const QCategory3DAxis *self) {
  return new QList<QString>(self->labels());
}

//  void QCategory3DAxis::labelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCategory3DAxis13labelsChangedEv(QCategory3DAxis *self) {
  self->labelsChanged();
}

//  QCategory3DAxisPrivate *QCategory3DAxis::dptr()
extern "C" Q_DECL_EXPORT
QCategory3DAxisPrivate *ritual_ZN15QCategory3DAxis4dptrEv(
    QCategory3DAxis *self) {
  return self->dptr();
}

//  a Python function taken by a CuteQCategory3DAxis, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCategory3DAxis(
    QCategory3DAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCategory3DAxis *>(self)->take(key, call);
}
