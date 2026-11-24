//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitemanimation.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(easingcurve) && QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsitemanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtransform.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsItemAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsItemAnimation : QGraphicsItemAnimation {
  using QGraphicsItemAnimation::beforeAnimationStep;
  using QGraphicsItemAnimation::afterAnimationStep;
};

//  A QGraphicsItemAnimation that Python can take functions over in. Every QGraphicsItemAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemAnimationCall0)(const void *, qreal, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsItemAnimationCall1)(const void *, qreal, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsItemAnimationCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsItemAnimationCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsItemAnimationCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsItemAnimationCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsItemAnimationCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsItemAnimationCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsItemAnimationCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphicsItemAnimation : public QGraphicsItemAnimation {
public:
  using QGraphicsItemAnimation::QGraphicsItemAnimation;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN22QGraphicsItemAnimation19beforeAnimationStepEd")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN22QGraphicsItemAnimation18afterAnimationStepEd")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
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

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemAnimation::beforeAnimationStep(qreal step)
  void beforeAnimationStep(qreal step) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsItemAnimationCall0 call = reinterpret_cast<CuteQGraphicsItemAnimationCall0>(taken[0]);
      call(this, step, &handled);
      if (handled) return;
    }
    QGraphicsItemAnimation::beforeAnimationStep(step);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemAnimation::afterAnimationStep(qreal step)
  void afterAnimationStep(qreal step) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsItemAnimationCall1 call = reinterpret_cast<CuteQGraphicsItemAnimationCall1>(taken[1]);
      call(this, step, &handled);
      if (handled) return;
    }
    QGraphicsItemAnimation::afterAnimationStep(step);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsItemAnimationCall2 call = reinterpret_cast<CuteQGraphicsItemAnimationCall2>(taken[2]);
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
      CuteQGraphicsItemAnimationCall3 call = reinterpret_cast<CuteQGraphicsItemAnimationCall3>(taken[3]);
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
      CuteQGraphicsItemAnimationCall4 call = reinterpret_cast<CuteQGraphicsItemAnimationCall4>(taken[4]);
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
      CuteQGraphicsItemAnimationCall5 call = reinterpret_cast<CuteQGraphicsItemAnimationCall5>(taken[5]);
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
      CuteQGraphicsItemAnimationCall6 call = reinterpret_cast<CuteQGraphicsItemAnimationCall6>(taken[6]);
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
      CuteQGraphicsItemAnimationCall7 call = reinterpret_cast<CuteQGraphicsItemAnimationCall7>(taken[7]);
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
      CuteQGraphicsItemAnimationCall8 call = reinterpret_cast<CuteQGraphicsItemAnimationCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphicsItemAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QGraphicsItemAnimation10metaObjectEv(
    const QGraphicsItemAnimation *self) {
  return self->metaObject();
}

//  QString QGraphicsItemAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QGraphicsItemAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsItemAnimation::tr(s, c, n));
}

//  QGraphicsItemAnimation::QGraphicsItemAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsItemAnimation *ritual_ZN22QGraphicsItemAnimationC1EP7QObject(
    QObject *parent) {
  return new CuteQGraphicsItemAnimation(parent);
}

//  QGraphicsItemAnimation::~QGraphicsItemAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimationD1Ev(QGraphicsItemAnimation *self) {
  delete self;
}

//  QGraphicsItem *QGraphicsItemAnimation::item() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK22QGraphicsItemAnimation4itemEv(
    const QGraphicsItemAnimation *self) {
  return self->item();
}

//  void QGraphicsItemAnimation::setItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation7setItemEP13QGraphicsItem(
    QGraphicsItemAnimation *self,
    QGraphicsItem *item) {
  self->setItem(item);
}

//  QTimeLine *QGraphicsItemAnimation::timeLine() const
extern "C" Q_DECL_EXPORT
QTimeLine *ritual_ZNK22QGraphicsItemAnimation8timeLineEv(
    const QGraphicsItemAnimation *self) {
  return self->timeLine();
}

//  void QGraphicsItemAnimation::setTimeLine(QTimeLine *timeLine)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation11setTimeLineEP9QTimeLine(
    QGraphicsItemAnimation *self,
    QTimeLine *timeLine) {
  self->setTimeLine(timeLine);
}

