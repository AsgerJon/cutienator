//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsmemorypool_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsmemorypool_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QQmlJS::MemoryPool::MemoryPool()
extern "C" Q_DECL_EXPORT
QQmlJS::MemoryPool *ritual_ZN6QQmlJS10MemoryPoolC1Ev() {
  return new QQmlJS::MemoryPool();
}

//  QQmlJS::MemoryPool::~MemoryPool()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS10MemoryPoolD1Ev(QQmlJS::MemoryPool *self) {
  delete self;
}

//  void QQmlJS::MemoryPool::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS10MemoryPool5resetEv(QQmlJS::MemoryPool *self) {
  self->reset();
}

//  QStringView QQmlJS::MemoryPool::newString(QString string)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QQmlJS10MemoryPool9newStringE7QString(
    QQmlJS::MemoryPool *self,
    const QString *string) {
  return new QString(self->newString(*string).toString());
}
