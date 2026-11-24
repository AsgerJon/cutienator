//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplace.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/qplace.h>
#include <QtLocation/qplacecategory.h>
#include <QtPositioning/qgeolocation.h>
#include <QtLocation/qplaceratings.h>
#include <QtLocation/qplacesupplier.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplaceicon.h>
#include <QtLocation/qplacecontent.h>
#include <QtCore/qurl.h>
#include <QtLocation/qplaceattribute.h>
#include <QtLocation/qplacecontactdetail.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplace.h"
#include "qplace_p.h"
#include <QtPositioning/QGeoLocation>
#ifdef QPLACE_DEBUG
#include <QDebug>
#endif
#include <QStringList>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplace.cpp, line 137, as _ZNK6QPlace6d_funcEv
inline const QPlacePrivate *QPlace::d_func() const
{
    return static_cast<const QPlacePrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QPlace::QPlace()
extern "C" Q_DECL_EXPORT
QPlace *ritual_ZN6QPlaceC1Ev() {
  return new QPlace();
}

//  QPlace::QPlace(const QPlace &other)
extern "C" Q_DECL_EXPORT
QPlace *ritual_ZN6QPlaceC1ERKS_(const QPlace *other) {
  return new QPlace(*other);
}

//  QPlace::~QPlace()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlaceD1Ev(QPlace *self) {
  delete self;
}

//  bool operator==(const QPlace &lhs, const QPlace &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QPlaceS1_(const QPlace *lhs, const QPlace *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlace &lhs, const QPlace &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QPlaceS1_(const QPlace *lhs, const QPlace *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QPlaceCategory> QPlace::categories() const
extern "C" Q_DECL_EXPORT
QList<QPlaceCategory> *ritual_ZNK6QPlace10categoriesEv(const QPlace *self) {
  return new QList<QPlaceCategory>(self->categories());
}

//  void QPlace::setCategory(const QPlaceCategory &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace11setCategoryERK14QPlaceCategory(
    QPlace *self,
    const QPlaceCategory *category) {
  self->setCategory(*category);
}

//  void QPlace::setCategories(const QList<QPlaceCategory> &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace13setCategoriesERK5QListI14QPlaceCategoryE(
    QPlace *self,
    const QList<QPlaceCategory> *categories) {
  self->setCategories(*categories);
}

//  QGeoLocation QPlace::location() const
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZNK6QPlace8locationEv(const QPlace *self) {
  return new QGeoLocation(self->location());
}

//  void QPlace::setLocation(const QGeoLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace11setLocationERK12QGeoLocation(
    QPlace *self,
    const QGeoLocation *location) {
  self->setLocation(*location);
}

//  QPlaceRatings QPlace::ratings() const
extern "C" Q_DECL_EXPORT
QPlaceRatings *ritual_ZNK6QPlace7ratingsEv(const QPlace *self) {
  return new QPlaceRatings(self->ratings());
}

//  void QPlace::setRatings(const QPlaceRatings &ratings)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace10setRatingsERK13QPlaceRatings(
    QPlace *self,
    const QPlaceRatings *ratings) {
  self->setRatings(*ratings);
}

//  QPlaceSupplier QPlace::supplier() const
extern "C" Q_DECL_EXPORT
QPlaceSupplier *ritual_ZNK6QPlace8supplierEv(const QPlace *self) {
  return new QPlaceSupplier(self->supplier());
}

//  void QPlace::setSupplier(const QPlaceSupplier &supplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace11setSupplierERK14QPlaceSupplier(
    QPlace *self,
    const QPlaceSupplier *supplier) {
  self->setSupplier(*supplier);
}

//  QString QPlace::attribution() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QPlace11attributionEv(const QPlace *self) {
  return new QString(self->attribution());
}

//  void QPlace::setAttribution(const QString &attribution)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace14setAttributionERK7QString(
    QPlace *self,
    const QString *attribution) {
  self->setAttribution(*attribution);
}

//  QPlaceIcon QPlace::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZNK6QPlace4iconEv(const QPlace *self) {
  return new QPlaceIcon(self->icon());
}

//  void QPlace::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace7setIconERK10QPlaceIcon(
    QPlace *self,
    const QPlaceIcon *icon) {
  self->setIcon(*icon);
}

//  QPlaceContent::Collection QPlace::content(QPlaceContent::Type type) const
extern "C" Q_DECL_EXPORT
QMap<int, QPlaceContent> *ritual_ZNK6QPlace7contentEN13QPlaceContent4TypeE(
    const QPlace *self,
    QPlaceContent::Type type) {
  return new QMap<int, QPlaceContent>(self->content(type));
}

//  void QPlace::setContent(QPlaceContent::Type type, const
//      QPlaceContent::Collection &content)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace10setContentEN13QPlaceContent4TypeERK4QMapIiS0_E(
    QPlace *self,
    QPlaceContent::Type type,
    const QMap<int, QPlaceContent> *content) {
  self->setContent(type, *content);
}

//  void QPlace::insertContent(QPlaceContent::Type type, const
//      QPlaceContent::Collection &content)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace13insertContentEN13QPlaceContent4TypeERK4QMapIiS0_E(
    QPlace *self,
    QPlaceContent::Type type,
    const QMap<int, QPlaceContent> *content) {
  self->insertContent(type, *content);
}

//  int QPlace::totalContentCount(QPlaceContent::Type type) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QPlace17totalContentCountEN13QPlaceContent4TypeE(
    const QPlace *self,
    QPlaceContent::Type type) {
  return self->totalContentCount(type);
}

//  void QPlace::setTotalContentCount(QPlaceContent::Type type, int total)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace20setTotalContentCountEN13QPlaceContent4TypeEi(
    QPlace *self,
    QPlaceContent::Type type,
    int total) {
  self->setTotalContentCount(type, total);
}

