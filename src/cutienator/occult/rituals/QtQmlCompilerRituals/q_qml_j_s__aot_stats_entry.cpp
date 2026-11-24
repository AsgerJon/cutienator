//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilerstats_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QQmlJS::AotStatsEntry::operator<(const AotStatsEntry &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS13AotStatsEntryltERKS0_(
    const QQmlJS::AotStatsEntry *self,
    const QQmlJS::AotStatsEntry *a0) {
  return self->operator<(*a0);
}

//  QQmlJS::AotStatsEntry::~AotStatsEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS13AotStatsEntryD1Ev(QQmlJS::AotStatsEntry *self) {
  delete self;
}
