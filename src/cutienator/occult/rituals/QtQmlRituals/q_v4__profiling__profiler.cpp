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

//  QString QV4::Profiling::Profiler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV49Profiling8Profiler2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QV4::Profiling::Profiler::tr(s, c, n));
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

//  void QV4::Profiling::Profiler::setTimer(const QElapsedTimer &timer)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling8Profiler8setTimerERK13QElapsedTimer(
    QV4::Profiling::Profiler *self,
    const QElapsedTimer *timer) {
  self->setTimer(*timer);
}

#endif  // !(!QT_CONFIG(qml_debug))
