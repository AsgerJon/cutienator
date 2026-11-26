//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4profiling_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4profiling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qelapsedtimer.h>

//  const QMetaObject *QV4::Profiling::Profiler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV49Profiling8Profiler10metaObjectEv(
    const QV4::Profiling::Profiler *self) {
  return self->metaObject();
}

//  void *QV4::Profiling::Profiler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN3QV49Profiling8Profiler11qt_metacastEPKc(
    QV4::Profiling::Profiler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QV4::Profiling::Profiler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV49Profiling8Profiler11qt_metacallEN11QMetaObject4CallEiPPv(
    QV4::Profiling::Profiler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QV4::Profiling::Profiler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV49Profiling8Profiler2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QV4::Profiling::Profiler::tr(s, c, n));
}

//  QV4::Profiling::Profiler::Profiler(QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::Profiling::Profiler *ritual_ZN3QV49Profiling8ProfilerC1EPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QV4::Profiling::Profiler(engine);
}

//  bool QV4::Profiling::Profiler::trackAlloc(size_t size, MemoryType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49Profiling8Profiler10trackAllocEmNS0_10MemoryTypeE(
    QV4::Profiling::Profiler *self,
    size_t size,
    QV4::Profiling::MemoryType type) {
  return self->trackAlloc(size, type);
}

//  bool QV4::Profiling::Profiler::trackDealloc(size_t size, MemoryType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49Profiling8Profiler12trackDeallocEmNS0_10MemoryTypeE(
    QV4::Profiling::Profiler *self,
    size_t size,
    QV4::Profiling::MemoryType type) {
  return self->trackDealloc(size, type);
}

//  void QV4::Profiling::Profiler::stopProfiling()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling8Profiler13stopProfilingEv(
    QV4::Profiling::Profiler *self) {
  self->stopProfiling();
}

//  void QV4::Profiling::Profiler::startProfiling(quint64 features)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling8Profiler14startProfilingEy(
    QV4::Profiling::Profiler *self,
    quint64 features) {
  self->startProfiling(features);
}

//  void QV4::Profiling::Profiler::reportData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling8Profiler10reportDataEv(
    QV4::Profiling::Profiler *self) {
  self->reportData();
}

//  void QV4::Profiling::Profiler::setTimer(const QElapsedTimer &timer)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling8Profiler8setTimerERK13QElapsedTimer(
    QV4::Profiling::Profiler *self,
    const QElapsedTimer *timer) {
  self->setTimer(*timer);
}

//  void QV4::Profiling::Profiler::dataReady(const
//      QV4::Profiling::FunctionLocationHash &a0, const
//      QList<QV4::Profiling::FunctionCallProperties> &a1, const
//      QList<QV4::Profiling::MemoryAllocationProperties> &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling8Profiler9dataReadyERK5QHashIyNS0_16FunctionLocationEERK5QListINS0_22FunctionCallPropertiesEERKS7_INS0_26MemoryAllocationPropertiesEE(
    QV4::Profiling::Profiler *self,
    const QV4::Profiling::FunctionLocationHash *a0,
    const QList<QV4::Profiling::FunctionCallProperties> *a1,
    const QList<QV4::Profiling::MemoryAllocationProperties> *a2) {
  self->dataReady(*a0, *a1, *a2);
}

#endif  // !(!QT_CONFIG(qml_debug))
