//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DLogic/6.12.0/Qt3DLogic/private/executor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DLogic/Qt3DLogic>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DLogic/6.12.0/Qt3DLogic/private/executor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *Qt3DLogic::Logic::Executor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DLogic5Logic8Executor10metaObjectEv(
    const Qt3DLogic::Logic::Executor *self) {
  return self->metaObject();
}

//  void *Qt3DLogic::Logic::Executor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DLogic5Logic8Executor11qt_metacastEPKc(
    Qt3DLogic::Logic::Executor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DLogic::Logic::Executor::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DLogic5Logic8Executor11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DLogic::Logic::Executor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void Qt3DLogic::Logic::Executor::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic8Executor8setSceneEPN8Qt3DCore6QSceneE(
    Qt3DLogic::Logic::Executor *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  void Qt3DLogic::Logic::Executor::processLogicFrameUpdates(const
//      QList<Qt3DCore::QNodeId> &nodeIds, float dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DLogic5Logic8Executor24processLogicFrameUpdatesERK5QListIN8Qt3DCore7QNodeIdEEf(
    Qt3DLogic::Logic::Executor *self,
    const QList<Qt3DCore::QNodeId> *nodeIds,
    float dt) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DLogic::Logic::Executor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "processLogicFrameUpdates(const QList<Qt3DCore::QNodeId> &,float)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "processLogicFrameUpdates(const QList<Qt3DCore::QNodeId> &,float)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(nodeIds)),
      const_cast<void *>(static_cast<const void *>(&dt)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
