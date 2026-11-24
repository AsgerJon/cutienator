//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplaceresult_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplaceresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplacesearchresult.h"
#include "qplacesearchresult_p.h"
#include "qplaceresult.h"
#include <QtCore/qnumeric.h>
#include "qplaceresult.h"
#include "qplaceresult_p.h"
#include <QtCore/qnumeric.h>
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

//  from ../qtlocation/src/location/places/qplaceresult.cpp, line 11, as _ZNK19QPlaceResultPrivate7compareEPK25QPlaceSearchResultPrivate
inline bool QPlaceResultPrivate::compare(const QPlaceSearchResultPrivate *other) const
{
    const QPlaceResultPrivate *od = static_cast<const QPlaceResultPrivate *>(other);
    return QPlaceSearchResultPrivate::compare(other)
           && ((qIsNaN(distance) && qIsNaN(od->distance))
                || QtPrivate::fuzzyCompare(distance, od->distance))
           && place == od->place
           && sponsored == od->sponsored;
}
//  -----------------------------------------------------------------------

//  A QPlaceResultPrivate that Python can take functions over in. Every QPlaceResultPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlaceResultPrivateCall0)(const void *, const QPlaceSearchResultPrivate *, int *);
typedef void * (*CuteQPlaceResultPrivateCall1)(const void *, int *);
typedef int (*CuteQPlaceResultPrivateCall2)(const void *, int *);
class CuteQPlaceResultPrivate : public QPlaceResultPrivate {
public:
  using QPlaceResultPrivate::QPlaceResultPrivate;
  CuteQPlaceResultPrivate(const QPlaceResultPrivate &other) : QPlaceResultPrivate(other) {}
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

  //  bool QPlaceResultPrivate::compare(const QPlaceSearchResultPrivate
  //      *other) const
  bool compare(const QPlaceSearchResultPrivate *other) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceResultPrivateCall0 call = reinterpret_cast<CuteQPlaceResultPrivateCall0>(taken[0]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QPlaceResultPrivate::compare(other);
  }

  //  QPlaceSearchResultPrivate *QPlaceResultPrivate::clone() const
  QPlaceSearchResultPrivate *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceResultPrivateCall1 call = reinterpret_cast<CuteQPlaceResultPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlaceSearchResultPrivate *>(given);
    }
    return QPlaceResultPrivate::clone();
  }

  //  QPlaceSearchResult::SearchResultType QPlaceResultPrivate::type()
  //      const
  QPlaceSearchResult::SearchResultType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlaceResultPrivateCall2 call = reinterpret_cast<CuteQPlaceResultPrivateCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceSearchResult::SearchResultType>(given);
    }
    return QPlaceResultPrivate::type();
  }
};

//  bool QPlaceResultPrivate::compare(const QPlaceSearchResultPrivate *other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QPlaceResultPrivate7compareEPK25QPlaceSearchResultPrivate(
    const QPlaceResultPrivate *self,
    const QPlaceSearchResultPrivate *other) {
  return self->compare(other);
}

//  QPlaceSearchResultPrivate *QPlaceResultPrivate::clone() const
extern "C" Q_DECL_EXPORT
QPlaceSearchResultPrivate *ritual_ZNK19QPlaceResultPrivate5cloneEv(
    const QPlaceResultPrivate *self) {
  return self->clone();
}

//  QPlaceSearchResult::SearchResultType QPlaceResultPrivate::type() const
extern "C" Q_DECL_EXPORT
QPlaceSearchResult::SearchResultType ritual_ZNK19QPlaceResultPrivate4typeEv(
    const QPlaceResultPrivate *self) {
  return self->type();
}

//  QPlaceResultPrivate::~QPlaceResultPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceResultPrivateD1Ev(QPlaceResultPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQPlaceResultPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceResultPrivate(
    QPlaceResultPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceResultPrivate *>(self)->take(key, call);
}

//  bool QPlaceResultPrivate::compare(const QPlaceSearchResultPrivate *other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QPlaceResultPrivate7compareEPK25QPlaceSearchResultPrivate(
    const QPlaceResultPrivate *self,
    const QPlaceSearchResultPrivate *other) {
  return self->QPlaceResultPrivate::compare(other);
}

//  QPlaceSearchResult::SearchResultType QPlaceResultPrivate::type() const
extern "C" Q_DECL_EXPORT
QPlaceSearchResult::SearchResultType ritual_own_ZNK19QPlaceResultPrivate4typeEv(
    const QPlaceResultPrivate *self) {
  return self->QPlaceResultPrivate::type();
}
