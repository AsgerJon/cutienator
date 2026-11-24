//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicstransform.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGraphicsScale that Python can take functions over in. Every QGraphicsScale
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsScaleCall0)(const void *, QMatrix4x4 *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsScaleCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsScaleCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsScaleCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsScaleCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsScaleCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsScaleCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsScaleCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphicsScale : public QGraphicsScale {
public:
  using QGraphicsScale::QGraphicsScale;
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
  //  void QGraphicsScale::applyTo(QMatrix4x4 *matrix) const
  void applyTo(QMatrix4x4 *matrix) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsScaleCall0 call = reinterpret_cast<CuteQGraphicsScaleCall0>(taken[0]);
      call(this, matrix, &handled);
      if (handled) return;
    }
    QGraphicsScale::applyTo(matrix);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsScaleCall1 call = reinterpret_cast<CuteQGraphicsScaleCall1>(taken[1]);
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
      CuteQGraphicsScaleCall2 call = reinterpret_cast<CuteQGraphicsScaleCall2>(taken[2]);
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
      CuteQGraphicsScaleCall3 call = reinterpret_cast<CuteQGraphicsScaleCall3>(taken[3]);
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
      CuteQGraphicsScaleCall4 call = reinterpret_cast<CuteQGraphicsScaleCall4>(taken[4]);
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
      CuteQGraphicsScaleCall5 call = reinterpret_cast<CuteQGraphicsScaleCall5>(taken[5]);
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
      CuteQGraphicsScaleCall6 call = reinterpret_cast<CuteQGraphicsScaleCall6>(taken[6]);
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
      CuteQGraphicsScaleCall7 call = reinterpret_cast<CuteQGraphicsScaleCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphicsScale::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGraphicsScale10metaObjectEv(
    const QGraphicsScale *self) {
  return self->metaObject();
}

//  QString QGraphicsScale::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGraphicsScale2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsScale::tr(s, c, n));
}

//  QGraphicsScale::QGraphicsScale(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsScale *ritual_ZN14QGraphicsScaleC1EP7QObject(QObject *parent) {
  return new CuteQGraphicsScale(parent);
}

//  QGraphicsScale::~QGraphicsScale()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScaleD1Ev(QGraphicsScale *self) {
  delete self;
}

//  QVector3D QGraphicsScale::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QGraphicsScale6originEv(const QGraphicsScale *self) {
  return new QVector3D(self->origin());
}

//  void QGraphicsScale::setOrigin(const QVector3D &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScale9setOriginERK9QVector3D(
    QGraphicsScale *self,
    const QVector3D *point) {
  self->setOrigin(*point);
}

//  qreal QGraphicsScale::xScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScale6xScaleEv(const QGraphicsScale *self) {
  return self->xScale();
}

//  void QGraphicsScale::setXScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScale9setXScaleEd(QGraphicsScale *self, qreal a0) {
  self->setXScale(a0);
}

//  qreal QGraphicsScale::yScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScale6yScaleEv(const QGraphicsScale *self) {
  return self->yScale();
}

//  void QGraphicsScale::setYScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScale9setYScaleEd(QGraphicsScale *self, qreal a0) {
  self->setYScale(a0);
}

//  qreal QGraphicsScale::zScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScale6zScaleEv(const QGraphicsScale *self) {
  return self->zScale();
}

//  void QGraphicsScale::setZScale(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScale9setZScaleEd(QGraphicsScale *self, qreal a0) {
  self->setZScale(a0);
}

//  void QGraphicsScale::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QGraphicsScale7applyToEP10QMatrix4x4(
    const QGraphicsScale *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  a Python function taken by a CuteQGraphicsScale, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsScale(
    QGraphicsScale *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsScale *>(self)->take(key, call);
}

//  void QGraphicsScale::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK14QGraphicsScale7applyToEP10QMatrix4x4(
    const QGraphicsScale *self,
    QMatrix4x4 *matrix) {
  self->QGraphicsScale::applyTo(matrix);
}

#endif  // QT_CONFIG(graphicsview)
