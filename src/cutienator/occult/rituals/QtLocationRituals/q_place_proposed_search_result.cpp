//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceproposedsearchresult.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/qplaceproposedsearchresult.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtLocation/qplacesearchrequest.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplaceproposedsearchresult.h>
#include <QtLocation/private/qplaceproposedsearchresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplaceproposedsearchresult.cpp, line 45, as _ZNK26QPlaceProposedSearchResult6d_funcEv
inline const QPlaceProposedSearchResultPrivate *QPlaceProposedSearchResult::d_func() const { return reinterpret_cast<const QPlaceProposedSearchResultPrivate *>(d_ptr.constData()); }
//  -----------------------------------------------------------------------

//  QPlaceProposedSearchResult::QPlaceProposedSearchResult()
extern "C" Q_DECL_EXPORT
QPlaceProposedSearchResult *ritual_ZN26QPlaceProposedSearchResultC1Ev() {
  return new QPlaceProposedSearchResult();
}

#if !(defined(Q_QDOC))
//  QPlaceProposedSearchResult::QPlaceProposedSearchResult(const
//      QPlaceSearchResult &other)
extern "C" Q_DECL_EXPORT
QPlaceProposedSearchResult *ritual_ZN26QPlaceProposedSearchResultC1ERK18QPlaceSearchResult(
    const QPlaceSearchResult *other) {
  return new QPlaceProposedSearchResult(*other);
}
#endif  // !(defined(Q_QDOC))

//  QPlaceProposedSearchResult::~QPlaceProposedSearchResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlaceProposedSearchResultD1Ev(
    QPlaceProposedSearchResult *self) {
  delete self;
}

//  QPlaceSearchRequest QPlaceProposedSearchResult::searchRequest() const
extern "C" Q_DECL_EXPORT
QPlaceSearchRequest *ritual_ZNK26QPlaceProposedSearchResult13searchRequestEv(
    const QPlaceProposedSearchResult *self) {
  return new QPlaceSearchRequest(self->searchRequest());
}

//  void QPlaceProposedSearchResult::setSearchRequest(const
//      QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlaceProposedSearchResult16setSearchRequestERK19QPlaceSearchRequest(
    QPlaceProposedSearchResult *self,
    const QPlaceSearchRequest *request) {
  self->setSearchRequest(*request);
}

//  const QPlaceProposedSearchResultPrivate
//      *QPlaceProposedSearchResult::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceProposedSearchResultPrivate *ritual_ZNK26QPlaceProposedSearchResult6d_funcEv(
    const QPlaceProposedSearchResult *self) {
  return self->d_func();
}
