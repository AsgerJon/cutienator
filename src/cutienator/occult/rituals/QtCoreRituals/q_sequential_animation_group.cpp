//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsequentialanimationgroup.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qsequentialanimationgroup.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QSequentialAnimationGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QSequentialAnimationGroup10metaObjectEv(
    const QSequentialAnimationGroup *self) {
  return self->metaObject();
}

//  QString QSequentialAnimationGroup::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QSequentialAnimationGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSequentialAnimationGroup::tr(s, c, n));
}

//  QSequentialAnimationGroup::QSequentialAnimationGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QSequentialAnimationGroup *ritual_ZN25QSequentialAnimationGroupC1EP7QObject(
    QObject *parent) {
  return new QSequentialAnimationGroup(parent);
}

//  QSequentialAnimationGroup::~QSequentialAnimationGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSequentialAnimationGroupD1Ev(
    QSequentialAnimationGroup *self) {
  delete self;
}

//  QPauseAnimation *QSequentialAnimationGroup::addPause(int msecs)
extern "C" Q_DECL_EXPORT
QPauseAnimation *ritual_ZN25QSequentialAnimationGroup8addPauseEi(
    QSequentialAnimationGroup *self,
    int msecs) {
  return self->addPause(msecs);
}

//  QPauseAnimation *QSequentialAnimationGroup::insertPause(int index, int
//      msecs)
extern "C" Q_DECL_EXPORT
QPauseAnimation *ritual_ZN25QSequentialAnimationGroup11insertPauseEii(
    QSequentialAnimationGroup *self,
    int index,
    int msecs) {
  return self->insertPause(index, msecs);
}

//  QAbstractAnimation *QSequentialAnimationGroup::currentAnimation() const
extern "C" Q_DECL_EXPORT
QAbstractAnimation *ritual_ZNK25QSequentialAnimationGroup16currentAnimationEv(
    const QSequentialAnimationGroup *self) {
  return self->currentAnimation();
}

//  int QSequentialAnimationGroup::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QSequentialAnimationGroup8durationEv(
    const QSequentialAnimationGroup *self) {
  return self->duration();
}
