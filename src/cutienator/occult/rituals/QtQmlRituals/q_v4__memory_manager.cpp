//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mm_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 10. Kept
//  as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mm_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <vector>
#include <QtCore/QObject>

//  QV4::MemoryManager::MemoryManager(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::MemoryManager *ritual_ZN3QV413MemoryManagerC1EPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QV4::MemoryManager(engine);
}

//  QV4::MemoryManager::~MemoryManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManagerD1Ev(QV4::MemoryManager *self) {
  delete self;
}

//  std::size_t QV4::MemoryManager::align(std::size_t size)
extern "C" Q_DECL_EXPORT
std::size_t ritual_ZN3QV413MemoryManager5alignEm(std::size_t size) {
  return QV4::MemoryManager::align(size);
}

//  void QV4::MemoryManager::runGC()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager5runGCEv(QV4::MemoryManager *self) {
  self->runGC();
}

//  bool QV4::MemoryManager::tryForceGCCompletion()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV413MemoryManager20tryForceGCCompletionEv(
    QV4::MemoryManager *self) {
  return self->tryForceGCCompletion();
}

//  void QV4::MemoryManager::runFullGC()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager9runFullGCEv(QV4::MemoryManager *self) {
  self->runFullGC();
}

//  void QV4::MemoryManager::dumpStats() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV413MemoryManager9dumpStatsEv(
    const QV4::MemoryManager *self) {
  self->dumpStats();
}

//  size_t QV4::MemoryManager::getRegularItemsMem() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV413MemoryManager18getRegularItemsMemEv(
    const QV4::MemoryManager *self) {
  return self->getRegularItemsMem();
}

//  size_t QV4::MemoryManager::getAllocatedMem() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV413MemoryManager15getAllocatedMemEv(
    const QV4::MemoryManager *self) {
  return self->getAllocatedMem();
}

//  size_t QV4::MemoryManager::getLargeItemsMem() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV413MemoryManager16getLargeItemsMemEv(
    const QV4::MemoryManager *self) {
  return self->getLargeItemsMem();
}

//  void QV4::MemoryManager::changeUnmanagedHeapSizeUsage(qptrdiff delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager28changeUnmanagedHeapSizeUsageEx(
    QV4::MemoryManager *self,
    qptrdiff delta) {
  self->changeUnmanagedHeapSizeUsage(delta);
}

//  void QV4::MemoryManager::updateUnmanagedHeapSizeGCLimit()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager30updateUnmanagedHeapSizeGCLimitEv(
    QV4::MemoryManager *self) {
  self->updateUnmanagedHeapSizeGCLimit();
}

//  void QV4::MemoryManager::registerWeakMap(Heap::MapObject *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager15registerWeakMapEPNS_4Heap9MapObjectE(
    QV4::MemoryManager *self,
    QV4::Heap::MapObject *map) {
  self->registerWeakMap(map);
}

//  void QV4::MemoryManager::registerWeakSet(Heap::SetObject *set)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager15registerWeakSetEPNS_4Heap9SetObjectE(
    QV4::MemoryManager *self,
    QV4::Heap::SetObject *set) {
  self->registerWeakSet(set);
}

//  void QV4::MemoryManager::onEventLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager11onEventLoopEv(QV4::MemoryManager *self) {
  self->onEventLoop();
}

//  void QV4::MemoryManager::setGCTimeLimit(int timeMs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager14setGCTimeLimitEi(
    QV4::MemoryManager *self,
    int timeMs) {
  self->setGCTimeLimit(timeMs);
}

//  MarkStack *QV4::MemoryManager::markStack()
extern "C" Q_DECL_EXPORT
QV4::MarkStack *ritual_ZN3QV413MemoryManager9markStackEv(
    QV4::MemoryManager *self) {
  return self->markStack();
}

//  std::vector<QObject *> QV4::MemoryManager::findObjectsForCompilationUnits
//      (std::vector<QQmlRefPointer<CompiledData::CompilationUnit>> &&units)
extern "C" Q_DECL_EXPORT
std::vector<QObject *> *ritual_ZN3QV413MemoryManager30findObjectsForCompilationUnitsEOSt6vectorI14QQmlRefPointerINS_12CompiledData15CompilationUnitEESaIS5_EE(
    QV4::MemoryManager *self,
    std::vector<QQmlRefPointer<QV4::CompiledData::CompilationUnit>> *units) {
  return new std::vector<QObject *>(
      self->findObjectsForCompilationUnits(
          std::move(*units)));
}

//  Heap::Base *QV4::MemoryManager::allocString(std::size_t unmanagedSize)
extern "C" Q_DECL_EXPORT
QV4::Heap::Base *ritual_ZN3QV413MemoryManager11allocStringEm(
    QV4::MemoryManager *self,
    std::size_t unmanagedSize) {
  return self->allocString(unmanagedSize);
}

//  Heap::Base *QV4::MemoryManager::allocData(std::size_t size)
extern "C" Q_DECL_EXPORT
QV4::Heap::Base *ritual_ZN3QV413MemoryManager9allocDataEm(
    QV4::MemoryManager *self,
    std::size_t size) {
  return self->allocData(size);
}

