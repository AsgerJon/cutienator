//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qanimationcontroller.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qanimationcontroller.h>
#include <QtCore/qstring.h>
#include <QtCore/QList>
#include <Qt3DAnimation/Qt3DAnimation>

//  const QMetaObject *Qt3DAnimation::QAnimationController::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation20QAnimationController10metaObjectEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QAnimationController::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation20QAnimationController11qt_metacastEPKc(
    Qt3DAnimation::QAnimationController *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QAnimationController::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation20QAnimationController11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QAnimationController *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QAnimationController::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation20QAnimationController2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QAnimationController::tr(s, c, n));
}

//  Qt3DAnimation::QAnimationController::QAnimationController(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationController *ritual_ZN13Qt3DAnimation20QAnimationControllerC1EP7QObject(
    QObject *parent) {
  return new Qt3DAnimation::QAnimationController(parent);
}

//  QList<Qt3DAnimation::QAnimationGroup *>
//      Qt3DAnimation::QAnimationController::animationGroupList()
extern "C" Q_DECL_EXPORT
QList<Qt3DAnimation::QAnimationGroup *> *ritual_ZN13Qt3DAnimation20QAnimationController18animationGroupListEv(
    Qt3DAnimation::QAnimationController *self) {
  return new QList<Qt3DAnimation::QAnimationGroup *>(
      self->animationGroupList());
}

//  int Qt3DAnimation::QAnimationController::activeAnimationGroup() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation20QAnimationController20activeAnimationGroupEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->activeAnimationGroup();
}

//  float Qt3DAnimation::QAnimationController::position() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation20QAnimationController8positionEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->position();
}

//  float Qt3DAnimation::QAnimationController::positionScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation20QAnimationController13positionScaleEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->positionScale();
}

//  float Qt3DAnimation::QAnimationController::positionOffset() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation20QAnimationController14positionOffsetEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->positionOffset();
}

//  Qt3DCore::QEntity *Qt3DAnimation::QAnimationController::entity() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK13Qt3DAnimation20QAnimationController6entityEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->entity();
}

//  bool Qt3DAnimation::QAnimationController::recursive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation20QAnimationController9recursiveEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->recursive();
}

//  void Qt3DAnimation::QAnimationController::setAnimationGroups(const
//      QList<Qt3DAnimation::QAnimationGroup *> &animationGroups)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController18setAnimationGroupsERK5QListIPNS_15QAnimationGroupEE(
    Qt3DAnimation::QAnimationController *self,
    const QList<Qt3DAnimation::QAnimationGroup *> *animationGroups) {
  self->setAnimationGroups(*animationGroups);
}

//  void Qt3DAnimation::QAnimationController::addAnimationGroup(Qt3DAnimation
//      ::QAnimationGroup *animationGroups)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController17addAnimationGroupEPNS_15QAnimationGroupE(
    Qt3DAnimation::QAnimationController *self,
    Qt3DAnimation::QAnimationGroup *animationGroups) {
  self->addAnimationGroup(animationGroups);
}

//  void Qt3DAnimation::QAnimationController::removeAnimationGroup(Qt3DAnimat
//      ion::QAnimationGroup *animationGroups)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController20removeAnimationGroupEPNS_15QAnimationGroupE(
    Qt3DAnimation::QAnimationController *self,
    Qt3DAnimation::QAnimationGroup *animationGroups) {
  self->removeAnimationGroup(animationGroups);
}

//  int Qt3DAnimation::QAnimationController::getAnimationIndex(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation20QAnimationController17getAnimationIndexERK7QString(
    const Qt3DAnimation::QAnimationController *self,
    const QString *name) {
  return self->getAnimationIndex(*name);
}

//  Qt3DAnimation::QAnimationGroup
//      *Qt3DAnimation::QAnimationController::getGroup(int index) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationGroup *ritual_ZNK13Qt3DAnimation20QAnimationController8getGroupEi(
    const Qt3DAnimation::QAnimationController *self,
    int index) {
  return self->getGroup(index);
}

