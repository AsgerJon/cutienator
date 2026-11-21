//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtreewidgetitemiterator.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWidgets/qtreewidgetitemiterator.h>

//  QTreeWidgetItemIterator::QTreeWidgetItemIterator(const
//      QTreeWidgetItemIterator &it)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratorC1ERKS_(
    const QTreeWidgetItemIterator *it) {
  return new QTreeWidgetItemIterator(*it);
}

//  QTreeWidgetItemIterator::QTreeWidgetItemIterator(QTreeWidget *widget,
//      IteratorFlags flags)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratorC1EP11QTreeWidget6QFlagsINS_12IteratorFlagEE(
    QTreeWidget *widget,
    int flags) {
  return new QTreeWidgetItemIterator(
      widget,
      QFlags<QTreeWidgetItemIterator::IteratorFlag>::fromInt(flags));
}

//  QTreeWidgetItemIterator::QTreeWidgetItemIterator(QTreeWidgetItem *item,
//      IteratorFlags flags)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratorC1EP15QTreeWidgetItem6QFlagsINS_12IteratorFlagEE(
    QTreeWidgetItem *item,
    int flags) {
  return new QTreeWidgetItemIterator(
      item,
      QFlags<QTreeWidgetItemIterator::IteratorFlag>::fromInt(flags));
}

//  QTreeWidgetItemIterator::~QTreeWidgetItemIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QTreeWidgetItemIteratorD1Ev(QTreeWidgetItemIterator *self) {
  delete self;
}

//  const QTreeWidgetItemIterator QTreeWidgetItemIterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratorppEi(
    QTreeWidgetItemIterator *self,
    int a0) {
  return new QTreeWidgetItemIterator(self->operator++(a0));
}

//  const QTreeWidgetItemIterator QTreeWidgetItemIterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratormmEi(
    QTreeWidgetItemIterator *self,
    int a0) {
  return new QTreeWidgetItemIterator(self->operator--(a0));
}

//  QTreeWidgetItem *QTreeWidgetItemIterator::operator*() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK23QTreeWidgetItemIteratordeEv(
    const QTreeWidgetItemIterator *self) {
  return self->operator*();
}
