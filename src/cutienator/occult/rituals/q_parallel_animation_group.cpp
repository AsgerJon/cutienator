//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qparallelanimationgroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qparallelanimationgroup.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QParallelAnimationGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QParallelAnimationGroup10metaObjectEv(
    const QParallelAnimationGroup *self) {
  return self->metaObject();
}

//  QString QParallelAnimationGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QParallelAnimationGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QParallelAnimationGroup::tr(s, c, n));
}

//  QParallelAnimationGroup::QParallelAnimationGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QParallelAnimationGroup *ritual_ZN23QParallelAnimationGroupC1EP7QObject(
    QObject *parent) {
  return new QParallelAnimationGroup(parent);
}

//  QParallelAnimationGroup::~QParallelAnimationGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QParallelAnimationGroupD1Ev(QParallelAnimationGroup *self) {
  delete self;
}

//  int QParallelAnimationGroup::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QParallelAnimationGroup8durationEv(
    const QParallelAnimationGroup *self) {
  return self->duration();
}