//  Heap::Object *QV4::MemoryManager::allocObjectWithMemberData(const
//      QV4::VTable *vtable, uint nMembers)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager25allocObjectWithMemberDataEPKNS_6VTableEj(
    QV4::MemoryManager *self,
    const QV4::VTable *vtable,
    uint nMembers) {
  return self->allocObjectWithMemberData(vtable, nMembers);
}

//  void QV4::MemoryManager::collectFromJSStack(MarkStack *markStack) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV413MemoryManager18collectFromJSStackEPNS_9MarkStackE(
    const QV4::MemoryManager *self,
    QV4::MarkStack *markStack) {
  self->collectFromJSStack(markStack);
}

//  void QV4::MemoryManager::sweep(bool lastSweep)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager5sweepEb(
    QV4::MemoryManager *self,
    bool lastSweep) {
  self->sweep(lastSweep);
}

//  void QV4::MemoryManager::cleanupDeletedQObjectWrappersInSweep()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413MemoryManager36cleanupDeletedQObjectWrappersInSweepEv(
    QV4::MemoryManager *self) {
  self->cleanupDeletedQObjectWrappersInSweep();
}

//  bool QV4::MemoryManager::isAboveUnmanagedHeapLimit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV413MemoryManager25isAboveUnmanagedHeapLimitEv(
    QV4::MemoryManager *self) {
  return self->isAboveUnmanagedHeapLimit();
}

//  bool QV4::MemoryManager::shouldRunGC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV413MemoryManager11shouldRunGCEv(
    const QV4::MemoryManager *self) {
  return self->shouldRunGC();
}

//  a std::vector<QObject *> a ritual of QV4::MemoryManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_MemoryManager__std_vector_QObject(
    std::vector<QObject *> *self) {
  delete self;
}

#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h>

//  QV4::Object::Data *QV4::MemoryManager::allocManaged<QV4::Object>(
//      std::size_t size, Heap::InternalClass *ic)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager12allocManagedINS_6ObjectEEEPNT_4DataEmPNS_4Heap13InternalClassE(
    QV4::MemoryManager *self, std::size_t size,
    QV4::Heap::InternalClass *ic) {
  return self->allocManaged<QV4::Object>(size, ic);
}

//  QV4::Object::Data *QV4::MemoryManager::allocManaged<QV4::Object>(
//      Heap::InternalClass *ic)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager12allocManagedINS_6ObjectEEEPNT_4DataEPNS_4Heap13InternalClassE(
    QV4::MemoryManager *self, QV4::Heap::InternalClass *ic) {
  return self->allocManaged<QV4::Object>(ic);
}

//  QV4::Object::Data *QV4::MemoryManager::allocManaged<QV4::Object>(
//      std::size_t size, InternalClass *ic)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager12allocManagedINS_6ObjectEEEPNT_4DataEmPNS_13InternalClassE(
    QV4::MemoryManager *self, std::size_t size, QV4::InternalClass *ic) {
  return self->allocManaged<QV4::Object>(size, ic);
}

//  QV4::Object::Data *QV4::MemoryManager::allocManaged<QV4::Object>(
//      InternalClass *ic)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager12allocManagedINS_6ObjectEEEPNT_4DataEPNS_13InternalClassE(
    QV4::MemoryManager *self, QV4::InternalClass *ic) {
  return self->allocManaged<QV4::Object>(ic);
}

//  QV4::Object::Data *QV4::MemoryManager::allocManaged<QV4::Object>(
//      std::size_t size)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager12allocManagedINS_6ObjectEEEPNT_4DataEm(
    QV4::MemoryManager *self, std::size_t size) {
  return self->allocManaged<QV4::Object>(size);
}

//  QV4::Object::Data *QV4::MemoryManager::allocManaged<QV4::Object>()
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager12allocManagedINS_6ObjectEEEPNT_4DataEv(
    QV4::MemoryManager *self) {
  return self->allocManaged<QV4::Object>();
}

//  QV4::Object::Data *QV4::MemoryManager::allocateObject<QV4::Object>(
//      Heap::InternalClass *ic)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager14allocateObjectINS_6ObjectEEEPNT_4DataEPNS_4Heap13InternalClassE(
    QV4::MemoryManager *self, QV4::Heap::InternalClass *ic) {
  return self->allocateObject<QV4::Object>(ic);
}

//  QV4::Object::Data *QV4::MemoryManager::allocateObject<QV4::Object>(
//      InternalClass *ic)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager14allocateObjectINS_6ObjectEEEPNT_4DataEPNS_13InternalClassE(
    QV4::MemoryManager *self, QV4::InternalClass *ic) {
  return self->allocateObject<QV4::Object>(ic);
}

//  QV4::Object::Data *QV4::MemoryManager::allocateObject<QV4::Object>()
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV413MemoryManager14allocateObjectINS_6ObjectEEEPNT_4DataEv(
    QV4::MemoryManager *self) {
  return self->allocateObject<QV4::Object>();
}

//  QV4::String::Data *QV4::MemoryManager::allocWithStringData<QV4::String,
//      const QString &>(std::size_t unmanagedSize, const QString &arg1)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV413MemoryManager19allocWithStringDataINS_6StringERK7QStringEEPNT_4DataEmOT0_(
    QV4::MemoryManager *self, std::size_t unmanagedSize,
    const QString *arg1) {
  return self->allocWithStringData<QV4::String, const QString &>(
      unmanagedSize, *arg1);
}
