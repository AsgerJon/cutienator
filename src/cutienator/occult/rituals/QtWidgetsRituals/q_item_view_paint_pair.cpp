//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QItemViewPaintPair::~QItemViewPaintPair()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QItemViewPaintPairD1Ev(QItemViewPaintPair *self) {
  delete self;
}

//  QList<QItemViewPaintPair>::QList()
extern "C" Q_DECL_EXPORT
QList<QItemViewPaintPair> *ritual_list_make_QItemViewPaintPair() {
  return new QList<QItemViewPaintPair>();
}

//  void QList<QItemViewPaintPair>::append(const QItemViewPaintPair &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QItemViewPaintPair(
    QList<QItemViewPaintPair> *self,
    const QItemViewPaintPair *element) {
  self->append(*element);
}

//  qsizetype QList<QItemViewPaintPair>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QItemViewPaintPair(
    const QList<QItemViewPaintPair> *self) {
  return self->size();
}

//  const QItemViewPaintPair &QList<QItemViewPaintPair>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QItemViewPaintPair *ritual_list_at_QItemViewPaintPair(
    const QList<QItemViewPaintPair> *self,
    long long index) {
  return new QItemViewPaintPair(self->at(index));
}

//  QList<QItemViewPaintPair>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QItemViewPaintPair(QList<QItemViewPaintPair> *self) {
  delete self;
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
