//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQuickPath may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPath : QQuickPath {
  using QQuickPath::componentComplete;
  using QQuickPath::classBegin;
};

//  A QQuickPath that Python can take functions over in. Every QQuickPath
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_path)
typedef void (*CuteQQuickPathCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_path)
#if QT_CONFIG(quick_path)
typedef void (*CuteQQuickPathCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_path)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPathCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPathCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPath : public QQuickPath {
public:
  using QQuickPath::QQuickPath;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_path)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_path)
#if QT_CONFIG(quick_path)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_path)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_path)
  //  void QQuickPath::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPathCall0 call = reinterpret_cast<CuteQQuickPathCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPath::componentComplete();
  }
#endif  // QT_CONFIG(quick_path)

#if QT_CONFIG(quick_path)
  //  void QQuickPath::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPathCall1 call = reinterpret_cast<CuteQQuickPathCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPath::classBegin();
  }
#endif  // QT_CONFIG(quick_path)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPathCall2 call = reinterpret_cast<CuteQQuickPathCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPathCall3 call = reinterpret_cast<CuteQQuickPathCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPathCall4 call = reinterpret_cast<CuteQQuickPathCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPathCall5 call = reinterpret_cast<CuteQQuickPathCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPathCall6 call = reinterpret_cast<CuteQQuickPathCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPathCall7 call = reinterpret_cast<CuteQQuickPathCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPathCall8 call = reinterpret_cast<CuteQQuickPathCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPath::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QQuickPath10metaObjectEv(
    const QQuickPath *self) {
  return self->metaObject();
}

//  QString QQuickPath::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QQuickPath2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPath::tr(s, c, n));
}

//  QQuickPath::QQuickPath(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPath *ritual_ZN10QQuickPathC1EP7QObject(QObject *parent) {
  return new CuteQQuickPath(parent);
}

//  QQuickPath::~QQuickPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPathD1Ev(QQuickPath *self) {
  delete self;
}

//  qreal QQuickPath::startX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPath6startXEv(const QQuickPath *self) {
  return self->startX();
}

//  void QQuickPath::setStartX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath9setStartXEd(QQuickPath *self, qreal x) {
  self->setStartX(x);
}

//  bool QQuickPath::hasStartX() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickPath9hasStartXEv(const QQuickPath *self) {
  return self->hasStartX();
}

//  qreal QQuickPath::startY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPath6startYEv(const QQuickPath *self) {
  return self->startY();
}

//  void QQuickPath::setStartY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath9setStartYEd(QQuickPath *self, qreal y) {
  self->setStartY(y);
}

//  bool QQuickPath::hasStartY() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickPath9hasStartYEv(const QQuickPath *self) {
  return self->hasStartY();
}

//  bool QQuickPath::isClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickPath8isClosedEv(const QQuickPath *self) {
  return self->isClosed();
}

//  QPainterPath QQuickPath::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK10QQuickPath4pathEv(const QQuickPath *self) {
  return new QPainterPath(self->path());
}

//  void QQuickPath::setPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath7setPathERK12QPainterPath(
    QQuickPath *self,
    const QPainterPath *path) {
  self->setPath(*path);
}

//  QStringList QQuickPath::attributes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QQuickPath10attributesEv(
    const QQuickPath *self) {
  return new QList<QString>(self->attributes());
}

//  qreal QQuickPath::attributeAt(const QString &a0, qreal a1) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QQuickPath11attributeAtERK7QStringd(
    const QQuickPath *self,
    const QString *a0,
    qreal a1) {
  return self->attributeAt(*a0, a1);
}

//  QPointF QQuickPath::pointAtPercent(qreal t) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickPath14pointAtPercentEd(
    const QQuickPath *self,
    qreal t) {
  return new QPointF(self->pointAtPercent(t));
}

//  QPointF QQuickPath::sequentialPointAt(qreal p, qreal *angle) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QQuickPath17sequentialPointAtEdPd(
    const QQuickPath *self,
    qreal p,
    qreal *angle) {
  return new QPointF(self->sequentialPointAt(p, angle));
}

