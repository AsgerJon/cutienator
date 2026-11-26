//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qanimationgroup.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qanimationgroup.h>
#include <QtCore/qstring.h>
#include <QtCore/QList>
#include <Qt3DAnimation/Qt3DAnimation>

//  const QMetaObject *Qt3DAnimation::QAnimationGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation15QAnimationGroup10metaObjectEv(
    const Qt3DAnimation::QAnimationGroup *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QAnimationGroup::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation15QAnimationGroup11qt_metacastEPKc(
    Qt3DAnimation::QAnimationGroup *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QAnimationGroup::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation15QAnimationGroup11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QAnimationGroup *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QAnimationGroup::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation15QAnimationGroup2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAnimationGroup::tr(s, c, n));
}

//  Qt3DAnimation::QAnimationGroup::QAnimationGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationGroup *ritual_ZN13Qt3DAnimation15QAnimationGroupC1EP7QObject(
    QObject *parent) {
  return new Qt3DAnimation::QAnimationGroup(parent);
}

//  QString Qt3DAnimation::QAnimationGroup::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation15QAnimationGroup4nameEv(
    const Qt3DAnimation::QAnimationGroup *self) {
  return new QString(self->name());
}

//  QList<Qt3DAnimation::QAbstractAnimation *>
//      Qt3DAnimation::QAnimationGroup::animationList()
extern "C" Q_DECL_EXPORT
QList<Qt3DAnimation::QAbstractAnimation *> *ritual_ZN13Qt3DAnimation15QAnimationGroup13animationListEv(
    Qt3DAnimation::QAnimationGroup *self) {
  return new QList<Qt3DAnimation::QAbstractAnimation *>(
      self->animationList());
}

//  float Qt3DAnimation::QAnimationGroup::position() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation15QAnimationGroup8positionEv(
    const Qt3DAnimation::QAnimationGroup *self) {
  return self->position();
}

//  float Qt3DAnimation::QAnimationGroup::duration() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation15QAnimationGroup8durationEv(
    const Qt3DAnimation::QAnimationGroup *self) {
  return self->duration();
}

//  void Qt3DAnimation::QAnimationGroup::setAnimations(const
//      QList<Qt3DAnimation::QAbstractAnimation *> &animations)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QAnimationGroup13setAnimationsERK5QListIPNS_18QAbstractAnimationEE(
    Qt3DAnimation::QAnimationGroup *self,
    const QList<Qt3DAnimation::QAbstractAnimation *> *animations) {
  self->setAnimations(*animations);
}

//  void Qt3DAnimation::QAnimationGroup::addAnimation(Qt3DAnimation::QAbstrac
//      tAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QAnimationGroup12addAnimationEPNS_18QAbstractAnimationE(
    Qt3DAnimation::QAnimationGroup *self,
    Qt3DAnimation::QAbstractAnimation *animation) {
  self->addAnimation(animation);
}

//  void Qt3DAnimation::QAnimationGroup::removeAnimation(Qt3DAnimation::QAbst
//      ractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QAnimationGroup15removeAnimationEPNS_18QAbstractAnimationE(
    Qt3DAnimation::QAnimationGroup *self,
    Qt3DAnimation::QAbstractAnimation *animation) {
  self->removeAnimation(animation);
}

//  void Qt3DAnimation::QAnimationGroup::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QAnimationGroup7setNameERK7QString(
    Qt3DAnimation::QAnimationGroup *self,
    const QString *name) {
  self->setName(*name);
}

//  void Qt3DAnimation::QAnimationGroup::setPosition(float position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QAnimationGroup11setPositionEf(
    Qt3DAnimation::QAnimationGroup *self,
    float position) {
  self->setPosition(position);
}

//  void Qt3DAnimation::QAnimationGroup::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QAnimationGroup11nameChangedERK7QString(
    Qt3DAnimation::QAnimationGroup *self,
    const QString *name) {
  self->nameChanged(*name);
}

//  void Qt3DAnimation::QAnimationGroup::positionChanged(float position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QAnimationGroup15positionChangedEf(
    Qt3DAnimation::QAnimationGroup *self,
    float position) {
  self->positionChanged(position);
}

//  void Qt3DAnimation::QAnimationGroup::durationChanged(float duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation15QAnimationGroup15durationChangedEf(
    Qt3DAnimation::QAnimationGroup *self,
    float duration) {
  self->durationChanged(duration);
}

//  QAnimationGroupPrivate *Qt3DAnimation::QAnimationGroup::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationGroupPrivate *ritual_ZN13Qt3DAnimation15QAnimationGroup6d_funcEv(
    Qt3DAnimation::QAnimationGroup *self) {
  return self->d_func();
}

//  const QAnimationGroupPrivate *Qt3DAnimation::QAnimationGroup::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationGroupPrivate *ritual_ZNK13Qt3DAnimation15QAnimationGroup6d_funcEv(
    const Qt3DAnimation::QAnimationGroup *self) {
  return self->d_func();
}

//  a QList<Qt3DAnimation::QAbstractAnimation *> a ritual of
//      Qt3DAnimation::QAnimationGroup gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QAnimationGroup__QList_Qt3DAnimation_QAbstractAnimation(
    QList<Qt3DAnimation::QAbstractAnimation *> *self) {
  delete self;
}
