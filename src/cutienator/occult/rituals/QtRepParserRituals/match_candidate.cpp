//  Written by dev_tooling.RitualGenerator from the records of
//  QtRepParser/qregexparser.h, Qt 6.12.0. Changes made here are lost.
#include <QtRepParser/qregexparser.h>
#include <QtCore/qstring.h>

//  MatchCandidate::MatchCandidate(const QString &n, const QString &t, int i)
extern "C" Q_DECL_EXPORT
MatchCandidate *ritual_ZN14MatchCandidateC1ERK7QStringS2_i(
    const QString *n,
    const QString *t,
    int i) {
  return new MatchCandidate(*n, *t, i);
}

//  MatchCandidate::~MatchCandidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14MatchCandidateD1Ev(MatchCandidate *self) {
  delete self;
}