//  QString QPlace::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QPlace4nameEv(const QPlace *self) {
  return new QString(self->name());
}

//  void QPlace::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace7setNameERK7QString(QPlace *self, const QString *name) {
  self->setName(*name);
}

//  QString QPlace::placeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QPlace7placeIdEv(const QPlace *self) {
  return new QString(self->placeId());
}

//  void QPlace::setPlaceId(const QString &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace10setPlaceIdERK7QString(
    QPlace *self,
    const QString *identifier) {
  self->setPlaceId(*identifier);
}

//  QString QPlace::primaryPhone() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QPlace12primaryPhoneEv(const QPlace *self) {
  return new QString(self->primaryPhone());
}

//  QString QPlace::primaryFax() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QPlace10primaryFaxEv(const QPlace *self) {
  return new QString(self->primaryFax());
}

//  QString QPlace::primaryEmail() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QPlace12primaryEmailEv(const QPlace *self) {
  return new QString(self->primaryEmail());
}

//  QUrl QPlace::primaryWebsite() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK6QPlace14primaryWebsiteEv(const QPlace *self) {
  return new QUrl(self->primaryWebsite());
}

//  bool QPlace::detailsFetched() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QPlace14detailsFetchedEv(const QPlace *self) {
  return self->detailsFetched();
}

//  void QPlace::setDetailsFetched(bool fetched)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace17setDetailsFetchedEb(QPlace *self, bool fetched) {
  self->setDetailsFetched(fetched);
}

//  QStringList QPlace::extendedAttributeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK6QPlace22extendedAttributeTypesEv(
    const QPlace *self) {
  return new QList<QString>(self->extendedAttributeTypes());
}

//  QPlaceAttribute QPlace::extendedAttribute(const QString &attributeType)
//      const
extern "C" Q_DECL_EXPORT
QPlaceAttribute *ritual_ZNK6QPlace17extendedAttributeERK7QString(
    const QPlace *self,
    const QString *attributeType) {
  return new QPlaceAttribute(self->extendedAttribute(*attributeType));
}

//  void QPlace::setExtendedAttribute(const QString &attributeType, const
//      QPlaceAttribute &attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace20setExtendedAttributeERK7QStringRK15QPlaceAttribute(
    QPlace *self,
    const QString *attributeType,
    const QPlaceAttribute *attribute) {
  self->setExtendedAttribute(*attributeType, *attribute);
}

//  void QPlace::removeExtendedAttribute(const QString &attributeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace23removeExtendedAttributeERK7QString(
    QPlace *self,
    const QString *attributeType) {
  self->removeExtendedAttribute(*attributeType);
}

//  QStringList QPlace::contactTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK6QPlace12contactTypesEv(const QPlace *self) {
  return new QList<QString>(self->contactTypes());
}

//  QList<QPlaceContactDetail> QPlace::contactDetails(const QString
//      &contactType) const
extern "C" Q_DECL_EXPORT
QList<QPlaceContactDetail> *ritual_ZNK6QPlace14contactDetailsERK7QString(
    const QPlace *self,
    const QString *contactType) {
  return new QList<QPlaceContactDetail>(self->contactDetails(*contactType));
}

//  void QPlace::setContactDetails(const QString &contactType,
//      QList<QPlaceContactDetail> details)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace17setContactDetailsERK7QString5QListI19QPlaceContactDetailE(
    QPlace *self,
    const QString *contactType,
    const QList<QPlaceContactDetail> *details) {
  self->setContactDetails(*contactType, *details);
}

//  void QPlace::appendContactDetail(const QString &contactType, const
//      QPlaceContactDetail &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace19appendContactDetailERK7QStringRK19QPlaceContactDetail(
    QPlace *self,
    const QString *contactType,
    const QPlaceContactDetail *detail) {
  self->appendContactDetail(*contactType, *detail);
}

//  void QPlace::removeContactDetails(const QString &contactType)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace20removeContactDetailsERK7QString(
    QPlace *self,
    const QString *contactType) {
  self->removeContactDetails(*contactType);
}

//  QLocation::Visibility QPlace::visibility() const
extern "C" Q_DECL_EXPORT
QLocation::Visibility ritual_ZNK6QPlace10visibilityEv(const QPlace *self) {
  return self->visibility();
}

//  void QPlace::setVisibility(QLocation::Visibility visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPlace13setVisibilityEN9QLocation10VisibilityE(
    QPlace *self,
    QLocation::Visibility visibility) {
  self->setVisibility(visibility);
}

//  bool QPlace::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QPlace7isEmptyEv(const QPlace *self) {
  return self->isEmpty();
}

//  bool QPlace::isEqual(const QPlace &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QPlace7isEqualERKS_(
    const QPlace *self,
    const QPlace *other) {
  return self->isEqual(*other);
}

//  const QPlacePrivate *QPlace::d_func() const
extern "C" Q_DECL_EXPORT
const QPlacePrivate *ritual_ZNK6QPlace6d_funcEv(const QPlace *self) {
  return self->d_func();
}

//  QList<QPlace>::QList()
extern "C" Q_DECL_EXPORT
QList<QPlace> *ritual_list_make_QPlace() {
  return new QList<QPlace>();
}

//  void QList<QPlace>::append(const QPlace &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPlace(QList<QPlace> *self, const QPlace *element) {
  self->append(*element);
}

//  qsizetype QList<QPlace>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPlace(const QList<QPlace> *self) {
  return self->size();
}

//  const QPlace &QList<QPlace>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPlace *ritual_list_at_QPlace(const QList<QPlace> *self, long long index) {
  return new QPlace(self->at(index));
}

//  QList<QPlace>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPlace(QList<QPlace> *self) {
  delete self;
}
