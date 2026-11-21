//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qanimationgroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qanimationgroup.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAnimationGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAnimationGroup10metaObjectEv(
    const QAnimationGroup *self) {
  return self->metaObject();
}

//  QString QAnimationGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAnimationGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAnimationGroup::tr(s, c, n));
}

//  QAnimationGroup::~QAnimationGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroupD1Ev(QAnimationGroup *self) {
  delete self;
}

//  QAbstractAnimation *QAnimationGroup::animationAt(int index) const
extern "C" Q_DECL_EXPORT
QAbstractAnimation *ritual_ZNK15QAnimationGroup11animationAtEi(
    const QAnimationGroup *self,
    int index) {
  return self->animationAt(index);
}

//  int QAnimationGroup::animationCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAnimationGroup14animationCountEv(
    const QAnimationGroup *self) {
  return self->animationCount();
}

//  int QAnimationGroup::indexOfAnimation(QAbstractAnimation *animation)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAnimationGroup16indexOfAnimationEP18QAbstractAnimation(
    const QAnimationGroup *self,
    QAbstractAnimation *animation) {
  return self->indexOfAnimation(animation);
}

//  void QAnimationGroup::addAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroup12addAnimationEP18QAbstractAnimation(
    QAnimationGroup *self,
    QAbstractAnimation *animation) {
  self->addAnimation(animation);
}

//  void QAnimationGroup::insertAnimation(int index, QAbstractAnimation
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroup15insertAnimationEiP18QAbstractAnimation(
    QAnimationGroup *self,
    int index,
    QAbstractAnimation *animation) {
  self->insertAnimation(index, animation);
}

//  void QAnimationGroup::removeAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroup15removeAnimationEP18QAbstractAnimation(
    QAnimationGroup *self,
    QAbstractAnimation *animation) {
  self->removeAnimation(animation);
}

//  QAbstractAnimation *QAnimationGroup::takeAnimation(int index)
extern "C" Q_DECL_EXPORT
QAbstractAnimation *ritual_ZN15QAnimationGroup13takeAnimationEi(
    QAnimationGroup *self,
    int index) {
  return self->takeAnimation(index);
}

//  void QAnimationGroup::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroup5clearEv(QAnimationGroup *self) {
  self->clear();
}
