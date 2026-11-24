//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplacesearchresult_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplacesearchresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacesearchresult.h>
#include <QtLocation/private/qplacesearchresult_p.h>
#include <QtLocation/qplaceresult.h>
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
//  -----------------------------------------------------------------------

//  A QPlaceSearchResultPrivate that Python can take functions over in. Every QPlaceSearchResultPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlaceSearchResultPrivateCall0)(const void *, const QPlaceSearchResultPrivate *, int *);
typedef void * (*CuteQPlaceSearchResultPrivateCall1)(const void *, int *);
typedef int (*CuteQPlaceSearchResultPrivateCall2)(const void *, int *);
class CuteQPlaceSearchResultPrivate : public QPlaceSearchResultPrivate {
public:
  using QPlaceSearchResultPrivate::QPlaceSearchResultPrivate;
  CuteQPlaceSearchResultPrivate(const QPlaceSearchResultPrivate &other) : QPlaceSearchResultPrivate(other) {}
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

  //  bool QPlaceSearchResultPrivate::compare(const
  //      QPlaceSearchResultPrivate *other) const
  bool compare(const QPlaceSearchResultPrivate *other) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceSearchResultPrivateCall0 call = reinterpret_cast<CuteQPlaceSearchResultPrivateCall0>(taken[0]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QPlaceSearchResultPrivate::compare(other);
  }

  //  QPlaceSearchResultPrivate *QPlaceSearchResultPrivate::clone() const
  QPlaceSearchResultPrivate *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceSearchResultPrivateCall1 call = reinterpret_cast<CuteQPlaceSearchResultPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlaceSearchResultPrivate *>(given);
    }
    return QPlaceSearchResultPrivate::clone();
  }

  //  QPlaceSearchResult::SearchResultType
  //      QPlaceSearchResultPrivate::type() const
  QPlaceSearchResult::SearchResultType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlaceSearchResultPrivateCall2 call = reinterpret_cast<CuteQPlaceSearchResultPrivateCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlaceSearchResult::SearchResultType>(given);
    }
    return QPlaceSearchResultPrivate::type();
  }
};

//  QPlaceSearchResultPrivate::~QPlaceSearchResultPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlaceSearchResultPrivateD1Ev(
    QPlaceSearchResultPrivate *self) {
  delete self;
}

//  bool QPlaceSearchResultPrivate::compare(const QPlaceSearchResultPrivate
//      *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QPlaceSearchResultPrivate7compareEPKS_(
    const QPlaceSearchResultPrivate *self,
    const QPlaceSearchResultPrivate *other) {
  return self->compare(other);
}

//  QPlaceSearchResultPrivate *QPlaceSearchResultPrivate::clone() const
extern "C" Q_DECL_EXPORT
QPlaceSearchResultPrivate *ritual_ZNK25QPlaceSearchResultPrivate5cloneEv(
    const QPlaceSearchResultPrivate *self) {
  return self->clone();
}

//  QPlaceSearchResult::SearchResultType QPlaceSearchResultPrivate::type()
//      const
extern "C" Q_DECL_EXPORT
QPlaceSearchResult::SearchResultType ritual_ZNK25QPlaceSearchResultPrivate4typeEv(
    const QPlaceSearchResultPrivate *self) {
  return self->type();
}

//  a Python function taken by a CuteQPlaceSearchResultPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceSearchResultPrivate(
    QPlaceSearchResultPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceSearchResultPrivate *>(self)->take(key, call);
}

//  bool QPlaceSearchResultPrivate::compare(const QPlaceSearchResultPrivate
//      *other) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QPlaceSearchResultPrivate7compareEPKS_(
    const QPlaceSearchResultPrivate *self,
    const QPlaceSearchResultPrivate *other) {
  return self->QPlaceSearchResultPrivate::compare(other);
}

//  QPlaceSearchResult::SearchResultType QPlaceSearchResultPrivate::type()
//      const
extern "C" Q_DECL_EXPORT
QPlaceSearchResult::SearchResultType ritual_own_ZNK25QPlaceSearchResultPrivate4typeEv(
    const QPlaceSearchResultPrivate *self) {
  return self->QPlaceSearchResultPrivate::type();
}
