//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacematchrequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/qplacematchrequest.h>
#include <QtLocation/qplace.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacematchrequest.h>
#include <QtCore/QSharedData>
#include <QtCore/QList>
#include <QtLocation/QPlace>
#include <QtLocation/QPlaceResult>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacematchrequest.cpp, line 14, as local:qplacematchrequest.cpp:QPlaceMatchRequestPrivate
class QPlaceMatchRequestPrivate : public QSharedData
{
public:
    bool operator==(const QPlaceMatchRequestPrivate &other) const;

    void clear();

    QList<QPlace> places;
    QVariantMap parameters;
};

//  from ../qtlocation/src/location/places/qplacematchrequest.cpp, line 25, as local:qplacematchrequest.cpp:QPlaceMatchRequestPrivate::operator==
inline QT_DEFINE_QSDP_SPECIALIZATION_DTOR(QPlaceMatchRequestPrivate)

bool QPlaceMatchRequestPrivate::operator==(const QPlaceMatchRequestPrivate &other) const
{
    return (places == other.places
            && parameters == other.parameters);
}

//  from ../qtlocation/src/location/places/qplacematchrequest.cpp, line 33, as local:qplacematchrequest.cpp:QPlaceMatchRequestPrivate::clear
inline void QPlaceMatchRequestPrivate::clear()
{
    places.clear();
    parameters.clear();
}

//  from ../qtlocation/src/location/places/qplacematchrequest.cpp, line 183, as _ZN18QPlaceMatchRequest6d_funcEv
inline QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func()
{
    return static_cast<QPlaceMatchRequestPrivate *>(d_ptr.data());
}

//  from ../qtlocation/src/location/places/qplacematchrequest.cpp, line 188, as _ZNK18QPlaceMatchRequest6d_funcEv
inline const QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func() const
{
    return static_cast<const QPlaceMatchRequestPrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QPlaceMatchRequest::QPlaceMatchRequest()
extern "C" Q_DECL_EXPORT
QPlaceMatchRequest *ritual_ZN18QPlaceMatchRequestC1Ev() {
  return new QPlaceMatchRequest();
}

//  QPlaceMatchRequest::QPlaceMatchRequest(const QPlaceMatchRequest &other)
extern "C" Q_DECL_EXPORT
QPlaceMatchRequest *ritual_ZN18QPlaceMatchRequestC1ERKS_(
    const QPlaceMatchRequest *other) {
  return new QPlaceMatchRequest(*other);
}

//  QPlaceMatchRequest::QPlaceMatchRequest(QPlaceMatchRequest &&other)
extern "C" Q_DECL_EXPORT
QPlaceMatchRequest *ritual_ZN18QPlaceMatchRequestC1EOS_(
    QPlaceMatchRequest *other) {
  return new QPlaceMatchRequest(std::move(*other));
}

//  QPlaceMatchRequest::~QPlaceMatchRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequestD1Ev(QPlaceMatchRequest *self) {
  delete self;
}

//  QPlaceMatchRequest &QPlaceMatchRequest::operator=(const
//      QPlaceMatchRequest &other)
extern "C" Q_DECL_EXPORT
QPlaceMatchRequest *ritual_ZN18QPlaceMatchRequestaSERKS_(
    QPlaceMatchRequest *self,
    const QPlaceMatchRequest *other) {
  return &(self->operator=(*other));
}

//  QPlaceMatchRequest &QPlaceMatchRequest::operator=(QPlaceMatchRequest
//      &&other)
extern "C" Q_DECL_EXPORT
QPlaceMatchRequest *ritual_ZN18QPlaceMatchRequestaSEOS_(
    QPlaceMatchRequest *self,
    QPlaceMatchRequest *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QPlaceMatchRequest::swap(QPlaceMatchRequest &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest4swapERS_(
    QPlaceMatchRequest *self,
    QPlaceMatchRequest *other) {
  self->swap(*other);
}

//  bool operator==(const QPlaceMatchRequest &lhs, const QPlaceMatchRequest
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QPlaceMatchRequestS1_(
    const QPlaceMatchRequest *lhs,
    const QPlaceMatchRequest *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceMatchRequest &lhs, const QPlaceMatchRequest
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QPlaceMatchRequestS1_(
    const QPlaceMatchRequest *lhs,
    const QPlaceMatchRequest *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QPlace> QPlaceMatchRequest::places() const
extern "C" Q_DECL_EXPORT
QList<QPlace> *ritual_ZNK18QPlaceMatchRequest6placesEv(
    const QPlaceMatchRequest *self) {
  return new QList<QPlace>(self->places());
}

//  void QPlaceMatchRequest::setPlaces(const QList<QPlace> &places)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest9setPlacesERK5QListI6QPlaceE(
    QPlaceMatchRequest *self,
    const QList<QPlace> *places) {
  self->setPlaces(*places);
}

//  void QPlaceMatchRequest::setResults(const QList<QPlaceSearchResult>
//      &results)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest10setResultsERK5QListI18QPlaceSearchResultE(
    QPlaceMatchRequest *self,
    const QList<QPlaceSearchResult> *results) {
  self->setResults(*results);
}

//  QVariantMap QPlaceMatchRequest::parameters() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK18QPlaceMatchRequest10parametersEv(
    const QPlaceMatchRequest *self) {
  return new QMap<QString, QVariant>(self->parameters());
}

//  void QPlaceMatchRequest::setParameters(const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest13setParametersERK4QMapI7QString8QVariantE(
    QPlaceMatchRequest *self,
    const QMap<QString, QVariant> *parameters) {
  self->setParameters(*parameters);
}

//  void QPlaceMatchRequest::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceMatchRequest5clearEv(QPlaceMatchRequest *self) {
  self->clear();
}

//  bool QPlaceMatchRequest::isEqual(const QPlaceMatchRequest &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QPlaceMatchRequest7isEqualERKS_(
    const QPlaceMatchRequest *self,
    const QPlaceMatchRequest *other) {
  return self->isEqual(*other);
}

//  QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func()
extern "C" Q_DECL_EXPORT
QPlaceMatchRequestPrivate *ritual_ZN18QPlaceMatchRequest6d_funcEv(
    QPlaceMatchRequest *self) {
  return self->d_func();
}

//  const QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceMatchRequestPrivate *ritual_ZNK18QPlaceMatchRequest6d_funcEv(
    const QPlaceMatchRequest *self) {
  return self->d_func();
}