//  QPointF QGraphicsItemAnimation::posAt(qreal step) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK22QGraphicsItemAnimation5posAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return new QPointF(self->posAt(step));
}

//  void QGraphicsItemAnimation::setPosAt(qreal step, const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation8setPosAtEdRK7QPointF(
    QGraphicsItemAnimation *self,
    qreal step,
    const QPointF *pos) {
  self->setPosAt(step, *pos);
}

//  QTransform QGraphicsItemAnimation::transformAt(qreal step) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK22QGraphicsItemAnimation11transformAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return new QTransform(self->transformAt(step));
}

//  qreal QGraphicsItemAnimation::rotationAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation10rotationAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->rotationAt(step);
}

//  void QGraphicsItemAnimation::setRotationAt(qreal step, qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation13setRotationAtEdd(
    QGraphicsItemAnimation *self,
    qreal step,
    qreal angle) {
  self->setRotationAt(step, angle);
}

//  qreal QGraphicsItemAnimation::xTranslationAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation14xTranslationAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->xTranslationAt(step);
}

//  qreal QGraphicsItemAnimation::yTranslationAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation14yTranslationAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->yTranslationAt(step);
}

//  void QGraphicsItemAnimation::setTranslationAt(qreal step, qreal dx, qreal
//      dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation16setTranslationAtEddd(
    QGraphicsItemAnimation *self,
    qreal step,
    qreal dx,
    qreal dy) {
  self->setTranslationAt(step, dx, dy);
}

//  qreal QGraphicsItemAnimation::verticalScaleAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation15verticalScaleAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->verticalScaleAt(step);
}

//  qreal QGraphicsItemAnimation::horizontalScaleAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation17horizontalScaleAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->horizontalScaleAt(step);
}

//  void QGraphicsItemAnimation::setScaleAt(qreal step, qreal sx, qreal sy)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation10setScaleAtEddd(
    QGraphicsItemAnimation *self,
    qreal step,
    qreal sx,
    qreal sy) {
  self->setScaleAt(step, sx, sy);
}

//  qreal QGraphicsItemAnimation::verticalShearAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation15verticalShearAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->verticalShearAt(step);
}

//  qreal QGraphicsItemAnimation::horizontalShearAt(qreal step) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsItemAnimation17horizontalShearAtEd(
    const QGraphicsItemAnimation *self,
    qreal step) {
  return self->horizontalShearAt(step);
}

//  void QGraphicsItemAnimation::setShearAt(qreal step, qreal sh, qreal sv)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation10setShearAtEddd(
    QGraphicsItemAnimation *self,
    qreal step,
    qreal sh,
    qreal sv) {
  self->setShearAt(step, sh, sv);
}

//  void QGraphicsItemAnimation::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation5clearEv(
    QGraphicsItemAnimation *self) {
  self->clear();
}

//  void QGraphicsItemAnimation::setStep(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation7setStepEd(
    QGraphicsItemAnimation *self,
    qreal x) {
  self->setStep(x);
}

//  void QGraphicsItemAnimation::beforeAnimationStep(qreal step)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation19beforeAnimationStepEd(
    QGraphicsItemAnimation *self,
    qreal step) {
  self->beforeAnimationStep(step);
}

//  void QGraphicsItemAnimation::afterAnimationStep(qreal step)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsItemAnimation18afterAnimationStepEd(
    QGraphicsItemAnimation *self,
    qreal step) {
  self->afterAnimationStep(step);
}

//  a Python function taken by a CuteQGraphicsItemAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsItemAnimation(
    QGraphicsItemAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsItemAnimation *>(self)->take(key, call);
}

//  void QGraphicsItemAnimation::beforeAnimationStep(qreal step)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsItemAnimation19beforeAnimationStepEd(
    QGraphicsItemAnimation *self,
    qreal step) {
  static_cast<OwnQGraphicsItemAnimation *>(self)->OwnQGraphicsItemAnimation::beforeAnimationStep(
      step);
}

//  void QGraphicsItemAnimation::afterAnimationStep(qreal step)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsItemAnimation18afterAnimationStepEd(
    QGraphicsItemAnimation *self,
    qreal step) {
  static_cast<OwnQGraphicsItemAnimation *>(self)->OwnQGraphicsItemAnimation::afterAnimationStep(
      step);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(easingcurve) && QT_CONFIG(graphicsview)
