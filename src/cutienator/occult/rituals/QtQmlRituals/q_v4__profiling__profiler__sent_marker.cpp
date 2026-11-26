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

//  QV4::Profiling::Profiler::SentMarker::SentMarker()
extern "C" Q_DECL_EXPORT
QV4::Profiling::Profiler::SentMarker *ritual_ZN3QV49Profiling8Profiler10SentMarkerC1Ev() {
  return new QV4::Profiling::Profiler::SentMarker();
}

//  QV4::Profiling::Profiler::SentMarker::SentMarker(const SentMarker &other)
extern "C" Q_DECL_EXPORT
QV4::Profiling::Profiler::SentMarker *ritual_ZN3QV49Profiling8Profiler10SentMarkerC1ERKS2_(
    const QV4::Profiling::Profiler::SentMarker *other) {
  return new QV4::Profiling::Profiler::SentMarker(*other);
}

//  QV4::Profiling::Profiler::SentMarker::~SentMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling8Profiler10SentMarkerD1Ev(
    QV4::Profiling::Profiler::SentMarker *self) {
  delete self;
}

//  SentMarker &QV4::Profiling::Profiler::SentMarker::operator=(const
//      SentMarker &other)
extern "C" Q_DECL_EXPORT
QV4::Profiling::Profiler::SentMarker *ritual_ZN3QV49Profiling8Profiler10SentMarkeraSERKS2_(
    QV4::Profiling::Profiler::SentMarker *self,
    const QV4::Profiling::Profiler::SentMarker *other) {
  return &(self->operator=(*other));
}

//  void QV4::Profiling::Profiler::SentMarker::setFunction(Function
//      *function)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling8Profiler10SentMarker11setFunctionEPNS_8FunctionE(
    QV4::Profiling::Profiler::SentMarker *self,
    QV4::Function *function) {
  self->setFunction(function);
}

//  bool QV4::Profiling::Profiler::SentMarker::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49Profiling8Profiler10SentMarker7isValidEv(
    const QV4::Profiling::Profiler::SentMarker *self) {
  return self->isValid();
}

#endif  // !(!QT_CONFIG(qml_debug))