//  void Qt3DAnimation::QAnimationController::setActiveAnimationGroup(int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController23setActiveAnimationGroupEi(
    Qt3DAnimation::QAnimationController *self,
    int index) {
  self->setActiveAnimationGroup(index);
}

//  void Qt3DAnimation::QAnimationController::setPosition(float position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController11setPositionEf(
    Qt3DAnimation::QAnimationController *self,
    float position) {
  self->setPosition(position);
}

//  void Qt3DAnimation::QAnimationController::setPositionScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController16setPositionScaleEf(
    Qt3DAnimation::QAnimationController *self,
    float scale) {
  self->setPositionScale(scale);
}

//  void Qt3DAnimation::QAnimationController::setPositionOffset(float offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController17setPositionOffsetEf(
    Qt3DAnimation::QAnimationController *self,
    float offset) {
  self->setPositionOffset(offset);
}

//  void Qt3DAnimation::QAnimationController::setEntity(Qt3DCore::QEntity
//      *entity)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController9setEntityEPN8Qt3DCore7QEntityE(
    Qt3DAnimation::QAnimationController *self,
    Qt3DCore::QEntity *entity) {
  self->setEntity(entity);
}

//  void Qt3DAnimation::QAnimationController::setRecursive(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController12setRecursiveEb(
    Qt3DAnimation::QAnimationController *self,
    bool recursive) {
  self->setRecursive(recursive);
}

//  void Qt3DAnimation::QAnimationController::activeAnimationGroupChanged(int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController27activeAnimationGroupChangedEi(
    Qt3DAnimation::QAnimationController *self,
    int index) {
  self->activeAnimationGroupChanged(index);
}

//  void Qt3DAnimation::QAnimationController::positionChanged(float position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController15positionChangedEf(
    Qt3DAnimation::QAnimationController *self,
    float position) {
  self->positionChanged(position);
}

//  void Qt3DAnimation::QAnimationController::positionScaleChanged(float
//      scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController20positionScaleChangedEf(
    Qt3DAnimation::QAnimationController *self,
    float scale) {
  self->positionScaleChanged(scale);
}

//  void Qt3DAnimation::QAnimationController::positionOffsetChanged(float
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController21positionOffsetChangedEf(
    Qt3DAnimation::QAnimationController *self,
    float offset) {
  self->positionOffsetChanged(offset);
}

//  void Qt3DAnimation::QAnimationController::entityChanged(Qt3DCore::QEntity
//      *entity)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController13entityChangedEPN8Qt3DCore7QEntityE(
    Qt3DAnimation::QAnimationController *self,
    Qt3DCore::QEntity *entity) {
  self->entityChanged(entity);
}

//  void Qt3DAnimation::QAnimationController::recursiveChanged(bool
//      recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation20QAnimationController16recursiveChangedEb(
    Qt3DAnimation::QAnimationController *self,
    bool recursive) {
  self->recursiveChanged(recursive);
}

//  QAnimationControllerPrivate
//      *Qt3DAnimation::QAnimationController::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationControllerPrivate *ritual_ZN13Qt3DAnimation20QAnimationController6d_funcEv(
    Qt3DAnimation::QAnimationController *self) {
  return self->d_func();
}

//  const QAnimationControllerPrivate
//      *Qt3DAnimation::QAnimationController::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationControllerPrivate *ritual_ZNK13Qt3DAnimation20QAnimationController6d_funcEv(
    const Qt3DAnimation::QAnimationController *self) {
  return self->d_func();
}

//  a QList<Qt3DAnimation::QAnimationGroup *> a ritual of
//      Qt3DAnimation::QAnimationController gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QAnimationController__QList_Qt3DAnimation_QAnimationGroup(
    QList<Qt3DAnimation::QAnimationGroup *> *self) {
  delete self;
}
