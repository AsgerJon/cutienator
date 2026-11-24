//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgoutputv1.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandxdgoutputv1.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandXdgOutputV1 that Python can take functions over in. Every QWaylandXdgOutputV1
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandXdgOutputV1Call0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandXdgOutputV1Call1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgOutputV1Call2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgOutputV1Call3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgOutputV1Call4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgOutputV1Call5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandXdgOutputV1Call6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandXdgOutputV1 : public QWaylandXdgOutputV1 {
public:
  using QWaylandXdgOutputV1::QWaylandXdgOutputV1;
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
      CuteQWaylandXdgOutputV1Call0 call = reinterpret_cast<CuteQWaylandXdgOutputV1Call0>(taken[0]);
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
      CuteQWaylandXdgOutputV1Call1 call = reinterpret_cast<CuteQWaylandXdgOutputV1Call1>(taken[1]);
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
      CuteQWaylandXdgOutputV1Call2 call = reinterpret_cast<CuteQWaylandXdgOutputV1Call2>(taken[2]);
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
      CuteQWaylandXdgOutputV1Call3 call = reinterpret_cast<CuteQWaylandXdgOutputV1Call3>(taken[3]);
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
      CuteQWaylandXdgOutputV1Call4 call = reinterpret_cast<CuteQWaylandXdgOutputV1Call4>(taken[4]);
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
      CuteQWaylandXdgOutputV1Call5 call = reinterpret_cast<CuteQWaylandXdgOutputV1Call5>(taken[5]);
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
      CuteQWaylandXdgOutputV1Call6 call = reinterpret_cast<CuteQWaylandXdgOutputV1Call6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandXdgOutputV1::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QWaylandXdgOutputV110metaObjectEv(
    const QWaylandXdgOutputV1 *self) {
  return self->metaObject();
}

//  QString QWaylandXdgOutputV1::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QWaylandXdgOutputV12trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgOutputV1::tr(s, c, n));
}

//  QWaylandXdgOutputV1::QWaylandXdgOutputV1()
extern "C" Q_DECL_EXPORT
QWaylandXdgOutputV1 *ritual_ZN19QWaylandXdgOutputV1C1Ev() {
  return new CuteQWaylandXdgOutputV1();
}

//  QWaylandXdgOutputV1::QWaylandXdgOutputV1(QWaylandOutput *output,
//      QWaylandXdgOutputManagerV1 *manager)
extern "C" Q_DECL_EXPORT
QWaylandXdgOutputV1 *ritual_ZN19QWaylandXdgOutputV1C1EP14QWaylandOutputP26QWaylandXdgOutputManagerV1(
    QWaylandOutput *output,
    QWaylandXdgOutputManagerV1 *manager) {
  return new CuteQWaylandXdgOutputV1(output, manager);
}

//  QWaylandXdgOutputV1::~QWaylandXdgOutputV1()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgOutputV1D1Ev(QWaylandXdgOutputV1 *self) {
  delete self;
}

//  QWaylandXdgOutputManagerV1 *QWaylandXdgOutputV1::manager() const
extern "C" Q_DECL_EXPORT
QWaylandXdgOutputManagerV1 *ritual_ZNK19QWaylandXdgOutputV17managerEv(
    const QWaylandXdgOutputV1 *self) {
  return self->manager();
}

//  QWaylandOutput *QWaylandXdgOutputV1::output() const
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZNK19QWaylandXdgOutputV16outputEv(
    const QWaylandXdgOutputV1 *self) {
  return self->output();
}

//  QString QWaylandXdgOutputV1::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QWaylandXdgOutputV14nameEv(
    const QWaylandXdgOutputV1 *self) {
  return new QString(self->name());
}

//  void QWaylandXdgOutputV1::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgOutputV17setNameERK7QString(
    QWaylandXdgOutputV1 *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QWaylandXdgOutputV1::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QWaylandXdgOutputV111descriptionEv(
    const QWaylandXdgOutputV1 *self) {
  return new QString(self->description());
}

//  void QWaylandXdgOutputV1::setDescription(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgOutputV114setDescriptionERK7QString(
    QWaylandXdgOutputV1 *self,
    const QString *name) {
  self->setDescription(*name);
}

//  QPoint QWaylandXdgOutputV1::logicalPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK19QWaylandXdgOutputV115logicalPositionEv(
    const QWaylandXdgOutputV1 *self) {
  return new QPoint(self->logicalPosition());
}

//  void QWaylandXdgOutputV1::setLogicalPosition(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgOutputV118setLogicalPositionERK6QPoint(
    QWaylandXdgOutputV1 *self,
    const QPoint *position) {
  self->setLogicalPosition(*position);
}

//  QSize QWaylandXdgOutputV1::logicalSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QWaylandXdgOutputV111logicalSizeEv(
    const QWaylandXdgOutputV1 *self) {
  return new QSize(self->logicalSize());
}

//  void QWaylandXdgOutputV1::setLogicalSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandXdgOutputV114setLogicalSizeERK5QSize(
    QWaylandXdgOutputV1 *self,
    const QSize *size) {
  self->setLogicalSize(*size);
}

//  QRect QWaylandXdgOutputV1::logicalGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QWaylandXdgOutputV115logicalGeometryEv(
    const QWaylandXdgOutputV1 *self) {
  return new QRect(self->logicalGeometry());
}

//  a Python function taken by a CuteQWaylandXdgOutputV1, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandXdgOutputV1(
    QWaylandXdgOutputV1 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandXdgOutputV1 *>(self)->take(key, call);
}
