//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacesearchresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplaceicon.h>
#include <QtCore/qlist.h>
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

//  from ../qtlocation/src/location/places/qplacesearchresult.cpp, line 22, as _ZNK18QPlaceSearchResult6d_funcEv
inline const QPlaceSearchResultPrivate *QPlaceSearchResult::d_func() const
{
    return static_cast<const QPlaceSearchResultPrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QPlaceSearchResult::QPlaceSearchResult()
extern "C" Q_DECL_EXPORT
QPlaceSearchResult *ritual_ZN18QPlaceSearchResultC1Ev() {
  return new QPlaceSearchResult();
}

//  QPlaceSearchResult::QPlaceSearchResult(const QPlaceSearchResult &other)
extern "C" Q_DECL_EXPORT
QPlaceSearchResult *ritual_ZN18QPlaceSearchResultC1ERKS_(
    const QPlaceSearchResult *other) {
  return new QPlaceSearchResult(*other);
}

//  QPlaceSearchResult::~QPlaceSearchResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceSearchResultD1Ev(QPlaceSearchResult *self) {
  delete self;
}

//  bool QPlaceSearchResult::operator==(const QPlaceSearchResult &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QPlaceSearchResulteqERKS_(
    const QPlaceSearchResult *self,
    const QPlaceSearchResult *other) {
  return self->operator==(*other);
}

//  bool QPlaceSearchResult::operator!=(const QPlaceSearchResult &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QPlaceSearchResultneERKS_(
    const QPlaceSearchResult *self,
    const QPlaceSearchResult *other) {
  return self->operator!=(*other);
}

//  SearchResultType QPlaceSearchResult::type() const
extern "C" Q_DECL_EXPORT
QPlaceSearchResult::SearchResultType ritual_ZNK18QPlaceSearchResult4typeEv(
    const QPlaceSearchResult *self) {
  return self->type();
}

//  QString QPlaceSearchResult::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QPlaceSearchResult5titleEv(
    const QPlaceSearchResult *self) {
  return new QString(self->title());
}

//  void QPlaceSearchResult::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceSearchResult8setTitleERK7QString(
    QPlaceSearchResult *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QPlaceIcon QPlaceSearchResult::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZNK18QPlaceSearchResult4iconEv(
    const QPlaceSearchResult *self) {
  return new QPlaceIcon(self->icon());
}

//  void QPlaceSearchResult::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlaceSearchResult7setIconERK10QPlaceIcon(
    QPlaceSearchResult *self,
    const QPlaceIcon *icon) {
  self->setIcon(*icon);
}

//  QPlaceSearchResult::QPlaceSearchResult(QPlaceSearchResultPrivate *d)
extern "C" Q_DECL_EXPORT
QPlaceSearchResult *ritual_ZN18QPlaceSearchResultC1EP25QPlaceSearchResultPrivate(
    QPlaceSearchResultPrivate *d) {
  return new QPlaceSearchResult(d);
}

//  const QPlaceSearchResultPrivate *QPlaceSearchResult::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceSearchResultPrivate *ritual_ZNK18QPlaceSearchResult6d_funcEv(
    const QPlaceSearchResult *self) {
  return self->d_func();
}

//  QList<QPlaceSearchResult>::QList()
extern "C" Q_DECL_EXPORT
QList<QPlaceSearchResult> *ritual_list_make_QPlaceSearchResult() {
  return new QList<QPlaceSearchResult>();
}

//  void QList<QPlaceSearchResult>::append(const QPlaceSearchResult &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPlaceSearchResult(
    QList<QPlaceSearchResult> *self,
    const QPlaceSearchResult *element) {
  self->append(*element);
}

//  qsizetype QList<QPlaceSearchResult>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPlaceSearchResult(
    const QList<QPlaceSearchResult> *self) {
  return self->size();
}

//  const QPlaceSearchResult &QList<QPlaceSearchResult>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QPlaceSearchResult *ritual_list_at_QPlaceSearchResult(
    const QList<QPlaceSearchResult> *self,
    long long index) {
  return new QPlaceSearchResult(self->at(index));
}

//  QList<QPlaceSearchResult>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPlaceSearchResult(QList<QPlaceSearchResult> *self) {
  delete self;
}