//  void QQuickPath::invalidateSequentialHistory() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QQuickPath27invalidateSequentialHistoryEv(
    const QQuickPath *self) {
  self->invalidateSequentialHistory();
}

//  QSizeF QQuickPath::scale() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK10QQuickPath5scaleEv(const QQuickPath *self) {
  return new QSizeF(self->scale());
}

//  void QQuickPath::setScale(const QSizeF &scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath8setScaleERK6QSizeF(
    QQuickPath *self,
    const QSizeF *scale) {
  self->setScale(*scale);
}

//  bool QQuickPath::simplify() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickPath8simplifyEv(const QQuickPath *self) {
  return self->simplify();
}

//  void QQuickPath::setSimplify(bool s)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath11setSimplifyEb(QQuickPath *self, bool s) {
  self->setSimplify(s);
}

//  bool QQuickPath::isAsynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QQuickPath14isAsynchronousEv(const QQuickPath *self) {
  return self->isAsynchronous();
}

//  void QQuickPath::setAsynchronous(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath15setAsynchronousEb(QQuickPath *self, bool a) {
  self->setAsynchronous(a);
}

//  void QQuickPath::processPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath11processPathEv(QQuickPath *self) {
  self->processPath();
}

//  void QQuickPath::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath17componentCompleteEv(QQuickPath *self) {
  self->componentComplete();
}

//  void QQuickPath::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath10classBeginEv(QQuickPath *self) {
  self->classBegin();
}

//  void QQuickPath::disconnectPathElements()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath22disconnectPathElementsEv(QQuickPath *self) {
  self->disconnectPathElements();
}

//  void QQuickPath::connectPathElements()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath19connectPathElementsEv(QQuickPath *self) {
  self->connectPathElements();
}

//  void QQuickPath::gatherAttributes()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath16gatherAttributesEv(QQuickPath *self) {
  self->gatherAttributes();
}

//  void QQuickPath::doProcessPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath13doProcessPathEv(QQuickPath *self) {
  self->doProcessPath();
}

//  void QQuickPath::interpolate(int idx, const QString &name, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath11interpolateEiRK7QStringd(
    QQuickPath *self,
    int idx,
    const QString *name,
    qreal value) {
  self->interpolate(idx, *name, value);
}

//  void QQuickPath::endpoint(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickPath8endpointERK7QString(
    QQuickPath *self,
    const QString *name) {
  self->endpoint(*name);
}

//  void QQuickPath::createPointCache() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QQuickPath16createPointCacheEv(const QQuickPath *self) {
  self->createPointCache();
}

//  QQuickPathPrivate *QQuickPath::d_func()
extern "C" Q_DECL_EXPORT
QQuickPathPrivate *ritual_ZN10QQuickPath6d_funcEv(QQuickPath *self) {
  return self->d_func();
}

//  const QQuickPathPrivate *QQuickPath::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPathPrivate *ritual_ZNK10QQuickPath6d_funcEv(
    const QQuickPath *self) {
  return self->d_func();
}

//  QPainterPath QQuickPath::createShapePath(const QPointF &startPoint, const
//      QPointF &endPoint, qreal &pathLength, bool *closed)
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN10QQuickPath15createShapePathERK7QPointFS2_RdPb(
    QQuickPath *self,
    const QPointF *startPoint,
    const QPointF *endPoint,
    qreal *pathLength,
    bool *closed) {
  return new QPainterPath(
      self->createShapePath(
          *startPoint,
          *endPoint,
          *pathLength,
          closed));
}

//  QQuickPath as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickPath_QQmlParserStatus(QQuickPath *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickPath, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPath(QQuickPath *self, const char *key, void *call) {
  return static_cast<CuteQQuickPath *>(self)->take(key, call);
}

//  void QQuickPath::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickPath17componentCompleteEv(QQuickPath *self) {
  static_cast<OwnQQuickPath *>(self)->OwnQQuickPath::componentComplete();
}

//  void QQuickPath::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QQuickPath10classBeginEv(QQuickPath *self) {
  static_cast<OwnQQuickPath *>(self)->OwnQQuickPath::classBegin();
}

#endif  // QT_CONFIG(quick_path)
