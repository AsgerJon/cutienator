//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicstransform.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGraphicsRotation that Python can take functions over in. Every QGraphicsRotation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsRotationCall0)(const void *, QMatrix4x4 *, int *);
typedef bool (*CuteQGraphicsRotationCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsRotationCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsRotationCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsRotationCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsRotationCall5)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsRotationCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsRotationCall7)(const void *, const QMetaMethod *, int *);
class CuteQGraphicsRotation : public QGraphicsRotation {
public:
  using QGraphicsRotation::QGraphicsRotation;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QGraphicsTransform7applyToEP10QMatrix4x4")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void QGraphicsRotation::applyTo(QMatrix4x4 *matrix) const
  void applyTo(QMatrix4x4 *matrix) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsRotationCall0 call = reinterpret_cast<CuteQGraphicsRotationCall0>(taken[0]);
      call(this, matrix, &handled);
      if (handled) return;
    }
    QGraphicsRotation::applyTo(matrix);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsRotationCall1 call = reinterpret_cast<CuteQGraphicsRotationCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsRotationCall2 call = reinterpret_cast<CuteQGraphicsRotationCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsRotationCall3 call = reinterpret_cast<CuteQGraphicsRotationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsRotationCall4 call = reinterpret_cast<CuteQGraphicsRotationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsRotationCall5 call = reinterpret_cast<CuteQGraphicsRotationCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsRotationCall6 call = reinterpret_cast<CuteQGraphicsRotationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsRotationCall7 call = reinterpret_cast<CuteQGraphicsRotationCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGraphicsRotation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGraphicsRotation10metaObjectEv(
    const QGraphicsRotation *self) {
  return self->metaObject();
}

//  QString QGraphicsRotation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGraphicsRotation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsRotation::tr(s, c, n));
}

//  QGraphicsRotation::QGraphicsRotation(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsRotation *ritual_ZN17QGraphicsRotationC1EP7QObject(
    QObject *parent) {
  return new CuteQGraphicsRotation(parent);
}

//  QGraphicsRotation::~QGraphicsRotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotationD1Ev(QGraphicsRotation *self) {
  delete self;
}

//  QVector3D QGraphicsRotation::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QGraphicsRotation6originEv(
    const QGraphicsRotation *self) {
  return new QVector3D(self->origin());
}

//  void QGraphicsRotation::setOrigin(const QVector3D &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotation9setOriginERK9QVector3D(
    QGraphicsRotation *self,
    const QVector3D *point) {
  self->setOrigin(*point);
}

//  qreal QGraphicsRotation::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGraphicsRotation5angleEv(const QGraphicsRotation *self) {
  return self->angle();
}

//  void QGraphicsRotation::setAngle(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotation8setAngleEd(
    QGraphicsRotation *self,
    qreal a0) {
  self->setAngle(a0);
}

//  QVector3D QGraphicsRotation::axis() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QGraphicsRotation4axisEv(
    const QGraphicsRotation *self) {
  return new QVector3D(self->axis());
}

//  void QGraphicsRotation::setAxis(const QVector3D &axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotation7setAxisERK9QVector3D(
    QGraphicsRotation *self,
    const QVector3D *axis) {
  self->setAxis(*axis);
}

//  void QGraphicsRotation::setAxis(Qt::Axis axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotation7setAxisEN2Qt4AxisE(
    QGraphicsRotation *self,
    Qt::Axis axis) {
  self->setAxis(axis);
}

//  void QGraphicsRotation::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QGraphicsRotation7applyToEP10QMatrix4x4(
    const QGraphicsRotation *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  a Python function taken by a CuteQGraphicsRotation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsRotation(
    QGraphicsRotation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsRotation *>(self)->take(key, call);
}

//  void QGraphicsRotation::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QGraphicsRotation7applyToEP10QMatrix4x4(
    const QGraphicsRotation *self,
    QMatrix4x4 *matrix) {
  self->QGraphicsRotation::applyTo(matrix);
}
