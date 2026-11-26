//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicstransform.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGraphicsTransform that Python can take functions over in. Every QGraphicsTransform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsTransformCall0)(const void *, QMatrix4x4 *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsTransformCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsTransformCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsTransformCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsTransformCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsTransformCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsTransformCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsTransformCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphicsTransform : public QGraphicsTransform {
public:
  using QGraphicsTransform::QGraphicsTransform;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK18QGraphicsTransform7applyToEP10QMatrix4x4")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
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

#if QT_CONFIG(graphicsview)
  //  void QGraphicsTransform::applyTo(QMatrix4x4 *matrix) const
  void applyTo(QMatrix4x4 *matrix) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsTransformCall0 call = reinterpret_cast<CuteQGraphicsTransformCall0>(taken[0]);
      call(this, matrix, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsTransformCall1 call = reinterpret_cast<CuteQGraphicsTransformCall1>(taken[1]);
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
      CuteQGraphicsTransformCall2 call = reinterpret_cast<CuteQGraphicsTransformCall2>(taken[2]);
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
      CuteQGraphicsTransformCall3 call = reinterpret_cast<CuteQGraphicsTransformCall3>(taken[3]);
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
      CuteQGraphicsTransformCall4 call = reinterpret_cast<CuteQGraphicsTransformCall4>(taken[4]);
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
      CuteQGraphicsTransformCall5 call = reinterpret_cast<CuteQGraphicsTransformCall5>(taken[5]);
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
      CuteQGraphicsTransformCall6 call = reinterpret_cast<CuteQGraphicsTransformCall6>(taken[6]);
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
      CuteQGraphicsTransformCall7 call = reinterpret_cast<CuteQGraphicsTransformCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphicsTransform::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QGraphicsTransform10metaObjectEv(
    const QGraphicsTransform *self) {
  return self->metaObject();
}

//  void *QGraphicsTransform::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QGraphicsTransform11qt_metacastEPKc(
    QGraphicsTransform *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGraphicsTransform::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGraphicsTransform11qt_metacallEN11QMetaObject4CallEiPPv(
    QGraphicsTransform *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGraphicsTransform::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QGraphicsTransform2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsTransform::tr(s, c, n));
}

//  QGraphicsTransform::QGraphicsTransform(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsTransform *ritual_ZN18QGraphicsTransformC1EP7QObject(
    QObject *parent) {
  return new CuteQGraphicsTransform(parent);
}

//  QGraphicsTransform::~QGraphicsTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsTransformD1Ev(QGraphicsTransform *self) {
  delete self;
}

//  void QGraphicsTransform::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QGraphicsTransform7applyToEP10QMatrix4x4(
    const QGraphicsTransform *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  void QGraphicsTransform::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsTransform6updateEv(QGraphicsTransform *self) {
  self->update();
}

//  QGraphicsTransform::QGraphicsTransform(QGraphicsTransformPrivate &p,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsTransform *ritual_ZN18QGraphicsTransformC1ER25QGraphicsTransformPrivateP7QObject(
    QGraphicsTransformPrivate *p,
    QObject *parent) {
  return new CuteQGraphicsTransform(*p, parent);
}

//  QGraphicsTransformPrivate *QGraphicsTransform::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsTransformPrivate *ritual_ZN18QGraphicsTransform6d_funcEv(
    QGraphicsTransform *self) {
  return self->d_func();
}

//  const QGraphicsTransformPrivate *QGraphicsTransform::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsTransformPrivate *ritual_ZNK18QGraphicsTransform6d_funcEv(
    const QGraphicsTransform *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsTransform, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsTransform(
    QGraphicsTransform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsTransform *>(self)->take(key, call);
}

//  QList<QGraphicsTransform *>::QList()
extern "C" Q_DECL_EXPORT
QList<QGraphicsTransform *> *ritual_list_make_QGraphicsTransform_ptr() {
  return new QList<QGraphicsTransform *>();
}

//  void QList<QGraphicsTransform *>::append(const QGraphicsTransform *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGraphicsTransform_ptr(
    QList<QGraphicsTransform *> *self,
    QGraphicsTransform *element) {
  self->append(element);
}

//  qsizetype QList<QGraphicsTransform *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGraphicsTransform_ptr(
    const QList<QGraphicsTransform *> *self) {
  return self->size();
}

//  const QGraphicsTransform * &QList<QGraphicsTransform *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QGraphicsTransform *ritual_list_at_QGraphicsTransform_ptr(
    const QList<QGraphicsTransform *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QGraphicsTransform *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGraphicsTransform_ptr(
    QList<QGraphicsTransform *> *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
