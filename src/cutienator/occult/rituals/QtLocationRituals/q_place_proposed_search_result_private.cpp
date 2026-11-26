//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplaceproposedsearchresult_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplaceproposedsearchresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacesearchresult.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacesearchresult.h>
#include <QtLocation/private/qplacesearchresult_p.h>
#include <QtLocation/qplaceresult.h>
#include <QtCore/qnumeric.h>
#include <QtLocation/qplaceproposedsearchresult.h>
#include <QtLocation/private/qplaceproposedsearchresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacesearchresult.cpp, line 27, as _ZNK25QPlaceSearchResultPrivate7compareEPKS_
inline bool QPlaceSearchResultPrivate::compare(const QPlaceSearchResultPrivate *other) const
{
    return title == other->title
            && icon == other->icon;
}

//  from ../qtlocation/src/location/places/qplaceproposedsearchresult.cpp, line 11, as _ZNK33QPlaceProposedSearchResultPrivate7compareEPK25QPlaceSearchResultPrivate
inline bool QPlaceProposedSearchResultPrivate::compare(const QPlaceSearchResultPrivate *other) const
{
    const QPlaceProposedSearchResultPrivate *od = static_cast<const QPlaceProposedSearchResultPrivate *>(other);
    return QPlaceSearchResultPrivate::compare(other) && searchRequest == od->searchRequest;
}
//  -----------------------------------------------------------------------

//  A QPlaceProposedSearchResultPrivate that Python can take functions over in. Every QPlaceProposedSearchResultPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlaceProposedSearchResultPrivateCall0)(const void *, const QPlaceSearchResultPrivate *, int *);
typedef void * (*CuteQPlaceProposedSearchResultPrivateCall1)(const void *, int *);
typedef int (*CuteQPlaceProposedSearchResultPrivateCall2)(const void *, int *);
class CuteQPlaceProposedSearchResultPrivate : public QPlaceProposedSearchResultPrivate {
public:
  using QPlaceProposedSearchResultPrivate::QPlaceProposedSearchResultPrivate;
  CuteQPlaceProposedSearchResultPrivate(const QPlaceProposedSearchResultPrivate & other) : QPlaceProposedSearchResultPrivate(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QPlaceSearchResultPrivate7compareEPKS_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlaceSearchResultPrivate5cloneEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlaceSearchResultPrivate4typeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool QPlaceProposedSearchResultPrivate::compare(const
  //      QPlaceSearchResultPrivate *other) const
  bool compare(const QPlaceSearchResultPrivate *other) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceProposedSearchResultPrivateCall0 call = reinterpret_cast<CuteQPlaceProposedSearchResultPrivateCall0>(taken[0]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QPlaceProposedSearchResultPrivate::compare(other);
  }

  //  QPlaceSearchResultPrivate *QPlaceProposedSearchResultPrivate::clone()
  //      const
  QPlaceSearchResultPrivate *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceProposedSearchResultPrivateCall1 call = reinterpret_cast<CuteQPlaceProposedSearchResultPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlaceSearchResultPrivate *>(given);
    }
    return QPlaceProposedSearchResultPrivate::clone();
  }

  //  QPlaceSearchResult::SearchResultType
  //      QPlaceProposedSearchResultPrivate::type() const
  QPlaceSearchResult::SearchResultType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlaceProposedSearchResultPrivateCall2 call = reinterpret_cast<CuteQPlaceProposedSearchResultPrivateCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceSearchResult::SearchResultType>(given);
    }
    return QPlaceProposedSearchResultPrivate::type();
  }
};

//  bool QPlaceProposedSearchResultPrivate::compare(const
//      QPlaceSearchResultPrivate *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QPlaceProposedSearchResultPrivate7compareEPK25QPlaceSearchResultPrivate(
    const QPlaceProposedSearchResultPrivate *self,
    const QPlaceSearchResultPrivate *other) {
  return self->compare(other);
}

//  QPlaceSearchResultPrivate *QPlaceProposedSearchResultPrivate::clone()
//      const
extern "C" Q_DECL_EXPORT
QPlaceSearchResultPrivate *ritual_ZNK33QPlaceProposedSearchResultPrivate5cloneEv(
    const QPlaceProposedSearchResultPrivate *self) {
  return self->clone();
}

//  QPlaceSearchResult::SearchResultType
//      QPlaceProposedSearchResultPrivate::type() const
extern "C" Q_DECL_EXPORT
QPlaceSearchResult::SearchResultType ritual_ZNK33QPlaceProposedSearchResultPrivate4typeEv(
    const QPlaceProposedSearchResultPrivate *self) {
  return self->type();
}

//  void QPlaceProposedSearchResultPrivate::copyIfPossible(QSharedDataPointer
//      <QPlaceSearchResultPrivate> &d_ptr, const QPlaceSearchResult &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QPlaceProposedSearchResultPrivate14copyIfPossibleER18QSharedDataPointerI25QPlaceSearchResultPrivateERK18QPlaceSearchResult(
    QSharedDataPointer<QPlaceSearchResultPrivate> *d_ptr,
    const QPlaceSearchResult *other) {
  QPlaceProposedSearchResultPrivate::copyIfPossible(*d_ptr, *other);
}

//  QPlaceProposedSearchResultPrivate::~QPlaceProposedSearchResultPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QPlaceProposedSearchResultPrivateD1Ev(
    QPlaceProposedSearchResultPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQPlaceProposedSearchResultPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceProposedSearchResultPrivate(
    QPlaceProposedSearchResultPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceProposedSearchResultPrivate *>(self)->take(key, call);
}

//  bool QPlaceProposedSearchResultPrivate::compare(const
//      QPlaceSearchResultPrivate *other) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK33QPlaceProposedSearchResultPrivate7compareEPK25QPlaceSearchResultPrivate(
    const QPlaceProposedSearchResultPrivate *self,
    const QPlaceSearchResultPrivate *other) {
  return self->QPlaceProposedSearchResultPrivate::compare(other);
}

//  QPlaceSearchResult::SearchResultType
//      QPlaceProposedSearchResultPrivate::type() const
extern "C" Q_DECL_EXPORT
QPlaceSearchResult::SearchResultType ritual_own_ZNK33QPlaceProposedSearchResultPrivate4typeEv(
    const QPlaceProposedSearchResultPrivate *self) {
  return self->QPlaceProposedSearchResultPrivate::type();
}
