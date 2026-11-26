//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtreewidgetitemiterator.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(treewidget)
#if QT_CONFIG(treewidget)
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

//  QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator=(const
//      QTreeWidgetItemIterator &it)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratoraSERKS_(
    QTreeWidgetItemIterator *self,
    const QTreeWidgetItemIterator *it) {
  return &(self->operator=(*it));
}

//  QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator++()
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratorppEv(
    QTreeWidgetItemIterator *self) {
  return &(self->operator++());
}

//  const QTreeWidgetItemIterator QTreeWidgetItemIterator::operator++(int a0)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratorppEi(
    QTreeWidgetItemIterator *self,
    int a0) {
  return new QTreeWidgetItemIterator(self->operator++(a0));
}

//  QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator+=(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QTreeWidgetItemIteratorpLEi(
    QTreeWidgetItemIterator *self,
    int n) {
  self->operator+=(n);
}

//  QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator--()
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratormmEv(
    QTreeWidgetItemIterator *self) {
  return &(self->operator--());
}

//  const QTreeWidgetItemIterator QTreeWidgetItemIterator::operator--(int a0)
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIterator *ritual_ZN23QTreeWidgetItemIteratormmEi(
    QTreeWidgetItemIterator *self,
    int a0) {
  return new QTreeWidgetItemIterator(self->operator--(a0));
}

//  QTreeWidgetItemIterator &QTreeWidgetItemIterator::operator-=(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QTreeWidgetItemIteratormIEi(
    QTreeWidgetItemIterator *self,
    int n) {
  self->operator-=(n);
}

//  QTreeWidgetItem *QTreeWidgetItemIterator::operator*() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK23QTreeWidgetItemIteratordeEv(
    const QTreeWidgetItemIterator *self) {
  return self->operator*();
}

//  bool QTreeWidgetItemIterator::matchesFlags(const QTreeWidgetItem *item)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QTreeWidgetItemIterator12matchesFlagsEPK15QTreeWidgetItem(
    const QTreeWidgetItemIterator *self,
    const QTreeWidgetItem *item) {
  return self->matchesFlags(item);
}

//  QTreeWidgetItemIteratorPrivate *QTreeWidgetItemIterator::d_func()
extern "C" Q_DECL_EXPORT
QTreeWidgetItemIteratorPrivate *ritual_ZN23QTreeWidgetItemIterator6d_funcEv(
    QTreeWidgetItemIterator *self) {
  return self->d_func();
}

//  const QTreeWidgetItemIteratorPrivate *QTreeWidgetItemIterator::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QTreeWidgetItemIteratorPrivate *ritual_ZNK23QTreeWidgetItemIterator6d_funcEv(
    const QTreeWidgetItemIterator *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(treewidget)
