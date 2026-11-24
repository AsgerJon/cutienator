//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgabstractanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgabstractanimation_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QSvgAbstractAnimation that Python can take functions over in. Every QSvgAbstractAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgAbstractAnimationCall0)(const void *, int *);
typedef void (*CuteQSvgAbstractAnimationCall1)(const void *, QSvgAbstractAnimatedProperty *, int *);
typedef bool (*CuteQSvgAbstractAnimationCall2)(const void *, int *);
class CuteQSvgAbstractAnimation : public QSvgAbstractAnimation {
public:
  using QSvgAbstractAnimation::QSvgAbstractAnimation;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QSvgAbstractAnimation13animationTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbstractAnimatedProperty")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QSvgAbstractAnimation8isActiveEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  AnimationType QSvgAbstractAnimation::animationType() const
  QSvgAbstractAnimation::AnimationType animationType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgAbstractAnimationCall0 call = reinterpret_cast<CuteQSvgAbstractAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgAbstractAnimation::AnimationType>(given);
    }
    return {};
  }

  //  void
  //      QSvgAbstractAnimation::appendProperty(QSvgAbstractAnimatedPropert
  //      y *property)
  void appendProperty(QSvgAbstractAnimatedProperty *property) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgAbstractAnimationCall1 call = reinterpret_cast<CuteQSvgAbstractAnimationCall1>(taken[1]);
      call(this, property, &handled);
      if (handled) return;
    }
    QSvgAbstractAnimation::appendProperty(property);
  }

  //  bool QSvgAbstractAnimation::isActive() const
  bool isActive() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgAbstractAnimationCall2 call = reinterpret_cast<CuteQSvgAbstractAnimationCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgAbstractAnimation::isActive();
  }
};

//  QSvgAbstractAnimation::~QSvgAbstractAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgAbstractAnimationD1Ev(QSvgAbstractAnimation *self) {
  delete self;
}

//  AnimationType QSvgAbstractAnimation::animationType() const
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimation::AnimationType ritual_ZNK21QSvgAbstractAnimation13animationTypeEv(
    const QSvgAbstractAnimation *self) {
  return self->animationType();
}

//  void QSvgAbstractAnimation::evaluateAnimation(qreal elapsedTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgAbstractAnimation17evaluateAnimationEd(
    QSvgAbstractAnimation *self,
    qreal elapsedTime) {
  self->evaluateAnimation(elapsedTime);
}

//  void QSvgAbstractAnimation::setRunningTime(int startMs, int durationMs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgAbstractAnimation14setRunningTimeEii(
    QSvgAbstractAnimation *self,
    int startMs,
    int durationMs) {
  self->setRunningTime(startMs, durationMs);
}

//  int QSvgAbstractAnimation::start() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSvgAbstractAnimation5startEv(
    const QSvgAbstractAnimation *self) {
  return self->start();
}

//  int QSvgAbstractAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSvgAbstractAnimation8durationEv(
    const QSvgAbstractAnimation *self) {
  return self->duration();
}

//  void QSvgAbstractAnimation::setIterationCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgAbstractAnimation17setIterationCountEi(
    QSvgAbstractAnimation *self,
    int count) {
  self->setIterationCount(count);
}

//  int QSvgAbstractAnimation::iterationCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSvgAbstractAnimation14iterationCountEv(
    const QSvgAbstractAnimation *self) {
  return self->iterationCount();
}

//  QSvgEasingInterface *QSvgAbstractAnimation::easing() const
extern "C" Q_DECL_EXPORT
QSvgEasingInterface *ritual_ZNK21QSvgAbstractAnimation6easingEv(
    const QSvgAbstractAnimation *self) {
  return self->easing();
}

//  void QSvgAbstractAnimation::appendProperty(QSvgAbstractAnimatedProperty
//      *property)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbstractAnimatedProperty(
    QSvgAbstractAnimation *self,
    QSvgAbstractAnimatedProperty *property) {
  self->appendProperty(property);
}

//  QList<QSvgAbstractAnimatedProperty *> QSvgAbstractAnimation::properties()
//      const
extern "C" Q_DECL_EXPORT
QList<QSvgAbstractAnimatedProperty *> *ritual_ZNK21QSvgAbstractAnimation10propertiesEv(
    const QSvgAbstractAnimation *self) {
  return new QList<QSvgAbstractAnimatedProperty *>(self->properties());
}

//  bool QSvgAbstractAnimation::finished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSvgAbstractAnimation8finishedEv(
    const QSvgAbstractAnimation *self) {
  return self->finished();
}

//  bool QSvgAbstractAnimation::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSvgAbstractAnimation8isActiveEv(
    const QSvgAbstractAnimation *self) {
  return self->isActive();
}

//  a Python function taken by a CuteQSvgAbstractAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgAbstractAnimation(
    QSvgAbstractAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgAbstractAnimation *>(self)->take(key, call);
}

//  void QSvgAbstractAnimation::appendProperty(QSvgAbstractAnimatedProperty
//      *property)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSvgAbstractAnimation14appendPropertyEP28QSvgAbstractAnimatedProperty(
    QSvgAbstractAnimation *self,
    QSvgAbstractAnimatedProperty *property) {
  self->QSvgAbstractAnimation::appendProperty(property);
}

//  bool QSvgAbstractAnimation::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSvgAbstractAnimation8isActiveEv(
    const QSvgAbstractAnimation *self) {
  return self->QSvgAbstractAnimation::isActive();
}

//  QList<QSvgAbstractAnimation *>::QList()
extern "C" Q_DECL_EXPORT
QList<QSvgAbstractAnimation *> *ritual_list_make_QSvgAbstractAnimation_ptr() {
  return new QList<QSvgAbstractAnimation *>();
}

//  void QList<QSvgAbstractAnimation *>::append(const QSvgAbstractAnimation *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSvgAbstractAnimation_ptr(
    QList<QSvgAbstractAnimation *> *self,
    QSvgAbstractAnimation *element) {
  self->append(element);
}

//  qsizetype QList<QSvgAbstractAnimation *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSvgAbstractAnimation_ptr(
    const QList<QSvgAbstractAnimation *> *self) {
  return self->size();
}

//  const QSvgAbstractAnimation * &QList<QSvgAbstractAnimation
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSvgAbstractAnimation *ritual_list_at_QSvgAbstractAnimation_ptr(
    const QList<QSvgAbstractAnimation *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QSvgAbstractAnimation *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSvgAbstractAnimation_ptr(
    QList<QSvgAbstractAnimation *> *self) {
  delete self;
}
