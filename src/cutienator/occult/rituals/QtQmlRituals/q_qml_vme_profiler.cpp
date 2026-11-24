//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlVmeProfiler::QQmlVmeProfiler()
extern "C" Q_DECL_EXPORT
QQmlVmeProfiler *ritual_ZN15QQmlVmeProfilerC1Ev() {
  return new QQmlVmeProfiler();
}

//  void QQmlVmeProfiler::init(QQmlProfiler *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlVmeProfiler4initEP12QQmlProfiler(
    QQmlVmeProfiler *self,
    QQmlProfiler *p) {
  self->init(p);
}

//  const QV4::CompiledData::Object *QQmlVmeProfiler::pop()
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Object *ritual_ZN15QQmlVmeProfiler3popEv(
    QQmlVmeProfiler *self) {
  return self->pop();
}

//  void QQmlVmeProfiler::push(const QV4::CompiledData::Object *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlVmeProfiler4pushEPKN3QV412CompiledData6ObjectE(
    QQmlVmeProfiler *self,
    const QV4::CompiledData::Object *object) {
  self->push(object);
}

//  QQmlVmeProfiler::~QQmlVmeProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlVmeProfilerD1Ev(QQmlVmeProfiler *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
