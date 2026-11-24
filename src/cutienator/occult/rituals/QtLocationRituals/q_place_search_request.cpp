//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacesearchrequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/qplacesearchrequest.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplacecategory.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplacesearchrequest.h"
#include "qplacesearchrequest_p.h"
#include "qgeocoordinate.h"
#include "qgeoshape.h"
#include <QtLocation/QPlaceCategory>
#include <QtCore/QSharedData>
#include <QtCore/QList>
#include <QtCore/QVariant>
#include <QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacesearchrequest.cpp, line 348, as _ZN19QPlaceSearchRequest6d_funcEv
inline QPlaceSearchRequestPrivate *QPlaceSearchRequest::d_func()
{
    return static_cast<QPlaceSearchRequestPrivate *>(d_ptr.data());
}

//  from ../qtlocation/src/location/places/qplacesearchrequest.cpp, line 353, as _ZNK19QPlaceSearchRequest6d_funcEv
inline const QPlaceSearchRequestPrivate *QPlaceSearchRequest::d_func() const
{
    return static_cast<const QPlaceSearchRequestPrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QPlaceSearchRequest::QPlaceSearchRequest()
extern "C" Q_DECL_EXPORT
QPlaceSearchRequest *ritual_ZN19QPlaceSearchRequestC1Ev() {
  return new QPlaceSearchRequest();
}

//  QPlaceSearchRequest::QPlaceSearchRequest(const QPlaceSearchRequest
//      &other)
extern "C" Q_DECL_EXPORT
QPlaceSearchRequest *ritual_ZN19QPlaceSearchRequestC1ERKS_(
    const QPlaceSearchRequest *other) {
  return new QPlaceSearchRequest(*other);
}

//  QPlaceSearchRequest::~QPlaceSearchRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequestD1Ev(QPlaceSearchRequest *self) {
  delete self;
}

//  bool operator==(const QPlaceSearchRequest &lhs, const QPlaceSearchRequest
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QPlaceSearchRequestS1_(
    const QPlaceSearchRequest *lhs,
    const QPlaceSearchRequest *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceSearchRequest &lhs, const QPlaceSearchRequest
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QPlaceSearchRequestS1_(
    const QPlaceSearchRequest *lhs,
    const QPlaceSearchRequest *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QPlaceSearchRequest::searchTerm() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QPlaceSearchRequest10searchTermEv(
    const QPlaceSearchRequest *self) {
  return new QString(self->searchTerm());
}

//  void QPlaceSearchRequest::setSearchTerm(const QString &term)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest13setSearchTermERK7QString(
    QPlaceSearchRequest *self,
    const QString *term) {
  self->setSearchTerm(*term);
}

//  QList<QPlaceCategory> QPlaceSearchRequest::categories() const
extern "C" Q_DECL_EXPORT
QList<QPlaceCategory> *ritual_ZNK19QPlaceSearchRequest10categoriesEv(
    const QPlaceSearchRequest *self) {
  return new QList<QPlaceCategory>(self->categories());
}

//  void QPlaceSearchRequest::setCategory(const QPlaceCategory &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest11setCategoryERK14QPlaceCategory(
    QPlaceSearchRequest *self,
    const QPlaceCategory *category) {
  self->setCategory(*category);
}

//  void QPlaceSearchRequest::setCategories(const QList<QPlaceCategory>
//      &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest13setCategoriesERK5QListI14QPlaceCategoryE(
    QPlaceSearchRequest *self,
    const QList<QPlaceCategory> *categories) {
  self->setCategories(*categories);
}

//  QGeoShape QPlaceSearchRequest::searchArea() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK19QPlaceSearchRequest10searchAreaEv(
    const QPlaceSearchRequest *self) {
  return new QGeoShape(self->searchArea());
}

//  void QPlaceSearchRequest::setSearchArea(const QGeoShape &area)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest13setSearchAreaERK9QGeoShape(
    QPlaceSearchRequest *self,
    const QGeoShape *area) {
  self->setSearchArea(*area);
}

//  QString QPlaceSearchRequest::recommendationId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QPlaceSearchRequest16recommendationIdEv(
    const QPlaceSearchRequest *self) {
  return new QString(self->recommendationId());
}

//  void QPlaceSearchRequest::setRecommendationId(const QString
//      &recommendationId)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest19setRecommendationIdERK7QString(
    QPlaceSearchRequest *self,
    const QString *recommendationId) {
  self->setRecommendationId(*recommendationId);
}

//  QVariant QPlaceSearchRequest::searchContext() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QPlaceSearchRequest13searchContextEv(
    const QPlaceSearchRequest *self) {
  return new QVariant(self->searchContext());
}

//  void QPlaceSearchRequest::setSearchContext(const QVariant &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest16setSearchContextERK8QVariant(
    QPlaceSearchRequest *self,
    const QVariant *context) {
  self->setSearchContext(*context);
}

//  QLocation::VisibilityScope QPlaceSearchRequest::visibilityScope() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QPlaceSearchRequest15visibilityScopeEv(
    const QPlaceSearchRequest *self) {
  return static_cast<int>(self->visibilityScope().toInt());
}

//  void QPlaceSearchRequest::setVisibilityScope(QLocation::VisibilityScope
//      visibilityScopes)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest18setVisibilityScopeE6QFlagsIN9QLocation10VisibilityEE(
    QPlaceSearchRequest *self,
    int visibilityScopes) {
  self->setVisibilityScope(
      QFlags<QLocation::Visibility>::fromInt(visibilityScopes));
}

//  RelevanceHint QPlaceSearchRequest::relevanceHint() const
extern "C" Q_DECL_EXPORT
QPlaceSearchRequest::RelevanceHint ritual_ZNK19QPlaceSearchRequest13relevanceHintEv(
    const QPlaceSearchRequest *self) {
  return self->relevanceHint();
}

//  void QPlaceSearchRequest::setRelevanceHint(RelevanceHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest16setRelevanceHintENS_13RelevanceHintE(
    QPlaceSearchRequest *self,
    QPlaceSearchRequest::RelevanceHint hint) {
  self->setRelevanceHint(hint);
}

//  int QPlaceSearchRequest::limit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QPlaceSearchRequest5limitEv(
    const QPlaceSearchRequest *self) {
  return self->limit();
}

//  void QPlaceSearchRequest::setLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest8setLimitEi(
    QPlaceSearchRequest *self,
    int limit) {
  self->setLimit(limit);
}

//  void QPlaceSearchRequest::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceSearchRequest5clearEv(QPlaceSearchRequest *self) {
  self->clear();
}

//  bool QPlaceSearchRequest::isEqual(const QPlaceSearchRequest &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QPlaceSearchRequest7isEqualERKS_(
    const QPlaceSearchRequest *self,
    const QPlaceSearchRequest *other) {
  return self->isEqual(*other);
}

//  QPlaceSearchRequestPrivate *QPlaceSearchRequest::d_func()
extern "C" Q_DECL_EXPORT
QPlaceSearchRequestPrivate *ritual_ZN19QPlaceSearchRequest6d_funcEv(
    QPlaceSearchRequest *self) {
  return self->d_func();
}

//  const QPlaceSearchRequestPrivate *QPlaceSearchRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceSearchRequestPrivate *ritual_ZNK19QPlaceSearchRequest6d_funcEv(
    const QPlaceSearchRequest *self) {
  return self->d_func();
}
