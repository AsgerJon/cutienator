//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpauseanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpauseanimation.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QPauseAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QPauseAnimation10metaObjectEv(
    const QPauseAnimation *self) {
  return self->metaObject();
}

//  QString QPauseAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QPauseAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPauseAnimation::tr(s, c, n));
}

//  QPauseAnimation::QPauseAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QPauseAnimation *ritual_ZN15QPauseAnimationC1EP7QObject(QObject *parent) {
  return new QPauseAnimation(parent);
}

//  QPauseAnimation::QPauseAnimation(int msecs, QObject *parent)
extern "C" Q_DECL_EXPORT
QPauseAnimation *ritual_ZN15QPauseAnimationC1EiP7QObject(
    int msecs,
    QObject *parent) {
  return new QPauseAnimation(msecs, parent);
}

//  QPauseAnimation::~QPauseAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPauseAnimationD1Ev(QPauseAnimation *self) {
  delete self;
}

//  int QPauseAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPauseAnimation8durationEv(const QPauseAnimation *self) {
  return self->duration();
}

//  void QPauseAnimation::setDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPauseAnimation11setDurationEi(
    QPauseAnimation *self,
    int msecs) {
  self->setDuration(msecs);
}
