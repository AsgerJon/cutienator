//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qspi_struct_marshallers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if __has_include(<QtGui/6.12.0/QtGui/private/qspi_struct_marshallers_p.h>)
#if QT_CONFIG(accessibility)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qspi_struct_marshallers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QSpiAccessibleCacheItem::~QSpiAccessibleCacheItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSpiAccessibleCacheItemD1Ev(QSpiAccessibleCacheItem *self) {
  delete self;
}

//  QList<QSpiAccessibleCacheItem>::QList()
extern "C" Q_DECL_EXPORT
QList<QSpiAccessibleCacheItem> *ritual_list_make_QSpiAccessibleCacheItem() {
  return new QList<QSpiAccessibleCacheItem>();
}

//  void QList<QSpiAccessibleCacheItem>::append(const QSpiAccessibleCacheItem
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSpiAccessibleCacheItem(
    QList<QSpiAccessibleCacheItem> *self,
    const QSpiAccessibleCacheItem *element) {
  self->append(*element);
}

//  qsizetype QList<QSpiAccessibleCacheItem>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSpiAccessibleCacheItem(
    const QList<QSpiAccessibleCacheItem> *self) {
  return self->size();
}

//  const QSpiAccessibleCacheItem
//      &QList<QSpiAccessibleCacheItem>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSpiAccessibleCacheItem *ritual_list_at_QSpiAccessibleCacheItem(
    const QList<QSpiAccessibleCacheItem> *self,
    long long index) {
  return new QSpiAccessibleCacheItem(self->at(index));
}

//  QList<QSpiAccessibleCacheItem>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSpiAccessibleCacheItem(
    QList<QSpiAccessibleCacheItem> *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
#endif  // __has_include(<QtGui/6.12.0/QtGui/private/qspi_struct_marshallers_p.h>)
