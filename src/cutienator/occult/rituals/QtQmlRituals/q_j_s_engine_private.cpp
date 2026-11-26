//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qjsengine_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: included qv4engine_p.h, as the
//  class holds a std::unique_ptr<QV4::ExecutionEngine>, whose
//  deleter needs the complete type. Kept as it is when the generator
//  runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/qjsengine.h>
#include <QtQml/6.12.0/QtQml/private/qv4engine_p.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qjsengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QJSEngine *QJSEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QJSEngine *ritual_ZN16QJSEnginePrivate6q_funcEv(QJSEnginePrivate *self) {
  return self->q_func();
}

//  const QJSEngine *QJSEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QJSEngine *ritual_ZNK16QJSEnginePrivate6q_funcEv(
    const QJSEnginePrivate *self) {
  return self->q_func();
}

//  QJSEnginePrivate *QJSEnginePrivate::get(QJSEngine *e)
extern "C" Q_DECL_EXPORT
QJSEnginePrivate *ritual_ZN16QJSEnginePrivate3getEP9QJSEngine(QJSEngine *e) {
  return QJSEnginePrivate::get(e);
}

//  const QJSEnginePrivate *QJSEnginePrivate::get(const QJSEngine *e)
extern "C" Q_DECL_EXPORT
const QJSEnginePrivate *ritual_ZN16QJSEnginePrivate3getEPK9QJSEngine(
    const QJSEngine *e) {
  return QJSEnginePrivate::get(e);
}

//  QJSEngine *QJSEnginePrivate::get(QJSEnginePrivate *e)
extern "C" Q_DECL_EXPORT
QJSEngine *ritual_ZN16QJSEnginePrivate3getEPS_(QJSEnginePrivate *e) {
  return QJSEnginePrivate::get(e);
}

//  const QJSEngine *QJSEnginePrivate::get(const QJSEnginePrivate *e)
extern "C" Q_DECL_EXPORT
const QJSEngine *ritual_ZN16QJSEnginePrivate3getEPKS_(
    const QJSEnginePrivate *e) {
  return QJSEnginePrivate::get(e);
}

//  QJSEnginePrivate *QJSEnginePrivate::get(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QJSEnginePrivate *ritual_ZN16QJSEnginePrivate3getEPN3QV415ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QJSEnginePrivate::get(e);
}

//  QJSEnginePrivate::QJSEnginePrivate()
extern "C" Q_DECL_EXPORT
QJSEnginePrivate *ritual_ZN16QJSEnginePrivateC1Ev() {
  return new QJSEnginePrivate();
}

//  QJSEnginePrivate::~QJSEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QJSEnginePrivateD1Ev(QJSEnginePrivate *self) {
  delete self;
}

//  void QJSEnginePrivate::addToDebugServer(QJSEngine *q)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QJSEnginePrivate16addToDebugServerEP9QJSEngine(
    QJSEngine *q) {
  QJSEnginePrivate::addToDebugServer(q);
}

//  void QJSEnginePrivate::removeFromDebugServer(QJSEngine *q)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QJSEnginePrivate21removeFromDebugServerEP9QJSEngine(
    QJSEngine *q) {
  QJSEnginePrivate::removeFromDebugServer(q);
}

//  void QJSEnginePrivate::uiLanguageChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QJSEnginePrivate17uiLanguageChangedEv(
    QJSEnginePrivate *self) {
  self->uiLanguageChanged();
}
